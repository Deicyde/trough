---
declaration: theorem
origin: cited
lean: NumberField.ArchimedeanNorms.height_eq, NumberField.ArchimedeanNorms.height_pos, NumberField.ArchimedeanNorms.normalizedLogHeight_eq, NumberField.ArchimedeanNorms.height_tensor, NumberField.ArchimedeanNorms.height_rescale, NumberField.ArchimedeanNorms.height_comap, NumberField.ArchimedeanNorms.height_eq_rationalFrame, NumberField.ArchimedeanNorms.normalizedLogHeight_eq_rationalFrame, NumberField.ArchimedeanNorms.height_eq_finitePlace
statement: formalized
proof: formalized
---

# Intrinsic heights of normed invertible modules

For a number field K, definite seminorms on the archimedean completion fibres of an invertible module over its ring of integers define a positive height equal to the section index divided by the weighted norm product for every nonzero integral section. Ordinary norms have weight one at real places and two at complex places. The normalized logarithmic height is (log index minus the weighted log norm sum) divided by [K:Q]. Tensor metrics multiply heights and add logarithmic heights. Positive placewise rescaling divides height by the weighted factor and subtracts its degree-normalized logarithm; equivalence pullback preserves both heights. Every rational frame evaluates this same height as the reciprocal of the product of its coefficient-ideal norm and the weighted archimedean product at its unit vector. Equivalently, the numerator is the finite-support product of residue cardinalities with negative coefficient-ideal exponents, with no extra finite-place weights. No integral basis is assumed, and only logarithmic height is divided by [K:Q].

*Quoted from the highlights in [formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml) of [FormalFrontier/dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic) at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `NumberField.ArchimedeanNorms.height_eq` (theorem), declared in [DedekindIdealArithmetic/NumberField/ModuleHeight.lean, line 141](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/ModuleHeight.lean#L141).
- `NumberField.ArchimedeanNorms.height_pos` (theorem), declared in [DedekindIdealArithmetic/NumberField/ModuleHeight.lean, line 158](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/ModuleHeight.lean#L158).
- `NumberField.ArchimedeanNorms.normalizedLogHeight_eq` (theorem), declared in [DedekindIdealArithmetic/NumberField/ModuleHeight.lean, line 170](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/ModuleHeight.lean#L170).
- `NumberField.ArchimedeanNorms.height_tensor` (theorem), declared in [DedekindIdealArithmetic/NumberField/MetricTensorProduct.lean, line 203](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/MetricTensorProduct.lean#L203).
- `NumberField.ArchimedeanNorms.height_rescale` (theorem), declared in [DedekindIdealArithmetic/NumberField/MetricRescaling.lean, line 126](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/MetricRescaling.lean#L126).
- `NumberField.ArchimedeanNorms.height_comap` (theorem), declared in [DedekindIdealArithmetic/NumberField/MetricTransport.lean, line 119](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/MetricTransport.lean#L119).
- `NumberField.ArchimedeanNorms.height_eq_rationalFrame` (theorem), declared in [DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean, line 74](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean#L74).
- `NumberField.ArchimedeanNorms.normalizedLogHeight_eq_rationalFrame` (theorem), declared in [DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean, line 100](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean#L100).
- `NumberField.ArchimedeanNorms.height_eq_finitePlace` (theorem), declared in [DedekindIdealArithmetic/NumberField/FinitePlaceHeight.lean, line 72](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/FinitePlaceHeight.lean#L72).

Read from the source at commit [c7630759](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/tree/c76307595a1151abc42eacc9a815cb2d1bba6dc8), without running Lean.

## Sources

- [dedekind-ideal-arithmetic at c7630759: formalization.yaml](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/formalization.yaml)
- [Source of `NumberField.ArchimedeanNorms.height_eq` in DedekindIdealArithmetic/NumberField/ModuleHeight.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/ModuleHeight.lean#L141)
- [Source of `NumberField.ArchimedeanNorms.height_pos` in DedekindIdealArithmetic/NumberField/ModuleHeight.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/ModuleHeight.lean#L158)
- [Source of `NumberField.ArchimedeanNorms.normalizedLogHeight_eq` in DedekindIdealArithmetic/NumberField/ModuleHeight.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/ModuleHeight.lean#L170)
- [Source of `NumberField.ArchimedeanNorms.height_tensor` in DedekindIdealArithmetic/NumberField/MetricTensorProduct.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/MetricTensorProduct.lean#L203)
- [Source of `NumberField.ArchimedeanNorms.height_rescale` in DedekindIdealArithmetic/NumberField/MetricRescaling.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/MetricRescaling.lean#L126)
- [Source of `NumberField.ArchimedeanNorms.height_comap` in DedekindIdealArithmetic/NumberField/MetricTransport.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/MetricTransport.lean#L119)
- [Source of `NumberField.ArchimedeanNorms.height_eq_rationalFrame` in DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean#L74)
- [Source of `NumberField.ArchimedeanNorms.normalizedLogHeight_eq_rationalFrame` in DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/RationalFrameHeight.lean#L100)
- [Source of `NumberField.ArchimedeanNorms.height_eq_finitePlace` in DedekindIdealArithmetic/NumberField/FinitePlaceHeight.lean](https://github.com/FormalFrontier/dedekind-ideal-arithmetic/blob/c76307595a1151abc42eacc9a815cb2d1bba6dc8/DedekindIdealArithmetic/NumberField/FinitePlaceHeight.lean#L72)
