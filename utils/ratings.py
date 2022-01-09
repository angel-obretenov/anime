def get_len_range_between(range1, range2, ratings):
    return len([a for a in ratings if range1 > a >= range2])


def calculate_ratings(ratings: list):
    max_rate, min_rate = 10, 1
    rating_list = {}

    for i in range(max_rate, min_rate, -1):
        number = get_len_range_between(i, i - 1, ratings)
        if number is not 0:
            rating_list[str(i)] = number

    return rating_list


def get_anime_rating_percentage(rating: float):
    liked = (rating / 10) * 100
    disliked = 100 - liked

    return round(liked, 2), round(disliked, 2)
