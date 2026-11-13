---
declaration: module
origin: cited
lean: MatrixMap.Dual.trace_eq, MatrixMap.IsHermitianPreserving.dual, MatrixMap.IsPositive.dual, MatrixMap.dual_Unital, CPTPMap.dual.PTP_POVM, CPTPMap.exp_val_Dual, HPMap.inner_hermDual, HPMap.inner_hermDual'
statement: formalized
proof: formalized
---

# Duals of matrix map

The module `QuantumInfo.Channels.Dual`, [QuantumInfo/Channels/Dual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean): 34 declarations, 20 with a docstring, 12 listed as significant; 1 private, not shown.

> Definitions and theorems about the dual of a matrix map.

**`MatrixMap.dual`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L34).

> The dual of a map between matrices, defined by `Tr[A M(B)] = Tr[(dual M)(A) B]`. Sometimes
> called the adjoint of the map instead.

```lean
def dual (M : MatrixMap dIn dOut R) : MatrixMap dOut dIn R
```

**`MatrixMap.Dual.trace_eq`**, a theorem, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L43). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The defining property of a dual map: inner products are preserved on the opposite argument.

```lean
theorem Dual.trace_eq (M : MatrixMap dIn dOut R) (A : Matrix dIn dIn R) (B : Matrix dOut dOut R) :
    (M A * B).trace = (A * M.dual B).trace
```

**`MatrixMap.IsHermitianPreserving.dual`**, a theorem, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L71). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dual of a `IsHermitianPreserving` map also `IsHermitianPreserving`.

```lean
theorem IsHermitianPreserving.dual {M : MatrixMap dIn dOut ℂ} (h : M.IsHermitianPreserving) :
    M.dual.IsHermitianPreserving
```

**`Matrix.PosSemidef.trace_mul_nonneg`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L116).

```lean
lemma _root_.Matrix.PosSemidef.trace_mul_nonneg {n : Type*} [Fintype n] [DecidableEq n]
    {A B : Matrix n n 𝕜} (hA : A.PosSemidef) (hB : B.PosSemidef) :
    0 ≤ (A * B).trace
```

**`MatrixMap.IsPositive.dual`**, a theorem, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L133). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dual of a `IsPositive` map also `IsPositive`.

```lean
theorem IsPositive.dual {M : MatrixMap dIn dOut ℂ} (h : M.IsPositive) : M.dual.IsPositive
```

**`MatrixMap.dual_Unital`**, a theorem, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L152). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dual of TracePreserving map is *not* trace-preserving, it's *unital*, that is, M*(I) = I.

```lean
theorem dual_Unital (h : M.IsTracePreserving) : M.dual.Unital
```

**`MatrixMap.IsTracePreserving.dual`**, an alias, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L163).

```lean
alias IsTracePreserving.dual
```

**`MatrixMap.dual_unique`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L168).

> If two matrix maps satisfy the trace duality property, they are equal.

```lean
lemma dual_unique
    (M : MatrixMap dIn dOut 𝕜) (M' : MatrixMap dOut dIn 𝕜)
    (h : ∀ A B, (M A * B).trace = (A * M' B).trace) : M.dual = M'
```

**`MatrixMap.dual_choi_matrix`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L184).

> The Choi matrix of the dual map is the transpose of the reindexed Choi matrix of the original map.

```lean
lemma dual_choi_matrix (M : MatrixMap dIn dOut 𝕜) :
    M.dual.choi_matrix = (M.choi_matrix.transpose).reindex (Equiv.prodComm dOut dIn) (Equiv.prodComm dOut dIn)
```

**`MatrixMap.dual_choi_matrix_posSemidef_of_posSemidef`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L207).

> If the Choi matrix of a map is positive semidefinite, then the Choi matrix of its dual is also
> positive semidefinite.

```lean
lemma dual_choi_matrix_posSemidef_of_posSemidef (M : MatrixMap dIn dOut 𝕜) (h : M.choi_matrix.PosSemidef) :
    M.dual.choi_matrix.PosSemidef
```

**`MatrixMap.dual_id`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L217).

> The dual of the identity map is the identity map.

```lean
lemma dual_id : (MatrixMap.id dIn 𝕜).dual = MatrixMap.id dIn 𝕜
```

**`MatrixMap.dual_kron`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L243).

> The dual of a Kronecker product of maps is the Kronecker product of their duals.

```lean
lemma dual_kron {A B C D : Type*} [Fintype A] [Fintype B] [Fintype C] [Fintype D]
    [DecidableEq A] [DecidableEq B] [DecidableEq C] [DecidableEq D]
    (M : MatrixMap A B 𝕜) (N : MatrixMap C D 𝕜) :
    (M ⊗ₖₘ N).dual = M.dual ⊗ₖₘ N.dual
```

**`MatrixMap.IsCompletelyPositive.dual`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L268).

```lean
lemma IsCompletelyPositive.dual {M : MatrixMap dIn dOut ℂ} (h : M.IsCompletelyPositive) : M.dual.IsCompletelyPositive
```

**`MatrixMap.Module.Basis.dualMap_toDualEquiv_symm_comp_toDualEquiv`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L282).

> The composition of the dual of the inverse of the dual basis isomorphism with the dual basis
> isomorphism is the evaluation map.

```lean
lemma Module.Basis.dualMap_toDualEquiv_symm_comp_toDualEquiv {ι R M : Type*} [Fintype ι] [DecidableEq ι] [CommRing R] [AddCommGroup M] [Module R M] [Module.IsReflexive R M] (b : Module.Basis ι R M) :
    b.toDualEquiv.symm.toLinearMap.dualMap ∘ₗ b.toDualEquiv.toLinearMap = (Module.evalEquiv R M).toLinearMap
```

**`MatrixMap.Module.Basis.toDualEquiv_symm_comp_dualMap_toDualEquiv`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L297).

> The composition of the inverse of the dual basis isomorphism with the dual of the dual basis
> isomorphism is the inverse of the evaluation map.

```lean
lemma Module.Basis.toDualEquiv_symm_comp_dualMap_toDualEquiv {ι R M : Type*} [Fintype ι] [DecidableEq ι] [CommRing R] [AddCommGroup M] [Module R M] [Module.IsReflexive R M] (b : Module.Basis ι R M) :
    b.toDualEquiv.symm.toLinearMap ∘ₗ b.toDualEquiv.toLinearMap.dualMap = (Module.evalEquiv R M).symm.toLinearMap
```

**`MatrixMap.dual_dual`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L310).

```lean
lemma dual_dual : M.dual.dual = M
```

**`CPTPMap.dual`**, a def, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L324).

```lean
def dual (M : CPTPMap dIn dOut) : CPUMap dOut dIn
```

**`CPTPMap.dual_pos`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L329).

```lean
lemma dual_pos (M : CPTPMap dIn dOut) {T : HermitianMat dOut ℂ} (hT : 0 ≤ T) :
    0 ≤ M.dual T
```

**`CPTPMap.dual.PTP_POVM`**, a theorem, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L335). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dual of a CPTP map preserves POVMs. Stated here just for two-element POVMs, that is, an
> operator `T` between 0 and 1.

```lean
theorem dual.PTP_POVM (M : CPTPMap dIn dOut) {T : HermitianMat dOut ℂ} (hT : 0 ≤ T ∧ T ≤ 1) :
    (0 ≤ M.dual T ∧ M.dual T ≤ 1)
```

**`CPTPMap.exp_val_Dual`**, a theorem, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L343). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The defining property of a dual channel, as specialized to `MState.exp_val`.

```lean
theorem exp_val_Dual (ℰ : CPTPMap dIn dOut) (ρ : MState dIn) (T : HermitianMat dOut ℂ) :
    (ℰ ρ).exp_val T  = ρ.exp_val (ℰ.dual T)
```

**`HPMap.ofHermitianMat`**, a def, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L355).

```lean
def HPMap.ofHermitianMat {dOut : Type*} (f : HermitianMat dIn ℂ →ₗ[ℝ] HermitianMat dOut ℂ) : HPMap dIn dOut
```

**`HPMap.linearMap_ofHermitianMat`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L393).

```lean
lemma HPMap.linearMap_ofHermitianMat (f : HermitianMat dIn ℂ →ₗ[ℝ] HermitianMat dOut ℂ) :
    LinearMap.ofClass (HPMap.ofHermitianMat f) = f
```

**`HPMap.ofHermitianMat_linearMap`**, a lemma, [line 407](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L407).

```lean
lemma HPMap.ofHermitianMat_linearMap (f : HPMap dIn dOut ℂ) :
    ofHermitianMat (LinearMap.ofClass f) = f
```

**`HPMap.hermDual`**, a def, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L425).

```lean
def HPMap.hermDual : HPMap dOut dIn
```

**`HPMap.hermDual_hermDual`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L429).

```lean
lemma HPMap.hermDual_hermDual : f.hermDual.hermDual = f
```

**`HPMap.inner_hermDual`**, a theorem, [line 435](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L435). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The defining property of a dual map: inner products are preserved on the opposite argument.

```lean
theorem HPMap.inner_hermDual (B : HermitianMat dOut ℂ) :
    ⟪f A, B⟫ = ⟪A, f.hermDual B⟫
```

**`HPMap.inner_hermDual'`**, a theorem, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L441). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

```lean
theorem HPMap.inner_hermDual' (B : HermitianMat dOut ℂ) :
    ⟪f A, B⟫ = ⟪A, f.hermDual B⟫
```

**`MatrixMap.IsPositive.hermDual`**, a theorem, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L446). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dual of a `IsPositive` map also `IsPositive`.

```lean
theorem MatrixMap.IsPositive.hermDual (h : MatrixMap.IsPositive f.map) : f.hermDual.map.IsPositive
```

**`HPMap.hermDual_Unital`**, a theorem, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L464). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dual of TracePreserving map is *not* trace-preserving, it's *unital*, that is, M*(I) = I.

```lean
theorem HPMap.hermDual_Unital [DecidableEq dIn] [DecidableEq dOut] (h : MatrixMap.IsTracePreserving f.map) :
    f.hermDual.map.Unital
```

**`MatrixMap.IsTracePreserving.hermDual`**, an alias, [line 476](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L476).

```lean
alias MatrixMap.IsTracePreserving.hermDual
```

**`PTPMap.hermDual`**, a def, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L482).

```lean
def hermDual (M : PTPMap dIn dOut) : PUMap dOut dIn
```

**`PTPMap.hermDual_pos`**, a lemma, [line 487](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L487).

```lean
lemma hermDual_pos (M : PTPMap dIn dOut) {T : HermitianMat dOut ℂ} (hT : 0 ≤ T) :
    0 ≤ M.hermDual T
```

**`PTPMap.hermDual.PTP_POVM`**, a theorem, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L493). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The dual of a PTP map preserves POVMs. Stated here just for two-element POVMs, that is, an
> operator `T` between 0 and 1.

```lean
theorem hermDual.PTP_POVM (M : PTPMap dIn dOut) {T : HermitianMat dOut ℂ} (hT : 0 ≤ T ∧ T ≤ 1) :
    (0 ≤ M.hermDual T ∧ M.hermDual T ≤ 1)
```

**`PTPMap.exp_val_hermDual`**, a theorem, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean#L501). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The defining property of a dual channel, as specialized to `MState.exp_val`.

```lean
theorem exp_val_hermDual (ℰ : PTPMap dIn dOut) (ρ : MState dIn) (T : HermitianMat dOut ℂ) :
    (ℰ ρ).exp_val T  = ρ.exp_val (ℰ.hermDual T)
```

## Depends on

- [Classes of Matrix Maps](bundled.md)

## Sources

- [QuantumInfo/Channels/Dual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/Channels/Dual.lean)
