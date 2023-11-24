class Node: #Node neboli uzel - jedna ta hodnota v spojovaném seznamu
    def __init__(self, value, link):
        self.value = value
        self.link = link

def print_linked_list(begin):
    current = begin
    while current != None:
        print(current.value, end= " ")
        current = current.link
    print()

def contains_i(begin, i):
    current = begin
    while current != None:
        if current.value == i:
            return print(True)
        current = current.link
    return print(False)

def find_last_node(begin):
    current = begin
    while current.link != None:
        current = current.link
    return current

begin = Node(5,Node(2, Node(16,None)))

print_linked_list(begin)

#přidat trojku na začátek

new = Node(3,None)
new.link = begin
begin = new #begin.link = new !takhle ne!, begin.link je odkaz prvku na který odkazuje begin

print_linked_list(begin)

#smazat první prvek

begin = begin.link

print_linked_list(begin)

#přidat na druhé místo 14

new = Node(14,begin.link)
begin.link = new

print_linked_list(begin)

#zjistit jestli seznam obsahuje číslo 1

contains_i(begin,16)

#na konec přidat 4

last = find_last_node(begin)
new = Node(4, None)
last.link = new

print_linked_list(begin)
