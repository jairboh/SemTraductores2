from anytree import Node, RenderTree

# Crear nodos
root = Node("Root")
child1 = Node("Child1", parent=root)
child2 = Node("Child2", parent=root)
grandchild1 = Node("Grandchild1", parent=child1)
grandchild2 = Node("Grandchild2", parent=child1)

# Imprimir el árbol
for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

# Salida:
# Root
# ├── Child1
# │   ├── Grandchild1
# │   └── Grandchild2
# └── Child2
