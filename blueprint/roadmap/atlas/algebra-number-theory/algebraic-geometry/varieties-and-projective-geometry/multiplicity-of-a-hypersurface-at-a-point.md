---
declaration: section
origin: cited
lean: Projectivization.mk_smul_eq, Projectivization.orthogonal_iff_rep_dotProduct_rep, MvPolynomial.orderAt, MvPolynomial.constantCoeff_aeval_X_add_C, MvPolynomial.pderiv_aeval_X_add_C, MvPolynomial.one_le_orderAt_iff, MvPolynomial.orderAt_eq_zero_iff, MvPolynomial.orderAt_C_of_ne_zero
statement: formalized
proof: formalized
---

# Multiplicity of a hypersurface at a point

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html).

## Projectivization

## Rescaling a representative does not change the projective point

Let $V$ be a module over
a division ring $K$. For every nonzero scalar $a \in K$ and every nonzero vector $v \in V$, the
points of the projectivization $\mathbb{P}(V)$ represented by $a v$ and by $v$ are equal.

Formalized by `Projectivization.mk_smul_eq`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#mk-smul-eq).

## Orthogonality of projective points via representatives

Let $K$ be a field and $m$ a
finite set. Let $p, q$ be points of the projective space $\mathbb{P}(K^m)$ and let
$\hat p, \hat q \in K^m$ be the fixed nonzero representatives chosen for $p$ and $q$. Then $p$
and $q$ are orthogonal (the dot product of a representative of $p$ with a representative of $q$
vanishes, which does not depend on the representatives) if and only if $\hat p \cdot \hat q = 0$.

Formalized by `Projectivization.orthogonal_iff_rep_dotProduct_rep`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#orthogonal-iff-rep-dot-product-rep).

## Order of vanishing at a point

Let $R$ be a commutative semiring, let $F$ be a
polynomial over $R$ in the variables $(X_i)_{i \in \sigma}$ and let $v \in R^\sigma$. The order
of vanishing $\operatorname{ord}_v F \in \mathbb{N} \cup \{\infty\}$ of $F$ at $v$ is the order
at the origin of the Taylor expansion $F(v + X)$, the polynomial obtained from $F$ by
substituting $X_i + v_i$ for each $X_i$: the least total degree of a monomial with nonzero
coefficient in $F(v + X)$, or $\infty$ if $F(v + X) = 0$. In particular it is $\infty$ for
$F = 0$.

Formalized by `MvPolynomial.orderAt`, a definition declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#order-at).

## Constant term of the Taylor expansion

Let $R$ be a commutative semiring, $F$ a
polynomial over $R$ in the variables $(X_i)_{i \in \sigma}$, and $v \in R^\sigma$. The constant
term of the Taylor expansion $F(X + v)$, obtained by substituting $X_i + v_i$ for each $X_i$, is
the value $F(v)$.

Formalized by `MvPolynomial.constantCoeff_aeval_X_add_C`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#constant-coeff-aeval-x-add-c).

## Partial derivatives commute with Taylor expansion

Let $R$ be a commutative semiring,
let $F$ be a polynomial over $R$ in the variables $(X_j)_{j \in \sigma}$, let $v \in R^\sigma$ and
let $i \in \sigma$. Writing $G(X + v)$ for the polynomial obtained from a polynomial $G$ by
substituting $X_j + v_j$ for each $X_j$, we have
$\frac{\partial}{\partial X_i}\bigl(F(X + v)\bigr) = \frac{\partial F}{\partial X_i}(X + v)$.

Formalized by `MvPolynomial.pderiv_aeval_X_add_C`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#pderiv-aeval-x-add-c).

## Vanishing to order at least one

Let $R$ be a commutative semiring, let $F$ be a
polynomial over $R$ in the variables $(X_i)_{i \in \sigma}$ and let $v \in R^\sigma$. Then the
order of vanishing $\operatorname{ord}_v F$ of $F$ at $v$ is at least $1$ if and only if
$F(v) = 0$.

Formalized by `MvPolynomial.one_le_orderAt_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#one-le-order-at-iff).

## Vanishing to order zero

Let $R$ be a commutative semiring, let $F$ be a polynomial over
$R$ in the variables $(X_i)_{i \in \sigma}$ and let $v \in R^\sigma$. Then the order of vanishing
$\operatorname{ord}_v F$ of $F$ at $v$ is $0$ if and only if $F(v) \neq 0$.

Formalized by `MvPolynomial.orderAt_eq_zero_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#order-at-eq-zero-iff).

## Nonzero constants vanish to order zero

Let $R$ be a commutative semiring and let
$a \in R$ be nonzero. For every point $v \in R^\sigma$, the constant polynomial $a$ in the
variables $(X_i)_{i \in \sigma}$ has order of vanishing $\operatorname{ord}_v a = 0$ at $v$.

Formalized by `MvPolynomial.orderAt_C_of_ne_zero`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#order-at-c-of-ne-zero).

## Only the zero polynomial vanishes to infinite order

Let $R$ be a commutative ring, let
$F$ be a polynomial over $R$ in the variables $(X_i)_{i \in \sigma}$ and let $v \in R^\sigma$.
Then the order of vanishing $\operatorname{ord}_v F \in \mathbb{N} \cup \{\infty\}$ of $F$ at $v$
equals $\infty$ if and only if $F = 0$.

Formalized by `MvPolynomial.orderAt_eq_top_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#order-at-eq-top-iff).

## Order of vanishing via first partial derivatives

Let $R$ be an integral domain of
characteristic zero, $F$ a polynomial over $R$ in the variables $(X_i)_{i \in \sigma}$,
$v \in R^\sigma$ and $n \in \mathbb{N}$. Then $F$ vanishes to order at least $n + 1$ at $v$ if
and only if $F(v) = 0$ and every first partial derivative $\partial F / \partial X_i$ vanishes to
order at least $n$ at $v$.

Formalized by `MvPolynomial.natCast_add_one_le_orderAt_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#nat-cast-add-one-le-order-at-iff).

## Vanishing to order at least two via first partial derivatives

Let $R$ be an integral
domain of characteristic zero and let $F$ be a multivariate polynomial over $R$ in the
variables $(X_i)_{i \in \sigma}$. For every point $v \in R^\sigma$, the polynomial $F$ vanishes
to order at least $2$ at $v$ if and only if $F(v) = 0$ and
$\frac{\partial F}{\partial X_i}(v) = 0$ for every $i \in \sigma$.

Equivalently, $v$ is a singular point of the hypersurface $F = 0$.

Formalized by `MvPolynomial.two_le_orderAt_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#two-le-order-at-iff).

## Scaling invariance of the order of vanishing

Let $K$ be a field and let $F$ be a
polynomial over $K$ in the variables $(X_i)_{i \in \sigma}$ that is homogeneous of some degree
$d$. For every nonzero $c \in K$ and every point $v \in K^\sigma$, the orders of vanishing agree:
$\operatorname{ord}_{cv} F = \operatorname{ord}_v F$.

Formalized by `MvPolynomial.orderAt_smul`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#order-at-smul).

## Multiplicity of a polynomial at a projective point

Let $K$ be a field and $F$ a
polynomial over $K$ in the variables $(X_i)_{i \in \sigma}$. The multiplicity of $F$ at a point
$p$ of the projective space $\mathbb{P}(K^\sigma)$ is the order of vanishing of $F$ at the chosen
representative $\bar p \in K^\sigma$ of $p$, as a natural number, with the value $\infty$ read
as $0$.

For homogeneous $F$ it does not depend on the representative. The order of vanishing is $\infty$
only for $F = 0$, so the multiplicity of the zero polynomial is the junk value $0$.

Formalized by `MvPolynomial.multiplicityAt`, a definition declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#multiplicity-at).

## The multiplicity can be computed at any representative

Let $K$ be a field and $F$ a
homogeneous polynomial over $K$ in the variables $(X_i)_{i \in \sigma}$. For every nonzero
$v \in K^\sigma$, the multiplicity of $F$ at the point $[v]$ of $\mathbb{P}(K^\sigma)$ spanned by
$v$ equals the order of vanishing of $F$ at $v$, with the value $\infty$ read as $0$.

Formalized by `MvPolynomial.multiplicityAt_mk`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#multiplicity-at-mk).

## The multiplicity of a nonzero polynomial is its order of vanishing

Let $K$ be a field
and $F \neq 0$ a polynomial over $K$ in the variables $(X_i)_{i \in \sigma}$. For every point
$p$ of $\mathbb{P}(K^\sigma)$, the multiplicity of $F$ at $p$, viewed in
$\mathbb{N} \cup \{\infty\}$, equals the order of vanishing of $F$ at the chosen representative
$\bar p \in K^\sigma$ of $p$.

Formalized by `MvPolynomial.natCast_multiplicityAt`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#nat-cast-multiplicity-at).

## Constants have multiplicity zero

Let $K$ be a field. For every $a \in K$, the constant
polynomial $a$ in the variables $(X_i)_{i \in \sigma}$ has multiplicity $0$ at every point $p$ of
the projective space $\mathbb{P}(K^\sigma)$. For $a = 0$ this is the junk value of the
multiplicity of the zero polynomial.

Formalized by `MvPolynomial.multiplicityAt_C`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#multiplicity-at-c).

## Positive multiplicity means vanishing

Let $K$ be a field, $F \neq 0$ a polynomial over
$K$ in the variables $(X_i)_{i \in \sigma}$, and $p$ a point of $\mathbb{P}(K^\sigma)$ with
chosen representative $\bar p \in K^\sigma$. The multiplicity of $F$ at $p$ is positive if and
only if $F(\bar p) = 0$.

Formalized by `MvPolynomial.multiplicityAt_pos_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#multiplicity-at-pos-iff).

## A linear form vanishes to order zero off its hyperplane

Let $K$ be a field, let
$\sigma$ be a finite set and let $w, v \in K^\sigma$ with
$w \cdot v = \sum_{i \in \sigma} w_i v_i \neq 0$. Then the linear form
$L = \sum_{i \in \sigma} w_i X_i$ has order of vanishing $\operatorname{ord}_v L = 0$ at $v$.

Formalized by `MvPolynomial.orderAt_sum_C_mul_X_of_dotProduct_ne_zero`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#order-at-sum-c-mul-x-of-dot-product-ne-z).

## A nonzero linear form vanishes to order one on its hyperplane

Let $K$ be a field, let
$\sigma$ be a finite set and let $w, v \in K^\sigma$ with $w \neq 0$ and
$w \cdot v = \sum_{i \in \sigma} w_i v_i = 0$. Then the linear form
$L = \sum_{i \in \sigma} w_i X_i$ has order of vanishing $\operatorname{ord}_v L = 1$ at $v$.

Formalized by `MvPolynomial.orderAt_sum_C_mul_X_of_dotProduct_eq_zero`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#order-at-sum-c-mul-x-of-dot-product-eq-z).

## A hyperplane has multiplicity one at its points

Let $K$ be a field, $\sigma$ a finite
type and $w \in K^\sigma$ nonzero, and let $p$ be a point of $\mathbb{P}(K^\sigma)$ orthogonal to
the point $[w]$ spanned by $w$, that is, $p$ lies on the hyperplane $\sum_i w_i x_i = 0$. Then
the linear form $\sum_i w_i X_i$ has multiplicity $1$ at $p$.

Formalized by `MvPolynomial.multiplicityAt_sum_C_mul_X_of_orthogonal`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#multiplicity-at-sum-c-mul-x-of-orthogona).

## A hyperplane has multiplicity zero off it

Let $K$ be a field, $\sigma$ a finite type and
$w \in K^\sigma$ nonzero, and let $p$ be a point of $\mathbb{P}(K^\sigma)$ that is not orthogonal
to the point $[w]$ spanned by $w$, that is, $p$ does not lie on the hyperplane
$\sum_i w_i x_i = 0$. Then the linear form $\sum_i w_i X_i$ has multiplicity $0$ at $p$.

Formalized by `MvPolynomial.multiplicityAt_sum_C_mul_X_of_not_orthogonal`, a theorem declared in [MathlibExt/AlgebraicGeometry/PointMultiplicity.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/AlgebraicGeometry/PointMultiplicity.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html#multiplicity-at-sum-c-mul-x-of-not-ortho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiplicity of a hypersurface at a point](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/multiplicity-of-a-hypersurface-at-a-point)
