from cube import Cube
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense
from collections import deque

cube = Cube()
# create model
solvedState = cube.getVectorStateOfCornerPieces()
n_inputs = len(solvedState)
model = keras.models.Sequential()
model.add(Dense(100, activation="relu", input_shape=[n_inputs]))
model.add(Dense(100, activation="relu"))
model.add(Dense(100, activation="relu"))
model.add(Dense(10, activation="softmax"))


def epsilonGreedyPolicy(state, epsilon=0):
    if np.random.rand() < epsilon:
        return np.random.randint(10)
    else:
        Q_values = model.predict(state[np.newaxis])
        return np.argmax(Q_values[0])

replay_buffer = deque(maxlen=2000)

def sampleExperiences(batch_size):
    indices = np.random.randint(len(replay_buffer), size=batch_size)
    batch = [replay_buffer[index] for index in indices]
    states, actions, rewards, next_states, dones = [
        np.array([experience[field_index] for experience in batch])
        for field_index in range(5)]
    return states, actions, rewards, next_states, dones

def playOneStep(cube, state, epsilon):
    action = epsilonGreedyPolicy(state, epsilon)
    cube.turnCube(cube.firstLayerAlgorithms[action])
    next_state = cube.getVectorStateOfCornerPieces()
    reward = cube.getNumberOfCornerPiecesSolved()
    done = (cube.getNumberOfCornerPiecesSolved() == 4)
    replay_buffer.append((state, action, reward, next_state, done))
    return next_state, reward, done

# define hyperparameters
batch_size = 32
discount_factor = 0.95
# optimizer and loss function
optimizer = keras.optimizers.Adam(lr=0.001)
loss_fn = keras.losses.mean_squared_error
print(model.weights)

def training_step(batch_size):
    experiences = sampleExperiences(batch_size)
    states, actions, rewards, next_states, dones = experiences
    next_Q_values =  model.predict(next_states)
    max_next_Q_values = np.max(next_Q_values, axis=1)
    target_Q_values = (rewards + (1 - dones) * discount_factor * max_next_Q_values)
    mask = tf.one_hot(actions, 10)
    with tf.GradientTape() as tape:
        all_Q_values = model(states)
        Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
        loss = tf.reduce_mean(loss_fn(target_Q_values, Q_values))
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

episode_maxes = []
for episode in range(1200):
    cube = Cube()
    cube.mix()
    obs = cube.getVectorStateOfCornerPieces()
    max_reward = -100
    for step in range(4):
        epsilon = max(1 - episode / 1000, 0.01)
        obs, reward, done = playOneStep(cube, obs, epsilon)
        max_reward = max(max_reward, reward)
        if done:
            print("SOLVED HERE!!!")
            break
    if episode > 50:
        training_step(batch_size)
    episode_maxes.append(max_reward)
    if episode % 100 == 99:
        print("episode finished: ", episode)
model.save_weights("corner_weights.h5")
print(episode_maxes[-100:-1])
