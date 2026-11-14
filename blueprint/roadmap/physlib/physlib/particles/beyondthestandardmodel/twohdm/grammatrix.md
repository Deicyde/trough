---
declaration: module
origin: cited
lean: TwoHiggsDoublet.gramMatrix, TwoHiggsDoublet.gramMatrix_selfAdjoint, TwoHiggsDoublet.eq_fst_norm_of_eq_gramMatrix, TwoHiggsDoublet.eq_snd_norm_of_eq_gramMatrix, TwoHiggsDoublet.gaugeGroupI_smul_gramMatrix, TwoHiggsDoublet.gramMatrix_det_eq, TwoHiggsDoublet.gramMatrix_det_eq_real, TwoHiggsDoublet.gramMatrix_det_nonneg
statement: formalized
proof: formalized
---

# The gram matrix for the two Higgs doublet model

The module `Physlib.Particles.BeyondTheStandardModel.TwoHDM.GramMatrix`, [Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean): 37 declarations, 4 with a docstring.

> We will show that the gram matrix of the two Higgs doublet model
> describes the gauge orbits of the configuration space.

## References

> * The main reference for material in this section is https://arxiv.org/pdf/hep-ph/0605184. [ref: arxiv\_hep\_ph\_0605184]

## A. The Gram matrix

**`TwoHiggsDoublet.gramMatrix`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L36).

> The Gram matrix of the two Higgs doublet.
> This matrix is used in https://arxiv.org/abs/hep-ph/0605184. [ref: arxiv\_hep\_ph\_0605184]

```lean
noncomputable def gramMatrix (H : TwoHiggsDoublet) : Matrix (Fin 2) (Fin 2) ℂ
```

**`TwoHiggsDoublet.gramMatrix_selfAdjoint`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L39).

```lean
lemma gramMatrix_selfAdjoint (H : TwoHiggsDoublet) :
    IsSelfAdjoint (gramMatrix H)
```

**`TwoHiggsDoublet.eq_fst_norm_of_eq_gramMatrix`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L45).

```lean
lemma eq_fst_norm_of_eq_gramMatrix {H1 H2 : TwoHiggsDoublet}
    (h : H1.gramMatrix = H2.gramMatrix) : ‖H1.Φ1‖ = ‖H2.Φ1‖
```

**`TwoHiggsDoublet.eq_snd_norm_of_eq_gramMatrix`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L50).

```lean
lemma eq_snd_norm_of_eq_gramMatrix {H1 H2 : TwoHiggsDoublet}
    (h : H1.gramMatrix = H2.gramMatrix) : ‖H1.Φ2‖ = ‖H2.Φ2‖
```

**`TwoHiggsDoublet.gaugeGroupI_smul_gramMatrix`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L56).

```lean
lemma gaugeGroupI_smul_gramMatrix (g : StandardModel.GaugeGroupI) (H : TwoHiggsDoublet) :
    (g • H).gramMatrix = H.gramMatrix
```

**`TwoHiggsDoublet.gramMatrix_det_eq`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L62).

```lean
lemma gramMatrix_det_eq (H : TwoHiggsDoublet) :
    H.gramMatrix.det = ‖H.Φ1‖ ^ 2 * ‖H.Φ2‖ ^ 2 - ‖⟪H.Φ1, H.Φ2⟫_ℂ‖ ^ 2
```

**`TwoHiggsDoublet.gramMatrix_det_eq_real`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L70).

```lean
lemma gramMatrix_det_eq_real (H : TwoHiggsDoublet) :
    H.gramMatrix.det.re = ‖H.Φ1‖ ^ 2 * ‖H.Φ2‖ ^ 2 - ‖⟪H.Φ1, H.Φ2⟫_ℂ‖ ^ 2
```

**`TwoHiggsDoublet.gramMatrix_det_nonneg`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L75).

```lean
lemma gramMatrix_det_nonneg (H : TwoHiggsDoublet) :
    0 ≤ H.gramMatrix.det.re
```

**`TwoHiggsDoublet.gramMatrix_tr_nonneg`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L84).

```lean
lemma gramMatrix_tr_nonneg (H : TwoHiggsDoublet) :
    0 ≤ H.gramMatrix.trace.re
```

**`TwoHiggsDoublet.gaugeGroupI_exists_fst_eq`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L92).

```lean
lemma gaugeGroupI_exists_fst_eq {H : TwoHiggsDoublet} (h1 : H.Φ1 ≠ 0) :
    ∃ g : StandardModel.GaugeGroupI,
      HiggsVec.repGaugeGroupI g H.Φ1 = (!₂[0, ‖H.Φ1‖] : HiggsVec) ∧
      (HiggsVec.repGaugeGroupI g H.Φ2) 1 = ⟪H.Φ1, H.Φ2⟫_ℂ / ‖H.Φ1‖ ∧
      ‖(HiggsVec.repGaugeGroupI g H.Φ2) 0‖ = Real.sqrt (H.gramMatrix.det.re) / ‖H.Φ1‖
```

**`TwoHiggsDoublet.gaugeGroupI_exists_fst_eq_snd_eq`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L144).

> Every two-Higgs-doublet configuration with `Φ1 ≠ 0` can be gauge-fixed to
> `Φ1 = (0, ‖Φ1‖)`, with the charged component of `Φ2` real and non-negative.

```lean
lemma gaugeGroupI_exists_fst_eq_snd_eq {H : TwoHiggsDoublet} (h1 : H.Φ1 ≠ 0) :
    ∃ g : StandardModel.GaugeGroupI,
      HiggsVec.repGaugeGroupI g H.Φ1 = (!₂[0, ‖H.Φ1‖] : HiggsVec) ∧
      HiggsVec.repGaugeGroupI g H.Φ2 =
        (!₂[√(H.gramMatrix.det.re) / ‖H.Φ1‖, ⟪H.Φ1, H.Φ2⟫_ℂ / ‖H.Φ1‖] : HiggsVec)
```

**`TwoHiggsDoublet.mem_orbit_gaugeGroupI_iff_gramMatrix`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L165).

```lean
lemma mem_orbit_gaugeGroupI_iff_gramMatrix (H1 H2 : TwoHiggsDoublet) :
    H1 ∈ MulAction.orbit GaugeGroupI H2 ↔ H1.gramMatrix = H2.gramMatrix
```

### A.1. Gram matrix is surjective

**`TwoHiggsDoublet.gramMatrix_surjective_det_tr`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L228).

```lean
lemma gramMatrix_surjective_det_tr (K : Matrix (Fin 2) (Fin 2) ℂ)
    (hKs : IsSelfAdjoint K) (hKdet : 0 ≤ K.det.re) (hKtr : 0 ≤ K.trace.re) :
    ∃ H : TwoHiggsDoublet, H.gramMatrix = K
```

## B. The Gram vector

**`TwoHiggsDoublet.gramVector`**, a def, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L289).

> A real vector containing the components of the Gram matrix in the Pauli basis.

```lean
noncomputable def gramVector (H : TwoHiggsDoublet) : Fin 1 ⊕ Fin 3 → ℝ
```

**`TwoHiggsDoublet.gramVector_eq`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L293).

> The lemma manifesting the definitional equality for the gramVector.

```lean
lemma gramVector_eq (H : TwoHiggsDoublet) : H.gramVector = fun μ =>
    2 * PauliMatrix.pauliBasis.repr ⟨gramMatrix H, gramMatrix_selfAdjoint H⟩ μ
```

**`TwoHiggsDoublet.gaugeGroupI_smul_fst_gramVector`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L297).

```lean
lemma gaugeGroupI_smul_fst_gramVector (g : StandardModel.GaugeGroupI)
    (H : TwoHiggsDoublet) (μ : Fin 1 ⊕ Fin 3) :
    (g • H).gramVector μ = H.gramVector μ
```

**`TwoHiggsDoublet.gramMatrix_eq_gramVector_sum_pauliMatrix`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L304).

```lean
lemma gramMatrix_eq_gramVector_sum_pauliMatrix (H : TwoHiggsDoublet) :
    gramMatrix H = (1 / 2 : ℝ) • ∑ μ, H.gramVector μ • PauliMatrix.pauliMatrix μ
```

**`TwoHiggsDoublet.gramMatrix_eq_component_gramVector`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L313).

```lean
lemma gramMatrix_eq_component_gramVector (H : TwoHiggsDoublet) :
    gramMatrix H =
    !![(1 / 2 : ℂ) * (H.gramVector (Sum.inl 0) + H.gramVector (Sum.inr 2)),
      (1 / 2 : ℂ) * (H.gramVector (Sum.inr 0) - Complex.I * H.gramVector (Sum.inr 1));
      (1 / 2 : ℂ) * (H.gramVector (Sum.inr 0) + Complex.I * H.gramVector (Sum.inr 1)),
      (1 / 2 : ℂ) * (H.gramVector (Sum.inl 0) - H.gramVector (Sum.inr 2))]
```

**`TwoHiggsDoublet.gramVector_inl_eq_trace_gramMatrix`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L324).

```lean
lemma gramVector_inl_eq_trace_gramMatrix (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inl 0) = H.gramMatrix.trace.re
```

**`TwoHiggsDoublet.gramVector_inl_nonneg`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L334).

```lean
lemma gramVector_inl_nonneg (H : TwoHiggsDoublet) :
    0 ≤ H.gramVector (Sum.inl 0)
```

**`TwoHiggsDoublet.normSq_Φ1_eq_gramVector`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L339).

```lean
lemma normSq_Φ1_eq_gramVector (H : TwoHiggsDoublet) :
    ‖H.Φ1‖ ^ 2 = (1/2 : ℝ) * (H.gramVector (Sum.inl 0) + H.gramVector (Sum.inr 2))
```

**`TwoHiggsDoublet.normSq_Φ2_eq_gramVector`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L346).

```lean
lemma normSq_Φ2_eq_gramVector (H : TwoHiggsDoublet) :
    ‖H.Φ2‖ ^ 2 = (1/2 : ℝ) * (H.gramVector (Sum.inl 0) - H.gramVector (Sum.inr 2))
```

**`TwoHiggsDoublet.Φ1_inner_Φ2_eq_gramVector`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L353).

```lean
lemma Φ1_inner_Φ2_eq_gramVector (H : TwoHiggsDoublet) :
    (⟪H.Φ1, H.Φ2⟫_ℂ) = (1/2 : ℝ) * (H.gramVector (Sum.inr 0) +
    Complex.I * H.gramVector (Sum.inr 1))
```

**`TwoHiggsDoublet.Φ2_inner_Φ1_eq_gramVector`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L360).

```lean
lemma Φ2_inner_Φ1_eq_gramVector (H : TwoHiggsDoublet) :
    (⟪H.Φ2, H.Φ1⟫_ℂ) = (1/2 : ℝ) * (H.gramVector (Sum.inr 0) -
    Complex.I * H.gramVector (Sum.inr 1))
```

**`TwoHiggsDoublet.Φ1_inner_Φ2_normSq_eq_gramVector`**, a lemma, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L369).

```lean
lemma Φ1_inner_Φ2_normSq_eq_gramVector (H : TwoHiggsDoublet) :
    ‖⟪H.Φ1, H.Φ2⟫_ℂ‖ ^ 2 =
    (1/4 : ℝ) * (H.gramVector (Sum.inr 0) ^ 2 + H.gramVector (Sum.inr 1) ^ 2)
```

**`TwoHiggsDoublet.gramVector_inl_zero_eq`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L380).

```lean
lemma gramVector_inl_zero_eq (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inl 0) = ‖H.Φ1‖ ^ 2 + ‖H.Φ2‖ ^ 2
```

**`TwoHiggsDoublet.gramVector_inl_zero_eq_gramMatrix`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L385).

```lean
lemma gramVector_inl_zero_eq_gramMatrix (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inl 0) = (H.gramMatrix 0 0).re + (H.gramMatrix 1 1).re
```

**`TwoHiggsDoublet.gramVector_inr_zero_eq`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L389).

```lean
lemma gramVector_inr_zero_eq (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inr 0) = 2 * (⟪H.Φ1, H.Φ2⟫_ℂ).re
```

**`TwoHiggsDoublet.gramVector_inr_zero_eq_gramMatrix`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L394).

```lean
lemma gramVector_inr_zero_eq_gramMatrix (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inr 0) = 2 * (H.gramMatrix 1 0).re
```

**`TwoHiggsDoublet.gramVector_inr_one_eq`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L399).

```lean
lemma gramVector_inr_one_eq (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inr 1) = 2 * (⟪H.Φ1, H.Φ2⟫_ℂ).im
```

**`TwoHiggsDoublet.gramVector_inr_one_eq_gramMatrix`**, a lemma, [line 404](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L404).

```lean
lemma gramVector_inr_one_eq_gramMatrix (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inr 1) = 2 * (H.gramMatrix 1 0).im
```

**`TwoHiggsDoublet.gramVector_inr_two_eq`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L409).

```lean
lemma gramVector_inr_two_eq (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inr 2) = ‖H.Φ1‖ ^ 2 - ‖H.Φ2‖ ^ 2
```

**`TwoHiggsDoublet.gramVector_inr_two_eq_gramMatrix`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L414).

```lean
lemma gramVector_inr_two_eq_gramMatrix (H : TwoHiggsDoublet) :
    H.gramVector (Sum.inr 2) = (H.gramMatrix 0 0).re - (H.gramMatrix 1 1).re
```

**`TwoHiggsDoublet.gramMatrix_det_eq_gramVector`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L418).

```lean
lemma gramMatrix_det_eq_gramVector (H : TwoHiggsDoublet) :
    H.gramMatrix.det.re =
    (1/4 : ℝ) * (H.gramVector (Sum.inl 0) ^ 2 -
    ∑ μ : Fin 3, H.gramVector (Sum.inr μ) ^ 2)
```

**`TwoHiggsDoublet.gramVector_inr_sum_sq_le_inl`**, a lemma, [line 427](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L427).

```lean
lemma gramVector_inr_sum_sq_le_inl (H : TwoHiggsDoublet) :
    ∑ μ : Fin 3, H.gramVector (Sum.inr μ) ^ 2 ≤ H.gramVector (Sum.inl 0) ^ 2
```

**`TwoHiggsDoublet.gramVector_surjective`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L433).

```lean
lemma gramVector_surjective (v : Fin 1 ⊕ Fin 3 → ℝ)
    (h_inl : 0 ≤ v (Sum.inl 0))
    (h_det : ∑ μ : Fin 3, v (Sum.inr μ) ^ 2 ≤ v (Sum.inl 0) ^ 2) :
    ∃ H : TwoHiggsDoublet, H.gramVector = v
```

**`TwoHiggsDoublet.mem_orbit_gaugeGroupI_iff_gramVector`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean#L464).

```lean
lemma mem_orbit_gaugeGroupI_iff_gramVector (H1 H2 : TwoHiggsDoublet) :
    H1 ∈ MulAction.orbit GaugeGroupI H2 ↔ H1.gramVector = H2.gramVector
```

## Depends on

- [The Two Higgs Doublet Model](basic.md)

## Sources

- [Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/BeyondTheStandardModel/TwoHDM/GramMatrix.lean)
