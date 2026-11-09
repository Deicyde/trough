# Complex roots of unity

The **complex roots of unity** are the [complex numbers](../../../overview/general-algebra/numbers/complex-number.md) $z$ that satisfy
$z^n = 1$ for some positive integer $n$. For each $n \ge 1$ the equation $z^n = 1$ has exactly $n$ solutions,
the numbers $e^{2\pi i k/n}$ with $0 \le k < n$, and they form a cyclic group of order $n$
under multiplication. They are the standard model of a finite [cyclic group](../../../overview/general-algebra/group-theory/part-01/cyclic-group.md),
they describe the regular polygons inscribed in the unit circle, and they are the roots of the
cyclotomic polynomials, the values of characters of finite abelian groups and the sample
points of the discrete Fourier transform.

## Definition

Let $n$ be a positive integer. A complex number $z$ is an **$n$-th root of unity** if
$z^n = 1$. Such a $z$ is nonzero, so it belongs to the multiplicative group
$\mathbb{C}^\times$ of nonzero complex numbers, and the $n$-th roots of unity form
[the subgroup of $\mathbb{C}^\times$ of elements whose $n$-th power is $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Basic.html#rootsOfUnity),
usually written $\mu_n$: [a unit lies in it exactly when its $n$-th power is $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Basic.html#mem_rootsOfUnity).
It is a [subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md) because $1^n = 1$, $(zw)^n = z^n w^n$ and $(z^{-1})^n = (z^n)^{-1}$.

## Statement

For every positive integer $n$, a nonzero complex number $z$ is an $n$-th root of unity
[if and only if $z = e^{2\pi i k/n}$ for some integer $k$ with $0 \le k < n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.mem_rootsOfUnity).
These $n$ numbers are pairwise distinct, so
[$\mu_n$ has exactly $n$ elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.card_rootsOfUnity). In terms of the
trigonometric functions,

$$e^{2\pi i k/n} = \cos\frac{2\pi k}{n} + i \sin\frac{2\pi k}{n},$$

so for $n \ge 3$ the $n$-th roots of unity are the vertices of the regular $n$-gon inscribed in
the unit circle with one vertex at $1$.

## Proof

The main tool is the [complex exponential](../../single-variable-complex-analysis/complex-valued-series/complex-exponential.md) and the fact that
[$e^w = 1$ exactly when $w$ is an integer multiple of $2\pi i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/Log.html#Complex.exp_eq_one_iff).

If $z = e^{2\pi i k/n}$, then, since [$e^{mw} = (e^w)^m$ for every natural number $m$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Exponential.html#Complex.exp_nat_mul),
$z^n = e^{2\pi i k} = 1$. Conversely, suppose $z^n = 1$. Taking absolute values gives
$|z|^n = 1$, so [$|z| = 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Basic.html#Complex.norm_eq_one_of_pow_eq_one), and $z = e^{i\theta}$
for some real $\theta$. Then $e^{in\theta} = 1$, so $n\theta = 2\pi m$ for an integer $m$.
Dividing $m$ by $n$ with remainder, $m = qn + k$ with $0 \le k < n$, gives
$z = e^{2\pi i q}\, e^{2\pi i k/n} = e^{2\pi i k/n}$.

For distinctness, if $e^{2\pi i k/n} = e^{2\pi i l/n}$ with $0 \le l \le k < n$, then
$e^{2\pi i (k-l)/n} = 1$, so $(k-l)/n$ is an integer in $[0, 1)$, hence $k = l$.

## Examples

- For $n = 1$ the only root is $1$, and for $n = 2$ the roots are $1$ and $-1$.
- For $n = 3$ the roots are $1$,
  $\omega = -\tfrac12 + \tfrac{\sqrt3}{2} i$ and $\omega^2 = \bar\omega = -\tfrac12 - \tfrac{\sqrt3}{2} i$.
- For $n = 4$ the roots are $1, i, -1, -i$; the powers of $i$ run through all four, and
  [$i$ is a primitive fourth root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_I).

## Properties

- **Cyclic structure.** The number $\omega_n = e^{2\pi i/n}$ is
  [a primitive $n$-th root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.isPrimitiveRoot_exp): its powers
  $1, \omega_n, \dots, \omega_n^{n-1}$ are exactly the elements of $\mu_n$, so $\mu_n$ is cyclic of
  order $n$, and the [order](../basic-definitions/order-of-an-element.md) of $\omega_n^k$ is $n/\gcd(k, n)$. More generally, for
  $n \ge 1$, [the $n$-th roots of unity in any integral domain form a cyclic group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Basic.html#rootsOfUnity.isCyclic).
- **Primitive roots.** The root $e^{2\pi i k/n}$ generates $\mu_n$ exactly when $\gcd(k, n) = 1$
  (see [primitive complex roots of unity](primitive-complex-roots-of-unity.md)), so
  [there are $\varphi(n)$ primitive $n$-th roots of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.card_primitiveRoots), where
  [$\varphi$](../../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md) is Euler's totient function.
- **Unit circle and conjugation.** For $n \ge 1$,
  [every $n$-th root of unity has absolute value $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.norm_eq_one_of_mem_rootsOfUnity),
  and so [its complex conjugate is its inverse](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.conj_rootsOfUnity).
- **Divisibility.** If $d$ divides $n$, then
  [every $d$-th root of unity is an $n$-th root of unity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Basic.html#rootsOfUnity_le_of_dvd).
- **Vanishing sum.** If $\omega$ is a primitive $n$-th root of unity and $n \ge 2$, then
  [$1 + \omega + \omega^2 + \dots + \omega^{n-1} = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/PrimitiveRoots.html#IsPrimitiveRoot.geom_sum_eq_zero),
  so the $n$-th roots of unity add up to $0$.
- **Factorization.** For $n \ge 1$, since $\mathbb{C}$ contains a primitive $n$-th root of unity,
  [$X^n - 1$ is the product of the factors $X - \zeta$ over all $\zeta \in \mu_n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Basic.html#Polynomial.X_pow_sub_one_eq_prod).
  Grouping the roots by their order shows that
  [$X^n - 1$ is the product of the cyclotomic polynomials $\Phi_d$ over the divisors $d$ of $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Polynomial/Cyclotomic/Basic.html#Polynomial.prod_cyclotomic_eq_X_pow_sub_one)
  (see [cyclotomic polynomial](../../ring-theory/polynomial-rings/cyclotomic-polynomials-in-q-x.md)).

## Related concepts

Every finite subgroup $G$ of $\mathbb{C}^\times$ of order $n$ equals $\mu_n$. For each
$g \in G$, [Lagrange's theorem](../../../overview/general-algebra/group-theory/part-02/lagranges-theorem.md) applied to the cyclic
subgroup generated by $g$ shows that the order of $g$ divides $n$, so $g^n = 1$. Hence
$G \subseteq \mu_n$, and both sets have $n$ elements. An element of $\mathbb{C}^\times$
has finite order exactly when it is a root of unity. A homomorphism from a finite group of order
$n$ to $\mathbb{C}^\times$ takes its values in $\mu_n$, which is why roots of unity appear throughout
the theory of dual groups
and the Fourier transform for finite abelian groups.

## In Mathlib

Mathlib defines the $n$-th roots of unity for any commutative monoid, as a subgroup of its group of
units, and the membership criterion holds in that generality. For the complex numbers the units are
the nonzero complex numbers, so a complex root of unity is a nonzero complex number viewed as a unit.
The exponent is a natural number and may be $0$; since $z^0 = 1$,
[the $0$-th roots of unity are all the units](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Basic.html#rootsOfUnity_zero), so the explicit description,
the primitive root $e^{2\pi i/n}$, the count, cyclicity and the absolute-value and conjugation
statements carry the standing hypothesis that $n$ is nonzero. The explicit description writes the
exponent as $2\pi i \cdot (k/n)$ with $k$ a natural number below $n$. The
number of elements is measured by the natural-number cardinality. Primitive roots are a separate
predicate on elements: $\zeta$ is a primitive $n$-th root of unity when $\zeta^n = 1$ and $n$
divides every exponent $l$ with $\zeta^l = 1$. Cyclicity, the vanishing sum and the factorization of
$X^n - 1$ into linear factors (given a primitive $n$-th root) are proved over arbitrary integral
domains, and the factorization into cyclotomic polynomials over any commutative ring.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Complex number](../../../overview/general-algebra/numbers/complex-number.md)
- [Complex exponential](../../single-variable-complex-analysis/complex-valued-series/complex-exponential.md)
- [Subgroup](../../../overview/general-algebra/group-theory/part-01/subgroup.md)

## Sources

- [Mathlib documentation: `Complex.mem_rootsOfUnity`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.mem_rootsOfUnity)
- [Source of `Complex.mem_rootsOfUnity` in Mathlib/RingTheory/RootsOfUnity/Complex.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/RootsOfUnity/Complex.lean#L111)
- [Mathlib undergraduate list: Group Theory › Abelian group](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L96)
