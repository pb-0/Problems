import sqlite3
import pandas as pd

df = pd.read_csv('ConsecutiveDatesSQL.csv')

conn = sqlite3.connect("Temp.db")

df.to_sql('df', conn, if_exists='replace')

statement = "select " \
            "start_date, " \
            "count(*) " \
            "from" \
            "(select" \
            " *," \
            "diff," \
            " DATE(date,diff) start_date " \
            "from " \
            "(select" \
            " *, " \
            "'-' || row_num || ' DAYS' as diff" \
            " from " \
            " (select DATE(substr(date, 7,4) || '-' || substr(date, 1,2) || '-' || substr(date, 4,2)) date, price, row_number() OVER(order by date) row_num from df where price >= 101)" \
            ")" \
            ")" \
            "group by 1"
result = pd.read_sql(statement, conn)
print(result)
# conn.execute(statement)