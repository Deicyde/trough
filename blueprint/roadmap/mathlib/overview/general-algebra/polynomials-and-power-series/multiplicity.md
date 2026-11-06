# Multiplicity

The **multiplicity** of a root $a$ of a [polynomial](polynomial-in-one-indeterminate.md) $p$ is the number of times the linear factor $X - a$ occurs in $p$: the largest $m$ such that $(X - a)^m$ divides $p$. It refines the yes-or-no question "is $a$ a root?" into a count, distinguishing simple roots from double and higher roots. Counting roots with multiplicity is what makes statements such as "a polynomial of degree $n$ over the complex numbers has exactly $n$ roots" true, and multiplicity is closely tied to the [derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md) of a polynomial and to separability.

## Definition

Let $R$ be a commutative [ring](../rings/ring.md), $p$ a nonzero polynomial with coefficients in $R$, and $a$ an element of $R$. The multiplicity of $a$ as a root of $p$ is
[the largest natural number $m$ such that $(X - a)^m$ divides $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity).
Such a largest $m$ exists because $X - a$ is monic, so a power of it that divides $p$ cannot have degree larger than that of $p$. Equivalently, for a nonzero $p$ and every $n$,
[$(X - a)^n$ divides $p$ exactly when $n$ is at most the multiplicity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.le_rootMultiplicity_iff).
In particular, if $m$ is the multiplicity of $a$ in a nonzero $p$, then [$p = (X - a)^m q$ for a polynomial $q$ not divisible by $X - a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.exists_eq_pow_rootMultiplicity_mul_and_not_dvd). By the [factor theorem](../../../hundred-theorems/part-04/the-factor-and-remainder-theorems.md), [$X - a$ divides $q$ exactly when $q(a) = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.dvd_iff_isRoot), so the condition on $q$ says $q(a) \neq 0$.

For a nonzero $p$, [the multiplicity of $a$ is positive exactly when $a$ is a root of $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity_pos), so elements that are not roots have multiplicity $0$. A root of multiplicity $1$ is called simple, and a root of multiplicity at least $2$ is called a multiple (double, triple, ...) root. The zero polynomial is divisible by every power of $X - a$; by convention its multiplicity at every point is [$0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity_zero).

## Examples

- Over the rational numbers, $p = X^3 - 3X + 2 = (X - 1)^2 (X + 2)$. The root $1$ has multiplicity $2$, the root $-2$ has multiplicity $1$, and every other number has multiplicity $0$. The multiplicities add up to $3$, the degree of $p$.
- Over any nonzero commutative ring, [the multiplicity of $a$ as a root of $(X - a)^n$ is $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/RingDivision.html#Polynomial.rootMultiplicity_X_sub_C_pow).
- At the point $0$, [the multiplicity of a nonzero polynomial is the smallest exponent of $X$ that appears in $p$ with a nonzero coefficient](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity_eq_natTrailingDegree'); for instance $X^5 + X^3$ has a root of multiplicity $3$ at $0$. More generally, [the multiplicity of a nonzero $p$ at $a$ is the smallest exponent of $X$ that appears with a nonzero coefficient in the polynomial $p(X + a)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/RingDivision.html#Polynomial.rootMultiplicity_eq_natTrailingDegree), which is $p$ rewritten so that the point $a$ moves to $0$.
- The polynomial $X^2 + 1$ has no real roots, so all its multiplicities over the real numbers are $0$; over the complex numbers it factors as $(X - i)(X + i)$ and has two simple roots.

## Properties

- **Products.** Over an integral domain, if $p$ and $q$ are nonzero then
  [the multiplicity of $a$ in $pq$ is the sum of its multiplicities in $p$ and in $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/RingDivision.html#Polynomial.rootMultiplicity_mul).
  Over an arbitrary commutative ring only an inequality survives: if $pq \neq 0$,
  [the multiplicity in $pq$ is at least the sum](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.le_rootMultiplicity_mul).
- **Sums.** If $p + q \neq 0$, then
  [the multiplicity of $a$ in $p + q$ is at least the smaller of its multiplicities in $p$ and in $q$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity_add).
- **Counting roots.** Over an integral domain the [roots](roots-of-a-polynomial.md) of $p$ form a multiset in which
  [each element occurs as often as its multiplicity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.count_roots).
  Since, for nonzero $p$, the product of the factors $(X - a)^m$ over the roots divides $p$, the
  [number of roots counted with multiplicity is at most the degree of $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Roots.html#Polynomial.card_roots'),
  and over an [algebraically closed field](../field-theory/algebraically-closed-field.md) such as the complex numbers (by the [fundamental theorem of algebra](../../analysis/complex-analysis/fundamental-theorem-of-algebra.md))
  [it equals the degree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/IsAlgClosed/Basic.html#IsAlgClosed.card_roots_eq_natDegree).
- **Derivative test.** Over a commutative ring, for nonzero $p$,
  [$a$ has multiplicity at least $2$ exactly when both $p(a) = 0$ and $p'(a) = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.one_lt_rootMultiplicity_iff_isRoot), where $p'$ is the derivative of $p$.
  In characteristic zero more is true: over a commutative ring of [characteristic zero](../field-theory/characteristic-zero.md) without zero divisors,
  [if $a$ is a root of a nonzero polynomial $p$ with multiplicity $m$, then the multiplicity of $a$ as a root of $p'$ is $m - 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.derivative_rootMultiplicity_of_root).
  The reason is that writing $p = (X - a)^m q$ with $q$ not divisible by $X - a$ gives
  $$p' = (X - a)^{m-1} r, \qquad r = m\,q + (X - a)\,q',$$
  and $r(a) = m\,q(a)$. This value is nonzero: $m \geq 1$ because $a$ is a root, so $m \neq 0$ in $R$ by characteristic zero; $q(a) \neq 0$ by the factor theorem; and $R$ has no zero divisors. Hence $r$ is nonzero and not divisible by $X - a$. It follows that $p'$ is nonzero, that $(X - a)^{m-1}$ divides $p'$, and that $(X - a)^m$ does not, since cancelling the monic factor $(X - a)^{m-1}$ would make $X - a$ divide $r$. By the divisibility criterion in the Definition section, the multiplicity of $a$ in $p'$ is exactly $m - 1$.
- **Separable polynomials.** Over a nonzero commutative ring, a [separable polynomial](separable-polynomial.md), one coprime to its derivative, has
  [no multiple roots: every multiplicity is at most $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Separable.html#Polynomial.rootMultiplicity_le_one_of_separable).

The characteristic-zero hypothesis in the formula for the multiplicity of a root of $p'$ cannot be dropped. Over a field of [prime characteristic](../field-theory/characteristic-p.md) $\ell$, the polynomial $(X - a)^\ell$ has a root of multiplicity $\ell$ at $a$, but its derivative $\ell\,(X - a)^{\ell-1}$ is the zero polynomial, whose multiplicity at $a$ is $0$ by convention rather than $\ell - 1$.

## Related concepts

Multiplicity of a root is the special case of the multiplicity of a prime factor in a [unique factorisation domain](../divisibility-in-integral-domains/unique-factorisation-domain.md): over a [field](../field-theory/field.md) $K$, the polynomial ring $K[X]$ is such a domain and $X - a$ is one of its prime elements. The same idea gives the order of vanishing of an analytic function at a point, the valuation of an integer at a prime, and the intersection multiplicities of algebraic geometry.

## In Mathlib

Mathlib defines the multiplicity for polynomials over an arbitrary ring, commutative or not, as a natural number, and it assigns the value $0$ to the zero polynomial instead of infinity. With that convention, [the multiplicity is $0$ for the zero polynomial and, for a nonzero polynomial, agrees with Mathlib's general multiplicity of $X - a$ as a divisor of $p$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity_eq_multiplicity). Many of the statements above therefore carry a hypothesis that some polynomial is nonzero, and additivity over products is proved for integral domains. The derivative test in characteristic zero is a corollary of a sharper statement: over any commutative ring, [if $a$ is a root of a nonzero polynomial $p$ whose multiplicity $m$, viewed as an element of the ring, is not a zero divisor, then the multiplicity of $a$ as a root of $p'$ is $m - 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/FieldDivision.html#Polynomial.derivative_rootMultiplicity_of_root_of_mem_nonZeroDivisors).

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Polynomial in one indeterminate](polynomial-in-one-indeterminate.md)
- [Ring](../rings/ring.md)
- [Polynomial functions](../../../undergraduate/single-variable-real-analysis/elementary-functions-trigonometric-rational-exp/polynomial-functions.md)
- [The Factor and Remainder Theorems](../../../hundred-theorems/part-04/the-factor-and-remainder-theorems.md)

## Proof depends on

- [Polynomial derivative](../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Characteristic zero](../field-theory/characteristic-zero.md)

## Sources

- [Mathlib documentation: `Polynomial.rootMultiplicity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Polynomial/Div.html#Polynomial.rootMultiplicity)
- [Source of `Polynomial.rootMultiplicity` in Mathlib/Algebra/Polynomial/Div.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Polynomial/Div.lean#L501)
- [Mathlib overview: General algebra › Polynomials and power series](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L98)
- [Mathlib undergraduate list: Ring Theory › Polynomial rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L164)
