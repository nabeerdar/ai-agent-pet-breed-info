from collections import deque

history = deque(maxlen=4)


def add_memory(entry):
    history.append(entry)


def get_memory():
    return list(history)