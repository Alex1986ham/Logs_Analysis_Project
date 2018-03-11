import psycopg2

dbname = "news"

def create_connection():
    """Connects to the database news and returns the two values db and c"""
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    return db, c

# 1. What are the most popular three articles of all time?
def most_popular_articles_view():
    """Creates a view of the most viewed articles, by connecting the two tables
    articles and log and counts the number of views grouped by the articles"""
    db, c = create_connection()
    sql_query = "create or replace view most_viewed_popular_articles as\
    select title, count(title) as views from articles,log\
    where log.path = concat('/article/',articles.slug)\
    group by title order by views desc;"
    c.execute(sql_query)
    db.commit()
    db.close()

def print_most_popular_article():
    """Takes the previously created view of the most viewed articles,
    limits the number of rows to 3 and prints them out"""
    db, c = create_connection()
    sql_query = "select * from most_viewed_popular_articles limit 3"
    c.execute(sql_query)
    result = c.fetchall()
    db.close()
    print ("\nPupular Articles:\n")
    for i in range(0, len(result), 1):
        print ("\"" + result[i][0] + "\" - " + str(result[i][1]) + " views")


# 2. Who are the most popular article authors of all time?
def most_pupular_authors_view():
    """Creates a view of the most viewed authors, by connecting the three tables
    articles, authors and log and counts the number of
    views grouped by the author"""
    db, c = create_connection()
    sql_query = "create or replace view most_popular_authors as select authors.name,\
    count(articles.author) as views from articles, log, authors where\
    log.path = concat('/article/',articles.slug) and\
    articles.author = authors.id group by authors.name order by views desc"
    c.execute(sql_query)
    db.commit()
    db.close()


def print_most_popular_authors():
    """Takes the previously created view of the most viewed authors
    and prints them out"""
    db, c = create_connection()
    sql_query = "select * from most_popular_authors"
    c.execute(sql_query)
    result = c.fetchall()
    db.close()
    print ("\nPopular Authors:\n")
    for i in range(0, len(result), 1):
        print ("\"" + result[i][0] + "\" - " + str(result[i][1]) + " views")



# 3. On which days did more than 1% of requests lead to errors?
def error_days_view():
    """Creates a view with an overview of days on which more than 1% of an
    error message was displayed"""
    db, c = create_connection()
    sql_query = "create or replace view error_days as select Date,Total,Error,\
    (Error::float*100)/Total::float as Percent from\
    (select time::timestamp::date as Date, count(status) as Total,\
    sum(case when status = '404 NOT FOUND' then 1 else 0 end) as Error\
    from log group by time::timestamp::date) as result\
    where (Error::float*100)/Total::float > 1.0 order by Percent desc;"
    c.execute(sql_query)
    db.commit()
    db.close()


def print_error_days():
    """Takes the previously created view of most error days
    and prints them out"""
    db, c = create_connection()
    query = "select * from error_days"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print ("\nDay with more than 1% of errors:\n")
    for i in range(0, len(result), 1):
         print (str(result[i][0])+ " - "+str(round(result[i][3], 2))+"% errors")


most_popular_articles_view()
print_most_popular_article()
most_pupular_authors_view()
print_most_popular_authors()
error_days_view ()
print_error_days()
