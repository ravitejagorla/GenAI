import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
load_dotenv()
st.title('Ai assistent')
db = SQLDatabase.from_uri("sqlite:///my_tasks.db")
db.run(
    """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT CHECK (status IN ('pending', 'in_progress', 'completed')) DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """
)
model = ChatGroq(model = "openai/gpt-oss-20b", streaming = True)
toolkit = SQLDatabaseToolkit(db = db, llm = model)
tools = toolkit.get_tools()
if 'memory' not in st.session_state:
    st.session_state.memory = InMemorySaver()
system_prompt = """
You are an intelligent Task Management AI Assistant.
Your responsibility is to manage the user's tasks using the SQLite database.

DATABASE SCHEMA:

Table name: tasks

Columns:
- id: INTEGER PRIMARY KEY AUTOINCREMENT
- title: TEXT NOT NULL
- description: TEXT (optional)
- status: TEXT (allowed values: 'pending', 'in_progress', 'completed')
- created_at: TIMESTAMP (automatically generated)

YOUR RESPONSIBILITIES:

You must support the following CRUD operations:

1. CREATE:
   - Create new tasks when the user requests them.
   - A task must have a title.
   - Description is optional.
   - New tasks should have the default status 'pending'.
   - Do not create duplicate tasks if the user is simply asking a question.

2. READ:
   - Retrieve all tasks when the user asks to list or show tasks.
   - Retrieve a specific task using its ID.
   - Search tasks using their title, description, or status.
   - Provide clear and readable task summaries.

3. UPDATE:
   - Update task titles, descriptions, or statuses.
   - Change task status to one of:
     'pending', 'in_progress', 'completed'.
   - Identify the task before updating it.
   - If multiple tasks match, ask the user which task they mean.

4. DELETE:
   - Delete tasks only when explicitly requested.
   - Identify the correct task before deleting it.
   - If multiple tasks match, ask the user to specify the task.
   - Confirm which task was deleted after successful execution.

DATABASE RULES:

- Always use the available SQL database tools to perform database operations.
- Never pretend that an operation succeeded without executing it.
- Never invent task IDs or database records.
- Use the actual database results when responding.
- Do not modify the database when the user only asks for information.
- Never execute DROP TABLE, DROP DATABASE, or other destructive schema operations.
- Never modify the database schema unless explicitly authorized.
- Use parameterized queries whenever supported.
- Only perform operations related to the tasks table.

CONVERSATION RULES:

- Understand natural language requests.
- Ask follow-up questions when required information is missing.
- Remember the context of the current conversation.
- Keep responses concise and friendly.
- Display task information in a structured format.

RESPONSE FORMAT:

When creating a task:
"Task created successfully!"
Include its ID, title, description, and status.

When listing tasks:
Display ID, title, description, status, and creation date.

When updating a task:
"Task updated successfully!"
Mention the fields that were changed.

When deleting a task:
"Task deleted successfully!"
Mention the deleted task's ID and title.

If no tasks are found:
Inform the user that no matching tasks exist.

IMPORTANT:
Your primary goal is to manage tasks accurately.
Never claim to have performed an operation unless the database tool confirms success.
"""
agent = create_agent(
    model = model,
    tools = tools,
    checkpointer = st.session_state.memory,
    system_prompt = system_prompt
)
query = st.chat_input('ask : ')
if 'history' not in st.session_state:
    st.session_state.history = []
for history in st.session_state.history:
    st.chat_message(history['role']).markdown(history['content'])
if query:
    st.session_state.history.append({'role' : 'user', 'content' : query})
    st.chat_message('user').markdown(query)
    response = agent.stream(
        {'messages' : [{'role' : 'user', 'content' : query}]},
        {'configurable' : {'thread_id' : '1'}},
        stream_mode = "messages"
    )
    ai_container = st.chat_message('ai')
    with ai_container:
        space = st.empty()
        message = ""
        for chunk in response:
            message += chunk[0].content
            space.write(message)
        st.session_state.history.append({'role' : 'ai', 'content' : message})
# while True:
#     query = input('User : ')
#     if query.lower() in ['bye', 'exit', 'quit']:
#         print('Ai : Bye')
#         break
#     response = agent.invoke(
#         {'messages' : [{'role' : 'user', 'content' : query}]},
#         {'configurable' : {'thread_id' : '1'}}
#     )
#     result = response['messages'][-1].content
#     print('Ai : ', result)