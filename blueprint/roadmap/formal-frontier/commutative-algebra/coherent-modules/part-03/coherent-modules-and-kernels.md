---
declaration: class
origin: cited
lean: Module.IsCoherent
statement: formalized
---

# Coherent modules and kernels

For a ring and an additive commutative monoid
with its given module structure, [`Module.IsCoherent`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Basic.lean)
means finite generation together with finite presentation of every finitely
generated submodule. [`Module.IsCoherent.iff_finite_and_fg_ker`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Basic.lean)
characterizes this by finitely generated kernels of *all* linear maps from
finite-rank free modules, including rank zero. The same leaf proves closure
under finitely generated submodules, finite products, kernels and cokernels,
quotients by finitely generated submodules, and extensions (with the stated
exactness and endpoint conditions). For rings `R` and `S`,
`Module.IsCoherent.of_restrictScalars` transfers coherence of an additive
commutative group `N` from `R` to `S` when `S` is finite over `R` and the given
module structures form scalar towers `R → S → S` and `R → S → N`.
No coherence of `S` over `R` is required, and the three universes are independent.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Module.IsCoherent` (class), declared in [CoherentModules/Basic.lean, line 51](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Basic.lean#L51).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Module.IsCoherent` in CoherentModules/Basic.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Basic.lean#L51)
