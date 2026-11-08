---
declaration: def
origin: cited
lean: SemimoduleCat.kernelIsLimit
statement: formalized
---

# Kernels over semirings

For an arbitrary `Semiring R`,
[`SemimoduleCat.kernelIsLimit`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Category/ModuleCat/Kernels.lean)
makes the existing kernel submodule, with its subtype inclusion, a categorical
kernel. `SemimoduleCat.hasKernels_semimoduleCat` gives kernels in
`SemimoduleCat.{v} R`, with independent coefficient and carrier universes.
Over a ring, `ModuleCat.kernelCone_semimodule_hom_apply` shows that the
comparison with Mathlib's module kernel preserves underlying elements.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `SemimoduleCat.kernelIsLimit` (def), declared in [CoherentModules/Algebra/Category/ModuleCat/Kernels.lean, line 68](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Category/ModuleCat/Kernels.lean#L68).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `SemimoduleCat.kernelIsLimit` in CoherentModules/Algebra/Category/ModuleCat/Kernels.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/Category/ModuleCat/Kernels.lean#L68)
