import time
import concurrent.futures
import threading

class CancelTask:
    def __init__(self):
        self.cancel_event = threading.Event()
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    def cancel(self):
        self.cancel_event.set()

    def submit(self, task, *args, **kwargs):
        future = self.executor.submit(task, *args, **kwargs)
        return future

def long_running_task(cancel_event):
    for i in range(10):
        if cancel_event.is_set():
            print(f"Task has been cancelled")
            return
        print(f"Task: Working... ({i+1}/10)")
        time.sleep(1)
    print(f"Task completed successfully")

def demo():
    cancel_task = CancelTask()

    future = cancel_task.submit(long_running_task, cancel_event=cancel_task.cancel_event)

    try:
        time.sleep(3)
        print("User decides to cancel the task.")
        cancel_task.cancel()

        future.result()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    demo()
