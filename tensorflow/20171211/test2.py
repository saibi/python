#!/usr/bin/env python3

import tensorflow as tf


#
# H(x) = Wx + b
#
W = tf.Variable(tf.random_normal([1]), name='weight') # [1] <- shape , 1Dimension
b = tf.Variable(tf.random_normal([1]), name='bias')

# X and Y data
X = tf.placeholder(tf.float32, shape=[None])
Y = tf.placeholder(tf.float32, shape=[None])

# Our hypothesis WX + b
hypothesis = X * W + b




#
# cost(W,b) = 1/m  *  sigma i=1 to m ( H(x(i)) - y(i) )^2
#

# cost/loss function
cost = tf.reduce_mean( tf.square(hypothesis - Y))

# minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)






# launch the graph in a session

sess = tf.Session()

# initialize global variables in the graph

sess.run(tf.global_variables_initializer())

# fit the line

for step in range(5001):
	cost_val, W_val, b_val, _ = sess.run( [cost, W, b, train], 
			feed_dict = { X: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
				Y: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] } )
	
	if step % 100 == 0 :
		print(step, cost_val, W_val, b_val)


# testing our model
print( sess.run(hypothesis, feed_dict={X:[5]}))
print( sess.run(hypothesis, feed_dict={X:[6]}))
print( sess.run(hypothesis, feed_dict={X:[2.5]}))
print( sess.run(hypothesis, feed_dict={X:[1.5, 3.5]}))
