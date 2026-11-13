---
declaration: section
origin: cited
lean: MathlibExt.Analysis.EulerLagrangeWanted.Analysis.lagrangianPartialX, MathlibExt.Analysis.EulerLagrangeWanted.Analysis.lagrangianPartialV, MathlibExt.Analysis.EulerLagrangeWanted.Analysis.IsVariationalExtremum, MathlibExt.Analysis.EulerLagrangeWanted.Analysis.euler_lagrange_equation
statement: formalized
---

# Euler–Lagrange equation

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/euler-lagrange-equation/index.html).

## Partial derivative of the Lagrangian in position

For a real function $L(t, y, v)$
of three real variables, a function $x : \mathbb{R} \to \mathbb{R}$ and a real number $t$, this
is the value $\frac{\partial L}{\partial y}(t, x(t), x'(t))$, the derivative at $y = x(t)$ of
the function $y \mapsto L(t, y, x'(t))$.

By convention, a derivative that does not exist is taken to be $0$, both for $x'(t)$ and for
the derivative in $y$.

Formalized by `MathlibExt.Analysis.EulerLagrangeWanted.Analysis.lagrangianPartialX`, a definition declared in [WantedExt/Analysis/EulerLagrangeWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EulerLagrangeWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/euler-lagrange-equation/index.html#lagrangian-partial-x).

## Partial derivative of the Lagrangian in velocity

For a real function $L(t, y, v)$
of three real variables, a function $x : \mathbb{R} \to \mathbb{R}$ and a real number $t$, this
is the value $\frac{\partial L}{\partial v}(t, x(t), x'(t))$, the derivative at $v = x'(t)$ of
the function $v \mapsto L(t, x(t), v)$.

By convention, a derivative that does not exist is taken to be $0$, both for $x'(t)$ and for
the derivative in $v$.

Formalized by `MathlibExt.Analysis.EulerLagrangeWanted.Analysis.lagrangianPartialV`, a definition declared in [WantedExt/Analysis/EulerLagrangeWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EulerLagrangeWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/euler-lagrange-equation/index.html#lagrangian-partial-v).

## Variational extremum

Let $a, b$ be real numbers and let $L(t, y, v)$
be a real function of three real variables. A function $x : \mathbb{R} \to \mathbb{R}$ is a
variational extremum of the action of $L$ on $(a, b)$ if $x$ is continuously differentiable and,
for every infinitely differentiable function $h : \mathbb{R} \to \mathbb{R}$ of compact support
whose closed support lies in the open interval $(a, b)$, the derivative at $\varepsilon = 0$ of

$$
\varepsilon \mapsto \int_{(a, b)}
L\big(t, x(t) + \varepsilon h(t), x'(t) + \varepsilon h'(t)\big)\,dt
$$

is $0$.

By convention, a derivative that does not exist is taken to be $0$, and so is the integral of a
function that is not integrable.

Formalized by `MathlibExt.Analysis.EulerLagrangeWanted.Analysis.IsVariationalExtremum`, a definition declared in [WantedExt/Analysis/EulerLagrangeWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EulerLagrangeWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/euler-lagrange-equation/index.html#is-variational-extremum).

## Euler–Lagrange equation

Let $a < b$ be real numbers, let $L(t, y, v)$ be a real function
of three real variables that is twice continuously differentiable on $\mathbb{R}^3$, and let
$x : \mathbb{R} \to \mathbb{R}$ be twice continuously differentiable. Write
$\partial L / \partial y$ and $\partial L / \partial v$ for the partial derivatives of $L$ in its
second and third arguments. If $x$ is a variational extremum of the action of $L$ on $(a, b)$,
then for every $t \in (a, b)$

$$
\frac{\partial L}{\partial y}(t, x(t), x'(t))
= \frac{d}{ds}\Big|_{s = t} \frac{\partial L}{\partial v}(s, x(s), x'(s)).
$$

## Sources

- L. Euler (1744) and J.-L. Lagrange (1755). Listed as §44 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `euler_lagrange_equation` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.EulerLagrangeWanted.Analysis.euler_lagrange_equation` is written with `theorem_wanted` in [WantedExt/Analysis/EulerLagrangeWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/EulerLagrangeWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/euler-lagrange-equation/index.html#euler-lagrange-equation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler–Lagrange equation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/euler-lagrange-equation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/convex-analysis-and-variations/euler-lagrange-equation)
