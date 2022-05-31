from pip import main


class No:
    
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
    
    def __str__(self):
        return str(self.dado)

class Arvore_binaria:
    
    def __init__(self, dado=None):
        if dado:
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

    def pos_ordem(self, no=None):
        if no is None:
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
    
    def minimo(self, aux="raiz"):
        if aux == "raiz":
            aux = self.raiz
        while aux.esq:
            aux = aux.esq
        return aux.dado

    def maximo(self):
        aux = self.raiz
        while aux.dir:
            aux = aux.dir
        return aux.dado

    def total_nos(self, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return 0
        else:
            return 1 + self.total_nos(no.esq) + self.total_nos(no.dir)

    def total_folhas(self, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return 0
        elif no.esq==None and no.dir==None:
            return 1
        else:
            return self.total_folhas(no.esq) + self.total_folhas(no.dir)

    def folhas(self, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return
        if no.esq==None and no.dir==None:
            print(no.dado, end=' ')
            return
        if no.esq:
            self.folhas(no.esq)
        if no.dir:
            self.folhas(no.dir)

    def altura(self, no=None, flag=True):
        if flag:
            if no:
                no = self.busca(no)
                if no is None:
                    return no
                no = no.raiz
            else:
                no = self.raiz
            flag = False
        esquerda = 0
        direita = 0
        if no is None:
            return -1
        else:
            esquerda = self.altura(no.esq, flag=False)
            direita = self.altura(no.dir, flag=False)
            if esquerda > direita:
                return esquerda + 1
            return direita + 1
    
    def nivel(self, valor, nivel=0, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return no
        if no.dado == valor:
            return nivel
        if valor < no.dado:
            return self.nivel(valor, nivel + 1, no.esq)
        return self.nivel(valor, nivel +1, no.dir)

    def remover(self, valor, no="raiz"):
        if no == "raiz":
            no = self.raiz
        if no is None:
            return no
        if valor < no.dado:
            no.esq = self.remover(valor, no.esq)
        elif valor > no.dado:
            no.dir = self.remover(valor, no.dir)
        else:
            if no.esq is None:
                if valor == self.raiz.dado:
                    self.raiz = no.dir
                return no.dir
            elif no.dir is None:
                if valor == self.raiz.dado:
                    self.raiz = no.esq
                return no.esq
            else:
                substituto = self.minimo(no.dir)
                no.dado = substituto
                if valor == self.raiz.dado:
                    self.raiz = substituto
                no.dir = self.remover(substituto, no.dir)
        return no