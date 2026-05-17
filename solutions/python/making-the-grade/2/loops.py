"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    rounded_scores = [
        round(score) for score in student_scores
    ]  # iterates through the list of student scores and rounds each score to the nearest integer using the built-in round() function.  #The resulting rounded scores are stored in a new list called rounded_scores, which is then returned as the output of the function.

    return rounded_scores  # returns the list of rounded student scores, which contains the original scores rounded to the nearest integer value.


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    failed_students = sum(
        scores <= 40 for scores in student_scores
    )  # iterates through the list of student scores and counts how many scores are at or below 40, which is typically considered a failing score. The expression score <= 40 evaluates to True (which is treated as 1) for each failing score and False (which is treated as 0) for each passing score. The sum() function then adds up these values to get the total count of failing students, which is returned as the output of the function.

    return failed_students  # returns the total count of failing students, which is the number of scores at or below 40 in the provided list of student scores.


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    best_scores = [
        score for score in student_scores if score >= threshold
    ]  # iterates through the list of student scores and selects only those scores that are at or above the specified threshold. The resulting list of best scores is stored in a new list called best_scores, which is then returned as the output of the function.

    return best_scores  # returns the list of scores that are at or above the specified threshold, which represents the "best" scores among the provided student scores.


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    lowest_grade = 41

    # logic: total range of scores is from lowest passing grade to highest score, divided into 4 equal intervals for D, C, B, A.
    total_range = highest - lowest_grade + 1  # inclusive

    # calculate the interval of each letter grade
    interval = round(total_range / 4.0)

    # Build from bottom up
    d = lowest_grade

    c = d + interval

    b = c + interval

    a = b + interval

    # Make sure A doesn't exceed highest
    if a > highest:
        a = highest + 1  # for upper bound logic

    lowest_thresholds = [d, c, b, a]  # lower bounds for D, C, B, A

    return lowest_thresholds


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    ranking = [
        f"{rank}. {name}: {score}"
        for rank, (name, score) in enumerate(
            zip(student_names, student_scores), start=1
        )
    ]  # iterates through the list of student names and scores simultaneously using the zip() function, while also keeping track of the rank using the enumerate() function. For each student, it formats a string in the specified format "<rank>. <student name>: <score>" and adds it to a new list called ranking. The resulting list of formatted strings is returned as the output of the function.

    return ranking  # returns the list of formatted strings that represent the students' ranks, names, and scores in descending order based on their exam scores.


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for name, score in student_info:
        if score == 100:
            return [
                name,
                score,
            ]  # iterates through the list of student information, which consists of sublists containing a student's name and score. If it finds a student with a perfect score of 100, it returns a new list containing that student's name and the perfect score. If no student with a perfect score is found after iterating through the entire list, the function returns an empty list.

    return (
        []
    )  # returns an empty list if no student with a perfect score of 100 is found in the provided list of student information.
