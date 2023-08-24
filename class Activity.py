class Activity:
    def __init__(self, name, enjoyment_factor):
        self.name = name
        self.enjoyment_factor = enjoyment_factor


class Guest:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def greedy_scheduling(activities, guests, total_time):
    schedule = []

    while guests:
        current_guest = guests[0]
        selected_activity = None
        max_enjoyment = float("-inf")
        for activity in activities:
            if activity.enjoyment_factor > max_enjoyment:
                max_enjoyment = activity.enjoyment_factor
                selected_activity = activity

        schedule.append(selected_activity)
        guests.remove(current_guest)

    if calculate_total_time(schedule) > total_time:
        adjust_schedule(schedule, total_time)

    return schedule


def calculate_total_time(schedule):
    total_time = 0
    for activity in schedule:
        total_time += activity.enjoyment_factor
    return total_time


def adjust_schedule(schedule, total_time):
    while calculate_total_time(schedule) > total_time:
        lowest_enjoyment_activity = schedule[0]
        min_enjoyment = float("inf")
        for activity in schedule:
            if activity.enjoyment_factor < min_enjoyment:
                min_enjoyment = activity.enjoyment_factor
                lowest_enjoyment_activity = activity
        schedule.remove(lowest_enjoyment_activity)


def print_schedule(schedule):
    for activity in schedule:
        print(activity.name)


# Example 1
activities1 = [Activity("Dancing", 8), Activity("Trivia", 9), Activity("Karaoke", 7)]
guests1 = [Guest("Guest1", 25), Guest("Guest2", 30), Guest("Guest3", 28)]
total_time1 = 4

# Example 2
activities2 = [Activity("Crafts", 7), Activity("Puzzle", 6), Activity("Magic Show", 9)]
guests2 = [Guest("Guest1", 48), Guest("Guest2", 35), Guest("Guest3", 42)]
total_time2 = 2

# Schedule activities for Example 1
schedule1 = greedy_scheduling(activities1, guests1, total_time1)
print("Example 1 Schedule:")
print_schedule(schedule1)
print()

# Schedule activities for Example 2
schedule2 = greedy_scheduling(activities2, guests2, total_time2)
print("Example 2 Schedule:")
print_schedule(schedule2)
print()
