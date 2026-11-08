---
declaration: def
origin: cited
lean: TrivSqZeroExt.kerIdealLinearEquiv
statement: formalized
---

# Square-zero kernels and projection base change

For a commutative semiring
`R` and an additive commutative `R`-module `M`,
[`TrivSqZeroExt.kerIdealLinearEquiv`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finite.lean)
identifies the projection kernel with `M`. If `M` is finite over `R`,
[`kerIdeal_finite`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finite.lean) makes the
kernel finite over the **whole extension**.
[`kerIdealBaseChange`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finite.lean)
identifies the projection-base-changed kernel with `M` **without** a finiteness
assumption; its pure-tensor and inverse formulas are simp lemmas.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TrivSqZeroExt.kerIdealLinearEquiv` (def), declared in [CoherentModules/Algebra/TrivSqZeroExt/Finite.lean, line 45](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finite.lean#L45).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `TrivSqZeroExt.kerIdealLinearEquiv` in CoherentModules/Algebra/TrivSqZeroExt/Finite.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Finite.lean#L45)
