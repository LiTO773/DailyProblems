import re

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
  
def serialize(root):
  depth = depthSerialize(root) // 2 - 1
  return trueSerialize(root, depth)

# Finds how many nested Node exist in the Node object
def depthSerialize(root):
  if (type(root) is Node):
    return 2 + depthSerialize(root.left) + depthSerialize(root.val) + depthSerialize(root.right)
  else:
    return 0

# Creates the String with the depth denoted by |
def trueSerialize(root, depth):
  if (type(root) is Node):
    return serialize(str(trueSerialize(root.left, depth - 1)) + ('|' * depth) + str(trueSerialize(root.val, depth - 1)) + ('|' * depth) + str(trueSerialize(root.right, depth - 1)))
  else:
    return root

def deserialize(node: str):
  biggestDepth = findBiggestDepth(node)
  return toNode(node, biggestDepth)


# Finds how many nested Node exist in the String
def findBiggestDepth(node: str, depth=1):
  return depth - 1 if len(node.split('|' * depth)) == 1 else findBiggestDepth(node, depth + 1)

# Transforms to node
def toNode(node: str, depth):
  if depth != 0:
    split = node.split('|' * depth)
    if len(split) > 1:
      return Node(split[1], toNode(split[0], depth - 1), toNode(split[2], depth - 1))
    else:
      return split[0]

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'