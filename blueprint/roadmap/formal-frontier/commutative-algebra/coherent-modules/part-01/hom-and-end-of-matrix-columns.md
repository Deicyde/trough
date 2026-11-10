---
declaration: def
origin: cited
lean: LinearMap.matrixModuleHomAddEquiv
statement: formalized
---

# Hom and End of matrix columns

Over an arbitrary possibly noncommutative
semiring `R`, finite-sum matrix actions retain the given coefficient-module
structures. For a finite nonempty index `I`,
[`LinearMap.matrixModuleHomAddEquiv`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/ColumnHom.lean)
identifies coefficient-linear maps additively with matrix-linear maps of columns;
its inverse is characterized at every coordinate.
`Module.matrixModuleEndRingEquiv` preserves the usual order of composition.
For the regular coefficient module this gives `Rᵐᵒᵖ`, not the full matrix semiring.
With empty `I`, coordinate extension is still surjective, but need not be
injective. Zero semirings are allowed, and no scalar-module structure on a
general Hom is used.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `LinearMap.matrixModuleHomAddEquiv` (def), declared in [CoherentModules/LinearAlgebra/Matrix/ColumnHom.lean, line 99](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/ColumnHom.lean#L99).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `LinearMap.matrixModuleHomAddEquiv` in CoherentModules/LinearAlgebra/Matrix/ColumnHom.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/ColumnHom.lean#L99)
