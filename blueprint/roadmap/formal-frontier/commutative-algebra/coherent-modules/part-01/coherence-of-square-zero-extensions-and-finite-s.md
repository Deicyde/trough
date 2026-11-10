---
declaration: theorem
origin: cited
lean: TrivSqZeroExt.isCoherentRing_iff_finite_of_divisionRing, TrivSqZeroExt.isCoherentRing_finsupp_iff_finite, TrivSqZeroExt.finsupp_faithfullyFlat_and_not_isCoherentRing, TrivSqZeroExt.finite_of_isCoherentRing_of_injective_smul, TrivSqZeroExt.isCoherentRing_iff_finite, TrivSqZeroExt.isCoherentRing
statement: formalized
proof: formalized
---

# Coherence of square-zero extensions and finite-support idealizations

For a division ring D and a bimodule M in independent universes, the trivial square-zero extension D ⋉ M is left coherent if and only if M is finitely generated on the left. Both compatible module actions are retained, without centrality. For the stock pointwise left module ι →₀ D and any compatible right action, this is equivalent to finiteness of ι, including the empty index type. For a field k and infinite ι, the canonical inclusion algebra k → TrivSqZeroExt k (ι →₀ k), a ↦ (a, 0), is faithfully flat but not coherent. The canonical field criterion allows the zero coefficient space; finite generation means finite dimension, not a finite underlying set. More generally, for a possibly noncommutative ring R and a bimodule M with its given commuting left and right actions, left coherence of R ⋉ M implies finite generation of M on the left whenever r ↦ r • v is injective for one vector v. Sufficiency holds for a left coherent base and a coefficient bimodule finitely presented on the left.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TrivSqZeroExt.isCoherentRing_iff_finite_of_divisionRing` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean, line 122](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L122).
- `TrivSqZeroExt.isCoherentRing_finsupp_iff_finite` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean, line 53](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean#L53).
- `TrivSqZeroExt.finsupp_faithfullyFlat_and_not_isCoherentRing` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean, line 84](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean#L84).
- `TrivSqZeroExt.finite_of_isCoherentRing_of_injective_smul` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean, line 99](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L99).
- `TrivSqZeroExt.isCoherentRing_iff_finite` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean, line 156](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L156).
- `TrivSqZeroExt.isCoherentRing` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean, line 57](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L57).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: formalization.yaml](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/formalization.yaml)
- [Source of `TrivSqZeroExt.isCoherentRing_iff_finite_of_divisionRing` in CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L122)
- [Source of `TrivSqZeroExt.isCoherentRing_finsupp_iff_finite` in CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean#L53)
- [Source of `TrivSqZeroExt.finsupp_faithfullyFlat_and_not_isCoherentRing` in CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finsupp.lean#L84)
- [Source of `TrivSqZeroExt.finite_of_isCoherentRing_of_injective_smul` in CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L99)
- [Source of `TrivSqZeroExt.isCoherentRing_iff_finite` in CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L156)
- [Source of `TrivSqZeroExt.isCoherentRing` in CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Coherent.lean#L57)
