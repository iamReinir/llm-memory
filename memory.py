from database import MemoryEntry, engine
from sqlalchemy.orm import Session
from config import mcp

IMPORTANT = 'important'

@mcp.tool()
def recall():
    """
    Use this to recall all important memories.
    """
    return get_memory(IMPORTANT)

def get_memory(memory_type):
    with Session(engine) as session:
        entries = session.query(MemoryEntry).filter_by(mem_type=memory_type).all()
        return [f"{entry.content}" for entry in entries]

@mcp.tool()
def remember(contents: list):
    """
    Use this to add important memories.
    """
    add_memories(IMPORTANT, contents)


def add_memories(memory_type: str, contents: list):
    """
    Add memories of a specific type.
    """
    with Session(engine) as session:
        for content in contents:
            entry = MemoryEntry(mem_type=memory_type, content=content)
            session.add(entry)
        session.commit()

@mcp.tool()
def delete_memory(entry_contents: list):
    """
    Delete memory entry.
    """
    with Session(engine) as session:
        for entry_content in entry_contents:
            entry = session.query(MemoryEntry).filter(MemoryEntry.content == entry_content).first()
            if entry:
                session.delete(entry)
            else:
                return f"Memory Entry {entry_content} not found"
        session.commit()
    return 'Memory Entries deleted'

@mcp.tool()
def update_memory(old_content, new_content):
    """
    Update memory entry content by ID.
    """
    with Session(engine) as session:
        entry = session.query(MemoryEntry).filter(MemoryEntry.content == old_content).first()
        if entry:
            entry.content = new_content
            session.commit()
        else:
            return f"Memory Entry not found"

"""
@mcp.tool()
def add_important_memory(content):
    add_memory(IMPORTANT, content)

@mcp.tool()
def add_memories(memory_type, contents):
    for content in contents:
        add_memory(memory_type, content)

@mcp.tool()
def add_important_memories(contents):
    for content in contents:
        add_memory(IMPORTANT, content)

@mcp.tool()
def get_memory_type(memory_type):
    with Session(engine) as session:
        entries = session.query(MemoryEntry).filter_by(mem_type=memory_type).all()
        return [entry.content for entry in entries]

@mcp.tool()
def get_memory_types(memory_types):
    result = {}
    for memory_type in memory_types:
        result[memory_type] = get_memory_type(memory_type)
    return result

@mcp.tool()
def get_important_memory():
    return get_memory_type(IMPORTANT)

@mcp.tool()
def update_memory(entry_id, new_content):
    with Session(engine) as session:
        entry = session.query(MemoryEntry).get(entry_id)
        if entry:
            entry.content = new_content
            session.commit()

@mcp.tool()
def update_memory_type(entry_id, new_type):
    with Session(engine) as session:
        entry = session.query(MemoryEntry).get(entry_id)
        if entry:
            entry.mem_type = new_type
            session.commit()

@mcp.tool()
def clear_memory(memory_type):
    with Session(engine) as session:
        session.query(MemoryEntry).filter_by(mem_type=memory_type).delete()
        session.commit()

@mcp.tool()
def mark_as_important(entry_id):
    with Session(engine) as session:
        entry = session.query(MemoryEntry).get(entry_id)
        if entry:
            entry.mem_type = IMPORTANT
            session.commit()

@mcp.tool()
def unmark_as_important(entry_id, new_type):
    with Session(engine) as session:
        entry = session.query(MemoryEntry).get(entry_id)
        if entry:
            entry.mem_type = new_type
            session.commit()
"""
