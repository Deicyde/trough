---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.r, MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.WithoutCollisions, MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.IsNBodySolution, MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.theorem_1_1
statement: formalized
---

# Hyperbolic motions in the N-body problem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/hyperbolic-motions-in-the-n-body-problem/index.html).

## Mutual distances

For a configuration $x = (x_1, \dots, x_N) \in E^N$ of $N$ points in a
finite-dimensional real inner product space $E$ and indices $i, j$, the mutual distance of the
$i$-th and $j$-th points is $r_{ij}(x) = \lVert x_i - x_j \rVert$.

Formalized by `MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.r`, a definition declared in [WantedExt/Analysis/ViscositySolutionsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ViscositySolutionsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/hyperbolic-motions-in-the-n-body-problem/index.html#r).

## Configurations without collisions

A configuration $x = (x_1, \dots, x_N) \in E^N$ of
$N$ points in a finite-dimensional real inner product space $E$ is without collisions if
$r_{ij}(x) = \lVert x_i - x_j \rVert \neq 0$ for all $i \neq j$.

Formalized by `MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.WithoutCollisions`, a definition declared in [WantedExt/Analysis/ViscositySolutionsWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ViscositySolutionsWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/hyperbolic-motions-in-the-n-body-problem/index.html#without-collisions).

## Solutions of the $N$-body problem

Let $E$ be a finite-dimensional real inner product
space, let $N$ be a natural number, give $E^N$ the inner product
$\langle u, v \rangle = \sum_i \langle u_i, v_i \rangle$, and let
$m = (m_1, \dots, m_N) \in \mathbb{R}^N$ be masses. Let
$U(y) = \sum_{i < j} m_i m_j \lVert y_i - y_j \rVert^{-1}$ be the Newtonian potential on $E^N$,
and for $f : E^N \to \mathbb{R}$ let $\nabla_m f(y) \in E^N$ be the mass-weighted gradient, with
components $(\nabla_m f(y))_i = m_i^{-1} (\nabla f(y))_i$, where $\nabla f$ is the gradient of $f$.
A curve $x : \mathbb{R} \to E^N$ is a solution of the $N$-body problem with masses $m$ if $x$ is
$C^2$ on $(0, \infty)$, $x$ is continuous at $0$, and $x''(t) = \nabla_m U(x(t))$ for every
$t > 0$.

By convention $0^{-1} = 0$ here, so a collision term contributes $0$ to $U$ and a zero mass
gives a zero component of $\nabla_m f$. Moreover $\nabla f(y) = 0$ at every point $y$ where $f$
is not differentiable; for instance, a curve that stays at a collision with $x'' = 0$ can be a
solution in this sense.

Formalized by `MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.IsNBodySolution`, a structure declared in [WantedExt/Analysis/ViscositySolutionsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ViscositySolutionsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/hyperbolic-motions-in-the-n-body-problem/index.html#is-nbody-solution).

## Maderna–Venturelli theorem on hyperbolic motions

Let $E$ be a finite-dimensional real
inner product space of dimension at least $2$, let $N$ be a natural number, and let
$m = (m_1, \dots, m_N)$ be positive masses. Let $x_0 \in E^N$, let $a \in E^N$ be a configuration
without collisions with $\lVert a \rVert_m = 1$, where
$\lVert a \rVert_m = \bigl(\sum_i m_i \lVert a_i \rVert^2\bigr)^{1/2}$, and let $h > 0$. Then
there are a solution $x : \mathbb{R} \to E^N$ of the $N$-body problem with masses $m$ and a
function $\varepsilon : \mathbb{R} \to E^N$ with $\lVert \varepsilon(t) \rVert / t \to 0$ as
$t \to \infty$ such that $x(0) = x_0$, the configuration $x(t)$ is without collisions for every
$t > 0$, and $x(t) = \sqrt{2h}\, t\, a + \varepsilon(t)$ for every $t \ge 0$.

## Sources

- E. Maderna and A. Venturelli, `Viscosity solutions and hyperbolic motions: a new PDE method for the N-body problem`, Annals of Math, 192 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_viscosity_solutions` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.ViscositySolutionsWanted.ViscositySolutions.theorem_1_1` is written with `theorem_wanted` in [WantedExt/Analysis/ViscositySolutionsWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ViscositySolutionsWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/hyperbolic-motions-in-the-n-body-problem/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperbolic motions in the N-body problem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/hyperbolic-motions-in-the-n-body-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/ordinary-differential-equations/hyperbolic-motions-in-the-n-body-problem)
