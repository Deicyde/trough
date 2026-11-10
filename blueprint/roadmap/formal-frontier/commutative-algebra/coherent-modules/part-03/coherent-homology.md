---
declaration: theorem
origin: cited
lean: CategoryTheory.ShortComplex.isCoherent_homology
statement: formalized
proof: formalized
---

# Coherent homology

Over any possibly noncommutative `Ring R`, a three-term
complex `S : CategoryTheory.ShortComplex (ModuleCat.{v} R)` with finite left
term `S.X₁` and coherent middle and right terms `S.X₂`, `S.X₃` has coherent
homology, by
[`CategoryTheory.ShortComplex.isCoherent_homology`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/ModuleCat.lean).
The conclusion concerns the chosen categorical `S.homology` with its given
`R`-action. Neither the left term nor `R` is assumed coherent, and no exactness
hypothesis is imposed. The ring universe is independent of the common object
universe `v`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `CategoryTheory.ShortComplex.isCoherent_homology` (theorem), declared in [CoherentModules/ModuleCat.lean, line 127](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/ModuleCat.lean#L127).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `CategoryTheory.ShortComplex.isCoherent_homology` in CoherentModules/ModuleCat.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/ModuleCat.lean#L127)
