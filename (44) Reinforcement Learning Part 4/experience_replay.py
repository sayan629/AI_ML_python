from collections import deque
import random

class ReplayMemory():
    
    # Create FIFO queue - experience replay memory
    def __init__(self, maxlen, seed = None):
        self.memory  = deque([], maxlen = maxlen)
        
    def append(self, new_experience):
        self.memory.append(new_experience)
    
    
    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)
        
    # current buffer size
    def __len__(self):
        return len(self.memory)