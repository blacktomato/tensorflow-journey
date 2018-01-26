#!/usr/bin/env python
# coding=utf-8
##############################################################
 # File Name : variable.py
 # Purpose : Introduction of variable
 # Creation Date : 廿十八年一月廿六日 (週五) 十五時廿分九秒
 # Last Modified : 廿十八年一月廿六日 (週五) 十五時52分35秒
 # Created By : SL Chung
##############################################################
import tensorflow as tf

state = tf.Variable(0, name="counter")
print(state)
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init = tf.global_variables_initializer() #must have if define variable

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))

