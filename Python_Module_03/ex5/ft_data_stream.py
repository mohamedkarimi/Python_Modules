import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release", "use"]

    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events[index]
        del events[index]
        yield event


print("=== Game Data Stream Processor ===")

event_generator = gen_event()

for i in range(1000):
    name, action = next(event_generator)
    print("Event", i, ": Player", name, "did action", action)

event_generator = gen_event()
events_list = []

for i in range(10):
    events_list.append(next(event_generator))

print("Built list of 10 events:", events_list)

for event in consume_event(events_list):
    print("Got event from list:", event)
    print("Remains in list:", events_list)
