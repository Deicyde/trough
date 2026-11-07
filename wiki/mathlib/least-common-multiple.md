The **least common multiple** of two elements $a$ and $b$ is a common multiple of both that divides every other common multiple. For nonzero [natural numbers](trough:Nat) it is the smallest positive integer divisible by both, written $\operatorname{lcm}(a, b)$, while $\operatorname{lcm}(a, 0) = 0$; the same idea makes sense in any commutative ring, where it is defined purely in terms of divisibility. It is the counterpart of the [greatest common divisor](trough:GCDMonoid.gcd), and for nonzero $a$ and $b$ their product is $ab$ up to a unit, so each determines the other. Least common multiples appear whenever periodic conditions are combined, as in adding fractions over a common denominator or solving simultaneous congruences.

## Definition

Let $R$ be a commutative ring, or more generally a commutative monoid with zero, and let $a, b \in R$. An element $m \in R$ is a **least common multiple** of $a$ and $b$ if

1. $a \mid m$ and $b \mid m$, and
2. whenever $a \mid c$ and $b \mid c$, also $m \mid c$.

The word "least" refers to the divisibility order, not to size. If $m$ and $m'$ are both least common multiples, each divides the other, so in an integral domain they differ by a unit factor: a least common multiple, when it exists, is unique up to associates. In the integers the units are $\pm 1$, and one takes the nonnegative choice. Since the only multiple of $0$ is $0$ itself, condition 1 forces $\operatorname{lcm}(a, 0) = 0$.

Least common multiples need not exist. In the ring $\mathbb{Z}[\sqrt{-5}]$ the elements $2$ and $1 + \sqrt{-5}$ have no least common multiple: both divide $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ and $2(1 + \sqrt{-5})$. Write $N(x + y\sqrt{-5}) = x^2 + 5y^2$ for the multiplicative norm. A least common multiple $m$ would be divisible by $2$ and by $1 + \sqrt{-5}$, so $N(m)$ would be divisible by $4$ and by $6$, hence by $12$; and $m$ would divide $6$ and $2(1 + \sqrt{-5})$, so $N(m)$ would divide $36$ and $24$, hence $12$. Thus $N(m) = 12$, but $x^2 + 5y^2 = 12$ has no integer solutions.

## Examples

- $\operatorname{lcm}(4, 6) = 12$, and $\operatorname{lcm}(12, 18) = 36$.
- If $\gcd(m, n) = 1$ then $\operatorname{lcm}(m, n) = mn$ for natural numbers $m$ and $n$.
- From prime factorisations: $12 = 2^2 \cdot 3$ and $18 = 2 \cdot 3^2$, and taking the larger exponent of each [prime](trough:Prime) gives $2^2 \cdot 3^2 = 36$. In general, for nonzero natural numbers $a$ and $b$, the exponent of each prime in $\operatorname{lcm}(a, b)$ is the larger of its exponents in $a$ and in $b$.
- Over the rationals, $x^2 - 1 = (x - 1)(x + 1)$ and $x^2 + x = x(x + 1)$ have least common multiple $x(x - 1)(x + 1) = x^3 - x$ among [polynomials](trough:Polynomial), normalized to be monic.

## Properties

Throughout, $R$ is a commutative monoid with zero in which cancellation by nonzero elements holds and every pair of elements has a gcd and an lcm, such as $\mathbb{N}$, $\mathbb{Z}$, or any [unique factorisation domain](trough:UniqueFactorizationMonoid).

- **Universal property.** For all $a, b, c$, $\operatorname{lcm}(a, b) \mid c$ if and only if $a \mid c$ and $b \mid c$. In particular $a$ divides $\operatorname{lcm}(a, b)$, and so does $b$.
- **Relation with the gcd.** The product $\gcd(a, b)\,\operatorname{lcm}(a, b)$ is associated to $ab$, that is, equal to it up to a unit. In $\mathbb{N}$, where the only unit is $1$, this reads
  $$\gcd(a, b)\,\operatorname{lcm}(a, b) = ab,$$
  so $\operatorname{lcm}(a, b) = ab / \gcd(a, b)$ for $a, b$ not both zero. In every case $\operatorname{lcm}(a, b)$ divides $ab$.
- **Zero.** $\operatorname{lcm}(a, b) = 0$ if and only if $a = 0$ or $b = 0$.
- **Primes.** For a prime element $p$, $p \mid \operatorname{lcm}(a, b)$ if and only if $p \mid a$ or $p \mid b$.
- **Algebraic laws.** Once the lcm is normalized to a canonical representative (nonnegative integers, monic polynomials), it is commutative and associative, so the least common multiple of a finite set is well defined, and it divides $c$ exactly when every member of the set does.
- **Congruences.** For natural numbers $a, b, m, n$, $a \equiv b \pmod m$ and $a \equiv b \pmod n$ hold together if and only if $a \equiv b \pmod{\operatorname{lcm}(m, n)}$. This underlies the uniqueness part of the [Chinese remainder theorem](trough:Ideal.quotientInfRingEquivPiQuotient), and it holds without any coprimality assumption.

## Ideals and existence

In an integral domain, $c$ is a common multiple of $a$ and $b$ exactly when $c$ lies in the [ideal](trough:Ideal) $(a) \cap (b)$, so a least common multiple exists precisely when this intersection is principal, and then it generates it. In a [Euclidean domain](trough:EuclideanDomain), for instance, $(a) \cap (b) = (\operatorname{lcm}(a, b))$. The same holds in every [principal ideal domain](trough:Submodule.IsPrincipal), and in a unique factorisation domain the lcm is built from factorisations by taking maximal exponents, so every unique factorisation domain has gcds and lcms. In an integral domain, every pair of elements has a gcd if and only if every pair has an lcm (for a single pair of nonzero elements, an lcm $m$ yields the gcd $ab/m$, but not conversely).

## Related concepts

- The [greatest common divisor](trough:GCDMonoid.gcd) is the dual notion, the greatest lower bound in the divisibility order where the lcm is the least upper bound.
- When $\gcd(a, b)$ is a unit, the lcm is the product $ab$ up to a unit. This applies in particular to [coprime](trough:IsCoprime) elements, those with $xa + yb = 1$ for some $x$ and $y$.
- For ideals, the role of the lcm is played by the intersection. In a Dedekind domain the ideals themselves have gcds and lcms, and there the lcm of two ideals is their intersection.
- If a ring has gcds and lcms, so does its [polynomial ring](trough:Polynomial.normalizedGcdMonoid).

## In Mathlib

For general commutative monoids, Mathlib treats the least common multiple as one of the two operations of a gcd monoid, a structure on a cancellative commutative monoid with zero. The structure takes the gcd as primary and asks of the lcm only that $\gcd(a, b)\operatorname{lcm}(a, b)$ be associated to $ab$ and that the lcm with $0$ be $0$; the universal property is then a theorem. Because the operation is only determined up to units, many identities hold in general only up to association, and exact equalities such as commutativity need the normalized variant, which picks a canonical representative in each class of associates. On the natural numbers the operation is the usual lcm, and on the integers it is always nonnegative. The lcm of a finite set is defined by folding the binary operation, with the empty set giving $1$.

## Depends on

- [Natural number](trough:Nat)
- [Integer](trough:Int)
- [Ring](trough:Ring)
