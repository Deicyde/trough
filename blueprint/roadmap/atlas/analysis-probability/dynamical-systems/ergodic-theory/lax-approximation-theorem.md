---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.Torus, MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.VolumePreservingEquiv, MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.deltaDist, MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.ToralDynamicalSystem, MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.ToralDynamicalSystem.toVolumePreservingEquiv, MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.cube, MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.cubeShift, MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.IsCyclicCubeExchange
statement: formalized
---

# Lax approximation theorem

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html).

## Torus

For a natural number $d$, the $d$-dimensional torus is
$\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$, the product of $d$ copies of the circle
$\mathbb{R}/\mathbb{Z}$.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.Torus`, an abbreviation declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#torus).

## Volume-preserving transformations of the torus

Let $d$ be a natural number. A
volume-preserving transformation of the torus $\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$ is a
bijection $T$ of $\mathbb{T}^d$ such that $T$ and $T^{-1}$ are measurable and $T$ preserves
the volume measure.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.VolumePreservingEquiv`, a structure declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#volume-preserving-equiv).

## Essential-supremum distance between volume-preserving maps

Let $d$ be a natural
number and let $T$ and $S$ be measurable, invertible, volume-preserving transformations of the
torus $\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$. Let $\rho$ be the distance on $\mathbb{T}^d$
given by the maximum over the coordinates of the distance on the circle $\mathbb{R}/\mathbb{Z}$
(taken to be $0$ when $d = 0$). The distance $\delta(T, S) \in [0, \infty]$ is the essential
supremum, with respect to the volume measure, of the function $x \mapsto \rho(T x, S x)$.

This is Knill's metric $\delta$.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.deltaDist`, a definition declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#delta-dist).

## Toral dynamical system

Let $d$ be a natural number. A toral dynamical system on the
torus $\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$ is a homeomorphism of $\mathbb{T}^d$ that
preserves the volume measure.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.ToralDynamicalSystem`, a structure declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#toral-dynamical-system).

## Toral dynamical systems as volume-preserving transformations

Let $d$ be a natural
number. A volume-preserving homeomorphism $T$ of the torus
$\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$ is regarded as a measurable, invertible,
volume-preserving transformation of $\mathbb{T}^d$: the same map, with its inverse, viewed as
a measurable equivalence.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.ToralDynamicalSystem.toVolumePreservingEquiv`, a definition declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#to-volume-preserving-equiv).

## Grid cube in the torus

Let $n$ and $d$ be natural numbers and let
$k = (k_0, \dots, k_{d-1})$ with each $k_i \in \{0, \dots, n-1\}$. The grid cube with
index $k$ is the set of points $x$ of the torus $\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$
such that, for every $i < d$, the coordinate $x_i$ is the class modulo $1$ of some real
number $r$ with $k_i/n \le r < (k_i + 1)/n$.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.cube`, a definition declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#cube).

## Coordinate shift between grid cubes

Let $n$ and $d$ be natural numbers, let
$\sigma$ be a permutation of the index set $\{0, \dots, n-1\}^d$, let $k$ be an index and
let $i < d$. The shift along axis $i$ determined by $\sigma$ and $k$ is the point
$(\sigma(k)_i - k_i)/n$ of the circle $\mathbb{R}/\mathbb{Z}$, that is, the class modulo $1$
of this real number.

For an index $j$, the grid cube with index $j$ is the set of points of the torus
$(\mathbb{R}/\mathbb{Z})^d$ whose $m$-th coordinate is the class of a real number in
$[j_m/n, (j_m + 1)/n)$ for every $m < d$. For $n > 0$, translating the $m$-th coordinate of
each point of the grid cube with index $k$ by the shift along axis $m$, for every $m < d$,
carries that cube onto the grid cube with index $\sigma(k)$.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.cubeShift`, a definition declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#cube-shift).

## Cyclic cube exchange

Let $n$ and $d$ be natural numbers. For an index
$k \in \{0, \dots, n-1\}^d$, the grid cube with index $k$ is the set of points of the torus
$\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$ whose $i$-th coordinate is the class of a real
number in $[k_i/n, (k_i + 1)/n)$ for every $i < d$. A measurable, invertible,
volume-preserving transformation $T$ of $\mathbb{T}^d$ is a cyclic cube exchange with $n$
subdivisions if $n > 0$ and there is a permutation $\sigma$ of $\{0, \dots, n-1\}^d$ that is
a single cycle moving every index, such that for every index $k$, every point $x$ of the
grid cube with index $k$ and every $i < d$, we have
$(T x)_i = x_i + (\sigma(k)_i - k_i)/n$ in $\mathbb{R}/\mathbb{Z}$. Thus $T$ translates each
grid cube $k$ rigidly onto the grid cube $\sigma(k)$.

Formalized by `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.IsCyclicCubeExchange`, a definition declared in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#is-cyclic-cube-exchange).

## Lax's approximation theorem

Let $d \ge 1$ be a natural number and let $T$ be a toral
dynamical system on the torus $\mathbb{T}^d = (\mathbb{R}/\mathbb{Z})^d$, regarded as a
measurable, invertible, volume-preserving transformation of $\mathbb{T}^d$. Then for every
$\varepsilon \in (0, \infty]$ there are a natural number $n$ and a measurable, invertible,
volume-preserving transformation $S$ of $\mathbb{T}^d$ such that $S$ is a cyclic cube exchange
with $n$ subdivisions and $\delta(T, S) < \varepsilon$, where $\delta$ is the
essential-supremum distance between volume-preserving maps.

## Sources

- P. D. Lax, *Approximation of measure preserving transformations*, Comm. Pure Appl. Math. 24 (1971). Knill, *Some fundamental theorems in mathematics*, §110. Problem `lax_approximation` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.LaxApproximationWanted.Dynamics.LaxApproximation.lax_approximation` is written with `theorem_wanted` in [WantedExt/Dynamics/LaxApproximationWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/LaxApproximationWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html#lax-approximation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lax approximation theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/ergodic-theory/lax-approximation-theorem)
