def finding_success_grade(average_score):
    if average_score >= 90 and average_score < 100:
        success_grade = 'AA'
    elif average_score >= 85 and average_score < 89:
        success_grade = 'BA'
    elif average_score >= 80 and average_score < 84:
        success_grade = 'BB'
    elif average_score >= 75 and average_score < 79:
        success_grade = 'CB'
    elif average_score >= 70 and average_score < 74:
        success_grade = 'CC'
    elif average_score >= 65 and average_score < 69:
        success_grade = 'DC'
    elif average_score >= 60 and average_score < 64:
        success_grade = 'DD'
    elif average_score >= 50 and average_score < 59:
        success_grade = 'FD'
    else:
        success_grade = 'FF'

    return success_grade
