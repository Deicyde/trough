---
declaration: theorem
origin: cited
lean: Ideal.isNilpotent_stabilizer_quotient_one_of_pow_eq_bot, Ideal.nilpotencyClass_stabilizer_quotient_one_le_of_pow_eq_bot
statement: formalized
proof: formalized
---

# Nilpotent principal-unit groups

For any left ideal I of a possibly noncommutative ring R and any natural N with I^N = 0, the principal-unit subgroup {u : Rˣ | u - 1 ∈ I} is nilpotent of class at most N - 1, using natural subtraction and including the trivial-subgroup cases N = 0 and N = 1.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.isNilpotent_stabilizer_quotient_one_of_pow_eq_bot` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 267](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L267).
- `Ideal.nilpotencyClass_stabilizer_quotient_one_le_of_pow_eq_bot` (theorem), declared in [GeneralLinearGroups/PrincipalUnits/Filtration.lean, line 278](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L278).

Read from the source at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), without running Lean.

## Sources

- [general-linear-groups at a2199cf0: formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml)
- [Source of `Ideal.isNilpotent_stabilizer_quotient_one_of_pow_eq_bot` in GeneralLinearGroups/PrincipalUnits/Filtration.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L267)
- [Source of `Ideal.nilpotencyClass_stabilizer_quotient_one_le_of_pow_eq_bot` in GeneralLinearGroups/PrincipalUnits/Filtration.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits/Filtration.lean#L278)
