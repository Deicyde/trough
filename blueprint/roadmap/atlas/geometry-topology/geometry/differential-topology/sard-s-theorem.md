---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Manifold.SardWanted.criticalSet, MathlibExt.Geometry.Manifold.SardWanted.criticalValues, MathlibExt.Geometry.Manifold.SardWanted.sard_euclidean_open, MathlibExt.Geometry.Manifold.SardWanted.sard_theorem, MathlibExt.Geometry.Manifold.ParametricSardWanted.badParameterSet, MathlibExt.Geometry.Manifold.ParametricSardWanted.parametricSard
statement: formalized
proof: formalized
---

# Sard's theorem

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html).

## Critical points of a map to Euclidean space

Let $M$ be a Hausdorff, second-countable
smooth manifold without boundary modelled on a finite-dimensional real normed space, and let
$f : M \to \mathbb{R}^n$ be a map. The critical set of $f$ is the set of points $x \in M$ at which
the manifold derivative of $f$ at $x$, a linear map $T_xM \to \mathbb{R}^n$, is not surjective.

The derivative is taken to be $0$ at points where $f$ is not differentiable.

Formalized by `MathlibExt.Geometry.Manifold.SardWanted.criticalSet`, a definition declared in [MathlibExt/Geometry/Manifold/Sard.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Sard.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html#critical-set).

## Critical values of a map to Euclidean space

Let $M$ be a Hausdorff, second-countable
smooth manifold without boundary modelled on a finite-dimensional real normed space, and let
$f : M \to \mathbb{R}^n$ be a map. The set of critical values of $f$ is the image under $f$ of its
critical set, the set of points $x \in M$ at which the manifold derivative of $f$ at $x$ is not
surjective.

Formalized by `MathlibExt.Geometry.Manifold.SardWanted.criticalValues`, a definition declared in [MathlibExt/Geometry/Manifold/Sard.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Sard.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html#critical-values).

## Sard's theorem on open subsets of finite-dimensional spaces

Let $E$ and $F$ be
finite-dimensional real normed spaces, let $\mu$ be an additive Haar measure on $F$ with its Borel
$\sigma$-algebra, let $U \subseteq E$ be open, and let $g : E \to F$ be $C^\infty$ on $U$. Then the
image under $g$ of the set of points $x \in U$ at which the derivative of $g$ is not surjective has
$\mu$-measure zero.

Formalized by `MathlibExt.Geometry.Manifold.SardWanted.sard_euclidean_open`, a theorem declared in [MathlibExt/Geometry/Manifold/Sard.lean, line 1413](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Sard.lean#L1413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html#sard-euclidean-open).

## Sard's theorem for maps into Euclidean space

Let $M$ be a Hausdorff, second-countable smooth
manifold without boundary modelled on a finite-dimensional real normed space, and let
$f : M \to \mathbb{R}^n$ be a $C^\infty$ map. Then the set of critical values of $f$, the image
under $f$ of the points of $M$ at which the manifold derivative of $f$ is not surjective, has
Lebesgue measure zero.

## Sources

- A. Sard, Bull. Amer. Math. Soc. 48 (1942) 883–890 measure of critical values; J. Lee, Introduction to Smooth Manifolds, 2nd ed.; Guillemin-Pollack, Differential Topology; Lean states finite-dimensional manifold to `EuclideanSpace ℝ (Fin n)` specialization.

Formalized by `MathlibExt.Geometry.Manifold.SardWanted.sard_theorem`, a theorem declared in [MathlibExt/Geometry/Manifold/Sard.lean, line 1434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/Sard.lean#L1434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html#sard-theorem).

## Bad parameter set

Let $F \colon \mathbb{R}^p \times \mathbb{R}^m \to \mathbb{R}^n$ be a map
and $y \in \mathbb{R}^n$. For $a \in \mathbb{R}^p$ write $F_a = F(a, \cdot)$ for the slice
$\mathbb{R}^m \to \mathbb{R}^n$. The bad parameter set of $F$ at $y$ is the set of
$a \in \mathbb{R}^p$ for which there is $x \in \mathbb{R}^m$ with $F(a, x) = y$ and the derivative
of $F_a$ at $x$ not surjective, that is, the set of $a$ for which $y$ is not a regular value of
$F_a$.

The derivative of a map at a point where it is not differentiable is taken to be zero.

Formalized by `MathlibExt.Geometry.Manifold.ParametricSardWanted.badParameterSet`, a definition declared in [MathlibExt/Geometry/Manifold/ParametricSard.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/ParametricSard.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html#bad-parameter-set).

## Parametric Sard theorem for real analytic families

Let $p, m, n$ be natural numbers, let
$F \colon \mathbb{R}^p \times \mathbb{R}^m \to \mathbb{R}^n$ be a real analytic ($C^\omega$) map
and let $y \in \mathbb{R}^n$. Suppose that the derivative of $F$ is surjective at every point
$(a, x)$ with $F(a, x) = y$. Then the bad parameter set of $F$ at $y$, the set of
$a \in \mathbb{R}^p$ for which some $x \in \mathbb{R}^m$ has $F(a, x) = y$ and the derivative of
the slice $F(a, \cdot) \colon \mathbb{R}^m \to \mathbb{R}^n$ at $x$ is not surjective, has
Lebesgue measure zero.

## Sources

- R. Abraham, Bull. Amer. Math. Soc. 69 (1963), 470–475, DOI 10.1090/S0002-9904-1963-10969-6 parametric transversality; V. Guillemin and A. Pollack, Differential Topology; J. Lee, Intro to Smooth Manifolds, 2nd ed.; Lean states Euclidean finite-dimensional measure-zero form with `fderiv ℝ F` surjective hypothesis.

Formalized by `MathlibExt.Geometry.Manifold.ParametricSardWanted.parametricSard`, a theorem declared in [MathlibExt/Geometry/Manifold/ParametricSard.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/ParametricSard.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html#parametric-sard).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sard's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/sard-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/differential-topology/sard-s-theorem)
