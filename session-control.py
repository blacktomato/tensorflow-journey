#!/usr/bin/env python
# coding=utf-8
##############################################################
 # File Name : session-control.py
 # Purpose : session
 # Creation Date : 廿十八年一月廿六日 (週五) 十五時四分33秒
 # Last Modified : 廿十八年一月廿六日 (週五) 十五時十九分45秒
 # Created By : SL Chung
##############################################################
import tensorflow as tf
matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1, matrix2)   #matrix multiply np.dot(m1, m2)

#method 1
sess = tf.Session()
result = sess.run(product)
print("[[3,3]] * [[2],[2]] = ", result)
sess.close()

#method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print("[[3,3]] * [[2],[2]] = ", result2)
