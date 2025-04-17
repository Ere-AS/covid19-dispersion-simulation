import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Patch
from matplotlib.widgets import Button, TextBox

# Estados
SANO = 0
INFECTADO = 1
RECUPERADO = 2
MUERTO = 3

colores = {
    SANO: '#3b82f6',
    INFECTADO: '#ef4444',
    RECUPERADO: '#22c55e',
    MUERTO: '#fefefe'
}

# Probabilidad general de infección
prob_infeccion = 0.3

class Persona:
    def __init__(self, x, y, vulnerable=False):
        self.x = x
        self.y = y
        self.estado = SANO
        self.vulnerable = vulnerable
        self.usa_cubrebocas = random.random() < 0.5
        self.infectado_desde = -1

    def mover(self, ancho, alto):
        if self.estado == MUERTO:
            return
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        self.x = max(0, min(ancho - 1, self.x + dx))
        self.y = max(0, min(alto - 1, self.y + dy))

    def actualizar_estado(self, prob_recuperacion, prob_muerte, dia_actual):
        if self.estado == INFECTADO and self.infectado_desde >= 0 and dia_actual > self.infectado_desde:
            r = random.random()
            if r < prob_muerte:
                self.estado = MUERTO
            elif r < prob_muerte + prob_recuperacion:
                self.estado = RECUPERADO

class Campo:
    def __init__(self, ancho, alto, num_personas, porcentaje_vulnerables):
        self.ancho = ancho
        self.alto = alto
        self.personas = []
        self.crear_personas(num_personas, porcentaje_vulnerables)

    def crear_personas(self, n, porcentaje_vulnerables):
        for _ in range(n):
            x = random.randint(0, self.ancho - 1)
            y = random.randint(0, self.alto - 1)
            vulnerable = random.random() < porcentaje_vulnerables
            self.personas.append(Persona(x, y, vulnerable))

    def infectar_inicial(self, cantidad=1, dia_actual=0):
        for p in self.personas:
            p.estado = SANO
            p.infectado_desde = -1
        infectados = random.sample(self.personas, cantidad)
        for p in infectados:
            p.estado = INFECTADO
            p.infectado_desde = dia_actual

    def simular_paso(self, dia_actual, radio=1, prob_recuperacion=0.05, prob_muerte=0.02):
        for p in self.personas:
            p.mover(self.ancho, self.alto)

        for p in self.personas:
            if p.estado == INFECTADO:
                for otra in self.personas:
                    if otra.estado == SANO:
                        distancia = abs(p.x - otra.x) + abs(p.y - otra.y)
                        if distancia <= radio:
                            if random.random() < prob_infeccion:
                                otra.estado = INFECTADO
                                otra.infectado_desde = dia_actual

        for p in self.personas:
            p.actualizar_estado(prob_recuperacion, prob_muerte, dia_actual)

    def obtener_posiciones_y_colores(self):
        xs, ys, cs, ec = [], [], [], []
        for p in self.personas:
            xs.append(p.x)
            ys.append(p.y)
            cs.append(colores[p.estado])
            ec.append('white' if p.usa_cubrebocas else 'black')
        return xs, ys, cs, ec

    def contar_estados(self):
        conteo = {SANO: 0, INFECTADO: 0, RECUPERADO: 0, MUERTO: 0}
        for p in self.personas:
            conteo[p.estado] += 1
        return conteo

campo = Campo(ancho=30, alto=30, num_personas=120, porcentaje_vulnerables=0.3)
campo.infectar_inicial(cantidad=5, dia_actual=0)

fig, ax = plt.subplots(figsize=(12, 12))
fig.canvas.manager.set_window_title("Modelo de dispersión COVID-19")
sc = ax.scatter([], [], s=120, alpha=1.0)
ax.set_xlim(0, campo.ancho)
ax.set_ylim(0, campo.alto)
ax.set_facecolor("black")
ax.set_xticks([])
ax.set_yticks([])

leyenda = [
    Patch(color=colores[SANO], label='Sano'),
    Patch(color=colores[INFECTADO], label='Infectado'),
    Patch(color=colores[RECUPERADO], label='Recuperado'),
    Patch(color=colores[MUERTO], label='Muerto'),
    Patch(facecolor='none', edgecolor='white', label='Usa cubrebocas')
]
ax.legend(handles=leyenda, loc='upper right', frameon=True, facecolor='black', edgecolor='white', labelcolor='white')

titulo = ax.text(0.5, 1.01, "Simulación de propagación del COVID-19", transform=ax.transAxes,
                 ha='center', fontsize=13, color='white', weight='bold')
texto_info = ax.text(0.02, 0.02, "", transform=ax.transAxes, fontsize=11, color='white', va='bottom')

ani = None
start_ax = plt.axes([0.4, 0.92, 0.2, 0.05])
start_button = Button(start_ax, 'Iniciar Simulación', color='gray', hovercolor='lightgreen')

ax.text(0.01, 0.97, 'Probabilidad de contagio', transform=fig.transFigure, fontsize=10, color='white')
box_prob_ax = plt.axes([0.01, 0.93, 0.2, 0.05])
box_prob = TextBox(box_prob_ax, '', initial=str(prob_infeccion))

dia_simulado = [0]

def update(frame):
    global ani, campo
    dia_actual = dia_simulado[0]
    campo.simular_paso(dia_actual)
    xs, ys, cs, ec = campo.obtener_posiciones_y_colores()
    sc.set_offsets(list(zip(xs, ys)))
    sc.set_facecolor(cs)
    sc.set_edgecolor(ec)

    conteo = campo.contar_estados()
    texto_info.set_text(
        f"Día: {dia_actual + 1} | Contagio: {prob_infeccion:.2f} | "
        f"Sanos: {conteo[SANO]} | Infectados: {conteo[INFECTADO]} | Recuperados: {conteo[RECUPERADO]} | Muertos: {conteo[MUERTO]}"
    )

    if conteo[INFECTADO] == 0:
        print("✅ Simulación detenida: No quedan personas infectadas.")
        ani.event_source.stop()
        start_button.ax.set_visible(True)
        dia_simulado[0] = 0
        campo = Campo(ancho=30, alto=30, num_personas=120, porcentaje_vulnerables=0.3)
        campo.infectar_inicial(cantidad=5, dia_actual=0)
        texto_info.set_text("Simulación finalizada. Puedes iniciar otra con un nuevo valor de contagio.")
        texto_info.set_text("Simulación finalizada. Puedes iniciar otra con un nuevo valor de contagio.")

    dia_simulado[0] += 1
    return sc, texto_info

def iniciar(event):
    global ani, prob_infeccion
    try:
        prob_infeccion = float(box_prob.text)
    except ValueError:
        print(" Error: Ingresa un valor numérico para la probabilidad de contagio")
        return
    ani = animation.FuncAnimation(fig, update, frames=50, interval=1000, blit=True)
    start_button.ax.set_visible(False)
    plt.draw()

start_button.on_clicked(iniciar)
plt.tight_layout()
plt.show()
