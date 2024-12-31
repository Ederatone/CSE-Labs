import time

def long_running_task(cancel_event):
    for i in range(10):
        if cancel_event.is_set():
            print(f"Task has been cancelled.")
            return
        print(f"Task: Working... ({i+1}/10)")
        time.sleep(1)
    print(f"Task completed successfully.")
