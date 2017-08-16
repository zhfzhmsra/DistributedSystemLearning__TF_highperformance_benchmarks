import tensorflow as tf

# with tf.variable_scope("foo"):
#     with tf.name_scope("bar"):
#         v = tf.get_variable("v", [1])
#         x = 1.0 + v
# assert v.name == "foo/v:0"
# assert x.op.name == "foo/bar/add"

#
# with tf.variable_scope('zhfzh'), tf.name_scope('fuz') as name_scope:
#     v = tf.get_variable("v", [1])
#     w = tf.get_variable('w', [10])
#     x = 1.0 + v
#
# p1 = tf.trainable_variables()
#
# p2 = tf.trainable_variables()
#
# p2 = None
#
# print (p1 == p2)
# print (p1 is p2)
#
# print ('Finished')

x = []
for i in range(20):
    with tf.variable_scope("outside", reuse=bool(i)), tf.name_scope('tower_%i' % i) as name_scope:
        print (name_scope)
        x.append(tf.get_variable("zhfzh", [1]))

for i in range(20):
    print (x[i].name)



