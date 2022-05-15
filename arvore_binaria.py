from pip import main


class No:
    def __init__(self, dado):
        self.dado = dado
        self.dir = None
        self.esq = None

class Arvore_binaria:
    def __init__(self, dado, no=None):
        if no:
            self.raiz = no
        else:
            no = No(dado)
            self.raiz = no
    
    def em_ordem(self):
        no = self.raiz
        if no.esq:
            self.em_ordem(no.esq)
        print(no, end=' ')
        if no.dir:
            self.em_ordem(no.dir)
    
    def pre_ordem(self):
        no = self.raiz
        print(no, end=' ')
        if no.esq:
            self.em_ordem(no.esq)
        if no.dir:
            self.em_ordem(no.dir)

    def pos_ordem(self):
        no = self.raiz
        if no.esq:
            self.em_ordem(no.esq)
        if no.dir:
            self.em_ordem(no.dir)
        print(no, end=' ')

class Arvore_busca(Arvore_binaria):
    def inserir(self, valor):
        pai = None
        x = self.raiz
        while(x):
            pai = x
            if valor < x.dado:
                x = x.esq
            else:
                x = x.dir
        if pai is None:
            self.raiz = No(valor)
        elif valor < pai.dado:
            pai.esq = No(valor)
        else:
            pai.dir = No(valor)

    def busca(self, valor, no):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return no
        if no.data == valor:
            return Arvore_busca(no)
        if valor < no.data:
            return self._busca(valor, no.esq)
        return self._busca(valor, no.dir)


