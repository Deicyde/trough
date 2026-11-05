---
article_id: af_68e1ab5432b474b960705a24
concept: Polynomial.rootMultiplicity
---

The **multiplicity** of a root $a$ of a [polynomial](trough:Polynomial) $p$ is the number of times the linear factor $X - a$ occurs in $p$: the largest $m$ such that $(X - a)^m$ divides $p$. It refines the yes-or-no question "is $a$ a root?" into a count, distinguishing simple roots from double and higher roots. Counting roots with multiplicity is what makes statements such as "a polynomial of degree $n$ over the complex numbers has exactly $n$ roots" true, and multiplicity is closely tied to the [derivative](trough:Polynomial.derivative) of a polynomial and to separability.

## Definition

Let $R$ be a commutative [ring](trough:Ring), $p$ a nonzero polynomial with coefficients in $R$, and $a$ an element of $R$. The multiplicity of $a$ as a root of $p$ is
[the largest natural number $m$ such that $(X - a)^m$ divides $p$](lean:Polynomial.rootMultiplicity).
Such a largest $m$ exists because $X - a$ is monic, so a power of it that divides $p$ cannot have degree larger than that of $p$. Equivalently, for a nonzero $p$ and every $n$,
[$(X - a)^n$ divides $p$ exactly when $n$ is at most the multiplicity](lean:Polynomial.le_rootMultiplicity_iff).
In particular, if $m$ is the multiplicity of $a$ in a nonzero $p$, then [$p = (X - a)^m q$ for a polynomial $q$ not divisible by $X - a$](lean:Polynomial.exists_eq_pow_rootMultiplicity_mul_and_not_dvd). By the [factor theorem](trough:Polynomial.dvd_iff_isRoot), [$X - a$ divides $q$ exactly when $q(a) = 0$](lean:Polynomial.dvd_iff_isRoot), so the condition on $q$ says $q(a) \neq 0$.

For a nonzero $p$, [the multiplicity of $a$ is positive exactly when $a$ is a root of $p$](lean:Polynomial.rootMultiplicity_pos), so elements that are not roots have multiplicity $0$. A root of multiplicity $1$ is called simple, and a root of multiplicity at least $2$ is called a multiple (double, triple, ...) root. The zero polynomial is divisible by every power of $X - a$; by convention its multiplicity at every point is [$0$](lean:Polynomial.rootMultiplicity_zero).

## Examples

- Over the rational numbers, $p = X^3 - 3X + 2 = (X - 1)^2 (X + 2)$. The root $1$ has multiplicity $2$, the root $-2$ has multiplicity $1$, and every other number has multiplicity $0$. The multiplicities add up to $3$, the degree of $p$.
- Over any nonzero commutative ring, [the multiplicity of $a$ as a root of $(X - a)^n$ is $n$](lean:Polynomial.rootMultiplicity_X_sub_C_pow).
- At the point $0$, [the multiplicity of a nonzero polynomial is the smallest exponent of $X$ that appears in $p$ with a nonzero coefficient](lean:Polynomial.rootMultiplicity_eq_natTrailingDegree'); for instance $X^5 + X^3$ has a root of multiplicity $3$ at $0$. More generally, [the multiplicity of a nonzero $p$ at $a$ is the smallest exponent of $X$ that appears with a nonzero coefficient in the polynomial $p(X + a)$](lean:Polynomial.rootMultiplicity_eq_natTrailingDegree), which is $p$ rewritten so that the point $a$ moves to $0$.
- The polynomial $X^2 + 1$ has no real roots, so all its multiplicities over the real numbers are $0$; over the complex numbers it factors as $(X - i)(X + i)$ and has two simple roots.

## Properties

- **Products.** Over an integral domain, if $p$ and $q$ are nonzero then
  [the multiplicity of $a$ in $pq$ is the sum of its multiplicities in $p$ and in $q$](lean:Polynomial.rootMultiplicity_mul).
  Over an arbitrary commutative ring only an inequality survives: if $pq \neq 0$,
  [the multiplicity in $pq$ is at least the sum](lean:Polynomial.le_rootMultiplicity_mul).
- **Sums.** If $p + q \neq 0$, then
  [the multiplicity of $a$ in $p + q$ is at least the smaller of its multiplicities in $p$ and in $q$](lean:Polynomial.rootMultiplicity_add).
- **Counting roots.** Over an integral domain the [roots](trough:Polynomial.roots) of $p$ form a multiset in which
  [each element occurs as often as its multiplicity](lean:Polynomial.count_roots).
  Since, for nonzero $p$, the product of the factors $(X - a)^m$ over the roots divides $p$, the
  [number of roots counted with multiplicity is at most the degree of $p$](lean:Polynomial.card_roots'),
  and over an [algebraically closed field](trough:IsAlgClosed) such as the complex numbers (by the [fundamental theorem of algebra](trough:Complex.isAlgClosed))
  [it equals the degree](lean:IsAlgClosed.card_roots_eq_natDegree).
- **Derivative test.** Over a commutative ring, for nonzero $p$,
  [$a$ has multiplicity at least $2$ exactly when both $p(a) = 0$ and $p'(a) = 0$](lean:Polynomial.one_lt_rootMultiplicity_iff_isRoot), where $p'$ is the derivative of $p$.
  In characteristic zero more is true: over a commutative ring of [characteristic zero](trough:CharZero) without zero divisors,
  [if $a$ is a root of a nonzero polynomial $p$ with multiplicity $m$, then the multiplicity of $a$ as a root of $p'$ is $m - 1$](lean:Polynomial.derivative_rootMultiplicity_of_root).
  The reason is that writing $p = (X - a)^m q$ with $q$ not divisible by $X - a$ gives
  $$p' = (X - a)^{m-1} r, \qquad r = m\,q + (X - a)\,q',$$
  and $r(a) = m\,q(a)$. This value is nonzero: $m \geq 1$ because $a$ is a root, so $m \neq 0$ in $R$ by characteristic zero; $q(a) \neq 0$ by the factor theorem; and $R$ has no zero divisors. Hence $r$ is nonzero and not divisible by $X - a$. It follows that $p'$ is nonzero, that $(X - a)^{m-1}$ divides $p'$, and that $(X - a)^m$ does not, since cancelling the monic factor $(X - a)^{m-1}$ would make $X - a$ divide $r$. By the divisibility criterion in the Definition section, the multiplicity of $a$ in $p'$ is exactly $m - 1$.
- **Separable polynomials.** Over a nonzero commutative ring, a [separable polynomial](trough:Polynomial.Separable), one coprime to its derivative, has
  [no multiple roots: every multiplicity is at most $1$](lean:Polynomial.rootMultiplicity_le_one_of_separable).

The characteristic-zero hypothesis in the formula for the multiplicity of a root of $p'$ cannot be dropped. Over a field of [prime characteristic](trough:CharP) $\ell$, the polynomial $(X - a)^\ell$ has a root of multiplicity $\ell$ at $a$, but its derivative $\ell\,(X - a)^{\ell-1}$ is the zero polynomial, whose multiplicity at $a$ is $0$ by convention rather than $\ell - 1$.

## Related concepts

Multiplicity of a root is the special case of the multiplicity of a prime factor in a [unique factorisation domain](trough:UniqueFactorizationMonoid): over a [field](trough:Field) $K$, the polynomial ring $K[X]$ is such a domain and $X - a$ is one of its prime elements. The same idea gives the order of vanishing of an analytic function at a point, the valuation of an integer at a prime, and the intersection multiplicities of algebraic geometry.

## In Mathlib

Mathlib defines the multiplicity for polynomials over an arbitrary ring, commutative or not, as a natural number, and it assigns the value $0$ to the zero polynomial instead of infinity. With that convention, [the multiplicity is $0$ for the zero polynomial and, for a nonzero polynomial, agrees with Mathlib's general multiplicity of $X - a$ as a divisor of $p$](lean:Polynomial.rootMultiplicity_eq_multiplicity). Many of the statements above therefore carry a hypothesis that some polynomial is nonzero, and additivity over products is proved for integral domains. The derivative test in characteristic zero is a corollary of a sharper statement: over any commutative ring, [if $a$ is a root of a nonzero polynomial $p$ whose multiplicity $m$, viewed as an element of the ring, is not a zero divisor, then the multiplicity of $a$ as a root of $p'$ is $m - 1$](lean:Polynomial.derivative_rootMultiplicity_of_root_of_mem_nonZeroDivisors).

## Depends on

- [Polynomial in one indeterminate](trough:Polynomial)
- [Ring](trough:Ring)
- [Polynomial functions](trough:Polynomial.eval)
- [The Factor and Remainder Theorems](trough:Polynomial.dvd_iff_isRoot)

## Proof depends on

- [Polynomial derivative](trough:Polynomial.derivative)
- [Characteristic zero](trough:CharZero)
