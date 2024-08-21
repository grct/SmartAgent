import uuid
from datetime import datetime
from src.settings import cursor, conn

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
cursor.execute('''
    INSERT INTO tools (id, nome, data_creazione)
    VALUES (?, ?, ?)
''', (str(uuid.uuid4()), "new_tool", now))
conn.commit()