from models.review import ReviewModel

reviews_list = [
    ReviewModel(content="Great session, I learned a lot!", rating=5, session_id=1, user_id=1),
    ReviewModel(content="It was okay, could be better.", rating=3, session_id=1, user_id=2),
    ReviewModel(content="Not very helpful, expected more.", rating=2, session_id=2, user_id=1),
    ReviewModel(content="Amazing instructor, highly recommend!", rating=5, session_id=2, user_id=3),
    ReviewModel(content="Good pace and clear explanations.", rating=4, session_id=3, user_id=2),
]