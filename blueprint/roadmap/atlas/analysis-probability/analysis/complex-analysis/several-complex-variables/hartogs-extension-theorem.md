---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Complex.HartogsWanted.continuousOn_fderiv_of_differentiableOn, MathlibExt.Analysis.Complex.HartogsWanted.barDeriv, MathlibExt.Analysis.Complex.HartogsWanted.barDeriv_eq_zero_of_differentiableAt, MathlibExt.Analysis.Complex.HartogsWanted.differentiableAt_of_barDeriv_eq_zero, MathlibExt.Analysis.Complex.HartogsWanted.exists_differentiable_barDeriv_eq_of_hasCompactSupport, MathlibExt.Analysis.Complex.HartogsWanted.hartogs_extension
statement: formalized
proof: formalized
---

# Hartogs extension theorem

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html).

## Holomorphic functions on open subsets of ℂⁿ have continuous derivative

Let $n \in
\mathbb{N}$, let $s$ be an open subset of $\mathbb{C}^n$ and let $f : \mathbb{C}^n \to \mathbb{C}$
be complex differentiable at every point of $s$. Then the complex derivative $x \mapsto Df(x)$,
with values in the complex linear maps $\mathbb{C}^n \to \mathbb{C}$, is continuous on $s$. Here
$\mathbb{C}^n$ carries the Euclidean norm.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.continuousOn_fderiv_of_differentiableOn`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsExtension.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsExtension.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html#continuous-on-fderiv-of-differentiable-o).

## The Wirtinger derivative with respect to z̄

For $f : \mathbb{C} \to \mathbb{C}$ and
$z \in \mathbb{C}$, the Wirtinger derivative of $f$ at $z$ is
$\frac{\partial f}{\partial \bar z}(z) = \frac{1}{2}\bigl(Df(z)(1) + i\,Df(z)(i)\bigr)$, where
$Df(z)$ is the real derivative of $f$ at $z$, taken to be $0$ when $f$ is not real differentiable
at $z$. When $f$ is real differentiable at $z$, this equals
$\frac{1}{2}\bigl(\frac{\partial f}{\partial x}(z) + i\,\frac{\partial f}{\partial y}(z)\bigr)$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.barDeriv`, a definition declared in [MathlibExt/Analysis/Complex/HartogsExtension.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsExtension.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html#bar-deriv).

## Vanishing of the Wirtinger derivative at points of complex differentiability

Let
$f : \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$. If $f$ is complex differentiable at $z$,
then the Wirtinger derivative $\partial f / \partial \bar z$ of $f$ vanishes at $z$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.barDeriv_eq_zero_of_differentiableAt`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsExtension.lean, line 887](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsExtension.lean#L887). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html#bar-deriv-eq-zero-of-differentiable-at).

## Cauchy–Riemann criterion for complex differentiability

Let $f : \mathbb{C} \to
\mathbb{C}$ and $z \in \mathbb{C}$. If $f$ is real differentiable at $z$ and its Wirtinger
derivative $\partial f / \partial \bar z$ vanishes at $z$, then $f$ is complex differentiable at
$z$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.differentiableAt_of_barDeriv_eq_zero`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsExtension.lean, line 898](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsExtension.lean#L898). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html#differentiable-at-of-bar-deriv-eq-zero).

## Solving the ∂̄-equation for compactly supported C¹ data

Let $g : \mathbb{C} \to
\mathbb{C}$ be real differentiable on all of $\mathbb{C}$, with continuous real derivative and
compact support. Then there is a function $u : \mathbb{C} \to \mathbb{C}$, real differentiable on
all of $\mathbb{C}$, whose Wirtinger derivative satisfies
$\frac{\partial u}{\partial \bar z}(z) = g(z)$ for every $z \in \mathbb{C}$.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.exists_differentiable_barDeriv_eq_of_hasCompactSupport`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsExtension.lean, line 1417](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsExtension.lean#L1417). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html#exists-differentiable-bar-deriv-eq-of-ha).

## Hartogs extension theorem

Let $n \ge 2$, let $U \subseteq \mathbb{C}^n$ be open and
connected, and let $K \subseteq U$ be compact with $U \setminus K$ connected. Then for every
function $f : \mathbb{C}^n \to \mathbb{C}$ that is holomorphic on $U \setminus K$ there is a
function $F : \mathbb{C}^n \to \mathbb{C}$ that is holomorphic on $U$ and agrees with $f$ on
$U \setminus K$. Here $\mathbb{C}^n$ carries the Euclidean norm.

Proof: The compactly supported Cauchy–Green equation in one coordinate, combined with a smooth
cutoff and one-variable identity continuation.

## Sources

- Hartogs extension phenomenon, F. Hartogs, Math. Ann. 62 (1906); see Hörmander, An Introduction to Complex Analysis in Several Variables; Lean is ℂⁿ n ≥ 2 finite-dimensional form via EuclideanSpace ℂ (Fin n) with U open connected K compact U\K connected.

Formalized by `MathlibExt.Analysis.Complex.HartogsWanted.hartogs_extension`, a theorem declared in [MathlibExt/Analysis/Complex/HartogsExtension.lean, line 1743](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/HartogsExtension.lean#L1743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html#hartogs-extension).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hartogs extension theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/several-complex-variables/hartogs-extension-theorem)
