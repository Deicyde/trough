---
article_id: af_a13c7aa18b29a759dac4e574
concept: Perfection
---

The **perfection** of a commutative ring $R$ of prime [characteristic](trough:CharP) $p$ is the ring of sequences $(x_0, x_1, x_2, \dots)$ of elements of $R$ in which each term is a $p$-th root of the one before it. On this ring the [Frobenius map](trough:frobenius) $x \mapsto x^p$ is bijective, and it is the universal perfect commutative ring of characteristic $p$ mapping to $R$: every homomorphism to $R$ from a perfect commutative ring of characteristic $p$ passes through it in exactly one way. The construction is basic in $p$-adic geometry, where the perfection of a quotient $\mathcal{O}/p\mathcal{O}$ produces the ring whose field of fractions is the tilt of a valued field.

## Definition

Let $p$ be a prime and $R$ a commutative [ring](trough:Ring) of characteristic $p$. The [perfection of $R$](lean:Perfection) is

$$R^{\mathrm{perf}} = \{ (x_n)_{n \ge 0} : x_n \in R \text{ and } x_{n+1}^p = x_n \text{ for all } n \}.$$

A sequence satisfying this condition is called compatible. Because Frobenius is a ring homomorphism in characteristic $p$, these sequences are closed under termwise addition, multiplication and negation, and [they form a subring of the ring of all sequences in $R$](lean:Perfection.subring). Equivalently, $R^{\mathrm{perf}}$ is the [inverse limit](trough:CategoryTheory.Limits.IsLimit) of the tower

$$\cdots \xrightarrow{\ \varphi\ } R \xrightarrow{\ \varphi\ } R \xrightarrow{\ \varphi\ } R$$

in which every map is the Frobenius $\varphi(x) = x^p$.

For each $n$, [the $n$-th coordinate $(x_m) \mapsto x_n$ is a ring homomorphism from $R^{\mathrm{perf}}$ to $R$](lean:Perfection.coeff), and [an element of $R^{\mathrm{perf}}$ is determined by its coordinates](lean:Perfection.ext). Write $\pi \colon R^{\mathrm{perf}} \to R$ for the zeroth coordinate.

A ring of characteristic $p$ is [perfect](lean:PerfectRing) when its Frobenius map is bijective. The perfection is perfect. Frobenius sends $(x_0, x_1, x_2, \dots)$ to $(x_0^p, x_0, x_1, \dots)$, and the shift $(x_0, x_1, x_2, \dots) \mapsto (x_1, x_2, \dots)$ undoes it: [the shift after Frobenius is the identity](lean:Perfection.pthRoot_frobenius), and [so is Frobenius after the shift](lean:Perfection.frobenius_pthRoot).

## Universal property

Let $P$ be a perfect commutative ring of characteristic $p$. Then [composing with $\pi$ gives a bijection from ring homomorphisms $P \to R^{\mathrm{perf}}$ to ring homomorphisms $P \to R$](lean:Perfection.lift). The inverse sends $f \colon P \to R$ to the map

$$y \mapsto \bigl( f(y), f(y^{1/p}), f(y^{1/p^2}), \dots \bigr),$$

where $y^{1/p^n}$ is the unique $p^n$-th root of $y$ in $P$. In particular, [two homomorphisms $P \to R^{\mathrm{perf}}$ that agree after composing with $\pi$ are equal](lean:Perfection.hom_ext).

The construction is functorial: [a ring homomorphism $g \colon R \to S$ between rings of characteristic $p$ induces a ring homomorphism $R^{\mathrm{perf}} \to S^{\mathrm{perf}}$](lean:Perfection.map), which [applies $g$ to each coordinate](lean:Perfection.coeff_map). In categorical language, perfection is [right adjoint](trough:CategoryTheory.Adjunction) to the inclusion of perfect rings of characteristic $p$ into commutative rings of characteristic $p$.

## Examples

- **Perfect rings.** If $R$ is already perfect, then [$R$, with the identity map, is its own perfection](lean:PerfectionMap.id): in a compatible sequence, $x_n$ must be the unique $p^n$-th root of $x_0$. This applies to finite fields and to algebraically closed fields of characteristic $p$.
- **A polynomial ring.** Let $R = \mathbb{F}_p[t]$ be the [polynomial](trough:Polynomial) ring. Let $(x_n)$ be a compatible sequence. If $x_0 = 0$, then every $x_n$ is $0$, because $\mathbb{F}_p[t]$ has no nonzero nilpotent elements. If $x_0 \neq 0$, then $x_0 = x_n^{p^n}$ has degree divisible by $p^n$ for every $n$, so $x_0$ and then every $x_n$ is constant. Frobenius fixes every element of $\mathbb{F}_p$, so the sequence is constant, and $\mathbb{F}_p[t]^{\mathrm{perf}} \cong \mathbb{F}_p$. The perfection keeps only what already has all $p$-power roots.
- **Nilpotents disappear.** A perfect ring has no nonzero nilpotent elements, since Frobenius is injective. For $R = \mathbb{F}_p[t]/(t^2)$, Frobenius sends $a + bt$ to $a^p = a$, so every term $x_n = x_{n+1}^p$ lies in $\mathbb{F}_p$, the sequence is constant, and $R^{\mathrm{perf}} \cong \mathbb{F}_p$.
- **Surjective Frobenius.** When Frobenius on $R$ is surjective, [every coordinate map $R^{\mathrm{perf}} \to R$ is surjective](lean:Perfection.coeff_surjective), and the perfection can be large. Let $A = \mathbb{F}_p[t^{1/p^\infty}]$ be the perfect ring obtained from $\mathbb{F}_p[t]$ by adjoining all $p$-power roots of $t$, and let $R = A/tA$. Frobenius on $R$ is surjective but not injective, since it kills the class of $t^{1/p}$. The isomorphisms $A/t^{p^n}A \cong A/tA$ given by taking $p^n$-th roots identify the Frobenius tower of $R$ with the tower of quotients $A/t^{p^n}A$, so $R^{\mathrm{perf}}$ is the $t$-adic completion of $A$.

## Tilting

Let $K$ be a field with a nonarchimedean absolute value $v \colon K \to \mathbb{R}_{\ge 0}$, let $\mathcal{O} = \{ x \in K : v(x) \le 1 \}$ be its valuation ring, and let $p$ be a prime with $v(p) < 1$. Then the [quotient ring](trough:Ideal.Quotient.ring) $\mathcal{O}/p\mathcal{O}$ has characteristic $p$, and [its perfection is the pre-tilt](lean:PreTilt) $\mathcal{O}^\flat$. Under these hypotheses [$\mathcal{O}^\flat$ is an integral domain](lean:PreTilt.isDomain), and [the tilt $K^\flat$ is its field of fractions](lean:Tilt) (see [field of fractions](trough:IsFractionRing)), a field of characteristic $p$. For the completion $\mathbb{C}_p$ of an algebraic closure of the $p$-adic numbers, the tilt carries an absolute value induced from $v$, for which it is a complete algebraically closed field of characteristic $p$. This passage from mixed characteristic to characteristic $p$ is the starting point of the theory of perfectoid fields.

When $\mathcal{O}$ is $p$-adically complete, reduction modulo $p$ gives a bijection, compatible with multiplication, from sequences $(y_n)$ in $\mathcal{O}$ with $y_{n+1}^p = y_n$ to elements of $\mathcal{O}^\flat$. This is how elements of the tilt are compared with elements of $\mathcal{O}$ itself.

## Related concepts

- The [perfect closure](trough:PerfectClosure) is the dual construction: the direct limit of $R \xrightarrow{\varphi} R \xrightarrow{\varphi} \cdots$, which adjoins $p$-th roots instead of selecting them. It is the universal homomorphism from $R$ to a perfect ring, the left adjoint of the same inclusion.
- The multiplicative part of the definition needs neither addition nor a characteristic: for any commutative monoid $M$ and any natural number $p$, [the sequences with $x_{n+1}^p = x_n$ form a submonoid of the monoid of all sequences in $M$](lean:Perfection.submonoid).
- The [ring of Witt vectors](trough:WittVector) of a perfect ring of characteristic $p$, such as $W(\mathcal{O}^\flat)$, leads back from characteristic $p$ to mixed characteristic.

## In Mathlib

Mathlib defines the perfection for any type with natural-number powers and any natural number $p$, as the sequences with $x_{n+1}^p = x_n$. For a commutative monoid this is a commutative monoid on which the $p$-th power map is bijective; the ring structure and characteristic $p$ arrive when $p$ is prime and the input is a commutative semiring of characteristic $p$, so semirings are allowed throughout. Mathlib's notion of a perfect ring asks only that $x \mapsto x^p$ be bijective, without a characteristic hypothesis. The universal property is an explicit bijection between sets of homomorphisms. A separate predicate says when a homomorphism $P \to R$ from a perfect ring is a perfection map: every compatible sequence of $p$-power roots in $R$ arises from exactly one $y$ in $P$ as the images of $y, y^{1/p}, y^{1/p^2}, \dots$. [Such a map yields an isomorphism from $P$ to $R^{\mathrm{perf}}$](lean:PerfectionMap.equiv), and [the zeroth coordinate $R^{\mathrm{perf}} \to R$ is itself a perfection map](lean:PerfectionMap.of). The tilt is defined for any field with a valuation valued in the nonnegative reals and any prime $p$ with $v(p) \neq 1$, with no completeness or perfectoid hypothesis; the ring $\mathcal{O}$ may be any ring mapping isomorphically onto the valuation ring.

## Depends on

- [Ring](trough:Ring)
- [Characteristic p](trough:CharP)
- [Frobenius morphism](trough:frobenius)
- [Ring morphism](trough:RingHom)
