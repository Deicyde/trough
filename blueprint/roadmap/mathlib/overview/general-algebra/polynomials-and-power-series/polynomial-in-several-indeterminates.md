---
article_id: af_8e6c83f35d6727013a83d4f8
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: MvPolynomial
mathlib_file: Mathlib/Algebra/MvPolynomial/Basic.lean
---

# Polynomial in several indeterminates

A **polynomial in several indeterminates** over a commutative [ring](../rings/ring.md) $R$ is a
finite sum of terms $c\,X_1^{a_1}X_2^{a_2}\cdots X_n^{a_n}$ with coefficients $c$ in $R$,
such as $x^2 + y^2 - 1$ or $xyz - 2$. These polynomials form a commutative ring,
written $R[X_1, \dots, X_n]$ or $R[X_i : i \in I]$, which generalizes the
[polynomials in one indeterminate](polynomial-in-one-indeterminate.md). It is a basic object of
commutative algebra and algebraic geometry: every finitely generated commutative
$R$-algebra is a quotient of such a ring, and the solution sets of systems of polynomial
equations are studied through its [ideals](../ideals-and-quotients/ideal-of-a-commutative-ring.md).

## Definition

Let $R$ be a commutative ring and $I$ a set indexing the indeterminates; $I$ may be
infinite. An exponent vector is a function $\alpha \colon I \to \mathbb{N}$ that is
zero outside a finite set (a [finitely supported function](../../data-structures/maps/finitely-supported-function.md)), and to each
exponent vector corresponds a monomial

$$X^\alpha = \prod_{i \in I} X_i^{\alpha(i)},$$

a finite product since almost all exponents vanish. A polynomial is a formal finite sum
$p = \sum_\alpha p_\alpha X^\alpha$, that is, a function $\alpha \mapsto p_\alpha$ from
exponent vectors to $R$ with only finitely many nonzero values. Polynomials are added
coefficientwise, and multiplied by extending the rule
[$X^\alpha \cdot X^\beta = X^{\alpha + \beta}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial.monomial_mul_monomial)
bilinearly, so that

$$(pq)_\gamma = \sum_{\alpha + \beta = \gamma} p_\alpha\, q_\beta.$$

The result is the [polynomial ring in the indeterminates $X_i$ with coefficients in $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial).
By construction, [two polynomials with the same coefficient at every monomial are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial.ext),
and [every polynomial is the sum of its finitely many nonzero terms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial.as_sum).
Each term is a constant times a product of powers of indeterminates:
[$c\,X^\alpha$ is the constant $c$ times $\prod_i X_i^{\alpha(i)}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial.monomial_eq).
The map sending $c$ to the constant polynomial $c$ is
[injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial.C_injective), so $R$ sits inside the polynomial ring.

The total degree of a nonzero polynomial is the largest value of
$\sum_i \alpha(i)$ over the exponent vectors $\alpha$ with $p_\alpha \neq 0$; for
example $x^3 y + y^2$ has total degree $4$.

## Examples

- With no indeterminates, the polynomial ring is
  [$R$ itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Equiv.html#MvPolynomial.isEmptyAlgEquiv); with exactly one, it is
  [the ring $R[X]$ of polynomials in one indeterminate](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Equiv.html#MvPolynomial.uniqueAlgEquiv).
- Polynomials in $n + 1$ indeterminates are the same as
  [polynomials in one indeterminate whose coefficients are polynomials in the other $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Equiv.html#MvPolynomial.finSuccEquiv);
  more generally, splitting the indeterminates into two sets $I$ and $J$ identifies
  $R[X_i, Y_j]$ with [$(R[Y_j])[X_i]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Equiv.html#MvPolynomial.sumAlgEquiv). This identification
  lets many properties pass from one indeterminate to finitely many by induction.
- In three indeterminates, $X_1X_2 + X_1X_3 + X_2X_3$ is unchanged by any permutation
  of the indeterminates; it is one of the elementary
  [symmetric polynomials](../../../undergraduate/ring-theory/polynomial-rings/symmetric-polynomials.md).
- The determinant of an $n \times n$ matrix is a polynomial with integer coefficients
  in its $n^2$ entries, regarded as indeterminates.

## Properties

**Universal property.** For every commutative $R$-algebra $A$ (see
[associative algebra](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)) and every family $(a_i)_{i \in I}$ of elements of
$A$, there is an $R$-algebra homomorphism from $R[X_i : i \in I]$ to $A$
[sending each $X_i$ to $a_i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Eval.html#MvPolynomial.aeval_X), and
[it is the only $R$-algebra homomorphism that agrees with it on every $X_i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial.algHom_ext).
This homomorphism is evaluation, or substitution, at the point $(a_i)$. In this sense
the polynomial ring is the free commutative $R$-algebra on the set $I$; dropping
commutativity gives the [free algebra](../algebras-over-a-ring/free-algebra-of-a-commutative-ring.md). Polynomials also admit
induction: [a statement that holds for constants, is preserved by sums, and is preserved by multiplication by an indeterminate holds for every polynomial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial.induction_on).

**Ring-theoretic properties.**

- If $R$ is an integral domain, so is $R[X_i : i \in I]$. The ring is nonzero because $R$
  sits inside it. To see that it has no zero divisors, fix a monomial order, such as the
  lexicographic order: a total order on monomials, compatible with multiplication, in
  which $1$ is the smallest monomial. The leading coefficient of a nonzero polynomial is
  its coefficient at its largest monomial, so it is nonzero. If $R$ has no zero divisors,
  [the leading coefficient of $pq$ is the product of the leading coefficients of $p$ and $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPolynomial/MonomialOrder.html#MonomialOrder.leadingCoeff_mul),
  so for nonzero $p$ and $q$ it is nonzero, and hence $pq \neq 0$. Comparing leading
  monomials under an order that ranks monomials first by degree shows, in the same way,
  that [for nonzero $p$ and $q$ the total degree of $pq$ is the sum of the total degrees of $p$ and $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/NoZeroDivisors.html#MvPolynomial.totalDegree_mul_of_isDomain).
- If $R$ is a [unique factorisation domain](../divisibility-in-integral-domains/unique-factorisation-domain.md), so is the
  polynomial ring in any set of indeterminates
  (see [unique factorisation in polynomial rings](a-x-i-is-a-ufd-when-a-is-a-ufd.md)).
- By the [Hilbert basis theorem](hilbert-basis-theorem.md) and induction on the
  number of indeterminates, if $R$ is a [Noetherian ring](../rings/noetherian-ring.md) then
  [so is the polynomial ring in finitely many indeterminates over $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Basic.html#MvPolynomial.isNoetherianRing).
  With infinitely many indeterminates over a nonzero ring this fails: the ideal generated
  by all the $X_i$ is not finitely generated.

**Polynomials and functions.** Each polynomial $p$ over $R$ defines a function
$R^I \to R$ by [evaluation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Eval.html#MvPolynomial.eval). If $R$ is an infinite integral domain,
[two polynomials that agree at every point of $R^I$ are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Funext.html#MvPolynomial.funext),
so polynomials may be identified with the functions they define. Over a finite field
this fails: over a field with $q$ elements, $X_1^q - X_1$ is a nonzero polynomial that
vanishes at every point.

## Related concepts

Every polynomial is uniquely a sum of homogeneous polynomials, one in each total degree
(see [decomposition into homogeneous components](../../../undergraduate/ring-theory/polynomial-rings/decomposition-into-sums-of-homogeneous-polynomia.md)).
The [Nullstellensatz](../../geometry/algebraic-geometry/nullstellensatz.md) describes,
over an algebraically closed field, which polynomials in finitely many indeterminates
vanish on the common zeros of an ideal, and the
[Schwartz–Zippel theorem](../../../thousand-plus/algebra/12-field-theory-and-polynomials/schwartz-zippel-theorem.md) bounds how many
points of a finite grid a nonzero polynomial over an integral domain can vanish at.
Allowing infinite sums of monomials in one indeterminate gives
[power series](power-series.md).

## In Mathlib

Mathlib allows the coefficients to lie in any commutative semiring, so polynomials with
natural-number coefficients are covered, and indexes the indeterminates by an arbitrary
type, which may be infinite. A polynomial is literally a finitely supported function
from exponent vectors to coefficients, and exponent vectors are themselves finitely
supported functions from the index type to the natural numbers; multiplication is the
convolution of the monoid algebra of the exponent vectors. Polynomials in one
indeterminate form a separate type, related to the several-indeterminate version with a
one-element index type by an isomorphism of algebras. The total degree is a natural
number, and the zero polynomial is given total degree $0$, so the additivity of total
degree under multiplication requires both factors to be nonzero. The integral domain
property holds over any semiring that is a domain and has cancellative addition, which
for a ring is automatic.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Finitely supported function](../../data-structures/maps/finitely-supported-function.md)

## Sources

- [Mathlib documentation: `MvPolynomial`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/MvPolynomial/Basic.html#MvPolynomial)
- [Source of `MvPolynomial` in Mathlib/Algebra/MvPolynomial/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/MvPolynomial/Basic.lean#L78)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L106)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L162)
