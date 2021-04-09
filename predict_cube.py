from cube import Cube
import cubeConstants
import numpy as np
import os
from collections import deque
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

initialCube = Cube()
# create model
solvedState = initialCube.getVectorStateOfEdgePieces()
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


replay_buffer = deque(maxlen=10000)


def sampleExperiences(batch_size):
    indices = np.random.randint(len(replay_buffer), size=batch_size)
    batch = [replay_buffer[index] for index in indices]
    states, actions, rewards, next_states, dones = [np.array([experience[field_index] for experience in batch])
                                                    for field_index in range(5)]
    return states, actions, rewards, next_states, dones


def playOneStep(cube, state, epsilon):
    action = epsilonGreedyPolicy(state, epsilon)
    cube.turnCube([cubeConstants.turnOptions[action]])

    next_state = cube.getVectorStateOfEdgePieces()
    reward = cube.getNumberOfCrossPiecesSolved() * 10
    done = (cube.getNumberOfCrossPiecesSolved() == 1)
    replay_buffer.append((state, action, reward, next_state, done))

    return next_state, reward, done


# define hyper-parameters
model_batch_size = 128
discount_factor = 0.95
# optimizer and loss function
optimizer = keras.optimizers.Adam(lr=0.001)
loss_fn = keras.losses.mean_squared_error
# print(model.weights)


def training_step(batch_size):
    experiences = sampleExperiences(batch_size)
    states, actions, rewards, next_states, dones = experiences
    next_Q_values = model.predict(next_states)
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
for episode in range(6000):
    initialCube = Cube()
    initialCube.mix()
    obs = initialCube.getVectorStateOfEdgePieces()
    max_reward = initialCube.getNumberOfCrossPiecesSolved() * 10
    if max_reward == 10:
        continue
    for step in range(4):
        currentEpsilon = max(1 - episode / 5000, 0.01)
        obs, currentReward, solved = playOneStep(initialCube, obs, currentEpsilon)
        max_reward = max(max_reward, currentReward)
        if solved:
            print("SOLVED HERE!!!")
            break
    if episode > 50:
        training_step(model_batch_size)
    episode_maxes.append(max_reward)
    if episode % 100 == 99:
        print("episode finished: ", episode)
model.save_weights("corner_weights.h5")
print(episode_maxes[-100:-1])
