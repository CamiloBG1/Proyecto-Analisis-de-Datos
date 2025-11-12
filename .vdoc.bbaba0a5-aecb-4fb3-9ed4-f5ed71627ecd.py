# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
import numpy as np
from janitor import clean_names
from dplython import *
import matplotlib.pyplot as plt
import seaborn as sns
#
#
#
#
usuarios = pd.read_excel("crecimiento_parque_automotor.xlsx",sheet_name="Cuentas").clean_names()

consumo = pd.read_excel("crecimiento_parque_automotor.xlsx",sheet_name="Consumo").clean_names()
#
#
#
