# Ring of Witt vectors

For a prime number $p$ and a commutative [ring](../rings/ring.md) $R$, the **ring of ($p$-typical) Witt vectors** $W(R)$ is a ring whose elements are infinite sequences $(a_0, a_1, a_2, \dots)$ of elements of $R$, added and multiplied by universal polynomial rules that imitate carrying digits. Its basic use is to produce rings of [characteristic zero](../field-theory/characteristic-zero.md) out of rings of [characteristic $p$](../field-theory/characteristic-p.md): applied to the field with $p$ elements it gives the [$p$-adic integers](../numbers/p-adic-integer.md), and applied to any perfect field $k$ of characteristic $p$ it gives a complete discrete valuation ring with residue field $k$ in which $p$ generates the maximal ideal. Witt vectors are a standard tool in number theory, algebraic geometry in characteristic $p$, and $p$-adic Hodge theory.

## Definition

Fix a prime $p$. The $n$-th **Witt polynomial** is the polynomial with integer coefficients

$$w_n = \sum_{i=0}^{n} p^i X_i^{p^{n-i}} = X_0^{p^n} + p X_1^{p^{n-1}} + \cdots + p^n X_n$$

in the variables $X_0, X_1, \dots$ ([the definition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/WittPolynomial.html#wittPolynomial)); for instance $w_0 = X_0$ and $w_1 = X_0^p + p X_1$. For a sequence $a = (a_0, a_1, \dots)$ in $R$, the elements $w_n(a)$ of $R$, obtained by evaluating $w_n$ at $a$ with its integer coefficients read in $R$, are its **ghost components**.

The key fact is the Witt structure theorem: [for every polynomial $\Phi$ with integer coefficients there is a unique family of polynomials $\varphi_0, \varphi_1, \dots$ with integer coefficients such that $w_n(\varphi_0, \varphi_1, \dots) = \Phi(w_n, w_n, \dots)$ for every $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/StructurePolynomial.html#wittStructureInt_existsUnique), where the copies of $w_n$ on the right are taken in separate sets of variables. Taking $\Phi = X + Y$ and $\Phi = XY$ gives polynomials $S_n$ and $P_n$, each involving only the first $n + 1$ coordinates of each argument, and one defines

$$a + b = (S_0(a, b), S_1(a, b), \dots), \qquad a \cdot b = (P_0(a, b), P_1(a, b), \dots).$$

So [the zeroth coordinate of a sum is the sum of zeroth coordinates](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Defs.html#WittVector.add_coeff_zero) and [likewise for products](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Defs.html#WittVector.mul_coeff_zero), but the higher coordinates involve carries:

$$S_1 = X_1 + Y_1 + \frac{X_0^p + Y_0^p - (X_0 + Y_0)^p}{p}, \qquad P_1 = X_0^p Y_1 + X_1 Y_0^p + p X_1 Y_1.$$

With these operations the set of sequences becomes a commutative ring, [the ring of Witt vectors $W(R)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Defs.html#WittVector), and by construction [the ghost map $a \mapsto (w_0(a), w_1(a), \dots)$ is a ring homomorphism from $W(R)$ to the product ring $R^{\mathbb{N}}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Basic.html#WittVector.ghostMap). The ring axioms are polynomial identities with integer coefficients; they can be checked after inverting $p$, where the ghost map identifies Witt vectors with ordinary sequences under coordinatewise operations.

## Examples

- **$p$ invertible.** If $p$ is invertible in $R$ (for instance if $R$ contains the rationals), then [the ghost map is a ring isomorphism from $W(R)$ onto the product of countably many copies of $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Basic.html#WittVector.ghostEquiv), so nothing new appears.
- **The prime field.** [$W(\mathbb{F}_p)$ is isomorphic to the ring $\mathbb{Z}_p$ of $p$-adic integers](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Compare.html#WittVector.equiv). At finite level, [the Witt vectors of length $n$ over $\mathbb{F}_p$ form a ring isomorphic to $\mathbb{Z}/p^n\mathbb{Z}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Compare.html#TruncatedWittVector.zmodEquivTrunc). For $p = 2$ the formulas for $S_0$ and $S_1$ give the first two coordinates of $(1, 0, 0, \dots) + (1, 0, 0, \dots)$ in $W(\mathbb{F}_2)$ as $0$ and $1$; in fact the whole sum is $2 = (0, 1, 0, \dots)$ (see the Properties section), mirroring $1 + 1 = 2$ in $\mathbb{Z}_2$.
- **Finite fields.** For the [finite field](../../../undergraduate/ring-theory/field-theory/finite-fields.md) with $p^f$ elements, the Witt vectors form the ring of integers of the unramified extension of degree $f$ of the [$p$-adic numbers](../numbers/p-adic-number.md).

## Properties

**Functoriality.** [A ring homomorphism $f\colon R \to S$ induces a ring homomorphism $W(R) \to W(S)$ that applies $f$ to every coordinate](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Basic.html#WittVector.map), and [it is injective when $f$ is](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Basic.html#WittVector.map_injective).

**Teichmüller representatives.** The map $r \mapsto [r] = (r, 0, 0, \dots)$ is [multiplicative and sends $1$ to $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Teichmuller.html#WittVector.teichmuller), though not additive, and [the ghost components of $[r]$ are $r, r^p, r^{p^2}, \dots$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Teichmuller.html#WittVector.ghostComponent_teichmuller).

**Frobenius and Verschiebung.** Each $W(R)$ carries [a ring endomorphism $F$, the Witt vector Frobenius](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Frobenius.html#WittVector.frobenius), and an additive map $V$, the [Verschiebung, which shifts coordinates and inserts a zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Verschiebung.html#WittVector.verschiebung): $V(a_0, a_1, \dots) = (0, a_0, a_1, \dots)$. They satisfy [$F(V(x)) = px$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Identities.html#WittVector.frobenius_verschiebung) and [the projection formula $V(x \cdot F(y)) = V(x) \cdot y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Identities.html#WittVector.verschiebung_mul_frobenius). When $R$ has characteristic $p$, [$F$ raises every coordinate to the $p$-th power](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Frobenius.html#WittVector.coeff_frobenius_charP), so it is induced by the [Frobenius morphism](../field-theory/frobenius-morphism.md) of $R$, and [$V(F(x)) = px$ as well](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Identities.html#WittVector.verschiebung_frobenius). In particular, in characteristic $p$, [the element $p$ of $W(R)$ is $(0, 1, 0, 0, \dots)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Identities.html#WittVector.coeff_p).

**Characteristic zero.** If $R$ has characteristic $p$, then [the $n$-th coordinate of $p^n$ is $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Identities.html#WittVector.coeff_p_pow), so $p$ is not nilpotent in $W(R)$. In fact $W(R)$ has characteristic zero, since the inclusion of $\mathbb{F}_p$ into $R$ induces an injective ring homomorphism from $W(\mathbb{F}_p) \cong \mathbb{Z}_p$ into $W(R)$ (the inclusion is injective because $R \neq 0$, and functoriality preserves injectivity). If $R$ is moreover an integral domain, [so is $W(R)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Domain.html#WittVector.instIsDomain).

**Perfect fields.** A ring of characteristic $p$ is perfect if its Frobenius map $x \mapsto x^p$ is bijective, so that every element $x$ has a unique $p^i$-th root, written $x^{p^{-i}}$, for each $i$. Let $k$ be a perfect field of characteristic $p$. Then [$W(k)$ is a discrete valuation ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/DiscreteValuationRing.html#WittVector.isDiscreteValuationRing), that is, a principal ideal domain with exactly one nonzero prime ideal, and [$p$ is an irreducible element of it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/DiscreteValuationRing.html#WittVector.irreducible), hence a uniformizer (a generator of that maximal ideal); [every nonzero element has the form $p^m u$ with $u$ a unit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/DiscreteValuationRing.html#WittVector.exists_eq_pow_p_mul'). More generally, for a perfect ring $k$ of characteristic $p$, [the quotient $W(k)/pW(k)$ is isomorphic to $k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Complete.html#WittVector.quotientPEquiv), [$W(k)$ is complete for the $p$-adic topology](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Complete.html#WittVector.isAdicCompleteIdealSpanP), and every Witt vector $x = (x_0, x_1, \dots)$ has a Teichmüller expansion: [for each $n$, $x$ is congruent modulo $p^{n+1}$ to $\sum_{i=0}^{n} [x_i^{p^{-i}}]\, p^i$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/TeichmullerSeries.html#WittVector.dvd_sub_sum_teichmuller_iterateFrobeniusEquiv_coeff). For $k = \mathbb{F}_p$ this writes every $p$-adic integer as a series $\sum_i \tau_i\, p^i$ whose digits $\tau_i$ are Teichmüller representatives, that is, $0$ or a $(p-1)$-st root of unity, instead of the integers $0, 1, \dots, p - 1$.

## Related concepts

The [perfection](perfection-of-a-ring.md) of a ring of characteristic $p$ is often combined with Witt vectors, since $W$ behaves best on perfect rings. The ring $W(k)$ for a perfect field $k$ is, up to isomorphism, the only complete discrete valuation ring of characteristic zero in which $p$ generates the maximal ideal and whose residue field is $k$; its fraction field carries the Frobenius semilinear structure used to define isocrystals. There is also a ring of big Witt vectors, indexed by all positive integers rather than by powers of $p$, of which the $p$-typical ring is a quotient.

## In Mathlib

Mathlib defines Witt vectors for any natural number $p$ and any type $R$ as a structure wrapping a sequence indexed by the natural numbers, whose terms it calls coefficients rather than coordinates. The ring structure is provided only when $p$ is known to be prime and $R$ is a commutative ring. Addition, multiplication and the other operations are defined by evaluating the integral structure polynomials on the coefficients, and the ring axioms are proved first for Witt vectors over polynomial rings with rational coefficients, where the ghost map is bijective, then carried to polynomial rings with integer coefficients, whose Witt vectors map injectively into the rational case, and finally transferred to an arbitrary commutative ring $R$ along the surjective map onto $W(R)$ induced by evaluating such polynomials at elements of $R$. Truncated Witt vectors of a fixed length are a separate type with its own ring structure.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ring](../rings/ring.md)
- [Prime numbers](../../../undergraduate/ring-theory/divisibility-in-integral-domains/prime-numbers.md)
- [Polynomial in several indeterminates](../polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Ring morphism](../rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `WittVector`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Defs.html#WittVector)
- [Source of `WittVector` in Mathlib/RingTheory/WittVector/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/WittVector/Defs.lean#L45)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L151)
