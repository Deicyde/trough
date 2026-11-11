---
declaration: section
origin: cited
lean: MathlibExt.Analysis.PoincareSiegelWanted.ComplexAnalysis.IsDiophantine, MathlibExt.Analysis.PoincareSiegelWanted.ComplexAnalysis.poincare_siegel
statement: formalized
---

# Siegel linearization theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/siegel-linearization-theorem/index.html).

## Diophantine real numbers

A real number $\alpha$ is Diophantine if there are real numbers
$C > 0$ and $\tau$ such that $C / |q|^{\tau} \le |\alpha - p/q|$ for all integers $p$ and $q$
with $q \neq 0$.

Any such exponent $\tau$ is at least $2$, by Dirichlet's approximation theorem. A Diophantine
$\alpha$ is irrational, so $e^{2\pi i \alpha}$ is not a root of unity.

Formalized by `MathlibExt.Analysis.PoincareSiegelWanted.ComplexAnalysis.IsDiophantine`, a definition declared in [WantedExt/Analysis/PoincareSiegelWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/PoincareSiegelWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/siegel-linearization-theorem/index.html#is-diophantine).

## Poincaré–Siegel linearisation theorem

Let $\alpha$ be a Diophantine real number and let
$\lambda = e^{2\pi i \alpha}$. If $f : \mathbb{C} \to \mathbb{C}$ is analytic at $0$ with
$f(0) = 0$ and $f'(0) = \lambda$, then there is a function $u : \mathbb{C} \to \mathbb{C}$,
analytic at $0$ with $u(0) = 0$ and $u'(0) = 1$, such that $f(u(z)) = u(\lambda z)$ for all $z$
in some neighbourhood of $0$.

## Sources

- C. L. Siegel, *Iteration of analytic functions*, Annals of Math. 43 (1942), 607-612. Earlier formal-power-series version: H. Poincaré thèse (1879). Listed as §83 (additional statement 1) in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `poincare_siegel_linearisation` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.PoincareSiegelWanted.ComplexAnalysis.poincare_siegel` is written with `theorem_wanted` in [WantedExt/Analysis/PoincareSiegelWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/PoincareSiegelWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/siegel-linearization-theorem/index.html#poincare-siegel).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Siegel linearization theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/siegel-linearization-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/complex-dynamics/siegel-linearization-theorem)
