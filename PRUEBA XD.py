import threading
import matplotlib.pyplot as plt

def plot_on_main_thread():
    if threading.current_thread().isMainThread():
        plt.plot([1, 2, 3], [4, 5, 6])
    else:
        raise Exception("Plotting must be done on the main thread.")