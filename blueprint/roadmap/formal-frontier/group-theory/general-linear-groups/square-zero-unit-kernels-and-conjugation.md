---
declaration: def
origin: cited
lean: RingHom.unitsKerEquivOfSquareZero, RingHom.unitsKerEquivOfSquareZero_conj_apply_coe
statement: formalized
---

# Square-zero unit kernels and conjugation

For any ring homomorphism f : R →+* S from a possibly noncommutative ring to a semiring with (ker f)^2 = 0, the units mapping to 1 are isomorphic to the additive group ker f by u ↦ u - 1 and x ↦ 1 + x, and conjugation by any g : Rˣ corresponds to x ↦ g * x * g⁻¹, without a surjectivity hypothesis.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `RingHom.unitsKerEquivOfSquareZero` (def), declared in [GeneralLinearGroups/SquareZeroUnits.lean, line 59](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/SquareZeroUnits.lean#L59).
- `RingHom.unitsKerEquivOfSquareZero_conj_apply_coe` (theorem), declared in [GeneralLinearGroups/SquareZeroUnits.lean, line 118](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/SquareZeroUnits.lean#L118).

Read from the source at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), without running Lean.

## Sources

- [general-linear-groups at a2199cf0: formalization.yaml](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/formalization.yaml)
- [Source of `RingHom.unitsKerEquivOfSquareZero` in GeneralLinearGroups/SquareZeroUnits.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/SquareZeroUnits.lean#L59)
- [Source of `RingHom.unitsKerEquivOfSquareZero_conj_apply_coe` in GeneralLinearGroups/SquareZeroUnits.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/SquareZeroUnits.lean#L118)
