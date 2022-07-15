print('Hello, Python!')

#Números
def numeros():
    print(3 ** 2) #quadrado
    print( 10 % 3) #resto da divisão

#Os nomes não podem começar com números
#Não pode haver espaços no nome, usamos _

def calculo():
    distancia = 100
    tempo = 20 
    velocidade = distancia/tempo
    print(velocidade)

#Strings
def strings():
    print('hello')
    print('Isso também é uma string')
    print("String com aspas duplas")

    len('hello world')

#formas de indexação
def indexacao():
    s = 'Hello Wolrd'
    print(s)
    print(s[0])
    print(s[1])
    print(s[1:])
    print(s[:3])
    print(s[-1])
    print(s[::1])
    print(s[::2])

    #Propriedades das Strings - As strings são IMUTÁVEIS
    #concatenação
    s = s + 'concatenei-me'
    #Repetições
    letra = 'z'
    print(letra*10)

    #Métodos embutidos em strings
    print(s.upper)
    print(s.lower)
    print(s.split)
    print(s.split('W'))

    #Formatos de impressão

    print("Vamos imprimir uma strint nesta string: %s",s)

    num = 10
    print("%1.2f", num)
    print("%1.0f", num)

    #Método string.format
    print('One: {p}, Two: {p}, Three: {p}'.format(p='Hi'))
    print('One: {p}, Two: {q}, Three: {r}'.format(p='Hi', q=1, r=12.3))

#Listas - SÃO MUTÁVEIS
def listas():
    lista = [1,2,3]
    lista2 = ['string',23,10.94,'Eduardo']
    len(lista2)
    print(lista2[0])
    print(lista[:3])
    print(lista + ['novo item'])
    print(lista)
    lista = lista + ['novo item']
    print(lista)

    #Dobrar a lista
    print(lista * 2)

    nova_lista = [1,2,3]
    nova_lista.append(4)
    print(nova_lista)
    nova_lista.pop(0)
    print(nova_lista)

    lista2 = ['a', 'e', 'x', 'b', 'c']
    print(lista2)
    print(lista.reverse())
    print(lista.sort())

    #Listas alinhadas

    list1 = [1,2,3]
    list2 = [4,5,6]
    list3 = [7,8,9]

    matriz = [list1, list2, list3]

    print(matriz[1])
    print(matriz[1][2])

#Dicionários - mapeamentos em python, algo tipo hash tables

def dicionarios():

    dicionario = {'chave1':'batatas', 'chave2':'olá', 'chave3':'[12,43,6]', 'chave4':['ola', 'adeus']}
    print(dicionario['chave2'])
    print(dicionario['chave2'].upper())
    print(dicionario['chave4'][1].upper())

    #Dicionários Vazio
    d ={}
    d['animal'] = 'cao'
    d['quantos'] = 42
    print(d)

    d = {'chave1':{'chavemestre':{'chave':'tesouro'}}}
    print(d['chave1']['chavemestre']['chave'])

    print(dicionario.keys()) #retorna todas as chaves
    print(dicionario.values()) #retorna todos os valores
    print(dicionario.items()) #método para retornar os pares

# TUPLAS
# muito semelhantes às listas, no entanto são imutáveis
#úteis para apresentar dias da semana ou datas num calendário

def tuplas():

    t = (1,2,3, 'one')
    print(len(t))
    print(t[0])
    print(t.index('one'))
    print(t.count('one'))

# SETS
#os conjuntos (sets) são uma coleção não ordenada de elementos únicos

def sets():
    x = set()
    x.add(2)
    print(x) #vai imprimir entre colchetes {}
    l = [1,3,2,4,1,2,5,6,7,3,6,2,8,2,7,2,9]
    print(set(l)) #útil para filtrar listas

# OPERADORES DE COMPARAÇÃO
# == , != , < , > , <= , >= , AND , OR
#retorna true ou false

#operadores em cadeia
# 1 < 2 < 3  TRUE
# 1 < 3 > 2 TRUE

# IF, ELIF, ELSE

def condicoes():
    cond = 'Bank'

    if cond == 'Auto Shop':
        print('Welcome to the Auto Shop!\n')
    elif cond == 'Bank':
        print('Welcome to the bank!\n')
    else:
        print('Where are you?')

    # FOR
    l = [1,2,3,4,5,6,7,8,9]
    for num in l:
        print(num)

    for num in l:
        if num % 2 == 0:
            print(num)
        else:
            print('Número ímpar')

    list_sum = 0

    for num in l:
        list_sum += num

#STRINGS
    print(list_sum)

    for letter in 'This is a string.':
        print(letter)

#TUPLAS
def tuplas2():
    tup = (1,2,3,4,5)

    for t in tup:
        print(t)

    l = [(2,4), (6,8), (10,12)]

    for tup in l:
        print(tup)

    for (t1,t2) in l:
        print(t1)

#DICIONÁRIOS
def dicionarios2():
    d = {'k1':1, 'k2':2, 'k3':3}

    for item in d:
        print(item)

    for k,v in d.item():
        print(k)
        print(v)


# WHILE

def iterativos():
    x = 0

    while x <= 10:
        print('atualmente x é: ', x)
        print('x continua menor que 10, vou adicionar +1')
        x += 1

    else:
        print('All Done!')

# BREAK, CONTINUE, PASS

    x = 0

    while x < 10:
        print(' x é atualmente: ', x)
        print('x é menor que 10, vou adicionar mais 1')
        x += 1
        if x == 3:
            print('x == 3')
        else:
            print('continuando...')
            continue

    while x < 10:
        print(' x é atualmente: ', x)
        print('x é menor que 10, vou adicionar mais 1')
        x += 1
        if x == 3:
            print('Breaking because x == 3')
            break
        else:
            print('continuando...')
            continue

# RANGE 

    range(0, 10) #não faz nada, devemos especificar ao Python que queremos que o range() seja convertido para uma lista

    print(list(range(0,10)))

    r = range(10,25)
    tuple(r)

    s = range(0,20,2)
    print(list(s))

# FUNÇÕES
# formalmente uma função é um dispositivo útil que agrupa um conjunto de instruções que para elas possam ser executadas mais que uma vez
# também podem especificar parâmetros que possam servir como entradas para as funções
# 
# sintaxe
def funcoes():
    def nome_da_funcao(arg1, arg2):
        # ...
        # A documentação da função ficará aqui
        # ...
        # Faça coisas aqui
        a = 10
        return #retorne o resultado

    def say_hello():
        print('hello')

    say_hello() #chamar a função

    def add_num(num1, num2):
        return num1 + num2

    add_num(3,8)

    def is_prime(num):
        #...
        # Método para verificarmos se é primo
        # ...
        for n in range(2, num):
            if num % n == 0:
                print('Não é primo')
                break
        else: 
            print('Primo') #Não estou certo desta identação

    is_prime(11)

    import math
    def is_prime2(num):

        # Método melhor para verificar

        if num % 2 == 0 and num > 2:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    is_prime2(11)

# DECLARAÇÕES ANINHADAS E ESCOPO
# vamos entender como o Python lida com os nomes das variáveis que atribuímos. O nome é armazenado em um namespace. Nomes das variáveis também têm escopo
# o escopo determina a visibilidade desse nome de variável para outras partes do seu código

print("DECLARAÇÕES ANINHADAS E ESCOPO")
x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#Em termos simples a ideia de escopo pode ser descrita por 3 regras gerais:
# 1. As atribuições de nomes criam ou alteram nomes locais por padrão
# 2. Existem 4 tipos possíveis de escopo: Local; Enclosing Functions; Global; Built-In;
# 3. Os nomes declarados em declarações globais e não locais mapeiam nomes atribuídos para preecher módulos e escopos de função

# L : Local - Nomes atribuídos de qualquer forma de uma função (def ou lambda) e declarações não globais nessa função

def local():
    # x é local aqui
    x = 10
    print(x)

local()

def local2():
    a = 100
    print(locals())

local2() # podemos usar a função locals para retornar um dicionários

# E : Enclosing functions locals - Nome no escopo local de todas e quaisquer funções encapsuladas (def ou lambda), de dentro para fora

name = 'This is a global name'

def greet():
    name = 'Eduardo'

    def hello():
        print('Hello' + name)
    
    hello()

greet()
print(name)

# G : Global (módulo) - Nomes atribuídos no nível superior de um arquivo de módulo, ou declarados como global em um def dentro de um arquivo

var_global = 'Variável Global'
print(var_global)

print(globals())

# B : Built In (Python) - Nomes pré-atribuídos no módulo: open, range, SyntaxError, ...

len
# <built-in function len>

# Variáveis Locais
# quando declaramos variáveis dentro de uma definição de função, elas não estão relacionadas de nenuma maneira a outras variáveis com os mesmos nomes usados fora da função
# Ou seja, os nomes de variáveis são locais para a função

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)

# Declaração Global 

x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is:', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is:', x)
func()
print('Vlaue of x (outside of func()) is :', x)

# Programação Orientada a Objetos 

print("PROGRAMAÇÃO ORIENTADA A OBJETOS")

# Vamos abordar os seguintes tópicos:
# Objetos
# Usando a palavra-chave class
# criando atributos de classe
# criando métodos em uma classe
# Herança
# Métodos especiais para classes

# relembrando objetos básicos
l = [1,2,3]
print(l.count(2)) # vamos chamar um método

# O que vamos fazer  é explorar como podemos criar um tipo de objeto como uma lista
# Em Python tudo é um objeto. Podemos usar a função type() para verificar o tipo de objeto

print(type(1))
print(type({}))
print(type(()))
print(type([]))

# A palavra chave para criarmos o nosso próprio tipo de objeto em Python é CLASS
# A classe é um modelo que define a natureza de um objeto. Das classes podemos construir instâncias. Uma instância é um objeto específico criado a partir de uma determinada classe

#Cria um novo tipo de objeto chamado Exemplo
class Exemplo(object):
    pass

#Instanciando Exemplo
x = Exemplo()

print(type(x))

# Por convenção damos às classes um nome que começa com uma letra maiúscula. Observe como x é agora a referência para a nossa nova instância da classe Exemplo. Em outras palavras, nós instanciamos a classe Exemplo
# Dentro da classe temos apenas um pass (que é usado quando queremos que algo não faça nada). Mas podemos definir atributos e métodos para a classe.
# Um atributo é uma característica de um objeto. Um método é uma operação que podemos realizar com o objeto.
# P.e, podemos criar uma classe chamada Dog. Um atributo de Dog pode ser a sua raça ou seu nome, enquanto um método para Dog pode ser algo como latir() que retorna um som.

# ATRIBUTO
# A sintaxe para criar um atributo é:
# self.attribute = something

# Existe um método especial chamado __init__()

# Esse método é usado para inicializar os atributos de um objeto. Por exemplo:

class Dog(object):
    def __init__(self, breed):
        self.breed = breed

sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

# Vamos descrever o que temos acima. O método especial __init__() é chamado automaticamente logo após o objeto ter sido criado:

# def __init__(self, breed): cada atributo em uma definição de classe começa com uma referência ao objeto da instância. É convencionalmente chamado de self (semelhante a 'this' em outras linguagens)
# Breed é o argumento. O valor é passado durante a instanciação da classe
# Agora criamos duas instâncias da classe Dog.
print(sam.breed)
print(frank.breed)

# Observe como não temos parênteses após o breed, isto é porque é um atributo e não leva nenhum argumento
# Em Python também existem atributso de objeto de classe. Estes atributos são os mesmos para qualquer instância da classe. Por exemplo, podemos criar o atributo espécie para a classe Dog.
# Os cães independentemente da sua raça, nome ou outros atributos serão sempre mamíferos. Aplicamos essa lógica da seguinte maneira

class Dog(object):

    #Atributos da classe
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed =  breed
        self.name = name

sam =  Dog('Lab', 'Sam')
print(sam.name)

# Observe que o Atributo da classe foi definido fora de qualquer método na classe. Também por convenção, nós os colocamos antes do __init__()

print(sam.species)

# MÉTODOS
# São funções definidas dentro do corpo de uma classe. Eles são usados para executar operações com os atributos dos nossos objetos. Os métodos são essenciais no conceito de encapsulamento em POU
# Isso é essencial para dividr as responsabilidades na programação, especialmente em grandes aplicações. Podemos basicamente pensar em métodos como funções que atuam em um objeto que levam o próprio objeto através de seu argumento self

class Circle(object):
    pi = 3,14

    # O círculo é estanciado com um raio (o padrão é 1)
    def __init__(self, radius = 1):
        self.radius = radius

    # Método de cálculo da área. Observe o uso do self
    def area(self):
        return self.radius * self.radius * Circle.pi

    # Método que redefine o raio
    def setRadius(self, radius):
        self.radius = radius

    # Método para obter o raio
    def getRadius(self):
        return self.radius

c = Circle()

c.setRadius(2)
print('O raio é:', c.getRadius())
print('A área é:', c.area())

# Observe como usamos a notação self para atributos de referência da classe dentro dos métodos


# HERANÇA 
# A herança é uma forma de formar novas classes usando classes que já foram definidas. As classes recÉm formadas são chamadas classes derivadas, as classes de que derivamos são chamadas de classes base
# Os benefícios importantes da henraça são a reutilização de código e redução da complexidade de um programa. As classes derivadas (descendentes) susbtituiem ou estendem a funcionalidade das classes base (ancestrais)

class Animal(object):
    def __init__(self):
        print("Animal created")
    
    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI()
d.eat()
d.bark()

# Neste exemplo, temos duas classes: Animal e Dog. O animal é a classe base, o cão é a classe derivada
# A classe derivada herda a funcionalidade da classe base
# É mostrado pelo método WhoAmI(). A classe derivada modifica o comportamento existente da classe base
# É mostrado pelo método eat() a funcionalidade da classe base. Finalmente, a classe derivada estende a funcionalidade da classe base, e também define um novo método bark()

# MÉTODOS ESPECIAIS
# Classes em Python podem implementar determinadas operações com nomes de método especiais. Estes métodos não são realmente chamados diretamente, mas pela sintaxe da linguagem específica do Python

print("MÉTODOS ESPECIAIS")

class Book(object):
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title:%s, author:%s, pages:%s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book was destroyed")

book = Book("Python Rocks!", "Rodrigo Tadewald", 159)

#Métodos especiais
print(book)
print(len(book))
del book

# Os métodos init(), str(), len(), e del() são definidos pelo uso de sublinhados. Eles nos permitem usar funções específicas do Python em objetos criados através da nossa classe

# MÓDULOS E PACOTES
# Os módulos no Python são simplesmente arquivos Pyton com a extensão .py que implementam um conjunto de funções.
# Para importar um módulo, usamos o comando import. A primeira vez que um módulo é carregado em um script Python em execução, ele é inicializado executando o código do módulo

# Importar a biblioteca de matemática
from ast import Or
import math

#Arrredondar um número
math.ceil(2.4)

# Duas funções muito importantes, que são úteis, quando se exploram módulos no Python - as funções dir() e help()
# Podemos procurar quais funções são implementadas em cada módulo usando a função dir()

print(dir(math))

# Quando encontramos a função que queremos usar, podemos ler mais sobre isso usando a função help(), dentro do interpretador Python:
help(math.ceil)

# ESCREVENDO MÓDULOS

# Escrever módulos em Python é muito simples. Para criar um módulo por conta própria, basta criar um novo arquivo .py com o nome do módulo e, em seguida, importá-lo usando o nome do arquivo Python (sem a extensão .py) usando o comando import

###################################
#           AVANÇADO              #
###################################  

# COMPREENSÃO DE LISTAS

# Compreensões de listas nos permitem construir listas usando uma notação diferente. Você pode pensar nisso essencialmente
# como um loop construído dentro de colchetes. Um exemplo simples:

print("COMPREESÃO DE LISTAS")

# Pega todas as letras em uma string
lst = [x for x in 'word']
#Verificar
print(lst)

# Outro exemplo
lst = [ x**2 for x in range(0,11)]
print(lst)

lst = [x for x in range(11) if x % 2 == 0]
print(lst)

# Também podemos fazer operações aritméticas mais complicadas
# Converte Celsius para Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5) * temp + 32) for temp in celsius]

print(fahrenheit)

# Também podemos realizar compreensões de listas aninhadas, por exemplo
lst = [x**2 for x in [x**2 for x in range(11)]]
print(lst)

#  COMPREENSÃO DE DICIONÁRIOS

print("COMPREENSÃO DE DICIONÁRIOS")

# Assim como a compreensão de listas, dicionários também suportam sua própria versão para criação rápido

d = {x:x**2 for x in range(10)}

# Uma das razões pelas quais não é tão comum é a dificuldade em estruturas os nomes das chaves que não se basieam nos valores

p =  'Python'
{p.index(x):x for x in p}

# EXPRESSÕES LAMBDA

# As expressões lambda nos permitem criar funções "anónimas". Isso basicamente siginfica que podemos criar funções ad hoc sem necessidade de definir corretamente uma função usando def
# Os objetos de função retornados em expressão lambda funcionam extamente como os criados e atribuídos por def
# A diferença fundamental que torna a lambda útil em papéis especializados é que o corpo do lambda é uma expressão única, não um bloco de declarações
# O corpo de lambda é semelhante ao que colocamos na declaração de retorno do corpo def
# Simplesmente escrevemos o resultado como uma expressão em vez de devolvê-lo explicitamente
# Como é limitado a uma expressão, uma lambda é menos complexa que uma def. A lambda foi projetada para codificar funções simples e a def para codificar funções maiores
# Vamos montar lentamente uma expressão lambda, desconstruindo uma função

print("EXPRESSÕES LAMBDA")

def square(num):
    result = num**2
    return result

print(square(2))

# Quebrando mais

def square(num):
    return num**2

print(square(2))

# Nós podemos realmente escrever isso em uma linha (embora seja uma forma ruim para fazê-lo)

def square(num) : return num**2

print(square(2))

# Essa é a forma de uma função que uma expressão lambda pretende replicar. Uma expressão lambda pode então ser escrita como

lambda num : num**2

# Acho que é suposto mostrar no terminal <function __main__.<lambda>(num)>

# Observe comom recuperamos uma função. Podemos atribuir essa função a uma variável

square = lambda num: num**2
print(square(3))

# Mais alguns exemplos

even = lambda x: x % 2 == 0

print(even(3))
print(even(4))

first = lambda s: s[0]
print(first('hello'))

rev = lambda s: s[::-1]
print(rev('hello'))

# Assim como uma função normal, podemos aceitar mais de um parâmetro em uma expressõa lambda

adder = lambda x,y: x + y
print(adder(2,3))

# OPERADOR TERNÁRIO
# O operador ternário é um jeito mais prático e rápido de usarmos o if else

print("OPERADOR TERNÁRIO\n")

idade = 21
if idade >= 18:
    print("Acesso autorizado")
else:
    print("Acesso NÃO autorizado")

# Com o operador ternário

print("Acesso autorizado" if idade >= 18 else "Acesso não autorizado")

"Sim" if True else "Não"

n = 16
# Verificar se o número é par ou ímpar
r = "PAR" if n % 2 == 0 else "ÍMPAR"
print(r)

# ERROS E EXPRESSÕES
print("\n ERROS E EXPRESSÕES\n")

# Aprender a ligar com erros e manipulação de exceções em Python

# Se fizermos print('Hello), obtermos um SyntaxError com a descrição adicional que era um EOL (End of Line Error)
# Podemos encontrar a lista completa de exceções embutidas em https://docs.python.org/3/library/exceptions.html

# TRY AND EXCEPT
# O código que pode causar uma exceção é colocado no bloco try e o tratamento da exceção é implementado no bloco except. O formato da sintaxe é o seguinte:

# try:
#   Você pode fazer algo aqui...
# except Exceptional:
#   Se causar a Exceptional, roda isso
# except Exceptionall:
#   Se causar a Exceptionall, roda isso
# else:
#   Se não causar excessões, roda isso

# Nós também podemos apenas verificar qualquer exceção apenas com o except.

def square(n):
    return n**2

print(square(2))
print(square(4))

# A função funciona perfeitamente, mas e se passássemos uma string em vez de um nr?
# square("hello") -> Íamos obter um erro
# Podemos então fazer

def square(n):
    try:
        return n**2
    except:
        print("Parâmetro inválido. Uma exceção ocorreu")

square("hello")

# O erro não será disparado e a nossa mensagem de erro será retornada. Isso é muito importante para que o programa continui correndo e funcionando se um erro acontecer

# RAISE
# Às vezes queremos disparar nossos próprios erros dependendo da situação. Vamos criar uma função que dado um núemro de 1-12 é retornado o respetivo mês

print("\nRAISE\n")

def mes(n):
    meses = [
        "Janeiro",
        "Fevereiro",
        "Março",
        "Abril",
        "Maio",
        "Junho",
        "Julho",
        "Agosto",
        "Setembro",
        "Outubro",
        "Novembro",
        "Dezembro"
    ]
    try:
        return meses[n-1]
    except:
        raise Exception("Mês Inválido")

# Observar o que acontece se fizermos mes(25). Na nossa função usamos raise e chamamos Exception() passando nossa mensagem como parâmetro
# Então quando passamos um valor inválido para a função duas exceções ocorreram: IndexError por cause que o índice da lsita meses não vai até 25-1. E a segnuda exceção é a nossa exceção que lançamos
# Vemos como fica mais fácil entender o erro com a mensagem da nossa exceção. Poderíamos apenas ter imprimido uma mensagem de erro com a função print() em vez de usarmos o raise, porém dependendo da situação é imporatnte forçarmos um erro para que resultados não acontençam. É melhor um erro que uma resposta errada

# FINALLY
# O finally é o bloco de código sempre executado, independetemente de existir uma exceção no bloco de código try.

print("\n FINALLY \n")

def square(n):
    try:
        return n**2
    except:
        print("Parâmetro inválido. Uma exceção ocorreu")
    finally:
        print("Eu sempre serei executado.")

square(9)
# square("PYTHON") -> testar para ver o "erro" acontecer

# MAP
# map() é uma função que leva dois argumentos: uma função e um objeto iterável. Na forma map(função, iterável)
# O primeiro argumento é o nome de uma função e a segunda uma sequência (p.e., uma lista). map() aplica a função a todos os elementos da sequência
# Retorna uma nova lista com os elementos alterados pela função

print("\n MAP \n")

def fahrenheit(T):
    return (9/5) * T + 32

def celsius(T):
    return (5/9) * T - 32

temp = [0, 22.5, 40, 100]

F_temps = list(map(fahrenheit, temp))

print(F_temps)

print(list(map(celsius, F_temps)))

# No exemplo acima não usamos uma expressão lambda. Ao usar lambda, não teríamos que definir e nomear as funções fahrenheit e celsius

print(list(map(lambda x : (5/9) * x - 32, F_temps)))

# map() pode ser aplicado a mais de um iterável. Os iteráveis devem ter o mesmo comprimento
# P.e., se estamos trabalhando com duas listas, map() aplicará sua função aos elementos das listas de argumentos, ou seja, aplica-se primeiro aos elementos com o índice 0
#, e depois aos elementos com o 1º índice até que o índice N seja alcançado

a = [1,2,3,4]
b = [5,6,7,8]
c = [9, 10, 11, 12]

print(list(map(lambda x,y:x+y,a,b)))
print(list(map(lambda x,y,z:x+y+z, a,b,c)))

# REDUCE
print("\n REDUCE \n")

# a função reduce(função, sequência) aplica continuamente uma função à sequência. Em seguida, ela retorna um único valor
# Se seq = [s1, s2, s3, ..., sn] reduce(função, sequência) funciona assim:
#   No início, os dois primeiros elementos da seq serão aplicados à função func(s1, s2)
#   A lista em que reduce() funciona parece assim: [função(s1,s2), s3, ...,sn]
#   No próximo passo, a função será aplicada no resultado anterior e no terceiro elemento da lista, ou seja, função(função(s1,s2), s3)
#   A lista parece agora: [função(função(s1, s2), s3), ..., sn]

# Continua assim até apenas um elemento é deixado e retorna esse elemento como resultado do reduce()

# Em Pyon3 temos que importar a função reduce
from functools import reduce

lst = [47, 11, 42, 13]
print(reduce(lambda x,y: x+y, lst))
# Vai imprimir 113

# Encontra o valor máximo de uma sequência
max_find = lambda a,b: a if (a>b) else b
print(reduce(max_find, lst))
# Vai fazer print de 47

# FILTER
print("\n FILTER \n")

# A função filter(função, lista) oferece uma maneira conveninente de filtrar todos os elementos de um iterável para o qua a função retorne True
# Precisa de uma função como seu primeiro argumento. A função precisa retornar um valor booleano (True ou False)

def even_check(num):
    if num % 2 == 0:
        return True

# Agora vamos filtrar uma lista de números. Nota: colocar a função em filtro sem parênteses pode parecer estranho, mas tenha em mente que as função também são objetos.
# A função filter retorna um objeto na memória onde o filtro ocorreu. Será necessários transformá-lo em lista para visualizá-lo

lista1 = [1, 4, 9, 16, 25]
print(list(filter(even_check, lista1)))

# filter() é mais comumente usado com funções lambda, porque usamos o filtro para um trabalho rápido, onde não queremos escrever um função inteira
# Vamos repetir o exemplo acima usando uma expressão lambda
print(list(filter(lambda x: x % 2 == 0, lst)))

# ZIP
print("\n ZIP \n")
# zip() cria um iterado que agrega elementos de cada um dos iteráveis
# Retorna um iterador de tuplas, onde o nº elemento da tupla contém o nº elementos de cada uma das sequências ou do iterável passado como argumentos.
# Com um único argumento iterável, ele retorna um iterador de tupla com um elemento. Sem argumentos, ele retorna um iterador vazio.

# O zip() só deve ser usado com entradas de comprimentos desiguais quando você não se preocupa com os valores interruptos, além dos valores mais longos
x = [1,2,3]
y = [4,5,6]

# Junta as duas listas. Lembre-se de usar a função list() para converter o resultado para uma lista
print(list(zip(x,y)))

# Observe como as tuplas são retornadas
# E se um iterável for mais longo que o outro?
x = [1,2,3]
y = [4,5,6,7,8]

# Junte as duas listas
print(list(zip(x,y))) # o zip é definido pelo comprimento iterável mais curto

# O que acontece se tentarmos compactar os dicionários
d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

print(list(zip(d1,d2)))
# Isso faz sentido porque simplesmente iterar através dos dicionários resultará em apenas as chaves. Teríamos que chamar métodos para misturar os valores
print(zip(d2,d1.values()))

# Ótimo! Finalmente, use o zip() para alternar as chaves e os valores dos dois dicionários
def switcharoo(d1,d2):
    dout = {}

    for d1key, d2val in zip(d1, d2.values()):
        dout[d1key] = d2val

    return dout

print(switcharoo(d1,d2))

# ENUMERATE 
print("\n ENUMERATE \n")
# enumerate permite que você conte elementos enquanto itera através de um objeto. O método retorna uma tupla na forma(contagem, elemento)

lst = ['a','b','c']

for number, item in enumerate(lst):
    print(number)
    print(item)

# torna-se útil quando preciamos de ter algum tipo de rastreador

# ALL e ANY
print("\n ALL e ANY \n")

# all e any são funções integradas em python que nos permitem verificar convenientemente a correspondência booleana em um iterável. all() retornará True se todos os elementos em um iterável foram True
# any retornará True se qualquer um dos elementos no iterável for True
lst = [True, True, False, True]
print(all(lst))
print(any(lst))

# DECORADORES
print("\n DECORADORES \n")
# Podem ser pensados como funções que modificam a funcionalidade de outra função. Eles ajudam a tornar seu código mais curto
# Para explicar corretamente os decoradores, vamos construí-los lentamente a partir de funções

def hello(name='Rodrigo'):

    def greet():
        return '\t This is inside the greet() function'

    def welcome():
        return "\t This is inside the welcome() function"

    if name == 'Rodrigo':
        return greet
    else: 
        return welcome

# Agora vamos ver que função será retornada se definirmos x = hello(), Note como os parêntesis fechados significam que o nome foi definido como Rodrigo
# Ia imprimir <function
            #  __main__.hello.<locals>.greet()>
# Note como x está apontado para função greet, dentro da função hello
print(x())

# O if e else dentro da função estão retornando greet e welcome, não greet() e welcome(). Se você colocar o parêntesis acabará por executar as funções.
# Sem eles, é possível passar os mesmos para outras variáveis

# Quando escrevemos x = hello(), hello() é executado e o nome passado é Rodrigo, então a função greet é retornada. Se mudarmos a definição para x = hello(name="Paulo")
# Podemo também tentar printar hello()() que fará com que a função greet seja executada

# FUNÇÕES COMO ARGUMENTOS
# Agora vamos ver como passar funções como argumentos para outras funções
def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello)

# Ótimo! Olhe como podemos passar funções como objetos e usá-los dentro de outras funções. Agora conseguimos construir nosso primeiro decorador
# No exemplo anterior nós criamos manualmente um decorador, aqui iremos modificá-lo

def new_decorator():
    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()

# Redefine a função
func_needs_decorator =  new_decorator(func_needs_decorator)

func_needs_decorator()

# O que aconteceu aqui? Um simples decorador entrou na função e modificou seu comportamento. Agora vamos entender como nós podemos reesrevevr este código usando o símbolo @, que Python usa como decorador

@new_decorator
def func_needs_decorator():
    print("This is function is in need of a Decorator")

func_needs_decorator()

# Agora você construiu um decorador manualmente e viu como usar o símbolo @ no Python para automatizar e limpar o seu código

# GERADORES
print("\n GERADORES \n")
# Nesta secção, aprenderemos como construir nossos próprios gerados com a instrução yield.
# Os geradores nos permitem gerar informação a medida que avançamos, em vez de guardar tudo na memória

# Vamos explorar um pouco mais fundo. Apredemos a criar funções com def e com a declaração return.
# As funções do gerador nos permitem escrever uma função que pode enviar de volta um valor e, em seguida, continuar de onde ele parou
# Esse tipo de função é um gerador em Python, permitindo gerar uma sequência de valores ao longo do tempo. A principal diferença na sintaxe será o uso de uma declaração yield

# Na maioria dos aspetos, uma função do gerador será muito semelhante a uma função normal. A principal diferença é quando uma função do gerador é compilada tornam-se um objeto
# que suporta um protocolo de iteração. Isso significa que quando eles são chamados em seu código, na verdade, não retornam um valor e param.
# As funções do gerador serão suspensas e retomando a execução e estado em torno do último ponto de geração de valor.
# A principal vantagem aqui é que, em vez de ter que calcular uma série inteira de valores antecipados, as funções do gerador podem ser suspensas, esse recurso é conhecido como suspensão de estado

# Função de gerador para o cubo de números
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10) :
    print(x)

# Agora, já que temos um função de gerador, não precisamos acompanhar todos os cubos que criamos
# Os geradores são os mlehores para calcular grandes conjuntos de resultados (particularmente nos cálculos que envolver os próprios loops) nos casos
# em que não queremos alocar a memória para todos os resultados ao mesmo tempo

def genfibon(n):
    '''Gera a sequencia de fibonacci até n'''
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b, a+b

for num in genfibon(10):
    print(num)

# E uma função normal, como seria?
def fibon(n):
    a = 1
    b = 1
    output = []

    for i in range(n):
        output.append(a)
        a,b = b, a+b

    return output

print(fibon(10))

# FUNÇÕES INTERNAS NEXT() E ITER()
# Uma chave para entender completamente os geradores é o next() e a função iter()

# O next() nos permite acessar o próximo elementos em uma sequência. Vamos verificar:

def simple_gen():
    for x in range(3):
        yield x

# Define um gerador simples
g = simple_gen()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
# Vai emitir um erro

# Depois de obter todos os valores do next(), isso causou um erro StopIteration. O que este erro nos informa é que todos os valores foram renderizados
# Porque não obtemos este erro com o loop for? O loop for automaticamente bloqueia esse errro e pára de ligar em seguida
# 
# Agora vamos ver como usar o iter()

s = 'hello'

# Itera sobre a string
for let in s:
    print(let)

# O código acima mostra que um objeto de string suporta iteração, mas não podemos iterar diretamente sobre ele como podemos com uma função gerador
# A função iter() nos permite fazer exatamente isso
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))

# A principal ideia é usar a palavra chave yield em uma função que fará com que a função se torne um gerador. Esta alteração pode poupar muita memória para grandes casos de uso

# MÓDULOS DE COLEÇÕES - PARTE1
print("\n MÓDULOS DE COLEÇÕES - PARTE1 \n")

# O módulo de coeções é um módulo interno que implementa tipos de dados de contêiner especializados que fornecem alternativas ao contêiners incorporados de uso geral da Python
# Nós já abordamos os conceitos básicos_ dict, list, set, tuple

# COUNTER 
print(" - COUNTER")
# Counter é uma subclasse dict que ajuda a contar objetos hash-able. Dentro disso, os elementos são armazenados como chaves de dicionários e as contagens dos objetos são armazenados como o valor

from collections import Counter
# Counter() com listas

l = [1,2,2,2,2,3,3,1,2,4,1,2,4,2,12,3,5,1,2,2,223,42,1,2,4,2,3,1,2,3,2,21]
print(Counter(l))

# Counter com stings
Counter('aadahdahsfafhashdahsda')

# Counter com palavras em uma frase
s = 'How many times does each word show up in this sentence word times each each word'

words = s.split()

Counter(words)

# Métodos com Counter()
c = Counter(words)
c.most_common(2)

# Defaultdict é um dicionários como objeto que fornece todos os métodos fornecidos pelo dicionário, mas leva o primeiro argumentos (default_factory)
# como tipo de dados padrão para o dicionário. Usar defaultdict é mais rápido do que fazer o mesmo usando o método dict.set_default
# Um defaultdict nunca gerará um KeyError. Qualquer chave que não existe obtém o valor retornao pela fábrica padrão

from collections import defaultdict
# d = {}
# d['one']
#
# ------------
# -----------
# KeyError ... etc ...

d = defaultdict(object)
d['one']

for item in d:
    print(item)

# Também pode inicializar com valores padrão
d = defaultdict(lambda: 0)
print(d['one'])

# MÓDULOS DE COLEÇÕES - PARTE2
print("\n MÓDULOS DE COLEÇÕES - PARTE2 \n")
print(" - OrderedDict")
# OrderedDict é uma subcalsse de dicionário que armazena a ordem em que seu conteúdo é adicionado

# Um exemplo de um dicionário normal
print('Normal dictionary:')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

# Um OrderedDict
from collections import OrderedDict

print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)

# Igualdade com um dicionário ordenado
# Um dicionário normal olha para seu próprio conteúdo quando testa por igualdade. Um OrderedDict também considera a ordem em que os items foram adicionados

print('Dictionaries are equal?')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

# Com um ordered dict

print('Dictionaries are equal?')

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'

d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)

# Named Tuple
# A tupla padrão usa índices numéricos para acessar seus membros, p.e.
t = (12,13,14)
print(t[0])

# Para casos de uso simples, isso geralmente é suficiente. Por outro lado, saber qual índice deve ser usado para cada valor pode levar a erros,
# especialmente se a tupla tiver muitos campos e for construída longe de onde ela é usada. Um namedtuple atribui nomes, bem como o índice numéridos, a cada membro

# Cada tipo de namedtuple é representado por sua própria classe, criado usando a função de fábrica namedtuple()
# Os argumentos são o nome da nova classe e uma string contendo os nomes dos elementos

# Basicamente, devemos pensar no namedtuple como uma maneira muito rápida de criar um novo tipo de objeto/classe com alguns campos de atributos. P.e.

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')

sam = Dog(age=2, breed='Lab', name='Sammy')

frank = Dog(age=2, breed='Shepard', name="Frankie")

# Construímos o namedtuple primeiro passando o nome do tipo de objeto (Dog) e depois passando uma string com a variedade de campos como uma string
# com espaços entre os nomes dos campos. Podemos chamar os vários atributos

print(sam)
print(sam.age)
print(sam.breed)
print(sam[0])

# DATETIME
print("\n DATE TIME\n")
# O python possui o módulo datatime para ajudar a lidar com timestamps em seu código. Os valores de tempo são representados com a classe de time
# Time têm atributos por hora, minuto, segundo e microsegundos. Eles também podem incluir informações de fuso horário.
# Os argumentos para incializar uma instância de time são opcionais, mas é improvável que o padrão de 0 seja o que você deseja

# TIME
# Vamos dar uma olhada em como podemos extrair informações de tempo do módulo datatime. Podemos criar um timestamp especificando datetime.time(hour, minute, second, microsecond)

import datetime

t = datetime.time(4, 20, 1)
# Vamos mostrar as diferenças entre os componentes

print(t)
print('hour: ', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

# Nota: Uma instância de tempo apenas mantém valores de tmepo e não uma data associada ao tempo
# Também podemos verificar os valores mínimos e máximos que uma hora do dia pode ter no módulo

print('Earliest :', datetime.time.min)
print('Latest: ', datetime.time.max)
print('Resolution: ', datetime.time.resolution)

# DATES
# o datetime também nos permiite trabalhar com timestamps de data. Os valores da data do calendário são representados com a classe date. 
# As instâncias possuem atributos por ano, mês e dia. É fácil criar uma data que represente a data de hoje usando o método today()

today = datetime.date.today()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year', today.year)
print('Mon : ', today.month)
print('Day :', today.day)

# Assim como o tempo, o intervalo de valores de data suportadoss pode ser determinado usando os atributos min e max
print('Earliest : ', datetime.date.min)
print('Latest: ', datetime.date.max)
print('Resolution: ', datetime.date.resolution)

# Outra maneira de criar novas instâncias de data é usando o método replace() de uma data já existente.
# P.e, você pode mudar o ano, deixando o dia e o mês sozinhos

d1 = datetime.date(2015,3,11)
print('d1:', d1)

d2 = d1.replate(year=1990)
print('d2:', d2)

# Operações aritméticas
# Podemos realizar operaões aritméticas em objetos de data para verificar diferenças de horário
print(d1)
print(d2)
print(d1-d2) # Vai nos dar a diferença em dias entre as duas datas. Podemos usar o método datetimme.timedelta para especificar várias unidades de horas (dia, minutos, horas, etc.)


