from pip import main


class No:
    
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
    
    def __str__(self):
        return str(self.dado)

class Arvore_binaria:
    
    def __init__(self, dado=None, no=None):
        if no:
            self.raiz = no
        elif dado:
            no = No(dado)
            self.raiz = no
        else:
            self.raiz = None
    
    def em_ordem(self, no=None):
        if no is None:
            no = self.raiz
        if no.esq:
            self.em_ordem(no.esq)
        print(no, end=' ')
        if no.dir:
            self.em_ordem(no.dir)
    
    def pre_ordem(self, no=None):
        if no is None:
            no = self.raiz
        print(no, end=' ')
        if no.esq:
            self.em_ordem(no.esq)
        if no.dir:
            self.em_ordem(no.dir)

    def pos_ordem(self):
        if no is None:
            no = self.raiz
        if no.esq:
            self.em_ordem(no.esq)
        if no.dir:
            self.em_ordem(no.dir)
        print(no, end=' ')

    def minimo(self):
        aux = self.raiz
        while aux.esq:
            aux = aux.esq
        return aux.dado

    def maximo(self):
        aux = self.raiz
        while aux.dir:
            aux = aux.dir
        return aux.dado

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

    def busca(self, valor, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return no
        if no.dado == valor:
            return Arvore_busca(no)
        if valor < no.dado:
            return self.busca(valor, no.esq)
        return self.busca(valor, no.dir)


