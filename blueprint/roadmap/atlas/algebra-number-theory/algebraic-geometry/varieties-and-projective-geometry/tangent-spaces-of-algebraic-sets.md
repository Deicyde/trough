---
declaration: section
origin: cited
lean: MvPolynomial.totalDerivativeAt, MvPolynomial.totalDerivativeAtLin, MvPolynomial.tangentSpacePoly, MvPolynomial.tangentSpaceIdeal, MvPolynomial.totalDerivativeAtLin_apply, MvPolynomial.mem_tangentSpacePoly, MvPolynomial.mem_tangentSpaceIdeal
statement: formalized
proof: formalized
---

# Tangent spaces of algebraic sets

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html).

## Total derivative at a point

For a field $k$, a polynomial $f \in k[x_1, \dots, x_n]$ and
$P, v \in k^n$, the total derivative of $f$ at $P$ along the translated direction $v$ is
$\sum_{i=1}^n \frac{\partial f}{\partial x_i}(P)\, v_i \in k$, where
$\frac{\partial f}{\partial x_i}$ is the formal partial derivative.

Formalized by `MvPolynomial.totalDerivativeAt`, a definition declared in [MathlibExt/AlgebraicGeometry/TangentSpace.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/TangentSpace.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html#total-derivative-at).

## Total derivative as a linear map

For a field $k$, a polynomial $f \in k[x_1, \dots, x_n]$
and a point $P \in k^n$, this is the $k$-linear map $k^n \to k$ sending $v$ to the total derivative
of $f$ at $P$ along $v$, namely $\sum_{i=1}^n \frac{\partial f}{\partial x_i}(P)\, v_i$.

Formalized by `MvPolynomial.totalDerivativeAtLin`, a definition declared in [MathlibExt/AlgebraicGeometry/TangentSpace.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/TangentSpace.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html#total-derivative-at-lin).

## Tangent space of a hypersurface

For a field $k$, a polynomial $f \in k[x_1, \dots, x_n]$
and a point $P \in k^n$, the tangent space of the hypersurface $f = 0$ at $P$ is the kernel of the
total derivative of $f$ at $P$, viewed as a $k$-linear map $k^n \to k$: the subspace of vectors
$v \in k^n$ with $\sum_{i=1}^n \frac{\partial f}{\partial x_i}(P)\, v_i = 0$. The point $P$ is not
required to satisfy $f(P) = 0$.

Formalized by `MvPolynomial.tangentSpacePoly`, a definition declared in [MathlibExt/AlgebraicGeometry/TangentSpace.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/TangentSpace.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html#tangent-space-poly).

## Tangent space of an ideal

For a field $k$, an ideal $I$ of $k[x_1, \dots, x_n]$ and a
point $P \in k^n$, the tangent space of $I$ at $P$ is the $k$-linear subspace of $k^n$ obtained
as the intersection, over all $f \in I$, of the tangent spaces at $P$ of the hypersurfaces
$f = 0$. The point $P$ is not required to be a common zero of $I$.

Formalized by `MvPolynomial.tangentSpaceIdeal`, a definition declared in [MathlibExt/AlgebraicGeometry/TangentSpace.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/TangentSpace.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html#tangent-space-ideal).

## Evaluating the total derivative linear map

For a field $k$, a polynomial
$f \in k[x_1, \dots, x_n]$ and $P, v \in k^n$, the total derivative of $f$ at $P$, viewed as a
$k$-linear map $k^n \to k$, sends $v$ to the total derivative of $f$ at $P$ along $v$.

Formalized by `MvPolynomial.totalDerivativeAtLin_apply`, a theorem declared in [MathlibExt/AlgebraicGeometry/TangentSpace.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/TangentSpace.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html#total-derivative-at-lin-apply).

## Membership in the tangent space of a hypersurface

Let $k$ be a field,
$f \in k[x_1, \dots, x_n]$, and $P, v \in k^n$. Then $v$ lies in the tangent space of the
hypersurface $f = 0$ at $P$ if and only if the total derivative of $f$ at $P$ along $v$ is zero.

Formalized by `MvPolynomial.mem_tangentSpacePoly`, a theorem declared in [MathlibExt/AlgebraicGeometry/TangentSpace.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/TangentSpace.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html#mem-tangent-space-poly).

## Membership in the tangent space of an ideal

Let $k$ be a field, $I$ an ideal of
$k[x_1, \dots, x_n]$, and $P, v \in k^n$. Then $v$ lies in the tangent space of $I$ at $P$ if and
only if, for every $f \in I$, the total derivative of $f$ at $P$ along $v$ is zero.

Formalized by `MvPolynomial.mem_tangentSpaceIdeal`, a theorem declared in [MathlibExt/AlgebraicGeometry/TangentSpace.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/TangentSpace.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html#mem-tangent-space-ideal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tangent spaces of algebraic sets](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/tangent-spaces-of-algebraic-sets)
