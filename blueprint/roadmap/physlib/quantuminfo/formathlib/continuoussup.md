---
declaration: module
origin: cited
lean: IsCompact.closure_continuous_sSup, IsCompact.closure_continuous_sInf, Bornology.IsBounded.continuous_sSup, Bornology.IsBounded.continuous_sInf, LinearMap.continuous_iSup, LinearMap.continuous_iInf, LinearMap.continuous_iSup', LinearMap.continuous_iInf'
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.ContinuousSup

The module `QuantumInfo.ForMathlib.ContinuousSup`, [QuantumInfo/ForMathlib/ContinuousSup.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean): 20 declarations, 11 with a docstring, 11 listed as significant.

**`IsCompact.sSup_image_eq_sSup_image_closure`**, a lemma, [line 21](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L21).

```lean
lemma sSup_image_eq_sSup_image_closure {f : β → α}
  (hS : IsCompact (closure S)) (hf : Continuous f) :
    sSup (f '' S) = sSup (f '' closure S)
```

**`IsCompact.sInf_image_eq_sInf_image_closure`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L38).

```lean
lemma sInf_image_eq_sInf_image_closure {f : β → α} (hS : IsCompact (closure S)) (hf : Continuous f) :
    sInf (f '' S) = sInf (f '' closure S)
```

**`IsCompact.closure_continuous_sSup`**, a theorem, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L44). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A version of `IsCompact.continuous_sSup` with a slightly weaker hypothesis on the set `K`,
> that its closure is compact (but the set itself need not be).

```lean
theorem closure_continuous_sSup (hS : IsCompact (closure S)) (hf : Continuous ↿f) :
    Continuous fun x ↦ sSup (f x '' S)
```

**`IsCompact.closure_continuous_sInf`**, a theorem, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L51). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A version of `IsCompact.continuous_sInf` with a slightly weaker hypothesis on the set `K`,
> that its closure is compact (but the set itself need not be).

```lean
theorem closure_continuous_sInf (hS : IsCompact (closure S)) (hf : Continuous ↿f) :
    Continuous fun x ↦ sInf (f x '' S)
```

**`IsCompact.continuous_iSup`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L55).

```lean
lemma continuous_iSup (hS : IsCompact (closure S)) (hf : Continuous ↿f) :
    Continuous fun x ↦ ⨆ y : S, f x y
```

**`IsCompact.continuous_iInf`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L60).

```lean
lemma continuous_iInf (hS : IsCompact (closure S)) (hf : Continuous ↿f) :
    Continuous fun x ↦ ⨅ y : S, f x y
```

**`Bornology.IsBounded.continuous_sSup`**, a theorem, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L71). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Similar to `IsCompact.continuous_sSup`, but taking a bounded set in the bornology instead
> of a compact set.

```lean
theorem continuous_sSup (hS : Bornology.IsBounded S) (hf : Continuous ↿f) :
    Continuous fun x ↦ sSup (f x '' S)
```

**`Bornology.IsBounded.continuous_sInf`**, a theorem, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L77). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Similar to `IsCompact.continuous_sInf`, but taking a bounded set in the bornology instead
> of a compact set.

```lean
theorem continuous_sInf (hS : Bornology.IsBounded S) (hf : Continuous ↿f) :
    Continuous fun x ↦ sInf (f x '' S)
```

**`Bornology.IsBounded.continuous_iSup`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L81).

```lean
lemma continuous_iSup (hS : Bornology.IsBounded S) (hf : Continuous ↿f) :
    Continuous fun x ↦ ⨆ y : S, f x y
```

**`Bornology.IsBounded.continuous_iInf`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L86).

```lean
lemma continuous_iInf (hS : Bornology.IsBounded S) (hf : Continuous ↿f) :
    Continuous fun x ↦ ⨅ y : S, f x y
```

**`LinearMap.continuous_iSup`**, a theorem, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L96). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For bilinear maps in suitably well-behaved spaces with `IsModuleTopology`, taking the supremum in one
> argument is still `Continuous`, by `Bornology.IsBounded.continuous_iSup`.

```lean
theorem continuous_iSup {E F 𝕜 : Type*}
  [CommRing 𝕜] [TopologicalSpace 𝕜] [IsTopologicalRing 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [OrderTopology 𝕜]
  [AddCommGroup E] [TopologicalSpace E] [Module 𝕜 E] [IsModuleTopology 𝕜 E]
  [AddCommGroup F] [Module 𝕜 F] [PseudoMetricSpace F] [ProperSpace F] [Module.Finite 𝕜 F] [IsModuleTopology 𝕜 F]
  (f : E →ₗ[𝕜] F →ₗ[𝕜] 𝕜) {S : Set F} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨆ y : S, f x y
```

**`LinearMap.continuous_iInf`**, a theorem, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L106). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For bilinear maps in suitably well-behaved spaces with `IsModuleTopology`, taking the infimum in one
> argument is still `Continuous`, by `Bornology.IsBounded.continuous_iInf`.

```lean
theorem continuous_iInf {E F 𝕜 : Type*}
  [CommRing 𝕜] [TopologicalSpace 𝕜] [IsTopologicalRing 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [OrderTopology 𝕜]
  [AddCommGroup E] [TopologicalSpace E] [Module 𝕜 E] [IsModuleTopology 𝕜 E]
  [AddCommGroup F] [Module 𝕜 F] [PseudoMetricSpace F] [ProperSpace F] [Module.Finite 𝕜 F] [IsModuleTopology 𝕜 F]
  (f : E →ₗ[𝕜] F →ₗ[𝕜] 𝕜) {S : Set F} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨅ y : S, f x y
```

**`LinearMap.continuous_iSup'`**, a theorem, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L116). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A specialization of `LinearMap.continuous_iSup` to finite dimensional spaces, in place
> of requiring a (non-instance) `IsModuleTopology`.

```lean
theorem continuous_iSup' {E F 𝕜 : Type*}
  [NontriviallyNormedField 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [OrderTopology 𝕜] [CompleteSpace 𝕜]
  [AddCommGroup E] [TopologicalSpace E] [IsTopologicalAddGroup E] [T2Space E]
  [Module 𝕜 E] [ContinuousSMul 𝕜 E] [FiniteDimensional 𝕜 E]
  [PseudoMetricSpace F] [ProperSpace F] [AddCommGroup F] [IsTopologicalAddGroup F] [T2Space F]
  [Module 𝕜 F] [ContinuousSMul 𝕜 F] [FiniteDimensional 𝕜 F]
  (f : E →ₗ[𝕜] F →ₗ[𝕜] 𝕜) {S : Set F} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨆ y : S, f x y
```

**`LinearMap.continuous_iInf'`**, a theorem, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L130). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A specialization of `LinearMap.continuous_iInf` to finite dimensional spaces, in place
> of requiring a (non-instance) `IsModuleTopology`.

```lean
theorem continuous_iInf' {E F 𝕜 : Type*}
  [NontriviallyNormedField 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [OrderTopology 𝕜] [CompleteSpace 𝕜]
  [AddCommGroup E] [TopologicalSpace E] [IsTopologicalAddGroup E] [T2Space E]
  [Module 𝕜 E] [ContinuousSMul 𝕜 E] [FiniteDimensional 𝕜 E]
  [PseudoMetricSpace F] [ProperSpace F] [AddCommGroup F] [IsTopologicalAddGroup F] [T2Space F]
  [Module 𝕜 F] [ContinuousSMul 𝕜 F] [FiniteDimensional 𝕜 F]
  (f : E →ₗ[𝕜] F →ₗ[𝕜] 𝕜) {S : Set F} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨅ y : S, f x y
```

**`LinearMap.BilinForm.continuous_iSup`**, a theorem, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L143). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Alias of `LinearMap.continuous_iSup' ` that takes `LinearMap.BilinForm`.

```lean
theorem BilinForm.continuous_iSup {𝕜 E : Type*}
  [RCLike 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [OrderTopology 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [ProperSpace E]
  (f : LinearMap.BilinForm 𝕜 E) {S : Set E} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨆ y : S, f x y
```

**`LinearMap.BilinForm.continuous_iInf`**, a theorem, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L151). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Alias of `LinearMap.continuous_iInf' ` that takes `LinearMap.BilinForm`.

```lean
theorem BilinForm.continuous_iInf {𝕜 E : Type*}
  [RCLike 𝕜] [ConditionallyCompleteLinearOrder 𝕜] [OrderTopology 𝕜]
  [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E] [ProperSpace E]
  (f : LinearMap.BilinForm 𝕜 E) {S : Set E} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨅ y : S, f x y
```

**`ContinuousLinearMap.continuous_iSup`**, a theorem, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L168). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A specialization of `Bornology.IsBounded.continuous_iSup_bilinear` to `ContinuousLinearMap`.

```lean
theorem continuous_iSup
  (f : F →SL[σ₁₂] E →L[𝕜] G) {S : Set E} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨆ y : S, f x y
```

**`ContinuousLinearMap.continuous_iInf`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L173).

```lean
lemma continuous_iInf
  (f : F →SL[σ₁₂] E →L[𝕜] G) {S : Set E} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨅ y : S, f x y
```

**`LinearMap.BilinForm.continuous_iSup_fst`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L181).

```lean
lemma LinearMap.BilinForm.continuous_iSup_fst
  {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  (f : LinearMap.BilinForm ℝ E) {S : Set E} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨆ y : S, f y x
```

**`LinearMap.BilinForm.continuous_iInf_fst`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean#L260).

```lean
lemma LinearMap.BilinForm.continuous_iInf_fst
  {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  (f : LinearMap.BilinForm ℝ E) {S : Set E} (hS : Bornology.IsBounded S) :
    Continuous fun x ↦ ⨅ y : S, f y x
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/ContinuousSup.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ContinuousSup.lean)
