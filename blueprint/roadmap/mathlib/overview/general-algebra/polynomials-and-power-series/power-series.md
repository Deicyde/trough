---
article_id: af_f5919d26b748960d5f1abbc1
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: PowerSeries
mathlib_file: Mathlib/RingTheory/PowerSeries/Basic.lean
---

# Power series

A **formal power series** in one indeterminate $X$ over a [ring](../rings/ring.md) $R$ is an
expression $\sum_{n \ge 0} a_n X^n$ with coefficients $a_n$ in $R$, added and multiplied as
if it were a [polynomial](polynomial-in-one-indeterminate.md) that never ends. Nothing is evaluated and no
question of convergence arises: a power series is just its sequence of coefficients, and the
set $R[[X]]$ of all such series is made into a ring by a multiplication that extends that of
polynomials. Formal power series
extend polynomials, serve as generating functions in combinatorics, and supply the basic
examples of complete [local rings](../rings/local-ring.md) in commutative algebra.

## Definition

Let $R$ be a ring. A formal power series over $R$ is a sequence $(a_0, a_1, a_2, \dots)$ of
elements of $R$, written $f = \sum_{n \ge 0} a_n X^n$. The element $a_n$ is the $n$th
coefficient of $f$, and $a_0$ is its constant coefficient. Two power series
[with the same coefficients are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#PowerSeries.ext). Addition is
coefficientwise, and multiplication is the Cauchy product

$$\Big(\sum_{n \ge 0} a_n X^n\Big)\Big(\sum_{n \ge 0} b_n X^n\Big) = \sum_{n \ge 0} c_n X^n, \qquad c_n = \sum_{i + j = n} a_i b_j .$$

That is, [the $n$th coefficient of a product is $\sum_{i+j=n} a_i b_j$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#PowerSeries.coeff_mul),
a finite sum, so the product is defined without any limit. With these operations the
[formal power series over $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#PowerSeries) form a ring $R[[X]]$, commutative when $R$
is. The polynomial ring $R[X]$ sits inside it: sending a polynomial to the power series with
the same coefficients is [injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#Polynomial.coe_injective) and
[respects multiplication](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#Polynomial.coe_mul).

## Examples

- **Geometric series.** Over a commutative ring,
  [$(1 + X + X^2 + \cdots)(1 - X) = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/WellKnown.html#PowerSeries.mk_one_mul_one_sub_eq_one). So
  $1 - X$ is a unit in $R[[X]]$, although for $R \neq 0$ it is not a unit in $R[X]$.
- **Exponential series.** Over a ring containing the rational numbers, the series
  $e^X = \sum_{n \ge 0} X^n / n!$ makes sense. When the ring is commutative,
  its formal derivative (the series $\sum_{n \ge 0} (n+1) a_{n+1} X^n$ for $f = \sum a_n X^n$)
  [is $e^X$ itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Exp.html#PowerSeries.derivative_exp), and for elements $a$ and
  $b$ of the ring, [$e^{aX} e^{bX} = e^{(a+b)X}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Exp.html#PowerSeries.exp_mul_exp_eq_exp_add),
  where $e^{aX}$ is the series with $n$th coefficient $a^n / n!$.
- **Generating functions.** The series $C(X) = \sum_{n \ge 0} C_n X^n$ whose coefficients are
  the [Catalan numbers](../../combinatorics/enumerative-combinatorics/catalan-numbers.md) satisfies
  [$C(X) = 1 + X\,C(X)^2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Catalan.html#PowerSeries.catalanSeries_sq_mul_X_add_one), the identity that
  encodes their recursion. Euler's [pentagonal number theorem](../../../thousand-plus/number-theory/part-05/pentagonal-number-theorem.md)
  is likewise an identity between an infinite product and an infinite sum of power series.

## Properties

- **Units.** A series [is a unit if and only if its constant coefficient is a unit of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Inverse.html#PowerSeries.isUnit_iff_constantCoeff). If $a_0$ is invertible, the coefficients of
  the inverse $\sum b_n X^n$ are found one at a time from $a_0 b_0 = 1$ and
  $a_0 b_n + a_1 b_{n-1} + \cdots + a_n b_0 = 0$ for $n \ge 1$.
- **Divisibility by $X$.** The series $f$ is divisible by $X$
  [exactly when its constant coefficient is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#PowerSeries.X_dvd_iff), and more generally
  $X^n$ divides $f$ [exactly when $a_0, \dots, a_{n-1}$ all vanish](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#PowerSeries.X_pow_dvd_iff).
- **Order.** The order of a nonzero series is the least $n$ with $a_n \neq 0$; the zero series
  has order $\infty$. If $R$ has no zero divisors, then
  [the order of a product is the sum of the orders](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Order.html#PowerSeries.order_mul), so a product of
  nonzero series is nonzero. Hence $R[[X]]$ is an integral domain whenever $R$ is, and for a
  commutative integral domain $R$ the element [$X$ is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/NoZeroDivisors.html#PowerSeries.prime_X).
- **Power series over a field.** If $k$ is a [field](../field-theory/field.md), every nonzero series is
  $X^n u$ with $n$ its order and $u$ a unit, so $k[[X]]$ is a discrete valuation ring, that is,
  a local principal ideal domain that is not a field. Its
  [maximal ideal is generated by $X$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Inverse.html#PowerSeries.maximalIdeal_eq_span_X), and its nonzero
  ideals are the ideals generated by the powers of $X$.
- **Noetherian property.** Over a commutative [Noetherian ring](../rings/noetherian-ring.md),
  [power series in finitely many indeterminates again form a Noetherian ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MvPowerSeries/Equiv.html#MvPowerSeries.isNoetherianRing); for one indeterminate this is the power series
  analogue of the [Hilbert basis theorem](hilbert-basis-theorem.md).
- **Truncations.** If $R$ is a topological space, give $R[[X]]$ the coefficientwise (product)
  topology, in which a sequence of series converges exactly when, for each $n$, the sequence of
  $n$th coefficients converges in $R$. For $R$ commutative, the
  polynomials obtained by cutting $f$ off after more and more terms
  [converge to $f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/PiTopology.html#PowerSeries.WithPiTopology.tendsto_trunc_atTop). When $R$ carries the
  discrete topology this is the $X$-adic topology, in which $R[[X]]$ is the completion of
  $R[X]$: the polynomials are dense in it, and every Cauchy sequence in it converges.

## Related concepts

Power series in several indeterminates are defined the same way, with coefficients indexed by
monomials. The formal derivative of a power series extends the
[polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md). The
[Weierstrass preparation theorem](../../../thousand-plus/analysis/32-several-complex-variables-and-analytic-spaces/weierstrass-preparation-theorem.md)
factors a power series over a complete local ring, provided its reduction modulo the maximal
ideal is nonzero, as a polynomial of a special (distinguished) form times a unit. Convergent power series in
analysis, which define functions on a disc and have a
[radius of convergence](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/radius-of-convergence.md), are a separate notion; a
formal power series is the purely algebraic object that remains when convergence is ignored.

## In Mathlib

Mathlib defines power series in one indeterminate as the special case of power series in
several indeterminates whose set of indeterminates has a single element. A series is then a
function from exponents to coefficients, and a layer of basic lemmas lets one index
coefficients by natural numbers as usual. The definition accepts any coefficient type; the
ring structure requires $R$ to be a semiring, so series with natural-number coefficients, such
as the Catalan series, are covered directly. No topology is attached by default: the
coefficientwise topology is available only when explicitly switched on. The order of a series
takes values in the natural numbers extended by $\infty$. Over a field the inverse is defined
for every series, and [the inverse is $0$ exactly when the constant coefficient is $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Inverse.html#PowerSeries.inv_eq_zero), so it agrees with the true inverse precisely on the units.
Convergent power series of analysis are formalized separately, as formal multilinear series.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)

## Sources

- [Mathlib documentation: `PowerSeries`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PowerSeries/Basic.html#PowerSeries)
- [Source of `PowerSeries` in Mathlib/RingTheory/PowerSeries/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/PowerSeries/Basic.lean#L55)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L107)
