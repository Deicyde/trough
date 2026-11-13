---
declaration: module
origin: cited
lean: HermitianMat.inner_eq_trace_mul, HermitianMat.inner_eq_trace_trivial, HermitianMat.inner_ge_zero, HermitianMat.inner_le_mul_trace, HermitianMat.inner_zero_iff, HermitianMat.unitInterval_IsCompact, HermitianMat.inner_def, HermitianMat.inner_add_right
statement: formalized
proof: formalized
---

# Inner product of Hermitian Matrices

The module `QuantumInfo.ForMathlib.HermitianMat.Inner`, [QuantumInfo/ForMathlib/HermitianMat/Inner.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean): 50 declarations (6 instances with no name), 12 with a docstring, 6 listed as significant; 1 private, not shown.

> For general matrices there are multiple reasonable notions of "inner product" (Hilbert–Schmidt inner product,
> Frobenius inner product), and so Mathlib avoids giving a canonical `InnerProductSpace` instance. But for the
> particular case of Hermitian matrices, these all coincide, so we can put a canonical `InnerProductSpace`
> instance.
>
> This \_does\_ however induce a `Norm` on `HermitianMat` as well, the Frobenius norm, and this is less obviously
> a uniquely correct choice. It is something that one essentially has to live with, with the way that Mathlib
> currently structures the instances. (Thankfully, all norms induce the same \_topology and bornology\_ on
> finite-dimensional matrices.)
>
> Some care to be taken so that the topology induced by the InnerProductSpace is defeq with the Subtype
> topology that HermitianMat inherits from the topology on Matrix. This can be done via
> `InnerProductSpace.ofCoreOfTopology`.

**An instance with no name**, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L43).

> The Hermitian inner product, `Tr[AB]`. This is equal to `Matrix.trace (A * B)`, but gives real
> values when the matrices are complex, using `IsMaximalSelfAdjoint`.

```lean
instance : Inner R (HermitianMat n α)
```

**`HermitianMat.inner_def`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L46).

```lean
lemma inner_def (A B : HermitianMat n α) :
    ⟪A, B⟫_R = selfadjMap (A.mat * B.mat).trace
```

**`HermitianMat.inner_add_right`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L59).

```lean
protected lemma inner_add_right : ⟪A, B + C⟫_R = ⟪A, B⟫_R + ⟪A, C⟫_R
```

**`HermitianMat.inner_add_left`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L62).

```lean
protected lemma inner_add_left : ⟪A + B, C⟫_R = ⟪A, C⟫_R + ⟪B, C⟫_R
```

**`HermitianMat.inner_zero_right`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L66).

```lean
protected lemma inner_zero_right : ⟪A, 0⟫_R = 0
```

**`HermitianMat.inner_zero_left`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L70).

```lean
protected lemma inner_zero_left : ⟪0, A⟫_R = 0
```

**`HermitianMat.inner_neg_left`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L80).

```lean
protected lemma inner_neg_left : ⟪-A, B⟫_R = -⟪A, B⟫_R
```

**`HermitianMat.inner_neg_right`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L84).

```lean
protected lemma inner_neg_right : ⟪A, -B⟫_R = -⟪A, B⟫_R
```

**`HermitianMat.inner_sub_left`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L87).

```lean
protected lemma inner_sub_left : ⟪A, B - C⟫_R = ⟪A, B⟫_R - ⟪A, C⟫_R
```

**`HermitianMat.inner_sub_right`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L90).

```lean
protected lemma inner_sub_right : ⟪A - B, C⟫_R = ⟪A, C⟫_R - ⟪B, C⟫_R
```

**`HermitianMat.inner_smul_left`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L96).

```lean
protected lemma inner_smul_left (r : R) : ⟪r • A, B⟫_R = r * ⟪A, B⟫_R
```

**`HermitianMat.inner_smul_right`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L100).

```lean
protected lemma inner_smul_right (r : R) : ⟪A, r • B⟫_R = r * ⟪A, B⟫_R
```

**`HermitianMat.innerₗ`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L105).

> The Hermitian inner product as bilinear form. Compare with `innerₗ` (in the root namespace)
> which requires an `InnerProductSpace` instance.

```lean
protected def innerₗ : LinearMap.BilinForm R (HermitianMat n α)
```

**`HermitianMat.inner_one`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L121).

```lean
lemma inner_one : ⟪A, 1⟫_R = A.trace
```

**`HermitianMat.one_inner`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L125).

```lean
lemma one_inner : ⟪1, A⟫_R = A.trace
```

**`HermitianMat.inner_eq_trace_mul`**, a theorem, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L135). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The inner product for Hermtian matrices is equal to the trace of the product.

```lean
theorem inner_eq_trace_mul : algebraMap R α ⟪A, B⟫_R = (A.mat * B.mat).trace
```

**`HermitianMat.inner_comm`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L142).

```lean
lemma inner_comm : ⟪A, B⟫_R = ⟪B, A⟫_R
```

**`HermitianMat.inner_eq_trace_trivial`**, a theorem, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L152). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `HermitianMat.inner` reduces to `Matrix.trace (A * B)` when the elements are a `TrivialStar`.

```lean
theorem inner_eq_trace_trivial : ⟪A, B⟫_α = (A.mat * B.mat).trace
```

**`HermitianMat.inner_eq_re_trace`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L164).

```lean
lemma inner_eq_re_trace : ⟪A, B⟫ = RCLike.re (A.mat * B.mat).trace
```

**`HermitianMat.inner_eq_trace_rc`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L167).

```lean
lemma inner_eq_trace_rc : ⟪A, B⟫ = (A.mat * B.mat).trace
```

**`HermitianMat.inner_self_nonneg`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L172).

```lean
lemma inner_self_nonneg: 0 ≤ ⟪A, A⟫
```

**`HermitianMat.inner_mul_nonneg`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L183).

```lean
lemma inner_mul_nonneg (h : 0 ≤ A.mat * B.mat) : 0 ≤ ⟪A, B⟫
```

**`HermitianMat.inner_ge_zero`**, a theorem, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L188). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The inner product for PSD matrices is nonnegative.

```lean
theorem inner_ge_zero (hA : 0 ≤ A) (hB : 0 ≤ B) : 0 ≤ ⟪A, B⟫
```

**`HermitianMat.inner_mono`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L196).

```lean
lemma inner_mono (hA : 0 ≤ A) : B ≤ C → ⟪A, B⟫ ≤ ⟪A, C⟫
```

**`HermitianMat.inner_mono'`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L201).

```lean
lemma inner_mono' (hA : 0 ≤ A) : B ≤ C → ⟪B, A⟫ ≤ ⟪C, A⟫
```

**`HermitianMat.inner_le_mul_trace`**, a theorem, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L207). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The inner product for PSD matrices is at most the product of their traces.

```lean
theorem inner_le_mul_trace (hA : 0 ≤ A) (hB : 0 ≤ B) : ⟪A, B⟫ ≤ A.trace * B.trace
```

**`HermitianMat.inner_zero_iff`**, a theorem, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L255). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The inner product of two PSD matrices is zero iff they have disjoint support, i.e., each lives entirely
> in the other's kernel.

```lean
theorem inner_zero_iff [DecidableEq n] (hA₁ : 0 ≤ A) (hB₁ : 0 ≤ B)
    : ⟪A, B⟫ = 0 ↔ A.support ≤ B.ker
```

**`HermitianMat.reindex_inner`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L264).

```lean
lemma reindex_inner (e : d ≃ d₂) (B : HermitianMat d₂ 𝕜) :
    ⟪A.reindex e, B⟫ = ⟪A, B.reindex e.symm⟫
```

> Theorems about `HermitianMat`s that have to do with the topological structure. Pretty much everything here will
> assume these are matrices over ℂ, but changes to upgrade this to other types are welcome.

**`HermitianMat.inner_continuous`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L289).

```lean
lemma inner_continuous : Continuous (Inner.inner ℝ (E := HermitianMat d 𝕜))
```

**`HermitianMat.inner_bilinForm_Continuous`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L294).

```lean
lemma inner_bilinForm_Continuous (A : HermitianMat d 𝕜) : Continuous ⇑(HermitianMat.innerₗ A)
```

**`HermitianMat.InnerProductCore`**, a def, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L307).

> We define the Hermitian inner product as our "canonical" inner product, which does induce a norm.
> This disagrees slightly with Mathlib convention on the `Matrix` type, which avoids asserting one norm
> as there are several reasonable ones; for Hermitian matrices, though, this seem to be the right choice.

```lean
noncomputable def InnerProductCore : InnerProductSpace.Core ℝ (HermitianMat d 𝕜)
```

**`HermitianMat.instNormedGroup`**, an instance, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L337).

> The `HermitianMat` type inherits the Frobenius necessarily, since it's going to need the
> Hermitian inner product, and in Mathlib an `InnerProductSpace` always carries the corresponding
> norm.

```lean
noncomputable instance instNormedGroup : NormedAddCommGroup (HermitianMat d 𝕜)
```

**`HermitianMat.norm_eq_frobenius`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L340).

```lean
lemma norm_eq_frobenius (A : HermitianMat d 𝕜) :
    ‖A‖ = (∑ i : d, ∑ j : d, ‖A i j‖ ^ 2) ^ (1 / 2 : ℝ)
```

**`HermitianMat.norm_eq_sqrt_inner_self`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L345).

```lean
lemma norm_eq_sqrt_inner_self (A : HermitianMat d 𝕜) : ‖A‖ = √(⟪A, A⟫)
```

**`HermitianMat.instNormedSpace`**, an instance, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L355).

```lean
noncomputable instance instNormedSpace : NormedSpace ℝ (HermitianMat d 𝕜)
```

**`HermitianMat.instInnerProductSpace`**, an instance, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L360).

```lean
noncomputable instance instInnerProductSpace : InnerProductSpace ℝ (HermitianMat d 𝕜)
```

**An instance with no name**, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L368).

```lean
instance : CompleteSpace (HermitianMat d 𝕜)
```

**An instance with no name**, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L372).

```lean
noncomputable instance : NormedAddCommGroup (HermitianMat d ℝ)
```

**An instance with no name**, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L375).

```lean
noncomputable instance : NormedAddCommGroup (HermitianMat d ℂ)
```

**`RCLike.instOrderClosed`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L380).

```lean
lemma _root_.RCLike.instOrderClosed : OrderClosedTopology 𝕜
```

**`HermitianMat.dist_le_of_mem_Icc`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L391).

```lean
lemma dist_le_of_mem_Icc (x : HermitianMat d 𝕜) (hA : A ≤ x) (hB : x ≤ B) :
    ‖x - A‖ ≤ ‖B - A‖
```

**`HermitianMat.Matrix.IsHermitian_isClosed`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L401).

```lean
lemma Matrix.IsHermitian_isClosed : IsClosed { A : Matrix n n 𝕜 | A.IsHermitian }
```

**`HermitianMat.Matrix.PosSemiDef_isClosed`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L410).

```lean
lemma Matrix.PosSemiDef_isClosed : IsClosed { A : Matrix n n 𝕜 | A.PosSemidef }
```

**`HermitianMat.isClosed_nonneg`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L418).

```lean
lemma isClosed_nonneg : IsClosed { A : HermitianMat n 𝕜 | 0 ≤ A }
```

**An instance with no name**, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L424).

```lean
instance : OrderClosedTopology (HermitianMat d 𝕜)
```

**An instance with no name**, [line 434](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L434).

> Equivalently: the matrices `X` such that `X - A` is PSD and `B - X` is PSD, form a compact set.

```lean
instance : CompactIccSpace (HermitianMat d 𝕜)
```

**`HermitianMat.unitInterval_IsCompact`**, a theorem, [line 452](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L452). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The PSD matrices that are `≤ 1` are a compact set. More generally, this is true of any closed interval,
> but stating that is a bit different because of how numerals are treated. The `0` and `1` here are already
> directly matrices, putting in an `(a : ℝ) • 1 ≤ m ∧ m ≤ (b : ℝ) • 1` involves casts. But that theorem should follow
> easily from this. More generally `A ≤ m ∧ m ≤ B` is compact.

```lean
theorem unitInterval_IsCompact : IsCompact {m : HermitianMat d 𝕜 | 0 ≤ m ∧ m ≤ 1}
```

**`HermitianMat.norm_one`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L456).

```lean
lemma norm_one : ‖(1 : HermitianMat d 𝕜)‖ = √(Fintype.card d : ℝ)
```

**`HermitianMat.norm_eq_trace_sq`**, a lemma, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L461).

```lean
lemma norm_eq_trace_sq : ‖A‖ ^ 2 = (A.mat ^ 2).trace
```

**`HermitianMat.inner_eq_doubly_stochastic_sum`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean#L477).

> The inner product ⟪A, B⟫ equals ∑\_\{ij} a\_i b\_j w\_\{ij} where a\_i, b\_j are eigenvalues
> and w\_\{ij} = ‖C\_\{ij}‖² for C = U\_A^* U\_B unitary.

```lean
lemma inner_eq_doubly_stochastic_sum {d : Type*} [Fintype d] [DecidableEq d]
    (A B : HermitianMat d ℂ) :
    let C := A.H.eigenvectorUnitary.val.conjTranspose * B.H.eigenvectorUnitary.val
    ⟪A, B⟫_ℝ = ∑ i, ∑ j,
      A.H.eigenvalues i * B.H.eigenvalues j * (‖C i j‖^2)
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Order](order.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Inner.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Inner.lean)
