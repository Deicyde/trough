---
declaration: def
origin: cited
lean: Filter.Product.compTendsto
statement: formalized
---

# Reindexing dependent filter products

For independently universed indices and fibres, a map `u : ι → κ` with
`Tendsto u F G` induces
[`Filter.Product.compTendsto`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/CompTendsto.lean)
from `G.Product R` to `F.Product (fun i => R (u i))`. It sends a section to its
precomposition, respects identity and composition, and agrees with the existing
`Filter.Germ.compTendsto` on constant families. No algebra, total-section existence
or proper-filter assumption is needed. The full criterion
`compTendsto_injective_iff` says that pullback is injective exactly when the original
total-section type is empty or
`Filter.map u F ⊓ principal {j | Nontrivial (R j)} =
G ⊓ principal {j | Nontrivial (R j)}`. Exact filter-image equality therefore suffices
(`compTendsto_injective_of_map_eq`), without injectivity of `u`, but is not necessary
for a fixed family. An index equivalence makes pullback surjective with only forward
convergence (`compTendsto_surjective_of_equiv`), but not necessarily injective.
Convergence in both directions gives `Filter.Product.compTendstoEquiv`, whose inverse
uses canonical dependent Pi reindexing. The
[dependent Bool client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/Filter/Product/CompTendsto.lean)
contrasts a four-to-two noninjective pullback with a two-to-two injective pullback
for the same unequal filters, by making the ignored fibre a singleton. It also
exhibits an injective, non-surjective diagonal.

The underlying
[`Filter.forall_eventually_eq_iff`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Basic.lean) works for
fibres in any independently universed `Sort`: two filters give the same eventual
equality on all pairs of total sections exactly when there is no total section or
their restrictions to `{i | ∃ x y : R i, x ≠ y}` agree. For Type-valued families,
[`Filter.productSetoid_eq_iff`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product.lean) expresses
this using the existing section setoids and stock `Nontrivial` support. An empty
fibre ignored by a filter still prevents total sections; eventual inhabitation
cannot replace the empty-total-section alternative.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Filter.Product.compTendsto` (def), declared in [MinimalPrimes/Order/Filter/Product/CompTendsto.lean, line 56](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/CompTendsto.lean#L56).

Read from the source at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), without running Lean.

## Sources

- [minimal-primes at 45952e34: README, headline results](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results)
- [Source of `Filter.Product.compTendsto` in MinimalPrimes/Order/Filter/Product/CompTendsto.lean](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/CompTendsto.lean#L56)
