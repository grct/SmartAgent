from langchain_anthropic import ChatAnthropic
import sqlite3


conn = sqlite3.connect('tools.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tools (
        id TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        data_creazione TEXT NOT NULL
    )
''')

conn.commit()

llm = ChatAnthropic(model="claude-3-haiku-20240307")