---
declaration: section
origin: cited
lean: MathlibExt.AlgebraicGeometry.EllipticCurve.ManinProjectiveDegree.PrimitiveTriple, MathlibExt.AlgebraicGeometry.EllipticCurve.ManinProjectiveDegree.primitiveTriple_of_no_common_irreducible, MathlibExt.AlgebraicGeometry.EllipticCurve.ManinProjectiveDegree.projective_first_natDegree, Int.eq_quadratic_of_recurrence, Int.sq_le_four_mul_of_quadratic_nonnegative, MathlibExt.AlgebraicGeometry.EllipticCurve.ManinDegreeData, MathlibExt.AlgebraicGeometry.EllipticCurve.ManinDegreeData.ofQuadratic, MathlibExt.AlgebraicGeometry.EllipticCurve.ManinDegreeData.hasse_bound
statement: formalized
proof: formalized
---

# Hasse bound

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html).

## Primitive triple of polynomials

Let $K$ be a field. Polynomials $a, b, c \in K[X]$
form a primitive triple when they generate the unit ideal of $K[X]$, that is, when there are
$u, v, w \in K[X]$ with $ua + vb + wc = 1$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinProjectiveDegree.PrimitiveTriple`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinProjectiveDegree.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinProjectiveDegree.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#primitive-triple).

## Polynomials with no common irreducible factor form a primitive triple

Let $K$ be a
field and let $a, b, c \in K[X]$ with $c \neq 0$. If no irreducible polynomial in $K[X]$
divides all of $a$, $b$ and $c$, then $a, b, c$ form a primitive triple: there are
$u, v, w \in K[X]$ with $ua + vb + wc = 1$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinProjectiveDegree.primitiveTriple_of_no_common_irreducible`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinProjectiveDegree.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinProjectiveDegree.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#primitive-triple-of-no-common-irreducibl).

## Numerator degrees from a primitive presentation of product and sum

Let $K$ be a field,
let $u, v, h \in K[X]$ form a primitive triple with $h \neq 0$, and let $x, y \in K(X)$ be
nonzero rational functions with $u/h = xy$ and $v/h = x + y$ in $K(X)$. Then
$\deg u = \deg \operatorname{num}(x) + \deg \operatorname{num}(y)$, where $\operatorname{num}$
denotes the numerator of a rational function written in lowest terms.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinProjectiveDegree.projective_first_natDegree`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinProjectiveDegree.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinProjectiveDegree.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#projective-first-nat-degree).

## Integer sequences with constant second difference two

Let $d : \mathbb{Z} \to \mathbb{Z}$
satisfy $d(n-1) + d(n+1) = 2d(n) + 2$ for every integer $n$, and let $q, N$ be integers with
$d(0) = q$ and $d(-1) = N$. Then $d(n) = n^2 + (q + 1 - N)n + q$ for every integer $n$.

Formalized by `Int.eq_quadratic_of_recurrence`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#eq-quadratic-of-recurrence).

## Discriminant bound for a nonnegative integral quadratic without adjacent zeros

Let
$a, q \in \mathbb{Z}$. If $n^2 + an + q \ge 0$ for every integer $n$ and there is no integer $n$
with $n^2 + an + q = 0$ and $(n+1)^2 + a(n+1) + q = 0$, then $a^2 \le 4q$.

Formalized by `Int.sq_le_four_mul_of_quadratic_nonnegative`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#sq-le-four-mul-of-quadratic-nonnegative).

## Manin degree data

For natural numbers $q$ and $N$, Manin degree data for $q$ and $N$ is
a sequence $d : \mathbb{Z} \to \mathbb{N}$ such that $d(0) = q$, $d(-1) = N$,
$d(n-1) + d(n+1) = 2d(n) + 2$ for every integer $n$, and there is no integer $n$ with
$d(n) = d(n+1) = 0$.

These are the properties of the polynomial-degree sequence used in Manin's proof of the Hasse
bound.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinDegreeData`, a structure declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#manin-degree-data).

## Manin degree data from a quadratic

Let $q$ and $N$ be natural numbers and put
$a = q + 1 - N \in \mathbb{Z}$. Suppose $n^2 + an + q \ge 0$ for every integer $n$, and there is
no integer $n$ at which both $n^2 + an + q$ and $(n+1)^2 + a(n+1) + q$ vanish. Then the sequence
$d(n) = n^2 + an + q$ is Manin degree data for $q$ and $N$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinDegreeData.ofQuadratic`, a definition declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#of-quadratic).

## Hasse bound from Manin degree data

Let $q$ and $N$ be natural numbers. If there is
Manin degree data for $q$ and $N$, then $(q + 1 - N)^2 \le 4q$, computed in the integers.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinDegreeData.hasse_bound`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinSequence.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#hasse-bound-2).

## Manin degree data over the field with three elements

Let $F$ be a field with exactly
three elements, let $W$ be any Weierstrass curve over $F$, and let $N$ be the number of
nonsingular points of $W$ over $F$, including the point at infinity. Then there is Manin degree
data for $(3, N)$: a function $d : \mathbb{Z} \to \mathbb{N}$ with $d(0) = 3$, $d(-1) = N$,
$d(n - 1) + d(n + 1) = 2 d(n) + 2$ for every integer $n$, and no integer $n$ with
$d(n) = d(n + 1) = 0$.

The proof needs only the elementary bound $N \le 2 \cdot 3 + 1$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwist.manin_degree_data_of_card_eq_three`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwist.lean, line 2294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwist.lean#L2294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#manin-degree-data-of-card-eq-three).

## Manin degree data for the odd-characteristic normal form

Let $F$ be a finite field with
$q$ elements, let $W$ be a Weierstrass curve $y^2 = x^3 + a_2 x^2 + a_4 x + a_6$ over $F$ (that
is, $a_1 = a_3 = 0$) with nonzero discriminant, and let $N$ be the number of points of $W$ over
$F$, including the point at infinity. Then there is Manin degree data for $(q, N)$: a function
$d : \mathbb{Z} \to \mathbb{N}$ with $d(0) = q$, $d(-1) = N$,
$d(n - 1) + d(n + 1) = 2 d(n) + 2$ for every integer $n$, and no integer $n$ with
$d(n) = d(n + 1) = 0$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwist.manin_degree_data_of_isCharNeTwoNF`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwist.lean, line 2304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwist.lean#L2304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#manin-degree-data-of-is-char-ne-two-nf).

## Hasse bound for the odd-characteristic normal form

Let $F$ be a finite field with $q$
elements and let $W$ be a Weierstrass curve $y^2 = x^3 + a_2 x^2 + a_4 x + a_6$ over $F$ (that
is, $a_1 = a_3 = 0$) with nonzero discriminant. If $N$ is the number of points of $W$ over $F$,
including the point at infinity, then $(q + 1 - N)^2 \le 4q$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwist.hasse_bound_of_isCharNeTwoNF`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwist.lean, line 2318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwist.lean#L2318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#hasse-bound-of-is-char-ne-two-nf).

## Manin degree data over the field with two elements

Let $F$ be a field with exactly
two elements, let $W$ be any Weierstrass curve over $F$, and let $N$ be the number of
nonsingular points of $W$ over $F$, including the point at infinity. Then there is Manin degree
data for $(2, N)$: a function $d : \mathbb{Z} \to \mathbb{N}$ with $d(0) = 2$, $d(-1) = N$,
$d(n - 1) + d(n + 1) = 2 d(n) + 2$ for every integer $n$, and no integer $n$ with
$d(n) = d(n + 1) = 0$.

The proof needs only the elementary bound $N \le 2 \cdot 2 + 1$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwistCharTwo.manin_degree_data_of_card_eq_two`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#manin-degree-data-of-card-eq-two).

## Manin degree data over the field with four elements

Let $F$ be a field with exactly
four elements, let $W$ be any Weierstrass curve over $F$, and let $N$ be the number of
nonsingular points of $W$ over $F$, including the point at infinity. Then there is Manin degree
data for $(4, N)$: a function $d : \mathbb{Z} \to \mathbb{N}$ with $d(0) = 4$, $d(-1) = N$,
$d(n - 1) + d(n + 1) = 2 d(n) + 2$ for every integer $n$, and no integer $n$ with
$d(n) = d(n + 1) = 0$.

The proof needs only the elementary bound $N \le 2 \cdot 4 + 1$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwistCharTwo.manin_degree_data_of_card_eq_four`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#manin-degree-data-of-card-eq-four).

## Manin degree data for the characteristic-two normal forms

Let $F$ be a finite field of
characteristic $2$ with $q$ elements, let $W$ be a Weierstrass curve over $F$ with nonzero
discriminant that is in one of the two characteristic-two normal forms
$y^2 + xy = x^3 + a_2 x^2 + a_6$ (that is, $a_1 = 1$ and $a_3 = a_4 = 0$) or
$y^2 + a_3 y = x^3 + a_4 x + a_6$ (that is, $a_1 = a_2 = 0$), and let $N$ be the number of
points of $W$ over $F$, including the point at infinity. Then there is Manin degree data for
$(q, N)$: a function $d : \mathbb{Z} \to \mathbb{N}$ with $d(0) = q$, $d(-1) = N$,
$d(n - 1) + d(n + 1) = 2 d(n) + 2$ for every integer $n$, and no integer $n$ with
$d(n) = d(n + 1) = 0$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwistCharTwo.manin_degree_data_of_isCharTwoNF`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean, line 3816](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean#L3816). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#manin-degree-data-of-is-char-two-nf).

## Hasse bound for the characteristic-two normal forms

Let $F$ be a finite field of
characteristic $2$ with $q$ elements and let $W$ be a Weierstrass curve over $F$ with nonzero
discriminant that is in one of the two characteristic-two normal forms
$y^2 + xy = x^3 + a_2 x^2 + a_6$ (that is, $a_1 = 1$ and $a_3 = a_4 = 0$) or
$y^2 + a_3 y = x^3 + a_4 x + a_6$ (that is, $a_1 = a_2 = 0$). If $N$ is the number of points of
$W$ over $F$, including the point at infinity, then $(q + 1 - N)^2 \le 4q$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwistCharTwo.hasse_bound_of_isCharTwoNF`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean, line 3829](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean#L3829). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#hasse-bound-of-is-char-two-nf).

## Hasse bound for the ordinary characteristic-two normal form

Let $F$ be a finite field of
characteristic $2$ with $q$ elements and let $W$ be a Weierstrass curve
$y^2 + xy = x^3 + a_2 x^2 + a_6$ over $F$ (that is, $a_1 = 1$ and $a_3 = a_4 = 0$) with nonzero
discriminant. If $N$ is the number of points of $W$ over $F$, including the point at infinity,
then $(q + 1 - N)^2 \le 4q$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwistCharTwo.hasse_bound_of_isCharTwoJNeZeroNF`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean, line 3836](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean#L3836). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#hasse-bound-of-is-char-two-jne-zero-nf).

## Hasse bound for the supersingular characteristic-two normal form

Let $F$ be a finite
field of characteristic $2$ with $q$ elements and let $W$ be a Weierstrass curve
$y^2 + a_3 y = x^3 + a_4 x + a_6$ over $F$ (that is, $a_1 = a_2 = 0$) with nonzero discriminant.
If $N$ is the number of points of $W$ over $F$, including the point at infinity, then
$(q + 1 - N)^2 \le 4q$.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.ManinTwistCharTwo.hasse_bound_of_isCharTwoJEqZeroNF`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean, line 3844](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/ManinTwistCharTwo.lean#L3844). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#hasse-bound-of-is-char-two-jeq-zero-nf).

## Hasse bound

Let $F$ be a finite field with $q$ elements and let $E$ be an elliptic curve over
$F$ given by a Weierstrass equation. If $N$ is the number of points of $E$ with coordinates in $F$,
including the point at infinity, then $(q + 1 - N)^2 \le 4q$ in $\mathbb{Z}$.

Proof: Manin's elementary polynomial-degree argument on a twist over the rational function field
$F(t)$, done separately for the odd-characteristic and characteristic-two normal forms. In
characteristic two the point count uses the fibres of the additive maps $y \mapsto y^2 + by$ with
$b \in F$, followed by the same projective neighboring-degree recurrence, as in
Chahal--Soomro--Top, *Rocky Mountain J. Math.* 44 (2014).

## Sources

- H. Hasse, J. Reine Angew. Math. 1936; modern Silverman, The Arithmetic of Elliptic Curves, 2nd ed.; Lean states integral squared form of |N-(q+1)| ≤ 2√q including point at infinity.

Formalized by `MathlibExt.AlgebraicGeometry.EllipticCurve.HasseBoundWanted.hasse_bound`, a theorem declared in [MathlibExt/AlgebraicGeometry/EllipticCurve/HasseBound.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/EllipticCurve/HasseBound.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html#hasse-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hasse bound](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/elliptic-curves/hasse-bound)
