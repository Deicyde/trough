---
article_id: af_09c6cb356916e6eac6c46ed8
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: Polynomial
mathlib_file: Mathlib/Algebra/Polynomial/Basic.lean
---

# Polynomial in one indeterminate

A **polynomial in one indeterminate** over a [ring](../rings/ring.md) $R$ is a formal expression
$a_0 + a_1 X + \dots + a_n X^n$ with coefficients $a_i$ in $R$, added and multiplied by the
familiar rules of high-school algebra. The polynomials over $R$ form a ring $R[X]$, the
[polynomial ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial). It is the simplest way to enlarge a ring by one new
element, and it underlies much of algebra: the theory of equations, field extensions,
algebraic geometry and the study of linear maps through their characteristic polynomials.

## Definition

Let $R$ be a ring. A polynomial over $R$ is a sequence $(a_0, a_1, a_2, \dots)$ of elements
of $R$ in which only finitely many terms are nonzero, that is, a
[finitely supported function](../../data-structures/maps/finitely-supported-function.md) from the natural numbers to $R$. The term $a_n$
is the coefficient of $X^n$, and
[two polynomials are equal exactly when all their coefficients agree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial.ext_iff).
Addition is coefficientwise, and multiplication is defined so that $X^i X^j = X^{i+j}$: the
product of $f = \sum_i a_i X^i$ and $g = \sum_j b_j X^j$ has
[as coefficient of $X^n$ the sum of $a_i b_j$ over all pairs with $i + j = n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Coeff.html#Polynomial.coeff_mul),

$$fg = \sum_{n \ge 0} \Bigl( \sum_{i+j=n} a_i b_j \Bigr) X^n.$$

The indeterminate $X$ is the sequence $(0, 1, 0, 0, \dots)$, and an element $a$ of $R$ is
identified with the constant polynomial $(a, 0, 0, \dots)$. With these identifications
[every polynomial is the finite sum of its terms $a_i X^i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Degree/Support.html#Polynomial.as_sum_range_C_mul_X_pow),
which justifies the usual notation. Even when $R$ is not commutative,
[$X$ commutes with every polynomial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial.X_mul).

The degree of a nonzero polynomial $f$ is the largest $n$ with $a_n \neq 0$, and $a_n$ is its
leading coefficient; $f$ is monic if its leading coefficient is $1$. The zero polynomial has
no nonzero coefficient, and its degree is set to $-\infty$.

When $R$ is commutative, a polynomial $f = a_0 + a_1 X + \dots + a_n X^n$ can be evaluated at
an element $x$ of $R$: [its value is $f(x) = a_0 + a_1 x + \dots + a_n x^n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Defs.html#Polynomial.eval),
and $x$ is [a root of $f$ when $f(x) = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Defs.html#Polynomial.IsRoot).

## Examples

- Over the rational numbers, $X^2 - 2$ is monic of degree $2$; over the real numbers it
  factors as $(X - \sqrt 2)(X + \sqrt 2)$.
- A polynomial is not the same thing as the function it defines. Over the field
  $\mathbb{Z}/p\mathbb{Z}$ with $p$ prime, [the polynomial $X^p - X$ is nonzero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Degree/Operations.html#Polynomial.X_pow_sub_X_ne_zero),
  since its degree $p$ exceeds $1$, yet by [Fermat's little theorem](../../../thousand-plus/number-theory/part-02/fermats-little-theorem.md)
  [$a^p = a$ for every $a$ in $\mathbb{Z}/p\mathbb{Z}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#ZMod.pow_card), so it vanishes at every point.
- Over $\mathbb{Z}/4\mathbb{Z}$ the polynomial $1 + 2X$ is invertible, because
  $(1 + 2X)^2 = 1 + 4X + 4X^2 = 1$. Here the coefficient $2$ is nilpotent, since $2^2 = 0$.
  Over a commutative ring,
  [a polynomial is a unit exactly when its constant term is a unit and all its other coefficients are nilpotent](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Nilpotent.html#Polynomial.isUnit_iff_coeff_isUnit_isNilpotent),
  so nilpotent coefficients, not zero divisors in general, are what allow units of positive
  degree: $\mathbb{Z}/6\mathbb{Z}$ has zero divisors but no nonzero nilpotents, and every unit
  of $(\mathbb{Z}/6\mathbb{Z})[X]$ is constant.

## Properties

- **Degree of a product.** If $R$ has no zero divisors, then
  [$\deg(fg) = \deg f + \deg g$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Degree/Operations.html#Polynomial.degree_mul), with the convention
  $-\infty + n = -\infty$. Hence $R[X]$ has no zero divisors when $R$ has none, and since $R$
  sits inside $R[X]$ as the constants,
  [$R[X]$ has no zero divisors exactly when $R$ has none](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial.noZeroDivisors_iff).
  When $R$ has no zero divisors, the degree formula also shows that
  [the units of $R[X]$ are the constant polynomials whose value is a unit of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Degree/Units.html#Polynomial.isUnit_iff).
- **Division with remainder.** Over a nonzero ring $R$, let $g$ be monic. Every $f$ can be
  written as [$f = gq + r$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.modByMonic_add_div) with a remainder $r$ satisfying
  [$\deg r < \deg g$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.degree_modByMonic_lt). When the coefficients form a
  [field](../field-theory/field.md) $K$, every nonzero $g$ can be made monic, and
  [$K[X]$ is a Euclidean domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.instEuclideanDomain) (see
  [$K[X]$ is Euclidean](k-x-is-euclidean.md)).
- **Roots.** For a commutative ring $R$ and $a$ in $R$,
  [$X - a$ divides $f$ if and only if $f(a) = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.dvd_iff_isRoot) (the
  [factor theorem](../../../hundred-theorems/part-05/the-factor-and-remainder-theorems.md)). If moreover $R$ is an integral domain,
  [a nonzero polynomial $f$ has at most $\deg f$ roots, counted with multiplicity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.card_roots');
  see [roots of a polynomial](roots-of-a-polynomial.md). Hence over an infinite integral domain
  [two polynomials that take the same value at every point are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.funext).
- **Universal property.** Let $R$ be commutative and $A$ an [$R$-algebra](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md).
  [Algebra homomorphisms from $R[X]$ to $A$ correspond one to one to elements of $A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/AlgebraMap.html#Polynomial.aevalEquiv):
  each $x$ in $A$ gives the evaluation map $f \mapsto f(x)$, and each homomorphism is determined
  by the image of $X$. More generally, a [ring morphism](../rings/ring-morphism.md) $\varphi$ from $R$ to a
  commutative ring $S$ and an element $s$ of $S$
  [give a ring morphism from $R[X]$ to $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Eval/Defs.html#Polynomial.eval%E2%82%82RingHom) that applies $\varphi$
  to the coefficients and substitutes $s$ for $X$; see [polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md).
- **Finiteness.** By the [Hilbert basis theorem](hilbert-basis-theorem.md),
  [if a commutative ring $R$ is Noetherian, then so is $R[X]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Basic.html#Polynomial.isNoetherianRing)
  (see [Noetherian ring](../rings/noetherian-ring.md)).

## Related concepts

Iterating the construction, or allowing any set of indeterminates, gives
[polynomials in several indeterminates](polynomial-in-several-indeterminates.md); dropping the finiteness
condition on the coefficients gives [formal power series](power-series.md). Within $R[X]$
one studies [irreducible polynomials](../divisibility-in-integral-domains/irreducible-element.md), with tests such as
[Eisenstein's criterion](eisensteins-criterion.md), the
[formal derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md) and
[separable polynomials](separable-polynomial.md). Quotients of $K[X]$ by an irreducible
polynomial build field extensions, as in the [rupture field](../field-theory/rupture-field.md) and the
[splitting field](../field-theory/splitting-field.md).

## In Mathlib

Mathlib defines polynomials over any semiring, commutative or not, so that the natural numbers
and other semirings without subtraction are allowed as coefficients; results that need
negatives, commutativity or the absence of zero divisors carry those as hypotheses. A
polynomial is stored as a finitely supported function from the natural numbers to the
coefficients, wrapped in its own structure so that it is used only through its own interface;
the constant polynomials come from a ring morphism from $R$ into $R[X]$, and $X$ is a separate
element. Mathlib has two notions of degree: one with values in the natural numbers extended by
a bottom element, where [the zero polynomial has degree bottom](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Degree/Defs.html#Polynomial.degree_zero),
playing the role of $-\infty$, and one with natural-number values, where
[the zero polynomial has degree $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Degree/Defs.html#Polynomial.natDegree_zero). The bound on the number
of roots appears in both forms: with the first for nonzero polynomials, and with the second for
all polynomials, the zero polynomial included, since Mathlib assigns it no roots. Division by
a monic polynomial is defined for every divisor, monic or not, and the identity $f = gq + r$
holds in all cases, with a quotient of zero when the divisor is not monic; only the degree
bound on the remainder needs a monic divisor and a nonzero ring. Over a field, a separate
division operation divides by any nonzero polynomial.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Finitely supported function](../../data-structures/maps/finitely-supported-function.md)

## Sources

- [Mathlib documentation: `Polynomial`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Basic.html#Polynomial)
- [Source of `Polynomial` in Mathlib/Algebra/Polynomial/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Basic.lean#L63)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L96)
