---
declaration: section
origin: cited
lean: isDedekindDomain_iff_contain_isDivide, isDedekindDomain_iff_principalProduct, isDedekindDomain_tfae_contain_isDivide_principalProduct, integrallyClosed_dimensionLEOne_iff_isDedekindDomain, isDiscreteValuationRing_localization_atPrime_iff_integrallyClosed_dimensionLEOne, IsDedekindDomain.isPrincipalIdealRing_quotient, isNoetherianRing_of_forall_isPrincipalIdealRing_quotient, isDiscreteValuationRing_localization_atPrime_of_forall_isPrincipalIdealRing_quotient
statement: formalized
proof: formalized
---

# Characterizations of Dedekind domains

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html).

## Dedekind domains as the Noetherian domains where to contain is to divide

An integral
domain $A$ is a Dedekind domain if and only if $A$ is Noetherian and, for all ideals $I$ and
$J$ of $A$, $I$ divides $J$ if and only if $J \subseteq I$.

## Sources

- ATLAS NumberTheoryI Theorem 3.23, conditions (1) and (5).

Formalized by `isDedekindDomain_iff_contain_isDivide`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/Characterizations.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/Characterizations.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-dedekind-domain-iff-contain-is-divide).

## Dedekind domains via principal products

An integral domain $A$ is a Dedekind domain if
and only if for every nonzero ideal $I$ of $A$ there is an ideal $J$ of $A$ such that $IJ$ is a
nonzero principal ideal.

## Sources

- ATLAS NumberTheoryI Theorem 3.23(6), corrected: the recorded condition omits both nonzero qualifiers, which makes it vacuous (take $J = 0$).

Formalized by `isDedekindDomain_iff_principalProduct`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/Characterizations.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/Characterizations.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-dedekind-domain-iff-principal-product).

## Equivalent characterizations of Dedekind domains

For an integral domain $A$, the
following are equivalent: (1) $A$ is a Dedekind domain; (2) $A$ is Noetherian and, for all
ideals $I$ and $J$ of $A$, $I$ divides $J$ if and only if $J \subseteq I$; (3) for every
nonzero ideal $I$ of $A$ there is an ideal $J$ of $A$ such that $IJ$ is a nonzero principal
ideal.

## Sources

- ATLAS NumberTheoryI Theorem 3.23, conditions (1), (5) and (6), with (6) corrected by the two nonzero qualifiers.

Formalized by `isDedekindDomain_tfae_contain_isDivide_principalProduct`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/Characterizations.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/Characterizations.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-dedekind-domain-tfae-contain-is-divid).

## Dedekind domains are the integrally closed Noetherian domains of dimension at most one

Let $A$ be a Noetherian integral domain. Then $A$ is integrally closed and has Krull dimension
at most one if and only if $A$ is a Dedekind domain.

## Sources

- ATLAS NumberTheoryI Definition 2.10, characterization form.

Formalized by `integrallyClosed_dimensionLEOne_iff_isDedekindDomain`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/DVRCharacterization.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/DVRCharacterization.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#integrally-closed-dimension-leone-iff-is).

## DVR localizations in a Noetherian domain

Let $A$ be a Noetherian integral domain. Then
the localizations $A_P$ at all nonzero prime ideals $P$ of $A$ are discrete valuation rings if
and only if $A$ is integrally closed and has Krull dimension at most one.

## Sources

- ATLAS NumberTheoryI Proposition 2.9.

Formalized by `isDiscreteValuationRing_localization_atPrime_iff_integrallyClosed_dimensionLEOne`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/DVRCharacterization.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/DVRCharacterization.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-discrete-valuation-ring-localization).

## Quotients of Dedekind domains by nonzero ideals are principal ideal rings

Every quotient
of a Dedekind domain by a nonzero ideal is a principal ideal ring.

Formalized by `IsDedekindDomain.isPrincipalIdealRing_quotient`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/PrincipalIdealQuotient.lean, line 16](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/PrincipalIdealQuotient.lean#L16). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-principal-ideal-ring-quotient).

## Domains with principal quotients are Noetherian

Let $A$ be an integral domain such that
for every nonzero ideal $I$ of $A$ the quotient ring $A/I$ is a principal ideal ring. Then $A$ is
a Noetherian ring.

For a nonzero ideal $I$, pick a nonzero $a \in I$; the image of $I$ in the principal ideal ring
$A/(a)$ is principal, and lifting a generator to some $b \in I$ shows $I = (a, b)$, so $I$ is
finitely generated.

Formalized by `isNoetherianRing_of_forall_isPrincipalIdealRing_quotient`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-noetherian-ring-of-forall-is-principa).

## Principal quotients give discrete valuation rings at nonzero primes

Let $A$ be an
integral domain such that for every nonzero ideal $I$ of $A$ the quotient ring $A/I$ is a
principal ideal ring. Then for every nonzero prime ideal $P$ of $A$, the localization $A_P$ is a
discrete valuation ring.

The image of $P$ in $A/P^2$ is principal, generated by the image of some $\pi \in P$, so
$P \subseteq (\pi) + P^2$. Hence the maximal ideal $\mathfrak{m}$ of $A_P$ satisfies
$\mathfrak{m} \subseteq (\pi) + \mathfrak{m}^2$, and Nakayama's lemma gives
$\mathfrak{m} = (\pi)$.

Formalized by `isDiscreteValuationRing_localization_atPrime_of_forall_isPrincipalIdealRing_quotient`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-discrete-valuation-ring-localization-2).

## Dedekind domains from principal quotients

Let $A$ be an integral domain such that for
every nonzero ideal $I$ of $A$ the quotient ring $A/I$ is a principal ideal ring. Then $A$ is a
Dedekind domain.

## Sources

- converse of ATLAS NumberTheoryI, Corollary 3.18, derived independently.

Formalized by `isDedekindDomain_of_forall_isPrincipalIdealRing_quotient`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-dedekind-domain-of-forall-is-principa).

## Two generators with one prescribed give principal quotients

Let $A$ be an integral
domain such that for every nonzero ideal $I$ of $A$ and every nonzero $a \in I$ there is $b \in A$
with $I = (a, b)$. Then for every nonzero ideal $I$ of $A$, the quotient ring $A/I$ is a
principal ideal ring.

For a nonzero ideal $I$, an ideal $J$ of $A/I$ has preimage $J'$ in $A$ containing $I$; pick a
nonzero $a \in I$, write $J' = (a, b)$, and the image of $b$ generates $J$ since the image of $a$
is zero.

Formalized by `isPrincipalIdealRing_quotient_of_forall_exists_span_pair`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-principal-ideal-ring-quotient-of-fora).

## Dedekind domains from two generators with one prescribed

Let $A$ be an integral domain
such that for every nonzero ideal $I$ of $A$ and every nonzero $a \in I$ there is $b \in A$ with
$I = (a, b)$. Then $A$ is a Dedekind domain.

## Sources

- converse of ATLAS NumberTheoryI, Theorem 3.22, derived independently.

Formalized by `isDedekindDomain_of_forall_exists_span_pair`, a theorem declared in [MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/DedekindDomain/QuotientPIRConverse.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html#is-dedekind-domain-of-forall-exists-span).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Characterizations of Dedekind domains](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/dedekind-domains/characterizations-of-dedekind-domains)
