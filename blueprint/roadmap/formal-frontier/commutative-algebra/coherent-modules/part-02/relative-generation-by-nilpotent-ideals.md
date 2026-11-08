---
declaration: theorem
origin: cited
lean: Submodule.le_sup_pow_smul_of_le_sup_smul
statement: formalized
proof: formalized
---

# Relative generation by nilpotent ideals

For a left ideal `I` of a
possibly noncommutative semiring `R` and submodules `N`, `P` of an additive
commutative `R`-semimodule,
[`Submodule.le_sup_pow_smul_of_le_sup_smul`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Operations.lean)
propagates `P ≤ N ⊔ I • P` to `P ≤ N ⊔ (I ^ n) • P` for every natural `n`.
Under global nilpotence `IsNilpotent I`, the companion
`Submodule.le_of_le_sup_smul_of_isNilpotent` gives `P ≤ N`.
The carrier universes are independent, and no finite generation, additive
inverses, cancellation or nontriviality is required.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Submodule.le_sup_pow_smul_of_le_sup_smul` (theorem), declared in [CoherentModules/RingTheory/Ideal/Operations.lean, line 51](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Operations.lean#L51).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `Submodule.le_sup_pow_smul_of_le_sup_smul` in CoherentModules/RingTheory/Ideal/Operations.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/RingTheory/Ideal/Operations.lean#L51)
