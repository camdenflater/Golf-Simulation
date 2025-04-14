import random

# Assign names of ten golfers
golfer_names = [
    "Bob", "Jim", "Leo", "Ray", "Sam",
    "Ava", "Ivy", "Mia", "Kim", "Eve"
]

# Create 18 holes and randomize par
all_holes = [random.randint(3, 5) for _ in range(18)]

# Create random course yardage layout based on hole par
def get_yardage(par):
    if par == 3:
        return random.randint(150, 200)
    elif par == 4:
        return random.randint(385, 450)
    elif par == 5:
        return random.randint(450, 495)

course_yardages = {f"{i + 1}": (par, get_yardage(par)) for i, par in enumerate(all_holes)}

def simulate_hole(stroke, par, yards, distance):

    # Based on what stroke you are on, randomize yardage and club based on how close you are until the hole
    random_yardages = {
        1: (random.randint(80, 150) if par == 3 else random.randint(200, 265)),
        2: (random.randint(20, 30) if par == 3 else random.randint(100, 120)),
        3: (random.randint(10, 30) if par == 3 else random.randint(35, 100)),
        4: random.randint(35, 50),
        5: random.randint(20, 25),
        6: random.randint(15, 20),
        7: random.randint(10, 15),
        8: random.randint(3, 7)
    }

    club = {
        1: (random.choice(['6 Iron', '7 Iron', '8 Iron', '9 Iron']) if par == 3 else random.choice(['Driver', '3 Wood'])),
        2: (random.choice(['52 Degree Wedge', '54 Degree Wedge']) if par == 3 else random.choice(['6 Iron', '7 Iron', '8 Iron', '9 Iron'])),
        3: (random.choice(['Putter']) if par == 3 else random.choice(['52 Degree Wedge', '54 Degree Wedge', '56 Degree Wedge'])),
        4: (random.choice(['Putter']) if par == 3 else random.choice(['52 Degree Wedge', '54 Degree Wedge'])),
        5: (random.choice(['Putter']) if par == 3 else random.choice(['54 Degree Wedge', '56 Degree Wedge'])),
        6: random.choice(['Putter']),
        7: random.choice(['Putter']),
        8: random.choice(['Putter'])
    }

    return (yards + random_yardages.get(stroke, 0), club.get(stroke, 0))
