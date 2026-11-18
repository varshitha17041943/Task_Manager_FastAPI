from fastapi import FastAPI
api=FastAPI()
from pydantic import BaseModel
from mysql.connector import connect
def connect_mysql():
    conn=connect(
        user="root",
        password="your_mysql_password",
        host="localhost",
        database="fastapi_taskmanager"
    )
    pen= conn.cursor()
    return conn,pen
class Taskrequest(BaseModel):
    id:int
    title:str
    completed:bool
@api.get("/")
def home():
    return {"message":"Welcome to Task Manager API"}

def row_to_task(row):
    return {"id": int(row[0]), "title": str(row[1]), "completed": bool(row[2])}

@api.post("/create")
def task_create(request:Taskrequest):
    id=request.id
    title=request.title
    completed=request.completed
    conn,pen=connect_mysql()
    pen.execute("insert into tasks(id,title,completed) value(%s,%s,%s)",(id,title,completed))
    conn.commit()
    conn.close()
    print(request)
    return "Task Created Successfully"

@api.get("/show")
def display_tasks():
    conn,pen=connect_mysql()
    pen.execute("select id,title,completed from tasks order by id")
    tasks = [row_to_task(row) for row in pen.fetchall()]
    conn.commit()
    conn.close()
    return tasks

@api.get("/showonetask")
def display_onetask(task_id: int):
    conn,pen=connect_mysql()
    pen.execute("select id,title,completed from tasks where id= %s",(task_id,))
    row=pen.fetchone()
    conn.commit()
    conn.close()
    return row_to_task(row)

@api.put("/update")
def update_task(request:Taskrequest):
    id=request.id
    title=request.title
    completed=request.completed
    conn,pen=connect_mysql()
    if title is not None:
        pen.execute("update tasks set title=%s where id=%s",(title,id))
    if completed is not None:
        pen.execute("update tasks set completed=%s where id=%s",(completed,id))
    conn.commit()
    conn.close()
    return "Task Updated"

@api.delete("/delete")
def delete_onetask(task_id: int):
    conn,pen=connect_mysql()
    pen.execute("delete from tasks where id= %s",(task_id,))
    conn.commit()
    conn.close()
    return "Task Deleted"