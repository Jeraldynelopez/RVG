#import dash
#import plotly.graph_objs as go
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')
import numpy as np
import io
import base64
import time
import math

from fronted.grupo2.titulo2 import *

#Diagrama de fases 
def fases_del_suelo_vol(volumen_solidos, volumen_agua, volumen_aire):
  v_solidos = np.array([volumen_solidos])
  v_agua = np.array([volumen_agua])
  v_aire = np.array([volumen_aire])
  v_limites = np.array([0, v_solidos[0], v_solidos[0]+v_agua[0], v_solidos[0]+v_agua[0]+v_aire[0]])
  plt.fill_between(np.arange(0, 100), 0, v_solidos[0], color='brown', alpha=0.9, label='Sólidos')
  plt.fill_between(np.arange(0, 100), v_solidos[0], v_solidos[0]+v_agua[0], color='blue', alpha=0.6, label='Agua')
  plt.fill_between(np.arange(0, 100), v_solidos[0]+v_agua[0], v_solidos[0]+v_agua[0]+v_aire[0], color='gray', alpha=0.5, label='Aire')
  plt.ylim(0, v_limites[-1])  # Utiliza el último elemento de v_limites como límite superior del eje y
  plt.legend()
  fig_buffer = io.BytesIO()
  plt.savefig(fig_buffer, format='png')
  plt.close()
  fig_buffer.seek(0)
  encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
  return encoded_image



def fases_del_suelo_grav(peso_solidos, peso_agua, peso_aire):
  p_solidos = np.array([peso_solidos])
  p_agua = np.array([peso_agua])
  p_aire = np.array([peso_aire])
  p_limites = np.array([0, p_solidos[0], p_solidos[0]+p_agua[0], p_solidos[0]+p_agua[0]+p_aire[0]])
  plt.fill_between(np.arange(0, 100), 0, p_solidos[0], color='brown', alpha=0.8, label='Sólidos')
  plt.fill_between(np.arange(0, 100), p_solidos[0], p_solidos[0]+p_agua[0], color='blue', alpha=0.9, label='Agua')
  plt.fill_between(np.arange(0, 100), p_solidos[0]+p_agua[0], p_solidos[0]+p_agua[0]+p_aire[0], color='gray', alpha=0.2, label='Aire')
  plt.ylim(0, p_limites[-1])
  plt.legend()
  fig_buffer = io.BytesIO()
  plt.savefig(fig_buffer, format='png')
  plt.close()
  fig_buffer.seek(0)
  encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
  return encoded_image
