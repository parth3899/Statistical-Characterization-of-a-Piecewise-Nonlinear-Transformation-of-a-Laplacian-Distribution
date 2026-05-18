import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy import integrate

# ---------------------------------------------------
# PARAMETERS
# ---------------------------------------------------
N = 1_000_000       # one million samples
np.random.seed(42)  # reproducibility

# ===================================================
# STEP 1: Generate U ~ Uniform(0, 1)
# ===================================================
U = np.random.uniform(0, 1, N)

# ===================================================
# STEP 2: Transform U -> X via Inverse CDF
# ===================================================
X = np.where(
    U < 0.5,
    np.log(2 * U),          # Eq. (7): x = ln(2u)
    -np.log(2 * (1 - U))    # Eq. (8): x = -ln(2(1-u))
)

# ===================================================
# STEP 3: Transform X -> Y via piecewise law
# ===================================================
Y = np.where(X >= 0, X, 2 * X**2)

# ===================================================
# THEORETICAL PDFs
# ===================================================
u_vals = np.linspace(0, 1, 500)
f_U = np.ones_like(u_vals)

x_vals = np.linspace(-8, 8, 1000)
f_X = 0.5 * np.exp(-np.abs(x_vals))

y_vals = np.linspace(1e-4, 14, 2000)
f_Y = (0.5 * np.exp(-y_vals)
       + (1.0 / (4.0 * np.sqrt(2.0 * y_vals)))
       * np.exp(-np.sqrt(y_vals / 2.0)))

# Sanity check: integral of f_Y should equal 1
val, _ = integrate.quad(
    lambda y: (0.5 * np.exp(-y)
               + np.exp(-np.sqrt(y / 2))
               / (4 * np.sqrt(2 * y))),
    0, np.inf)
print(f"Integral of f_Y = {val:.6f}")

# ===================================================
# STEP 4: Plot
# ===================================================
fig = plt.figure(figsize=(16, 6))
gs = gridspec.GridSpec(1, 3, wspace=0.35)

# Panel 1 - U
ax1 = fig.add_subplot(gs[0])
ax1.hist(U, bins=80, density=True,
         color='steelblue', alpha=0.65,
         label='Simulated histogram')
ax1.plot(u_vals, f_U, 'r-', lw=2.2,
         label='Theoretical $f_U(u)=1$')
ax1.set_xlim(-0.05, 1.05)
ax1.set_ylim(0, 1.5)
ax1.set_xlabel('u')
ax1.set_ylabel('Density')
ax1.set_title('$U \\sim$ Uniform(0,1)')
ax1.legend()
ax1.grid(alpha=0.3)

# Panel 2 - X
ax2 = fig.add_subplot(gs[1])
ax2.hist(X, bins=120, density=True,
         color='mediumseagreen', alpha=0.65,
         label='Simulated histogram')
ax2.plot(x_vals, f_X, 'r-', lw=2.2,
         label='Theoretical $f_X(x)$')
ax2.set_xlim(-8, 8)
ax2.set_ylim(0, 0.60)
ax2.set_xlabel('x')
ax2.set_ylabel('Density')
ax2.set_title('$X \\sim$ Laplacian')
ax2.legend()
ax2.grid(alpha=0.3)

# Panel 3 - Y
ax3 = fig.add_subplot(gs[2])
ax3.hist(Y, bins=150, density=True, range=(0, 14),
         color='steelblue', alpha=0.55,
         label='Simulated histogram')
ax3.plot(y_vals, f_Y, 'r-', lw=2.2,
         label='Theoretical $f_Y(y)$')
ax3.set_xlim(-0.3, 14)
ax3.set_ylim(0, 0.60)
ax3.set_xlabel('y')
ax3.set_ylabel('Density')
ax3.set_title('Output $Y$')
ax3.legend()
ax3.grid(alpha=0.3)

plt.savefig('simulation_results.png', dpi=150, bbox_inches='tight')
plt.show()
print("Plot saved to simulation_results.png")

# ===================================================
# STEP 5: Summary statistics
# ===================================================
print(f"U: mean={np.mean(U):.4f}, std={np.std(U):.4f}")
print(f"X: mean={np.mean(X):.4f}, std={np.std(X):.4f}")
print(f"Y: mean={np.mean(Y):.4f}, std={np.std(Y):.4f}")