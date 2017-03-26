#!/bin/python

import tensorflow as tf
from model import train_bottleneck_features

flags = tf.app.flags
FLAGS = flags.FLAGS

flags.DEFINE_integer('batch_size', 32, 'The batch size for the generator')
flags.DEFINE_boolean('save', True, 'Save the generated bottleneck model to S3.')

def main(_):
	print("Using batchsize", FLAGS.batch_size)
	train_bottleneck_features(FLAGS.batch_size, FLAGS.save)

if __name__ == '__main__':
	tf.app.run()