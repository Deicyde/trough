---
declaration: theorem
origin: cited
lean: Module.FaithfullyFlat.directSum_away_iff
statement: formalized
proof: formalized
---

# Families of principal localizations

For a `CommRing R` and any family
`s : ι → R`,
[`Module.FaithfullyFlat.directSum_away_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Localization.lean)
characterizes faithful flatness of `⨁ i, Localization.Away (s i)` by
`Ideal.span (Set.range s) = ⊤`, without finite or nonempty indexing.
For **finite** index types,
[`Module.FaithfullyFlat.pi_away_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Localization.lean)
gives the same unit-span criterion for `Π i, Localization.Away (s i)`.
The localizations need not individually be faithfully flat; zero rings and
independent ring and index universes are allowed. The finite-index hypothesis
for the product unit-span criterion is essential: the
[coordinate-idempotent product](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Flat/LocalizationProductInfinite.lean)
is faithfully flat although its generators span a proper ideal. The
[ideal-detection consequences](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModulesTest/RingTheory/Flat/LocalizationProductCriteria.lean)
show that this ideal is not finitely generated.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.FaithfullyFlat.directSum_away_iff` (theorem), declared in [CoherentModules/RingTheory/Flat/Localization.lean, line 73](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Localization.lean#L73).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.FaithfullyFlat.directSum_away_iff` in CoherentModules/RingTheory/Flat/Localization.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Flat/Localization.lean#L73)
