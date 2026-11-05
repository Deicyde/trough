---
article_id: af_7be2f4b964ca6f85c5b23855
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: NumberField.Units.exist_unique_eq_mul_prod
mathlib_file: Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean
---

# Dirichlet unit theorem

The **Dirichlet unit theorem** describes the group of units of the ring of integers of a
number field: it is the product of the finite cyclic group of roots of unity in the field and a
free abelian group whose rank is determined by how the field embeds into the
[complex numbers](../numbers/complex-number.md). It is one of the two basic finiteness results of algebraic
number theory, alongside the [finiteness of the class number](finiteness-of-the-class-number.md), and the size of the units,
measured by the regulator, enters the [class number formula](dirichlet-class-number-formula.md).

## Statement

Let $K$ be a number field, a [field](../field-theory/field.md) of finite degree $n$ over $\mathbb{Q}$, and let
$\mathcal{O}_K$ be its ring of integers, the elements of $K$ that are roots of monic polynomials
with integer coefficients. Of the $n$ field embeddings $K \to \mathbb{C}$, say $r_1$ land in
$\mathbb{R}$ and the remaining $2r_2$ come in complex-conjugate pairs, so that
$r_1 + 2r_2 = n$. Each real embedding, and each conjugate pair, gives an absolute value
$|\cdot|_w$ on $K$, called an infinite place; there are $r_1 + r_2$ of them. Put

$$r = r_1 + r_2 - 1.$$

The roots of unity in $K$ all lie in $\mathcal{O}_K$ and form a finite cyclic
[group](../group-theory/part-01/group.md) $\mu_K$. The theorem says that there are units
$\varepsilon_1, \dots, \varepsilon_r$ of $\mathcal{O}_K$, a *fundamental system of units*, such that
every unit $u$ can be written in exactly one way as

$$u = \zeta\, \varepsilon_1^{a_1} \cdots \varepsilon_r^{a_r}, \qquad \zeta \in \mu_K,\ a_1, \dots, a_r \in \mathbb{Z}.$$

Mathlib chooses a particular fundamental system and proves that
[every unit is uniquely a root of unity times a product of integer powers of its members](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.exist_unique_eq_mul_prod). In group-theoretic terms,
$\mathcal{O}_K^\times \cong \mu_K \times \mathbb{Z}^r$: the unit group is finitely generated, its
torsion subgroup is $\mu_K$, and
[the quotient by $\mu_K$ has rank $r$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.finrank_modTorsion), in line with
the [structure theorem for finitely generated abelian groups](../group-theory/part-02/structure-of-finitely-generated-abelian-groups.md).

## Examples

- **The rationals.** For $K = \mathbb{Q}$ we have $r_1 = 1$, $r_2 = 0$ and $r = 0$, and indeed
  [the only units of its ring of integers $\mathbb{Z}$ are $1$ and $-1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Basic.html#Rat.RingOfIntegers.isUnit_iff).
- **Imaginary quadratic fields.** Here $r_1 = 0$, $r_2 = 1$ and $r = 0$, so there are only finitely
  many units: $\pm 1, \pm i$ in the Gaussian integers, the six sixth roots of unity in
  $\mathbb{Z}[\tfrac{1 + \sqrt{-3}}{2}]$, and just $\pm 1$ in every other case.
- **Real quadratic fields.** Here $r_1 = 2$ and $r = 1$. For $K = \mathbb{Q}(\sqrt 2)$ the ring
  of integers is $\mathbb{Z}[\sqrt 2]$, and the units are exactly the numbers $\pm(1 + \sqrt 2)^k$
  with $k \in \mathbb{Z}$. An element $a + b\sqrt 2$ is a unit exactly when its norm
  $a^2 - 2b^2$ is $\pm 1$, an instance of the general criterion that
  [an algebraic integer is a unit if and only if its norm has absolute value $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Basic.html#NumberField.isUnit_iff_norm).
- **A cubic field.** For $K = \mathbb{Q}(\sqrt[3]{2})$, with $r_1 = 1$ and $r_2 = 1$, the rank is again
  $1$; the identity $(\sqrt[3]{2} - 1)(\sqrt[3]{4} + \sqrt[3]{2} + 1) = 1$ exhibits a unit of
  infinite order. Since the degree is odd,
  [the only roots of unity in $K$ are $1$ and $-1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Basic.html#NumberField.Units.torsion_eq_one_or_neg_one_of_odd_finrank).
- **Cyclotomic fields.** For a prime $p \ge 3$, the field $\mathbb{Q}(\zeta_p)$ has no real
  embeddings and degree $p - 1$, so $r = \tfrac{p-1}{2} - 1 = \tfrac{p-3}{2}$.

## Proof

Write $d_w$ for $1$ when $w$ is real and $2$ when it is complex, and send a unit $u$ to its
logarithm vector $\ell(u) = \big(d_w \log |u|_w\big)_w$ in $\mathbb{R}^{r_1 + r_2}$. This is a group
homomorphism from multiplication to addition. A unit has norm $\pm 1$, so
[the coordinates of $\ell(u)$ sum to zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Basic.html#NumberField.Units.sum_mult_mul_log), and the image
lies in a hyperplane of dimension $r$.

The kernel is finite: [a unit is a root of unity exactly when $|u|_w = 1$ at every infinite place](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Basic.html#NumberField.Units.mem_torsion), and since the minimal polynomial of an element of
$\mathcal{O}_K$ has integer coefficients, degree at most $n$, and coefficients bounded in terms of
the absolute values $|\cdot|_w$ of the element, only finitely many elements of $\mathcal{O}_K$ have
all $|\cdot|_w$ bounded. The same bound shows that every ball meets the image in finitely
many points, so the image is a discrete subgroup of the hyperplane, hence a free abelian group of
rank at most $r$.

The main step is that the image spans the hyperplane. Using [Minkowski's theorem](../../../hundred-theorems/part-02/minkowskis-fundamental-theorem.md) on
lattice points in convex bodies, one builds a sequence of nonzero algebraic integers of bounded norm
that shrink at every place except a chosen one; since only finitely many
[ideals](../ideals-and-quotients/ideal-of-a-commutative-ring.md) of $\mathcal{O}_K$ have norm below a given bound, two of them generate the
same principal ideal, and their quotient is a unit. Thus, [for each infinite place $w_1$ there is a unit $u$ with $\log |u|_w < 0$ at every place $w \neq w_1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.dirichletUnitTheorem.exists_unit).
A determinant estimate shows that $r$ of these vectors are linearly independent. The image is
therefore a lattice of rank exactly $r$, and lifting a [basis](../../linear-algebra/fundamentals/basis.md) of it to units
gives a fundamental system.

## Consequences

- **Generation.** [The fundamental units together with the roots of unity generate the whole unit group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.closure_fundSystem_sup_torsion_eq_top).
- **The regulator.** Delete one coordinate from the logarithm vectors of a fundamental system;
  the absolute value of the determinant of the resulting $r \times r$ matrix is the regulator of
  $K$. It depends neither on the fundamental system nor on the deleted coordinate, and
  [it is strictly positive](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Regulator.html#NumberField.Units.regulator_pos).
- **[Pell's equation](../../../hundred-theorems/part-02/solutions-to-pells-equation.md).** For a positive integer $d$ that is not a square,
  the solutions of $x^2 - dy^2 = 1$ are the units of norm $1$ in $\mathbb{Z}[\sqrt d]$, and the same
  rank-one phenomenon appears: [every solution is, up to sign, an integer power of the fundamental solution](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Pell.html#Pell.IsFundamental.eq_zpow_or_neg_zpow), the one with $x > 1$, $y > 0$ and $x$
  least.

## In Mathlib

Mathlib works with the unit group of the ring of integers of any field that is a number field.
The roots of unity are its torsion subgroup, the units of finite order. The rank is defined as the
number of infinite places minus one, and a separate result shows that
[the number of infinite places is $r_1 + r_2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/InfinitePlace/Basic.html#NumberField.InfinitePlace.card_eq_nrRealPlaces_add_nrComplexPlaces),
while [$r_1 + 2r_2$ is the degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/InfinitePlace/Basic.html#NumberField.InfinitePlace.card_add_two_mul_card_eq_rank).
The logarithmic embedding in the proof drops one distinguished place, so it lands in
$\mathbb{R}^r$ rather than in a hyperplane of $\mathbb{R}^{r_1 + r_2}$. The quotient of the units by
the roots of unity is treated as a module over the integers; Mathlib picks a
[basis of it](../../../thousand-plus/number-theory/part-02/dirichlets-unit-theorem.md), and its fundamental
system consists of arbitrary lifts of the basis elements. The uniqueness statement refers to that
chosen system, not to every fundamental system.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Field](../field-theory/field.md)
- [Complex number](../numbers/complex-number.md)
- [Group](../group-theory/part-01/group.md)
- [Cyclic group](../group-theory/part-01/cyclic-group.md)
- [Polynomial in one indeterminate](../polynomials-and-power-series/polynomial-in-one-indeterminate.md)

## Proof depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Minkowski’s Fundamental Theorem](../../../hundred-theorems/part-02/minkowskis-fundamental-theorem.md)
- [Basis](../../linear-algebra/fundamentals/basis.md)
- [Minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Ideal of a commutative ring](../ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Determinant](../../linear-algebra/matrices/determinant.md)

## Sources

- [Mathlib documentation: `NumberField.Units.exist_unique_eq_mul_prod`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.html#NumberField.Units.exist_unique_eq_mul_prod)
- [Source of `NumberField.Units.exist_unique_eq_mul_prod` in Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/NumberTheory/NumberField/Units/DirichletTheorem.lean#L504)
- [Mathlib overview: General algebra › Algebraic Number Theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L158)
