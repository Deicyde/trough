---
declaration: def
origin: cited
lean: Ideal.principalUnitsQuotientEquiv, Ideal.principalUnitsToQuotient_ker, Ideal.principalUnitsQuotientEquiv_symm_mk
statement: formalized
---

# Principal-unit quotients and Jacobson lifting

For left ideals I, J in any ring R with I^2 ≤ J and I ≤ Ring.jacobson R, the subgroup U(I) = {u : Rˣ | u - 1 ∈ I} modulo the kernel of u ↦ [u - 1] is canonically isomorphic to the additive quotient I / (I ∩ J), with inverse [x] ↦ [1 + x], without two-sidedness or J ≤ I.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Ideal.principalUnitsQuotientEquiv` (def), declared in [GeneralLinearGroups/PrincipalUnits.lean, line 212](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L212).
- `Ideal.principalUnitsToQuotient_ker` (theorem), declared in [GeneralLinearGroups/PrincipalUnits.lean, line 175](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L175).
- `Ideal.principalUnitsQuotientEquiv_symm_mk` (theorem), declared in [GeneralLinearGroups/PrincipalUnits.lean, line 231](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L231).

Read from the source at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), without running Lean.

## Sources

- [general-linear-groups at a2199cf0: formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml)
- [Source of `Ideal.principalUnitsQuotientEquiv` in GeneralLinearGroups/PrincipalUnits.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L212)
- [Source of `Ideal.principalUnitsToQuotient_ker` in GeneralLinearGroups/PrincipalUnits.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L175)
- [Source of `Ideal.principalUnitsQuotientEquiv_symm_mk` in GeneralLinearGroups/PrincipalUnits.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/PrincipalUnits.lean#L231)
