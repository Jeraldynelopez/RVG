import dash
import plotly.graph_objs as go
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')
import numpy as np
import io
import base64

from fronted.grupo2.titulo2 import *


#Diagrama de fases 
def fases_del_suelo_vol (volumen_solidos,volumen_agua,volumen_aire,volumen_total):
  solidos = np.array([volumen_solidos])
  agua = np.array([volumen_agua])
  aire = np.array([volumen_aire])
  limites = np.array([0, solidos[0], solidos[0]+agua[0], solidos[0]+agua[0]+aire[0]])
  plt.fill_between(np.arange(0, 100), 0, solidos[0], color='brown', alpha=0.5, label='Sólidos')
  plt.fill_between(np.arange(0, 100), solidos[0], solidos[0]+agua[0], color='blue', alpha=0.5, label='Agua')
  plt.fill_between(np.arange(0, 100), solidos[0]+agua[0], solidos[0]+agua[0]+aire[0], color='gray', alpha=0.5, label='Aire')
  plt.ylim(0,volumen_total)
  plt.legend()
  plt.show()
  # Guardar la figura en un objeto BytesIO
  fig_buffer = io.BytesIO()
  plt.savefig(fig_buffer, format='png')
  plt.close()
  fig_buffer.seek(0)
  encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
  # Crear la figura HTML con Dash
  return encoded_image



def fases_del_suelo_grav (peso_solidos,peso_agua,peso_aire,peso_total):
  solidos = np.array([peso_solidos])
  agua = np.array([peso_agua])
  aire = np.array([peso_aire])
  limites = np.array([0, solidos[0], solidos[0]+agua[0], solidos[0]+agua[0]+aire[0]])
  plt.fill_between(np.arange(0, 100), 0, solidos[0], color='brown', alpha=0.5, label='Sólidos')
  plt.fill_between(np.arange(0, 100), solidos[0], solidos[0]+agua[0], color='blue', alpha=0.5, label='Agua')
  plt.fill_between(np.arange(0, 100), solidos[0]+agua[0], solidos[0]+agua[0]+aire[0], color='gray', alpha=0.5, label='Aire')
  plt.ylim(0,peso_total)
  plt.legend()
  plt.show()
  # Guardar la figura en un objeto BytesIO
  fig_buffer = io.BytesIO()
  plt.savefig(fig_buffer, format='png')
  plt.close()
  fig_buffer.seek(0)
  encoded_image = base64.b64encode(fig_buffer.getvalue()).decode()
  # Crear la figura HTML con Dash
  return encoded_image