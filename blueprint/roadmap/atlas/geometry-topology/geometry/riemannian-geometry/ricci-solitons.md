---
declaration: section
origin: cited
lean: Manifold.IsGradientRicciSoliton, Manifold.IsGradientShrinkingRicciSoliton, Manifold.isGradientRicciSoliton_gaussian, Manifold.isGradientShrinkingRicciSoliton_gaussian, Manifold.isGradientRicciSoliton_gaussian_iff, Manifold.isGradientShrinkingRicciSoliton_gaussian_iff
statement: formalized
proof: formalized
---

# Ricci solitons

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html).

## Gradient Ricci soliton

Let $M$ be a smooth manifold (possibly with boundary or corners)
modelled on a finite-dimensional real normed space, with a smooth Riemannian metric $g$. A
function $f : M \to \mathbb{R}$ and a constant $c \in \mathbb{R}$ form a gradient Ricci soliton
if $f$ is smooth and, for every point $x \in M$ and all tangent vectors $u, v \in T_x M$,
$\operatorname{Ric}_x(u, v) + (\operatorname{Hess} f)_x(u, v) = c \, g_x(u, v)$, where
$\operatorname{Ric}$ is the Ricci curvature of $g$ and $\operatorname{Hess} f$ is the covariant
Hessian of $f$.

Completeness and connectedness of $M$ are not part of this predicate; they are separate
hypotheses on $M$.

## Sources

- Oberwolfach Report 27/2012 (Geometrie): T. Yokota, p. 1651, defines a gradient shrinking Ricci soliton by `Ric(g) + Hess f = g / (2 * λ)` with `λ > 0` and `f` smooth, and R. Haslhofer (with R. Müller), p. 1669, eq. (1), uses `Rc + Hess f` equal to `g / 2`.

Formalized by `Manifold.IsGradientRicciSoliton`, a structure declared in [MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html#is-gradient-ricci-soliton).

## Gradient shrinking Ricci soliton

On a Riemannian manifold $(M, g)$, a function
$f : M \to \mathbb{R}$ and a constant $c \in \mathbb{R}$ form a gradient shrinking Ricci soliton
if they form a gradient Ricci soliton and $c > 0$.

Completeness and connectedness of $M$ are not part of this predicate.

## Sources

- Oberwolfach Report 27/2012 (Geometrie). In Yokota's notation (p. 1651) this is `c = 1 / (2 * λ)` with `λ > 0`; Haslhofer's normalization (p. 1669, eq. (1)) is `c = 1 / 2`.

Formalized by `Manifold.IsGradientShrinkingRicciSoliton`, a structure declared in [MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html#is-gradient-shrinking-ricci-soliton).

## The Gaussian gradient Ricci soliton

Let $F$ be a finite-dimensional real inner product
space, viewed as a Riemannian manifold with the metric given by its inner product, and let
$a \in \mathbb{R}$. The function $f(x) = \frac{a}{2} \|x\|^2$ on $F$ is a gradient Ricci soliton
with constant $a$.

For $a < 0$ this is the expanding Gaussian soliton.

Formalized by `Manifold.isGradientRicciSoliton_gaussian`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html#is-gradient-ricci-soliton-gaussian).

## The Gaussian shrinking soliton

Let $F$ be a finite-dimensional real inner product space,
viewed as a Riemannian manifold with the metric given by its inner product, and let $a > 0$. The
function $f(x) = \frac{a}{2} \|x\|^2$ on $F$ is a gradient shrinking Ricci soliton with
constant $a$.

## Sources

- Oberwolfach Report 27/2012 (Geometrie), T. Yokota, p. 1652; for `a = 1 / 2` this is the Gaussian shrinker `(ℝⁿ, g_E, ‖x‖ ^ 2 / 4)`.

Formalized by `Manifold.isGradientShrinkingRicciSoliton_gaussian`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html#is-gradient-shrinking-ricci-soliton-gaus).

## Gaussian potentials that are gradient Ricci solitons

Let $F$ be a real inner product
space of positive finite dimension, viewed as a Riemannian manifold with the metric given by its
inner product, and let $a, c \in \mathbb{R}$. The function $f(x) = \frac{a}{2} \|x\|^2$ on $F$ is
a gradient Ricci soliton with constant $c$ if and only if $a = c$.

Formalized by `Manifold.isGradientRicciSoliton_gaussian_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html#is-gradient-ricci-soliton-gaussian-iff).

## Gaussian potentials that are gradient shrinking Ricci solitons

Let $F$ be a real inner
product space of positive finite dimension, viewed as a Riemannian manifold with the metric given
by its inner product, and let $a, c \in \mathbb{R}$. The function $f(x) = \frac{a}{2} \|x\|^2$ on
$F$ is a gradient shrinking Ricci soliton with constant $c$ if and only if $a = c$ and $c > 0$.

Formalized by `Manifold.isGradientShrinkingRicciSoliton_gaussian_iff`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Riemannian/RicciSoliton.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html#is-gradient-shrinking-ricci-soliton-gaus-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ricci solitons](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/ricci-solitons/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/riemannian-geometry/ricci-solitons)
