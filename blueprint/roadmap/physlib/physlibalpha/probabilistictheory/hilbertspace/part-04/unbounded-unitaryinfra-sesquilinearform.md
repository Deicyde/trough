---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional, ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.measure, ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.regular, ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.integral, ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.integral_eq_zero_of_support_disjoint, ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.measure_ext, ProbabilisticTheory.QuantumMechanics.pullbackPairing, ProbabilisticTheory.QuantumMechanics.transpose_mapRange_pullback
statement: formalized
proof: formalized
---

# The spectral forms of a bounded normal operator

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.UnitaryInfra.SesquilinearForm`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean): 87 declarations, 36 with a docstring.

> Complex measures `⟪y, E(·) x⟫` of a bounded normal operator and their sesquilinear forms.

## i. Overview

> For a bounded normal operator `U` and vectors `x`, `y`, the functional `f ↦ ⟪x, f(U) y⟫` on
> continuous functions on the spectrum is given, by the Riesz–Markov–Kakutani theorem and
> polarization, by a complex measure. Evaluating these measures on a measurable set `S` gives a
> bounded sesquilinear form for each such set.

## ii. Key results

> - `CompactPositiveFunctional` : a positive functional on compactly supported continuous functions,
>   with its Riesz measure.
> - `cfcScalarMeasure` : the measure representing `f ↦ ⟪x, f(U) x⟫`.
> - `polarizedCfcScalarMeasure` : the complex measure representing `f ↦ ⟪y, f(U) x⟫`.
> - `polarizedCfcScalarMeasure_complexIntegral_eq_inner` : integrating a real continuous `f` against
>   the polarized measure gives `⟪y, f(U) x⟫`.
> - `polarizedCfcScalarMeasure_smul_left`, `polarizedCfcScalarMeasure_smul_right` : the polarized
>   measure is sesquilinear in the two vectors.
> - `polarizedCfcScalarMeasure_norm_le_mul` : the polarized measure of a set is bounded by
>   `2 ‖x‖ ‖y‖`.
> - `cfcSesquilinearForm` : the bounded sesquilinear form of a measurable set.

## iv. References

> * None.

**`ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional`**, a structure, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L75).

> A positive scalar functional on a compact spectrum.

```lean
structure CompactPositiveFunctional where
  /-- The underlying positive linear functional. -/
  functional : CompactlySupportedContinuousMap X ℝ →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.measure`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L84).

> The regular Borel measure represented by the scalar functional.

```lean
noncomputable def measure : Measure X
```

**`ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.regular`**, an instance, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L86).

```lean
instance regular : (Λ.measure).Regular
```

**`ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.integral`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L90).

```lean
lemma integral (f : CompactlySupportedContinuousMap X ℝ) :
    ∫ x, f x ∂Λ.measure = Λ.functional f
```

**`ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.integral_eq_zero_of_support_disjoint`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L94).

```lean
lemma integral_eq_zero_of_support_disjoint {f : CompactlySupportedContinuousMap X ℝ}
    {S : Set X} (hS_meas : MeasurableSet S) (hS : ∀ x ∈ S, f x = 0) :
    ∫ x, f x ∂(Λ.measure.restrict S) = 0
```

**`ProbabilisticTheory.QuantumMechanics.CompactPositiveFunctional.measure_ext`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L101).

```lean
lemma measure_ext {Λ₁ Λ₂ : CompactPositiveFunctional (X := X)}
    (hΛ : ∀ f, Λ₁.functional f = Λ₂.functional f) :
    Λ₁.measure = Λ₂.measure
```

## A. Integrals along the range map

**`ProbabilisticTheory.QuantumMechanics.pullbackPairing`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L121).

> Pull a bilinear pairing back along a continuous linear map in its second argument.

```lean
def pullbackPairing (L : F →L[ℝ] G) (B : E →L[ℝ] G →L[ℝ] K) :
    E →L[ℝ] F →L[ℝ] K
```

**`ProbabilisticTheory.QuantumMechanics.transpose_mapRange_pullback`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L126).

```lean
lemma transpose_mapRange_pullback (μ : VectorMeasure X F) (L : F →L[ℝ] G)
    (B : E →L[ℝ] G →L[ℝ] K) :
    (μ.mapRange L.toAddMonoidHom L.continuous).transpose B =
      μ.transpose (pullbackPairing L B)
```

**`ProbabilisticTheory.QuantumMechanics.integral_mapRange_pullback`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L135).

```lean
lemma integral_mapRange_pullback (μ : VectorMeasure X F) (L : F →L[ℝ] G)
    (B : E →L[ℝ] G →L[ℝ] K) (f : X → E)
    (hfμ : μ.Integrable f) (hfL : (μ.mapRange L.toAddMonoidHom L.continuous).Integrable f) :
    ∫ᵛ x, f x ∂[B; μ.mapRange L.toAddMonoidHom L.continuous] =
      ∫ᵛ x, f x ∂[pullbackPairing L B; μ]
```

## B. Complexification of finite signed measures

**`ProbabilisticTheory.QuantumMechanics.complexSignedPairing`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L157).

> The pairing used for a complex-valued function against a real signed measure.

```lean
def complexSignedPairing : ℂ →L[ℝ] ℝ →L[ℝ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.postcomposePairing`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L162).

> Postcompose a pairing `E →L[ℝ] F →L[ℝ] G` with a continuous linear map `G →L[ℝ] K`, giving a
> pairing `E →L[ℝ] F →L[ℝ] K`.

```lean
def postcomposePairing {E F G K : Type*}
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F]
    [NormedAddCommGroup G] [NormedSpace ℝ G]
    [NormedAddCommGroup K] [NormedSpace ℝ K]
    (C : G →L[ℝ] K) (B : E →L[ℝ] F →L[ℝ] G) :
    E →L[ℝ] F →L[ℝ] K
```

**`ProbabilisticTheory.QuantumMechanics.transpose_postcomposePairing_apply`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L180).

```lean
lemma transpose_postcomposePairing_apply {X E F G K : Type*} [MeasurableSpace X]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F]
    [NormedAddCommGroup G] [NormedSpace ℝ G]
    [NormedAddCommGroup K] [NormedSpace ℝ K]
    (μ : VectorMeasure X F) (C : G →L[ℝ] K) (B : E →L[ℝ] F →L[ℝ] G)
    (s : Set X) (x : E) :
    μ.transpose (postcomposePairing C B) s x = C (μ.transpose B s x)
```

**`ProbabilisticTheory.QuantumMechanics.setToL1S_compContinuousLinearMap`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L195).

```lean
lemma setToL1S_compContinuousLinearMap {X E F G : Type*} [MeasurableSpace X]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F]
    [NormedAddCommGroup G] [NormedSpace ℝ G]
    (T : Set X → E →L[ℝ] F) (T' : Set X → E →L[ℝ] G) (C : F →L[ℝ] G)
    {μ : Measure X}
    (h : ∀ s, MeasurableSet s → ∀ x, T' s x = C (T s x))
    (f : X →₁ₛ[μ] E) :
    L1.SimpleFunc.setToL1S T' f = C (L1.SimpleFunc.setToL1S T f)
```

**`ProbabilisticTheory.QuantumMechanics.setToL1_compContinuousLinearMap`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L212).

```lean
lemma setToL1_compContinuousLinearMap {X E F G : Type*} [MeasurableSpace X]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
    [NormedAddCommGroup G] [NormedSpace ℝ G] [CompleteSpace G]
    {μ : Measure X} {T : Set X → E →L[ℝ] F} {T' : Set X → E →L[ℝ] G}
    {C₀ C₁ : ℝ} (hT : DominatedFinMeasAdditive μ T C₀)
    (hT' : DominatedFinMeasAdditive μ T' C₁) (C : F →L[ℝ] G)
    (h : ∀ s, MeasurableSet s → ∀ x, T' s x = C (T s x))
    (f : X →₁[μ] E) :
    L1.setToL1 hT' f = C (L1.setToL1 hT f)
```

**`ProbabilisticTheory.QuantumMechanics.setToFun_compContinuousLinearMap`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L230).

```lean
lemma setToFun_compContinuousLinearMap {X E F G : Type*} [MeasurableSpace X]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F]
    [NormedAddCommGroup G] [NormedSpace ℝ G] [CompleteSpace G]
    {μ : Measure X} {T : Set X → E →L[ℝ] F} {T' : Set X → E →L[ℝ] G}
    {C₀ C₁ : ℝ} (hT : DominatedFinMeasAdditive μ T C₀)
    (hT' : DominatedFinMeasAdditive μ T' C₁) (C : F →L[ℝ] G)
    (h : ∀ s, MeasurableSet s → ∀ x, T' s x = C (T s x))
    {f : X → E} (hf : Integrable f μ) :
    MeasureTheory.setToFun μ T' hT' f = C (MeasureTheory.setToFun μ T hT f)
```

**`ProbabilisticTheory.QuantumMechanics.integral_postcomposePairing`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L243).

```lean
lemma integral_postcomposePairing {X E F G K : Type*} [MeasurableSpace X]
    [NormedAddCommGroup E] [NormedSpace ℝ E]
    [NormedAddCommGroup F] [NormedSpace ℝ F]
    [NormedAddCommGroup G] [NormedSpace ℝ G] [CompleteSpace G]
    [NormedAddCommGroup K] [NormedSpace ℝ K] [CompleteSpace K]
    (μ : VectorMeasure X F) (B : E →L[ℝ] F →L[ℝ] G) (C : G →L[ℝ] K)
    (f : X → E) (hf : μ.Integrable f) :
    C (∫ᵛ x, f x ∂[B; μ]) =
      ∫ᵛ x, f x ∂[postcomposePairing C B; μ]
```

**`ProbabilisticTheory.QuantumMechanics.imaginaryOfRealCLM`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L265).

> Multiplication by `I`, followed by the canonical embedding of a real signed measure into a
> complex vector measure.

```lean
def imaginaryOfRealCLM : ℝ →L[ℝ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.imaginaryOfRealCLM_apply`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L269).

```lean
lemma imaginaryOfRealCLM_apply (r : ℝ) : imaginaryOfRealCLM r = Complex.I * r
```

**`ProbabilisticTheory.QuantumMechanics.signedMeasure_toComplexMeasure_eq_add_mapRange`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L272).

```lean
lemma signedMeasure_toComplexMeasure_eq_add_mapRange
    {Y : Type*} [MeasurableSpace Y] (s t : SignedMeasure Y) :
    s.toComplexMeasure t =
      s.mapRange Complex.ofRealCLM.toAddMonoidHom Complex.ofRealCLM.continuous +
        t.mapRange imaginaryOfRealCLM.toAddMonoidHom imaginaryOfRealCLM.continuous
```

**`ProbabilisticTheory.QuantumMechanics.integral_toComplexMeasure_eq_add_mapRange`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L286).

```lean
lemma integral_toComplexMeasure_eq_add_mapRange
    {X : Type*} [MeasurableSpace X] (s t : SignedMeasure X) (f : X → ℂ)
    (hs : (s.mapRange Complex.ofRealCLM.toAddMonoidHom
      Complex.ofRealCLM.continuous).Integrable f)
    (ht : (t.mapRange imaginaryOfRealCLM.toAddMonoidHom
      imaginaryOfRealCLM.continuous).Integrable f) :
    ∫ᵛ x, f x ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ); s.toComplexMeasure t] =
      (∫ᵛ x, f x ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
        s.mapRange Complex.ofRealCLM.toAddMonoidHom Complex.ofRealCLM.continuous]) +
      ∫ᵛ x, f x ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
        t.mapRange imaginaryOfRealCLM.toAddMonoidHom imaginaryOfRealCLM.continuous]
```

**`ProbabilisticTheory.QuantumMechanics.pullbackPairing_ofReal_lsmul`**, a lemma, [line 300](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L300).

```lean
lemma pullbackPairing_ofReal_lsmul :
    pullbackPairing Complex.ofRealCLM
      (ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ)) = complexSignedPairing
```

**`ProbabilisticTheory.QuantumMechanics.integral_mapRange_ofReal_signedMeasure`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L307).

```lean
lemma integral_mapRange_ofReal_signedMeasure
    {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (f : X → ℂ) (hf : Integrable f μ) :
    ∫ᵛ x, f x ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      μ.toSignedMeasure.mapRange Complex.ofRealCLM.toAddMonoidHom
        Complex.ofRealCLM.continuous] =
      ∫ᵛ x, f x ∂<•μ.toSignedMeasure
```

**`ProbabilisticTheory.QuantumMechanics.integrable_mapRange_toSignedMeasure`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L343).

```lean
lemma integrable_mapRange_toSignedMeasure
    {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (L : ℝ →L[ℝ] ℂ) (hL : ∀ r : ℝ, ‖L r‖ = ‖r‖)
    (f : X → ℂ) (hf : Integrable f μ) :
    (μ.toSignedMeasure.mapRange L.toAddMonoidHom L.continuous).Integrable f
```

**`ProbabilisticTheory.QuantumMechanics.integrable_mapRange_ofReal_signedMeasure`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L368).

```lean
lemma integrable_mapRange_ofReal_signedMeasure
    {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (f : X → ℂ) (hf : Integrable f μ) :
    (μ.toSignedMeasure.mapRange Complex.ofRealCLM.toAddMonoidHom
      Complex.ofRealCLM.continuous).Integrable f
```

**`ProbabilisticTheory.QuantumMechanics.integrable_mapRange_imaginaryOfReal_signedMeasure`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L377).

```lean
lemma integrable_mapRange_imaginaryOfReal_signedMeasure
    {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (f : X → ℂ) (hf : Integrable f μ) :
    (μ.toSignedMeasure.mapRange imaginaryOfRealCLM.toAddMonoidHom
      imaginaryOfRealCLM.continuous).Integrable f
```

**`ProbabilisticTheory.QuantumMechanics.mapRange_sub_toSignedMeasure`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L387).

```lean
lemma mapRange_sub_toSignedMeasure
    {X : Type*} [MeasurableSpace X] (μ ν : Measure X)
    [IsFiniteMeasure μ] [IsFiniteMeasure ν] (L : ℝ →L[ℝ] ℂ) :
    (μ.toSignedMeasure - ν.toSignedMeasure).mapRange L.toAddMonoidHom L.continuous =
      μ.toSignedMeasure.mapRange L.toAddMonoidHom L.continuous -
        ν.toSignedMeasure.mapRange L.toAddMonoidHom L.continuous
```

**`ProbabilisticTheory.QuantumMechanics.integral_mapRange_ofReal_signedDifference`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L400).

```lean
lemma integral_mapRange_ofReal_signedDifference
    {X : Type*} [MeasurableSpace X]
    (μ ν : Measure X) [IsFiniteMeasure μ] [IsFiniteMeasure ν]
    (c : ℝ) (f : X → ℂ) (hμ : Integrable f μ) (hν : Integrable f ν) :
    ∫ᵛ x, f x ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      (c • (μ.toSignedMeasure - ν.toSignedMeasure)).mapRange
        Complex.ofRealCLM.toAddMonoidHom Complex.ofRealCLM.continuous] =
      c • ((∫ x, f x ∂μ) - ∫ x, f x ∂ν)
```

**`ProbabilisticTheory.QuantumMechanics.imaginaryMulCLM`**, a def, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L419).

> Multiplication by `I`, as a continuous ℝ-linear map on `ℂ`.

```lean
def imaginaryMulCLM : ℂ →L[ℝ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.imaginaryMulCLM_apply`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L423).

```lean
lemma imaginaryMulCLM_apply (z : ℂ) : imaginaryMulCLM z = Complex.I * z
```

**`ProbabilisticTheory.QuantumMechanics.imaginarySignedPairing`**, a def, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L427).

> The `ℂ →L[ℝ] ℝ →L[ℝ] ℂ` pairing post-composed with multiplication by `I`.

```lean
def imaginarySignedPairing : ℂ →L[ℝ] ℝ →L[ℝ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.pullbackPairing_imaginaryOfReal_lsmul`**, a lemma, [line 430](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L430).

```lean
lemma pullbackPairing_imaginaryOfReal_lsmul :
    pullbackPairing imaginaryOfRealCLM
      (ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ)) = imaginarySignedPairing
```

**`ProbabilisticTheory.QuantumMechanics.integral_mapRange_imaginaryOfReal_signedMeasure`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L439).

```lean
lemma integral_mapRange_imaginaryOfReal_signedMeasure
    {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (f : X → ℂ) (hf : Integrable f μ) :
    ∫ᵛ x, f x ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      μ.toSignedMeasure.mapRange imaginaryOfRealCLM.toAddMonoidHom
        imaginaryOfRealCLM.continuous] =
      Complex.I * (∫ x, f x ∂μ)
```

**`ProbabilisticTheory.QuantumMechanics.integral_mapRange_imaginaryOfReal_signedDifference`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L479).

```lean
lemma integral_mapRange_imaginaryOfReal_signedDifference
    {X : Type*} [MeasurableSpace X]
    (μ ν : Measure X) [IsFiniteMeasure μ] [IsFiniteMeasure ν]
    (c : ℝ) (f : X → ℂ) (hμ : Integrable f μ) (hν : Integrable f ν) :
    ∫ᵛ x, f x ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      (c • (μ.toSignedMeasure - ν.toSignedMeasure)).mapRange
        imaginaryOfRealCLM.toAddMonoidHom imaginaryOfRealCLM.continuous] =
      c • (Complex.I * ((∫ x, f x ∂μ) - ∫ x, f x ∂ν))
```

## C. Finiteness of the polarized scalar measures

**`ProbabilisticTheory.QuantumMechanics.isFiniteMeasure_toComplexMeasure`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L501).

```lean
lemma isFiniteMeasure_toComplexMeasure
    {X : Type*} [MeasurableSpace X] (s t : MeasureTheory.SignedMeasure X)
    [IsFiniteMeasure s.variation] [IsFiniteMeasure t.variation] :
    IsFiniteMeasure (s.toComplexMeasure t).variation
```

## D. A general positive-contraction norm estimate

> This is a standalone fact about `H →L[ℂ] H` for any complex Hilbert space `H`, not specific to the
> continuous functional calculus of a fixed normal operator: it is Step 2 of the idempotency
> argument below, quantifying `0 ≤ A ≤ 1 ⟹ A ^ 2 ≤ A` into a norm bound.

**`ProbabilisticTheory.QuantumMechanics.norm_sq_le_inner_of_isPositive_of_le_one`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L534).

> **The positive-contraction norm estimate.** If `0 ≤ A ≤ 1` in the Loewner order on
> `H →L[ℂ] H`, then `‖A x‖ ^ 2 ≤ re ⟪x, A x⟫` for every `x`.  Proved from `A ^ 2 ≤ A`
> (`CStarAlgebra.pow_antitone`, using the `CStarAlgebra (H →L[ℂ] H)` instance) and self-adjointness
> of `A` to identify `⟪x, A ^ 2 x⟫` with `⟪A x, A x⟫ = ‖A x‖ ^ 2`.

```lean
lemma norm_sq_le_inner_of_isPositive_of_le_one {A : H →L[ℂ] H}
    (hA0 : 0 ≤ A) (hA1 : A ≤ 1) (x : H) :
    ‖A x‖ ^ 2 ≤ RCLike.re ⟪x, A x⟫_ℂ
```

## E. Positive scalar functionals from the continuous functional calculus

**`ProbabilisticTheory.QuantumMechanics.realToComplexContinuousMap`**, a def, [line 570](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L570).

> Regard a real-valued continuous function on the spectrum of a normal operator as a complex
> valued one.  Keeping this map explicit prevents the real/complex scalar changes in the Riesz
> construction from being hidden in coercions.

```lean
noncomputable def realToComplexContinuousMap
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    C(spectrum ℂ U, ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.realToComplexContinuousMap_apply`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L578).

```lean
lemma realToComplexContinuousMap_apply
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) (z : spectrum ℂ U) :
    realToComplexContinuousMap U f z = f z
```

**`ProbabilisticTheory.QuantumMechanics.realToComplexContinuousMap_add`**, a lemma, [line 584](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L584).

```lean
lemma realToComplexContinuousMap_add
    (f g : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    realToComplexContinuousMap U (f + g) =
      realToComplexContinuousMap U f + realToComplexContinuousMap U g
```

**`ProbabilisticTheory.QuantumMechanics.realToComplexContinuousMap_smul`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L592).

```lean
lemma realToComplexContinuousMap_smul (r : ℝ)
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    realToComplexContinuousMap U (r • f) =
      (r : ℂ) • realToComplexContinuousMap U f
```

**`ProbabilisticTheory.QuantumMechanics.cfcRealOperator`**, a def, [line 601](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L601).

> The operator obtained by applying the complex continuous functional calculus to a real test
> function.

```lean
noncomputable def cfcRealOperator
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.cfcRealOperator_isSelfAdjoint`**, a lemma, [line 605](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L605).

```lean
lemma cfcRealOperator_isSelfAdjoint
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    IsSelfAdjoint (cfcRealOperator U hU f)
```

**`ProbabilisticTheory.QuantumMechanics.cfcRealOperator_nonneg`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L617).

```lean
lemma cfcRealOperator_nonneg
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ)
    (hf : ∀ z, 0 ≤ f z) :
    ContinuousLinearMap.IsPositive (cfcRealOperator U hU f)
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarFunctional`**, a def, [line 638](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L638).

> The vector state of the continuous functional calculus, restricted to real test functions.
> The positivity proof is the square-root argument above; this is the exact input required by
> Riesz--Markov.

```lean
noncomputable def cfcScalarFunctional (x : H) :
    CompactPositiveFunctional (X := spectrum ℂ U)
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarFunctional_apply`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L656).

```lean
lemma cfcScalarFunctional_apply (x : H)
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    (cfcScalarFunctional (hU := hU) U x).functional f =
      RCLike.re ⟪x, cfcRealOperator U hU f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure`**, a def, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L663).

> The scalar spectral measure supplied by Riesz--Markov for the vector state at `x`.

```lean
noncomputable def cfcScalarMeasure (x : H) : Measure (spectrum ℂ U)
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_isFinite`**, an instance, [line 666](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L666).

```lean
instance cfcScalarMeasure_isFinite (x : H) : IsFiniteMeasure (cfcScalarMeasure U hU x)
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_integral`**, a lemma, [line 670](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L670).

```lean
lemma cfcScalarMeasure_integral (x : H)
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    ∫ z, f z ∂cfcScalarMeasure U hU x =
      RCLike.re ⟪x, cfcRealOperator U hU f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_integral_complex`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L676).

```lean
lemma cfcScalarMeasure_integral_complex (x : H)
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) :
    ((∫ z, f z ∂cfcScalarMeasure U hU x : ℝ) : ℂ) =
      ⟪cfcRealOperator U hU f x, x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcRealIntegral`**, a def, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L694).

> The integral of a real function against the polarized measure.

```lean
noncomputable def polarizedCfcRealIntegral
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) (x y : H) : ℂ
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcRealIntegral_eq_inner`**, a lemma, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L703).

```lean
lemma polarizedCfcRealIntegral_eq_inner
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) (x y : H) :
    polarizedCfcRealIntegral U hU f x y =
      ⟪y, cfcRealOperator U hU f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.VectorStateSpectralData`**, a structure, [line 727](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L727).

> The scalar half of the normal-operator spectral construction.  The operator-valued assembly
> below uses this data to build the actual weak-operator spectral measure.

```lean
structure VectorStateSpectralData where
  /-- The scalar measure attached to each vector `x`. -/
  measure : H → Measure (spectrum ℂ U)
  integral_identity : ∀ x f,
    ∫ z, f z ∂measure x = RCLike.re ⟪x, cfcRealOperator U hU f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cfcVectorStateSpectralData`**, a def, [line 734](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L734).

> The scalar spectral data of `U`'s continuous functional calculus.

```lean
noncomputable def cfcVectorStateSpectralData : VectorStateSpectralData U hU
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_parallelogram`**, a lemma, [line 738](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L738).

```lean
lemma cfcScalarMeasure_parallelogram (x y : H) :
    cfcScalarMeasure U hU (x + y) + cfcScalarMeasure U hU (x - y) =
      (cfcScalarMeasure U hU x + cfcScalarMeasure U hU x) +
        (cfcScalarMeasure U hU y + cfcScalarMeasure U hU y)
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_neg`**, a lemma, [line 768](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L768).

```lean
lemma cfcScalarMeasure_neg (x : H) :
    cfcScalarMeasure U hU (-x) = cfcScalarMeasure U hU x
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_I_smul`**, a lemma, [line 778](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L778).

```lean
lemma cfcScalarMeasure_I_smul (x : H) :
    cfcScalarMeasure U hU (Complex.I • x) = cfcScalarMeasure U hU x
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure`**, a def, [line 793](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L793).

> The complex measure `⟪y, E(·) x⟫`, obtained by polarizing the four measures `⟪v, E(·) v⟫`.

```lean
noncomputable def polarizedCfcScalarMeasure (x y : H) : ComplexMeasure (spectrum ℂ U)
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_isFiniteMeasure`**, a lemma, [line 801](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L801).

```lean
lemma polarizedCfcScalarMeasure_isFiniteMeasure (x y : H) :
    IsFiniteMeasure
      (polarizedCfcScalarMeasure (hU := hU) U x y).variation
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_complexIntegral`**, a lemma, [line 853](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L853).

```lean
lemma polarizedCfcScalarMeasure_complexIntegral
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) (x y : H) :
    ∫ᵛ z, (f z : ℂ) ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      polarizedCfcScalarMeasure (hU := hU) U x y] =
      polarizedCfcRealIntegral U hU f x y
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_complexIntegral_eq_inner`**, a lemma, [line 902](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L902).

```lean
lemma polarizedCfcScalarMeasure_complexIntegral_eq_inner
    (f : CompactlySupportedContinuousMap (spectrum ℂ U) ℝ) (x y : H) :
    ∫ᵛ z, (f z : ℂ) ∂[ContinuousLinearMap.lsmul ℝ ℂ (E := ℂ);
      polarizedCfcScalarMeasure (hU := hU) U x y] =
      ⟪y, cfcRealOperator U hU f x⟫_ℂ
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_apply`**, a lemma, [line 910](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L910).

```lean
lemma polarizedCfcScalarMeasure_apply {x y : H}
    {S : Set (spectrum ℂ U)} (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U x y S =
      ((1 / 4 : ℝ) *
          ((cfcScalarMeasure U hU (x + y)).real S -
            (cfcScalarMeasure U hU (x - y)).real S) : ℂ) +
        Complex.I * ((1 / 4 : ℝ) *
          ((cfcScalarMeasure U hU (x + Complex.I • y)).real S -
            (cfcScalarMeasure U hU (x - Complex.I • y)).real S) : ℂ)
```

## F. Sesquilinearity of the polarized measure

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_parallelogram`**, a lemma, [line 927](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L927).

> The real-valued version of the parallelogram law, at a fixed (not necessarily measurable)
> set `S`.  This is the algebraic engine behind the sesquilinearity proofs below.

```lean
lemma cfcScalarMeasure_real_parallelogram (a b : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU (a + b)).real S + (cfcScalarMeasure U hU (a - b)).real S =
      2 * (cfcScalarMeasure U hU a).real S + 2 * (cfcScalarMeasure U hU b).real S
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_neg`**, a lemma, [line 942](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L942).

```lean
lemma cfcScalarMeasure_real_neg (a : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU (-a)).real S = (cfcScalarMeasure U hU a).real S
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_I_smul`**, a lemma, [line 946](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L946).

```lean
lemma cfcScalarMeasure_real_I_smul (a : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU (Complex.I • a)).real S = (cfcScalarMeasure U hU a).real S
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_nonneg`**, a lemma, [line 950](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L950).

```lean
lemma cfcScalarMeasure_real_nonneg (a : H) (S : Set (spectrum ℂ U)) :
    0 ≤ (cfcScalarMeasure U hU a).real S
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_univ`**, a lemma, [line 955](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L955).

> The Riesz measure for the vector state at `x` has total mass `‖x‖ ^ 2`: the vector-state
> counterpart of `cfcHom hU 1 = 1`.

```lean
lemma cfcScalarMeasure_real_univ (x : H) :
    (cfcScalarMeasure U hU x).real Set.univ = ‖x‖ ^ 2
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_le_univ`**, a lemma, [line 977](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L977).

```lean
lemma cfcScalarMeasure_real_le_univ (a : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU a).real S ≤ ‖a‖ ^ 2
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_polar_symm`**, a lemma, [line 984](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L984).

> The real polarization `Q(a + b) - Q(a - b)` of the diagonal measures is symmetric in `a` and
> `b`.

```lean
lemma cfcScalarMeasure_real_polar_symm (a b : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU (a + b)).real S - (cfcScalarMeasure U hU (a - b)).real S =
      (cfcScalarMeasure U hU (b + a)).real S - (cfcScalarMeasure U hU (b - a)).real S
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_polar_add_left`**, a lemma, [line 994](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L994).

> First-argument additivity of the real polarization `Q(a+b) - Q(a-b)`, established by pure
> algebra from the parallelogram law (`cfcScalarMeasure_real_parallelogram`); no continuity is
> needed for this step, matching the classical Jordan--von Neumann polarization argument
> (`Mathlib.Analysis.InnerProductSpace.OfNorm`).

```lean
lemma cfcScalarMeasure_real_polar_add_left (x y z : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU (x + y + z)).real S - (cfcScalarMeasure U hU (x + y - z)).real S =
      ((cfcScalarMeasure U hU (x + z)).real S - (cfcScalarMeasure U hU (x - z)).real S) +
        ((cfcScalarMeasure U hU (y + z)).real S - (cfcScalarMeasure U hU (y - z)).real S)
```

**`ProbabilisticTheory.QuantumMechanics.cfcScalarMeasure_real_polar_add_right`**, a lemma, [line 1018](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1018).

> Second-argument additivity of the real polarization, obtained from first-argument additivity
> (`cfcScalarMeasure_real_polar_add_left`) via the symmetry `cfcScalarMeasure_real_polar_symm`.

```lean
lemma cfcScalarMeasure_real_polar_add_right (a b c : H) (S : Set (spectrum ℂ U)) :
    (cfcScalarMeasure U hU (a + (b + c))).real S -
        (cfcScalarMeasure U hU (a - (b + c))).real S =
      ((cfcScalarMeasure U hU (a + b)).real S - (cfcScalarMeasure U hU (a - b)).real S) +
        ((cfcScalarMeasure U hU (a + c)).real S - (cfcScalarMeasure U hU (a - c)).real S)
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_add_right`**, a lemma, [line 1038](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1038).

> Additivity of the polarized measure in its second (right) vector argument, for a fixed
> measurable set `S`.  This is the sesquilinearity step promised in the module docstring: it
> follows from the parallelogram law by pure algebra, with no continuity or Riesz-representation
> machinery required.

```lean
lemma polarizedCfcScalarMeasure_add_right (x y₁ y₂ : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U x (y₁ + y₂) S =
      polarizedCfcScalarMeasure (hU := hU) U x y₁ S +
        polarizedCfcScalarMeasure (hU := hU) U x y₂ S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_add_left`**, a lemma, [line 1062](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1062).

> Additivity of the polarized measure in its first (left) vector argument, for a fixed
> measurable set `S`.

```lean
lemma polarizedCfcScalarMeasure_add_left (x₁ x₂ y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U (x₁ + x₂) y S =
      polarizedCfcScalarMeasure (hU := hU) U x₁ y S +
        polarizedCfcScalarMeasure (hU := hU) U x₂ y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_I_smul_right`**, a lemma, [line 1084](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1084).

> Multiplying the second vector by `i` multiplies the polarized measure by `-i`.

```lean
lemma polarizedCfcScalarMeasure_I_smul_right (x y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U x (Complex.I • y) S =
      -Complex.I * polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_I_smul_left`**, a lemma, [line 1101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1101).

> Multiplying the first vector by `i` multiplies the polarized measure by `i`.

```lean
lemma polarizedCfcScalarMeasure_I_smul_left (x y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U (Complex.I • x) y S =
      Complex.I * polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_norm_le`**, a lemma, [line 1122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1122).

> A crude but sufficient bound on the polarized measure, from the parallelogram law and
> `cfcScalarMeasure_real_le_univ`.  This is enough to see `(x, y) ↦ polarizedCfcScalarMeasure U hU
> x y S` is jointly bounded, the input a Riesz-representation argument needs.

```lean
lemma polarizedCfcScalarMeasure_norm_le (x y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    ‖polarizedCfcScalarMeasure (hU := hU) U x y S‖ ≤ ‖x‖ ^ 2 + ‖y‖ ^ 2
```

**`ProbabilisticTheory.QuantumMechanics.real_linear_of_additive_bounded`**, a lemma, [line 1161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1161).

> An additive `ℝ → ℂ` function that is bounded on `[-1, 1]` is automatically `ℝ`-linear.  This
> packages the classical "Cauchy's functional equation" regularity argument (additive + locally
> bounded ⟹ continuous, then continuous additive between real topological vector spaces ⟹
> `ℝ`-linear via `map_real_smul`) that both real-scalar-homogeneity lemmas below reduce to.

```lean
lemma real_linear_of_additive_bounded {φ : ℝ → ℂ}
    (hadd : ∀ a b : ℝ, φ (a + b) = φ a + φ b)
    {C : ℝ} (hbound : ∀ t : ℝ, |t| ≤ 1 → ‖φ t‖ ≤ C) (r : ℝ) :
    φ r = (r : ℂ) * φ 1
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_real_smul_right`**, a lemma, [line 1208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1208).

> The polarized measure is real homogeneous in the second vector.

```lean
lemma polarizedCfcScalarMeasure_real_smul_right (x y : H) (r : ℝ) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U x (r • y) S =
      (r : ℂ) * polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_real_smul_left`**, a lemma, [line 1233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1233).

> Real-scalar homogeneity in the left (first) argument, the counterpart of
> `polarizedCfcScalarMeasure_real_smul_right` needed for conjugate-linearity in `x` (real scalars
> are self-conjugate, so the same statement serves both roles).

```lean
lemma polarizedCfcScalarMeasure_real_smul_left (x y : H) (r : ℝ) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U (r • x) y S =
      (r : ℂ) * polarizedCfcScalarMeasure (hU := hU) U x y S
```

## G. Polarization

**`ProbabilisticTheory.QuantumMechanics.inner_map_polarization_continuous`**, a lemma, [line 1261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1261).

> The standard complex polarization identity, exposed at the continuous-operator level for the
> assembly proof.  The scalar measures obtained above will be polarized with precisely these four
> diagonal terms.

```lean
lemma inner_map_polarization_continuous (A : H →L[ℂ] H) (x y : H) :
    ⟪A y, x⟫_ℂ =
      (⟪A (x + y), x + y⟫_ℂ - ⟪A (x - y), x - y⟫_ℂ +
          Complex.I * ⟪A (x + Complex.I • y), x + Complex.I • y⟫_ℂ -
        Complex.I * ⟪A (x - Complex.I • y), x - Complex.I • y⟫_ℂ) / 4
```

## H. Full complex sesquilinearity of the polarized measure

> Writing `c = c.re + c.im i`, homogeneity for real scalars and for `i` gives complex linearity in the
> first vector and conjugate linearity in the second.

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_smul_left`**, a lemma, [line 1274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1274).

> Full `ℂ`-linearity of the polarized measure in its first (left) argument.

```lean
lemma polarizedCfcScalarMeasure_smul_left (c : ℂ) (x y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U (c • x) y S =
      c * polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_smul_right`**, a lemma, [line 1291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1291).

> Full conjugate-`ℂ`-linearity of the polarized measure in its second (right) argument.

```lean
lemma polarizedCfcScalarMeasure_smul_right (c : ℂ) (x y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    polarizedCfcScalarMeasure (hU := hU) U x (c • y) S =
      (starRingEnd ℂ c) * polarizedCfcScalarMeasure (hU := hU) U x y S
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_zero_left`**, a lemma, [line 1311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1311).

```lean
lemma polarizedCfcScalarMeasure_zero_left (y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) : polarizedCfcScalarMeasure (hU := hU) U 0 y S = 0
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_zero_right`**, a lemma, [line 1316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1316).

```lean
lemma polarizedCfcScalarMeasure_zero_right (x : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) : polarizedCfcScalarMeasure (hU := hU) U x 0 S = 0
```

**`ProbabilisticTheory.QuantumMechanics.polarizedCfcScalarMeasure_norm_le_mul`**, a lemma, [line 1322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1322).

> The polarized measure is bounded by `‖x‖ ‖y‖`.

```lean
lemma polarizedCfcScalarMeasure_norm_le_mul (x y : H) {S : Set (spectrum ℂ U)}
    (hS : MeasurableSet S) :
    ‖polarizedCfcScalarMeasure (hU := hU) U x y S‖ ≤ 2 * ‖x‖ * ‖y‖
```

## I. Riesz representation of the polarized measure

**`ProbabilisticTheory.QuantumMechanics.cfcSesquilinearFormAux`**, a def, [line 1361](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1361).

> The algebraic (not-yet-continuous) sesquilinear form representing `S`, conjugate-linear in the
> first argument and linear in the second — the convention Mathlib's
> `InnerProductSpace.continuousLinearMapOfBilin` expects.

```lean
noncomputable def cfcSesquilinearFormAux (S : Set (spectrum ℂ U)) (hS : MeasurableSet S) :
    H →ₛₗ[starRingEnd ℂ] H →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cfcSesquilinearFormAux_apply`**, a lemma, [line 1376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1376).

```lean
lemma cfcSesquilinearFormAux_apply (S : Set (spectrum ℂ U)) (hS : MeasurableSet S) (x y : H) :
    cfcSesquilinearFormAux U hU S hS x y =
      starRingEnd ℂ (polarizedCfcScalarMeasure (hU := hU) U x y S)
```

**`ProbabilisticTheory.QuantumMechanics.cfcSesquilinearForm`**, a def, [line 1382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1382).

> The continuous sesquilinear form, in the shape `InnerProductSpace.continuousLinearMapOfBilin`
> consumes.

```lean
noncomputable def cfcSesquilinearForm (S : Set (spectrum ℂ U)) (hS : MeasurableSet S) :
    H →L⋆[ℂ] H →L[ℂ] ℂ
```

**`ProbabilisticTheory.QuantumMechanics.cfcSesquilinearForm_apply`**, a lemma, [line 1389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean#L1389).

```lean
lemma cfcSesquilinearForm_apply (S : Set (spectrum ℂ U)) (hS : MeasurableSet S) (x y : H) :
    cfcSesquilinearForm U hU S hS x y =
      starRingEnd ℂ (polarizedCfcScalarMeasure (hU := hU) U x y S)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/UnitaryInfra/SesquilinearForm.lean)
