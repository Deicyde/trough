---
declaration: instance
origin: cited
lean: PolynomialModule.Extension.polynomialModule, PolynomialModule.Extension.coeff_smul, PolynomialModule.Extension.universalProperty, PolynomialModule.Extension.coordinate, PolynomialModule.Extension.polynomialLinearEquivPolynomialModule
statement: formalized
---

# Polynomial scalar extension over semirings

For any possibly noncommutative semiring R and any left R-module M with additive commutative-monoid structure, finitely supported coefficient sequences form a canonical R[X]-module. Constant polynomials act by the original coefficient action and X shifts degree. This module represents C-semilinear maps from M and is natural under semilinear coefficient maps. Under the original commutative-ring and additive-group hypotheses, it agrees with Mathlib's PolynomialModule, including its fixed polynomial action and ordered coefficient formula.

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/formalization.yaml) of [FormalFrontier/graded-rings](https://github.com/FormalFrontier/graded-rings) at commit [6a459e8e](https://github.com/FormalFrontier/graded-rings/tree/6a459e8e4d20392fe4f2a58191a621592f4788bb), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `PolynomialModule.Extension.polynomialModule` (instance), declared in [GradedRings/PolynomialModule/Basic.lean, line 232](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/Basic.lean#L232).
- `PolynomialModule.Extension.coeff_smul` (theorem), declared in [GradedRings/PolynomialModule/Basic.lean, line 393](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/Basic.lean#L393).
- `PolynomialModule.Extension.universalProperty` (def), declared in [GradedRings/PolynomialModule/UniversalProperty.lean, line 187](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/UniversalProperty.lean#L187).
- `PolynomialModule.Extension.coordinate` (def), declared in [GradedRings/PolynomialModule/UniversalProperty.lean, line 444](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/UniversalProperty.lean#L444).
- `PolynomialModule.Extension.polynomialLinearEquivPolynomialModule` (def), declared in [GradedRings/PolynomialModule/Comparison.lean, line 198](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/Comparison.lean#L198).

Read from the source at commit [6a459e8e](https://github.com/FormalFrontier/graded-rings/tree/6a459e8e4d20392fe4f2a58191a621592f4788bb), without running Lean.

## Sources

- [graded-rings at 6a459e8e: formalization.yaml](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/formalization.yaml)
- [Source of `PolynomialModule.Extension.polynomialModule` in GradedRings/PolynomialModule/Basic.lean](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/Basic.lean#L232)
- [Source of `PolynomialModule.Extension.coeff_smul` in GradedRings/PolynomialModule/Basic.lean](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/Basic.lean#L393)
- [Source of `PolynomialModule.Extension.universalProperty` in GradedRings/PolynomialModule/UniversalProperty.lean](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/UniversalProperty.lean#L187)
- [Source of `PolynomialModule.Extension.coordinate` in GradedRings/PolynomialModule/UniversalProperty.lean](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/UniversalProperty.lean#L444)
- [Source of `PolynomialModule.Extension.polynomialLinearEquivPolynomialModule` in GradedRings/PolynomialModule/Comparison.lean](https://github.com/FormalFrontier/graded-rings/blob/6a459e8e4d20392fe4f2a58191a621592f4788bb/GradedRings/PolynomialModule/Comparison.lean#L198)
