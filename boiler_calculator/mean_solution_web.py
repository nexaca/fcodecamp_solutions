import numpy as np

def calculate(list):
    if len(list) < 9:
      raise ValueError('List must contain nine numbers.')

    a = np.array(list)
    a = a.astype(np.int32)
    b = a.reshape(3,3)

    calculations = {
        'mean': [np.mean(b, axis=0).tolist(), np.mean(b, axis=1).tolist(), np.mean(b.flatten()).tolist()],
        'variance': [np.var(b, axis=0).tolist(), np.var(b, axis=1).tolist(), np.var(b.flatten()).tolist()],
        'standard deviation': [np.std(b, axis=0).tolist(), np.std(b, axis=1).tolist(), np.std(b.flatten()).tolist()],
        'max': [np.max(b, axis=0).tolist(), np.max(b, axis=1).tolist(), np.max(b.flatten()).tolist()],
        'min': [np.min(b, axis=0).tolist(), np.min(b, axis=1).tolist(), np.min(b.flatten()).tolist()],
        'sum': [np.sum(b, axis=0).tolist(), np.sum(b, axis=1).tolist(), np.sum(b.flatten()).tolist()]
    }

    return calculations