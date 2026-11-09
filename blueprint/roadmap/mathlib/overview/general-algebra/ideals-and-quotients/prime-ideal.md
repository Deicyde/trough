# Prime ideal

A **prime ideal** of a commutative [ring](../rings/ring.md) is a proper
[ideal](ideal-of-a-commutative-ring.md) with the property that whenever a product of two elements
lies in it, one of the two factors already does. The definition transfers a
characteristic property of a prime number (Euclid's lemma: it divides a product
only if it divides one of the factors) from elements to ideals. Prime ideals are
exactly the ideals whose [quotient ring](quotient-ring.md) is an
integral domain, a nonzero commutative ring in which a product of nonzero
elements is nonzero, and they
are the points of the [prime spectrum](../../geometry/algebraic-geometry/prime-spectrum.md), the space on which
algebraic geometry is built.

## Definition

Let $R$ be a commutative ring. An ideal $P$ of $R$ is
[prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.IsPrime) if

- $P \neq R$, and
- for all $a, b \in R$, if $ab \in P$ then $a \in P$ or $b \in P$.

Since an ideal equals $R$ exactly when it contains $1$, the first condition says
that $1 \notin P$. Read contrapositively, the second condition says that
[the product of two elements outside $P$ is again outside $P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.IsPrime.mul_notMem).
Together with [$1 \notin P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.IsPrime.one_notMem), this means that the
complement $R \setminus P$ is a multiplicatively closed set.

The leading characterization is through quotients: for an ideal $P$ of $R$,
[the quotient $R/P$ is an integral domain exactly when $P$ is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Basic.html#Ideal.Quotient.isDomain_iff_prime).
The condition $P \neq R$ corresponds to the requirement that an integral domain
have $0 \neq 1$, and the product condition to the absence of zero divisors in
$R/P$.

## Examples

- **The integers.** For a nonzero element $p$ of a commutative ring,
  [the principal ideal $(p)$ is prime exactly when $p$ is a prime element](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maximal.html#Ideal.span_singleton_prime)
  (see [prime element](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)). In the [integers](../numbers/integer.md) an integer
  $k$ is a prime element
  [exactly when its absolute value is a prime number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Int/Basic.html#Int.prime_iff_natAbs_prime),
  so the nonzero prime ideals of $\mathbb{Z}$ are the ideals $p\mathbb{Z}$ with
  $p$ a prime number. Since every ideal of $\mathbb{Z}$ is principal, the only
  other prime ideal is $\{0\}$.
- **The zero ideal.** For a commutative ring $R$,
  [if $R$ is an integral domain then $\{0\}$ is a prime ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.isPrime_bot),
  and [conversely, if $\{0\}$ is prime then $R$ is an integral domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#IsDomain.of_bot_isPrime).
- **Fields.** In a [field](../field-theory/field.md),
  [every prime ideal is $\{0\}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.eq_bot_of_prime), and $\{0\}$ is
  prime because a field is an integral domain, so $\{0\}$ is the only prime
  ideal.
- **Polynomials.** In the [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) ring $\mathbb{Z}[x]$, the
  ideal $(x)$ is prime, because $\mathbb{Z}[x]/(x)$ is isomorphic to $\mathbb{Z}$,
  an integral domain. The ideal $(4, x)$ is not prime: $2 \cdot 2 \in (4, x)$, but
  $2 \notin (4, x)$.

## Properties

**Maximal ideals are prime.** In a commutative ring,
[every maximal ideal is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maximal.html#Ideal.IsMaximal.isPrime), as one also sees
from the quotients: the quotient by a [maximal ideal](maximal-ideal.md) is a
field, and every field is an integral domain. The converse fails: $\{0\}$ is a
prime ideal of $\mathbb{Z}$ that is not maximal, and so is $(x)$ in
$\mathbb{Z}[x]$, which lies strictly inside the proper ideal $(2, x)$. Since
[every proper ideal is contained in a maximal ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maximal.html#Ideal.exists_le_maximal),
every proper ideal is contained in a prime ideal, and in particular every
nonzero commutative ring has at least one prime ideal.

**Products and powers.** By induction on the number of factors,
[a finite product of elements lies in a prime ideal $P$ exactly when one of the factors does](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Operations.html#Ideal.IsPrime.prod_mem_iff).
In particular [if $r^n \in P$ for some $n$, then $r \in P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.IsPrime.mem_of_pow_mem).
The radical of an ideal $I$ is the set of elements $r$ with $r^n \in I$ for some
$n \geq 1$, and $I$ is a radical ideal when it equals its radical; so a prime
ideal is a radical ideal:
[it equals its own radical](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Operations.html#Ideal.IsPrime.radical). The same property holds
one level up, for ideals: for ideals $I$ and $J$,
[the product $IJ$ is contained in $P$ exactly when $I \subseteq P$ or $J \subseteq P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Operations.html#Ideal.IsPrime.mul_le),
and likewise [$I \cap J \subseteq P$ exactly when $I \subseteq P$ or $J \subseteq P$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Operations.html#Ideal.IsPrime.inf_le).

**Radicals.** Prime ideals determine radicals: for every ideal $I$ of $R$,
[the radical of $I$ is the intersection of all prime ideals containing $I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Operations.html#Ideal.radical_eq_sInf).

**Ring morphisms.** If $f \colon R \to S$ is a [ring morphism](../rings/ring-morphism.md)
of commutative rings and $Q$ is a prime ideal of $S$, then
[the preimage $f^{-1}(Q)$ is a prime ideal of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maps.html#Ideal.IsPrime.comap).
In particular, taking $Q = \{0\}$ in an integral domain,
[the kernel of a ring morphism into an integral domain is a prime ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maps.html#RingHom.ker_isPrime).
Images of prime ideals, by contrast, need not be prime.

**Existence by maximality.** Let $S$ be a multiplicatively closed subset of $R$
and $I$ an ideal disjoint from $S$ such that every ideal strictly containing $I$
meets $S$. Then [$I$ is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maximal.html#Ideal.isPrime_of_maximally_disjoint).
Combined with Zorn's lemma, this shows that
[every ideal disjoint from $S$ is contained in a prime ideal disjoint from $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maximal.html#Ideal.exists_le_prime_disjoint);
such an ideal exists only when $0 \notin S$. Similarly,
[the intersection of a nonempty chain of prime ideals is prime](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Maximal.html#Ideal.sInf_isPrime_of_isChain),
so, by Zorn's lemma applied to reverse inclusion, every prime ideal contains a
minimal prime ideal, one that contains no strictly smaller prime ideal.

## Related concepts

- **Localization.** Because $R \setminus P$ is multiplicatively closed, one can
  [localize](../rings/localization.md) $R$ at it, inverting every element outside $P$.
  [The resulting ring $R_P$ is a local ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Localization/AtPrime/Basic.html#Localization.AtPrime.isLocalRing)
  (see [local ring](../rings/local-ring.md)), whose unique maximal ideal comes from $P$.
- **Prime spectrum.** The set of all prime ideals of $R$, equipped with the
  [Zariski topology](../../geometry/algebraic-geometry/zariski-topology.md), is the
  [prime spectrum](../../geometry/algebraic-geometry/prime-spectrum.md) of $R$.
- **Prime elements.** A nonzero element $p$ is prime exactly when the principal
  ideal $(p)$ is prime, so prime ideals generalize prime elements; in rings
  without unique factorization, such as many rings of integers of number fields
  (for instance $\mathbb{Z}[\sqrt{-5}]$),
  factorization of ideals into prime ideals takes the place of factorization of
  elements.

## In Mathlib

Mathlib states primality as a property of an ideal that may be supplied
automatically, so that facts such as the primality of maximal ideals, of the zero
ideal of an integral domain and of preimages are found without being invoked by
name. The definition is made for an arbitrary semiring rather than only for
commutative rings. For a noncommutative ring an ideal in Mathlib means a left
ideal, and the elementwise product condition is then stronger than the usual
noncommutative notion of a prime ideal, which is phrased with products of
ideals; most results about prime ideals, such as the description of the radical,
assume commutativity. Prime ideals of a lattice in the sense of order theory are
a separate notion with their own definition.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Ideal of a commutative ring](ideal-of-a-commutative-ring.md)
- [Quotient ring](quotient-ring.md)

## Sources

- [Mathlib documentation: `Ideal.IsPrime`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Prime.html#Ideal.IsPrime)
- [Source of `Ideal.IsPrime` in Mathlib/RingTheory/Ideal/Prime.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/Ideal/Prime.lean#L38)
- [Mathlib overview: General algebra › Ideals and quotients](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L77)
- [Mathlib undergraduate list: Ring Theory › Ideals and Quotients](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L134)
