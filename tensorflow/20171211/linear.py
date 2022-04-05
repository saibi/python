#!/usr/bin/env python3

import tensorflow as tf



#
# H(x) = Wx + b
#

# X and Y data
x_train = [1, 2, 3];
y_train = [1, 2, 3];

W = tf.Variable(tf.random_normal([1]), name='weight') # [1] <- shape , 1Dimension
b = tf.Variable(tf.random_normal([1]), name='bias')

# Our hypothesis WX + b
hypothesis = x_train * W + b




#
# cost(W,b) = 1/m  *  sigma i=1 to m ( H(x(i)) - y(i) )^2
#

# cost/loss function
cost = tf.reduce_mean( tf.square(hypothesis - y_train))

# minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)






# launch the graph in a session

sess = tf.Session()

# initialize global variables in the graph

sess.run(tf.global_variables_initializer())

# fit the line

for step in range(2001):
	sess.run(train)
	if step % 20 == 0 :
		print(step, sess.run(cost), sess.run(W), sess.run(b))

