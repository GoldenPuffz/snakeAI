import torch
import random
import numpy as np
from game import SnakeGameAI, Direction, Point
from collections import deque #data structure where they store memory

MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = .001 #learning rate

class Agent:

    def __init__(self):
        pass
