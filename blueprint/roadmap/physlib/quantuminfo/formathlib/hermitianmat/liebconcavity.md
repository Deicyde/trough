---
declaration: module
origin: cited
lean: HermitianMatBridge.Φ, HermitianMatBridge.Φ_continuous, HermitianMatBridge.Φ_isSelfAdjoint, HermitianMatBridge.Φ_nonneg, HermitianMatBridge.Φ_mem_pdSet, HermitianMatBridge.Φ_cfc, HermitianMatBridge.Φ_rpow, HermitianMatBridge.trace_Φ_eq
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.LiebConcavity

The module `QuantumInfo.ForMathlib.HermitianMat.LiebConcavity`, [QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean): 10 declarations, 8 with a docstring; 11 private, not shown.

## Main result for DPI

> We derive the concavity of the trace functional `σ ↦ Tr[(σ^s H σ^s)^p]` from
> the Lieb–Ando trace inequalities proved in `LiebAndoTrace.lean`.

**`HermitianMatBridge.Φ`**, an abbrev, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L34).

> Abbreviation for the star algebra isomorphism.

```lean
noncomputable abbrev Φ : Matrix d d ℂ ≃⋆ₐ[ℂ] (EuclideanSpace ℂ d →L[ℂ] EuclideanSpace ℂ d)
```

**`HermitianMatBridge.Φ_continuous`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L38).

> `Φ` is continuous (as a linear map between finite-dimensional spaces).

```lean
lemma Φ_continuous : Continuous (⇑Φ : Matrix d d ℂ → _)
```

**`HermitianMatBridge.Φ_isSelfAdjoint`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L42).

> `Φ` maps Hermitian matrices to self-adjoint operators.

```lean
lemma Φ_isSelfAdjoint (A : HermitianMat d ℂ) :
    IsSelfAdjoint (Φ A.mat)
```

**`HermitianMatBridge.Φ_nonneg`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L50).

```lean
lemma Φ_nonneg (A : HermitianMat d ℂ) (hA : 0 ≤ A) :
    (0 : EuclideanSpace ℂ d →L[ℂ] EuclideanSpace ℂ d) ≤ Φ A.mat
```

**`HermitianMatBridge.Φ_mem_pdSet`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L82).

> `Φ` maps PosDef HermitianMat to pdSet.

```lean
lemma Φ_mem_pdSet [Nonempty d] (A : HermitianMat d ℂ) (hA : A.mat.PosDef) :
    Φ A.mat ∈ pdSet (ℋ := EuclideanSpace ℂ d)
```

**`HermitianMatBridge.Φ_cfc`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L100).

> `Φ` commutes with CFC for Hermitian matrices.

```lean
lemma Φ_cfc (A : HermitianMat d ℂ) (f : ℝ → ℝ) :
    Φ (cfc f A.mat) = cfc f (Φ A.mat)
```

**`HermitianMatBridge.Φ_rpow`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L107).

> `Φ` commutes with rpow for PSD matrices.

```lean
lemma Φ_rpow (A : HermitianMat d ℂ) (hA : 0 ≤ A) (r : ℝ) :
    Φ (A ^ r).mat = (Φ A.mat) ^ r
```

**`HermitianMatBridge.trace_Φ_eq`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L114).

> General trace bridge: the operator trace of Φ(M) equals the matrix trace of M,
> for any matrix M (not just Hermitian).

```lean
lemma trace_Φ_eq (M : Matrix d d ℂ) :
    (LinearMap.trace ℂ (EuclideanSpace ℂ d)) (Φ M).toLinearMap = M.trace
```

**`HermitianMatBridge.traceRe_Φ_general`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L122).

> `traceRe(Φ(M)) = re(Tr[M])` for any matrix M.

```lean
lemma traceRe_Φ_general (M : Matrix d d ℂ) :
    traceRe (Φ M) = Complex.re M.trace
```

### Density and continuity lemmas for PD/PSD extension

### Helper lemmas for the core concavity proof

### Core concavity on positive definite matrices

**`HermitianMat.trace_conj_rpow_concave`**, a lemma, [line 485](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean#L485).

```lean
lemma trace_conj_rpow_concave {α : ℝ} (hα : 1 < α)
    (H : HermitianMat d ℂ) (hH : 0 ≤ H) :
    ConcaveOn ℝ {σ : HermitianMat d ℂ | 0 ≤ σ}
      (fun σ ↦ ((H.conj (σ ^ ((α - 1) / (2 * α))).mat) ^ (α / (α - 1))).trace)
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LiebAndoTrace](../hayatagroup/traceinequality-liebandotrace.md)
- [Matrix Powers With Real Exponents](rpow.md)

## Proof depends on

- [Schatten norms](schatten.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/LiebConcavity.lean)
