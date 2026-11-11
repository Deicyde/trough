---
declaration: section
origin: cited
lean: NewtonPolygon.exponentToReal, NewtonPolygon.newtonSupport, NewtonPolygon.newtonPolygon, NewtonPolygon.newtonPolygonInterior, NewtonPolygon.newtonPolygonBoundary, NewtonPolygon.edgeRestriction, NewtonPolygon.mem_newtonSupport, NewtonPolygon.newtonSupport_zero
statement: formalized
proof: formalized
---

# Newton polygon

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html).

## Exponent vectors as points of the plane

The map from exponent vectors of monomials in two
variables to $\mathbb{R}^2$ sends $e = (e_0, e_1) \in \mathbb{N}^2$ to the point
$(e_0, e_1) \in \mathbb{R}^2$.

Formalized by `NewtonPolygon.exponentToReal`, a definition declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#exponent-to-real).

## Newton support

Let $f$ be a polynomial in two variables $x_0, x_1$ over a commutative
semiring $k$. The Newton support of $f$ is the set of exponent vectors $(e_0, e_1) \in \mathbb{N}^2$
of the monomials $x_0^{e_0} x_1^{e_1}$ with nonzero coefficient in $f$, viewed as points of
$\mathbb{R}^2$.

Formalized by `NewtonPolygon.newtonSupport`, a definition declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-support).

## Newton polygon

Let $f$ be a polynomial in two variables over a commutative semiring $k$.
The Newton polygon of $f$ is the convex hull in $\mathbb{R}^2$ of the Newton support of $f$, the
set of exponent vectors of the monomials with nonzero coefficient in $f$, viewed as points of
$\mathbb{R}^2$.

Formalized by `NewtonPolygon.newtonPolygon`, a definition declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-polygon).

## Interior of the Newton polygon

For a polynomial $f$ in two variables over a commutative
semiring $k$, the interior of the Newton polygon of $f$ is its topological interior as a subset
of $\mathbb{R}^2$.

Formalized by `NewtonPolygon.newtonPolygonInterior`, a definition declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-polygon-interior).

## Boundary of the Newton polygon

For a polynomial $f$ in two variables over a commutative
semiring $k$, the boundary of the Newton polygon of $f$ is its topological boundary in
$\mathbb{R}^2$: the closure of the Newton polygon minus its interior.

Formalized by `NewtonPolygon.newtonPolygonBoundary`, a definition declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-polygon-boundary).

## Restriction of a polynomial to a set of exponents

Let $f$ be a polynomial in two variables
over a commutative semiring $k$, and let $\Gamma \subseteq \mathbb{R}^2$. The restriction of $f$ to
$\Gamma$ is the polynomial formed by the terms of $f$ whose exponent vector, viewed as a point of
$\mathbb{R}^2$, lies in $\Gamma$; the other terms are dropped.

Formalized by `NewtonPolygon.edgeRestriction`, a definition declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#edge-restriction).

## Membership in the Newton support

Let $f$ be a polynomial in two variables over a
commutative semiring $k$. A point $x \in \mathbb{R}^2$ lies in the Newton support of $f$ if and
only if $x$ is the exponent vector $e \in \mathbb{N}^2$ of some monomial with nonzero coefficient
in $f$, viewed as a point of $\mathbb{R}^2$.

Formalized by `NewtonPolygon.mem_newtonSupport`, a theorem declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#mem-newton-support).

## The Newton support of the zero polynomial is empty

For every commutative semiring $k$, the
Newton support of the zero polynomial in two variables over $k$ is the empty subset of
$\mathbb{R}^2$.

Formalized by `NewtonPolygon.newtonSupport_zero`, a theorem declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-support-zero).

## The Newton polygon of the zero polynomial is empty

For every commutative semiring $k$, the
Newton polygon of the zero polynomial in two variables over $k$ is the empty subset of
$\mathbb{R}^2$.

Formalized by `NewtonPolygon.newtonPolygon_zero`, a theorem declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-polygon-zero).

## The Newton support lies in the Newton polygon

For every polynomial $f$ in two variables
over a commutative semiring $k$, the Newton support of $f$ is contained in the Newton polygon of
$f$, the convex hull of the Newton support in $\mathbb{R}^2$.

Formalized by `NewtonPolygon.newtonSupport_subset_newtonPolygon`, a theorem declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-support-subset-newton-polygon).

## The interior of the Newton polygon lies in the polygon

For every polynomial $f$ in two
variables over a commutative semiring $k$, the interior of the Newton polygon of $f$ in
$\mathbb{R}^2$ is contained in the Newton polygon of $f$.

Formalized by `NewtonPolygon.newtonPolygonInterior_subset_newtonPolygon`, a theorem declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#newton-polygon-interior-subset-newton-po).

## Edge restriction to the empty set

For every polynomial $f$ in two variables over a
commutative semiring $k$, the restriction of $f$ to the empty set, that is, the sum of the terms
of $f$ whose exponent vector, viewed as a point of $\mathbb{R}^2$, lies in $\emptyset$, is the
zero polynomial.

Formalized by `NewtonPolygon.edgeRestriction_empty`, a theorem declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#edge-restriction-empty).

## Edge restriction to the whole plane

For every polynomial $f$ in two variables over a
commutative semiring $k$, the restriction of $f$ to all of $\mathbb{R}^2$, that is, the sum of the
terms of $f$ whose exponent vector, viewed as a point of $\mathbb{R}^2$, lies in $\mathbb{R}^2$, is
$f$ itself.

Formalized by `NewtonPolygon.edgeRestriction_univ`, a theorem declared in [MathlibExt/Analysis/Convex/NewtonPolygon.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/NewtonPolygon.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html#edge-restriction-univ).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Newton polygon](https://deicyde.github.io/atlas-lean/roadmap/Algebra/polynomials/newton-polygon/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Algebra/polynomials/newton-polygon)
