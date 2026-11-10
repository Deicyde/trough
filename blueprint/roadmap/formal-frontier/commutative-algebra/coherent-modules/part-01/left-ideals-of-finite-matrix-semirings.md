---
declaration: def
origin: cited
lean: Submodule.matrixRowsOrderIso
statement: formalized
---

# Left ideals of finite matrix semirings

For `[Semiring R]`, `[Fintype I]`
and `[DecidableEq I]`, including empty `I`,
[`Submodule.matrixRowsOrderIso`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/RowIdeal.lean)
identifies left ideals of `Matrix I I R` with `R`-submodules of the row module
`I → R`. Left Artinianity and left Noetherianity of the matrix semiring are
equivalent to the corresponding conditions on this row module, not to
unrestricted conditions on the coefficient semiring.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Submodule.matrixRowsOrderIso` (def), declared in [CoherentModules/LinearAlgebra/Matrix/RowIdeal.lean, line 172](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/RowIdeal.lean#L172).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Submodule.matrixRowsOrderIso` in CoherentModules/LinearAlgebra/Matrix/RowIdeal.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/LinearAlgebra/Matrix/RowIdeal.lean#L172)
