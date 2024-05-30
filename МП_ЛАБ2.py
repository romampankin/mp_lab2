import random
import time
import csv
import datetime
from datetime import datetime
# import matplotlib.pyplot as plt

import timeit

timer = timeit.default_timer

class residents:
  def __init__(self, name, street, house, floor, year):
    self.name = name
    self.street = street
    self.house = house
    self.floor = floor
    self.year = year
  def __gt__(self, other): #>
    return (self.street, self.house, self.floor, self.name, self.year) > (other.street, other.house, other.floor, other.name, other.year)
  def __ge__(self, other): #>=
    return (self.street, self.house, self.floor, self.name, self.year) >= (other.street, other.house, other.floor, other.name, other.year)
  def __lt__(self, other): #<
    return (self.street, self.house, self.floor, self.name, self.year) < (other.street, other.house, other.floor, other.name, other.year)
  def __le__(self, other): #<=
    return (self.street, self.house, self.floor, self.name, self.year) <= (other.street, other.house, other.floor, other.name, other.year)
  def __eq__(self, other): #==
    return (self.street, self.house, self.floor, self.name, self.year) == (other.street, other.house, other.floor, other.name, other.year)
  def get_info(self):
        print(f"{self.name}, {self.street}, {self.house}, {self.floor}, {self.year}", end="")
        print()

class TreeNode:
    def __init__(self, value=None, content=None):
        self.left = None
        self.right = None
        self.value = value
        self.content = content

    def insert(self, value, content=None):
        if self.value is None:
            self.value = value
            self.content = content
        elif value < self.value:
            if self.left is None:
                self.left = TreeNode(value, content)
            else:
                self.left.insert(value, content)
        else:
            if self.right is None:
                self.right = TreeNode(value, content)
            else:
                self.right.insert(value, content)

    def traversal(self): 
        if self.left:
            self.left.traversal()
        print(self.value, self.content)
        if self.right:
            self.right.traversal()

    def find(self, value):
        if value < self.value:
            if self.left is None:
                raise Exception('error, node content is None')
                # return None
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                raise Exception('error, node content is None')
                # return None
            else:
                return self.right.find(value)
        else:
            return self.content


class RBNode:
    def __init__(self, val, content=None):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None
        self.content = content


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val, content=None):
        # Ordinary Binary Search Insertion
        new_node = RBNode(val, content)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True  # new node must be red
        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # Set the parent and insert the new node
        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Fix the tree
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right  # uncle
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent

                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)

        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        if curr.content is None:
            raise Exception('error, node content is None')
        else:
            return curr.content

    # rotate left at node x
    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # rotate right at node x
    def rotate_right(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y

        elif x == x.parent.right:
            x.parent.right = y

        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __repr__(self):
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)


def print_tree(node, lines, level=0):
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        print(node.val, node.content)
        print_tree(node.right, lines, level + 1)


def get_nums(num):
    random.seed(1)
    nums = []
    for _ in range(num):
        nums.append(random.randint(1, num - 1))
    return nums


class HashTable:
    __collisions = 0

    def __init__(self, n=100):
        self.MAX = n
        self.arr = [[] for i in range(self.MAX)]

    def __get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        hsh = self.__get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[hsh]):
            if len(element) == 2 and element[0] == key:
                self.arr[hsh][idx] = (key, value)
                found = True
                break
        if not found and len(self.arr[hsh]) > 0:
            self.arr[hsh].append((key, value))
            self.__collisions += 1
        elif not found:
            self.arr[hsh].append((key, value))

    def __getitem__(self, key):
        hsh = self.__get_hash(key)
        for element in self.arr[hsh]:
            if element[0] == key:
                return element[1]

        raise Exception(f"No {key} key in HashTable")

    def __delitem__(self, key):
        hsh = self.__get_hash(key)
        for idx, element in enumerate(self.arr[hsh]):
            if element[0] == key:
                del self.arr[hsh][idx]

    def get_collisions_number(self):
        return self.__collisions

    def pr(self):
        for i in self.arr:
            print(i)



bin_tree_time, rb_tree_time, hash_table_time, collision_number, dictionary_time = {}, {}, {}, {}, {}

target = 'Петровская Полина Максимовна'

cnt = 0

for i in range(1, 7):

    with open(f'жильцы_{i}.csv') as file:

        next(file)

        #создание структур хранения
        binary_tree1 = TreeNode()
        red_black_tree1 = RBTree()
        hash_table1 = HashTable(100)
        def_dict = {}

        #заполнение данными
        for row in file:
            r = row.split(',')[:5]
            # print(r)
            w = residents(r[0], r[1], int(r[2]), int(r[3]), int(r[4]))

            binary_tree1.insert(value=r[0], content=w)
            red_black_tree1.insert(val=r[0], content=w)
            hash_table1[r[0]] = w
            def_dict[r[0]] = w



        #поиск элементов и подсчет времени


        start_time1 = timer()
        # print("Бинарное дерево")
        binary_tree1.find(target).get_info()  # поиск в бинарном дереве
        end_time1 = timer()
        time1 = end_time1 - start_time1
        bin_tree_time[i] = time1


        start_time2 = timer()
        # print("Красно-черное дерево")
        red_black_tree1.exists(target).get_info()  # поиск в красно-черном дереве
        end_time2 = timer()
        time2 = end_time2 - start_time2
        rb_tree_time[i] = time2


        start_time3 = timer()
        # print("Хэш-таблица")
        hash_table1[target].get_info()  # поиск в хэш таблице.
        end_time3 = timer()
        time3 = end_time3 - start_time3
        hash_table_time[i] = time3


        start_time4 = timer()
        # print("Ассоциативный массиве")
        def_dict[target].get_info()  # поиск в ассоциативном массиве
        end_time4 = timer()
        time4 = end_time4 - start_time4
        dictionary_time[i] = time4

        collision_number[i] = hash_table1.get_collisions_number()  # вывод количества коллизий



print(f'\nbin_tree_time: {bin_tree_time}', f'rb_tree_time: {rb_tree_time}', f'hash_table_time: {hash_table_time}', f'dictionary_time: {dictionary_time}', f'collision_number{collision_number}', sep='\n')
