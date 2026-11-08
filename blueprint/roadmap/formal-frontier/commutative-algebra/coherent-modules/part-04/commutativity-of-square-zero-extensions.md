---
declaration: theorem
origin: cited
lean: TrivSqZeroExt.isMulCommutative_iff
statement: formalized
proof: formalized
---

# Commutativity of square-zero extensions

For `Mul R`, `AddZeroClass M`,
`IsAddCommutative M`, and two given zero-preserving scalar actions
`[SMulZeroClass R M]` and `[SMulZeroClass Rᵐᵒᵖ M]`,
[`TrivSqZeroExt.isMulCommutative_iff`](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Commutativity.lean)
characterizes `IsMulCommutative (TrivSqZeroExt R M)` by
`IsMulCommutative R ∧ IsCentralScalar R M`. It retains the original
multiplication, addition, zero and both actions, with independent carrier
universes. No additive associativity, coefficient zero or one, module structure,
action compatibility or finiteness is required. This is a criterion for the
multiplication alone, not an assertion of a unit or a square-zero ideal at
these hypotheses.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results) of [FormalFrontier/coherent-modules](https://github.com/FormalFrontier/coherent-modules) at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `TrivSqZeroExt.isMulCommutative_iff` (theorem), declared in [CoherentModules/Algebra/TrivSqZeroExt/Commutativity.lean, line 47](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Commutativity.lean#L47).

Read from the source at commit [b670b34e](https://github.com/FormalFrontier/coherent-modules/tree/b670b34e8741624c22b88375b9086d6d393cbbc3), without running Lean.

## Sources

- [coherent-modules at b670b34e: README, headline results](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/README.md#headline-results)
- [Source of `TrivSqZeroExt.isMulCommutative_iff` in CoherentModules/Algebra/TrivSqZeroExt/Commutativity.lean](https://github.com/FormalFrontier/coherent-modules/blob/b670b34e8741624c22b88375b9086d6d393cbbc3/CoherentModules/Algebra/TrivSqZeroExt/Commutativity.lean#L47)
