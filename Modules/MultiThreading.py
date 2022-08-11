import time
import threading

def function_0():
    print("Thread 1: Is starting...")
    time.sleep(.4)
    print("Thread 1: Is done!")


def function_1(arg=5):
    print("Thread 2: Is starting...")
    time.sleep(.1)
    for num in range(arg):
        print(f"Thread 2: {num}")
        time.sleep(.1)
    print("Thread 2: Is done!")


def function_2():
    print("Thread 3: Is starting...")
    while True:
        print("Thread 3: Daemon process running...")
        time.sleep(.1)


if __name__ == "__main__":
    # Normal thread without any arguments.
    thread_0 = threading.Thread(target=function_0)
    # Thread with a single argument passed.
    thread_1 = threading.Thread(target=function_1, args=(3,))
    # Deamon thread: This thread will terminate when the program stops.
    thread_2 = threading.Thread(target=function_2, daemon=True)
    # Run the threads.
    thread_0.start()
    thread_1.start()
    thread_2.start()

