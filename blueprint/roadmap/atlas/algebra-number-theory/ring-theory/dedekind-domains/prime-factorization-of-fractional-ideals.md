---
declaration: section
origin: cited
lean: FractionalIdeal.unitsSupportFinset, FractionalIdeal.unitsToFinsupp, FractionalIdeal.finsuppProd_ne_zero, FractionalIdeal.finsuppToUnits, FractionalIdeal.count_finsuppToUnits, FractionalIdeal.toUnits_left_inv, FractionalIdeal.toUnits_right_inv, FractionalIdeal.unitsToFinsupp_mul
statement: formalized
proof: formalized
---

# Prime factorization of fractional ideals

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html).

## Support of the prime exponents of a fractional ideal

Let $R$ be a Dedekind domain with
fraction field $K$. For a unit fractional ideal $I$ of $R$ in $K$, this is the finite set of
height-one primes $v$ of $R$ at which the $v$-adic valuation of $I$ is nonzero.

Formalized by `FractionalIdeal.unitsSupportFinset`, a definition declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#units-support-finset).

## Prime exponents of an invertible fractional ideal

Let $R$ be a Dedekind domain with
fraction field $K$, and let $I$ be a unit of the monoid of fractional ideals of $R$ in $K$.
The prime exponents of $I$ form the finitely supported function from the height-one primes of
$R$ to $\mathbb{Z}$ that sends each height-one prime $v$ to the exponent $\operatorname{ord}_v(I)$
of $v$ in the factorization $I = \prod_v v^{\operatorname{ord}_v(I)}$; its support is the finite
set of $v$ with $\operatorname{ord}_v(I) \neq 0$.

Formalized by `FractionalIdeal.unitsToFinsupp`, a definition declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#units-to-finsupp).

## Products of prime powers are nonzero

Let $R$ be a Dedekind domain with fraction field
$K$. For every finitely supported function $e$ from the height-one primes of $R$ to $\mathbb{Z}$,
the fractional ideal $\prod_v v^{e(v)}$ of $R$ in $K$, the product over the primes $v$ with
$e(v) \neq 0$, is nonzero.

Formalized by `FractionalIdeal.finsuppProd_ne_zero`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#finsupp-prod-ne-zero).

## Fractional ideal with prescribed prime exponents

Let $R$ be a Dedekind domain with
fraction field $K$. For a finitely supported function $e$ from the height-one primes of $R$ to
$\mathbb{Z}$, this is the fractional ideal $\prod_v v^{e(v)}$ of $R$ in $K$, the product over the
primes $v$ with $e(v) \neq 0$, regarded as a unit of the monoid of fractional ideals (it is
nonzero, hence invertible).

Formalized by `FractionalIdeal.finsuppToUnits`, a definition declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#finsupp-to-units).

## Valuations of a product of prime powers

Let $R$ be a Dedekind domain with fraction
field $K$. For every finitely supported function $e$ from the height-one primes of $R$ to
$\mathbb{Z}$ and every height-one prime $v$ of $R$, the $v$-adic valuation of the fractional
ideal $\prod_w w^{e(w)}$, the product over the primes $w$ with $e(w) \neq 0$, equals $e(v)$.

Formalized by `FractionalIdeal.count_finsuppToUnits`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#count-finsupp-to-units).

## Reconstructing a fractional ideal from its prime exponents

Let $R$ be a Dedekind domain
with fraction field $K$, and for a unit fractional ideal $I$ of $R$ in $K$ and a height-one prime
$v$ of $R$ write $\operatorname{val}_v(I)$ for the $v$-adic valuation of $I$. Every unit
fractional ideal $I$ of $R$ in $K$ equals $\prod_v v^{\operatorname{val}_v(I)}$, the product over
the height-one primes $v$ of $R$ with $\operatorname{val}_v(I) \neq 0$.

Formalized by `FractionalIdeal.toUnits_left_inv`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#to-units-left-inv).

## Recovering prime exponents from a product of prime powers

Let $R$ be a Dedekind domain
with fraction field $K$, and let $e$ be a finitely supported function from the height-one primes
of $R$ to $\mathbb{Z}$. The prime-exponent function of the fractional ideal $\prod_w w^{e(w)}$,
the product over the primes $w$ with $e(w) \neq 0$, is $e$: its $v$-adic valuation is $e(v)$
for every height-one prime $v$ of $R$.

Formalized by `FractionalIdeal.toUnits_right_inv`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#to-units-right-inv).

## Prime exponents are additive

Let $R$ be a Dedekind domain with fraction field $K$, and
for a unit fractional ideal $I$ of $R$ in $K$ and a height-one prime $v$ of $R$ write
$\operatorname{val}_v(I)$ for the $v$-adic valuation of $I$. For all unit fractional ideals $I$
and $J$ of $R$ in $K$ and every height-one prime $v$ of $R$,
$\operatorname{val}_v(IJ) = \operatorname{val}_v(I) + \operatorname{val}_v(J)$.

Formalized by `FractionalIdeal.unitsToFinsupp_mul`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#units-to-finsupp-mul).

## Prime factorization isomorphism for fractional ideals

Let $R$ be a Dedekind domain with
fraction field $K$, and for a unit fractional ideal $I$ of $R$ in $K$ and a height-one prime $v$
of $R$ write $\operatorname{val}_v(I)$ for the $v$-adic valuation of $I$. The factorization
isomorphism is the group isomorphism from the unit group of the fractional ideals of $R$ in $K$
to the additive group of finitely supported functions from the height-one primes of $R$ to
$\mathbb{Z}$ (written multiplicatively) that sends $I$ to the function
$v \mapsto \operatorname{val}_v(I)$. Its inverse sends $e$ to $\prod_v v^{e(v)}$, the product
over the primes $v$ with $e(v) \neq 0$.

Formalized by `FractionalIdeal.factorizationMulEquiv`, a definition declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#factorization-mul-equiv).

## Exponent function of a prime ideal

Let $R$ be a Dedekind domain with fraction field
$K$ and let $w$ be a height-one prime of $R$. The factorization isomorphism sends the fractional
ideal $w$, as a unit fractional ideal of $R$ in $K$, to the function on height-one primes of $R$
that is $1$ at $w$ and $0$ elsewhere.

Formalized by `FractionalIdeal.factorizationMulEquiv_prime_self`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#factorization-mul-equiv-prime-self).

## Inverse factorization of a single prime power

Let $R$ be a Dedekind domain with fraction
field $K$, let $w$ be a height-one prime of $R$ and let $n \in \mathbb{Z}$. The inverse of the
factorization isomorphism sends the function on height-one primes of $R$ that is $n$ at $w$ and
$0$ elsewhere to the fractional ideal $w^n$.

Formalized by `FractionalIdeal.symm_single_zpow`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FactorizationEquiv.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#symm-single-zpow).

## Finitely many primes contain a nonzero element

In a Dedekind domain $A$, every nonzero
element $a$ lies in only finitely many prime ideals of $A$.

## Sources

- ATLAS `NumberTheoryI` Lemma 3.6.

Formalized by `Ideal.finite_setOf_isPrime_and_mem`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#finite-set-of-is-prime-and-mem).

## Finitely many primes contain a nonzero ideal

In a Dedekind domain $A$, every nonzero
ideal $I$ is contained in only finitely many prime ideals of $A$.

## Sources

- ATLAS `NumberTheoryI` Corollary 3.7.

Formalized by `Ideal.finite_setOf_isPrime_and_le`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#finite-set-of-is-prime-and-le).

## Vanishing multiplicity of a prime factor

Let $A$ be a Dedekind domain, let $\mathfrak p$
be a prime ideal of $A$ and let $I$ be a nonzero ideal of $A$. Then the multiplicity of
$\mathfrak p$ in the factorization of $I$ into prime ideals is zero if and only if
$I \not\subseteq \mathfrak p$.

In particular, if $\mathfrak p$ and $\mathfrak q$ are distinct nonzero prime ideals of $A$, then
the multiplicity of $\mathfrak p$ in the factorization of $\mathfrak q$ is zero.

## Sources

- ATLAS `NumberTheoryI` Lemma 3.9.

Formalized by `Ideal.count_normalizedFactors_eq_zero_iff`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#count-normalized-factors-eq-zero-iff).

## Fractional ideals have finite support

Let $A$ be a Dedekind domain with field of
fractions $K$, and let $I$ be a fractional ideal of $A$ in $K$. For a nonzero prime ideal
$\mathfrak p$ of $A$, let $v_{\mathfrak p}(I) \in \mathbb Z$ be the exponent of $\mathfrak p$ in
the factorization of $I$ into prime ideals, with $v_{\mathfrak p}(0) = 0$. Then
$v_{\mathfrak p}(I) \neq 0$ for only finitely many nonzero prime ideals $\mathfrak p$ of $A$.

In particular, for $x \in K^\times$ the valuations $v_{\mathfrak p}(xA)$ vanish for all but
finitely many $\mathfrak p$.

## Sources

- ATLAS `NumberTheoryI` Corollary 3.10. The book's hypothesis $I \neq 0$ is dropped, since every valuation of the zero ideal is zero.

Formalized by `FractionalIdeal.count_eq_zero_for_all_but_finitely_many`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/DedekindDomain/FiniteSupport.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#count-eq-zero-for-all-but-finitely-many).

## Ideal multiplicity is unchanged by localization at a maximal ideal

Let $R$ be a
Dedekind domain, $\mathfrak p$ a maximal ideal of $R$, and $R_{\mathfrak p}$ a local ring that
is a localization of $R$ at $\mathfrak p$, with maximal ideal $\mathfrak m$. Then for every
ideal $I$ of $R$, the multiplicity of $\mathfrak m$ in the extended ideal $I R_{\mathfrak p}$
equals the multiplicity of $\mathfrak p$ in $I$. Here the multiplicity of an ideal $J$ in an
ideal $K$ is the largest $n$ with $J^n \mid K$, or $\infty$ if $J^n \mid K$ for every $n$.

Formalized by `IsLocalization.AtPrime.emultiplicity_maximalIdeal_map_eq`, a theorem declared in [MathlibExt/RingTheory/Localization/AtPrime/Multiplicity.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Localization/AtPrime/Multiplicity.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html#emultiplicity-maximal-ideal-map-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime factorization of fractional ideals](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/dedekind-domains/prime-factorization-of-fractional-ideals)
