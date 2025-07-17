from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib.figure import Figure
from matplotlib.patches import Polygon

class MatplotlibWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Crear figura y ejes
        fig = Figure()
        ax = fig.add_subplot(111)

        # Coordenadas del triángulo
        triangle = [[0, 0], [1, 0], [0.5, 1]]

        # Crear polígono y agregar al gráfico
        polygon = Polygon(triangle, closed=True, color='skyblue', edgecolor='black')
        ax.add_patch(polygon)

        # Ajustar límites de los ejes
        ax.set_xlim(-0.5, 1.5)
        ax.set_ylim(-0.5, 1.5)
        ax.set_aspect('equal')

        # Agregar la figura a la interfaz de Kivy
        self.add_widget(FigureCanvasKivyAgg(fig))

class MiApp(App):
    def build(self):
        return MatplotlibWidget()

if __name__ == '__main__':
    MiApp().run()
