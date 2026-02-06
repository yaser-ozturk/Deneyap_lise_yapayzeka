import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# ---------- GİRİŞ / ÇIKIŞ TANIMLARI ----------
bulasik_miktari = ctrl.Antecedent(np.arange(0, 100, 1), 'bulaşık miktarı')
kirlilik = ctrl.Antecedent(np.arange(0, 100, 1), 'kirlilik seviyesi')
yikama = ctrl.Consequent(np.arange(0, 180, 1), 'yıkama süresi')

# ---------- MEMBERSHIP FUNCTION ----------
bulasik_miktari['az'] = fuzz.trimf(bulasik_miktari.universe, [0, 0, 30])
bulasik_miktari['normal'] = fuzz.trimf(bulasik_miktari.universe, [10, 30, 60])
bulasik_miktari['çok'] = fuzz.trimf(bulasik_miktari.universe, [50, 60, 100])

kirlilik['az'] = fuzz.trimf(kirlilik.universe, [0, 0, 30])
kirlilik['normal'] = fuzz.trimf(kirlilik.universe, [10, 30, 60])
kirlilik['çok'] = fuzz.trimf(kirlilik.universe, [50, 60, 100])

yikama['kısa'] = fuzz.trimf(yikama.universe, [0, 0, 50])
yikama['normal'] = fuzz.trimf(yikama.universe, [40, 50, 100])
yikama['uzun'] = fuzz.trimf(yikama.universe, [60, 80, 180])

# ---------- KURALLAR ----------
rules = [
    ctrl.Rule(bulasik_miktari['az'] & kirlilik['az'], yikama['kısa']),
    ctrl.Rule(bulasik_miktari['normal'] & kirlilik['az'], yikama['normal']),
    ctrl.Rule(bulasik_miktari['çok'] & kirlilik['az'], yikama['normal']),
    ctrl.Rule(bulasik_miktari['az'] & kirlilik['normal'], yikama['normal']),
    ctrl.Rule(bulasik_miktari['normal'] & kirlilik['normal'], yikama['uzun']),
    ctrl.Rule(bulasik_miktari['çok'] & kirlilik['normal'], yikama['uzun']),
    ctrl.Rule(bulasik_miktari['az'] & kirlilik['çok'], yikama['normal']),
    ctrl.Rule(bulasik_miktari['normal'] & kirlilik['çok'], yikama['uzun']),
    ctrl.Rule(bulasik_miktari['çok'] & kirlilik['çok'], yikama['uzun']),
]

system = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(system)

# ---------- GİRİŞ DEĞERLERİ ----------
sim.input['bulaşık miktarı'] = 50
sim.input['kirlilik seviyesi'] = 80
sim.compute()

print("Yıkama Süresi:", sim.output['yıkama süresi'])

# ---------- ÇİZİMLER ----------
bulasik_miktari.view(sim=sim)
kirlilik.view(sim=sim)
yikama.view(sim=sim)

plt.show()
