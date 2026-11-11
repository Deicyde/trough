---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.SeshadriConstant.PlanePolynomial, MathlibExt.AlgebraicGeometry.SeshadriConstant.AffinePoint, MathlibExt.AlgebraicGeometry.SeshadriConstant.shifted, MathlibExt.AlgebraicGeometry.SeshadriConstant.monomialDegree, MathlibExt.AlgebraicGeometry.SeshadriConstant.multiplicity, MathlibExt.AlgebraicGeometry.SeshadriConstant.multiplicity_X_sub_C, MathlibExt.AlgebraicGeometry.SeshadriConstant.seshadriRatios, MathlibExt.AlgebraicGeometry.SeshadriConstant.affineSeshadriConstant
statement: formalized
---

# Seshadri constants of points in the plane

17 results, 12 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html).

## Polynomials in two complex variables

A plane polynomial is a polynomial
$f \in \mathbb{C}[X_0, X_1]$ in two variables $X_0, X_1$ with complex coefficients.

Such polynomials are used to represent affine plane curves.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.PlanePolynomial`, an abbreviation declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#plane-polynomial).

## Points of the complex affine plane

A point of the complex affine plane is a pair
$a = (a_0, a_1)$ of complex numbers, that is, an element of $\mathbb{C}^2$, with coordinates
indexed by $0$ and $1$.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.AffinePoint`, an abbreviation declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#affine-point).

## Translate of a plane polynomial

For a polynomial $f \in \mathbb{C}[x_1, x_2]$ and a
point $a = (a_1, a_2) \in \mathbb{C}^2$, the translate of $f$ by $a$ is the polynomial
$f(x_1 + a_1, x_2 + a_2)$, obtained by substituting $x_i + a_i$ for $x_i$. It moves the point $a$
to the origin.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.shifted`, a definition declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#shifted).

## Total degree of a monomial

The total degree of the exponent vector
$m = (m_0, m_1)$ of a monomial $X_0^{m_0} X_1^{m_1}$ in two variables is $m_0 + m_1$.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.monomialDegree`, a definition declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#monomial-degree).

## Multiplicity of a plane polynomial at a point

For a polynomial
$f \in \mathbb{C}[X_0, X_1]$ and a point $a = (a_0, a_1) \in \mathbb{C}^2$, the multiplicity
of $f$ at $a$ is the least total degree of a monomial occurring with nonzero coefficient in
the translated polynomial $f(X_0 + a_0, X_1 + a_1)$. For the zero polynomial it is $0$.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.multiplicity`, a definition declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#multiplicity).

## The first-coordinate line through a point has multiplicity one there

For every point
$a = (a_0, a_1) \in \mathbb{C}^2$, the polynomial $X_0 - a_0 \in \mathbb{C}[X_0, X_1]$, which
defines the line through $a$ on which the first coordinate is constant, has multiplicity $1$
at $a$.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.multiplicity_X_sub_C`, a theorem declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#multiplicity-x-sub-c).

## Seshadri ratios of ten points

For a configuration $x = (x_0, \dots, x_9)$ of ten
points of $\mathbb{C}^2$, not necessarily distinct, the Seshadri ratios of $x$ are the real
numbers $\deg f / \sum_{i=0}^{9} \operatorname{mult}_{x_i} f$, where $f$ ranges over the
nonzero polynomials in $\mathbb{C}[X_0, X_1]$ with
$\sum_{i=0}^{9} \operatorname{mult}_{x_i} f > 0$, $\deg f$ is the total degree of $f$, and
$\operatorname{mult}_{x_i} f$ is the multiplicity of $f$ at $x_i$.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.seshadriRatios`, a definition declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#seshadri-ratios).

## Seshadri constant of ten affine points

For a configuration
$x = (x_0, \dots, x_9)$ of ten points of $\mathbb{C}^2$, not necessarily distinct, the
affine Seshadri constant of $x$ is the infimum of the ratios
$\deg f / \sum_{i=0}^{9} \operatorname{mult}_{x_i} f$ over all nonzero polynomials
$f \in \mathbb{C}[X_0, X_1]$ with $\sum_{i=0}^{9} \operatorname{mult}_{x_i} f > 0$, where
$\deg f$ is the total degree of $f$ and $\operatorname{mult}_{x_i} f$ is the multiplicity
of $f$ at $x_i$.

The set of these ratios is nonempty and bounded below by $0$.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.affineSeshadriConstant`, a definition declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#affine-seshadri-constant).

## The affine Seshadri constant is at most one

For every configuration
$x = (x_0, \dots, x_9)$ of ten points of $\mathbb{C}^2$, not necessarily distinct, the
affine Seshadri constant of $x$ is at most $1$.

The bound comes from the polynomial $X_0 - c \in \mathbb{C}[X_0, X_1]$, where $c$ is the first
coordinate of $x_0$: it has total degree $1$ and multiplicity $1$ at $x_0$.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.affineSeshadriConstant_le_one`, a theorem declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#affine-seshadri-constant-le-one).

## Generic ten-point Seshadri constant

The generic ten-point Seshadri constant is the
supremum, over all configurations $x = (x_0, \dots, x_9)$ of ten pairwise distinct points
of $\mathbb{C}^2$, of the affine Seshadri constant of $x$.

This models the Seshadri constant of ten very general points of $\mathbb{P}^2$ in one
affine chart.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.genericSeshadriConstant`, a definition declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#generic-seshadri-constant).

## Ten-point Seshadri constant

The ten-point Seshadri constant is the generic
ten-point Seshadri constant: the supremum, over all configurations of ten pairwise distinct
points of $\mathbb{C}^2$, of their affine Seshadri constants.

It models the catalogue constant $C_{74}$, the Seshadri constant of $\mathbb{P}^2$ at ten
very general points, in one affine chart.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstant.seshadriConstant10`, a definition declared in [MathlibExt/AlgebraicGeometry/SeshadriConstant.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/SeshadriConstant.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#seshadri-constant10).

## Nagata's conjecture for ten points

The proposition that the generic ten-point
Seshadri constant of $\mathbb{P}^2$, in the affine-chart model, equals $1/\sqrt{10}$.

It is recorded as a proposition only and is not asserted.

Formalized by `MathlibExt.AlgebraicGeometry.SeshadriConstantWanted.nagataConjecture10`, a definition declared in [WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#nagata-conjecture10).

## Eckl's 2008 lower bound for the ten-point Seshadri constant

The generic ten-point Seshadri constant of $\mathbb{P}^2$, in the affine-chart model, is at least
$4/13$.

## Sources

- Eckl (2008), asymptotic Dumnicki method, catalogue lower bound `4/13`.

Stated but not proved: `MathlibExt.AlgebraicGeometry.SeshadriConstantWanted.eckl2008LowerBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#eckl2008-lower-bound-wanted).

## Harbourne–Roé lower bound for the ten-point Seshadri constant

The generic ten-point Seshadri constant of $\mathbb{P}^2$, in the affine-chart model, is at least
$177/560$.

## Sources

- Harbourne--Roé (2009), nef divisor bound `177/560`.

Stated but not proved: `MathlibExt.AlgebraicGeometry.SeshadriConstantWanted.harbourneRoe2009LowerBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#harbourne-roe2009-lower-bound-wanted).

## Ciliberto–Miranda lower bound for the ten-point Seshadri constant

The generic ten-point Seshadri constant of $\mathbb{P}^2$, in the affine-chart model, is at least
$55/174$.

## Sources

- Ciliberto--Miranda (2011), degeneration bound `55/174`.

Stated but not proved: `MathlibExt.AlgebraicGeometry.SeshadriConstantWanted.cilibertoMiranda2011LowerBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#ciliberto-miranda2011-lower-bound-wanted).

## Eckl's 2011 lower bound for the ten-point Seshadri constant

The generic ten-point Seshadri constant of $\mathbb{P}^2$, in the affine-chart model, is at least
$117/370$.

## Sources

- Eckl (2011), improved catalogue lower bound `117/370`.

Stated but not proved: `MathlibExt.AlgebraicGeometry.SeshadriConstantWanted.eckl2011LowerBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#eckl2011-lower-bound-wanted).

## Submaximal upper bound for the ten-point Seshadri constant

The generic ten-point Seshadri constant of $\mathbb{P}^2$, in the affine-chart model, is at most
$1/\sqrt{10}$.

## Sources

- the general submaximal upper bound `ε ≤ √(D²/r)` for `D = 𝒪_{ℙ²}(1)` and `r = 10`.

Stated but not proved: `MathlibExt.AlgebraicGeometry.SeshadriConstantWanted.submaximalUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/AlgebraicGeometry/SeshadriConstantWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html#submaximal-upper-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Seshadri constants of points in the plane](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/seshadri-constants-of-points-in-the-plane)
