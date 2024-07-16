import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # Clear the input field


todos = functions.get_todos()
st.title("My To-do App")
st.subheader("Welcome to To-Do App")
st.write('This app is to increase your productivity.')


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label=" ", placeholder="Add new ToDo...",
              on_change=add_todo, key='new_todo')


