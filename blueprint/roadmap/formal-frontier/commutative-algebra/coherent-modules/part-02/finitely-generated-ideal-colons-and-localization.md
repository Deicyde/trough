---
declaration: theorem
origin: cited
lean: IsLocalization.comap_map_colon
statement: formalized
proof: formalized
---

# Finitely generated ideal colons and localization

For commutative
semirings `R`, `S`, a submonoid `T : Submonoid R` and an `R`-algebra `S`
satisfying `[IsLocalization T S]`,
[`IsLocalization.comap_map_colon`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Localization.lean)
gives
```lean
Ideal.comap (algebraMap R S)
    ((I.colon (J : Set R)).map (algebraMap R S)) =
  (Ideal.comap (algebraMap R S) (I.map (algebraMap R S))).colon (J : Set R)
```
for any ideal `I` and finitely generated ideal `J`, with
`Submodule.FG (J : Submodule R R)`. Thus multiplicative saturation, expressed
by extension followed by contraction, commutes with colon by `J`.
Finite generation concerns the ideal, not its underlying set. The two
universes are independent; zero semirings, `0 ∈ T`, `J = ⊥` and top ideals
are allowed. No finiteness or radicality of `I` is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `IsLocalization.comap_map_colon` (theorem), declared in [CoherentModules/RingTheory/Ideal/Localization.lean, line 29](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Localization.lean#L29).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `IsLocalization.comap_map_colon` in CoherentModules/RingTheory/Ideal/Localization.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Localization.lean#L29)
