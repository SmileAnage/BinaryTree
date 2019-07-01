"""
    二叉树
"""
from day03.squeue import *


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def proTraverse(root):
    """
        先序遍历
        先访问树根，在访问左子树，最后访问右子树
    :param root:二叉树
    """
    if root == None:
        return
    print(root.value, end=" ")
    proTraverse(root.left)
    proTraverse(root.right)


def midTraverse(root):
    """
        中序遍历
        先访问左子树，在访问树根，最后访问右子树
    :param root:
    """
    if root == None:
        return
    midTraverse(root.left)
    print(root.value, end=" ")
    midTraverse(root.right)


def afterTraverse(root):
    """
        后序遍历
        先访问左子树，再访问右子树，最后访问树根
    :param root:
    """
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value, end=" ")


def levelTraverse(root):
    """
        层次遍历
        让初始节点先入队，谁出队就遍历谁，并且让它的左右孩子分别入队，直到队列为空
    """
    sq = SQueue()
    sq.enqueue(root)  # 初始节点入队
    while not sq.is_empty():
        root = sq.dequeue()
        # 　打印出队元素
        print(root.value, end=" ")
        if root.left:
            sq.enqueue(root.left)
        if root.right:
            sq.enqueue(root.right)


if __name__ == '__main__':
    root = Node("A", Node("B"), Node("C", Node("D", Node("F"), Node("G")), Node("E", Node("I"), Node("H"))))
    print("先序遍历".center(22, "-"))
    proTraverse(root)
    print()
    print("中序遍历".center(22, "-"))
    midTraverse(root)
    print()
    print("后序遍历".center(22, "-"))
    afterTraverse(root)
    print()
    print("层次遍历".center(22, "-"))
    levelTraverse(root)
