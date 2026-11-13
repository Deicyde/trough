---
declaration: section
origin: cited
lean: Manifold.laplacian, Manifold.laplacian_vectorSpace, Manifold.laplacian_vectorSpace_eq_laplacian, Manifold.laplacian_norm_sq, Manifold.laplacian_gaussian
statement: formalized
proof: formalized
---

# Laplace–Beltrami operator

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator/index.html).

## Laplace–Beltrami operator

The Laplace-Beltrami operator applied to `f : M → ℝ` at `x`: `Δf(x)` is the metric
trace `∑ i, hessian I f x (e i) (e i)` over the orthonormal basis
`e = stdOrthonormalBasis ℝ (TangentSpace I x)`, the same basis convention as
`Manifold.scalarCurvature`. For the textbook Hessian, which is bilinear, this trace
does not depend on the orthonormal basis; the regularity caveat of `Manifold.hessian`
applies here unchanged.

Sign convention `Δf = tr_g ∇²f`, the convention `Δ = div ∘ grad` under which `Δ` is the
sum `∑ ∂²/∂x_i²` on Euclidean space and `Δ(‖x‖²) = 2n`; the operator `-Δ` is then the
nonnegative one, and the opposite sign convention is also common. Reference with the
same conventions: Lee, Introduction to Riemannian Manifolds (2nd ed., GTM 176).

Mathlib's flat Laplacian is `Laplacian.laplacian` (instance
`InnerProductSpace.instLaplacian`, notation `Δ` after `open Laplacian`): the trace of
the second derivative over an orthonormal basis of a finite-dimensional real inner
product space. On the model space `𝓘(ℝ, F)`, under
`DifferentiableAt ℝ (fderiv ℝ f) x`, this operator agrees with Mathlib's `Δ`
(same orthonormal-basis trace, same sign); see `laplacian_vectorSpace_eq_laplacian`
for the proved agreement. What is new here is the manifold operator itself.

Formalized by `Manifold.laplacian`, a definition declared in [MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator/index.html#laplacian).

## Laplacian on a vector space as a sum of second directional derivatives

Let $F$ be a
finite-dimensional real inner product space of dimension $n$ with its standard Riemannian
metric, let $f : F \to \mathbb{R}$ and $x \in F$, and let $e_1, \dots, e_n$ be the orthonormal
basis of the tangent space $T_xF$ used in the definition of the Laplacian, viewed as vectors of
$F$. For each $i$ let $g_i(y) = Df(y)(e_i)$, where $D$ denotes the Fréchet derivative. Then the
Laplacian of $f$ at $x$ is $\Delta f(x) = \sum_{i=1}^{n} Dg_i(x)(e_i)$. No differentiability of
$f$ is assumed; a Fréchet derivative that does not exist is taken to be $0$.

When $Df$ is differentiable at $x$, the right side is the flat Laplacian
$\sum_i D^2 f(x)(e_i, e_i)$ of $f$ at $x$.

Formalized by `Manifold.laplacian_vectorSpace`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator/index.html#laplacian-vector-space).

## The Laplacian on a vector space is the flat Laplacian at twice-differentiable points

Let
$F$ be a finite-dimensional real inner product space with its standard Riemannian metric, let
$f : F \to \mathbb{R}$ and $x \in F$, and let $Df$ denote the Fréchet derivative of $f$, taken to
be $0$ at points where $f$ is not differentiable. Suppose $Df$ is differentiable at $x$, with
derivative $D^2 f(x)$ there. Then the Laplacian $\Delta f(x)$ equals $\sum_i D^2 f(x)(b_i, b_i)$
for any orthonormal basis $(b_i)$ of $F$, the flat Laplacian of $f$ at $x$.

Without the hypothesis the two can differ: $D^2 f(x)$ is taken to be $0$ when $Df$ is not
differentiable at $x$, while $\Delta f(x)$ is the sum, over the vectors $v$ of the orthonormal
basis used in its definition, of the derivative at $x$ in direction $v$ of the function
$y \mapsto Df(y)(v)$.

Formalized by `Manifold.laplacian_vectorSpace_eq_laplacian`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator/index.html#laplacian-vector-space-eq-laplacian).

## Laplacian of the squared norm

Let $F$ be a finite-dimensional real inner product space
of dimension $n$ with its standard Riemannian metric. For every $x \in F$, the Laplacian of the
function $y \mapsto \|y\|^2$ at $x$ is $2n$.

The Hessian of $\|\cdot\|^2$ is $2\langle \cdot, \cdot \rangle$, so each of its diagonal entries
in an orthonormal basis is $2$.

Formalized by `Manifold.laplacian_norm_sq`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator/index.html#laplacian-norm-sq).

## Laplacian of the Gaussian potential

Let $F$ be a finite-dimensional real inner product
space of dimension $n$ with its standard Riemannian metric. For every real number $a$ and every
$x \in F$, the Laplacian of the function $y \mapsto \frac{a}{2}\|y\|^2$ at $x$ is $a \cdot n$.

This function is the potential of the Gaussian gradient Ricci soliton; each diagonal entry of
its Hessian in an orthonormal basis is $a$.

Formalized by `Manifold.laplacian_gaussian`, a theorem declared in [MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/Riemannian/Laplacian.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator/index.html#laplacian-gaussian).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Laplace–Beltrami operator](https://deicyde.github.io/atlas-lean/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/riemannian-geometry/laplace-beltrami-operator)
