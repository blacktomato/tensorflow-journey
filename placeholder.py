#!/usr/bin/env python
# coding=utf-8
##############################################################
 # File Name : placeholder.py
 # Purpose :
 # Creation Date : 廿十八年一月廿六日 (週五) 十五時59分〇秒
 # Last Modified : 廿十八年一月廿六日 (週五) 十六時七分48秒
 # Created By : SL Chung
##############################################################
import tensorflow as tf

input1 = tf.placeholder(tf.float32) #must define dtype
input2 = tf.placeholder(tf.float32) #second parameter can be the shape

output = tf.multiply(input1, input2)

with tf.Session() as sess:
    print(sess.run(output, feed_dict={input1: [6.], input2: [5.]}))

