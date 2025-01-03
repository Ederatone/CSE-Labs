import asyncio


# manage event subscriptions and emissions
class EventEmitter:
    def __init__(self):
        self.listeners = {}

    def on(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def emit(self, event_name, *args, **kwargs):
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                asyncio.create_task(callback(*args, **kwargs))


# entity that reacts to events
class User:
    def __init__(self, name, event_emitter):
        self.name = name
        self.event_emitter = event_emitter
        self.event_emitter.on("message", self.receive_message)

    async def receive_message(self, sender, message):
        print(f"{self.name} received a message from {sender}: {message}")


# demo function
async def demo():
    emitter = EventEmitter()
    user1 = User("Pablo", emitter)
    user2 = User("Bob", emitter)

    emitter.emit("message", user1.name, "Hello Bob!")
    await asyncio.sleep(2)
    print('\n')

    emitter.emit("message", user2.name, "Hi Pablo!")
    await asyncio.sleep(1)

# run demo
if __name__ == "__main__":
    asyncio.run(demo())
