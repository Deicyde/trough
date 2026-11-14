---
declaration: module
origin: cited
lean: OperatorGeometricMean.operatorPowerMean_jointlyConcaveOn_pdSet, OperatorGeometricMean.operatorPowerMean_jointlyConvexOn_pdSet, OperatorGeometricMean.operatorPowerMean
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.OperatorGeometricMean

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.OperatorGeometricMean`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/OperatorGeometricMean.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/OperatorGeometricMean.lean): 3 declarations, 3 with a docstring, 2 listed as significant; 4 private, not shown.

**`OperatorGeometricMean.operatorPowerMean`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/OperatorGeometricMean.lean#L24).

> The operator `(α, β)`-power mean, realized as a generalized perspective.

```lean
noncomputable def operatorPowerMean (α β : ℝ) (A B : L ℋ) : L ℋ
```

**`OperatorGeometricMean.operatorPowerMean_jointlyConcaveOn_pdSet`**, a theorem, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/OperatorGeometricMean.lean#L55). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Theorem 1.1, concave range: the operator `(α, β)`-power mean is jointly concave on
> strictly positive operators for `0 ≤ α, β ≤ 1`.

```lean
theorem operatorPowerMean_jointlyConcaveOn_pdSet
    {α β : ℝ}
    (hα : α ∈ Set.Icc (0 : ℝ) 1)
    (hβ : β ∈ Set.Icc (0 : ℝ) 1) :
    JointlyConcaveOn (pdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ))
      (operatorPowerMean (ℋ := ℋ) α β)
```

**`OperatorGeometricMean.operatorPowerMean_jointlyConvexOn_pdSet`**, a theorem, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/OperatorGeometricMean.lean#L89). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Theorem 1.1, convex range: the operator `(α, β)`-power mean is jointly convex on
> strictly positive operators for `1 ≤ α ≤ 2` and `0 ≤ β ≤ 1`.

```lean
theorem operatorPowerMean_jointlyConvexOn_pdSet
    {α β : ℝ}
    (hα : α ∈ Set.Icc (1 : ℝ) 2)
    (hβ : β ∈ Set.Icc (0 : ℝ) 1) :
    JointlyConvexOn (pdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ))
      (operatorPowerMean (ℋ := ℋ) α β)
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.GeneralizedPerspectiveFunction](traceinequality-generalizedperspectivefunction.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/OperatorGeometricMean.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/OperatorGeometricMean.lean)
