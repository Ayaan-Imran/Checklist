import sqlite3

# Create database and table
connection = sqlite3.connect("lists.db")
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS list (
    task text
)
""")
connection.commit()


# Takes mode
task = ""
mode = input("Do you want to create a task (1) or finish a task (2) or see which tasks are pending (3): ")
if mode == "1":
    task = input("Enter your task: ")
    c.execute("INSERT INTO list VALUES ({})".format('{}'.format(task)))
    connection.commit()

    c.execute("SELECT rowid, * FROM list WHERE task={}".format(task))
    lst = c.fetchall()
    connection.commit()

    print("Task is made! The number of your task is {}. I hope you aren't having a hard day!".format(lst[0][1]))
elif mode == "2":
    task = input("Are you choosing the number system(1) or the whole sentence(2): ")
    if task == "1":
        number = input("Enter your number: ")
        query = "DELETE FROM list WHERE id={}".format(number)
        c.execute(query)
        connection.commit()
        print("Successfully removed the task. You are doing good. Note, the other tasks numbers have changed. Please run the programme again to view the numbers")

    else:
        sentence = input("Please enter your sentence: ")
        c.execute("DELTE FROM list WHERE task={}".format('{}'.format(sentence)))
        connection.commit()
        print("Successfully removed the task. You are doing good. Note, the other tasks numbers have changed. Please run the programme again to view the numbers")
else:
    c.execute("SELECT rowid, * FROM list")
    for i in c.fetchall():
        print(i)

connection.close()