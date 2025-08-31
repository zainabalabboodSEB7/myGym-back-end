from models.session import SessionModel
from datetime import datetime  

sessions_list = [
    SessionModel(
        name="Morning Yoga",
        description="Start your day with a calming yoga flow.",
        duration_minutes=60,
        capacity=20,
        category_id=1 , # Yoga
        start_time=datetime(2025, 9, 1, 8, 0),
        end_time=datetime(2025, 9, 1, 9, 0)

    ),
    SessionModel(
        name="Pilates Basics",
        description="Beginner-friendly pilates session focusing on core strength.",
        duration_minutes=45,
        capacity=15,
        category_id=2,  # Pilates
        start_time=datetime(2025, 9, 4, 17, 30),
        end_time=datetime(2025, 9, 4, 18, 30)
          
    ),
    SessionModel(
        name="Cardio Blast",
        description="High-intensity cardio workout to get your heart pumping.",
        duration_minutes=30,
        capacity=25,
        category_id=3 , # Cardio
        start_time=datetime(2025, 9, 15, 17, 30),
        end_time=datetime(2025, 9, 15, 18, 30)
    ),
    SessionModel(
        name="Strength 101",
        description="Learn basic strength training techniques.",
        duration_minutes=50,
        capacity=18,
        category_id=4 , # Strength Training
        start_time=datetime(2025, 9, 8, 17, 30),
        end_time=datetime(2025, 9, 8, 18, 30)
    ),
    SessionModel(
        name="Evening HIIT",
        description="Intense interval training to burn fat and build stamina.",
        duration_minutes=40,
        capacity=20,
        category_id=5 , # HIIT
        start_time=datetime(2025, 9, 10, 17, 30),
        end_time=datetime(2025, 9, 10, 18, 30)
    ),
    SessionModel(
        name="Zumba Party",
        description="Dance your way to fitness with fun zumba moves.",
        duration_minutes=55,
        capacity=30,
        category_id=6,  # Zumba
        start_time=datetime(2025, 9, 9, 17, 30),
        end_time=datetime(2025, 9, 9, 18, 30)
    ),
]

