def get_query(from_time, to_time, substr):
    return "SELECT demographics.benefit_chapter, count(demographics.benefit_chapter) FROM visits LEFT JOIN demographics ON visits.student_id = demographics.student_id WHERE (location = \'" + substr + "\') and check_in_date >= \'" + from_time + "\' AND check_in_date <= \'" + to_time + "\' GROUP BY demographics.benefit_chapter;"
