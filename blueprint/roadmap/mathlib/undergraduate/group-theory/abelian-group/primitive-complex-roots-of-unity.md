---
article_id: af_849285d1717f7195381a22d5
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Complex.isPrimitiveRoot_iff
mathlib_file: Mathlib/RingTheory/RootsOfUnity/Complex.lean
---

# Primitive complex roots of unity

For a positive integer $n$, a **primitive $n$-th root of unity** is a [complex number](../../../overview/general-algebra/numbers/complex-number.md) $\zeta$ with
$\zeta^n = 1$ whose powers $\zeta, \zeta^2, \dots, \zeta^{n-1}$ all differ from $1$. The
primitive $n$-th roots are the generators of the cyclic group of
[complex $n$-th roots of unity](complex-roots-of-unity.md), and they have an explicit
description: they are the numbers $e^{2\pi i k/n}$ with $k$ coprime to $n$. They are the
roots of the [cyclotomic polynomials](../../ring-theory/polynomial-rings/cyclotomic-polynomials-in-q-x.md), and they appear
throughout algebra and number theory, from the structure of finite cyclic groups to
Fourier analysis on them.

## Definition

Let $n \ge 1$. A complex number $\zeta$ is a primitive $n$-th root of unity when
[$\zeta^n = 1$ and $\zeta^m \neq 1$ for every $m$ with $0 < m < n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.iff).
Equivalently, $\zeta$ has [order](../basic-definitions/order-of-an-element.md) exactly $n$ in the multiplicative group of
nonzero complex numbers: [$\zeta$ is a primitive $n$-th root precisely when its order is $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.iff_orderOf).

## Statement

For $n \ge 1$, the primitive $n$-th roots of unity in $\mathbb{C}$ are
[exactly the numbers $e^{2\pi i k/n}$ with $0 \le k < n$ and $\gcd(k, n) = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_iff).
These numbers lie on the unit circle at the angles $2\pi k/n$, and distinct values of $k$ in
this range give distinct numbers, so
[there are exactly $\varphi(n)$ primitive $n$-th roots of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.card_primitiveRoots),
where $\varphi$ is [Euler's totient function](../../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md).

## Examples

- For $n = 1$ the only primitive root is $1$ itself, and for $n = 2$ it is $-1$.
- For $n = 4$ the primitive roots are $i$ and $-i$: [$i$ is a primitive fourth root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_I), and so is
  [$-i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_neg_I), while $-1$ is not, since $(-1)^2 = 1$.
- For $n = 3$ the primitive roots are $\tfrac{-1 \pm i\sqrt{3}}{2}$, and for $n = 6$ they are
  $\tfrac{1 \pm i\sqrt{3}}{2}$.
- For every $n \ge 1$, [the number $e^{2\pi i/n}$ is a primitive $n$-th root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_exp).
- More generally, if $q = a/b$ is a rational number in lowest terms with $b \ge 1$, then
  [$e^{2\pi i q}$ is a primitive $b$-th root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_exp_rat).

## Proof

Write $\omega = e^{2\pi i/n}$. By the periodicity of the
[complex exponential](../../single-variable-complex-analysis/complex-valued-series/complex-exponential.md), $\omega^m = e^{2\pi i m/n}$ equals $1$ exactly when
$n$ divides $m$, so $\omega$ has order $n$. The $n$ numbers $1, \omega, \dots, \omega^{n-1}$
are distinct roots of $x^n - 1$, a polynomial with at most $n$ roots, so every $n$-th root of
unity is $\omega^k = e^{2\pi i k/n}$ for a unique $k$ with $0 \le k < n$. Finally, the order of
$\omega^k$ is $n/\gcd(k, n)$, which equals $n$ exactly when $\gcd(k, n) = 1$.

## Properties

Throughout, $n \ge 1$ and $\zeta$ is a primitive $n$-th root of unity.

- **Generators.** Every $n$-th root of unity is a power of $\zeta$:
  [each $\xi$ with $\xi^n = 1$ equals $\zeta^k$ for some $k$ with $0 \le k < n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.eq_pow_of_pow_eq_one).
  So the $n$-th roots of unity form a [cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md) of order $n$, and its
  generators are exactly the primitive $n$-th roots of unity.
- **Powers.** [The power $\zeta^k$ is a primitive $n$-th root exactly when $\gcd(k, n) = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.pow_iff_coprime), and in general
  [$\zeta^k$ is a primitive $(n/\gcd(n, k))$-th root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.pow_div_gcd).
  Thus the primitive $n$-th roots correspond to the
  [invertible residues modulo $n$](../../ring-theory/divisibility-in-integral-domains/z-n-z-and-its-invertible-elements.md).
- **Absolute value.** [Every primitive $n$-th root has absolute value $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#IsPrimitiveRoot.norm'_eq_one).
- **Vanishing sum.** For $n \ge 2$,
  [$1 + \zeta + \zeta^2 + \cdots + \zeta^{n-1} = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.geom_sum_eq_zero),
  because the sum is a geometric series and $\zeta^n = 1$ while $\zeta \neq 1$.
- **Sorting the roots of unity by order.** A complex number is a primitive root of unity for
  at most one exponent: [if $\zeta$ is a primitive $k$-th root and a primitive $l$-th root, then $k = l$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.unique). Each $n$-th root of unity has some order $d$
  dividing $n$, so [the $n$-th roots of unity are the union, over the divisors $d$ of $n$, of the primitive $d$-th roots](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.nthRoots_one_eq_biUnion_primitiveRoots).
  Counting both sides gives the identity
  [$\sum_{d \mid n} \varphi(d) = n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Nat/Totient.html#Nat.sum_totient).

## Cyclotomic polynomials

The $n$-th cyclotomic polynomial $\Phi_n$ collects the primitive $n$-th roots. In any integral domain
that contains a primitive $n$-th root of unity, such as $\mathbb{C}$,
[the polynomial $\Phi_n$ is the product of $x - \zeta$ over the primitive $n$-th roots $\zeta$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Basic.html#Polynomial.cyclotomic_eq_prod_X_sub_primitiveRoots), and for $n \ge 1$
[a complex number is a root of $\Phi_n$ exactly when it is a primitive $n$-th root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Roots.html#Polynomial.isRoot_cyclotomic_iff). Its
[degree is $\varphi(n)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Basic.html#Polynomial.natDegree_cyclotomic). [Its coefficients are integers: over any ring, $\Phi_n$ is the image of the integer polynomial $\Phi_n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Basic.html#Polynomial.map_cyclotomic_int), and for $n \ge 1$ [it is irreducible over the rationals](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Roots.html#Polynomial.cyclotomic.irreducible_rat),
so all primitive $n$-th roots are conjugate algebraic numbers.

## In Mathlib

Mathlib defines primitive roots of unity for an element of any commutative monoid, not only
for complex numbers: $\zeta$ is a primitive $n$-th root when $\zeta^n = 1$ and $n$ divides
every exponent $m$ with $\zeta^m = 1$. This agrees with the definition above for $n \ge 1$,
but it also gives a meaning to $n = 0$: a primitive $0$-th root is an element none of whose
positive powers is $1$. In $\mathbb{C}$ every number that is not a root of unity, $0$ and $2$
among them, is a primitive $0$-th root, which is why the description by exponentials assumes
$n \neq 0$. This matches the convention that an element of infinite order has order $0$. The
finite set of primitive $n$-th roots is taken to be empty for $n = 0$, consistent with
$\varphi(0) = 0$, so the count of primitive roots holds for every $n$. The theorems on
generators, vanishing sums, the decomposition by divisors, and the product and root
descriptions of $\Phi_n$ are proved in any integral domain, not only in $\mathbb{C}$; there
the root criterion for $\Phi_n$ asks that $n$ be nonzero as an element of the domain. The
lemmas on powers of a primitive root hold in any commutative monoid, the degree formula holds
over any nontrivial ring, and irreducibility is stated over $\mathbb{Q}$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Complex exponential](../../single-variable-complex-analysis/complex-valued-series/complex-exponential.md)
- [Complex roots of unity](complex-roots-of-unity.md)
- [Order of an element](../basic-definitions/order-of-an-element.md)
- [Euler's totient function ($\varphi$)](../../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)

## Proof depends on

- [Roots of a polynomial](../../../overview/general-algebra/polynomials-and-power-series/roots-of-a-polynomial.md)

## Sources

- [Mathlib documentation: `Complex.isPrimitiveRoot_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_iff)
- [Source of `Complex.isPrimitiveRoot_iff` in Mathlib/RingTheory/RootsOfUnity/Complex.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/RootsOfUnity/Complex.lean#L97)
- [Mathlib undergraduate list: Group Theory › Abelian group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L97)
