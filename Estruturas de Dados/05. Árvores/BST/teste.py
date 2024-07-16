from arvore_binaria import Arvore

arvore = Arvore()

arvore.incluir(10)
arvore.incluir(5)
arvore.incluir(15)

arvore.buscar(10)
arvore.buscar(7)

print("In-order:", arvore.in_order())
print("Pre-order:", arvore.pre_order())
print("Pos-order:", arvore.pos_order())

arvore.excluir(10)
print("Após as exclusões - In-order:", arvore.in_order())
print("Após as exclusões - Pre-order:", arvore.pre_order())
print("Após as exclusões - Pos-order:", arvore.pos_order())

arvore.excluir(5)
print("Após as exclusões - In-order:", arvore.in_order())
print("Após as exclusões - Pre-order:", arvore.pre_order())
print("Após as exclusões - Pos-order:", arvore.pos_order())

arvore.excluir(15)
print("Após as exclusões - In-order:", arvore.in_order())
print("Após as exclusões - Pre-order:", arvore.pre_order())
print("Após as exclusões - Pos-order:", arvore.pos_order())
