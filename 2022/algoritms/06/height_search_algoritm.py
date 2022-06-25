from collections import deque

graph = {}
graph['roman'] = ['natalia', 'daniil', 'alex']
graph['natalia'] = ['roman', 'daniil', 'vera']
graph['daniil'] = ['natalia', 'roman']
graph['vera'] = ['alex', 'nastya']
graph['alex'] = ['vera']
graph['nastya'] = ['vera', 'vadim']
graph['vadim'] = ['roman']

def height_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person, " is mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    if name[-1] == 'n':
        return True
    return False

height_search('roman')
