import turtle as tr

#Criar a tela
wn = tr.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("gray")
wn.title("Snake")
wn.tracer(0)

#Criar a cobra
def instanciarCobra(parte):
    parte.speed(0)
    parte.shape("square")
    parte.color("Green")
    parte.penup()
    parte.Velocidade = [0, 0, 0]
    parte.dx = 0
    parte.dy = 0

cabeca = tr.Turtle()
cobra = [cabeca]

instanciarCobra(cobra[0])

#Cria a movimentação da cobra
def movimentacao(objeto):
    posx = objeto.xcor()
    posy = objeto.ycor()
    posx += objeto.Velocidade[0] * objeto.Velocidade[2]
    posy += objeto.Velocidade[1] * objeto.Velocidade[2]
    objeto.setx(posx)
    objeto.sety(posy)

#altera a direção das partes da cobra
def alter(objeto, x, y):
    objeto.dx = x
    objeto.dy = y

wn.listen()

#Cria o alimento e o crescimento da cobra
#Cria a mecânica de morte

#loop principal do jogo:
while True:
    movimentacao(cobra[0])
    wn.update()