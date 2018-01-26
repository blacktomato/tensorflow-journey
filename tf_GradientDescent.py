#!/usr/bin/env python
# coding=utf-8
##############################################################
 # File Name : tf_1.py
 # Purpose : Use tensorflow to found the linear function 
 # Creation Date : 廿十八年一月廿五日 (週四) 廿一時十五分56秒
 # Last Modified : 廿十八年一月廿五日 (週四) 廿一時32分43秒
 # Created By : SL Chung
##############################################################
import tensorflow as tf
import numpy as np

#create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

### create tensorflow structure start ###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()
### create tensorflow structure end   ###

sess = tf.Session()
sess.run(init) #line27 Very important 

for step in range(201): 
    sess.run(train) #line25
    if step % 20 == 0:
        print("Step: ", step, ", Weights: ", sess.run(Weights),  ", Biases: ", sess.run(biases)) 
