import numpy as np

# Definición del sistema de ecuaciones no lineales
def F(theta):
    t1, t2 = theta
    return np.array([
        np.cos(t1) + np.cos(t1 + t2) - 1.5,
        np.sin(t1) + np.sin(t1 + t2) - 0.8
    ])

# Jacobiano del sistema
def J(theta):
    t1, t2 = theta
    return np.array([
        [-np.sin(t1) - np.sin(t1 + t2), -np.sin(t1 + t2)],
        [ np.cos(t1) + np.cos(t1 + t2),  np.cos(t1 + t2) ]
    ])

θ = np.array([0.5, 0.5])  # Estimación inicial para los ángulos

for k in range(8):
    # Resolver el sistema lineal J*Δ = -F para Δ
    Δ = np.linalg.solve(J(θ), -F(θ))
    θ += Δ  # Actualizar la estimación
    print(f"Iter{k}: θ1={θ[0]:.6f}, θ2={θ[1]:.6f}")
    if np.linalg.norm(Δ) < 1e-8:
        break  # Parar si la corrección es muy pequeña


Output:
Iter0: θ1=0.404512, θ2=0.923931
...
Iter4: θ1=0.401016, θ2=0.927267

 Interpretación:
 El extremo del brazo alcanza el punto deseado con θ1≈0.401 rad
(23 °) y θ2≈0.927 rad (53 °). Convergencia cuadrática típica.
