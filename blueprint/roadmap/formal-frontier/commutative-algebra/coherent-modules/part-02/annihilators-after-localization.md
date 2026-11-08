---
declaration: theorem
origin: cited
lean: IsLocalizedModule.map_annihilator
statement: formalized
proof: formalized
---

# Annihilators after localization

For commutative semirings `R`, `A`,
a submonoid `T : Submonoid R`, an `R`-algebra `A` realizing localization at
`T`, and a standard localized-module map `f : M →ₗ[R] N`,
[`IsLocalizedModule.map_annihilator`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/LocalizedModule.lean)
gives
```lean
Ideal.map (algebraMap R A) (Module.annihilator R M) =
  Module.annihilator A N
```
when `M` is finitely generated over `R`. The semimodules are additive
commutative monoids, `N` has its compatible `A`-action, and all four carrier
universes are independent. Zero semirings, zero modules and `0 ∈ T` are
allowed; no finite presentation, flatness or faithful-action assumption is
added. The supporting
[`IsLocalizedModule.comp_eq_iff_exists_smul_eq`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/LocalizedModule/Finite.lean)
characterizes equality after localization for two maps from a finitely
generated semimodule by a single submonoid multiplier making them equal.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `IsLocalizedModule.map_annihilator` (theorem), declared in [CoherentModules/Algebra/Module/LocalizedModule.lean, line 82](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/LocalizedModule.lean#L82).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `IsLocalizedModule.map_annihilator` in CoherentModules/Algebra/Module/LocalizedModule.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Module/LocalizedModule.lean#L82)
