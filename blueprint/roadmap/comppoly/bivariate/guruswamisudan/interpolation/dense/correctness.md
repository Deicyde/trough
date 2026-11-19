---
catalog: module
lean: CompPoly.GuruswamiSudan.normalizeVector?_some_data, CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis_weightedDegree_le, CompPoly.GuruswamiSudan.interpolationPolynomial_weightedDegree_le, CompPoly.GuruswamiSudan.isHomogeneousSolution_map_div, CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis_satisfies_of_solution, CompPoly.GuruswamiSudan.interpolationPolynomial_satisfies_of_solution, CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_getD_of_lt, CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_size, CompPoly.GuruswamiSudan.cbivariate_ne_zero_exists_coeff_ne_zero, CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_nonzero_of_complete, CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis_eq_of_complete, CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_solution_of_satisfies, CompPoly.GuruswamiSudan.normalizeVector?_some_of_nonzero, CompPoly.GuruswamiSudan.weightedDegreeBasis_sound, CompPoly.GuruswamiSudan.denseInterpolateWithBasis_sound, CompPoly.GuruswamiSudan.denseInterpolateWithBasis_complete, CompPoly.GuruswamiSudan.denseInterpolateWithBasisAndKernel_sound_of_bounded_basis, CompPoly.GuruswamiSudan.denseInterpolateWithWeightedDegreeBasis_sound, CompPoly.GuruswamiSudan.denseInterpolate_sound, CompPoly.GuruswamiSudan.denseInterpolateWithBasis_exists_of_dimension_slack, CompPoly.GuruswamiSudan.denseInterpolate_exists_of_dimension_slack, CompPoly.GuruswamiSudan.weightedDegreeBasis_complete_of_messageDegree_gt_one, CompPoly.GuruswamiSudan.denseInterpolate_complete_of_messageDegree_gt_one, CompPoly.GuruswamiSudan.denseInterpContext, CompPoly.GuruswamiSudan.denseInterpContext_correct, CompPoly.GuruswamiSudan.denseInterpContext_complete
statement: formalized
proof: formalized
---

# Dense Guruswami-Sudan Interpolation Correctness

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.Dense.Correctness`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean), by Valerii Huhnin.

> Correctness contracts for the dense interpolation path and its constructive
> low-message branch.

`CompPoly.GuruswamiSudan.normalizeVector?_some_data` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L84))

```lean
theorem normalizeVector?_some_data {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {v w : Array F} (h : normalizeVector? v = some w) :
    ∃ pivot, pivot < v.size ∧ v.getD pivot 0 ≠ 0 ∧
      w = v.map (fun x ↦ x / v.getD pivot 0) ∧
      w.size = v.size ∧ w.getD pivot 0 = 1
```

`CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis_weightedDegree_le` (theorem, [line 488](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L488))

```lean
theorem interpolationPolynomialOnBasis_weightedDegree_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (basis : Array CBivariate.Monomial) (params : GSInterpParams) (coeffs : Array F)
    (hbound : ∀ monomial, monomial ∈ basis.toList →
      1 * monomial.xDegree + yWeight params * monomial.yDegree ≤
        params.weightedDegreeBound) :
    CBivariate.natWeightedDegree (interpolationPolynomialOnBasis basis coeffs)
      1 (yWeight params) ≤ params.weightedDegreeBound
```

`CompPoly.GuruswamiSudan.interpolationPolynomial_weightedDegree_le` (theorem, [line 500](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L500))

```lean
theorem interpolationPolynomial_weightedDegree_le {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (params : GSInterpParams) (coeffs : Array F) :
    CBivariate.natWeightedDegree (interpolationPolynomial params coeffs)
      1 (yWeight params) ≤ params.weightedDegreeBound
```

`CompPoly.GuruswamiSudan.isHomogeneousSolution_map_div` (theorem, [line 539](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L539))

```lean
theorem isHomogeneousSolution_map_div {F : Type*} [Field F]
    {M : DenseMatrix F} {v : Array F} (a : F)
    (hsol : DenseMatrix.IsHomogeneousSolution M v) :
    DenseMatrix.IsHomogeneousSolution M (v.map fun x ↦ x / a)
```

`CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis_satisfies_of_solution` (theorem, [line 548](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L548))

```lean
theorem interpolationPolynomialOnBasis_satisfies_of_solution {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {basis : Array CBivariate.Monomial}
    {points : Array (F × F)} {params : GSInterpParams} {coeffs : Array F}
    (hsol :
      DenseMatrix.IsHomogeneousSolution (interpolationMatrixOnBasis basis points params) coeffs) :
    CBivariate.SatisfiesMultiplicityConstraints
      (interpolationPolynomialOnBasis basis coeffs) points params.multiplicity
```

`CompPoly.GuruswamiSudan.interpolationPolynomial_satisfies_of_solution` (theorem, [line 573](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L573))

```lean
theorem interpolationPolynomial_satisfies_of_solution {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (F × F)} {params : GSInterpParams} {coeffs : Array F}
    (hsol : DenseMatrix.IsHomogeneousSolution (interpolationMatrix points params) coeffs) :
    CBivariate.SatisfiesMultiplicityConstraints
      (interpolationPolynomial params coeffs) points params.multiplicity
```

`CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_getD_of_lt` (theorem, [line 582](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L582))

```lean
theorem interpolationCoefficientVectorOnBasis_getD_of_lt {F : Type*} [Zero F]
    (basis : Array CBivariate.Monomial) (Q : CBivariate F) {k : Nat}
    (hk : k < basis.size) :
    (interpolationCoefficientVectorOnBasis basis Q).getD k 0 =
      CBivariate.coeff Q (basis.getD k ⟨0, 0⟩).xDegree
        (basis.getD k ⟨0, 0⟩).yDegree
```

`CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_size` (theorem, [line 591](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L591))

```lean
theorem interpolationCoefficientVectorOnBasis_size {F : Type*} [Zero F]
    (basis : Array CBivariate.Monomial) (Q : CBivariate F) :
    (interpolationCoefficientVectorOnBasis basis Q).size = basis.size
```

`CompPoly.GuruswamiSudan.cbivariate_ne_zero_exists_coeff_ne_zero` (theorem, [line 597](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L597))

```lean
theorem cbivariate_ne_zero_exists_coeff_ne_zero {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {Q : CBivariate F} (hQ : Q ≠ 0) :
    ∃ i j, CBivariate.coeff Q i j ≠ 0
```

`CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_nonzero_of_complete` (theorem, [line 609](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L609))

```lean
theorem interpolationCoefficientVectorOnBasis_nonzero_of_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {basis : Array CBivariate.Monomial} {Q : CBivariate F}
    (hQ : Q ≠ 0)
    (hcomplete : ∀ i j, CBivariate.coeff Q i j ≠ 0 →
      ({ xDegree := i, yDegree := j } : CBivariate.Monomial) ∈ basis.toList) :
    DenseMatrix.NonzeroVector (interpolationCoefficientVectorOnBasis basis Q)
```

`CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis_eq_of_complete` (theorem, [line 627](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L627))

```lean
theorem interpolationPolynomialOnBasis_eq_of_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {basis : Array CBivariate.Monomial} {Q : CBivariate F}
    (hnodup : basis.toList.Nodup)
    (hcomplete : ∀ i j, CBivariate.coeff Q i j ≠ 0 →
      ({ xDegree := i, yDegree := j } : CBivariate.Monomial) ∈ basis.toList) :
    interpolationPolynomialOnBasis basis
        (interpolationCoefficientVectorOnBasis basis Q) = Q
```

`CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis_solution_of_satisfies` (theorem, [line 671](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L671))

```lean
theorem interpolationCoefficientVectorOnBasis_solution_of_satisfies {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {basis : Array CBivariate.Monomial}
    {points : Array (F × F)} {params : GSInterpParams} {Q : CBivariate F}
    (hpoly :
      interpolationPolynomialOnBasis basis
        (interpolationCoefficientVectorOnBasis basis Q) = Q)
    (hconstraints :
      CBivariate.SatisfiesMultiplicityConstraints Q points params.multiplicity) :
    DenseMatrix.IsHomogeneousSolution (interpolationMatrixOnBasis basis points params)
      (interpolationCoefficientVectorOnBasis basis Q)
```

`CompPoly.GuruswamiSudan.normalizeVector?_some_of_nonzero` (theorem, [line 714](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L714))

```lean
theorem normalizeVector?_some_of_nonzero {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    {v : Array F} (hnz : DenseMatrix.NonzeroVector v) :
    ∃ norm, normalizeVector? v = some norm
```

`CompPoly.GuruswamiSudan.weightedDegreeBasis_sound` (theorem, [line 740](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L740))

> Soundness of the weighted-degree basis used by the public GS interpolation path.

```lean
theorem weightedDegreeBasis_sound (params : GSInterpParams) :
    ∀ monomial, monomial ∈ (interpolationMonomials params).toList →
      1 * monomial.xDegree + yWeight params * monomial.yDegree ≤
        params.weightedDegreeBound
```

`CompPoly.GuruswamiSudan.denseInterpolateWithBasis_sound` (theorem, [line 750](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L750))

> Soundness for one returned basis-parametric dense witness.

```lean
theorem denseInterpolateWithBasis_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {kernelContext : LinearKernelContext F}
    {basis : Array CBivariate.Monomial}
    {points : Array (Prod F F)} {params : GSInterpParams} {Q : CBivariate F}
    (hbasis : basis.toList.Nodup)
    (h : denseInterpolateWithBasisAndKernel kernelContext basis points params = some Q) :
    Q ≠ 0 ∧
      (∃ coeffs, Q = interpolationPolynomialOnBasis basis coeffs) ∧
        CBivariate.SatisfiesMultiplicityConstraints Q points params.multiplicity
```

`CompPoly.GuruswamiSudan.denseInterpolateWithBasis_complete` (theorem, [line 803](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L803))

> Basis-parametric dense completeness for finite homogeneous systems.

```lean
theorem denseInterpolateWithBasis_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {kernelContext : LinearKernelContext F}
    {basis : Array CBivariate.Monomial}
    {points : Array (Prod F F)} {params : GSInterpParams}
    (hExists : ∃ coeffs,
      DenseMatrix.VectorWidth (interpolationMatrixOnBasis basis points params) coeffs ∧
        DenseMatrix.IsHomogeneousSolution (interpolationMatrixOnBasis basis points params)
          coeffs ∧
          DenseMatrix.NonzeroVector coeffs) :
    ∃ Q, denseInterpolateWithBasisAndKernel kernelContext basis points params = some Q
```

`CompPoly.GuruswamiSudan.denseInterpolateWithBasisAndKernel_sound_of_bounded_basis` (theorem, [line 838](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L838))

> Basis-parametric dense soundness specialized to a bounded basis.

```lean
theorem denseInterpolateWithBasisAndKernel_sound_of_bounded_basis {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {kernelContext : LinearKernelContext F}
    {basis : Array CBivariate.Monomial}
    {points : Array (Prod F F)} {params : GSInterpParams} {Q : CBivariate F}
    (hbasis : basis.toList.Nodup)
    (hbound : ∀ monomial, monomial ∈ basis.toList →
      1 * monomial.xDegree + yWeight params * monomial.yDegree ≤
        params.weightedDegreeBound)
    (h : denseInterpolateWithBasisAndKernel kernelContext basis points params = some Q) :
    ValidInterpolationWitness points params Q
```

`CompPoly.GuruswamiSudan.denseInterpolateWithWeightedDegreeBasis_sound` (theorem, [line 859](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L859))

> Dense weighted-degree-basis soundness for the positive-message branch.

```lean
theorem denseInterpolateWithWeightedDegreeBasis_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {kernelContext : LinearKernelContext F}
    {points : Array (Prod F F)} {params : GSInterpParams} {Q : CBivariate F}
    (h : denseInterpolateWithBasisAndKernel kernelContext
      (interpolationMonomials params) points params = some Q) :
    ValidInterpolationWitness points params Q
```

`CompPoly.GuruswamiSudan.denseInterpolate_sound` (theorem, [line 874](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L874))

> Soundness for one returned public interpolation witness.

```lean
theorem denseInterpolate_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {kernelContext : LinearKernelContext F}
    {points : Array (Prod F F)} {params : GSInterpParams} {Q : CBivariate F}
    (h : denseInterpolateWithKernel kernelContext points params = some Q) :
    ValidInterpolationWitness points params Q
```

`CompPoly.GuruswamiSudan.denseInterpolateWithBasis_exists_of_dimension_slack` (theorem, [line 892](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L892))

> If a basis-parametric dense interpolation matrix has more columns than rows,
> the dense solver finds a nonzero homogeneous witness.

```lean
theorem denseInterpolateWithBasis_exists_of_dimension_slack {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (basis : Array CBivariate.Monomial)
    (points : Array (F × F)) (params : GSInterpParams)
    (hSlack : HasInterpolationDimensionSlackOnBasis basis points params) :
    ∃ Q, denseInterpolateWithBasisAndKernel (denseLinearKernelContext F)
      basis points params = some Q
```

`CompPoly.GuruswamiSudan.denseInterpolate_exists_of_dimension_slack` (theorem, [line 918](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L918))

> Dimension slack for the public interpolation basis gives an interpolation
> witness. The low-message branch is constructive; otherwise the witness comes
> from the dense matrix.

```lean
theorem denseInterpolate_exists_of_dimension_slack {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (points : Array (F × F)) (params : GSInterpParams)
    (hSlack : HasInterpolationDimensionSlack points params) :
    ∃ Q, denseInterpolate points params = some Q
```

`CompPoly.GuruswamiSudan.weightedDegreeBasis_complete_of_messageDegree_gt_one` (theorem, [line 933](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L933))

> When `messageDegree > 1`, the weighted-degree basis is complete for the
> semantic weighted-degree predicate.

```lean
theorem weightedDegreeBasis_complete_of_messageDegree_gt_one {F : Type*}
    [Zero F] [BEq F] [LawfulBEq F]
    {params : GSInterpParams} (hHigh : ¬ params.messageDegree ≤ 1)
    {Q : CBivariate F}
    (hdeg :
      CBivariate.natWeightedDegree Q 1 (yWeight params) ≤
        params.weightedDegreeBound) :
    ∀ i j, CBivariate.coeff Q i j ≠ 0 →
      ({ xDegree := i, yDegree := j } : CBivariate.Monomial) ∈
        (interpolationMonomials params).toList
```

`CompPoly.GuruswamiSudan.denseInterpolate_complete_of_messageDegree_gt_one` (theorem, [line 977](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L977))

> Dense interpolation completeness in the ordinary positive-`Y`-weight range.

```lean
theorem denseInterpolate_complete_of_messageDegree_gt_one {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    {points : Array (F × F)} {params : GSInterpParams}
    (hHigh : ¬ params.messageDegree ≤ 1) :
    (exists Q, ValidInterpolationWitness points params Q) →
      exists Q, denseInterpolate points params = some Q
```

`CompPoly.GuruswamiSudan.denseInterpContext` (definition, [line 1021](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L1021))

> The executable interpolation path packaged as a certified GS interpolation backend.

```lean
def denseInterpContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    [DecidableEq F] : GSInterpContext F
```

`CompPoly.GuruswamiSudan.denseInterpContext_correct` (theorem, [line 1036](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L1036))

> Executable interpolation backend soundness.

```lean
theorem denseInterpContext_correct (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    [DecidableEq F] :
    ∀ points params Q,
      (denseInterpContext F).interpolate points params = some Q →
        ValidInterpolationWitness points params Q
```

`CompPoly.GuruswamiSudan.denseInterpContext_complete` (theorem, [line 1044](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean#L1044))

> Executable interpolation backend completeness.

```lean
theorem denseInterpContext_complete (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    [DecidableEq F] :
    ∀ points params,
      DistinctXCoordinates points →
      (exists Q, ValidInterpolationWitness points params Q) →
        exists Q, (denseInterpContext F).interpolate points params = some Q
```

## Depends on

- [Dense Guruswami-Sudan Interpolation](algorithm.md)

## Proof depends on

- [Shared Guruswami-Sudan Interpolation Correctness](../correctness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Correctness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.Dense.Correctness.json)
