from collections import namedtuple

Task = namedtuple("Task", ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_defaults():
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    t = Task("buy milk", 'Brian')
    assert t.summary == "buy milk"
    assert t.owner == 'Brian'
    assert (t.done, t.id) == (False, None)
