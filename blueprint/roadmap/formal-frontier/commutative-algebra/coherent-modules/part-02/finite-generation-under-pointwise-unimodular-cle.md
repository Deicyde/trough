---
declaration: theorem
origin: cited
lean: Submodule.fg_of_fg_comap_of_one_mem_span_smul_mem_range
statement: formalized
proof: formalized
---

# Finite generation under pointwise unimodular clearing

For arbitrary,
possibly noncommutative semirings `R`, `S` and `f : M →ₛₗ[φ] N` between
additive commutative left semimodules,
[`Submodule.fg_of_fg_comap_of_one_mem_span_smul_mem_range`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/SpanRank.lean)
proves an `S`-submodule `P` finitely generated if `P.comap f` is finitely
generated over `R` and, for every `n ∈ P`, the clearers
`{a : S | ∃ m : M, f m = a • n}` generate the unit **left** ideal.
The companion `span_image_comap_eq_of_one_mem_span_smul_mem_range` identifies
`P` with the target-scalar span of its comap image without any finite-generation
premise. The existing single-left-inverse and unit-clearing criteria remain
specializations. The four universes are independent; neither Noetherianity
nor surjectivity of `φ` or `f` is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Submodule.fg_of_fg_comap_of_one_mem_span_smul_mem_range` (theorem), declared in [CoherentModules/Algebra/Module/SpanRank.lean, line 106](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/SpanRank.lean#L106).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Submodule.fg_of_fg_comap_of_one_mem_span_smul_mem_range` in CoherentModules/Algebra/Module/SpanRank.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/SpanRank.lean#L106)
