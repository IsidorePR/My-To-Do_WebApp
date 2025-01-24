import streamlit as st
import ToDoFunction

Tasks = ToDoFunction.get_ToDos()

def add_task():
    Task = st.session_state['new_task'] + "\n"
    Tasks.append(Task)

    ToDoFunction.write_ToDos(Tasks)

st.title("My To Do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, Task in enumerate(Tasks):
    checkbox = st.checkbox(Task, key=Task)
    if checkbox:
        Tasks.pop(index)
        ToDoFunction.write_ToDos(Tasks)
        del st.session_state[Task]
        st.rerun()


st.text_input(label= "Enter a Todo", placeholder="Add New Todo...",
              on_change=add_task, key = 'new_task' )

st.session_state