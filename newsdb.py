import psycopg2

DBNAME = "news"


# Connecting to the database and fetching all the answer
def get_answer(query_answer):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query_answer)
    answer = c.fetchall()
    db.close()
    return answer


# Print the answer for question 1 and 2
def print_answer(query_answer):
    print (query_answer[1])
    for index, answer in enumerate(query_answer[0]):
        print (
            "\t", index+1, "-", answer[0],
            "\t <--> ", str(answer[1]), "views")
    print(' ')


# Print the answer for question 3.
def print_error(query_answer):
    print (query_answer[1])
    for answer in query_answer[0]:
        print ("\t", answer[0], "<-->", str(answer[1]) + "% errors")


# What are the most popular three articles of all time?
query_1_answer = ("The 3 most popular three articles of all time are:")
query_1 = """SELECT title, COUNT(log.id) AS views
    FROM articles, log
    WHERE log.path = CONCAT('/article/', articles.slug)
    GROUP BY articles.title ORDER BY views desc LIMIT 3;"""


# Who are the most popular article authors of all time?
query_2_answer = ("The most popular article authors of all time are:")
query_2 = """SELECT authors.name, COUNT(*) AS views
    FROM articles JOIN authors
    ON articles.author = authors.id JOIN log
    ON log.path LIKE CONCAT('%', articles.slug, '%')
    WHERE log.status LIKE '%200%'
    GROUP BY authors.name ORDER BY views DESC"""


# On which days did more than 1% of requests lead to errors?
query_3_answer = ("Days which have more than 1% of requests lead to errors")
query_3 = """SELECT day, percentage
    FROM (SELECT day, round((sum(requests)/(SELECT count(*)
    FROM log WHERE substring(cast(log.time AS text), 0, 11) = day) * 100), 2)
    AS percentage
    FROM (SELECT substring(cast(log.time AS text), 0, 11) AS day,
    count(*) AS requests FROM log WHERE status LIKE '%404%' GROUP BY day)
    AS log_percentage GROUP BY day ORDER BY percentage DESC) AS final_query
    WHERE percentage >= 1"""


if __name__ == '__main__':
    popular_article_result = get_answer(query_1), query_1_answer
    popular_author_result = get_answer(query_2), query_2_answer
    errors_day = get_answer(query_3), query_3_answer

    print_answer(popular_article_result)
    print_answer(popular_author_result)
    print_error(errors_day)
