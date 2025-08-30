from models.session import SessionModel

sessions_list = [
    SessionModel(
        name="Morning Yoga",
        description="Start your day with a calming yoga flow.",
        duration_minutes=60,
        capacity=20,
        category_id=1  # Yoga
    ),
    SessionModel(
        name="Pilates Basics",
        description="Beginner-friendly pilates session focusing on core strength.",
        duration_minutes=45,
        capacity=15,
        category_id=2  # Pilates
    ),
    SessionModel(
        name="Cardio Blast",
        description="High-intensity cardio workout to get your heart pumping.",
        duration_minutes=30,
        capacity=25,
        category_id=3  # Cardio
    ),
    SessionModel(
        name="Strength 101",
        description="Learn basic strength training techniques.",
        duration_minutes=50,
        capacity=18,
        category_id=4  # Strength Training
    ),
    SessionModel(
        name="Evening HIIT",
        description="Intense interval training to burn fat and build stamina.",
        duration_minutes=40,
        capacity=20,
        category_id=5  # HIIT
    ),
    SessionModel(
        name="Zumba Party",
        description="Dance your way to fitness with fun zumba moves.",
        duration_minutes=55,
        capacity=30,
        category_id=6  # Zumba
    ),
]
