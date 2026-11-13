---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HeatKernelWanted.Analysis.ODE.heatSolution, MathlibExt.Analysis.HeatKernelWanted.Analysis.ODE.heat_kernel_solves_heat_equation
statement: formalized
---

# Heat equation

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/heat-equation/index.html).

## Heat-kernel solution

For $f\colon \mathbb{R} \to \mathbb{R}$, the heat solution
$u(t, x)$ of $f$ is given for $t > 0$ by

$$u(t, x) = (4 \pi t)^{-1/2} \int_{\mathbb{R}} e^{-(x - y)^2/(4t)} f(y) \, dy$$

and by $u(t, x) = f(x)$ for $t \le 0$.

The integral is the Lebesgue integral, taken to be $0$ when the integrand is not integrable. The
value for $t \le 0$ only makes $u$ defined for all real $t$ and $x$; the heat equation statement
constrains $u$ only for $t > 0$.

Formalized by `MathlibExt.Analysis.HeatKernelWanted.Analysis.ODE.heatSolution`, a definition declared in [WantedExt/Analysis/HeatKernelWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HeatKernelWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/heat-equation/index.html#heat-solution).

## The Gaussian heat kernel solves the heat equation

Let $f\colon \mathbb{R} \to \mathbb{R}$
be continuous and bounded, and let $u(t, x)$ be the heat solution of $f$. Then for every
$t > 0$ and every $x \in \mathbb{R}$ there are a function $u_x\colon \mathbb{R} \to \mathbb{R}$
and a real number $u_{xx}$ such that $u(t, \cdot)$ has derivative $u_x(y)$ at every
$y \in \mathbb{R}$, $u_x$ has derivative $u_{xx}$ at $x$, and $u(\cdot, x)$ has derivative
$u_{xx}$ at $t$; that is, $\partial_t u = \partial_x^2 u$ on $(0, \infty) \times \mathbb{R}$.
Moreover, for every $x \in \mathbb{R}$, $u(t, x) \to f(x)$ as $t \to 0$ from above.

## Sources

- Classical heat-equation theory. Problem `heat_kernel_solves_heat_equation` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.HeatKernelWanted.Analysis.ODE.heat_kernel_solves_heat_equation` is written with `theorem_wanted` in [WantedExt/Analysis/HeatKernelWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/HeatKernelWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/heat-equation/index.html#heat-kernel-solves-heat-equation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Heat equation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/partial-differential-equations/heat-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/partial-differential-equations/heat-equation)
