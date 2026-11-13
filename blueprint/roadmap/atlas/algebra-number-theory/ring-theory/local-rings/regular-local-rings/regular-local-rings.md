---
declaration: section
origin: cited
lean: IsRegularLocalRing.quotient_span_singleton_of_notMem_sq_of_forall_minimalPrimes_notMem, IsLocalRing.uniqueFactorizationMonoid_of_isPrincipalIdealRing_quotient, IsRegularLocalRing.mvPowerSeries_fin, IsRegularLocalRing.isDomain_and_isIntegrallyClosed_of_ringKrullDim_le_one, IsRegularLocalRing.adjoinRoot_of_monic_of_coeff_mem_maximalIdeal_of_coeff_zero_not_mem_sq, IsRegularLocalRing.uniqueFactorizationMonoid_of_ringKrullDim_le_two
statement: formalized
proof: formalized
---

# Regular local rings: its own results

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html).

## Quotient of a regular local ring by a regular parameter is regular

Quotienting a regular local ring by a parameter outside the square of the
maximal ideal and outside every minimal prime stays regular, with the
embedding dimension dropping by exactly one.

Formalized by `IsRegularLocalRing.quotient_span_singleton_of_notMem_sq_of_forall_minimalPrimes_notMem`, a theorem declared in [MathlibExt/RingTheory/RegularLocalRing/QuotientSpanSingleton.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/RegularLocalRing/QuotientSpanSingleton.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html#quotient-span-singleton-of-not-mem-sq-of).

## Unique factorization from a principal ideal ring quotient

A Noetherian local domain is a unique factorization monoid when
quotienting by a principal prime ideal gives a principal ideal ring.

Formalized by `IsLocalRing.uniqueFactorizationMonoid_of_isPrincipalIdealRing_quotient`, a theorem declared in [MathlibExt/RingTheory/LocalRing/UFDQuotient.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/LocalRing/UFDQuotient.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html#unique-factorization-monoid-of-is-princi).

## Multivariable power series over a regular local ring are regular local

Multivariable power series over a regular local ring form a
regular local ring. The discrete-valuation-ring case follows by typeclass
inference, since a DVR is a regular local ring.

Formalized by `IsRegularLocalRing.mvPowerSeries_fin`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/RegularLocalRing.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/MvPowerSeries/RegularLocalRing.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html#mv-power-series-fin).

## Regular local rings of dimension at most one are normal domains

A regular local ring of Krull dimension at most one is a domain and
integrally closed.

Formalized by `IsRegularLocalRing.isDomain_and_isIntegrallyClosed_of_ringKrullDim_le_one`, a theorem declared in [MathlibExt/RingTheory/Regular/DimLeOne.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/Regular/DimLeOne.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html#is-domain-and-is-integrally-closed-of-ri).

## Adjoining a root of an Eisenstein-like polynomial preserves regularity

Adjoining a root of a monic polynomial whose non-leading coefficients lie
in the maximal ideal and whose constant coefficient lies outside the square
of the maximal ideal preserves regularity and Krull dimension.

Formalized by `IsRegularLocalRing.adjoinRoot_of_monic_of_coeff_mem_maximalIdeal_of_coeff_zero_not_mem_sq`, a theorem declared in [MathlibExt/RingTheory/RegularLocalRing/AdjoinRoot.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/RegularLocalRing/AdjoinRoot.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html#adjoin-root-of-monic-of-coeff-mem-maxima).

## Regular local rings of dimension at most two are UFDs

A regular local ring of Krull dimension at most two is a unique
factorization monoid.

Formalized by `IsRegularLocalRing.uniqueFactorizationMonoid_of_ringKrullDim_le_two`, a theorem declared in [MathlibExt/RingTheory/RegularLocalRing/UFD.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/RegularLocalRing/UFD.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html#unique-factorization-monoid-of-ring-krul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular local rings](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/regular-local-rings/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RingTheory/local-rings/regular-local-rings)
