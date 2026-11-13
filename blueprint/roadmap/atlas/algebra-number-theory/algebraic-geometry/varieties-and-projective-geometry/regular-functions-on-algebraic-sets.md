---
declaration: section
origin: cited
lean: FractionRing.IsRegularAt, FractionRing.isRegularAt_algebraMap, FractionRing.isRegularAt_zero, FractionRing.isRegularAt_one, MvPolynomial.AffineCoordinateRing, MvPolynomial.AffineCoordinateRing.evalAt, MvPolynomial.AffineCoordinateRing.evalAt_mk, MvPolynomial.AffineCoordinateRing.IsRegularAt
statement: formalized
proof: formalized
---

# Regular functions on algebraic sets

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html).

## Fraction Ring

## Regularity of a fraction at an evaluation

Let $A$ and $K$ be commutative rings and
$\mathrm{ev} : A \to K$ a ring homomorphism. An element $r$ of the total ring of fractions of
$A$ (its localization at the non-zero-divisors) is regular at $\mathrm{ev}$ when there is some
$g \in A$ with $\mathrm{ev}(g) \neq 0$ such that $g r$ lies in the image of $A$ in its total ring
of fractions.

Formalized by `FractionRing.IsRegularAt`, a definition declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#is-regular-at).

## Elements of the base ring are regular

Let $A$ be a commutative ring and $K$ a nontrivial
commutative ring. For every ring homomorphism $\mathrm{ev} : A \to K$ and every $a \in A$, the
image of $a$ in the total ring of fractions of $A$ is regular at $\mathrm{ev}$.

Formalized by `FractionRing.isRegularAt_algebraMap`, a theorem declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#is-regular-at-algebra-map).

## Zero is regular

Let $A$ be a commutative ring and $K$ a nontrivial commutative ring.
For every ring homomorphism $\mathrm{ev} : A \to K$, the element $0$ of the total ring of fractions
of $A$ is regular at $\mathrm{ev}$.

Formalized by `FractionRing.isRegularAt_zero`, a theorem declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#is-regular-at-zero).

## One is regular

Let $A$ be a commutative ring and $K$ a nontrivial commutative ring.
For every ring homomorphism $\mathrm{ev} : A \to K$, the element $1$ of the total ring of fractions
of $A$ is regular at $\mathrm{ev}$.

Formalized by `FractionRing.isRegularAt_one`, a theorem declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#is-regular-at-one).

## Affine coordinate ring

Let $K$ be a field, $\sigma$ an index set and
$X \subseteq K^\sigma$ a set of points. The affine coordinate ring of $X$ is the quotient
$K[x_i : i \in \sigma] / I(X)$ of the polynomial ring over $K$ in variables indexed by $\sigma$
by the vanishing ideal $I(X)$, the ideal of all polynomials that vanish at every point of $X$.

Formalized by `MvPolynomial.AffineCoordinateRing`, an abbreviation declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#affine-coordinate-ring).

## Evaluation at a point of an affine set

Let $K$ be a field, $\sigma$ an index set and
$X \subseteq K^\sigma$ a set of points. For a point $P \in X$, evaluation at $P$ is the ring
homomorphism from the affine coordinate ring of $X$ to $K$ that sends the residue class of a
polynomial $f$ to $f(P)$; it is well defined because every polynomial in the vanishing ideal of
$X$ vanishes at $P$.

Formalized by `MvPolynomial.AffineCoordinateRing.evalAt`, a definition declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#eval-at).

## Evaluating a residue class

Let $K$ be a field, $\sigma$ an index set,
$X \subseteq K^\sigma$ a set of points and $P \in X$. For every polynomial $f$ over $K$ in
variables indexed by $\sigma$, evaluating the residue class of $f$ in the affine coordinate ring
of $X$ at $P$ gives $f(P)$.

Formalized by `MvPolynomial.AffineCoordinateRing.evalAt_mk`, a theorem declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#eval-at-mk).

## Regularity of a rational function at a point

Let $K$ be a field, $\sigma$ an index set
and $X \subseteq K^\sigma$ a set of points whose affine coordinate ring $A$ is an integral domain.
A rational function on $X$ is an element $r$ of the field of fractions of $A$; it is regular at a
point $P \in X$ when there is some $g \in A$ whose value $g(P)$ under evaluation at $P$ is nonzero
such that $g r$ lies in the image of $A$ in its field of fractions.

Formalized by `MvPolynomial.AffineCoordinateRing.IsRegularAt`, a definition declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#is-regular-at-2).

## Elements of the coordinate ring are regular

Let $K$ be a field, $\sigma$ an index set and
$X \subseteq K^\sigma$ a set of points whose affine coordinate ring $A$ is an integral domain. For
every $a \in A$ and every point $P \in X$, the image of $a$ in the field of fractions of $A$ is a
rational function on $X$ that is regular at $P$.

Formalized by `MvPolynomial.AffineCoordinateRing.isRegularAt_algebraMap`, a theorem declared in [MathlibExt/RingTheory/Localization/RegularAt.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Localization/RegularAt.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html#is-regular-at-algebra-map-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular functions on algebraic sets](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/regular-functions-on-algebraic-sets)
