---
declaration: module
origin: cited
lean: HermitianMat.H, HermitianMat.ker_eq_eigenspace_zero, HermitianMat.support_eq_sup_eigenspace_nonzero, HermitianMat.kron_commute, HermitianMat.kron_id_commute_id_kro, Matrix.range_mul_conjTranspose_of_ker_le_ker, HermitianMat.spectrum_rcLike, HermitianMat
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Basic

The module `QuantumInfo.ForMathlib.HermitianMat.Basic`, [QuantumInfo/ForMathlib/HermitianMat/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean): 130 declarations (22 instances with no name), 17 with a docstring, 7 listed as significant.

**`HermitianMat`**, a def, [line 17](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L17).

> The type of Hermitian matrices, as a `Subtype`. Equivalent to a `Matrix n n α` bundled
> with the fact that `Matrix.IsHermitian`.

```lean
def HermitianMat (n : Type*) (α : Type*) [AddGroup α] [StarAddMonoid α]
```

**An instance with no name**, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L30).

```lean
instance [IsEmpty n] : Subsingleton (HermitianMat n α)
```

**`HermitianMat.eq_IsHermitian`**, a lemma, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L33).

```lean
lemma eq_IsHermitian : HermitianMat n α  = { m : Matrix n n α // m.IsHermitian}
```

**`HermitianMat.mat`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L36).

```lean
def mat : HermitianMat n α → Matrix n n α
```

**An instance with no name**, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L39).

```lean
instance : Coe (HermitianMat n α) (Matrix n n α)
```

**`HermitianMat.val_eq_coe`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L42).

```lean
lemma val_eq_coe (A : HermitianMat n α) : A.val = A
```

**`HermitianMat.mat_mk`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L46).

```lean
lemma mat_mk (x : Matrix n n α) (h) : mat ⟨x, h⟩ = x
```

**`HermitianMat.mk_mat`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L50).

```lean
lemma mk_mat {A : HermitianMat n α} (h : A.mat.IsHermitian) : ⟨A.mat, h⟩ = A
```

**`HermitianMat.H`**, a theorem, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L55). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Alias for HermitianMat.property or HermitianMat.2, this gets the fact that the value
> is actually `IsHermitian`.

```lean
theorem H (A : HermitianMat n α) : A.mat.IsHermitian
```

**`HermitianMat.ext`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L58).

```lean
protected lemma ext {A B : HermitianMat n α} : A.mat = B.mat → A = B
```

**`HermitianMat.instFun`**, an instance, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L61).

```lean
instance instFun : FunLike (HermitianMat n α) n (n → α)
```

**`HermitianMat.mat_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L66).

```lean
lemma mat_apply {A : HermitianMat n α} {i j : n} : A.mat i j = A i j
```

**`HermitianMat.conjTranspose_mat`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L70).

```lean
lemma conjTranspose_mat (A : HermitianMat n α) :
    A.mat.conjTranspose = A.mat
```

**An instance with no name**, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L74).

```lean
instance : AddGroup (HermitianMat n α)
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L77).

```lean
instance [IsEmpty n] : Unique (HermitianMat n α)
```

**`HermitianMat.mat_zero`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L82).

```lean
lemma mat_zero : (0 : HermitianMat n α).mat = 0
```

**`HermitianMat.mk_zero`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L86).

```lean
lemma mk_zero (h : (0 : Matrix n n α).IsHermitian) : ⟨0, h⟩ = (0 : HermitianMat n α)
```

**`HermitianMat.zero_apply`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L90).

```lean
lemma zero_apply (i j : n) : (0 : HermitianMat n 𝕜) i j = 0
```

**`HermitianMat.mat_add`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L94).

```lean
lemma mat_add (A B : HermitianMat n α) :
    (A + B).mat = A.mat + B.mat
```

**`HermitianMat.mat_sub`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L99).

```lean
lemma mat_sub (A B : HermitianMat n α) :
    (A - B).mat = A.mat - B.mat
```

**`HermitianMat.mat_neg`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L104).

```lean
lemma mat_neg (A : HermitianMat n α) :
    (-A).mat = -A.mat
```

**An instance with no name**, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L111).

```lean
instance : SMul R (HermitianMat n α)
```

**`HermitianMat.mat_smul`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L115).

```lean
lemma mat_smul (c : R) (A : HermitianMat n α) :
    (c • A).mat = c • A.mat
```

**`HermitianMat.smul_apply`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L120).

```lean
lemma smul_apply (c : R) (A : HermitianMat n α) (i j : n) :
    (c • A) i j = c • A i j
```

**An instance with no name**, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L128).

```lean
instance : TopologicalSpace (HermitianMat n α)
```

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L131).

```lean
instance [T2Space α] : T2Space (HermitianMat m α)
```

**`HermitianMat.continuous_mat`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L138).

```lean
lemma continuous_mat : Continuous (HermitianMat.mat : HermitianMat n α → Matrix n n α)
```

**`HermitianMat.continuousOn_iff_coe`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L141).

```lean
lemma continuousOn_iff_coe {X : Type*} [TopologicalSpace X] {s : Set X}
    (f : X → HermitianMat n α) :
    ContinuousOn f s ↔ ContinuousOn (fun x => (f x).mat) s
```

**An instance with no name**, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L155).

```lean
instance : ContinuousAdd (HermitianMat n α)
```

**An instance with no name**, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L158).

```lean
instance : ContinuousNeg (HermitianMat n α)
```

**An instance with no name**, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L161).

```lean
instance : IsTopologicalAddGroup (HermitianMat n α)
```

**An instance with no name**, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L166).

```lean
instance : ContinuousSMul R (HermitianMat n α)
```

**An instance with no name**, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L172).

```lean
instance : IsTopologicalAddGroup (HermitianMat n 𝕜)
```

**An instance with no name**, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L174).

```lean
instance : ContinuousSMul ℝ (HermitianMat n ℂ)
```

**An instance with no name**, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L177).

```lean
instance : T3Space (HermitianMat n 𝕜)
```

**An instance with no name**, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L185).

```lean
instance : MulAction R (HermitianMat n α)
```

**An instance with no name**, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L194).

```lean
instance : AddCommGroup (HermitianMat n α)
```

**`HermitianMat.mat_finset_sum`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L198).

```lean
lemma mat_finset_sum (f : ι → HermitianMat n α) (s : Finset ι) :
    (∑ i ∈ s, f i).mat = ∑ i ∈ s, (f i).mat
```

**An instance with no name**, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L206).

```lean
instance : Module R (HermitianMat n α)
```

**`HermitianMat.matₗ`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L213).

> The projection from HermitianMat to Matrix, as a continuous linear map.

```lean
def matₗ : HermitianMat n α →L[R] Matrix n n α
```

**An instance with no name**, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L225).

```lean
instance : One (HermitianMat n α)
```

**`HermitianMat.mat_one`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L231).

```lean
lemma mat_one : (1 : HermitianMat n α).mat = 1
```

**`HermitianMat.mk_one`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L235).

```lean
lemma mk_one (h : (1 : Matrix n n α).IsHermitian) : ⟨1, h⟩ = (1 : HermitianMat n α)
```

**`HermitianMat.one_apply`**, a lemma, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L239).

```lean
lemma one_apply (i j : n) : (1 : HermitianMat n α) i j = (1 : Matrix n n α) i j
```

**An instance with no name**, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L242).

```lean
noncomputable instance : AddCommMonoidWithOne (HermitianMat n 𝕜)
```

**An instance with no name**, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L244).

```lean
instance [i : Nonempty n] : NeZero (1 : HermitianMat n 𝕜)
```

**`HermitianMat.instInv`**, an instance, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L255).

```lean
noncomputable instance instInv : Inv (HermitianMat m α)
```

**`HermitianMat.mat_inv`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L259).

```lean
lemma mat_inv : (A⁻¹).mat = A.mat⁻¹
```

**`HermitianMat.zero_inv`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L263).

```lean
lemma zero_inv : ((0 : HermitianMat m α)⁻¹) = 0
```

**`HermitianMat.one_inv`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L267).

```lean
lemma one_inv : ((1 : HermitianMat m α)⁻¹) = 1
```

**`HermitianMat.instPow`**, an instance, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L270).

```lean
noncomputable instance instPow : Pow (HermitianMat m α) ℕ
```

**`HermitianMat.mat_pow`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L274).

```lean
lemma mat_pow (n : ℕ) : (A ^ n).mat = A.mat ^ n
```

**`HermitianMat.pow_zero`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L278).

```lean
lemma pow_zero : A ^ 0 = 1
```

**`HermitianMat.zero_pow`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L282).

```lean
lemma zero_pow (hn : n ≠ 0): (0 : HermitianMat m α) ^ n = 0
```

**`HermitianMat.one_pow`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L286).

```lean
lemma one_pow : ((1 : HermitianMat m α) ^ n) = 1
```

**`HermitianMat.instZPow`**, an instance, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L289).

```lean
noncomputable instance instZPow : Pow (HermitianMat m α) ℤ
```

**`HermitianMat.mat_zpow`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L293).

```lean
lemma mat_zpow (z : ℤ) : (A ^ z).mat = A.mat ^ z
```

**`HermitianMat.zpow_natCast`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L297).

```lean
lemma zpow_natCast : A ^ (n : ℤ) = A ^ n
```

**`HermitianMat.zpow_zero`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L301).

```lean
lemma zpow_zero : A ^ (0 : ℤ) = 1
```

**`HermitianMat.zpow_one`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L305).

```lean
lemma zpow_one : A ^ (1 : ℤ) = A
```

**`HermitianMat.one_zpow`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L309).

```lean
lemma one_zpow : ((1 : HermitianMat m α) ^ z) = 1
```

**`HermitianMat.zpow_neg_one`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L313).

```lean
lemma zpow_neg_one : A ^ (-1 : ℤ) = A⁻¹
```

**`HermitianMat.inv_zpow`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L317).

```lean
lemma inv_zpow : A⁻¹ ^ z = (A ^ z)⁻¹
```

**`Matrix.inv_commute`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L324).

```lean
lemma _root_.Matrix.inv_commute {α : Type*} {A : Matrix m m α} [CommRing α] : Commute A⁻¹ A
```

**`HermitianMat.commute_inv_self`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L330).

```lean
lemma commute_inv_self : Commute A⁻¹.mat A.mat
```

**`HermitianMat.commute_self_inv`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L334).

```lean
lemma commute_self_inv : Commute A.mat A⁻¹.mat
```

**`HermitianMat.FiniteDimensional`**, an instance, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L341).

```lean
instance FiniteDimensional : FiniteDimensional ℝ (HermitianMat n 𝕜)
```

**`HermitianMat.im_diag_eq_zero`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L345).

```lean
lemma im_diag_eq_zero (A : HermitianMat n 𝕜) (x : n) :
    RCLike.im (A x x) = 0
```

**`HermitianMat.complex_im_eq_zero`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L351).

```lean
lemma complex_im_eq_zero (A : HermitianMat n ℂ) (x : n) :
    (A x x).im = 0
```

**`HermitianMat.conj`**, a def, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L367).

> The Hermitian matrix given by conjugating by a (possibly rectangular) Matrix. If we required `B` to be
> square, this would apply to any `Semigroup`+`StarMul` (as proved by `IsSelfAdjoint.conjugate`). But this lets
> us conjugate to other sizes too, as is done in e.g. Kraus operators. That is, it's a \_heterogeneous\_ conjguation.

```lean
def conj {m} (B : Matrix m n α) : HermitianMat n α →+ HermitianMat m α
```

**`HermitianMat.conj_apply`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L379).

```lean
lemma conj_apply (B : Matrix m n α) (A : HermitianMat n α) :
    conj B A = ⟨B * A.mat * B.conjTranspose, (conj B A).2⟩
```

**`HermitianMat.conj_apply_mat`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L384).

```lean
lemma conj_apply_mat (B : Matrix m n α) (A : HermitianMat n α) :
    (A.conj B).mat = B * A.mat * B.conjTranspose
```

**`HermitianMat.conj_conj`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L388).

```lean
lemma conj_conj {m l} [Fintype m] (B : Matrix m n α) (C : Matrix l m α) :
    (A.conj B).conj C = A.conj (C * B)
```

**`HermitianMat.conj_zero`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L397).

```lean
lemma conj_zero [DecidableEq n] : A.conj (0 : Matrix m n α) = 0
```

**`HermitianMat.conj_one`**, a lemma, [line 402](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L402).

```lean
lemma conj_one [DecidableEq n] : A.conj 1 = A
```

**`HermitianMat.conj_one_unitary`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L406).

```lean
lemma conj_one_unitary [DecidableEq n] (U : Matrix.unitaryGroup n α) :
    conj U.val 1 = 1
```

**`HermitianMat.conjLinear`**, a def, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L415).

> `HermitianMat.conj` as an `R`-linear map, where `R` is the ring of relevant reals.

```lean
def conjLinear {m} (B : Matrix m n α) : HermitianMat n α →ₗ[R] HermitianMat m α
```

**`HermitianMat.conjLinear_apply`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L422).

```lean
lemma conjLinear_apply (B : Matrix m n α) : conjLinear R B A = conj B A
```

**`HermitianMat.continuous_conj`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L428).

```lean
lemma continuous_conj [TopologicalSpace α] [IsTopologicalRing α] [ContinuousStar α]
    (ρ : HermitianMat n α) :
    Continuous (ρ.conj (m := m) ·)
```

**`HermitianMat.continuous_conj_right`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L437).

> conj is continuous in its right argument.

```lean
lemma continuous_conj_right [TopologicalSpace α] [IsTopologicalRing α] (B : Matrix m n α) :
    Continuous (HermitianMat.conj B)
```

**An instance with no name**, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L448).

```lean
instance [i : Nonempty n] : FaithfulSMul ℝ (HermitianMat n 𝕜)
```

**`HermitianMat.lin`**, a def, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L453).

> The continuous linear map associated with a Hermitian matrix.

```lean
noncomputable def lin : EuclideanSpace 𝕜 n →L[𝕜] EuclideanSpace 𝕜 n
```

**`HermitianMat.isSymmetric`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L458).

```lean
lemma isSymmetric : A.lin.IsSymmetric
```

**`HermitianMat.lin_zero`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L462).

```lean
lemma lin_zero : (0 : HermitianMat n 𝕜).lin = 0
```

**`HermitianMat.lin_one`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L466).

```lean
lemma lin_one : (1 : HermitianMat n 𝕜).lin = 1
```

**`HermitianMat.eigenspace`**, a def, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L469).

```lean
noncomputable def eigenspace (μ : 𝕜) : Submodule 𝕜 (EuclideanSpace 𝕜 n)
```

**`HermitianMat.ker`**, a def, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L474).

> The kernel of a Hermitian matrix `A` as a submodule of Euclidean space, defined by
> `LinearMap.ker A.toMat.toEuclideanLin`. Equivalently, the zero-eigenspace.

```lean
noncomputable def ker : Submodule 𝕜 (EuclideanSpace 𝕜 n)
```

**`HermitianMat.mem_ker_iff_mulVec_zero`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L477).

```lean
lemma mem_ker_iff_mulVec_zero (x : EuclideanSpace 𝕜 n) : x ∈ A.ker ↔ A.mat.mulVec x = 0
```

**`HermitianMat.ker_eq_eigenspace_zero`**, a theorem, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L481). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The kernel of a Hermitian matrix is its zero eigenspace.

```lean
theorem ker_eq_eigenspace_zero : A.ker = A.eigenspace 0
```

**`HermitianMat.ker_zero`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L486).

```lean
lemma ker_zero : (0 : HermitianMat n 𝕜).ker = ⊤
```

**`HermitianMat.ker_one`**, a lemma, [line 490](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L490).

```lean
lemma ker_one : (1 : HermitianMat n 𝕜).ker = ⊥
```

**`HermitianMat.ker_pos_smul`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L493).

```lean
lemma ker_pos_smul {c : ℝ} (hc : c ≠ 0) : (c • A).ker = A.ker
```

**`HermitianMat.support`**, a def, [line 499](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L499).

> The support of a Hermitian matrix `A` as a submodule of Euclidean space, defined by
> `LinearMap.range A.toMat.toEuclideanLin`. Equivalently, the sum of all nonzero eigenspaces.

```lean
noncomputable def support : Submodule 𝕜 (EuclideanSpace 𝕜 n)
```

**`HermitianMat.support_eq_sup_eigenspace_nonzero`**, a theorem, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L503). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The support of a Hermitian matrix is the sum of its nonzero eigenspaces.

```lean
theorem support_eq_sup_eigenspace_nonzero : A.support = ⨆ μ ≠ 0, A.eigenspace μ
```

**`HermitianMat.support_zero`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L507).

```lean
lemma support_zero : (0 : HermitianMat n 𝕜).support = ⊥
```

**`HermitianMat.support_one`**, a lemma, [line 511](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L511).

```lean
lemma support_one : (1 : HermitianMat n 𝕜).support = ⊤
```

**`HermitianMat.ker_orthogonal_eq_support`**, a lemma, [line 515](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L515).

```lean
lemma ker_orthogonal_eq_support : A.kerᗮ = A.support
```

**`HermitianMat.support_orthogonal_eq_range`**, a lemma, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L521).

```lean
lemma support_orthogonal_eq_range : A.supportᗮ = A.ker
```

**`HermitianMat.diagonal`**, a def, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L533).

```lean
def diagonal (f : n → ℝ) : HermitianMat n 𝕜
```

**`HermitianMat.diagonal_mat`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L540).

```lean
lemma diagonal_mat : (diagonal 𝕜 f).mat = Matrix.diagonal (f · : n → 𝕜)
```

**`HermitianMat.diagonal_zero`**, a lemma, [line 544](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L544).

```lean
lemma diagonal_zero : (diagonal 𝕜 0) = (0 : HermitianMat n 𝕜)
```

**`HermitianMat.diagonal_eq_zero`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L548).

```lean
lemma diagonal_eq_zero {f : n → ℝ} : diagonal 𝕜 f = 0 ↔ f = 0
```

**`HermitianMat.diagonal_one`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L552).

```lean
lemma diagonal_one : (diagonal 𝕜 1) = (1 : HermitianMat n 𝕜)
```

**`HermitianMat.diagonal_eq_one`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L556).

```lean
lemma diagonal_eq_one {f : n → ℝ} : diagonal 𝕜 f = 1 ↔ f = 1
```

**`HermitianMat.diagonal_add`**, a lemma, [line 559](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L559).

```lean
lemma diagonal_add : diagonal 𝕜 (f + g) = diagonal 𝕜 f + diagonal 𝕜 g
```

**`HermitianMat.diagonal_add_apply`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L562).

```lean
lemma diagonal_add_apply : diagonal 𝕜 (fun x ↦ f x + g x) = diagonal 𝕜 f + diagonal 𝕜 g
```

**`HermitianMat.diagonal_sub`**, a lemma, [line 565](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L565).

```lean
lemma diagonal_sub : diagonal 𝕜 (f - g) = diagonal 𝕜 f - diagonal 𝕜 g
```

**`HermitianMat.diagonal_mul`**, a lemma, [line 568](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L568).

```lean
lemma diagonal_mul (c : ℝ) : diagonal 𝕜 (fun x ↦ c * f x) = c • diagonal 𝕜 f
```

**`HermitianMat.diagonal_conj_diagonal`**, a lemma, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L572).

```lean
lemma diagonal_conj_diagonal [Fintype n] :
    (diagonal 𝕜 f).conj (diagonal 𝕜 g) = diagonal 𝕜 (fun i ↦ f i * (g i)^2)
```

**`HermitianMat.eq_conj_diagonal`**, a lemma, [line 582](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L582).

> A Hermitian matrix is equal to its diagonalization conjugated by its eigenvector unitary matrix.

```lean
lemma eq_conj_diagonal [Fintype n] (A : HermitianMat n 𝕜) :
    A = (diagonal 𝕜 A.H.eigenvalues).conj A.H.eigenvectorUnitary
```

**`HermitianMat.kronecker`**, a def, [line 596](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L596).

> The kronecker product of two HermitianMats, see `Matrix.kroneckerMap`.

```lean
def kronecker (A : HermitianMat m α) (B : HermitianMat n α) : HermitianMat (m × n) α
```

**`HermitianMat.kronecker_mat`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L604).

```lean
lemma kronecker_mat (A : HermitianMat m α) (B : HermitianMat n α) :
    (A ⊗ₖ B).mat = A.mat ⊗ₖ B.mat
```

**`HermitianMat.zero_kronecker`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L609).

```lean
lemma zero_kronecker (A : HermitianMat m α) : (0 : HermitianMat n α) ⊗ₖ A = 0
```

**`HermitianMat.kronecker_zero`**, a lemma, [line 613](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L613).

```lean
lemma kronecker_zero (A : HermitianMat m α) : A ⊗ₖ (0 : HermitianMat n α) = 0
```

**`HermitianMat.kronecker_one_one`**, a lemma, [line 618](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L618).

```lean
lemma kronecker_one_one : (1 : HermitianMat m α) ⊗ₖ (1 : HermitianMat n α) = 1
```

**`HermitianMat.add_kronecker`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L622).

```lean
lemma add_kronecker : (A + B) ⊗ₖ C = A ⊗ₖ C + B ⊗ₖ C
```

**`HermitianMat.kronecker_add`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L626).

```lean
lemma kronecker_add : A ⊗ₖ (B + C) = A ⊗ₖ B + A ⊗ₖ C
```

**`HermitianMat.kronecker_diagonal`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L629).

```lean
lemma kronecker_diagonal [DecidableEq m] [DecidableEq n] (d₁ : m → ℝ) (d₂ : n → ℝ) :
    (diagonal 𝕜 d₁ ⊗ₖ diagonal 𝕜 d₂) = diagonal 𝕜 (fun (i : m × n) => d₁ i.1 * d₂ i.2)
```

**`HermitianMat.kron_commute`**, a theorem, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L640). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A ⊗ₖ B always commutes with C ⊗ₖ D if the pairs commute.

```lean
theorem kron_commute [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    {A C : HermitianMat m α} {B D : HermitianMat n α}
    (hAC : Commute A.mat C.mat) (hBD : Commute B.mat D.mat):
    Commute (A ⊗ₖ B).mat (C ⊗ₖ D).mat
```

**`HermitianMat.kron_id_commute_id_kro`**, a theorem, [line 651](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L651). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A ⊗ₖ 1 always commutes with 1 ⊗ₖ B

```lean
theorem kron_id_commute_id_kro [Fintype m] [Fintype n] [DecidableEq m] [DecidableEq n]
    (A : HermitianMat m α) (B : HermitianMat n α) :
    Commute (A ⊗ₖ (1 : HermitianMat n α)).mat ((1 : HermitianMat m α) ⊗ₖ B).mat
```

**`HermitianMat.kronecker_conj`**, a lemma, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L659).

```lean
lemma kronecker_conj [Fintype m] [Fintype n]
    (A : HermitianMat m α) (B : HermitianMat n α) (C : Matrix p m α) (D : Matrix q n α) :
    (A ⊗ₖ B).conj (C ⊗ₖ D) = (A.conj C) ⊗ₖ (B.conj D)
```

**`HermitianMat.range_le_ker_imp_zero`**, a lemma, [line 674](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L674).

```lean
lemma range_le_ker_imp_zero {A : HermitianMat d 𝕜}
    (h : LinearMap.range A.mat.toEuclideanLin ≤ LinearMap.ker A.mat.toEuclideanLin) : A = 0
```

**`Matrix.range_mul_conjTranspose_of_ker_le_ker`**, a theorem, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L703). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> If ker M ⊆ ker A, then range (A Mᴴ) = range A.

```lean
theorem _root_.Matrix.range_mul_conjTranspose_of_ker_le_ker {A : Matrix d d 𝕜} {M : Matrix d₂ d 𝕜}
    (h : LinearMap.ker M.toEuclideanLin ≤ LinearMap.ker A.toEuclideanLin) :
    LinearMap.range (A * M.conjTranspose).toEuclideanLin = LinearMap.range A.toEuclideanLin
```

**`HermitianMat.conj_ne_zero`**, a lemma, [line 744](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L744).

```lean
lemma conj_ne_zero {A : HermitianMat d 𝕜} {M : Matrix d₂ d 𝕜} (hA : A ≠ 0)
    (h : LinearMap.ker M.toEuclideanLin ≤ A.ker) : A.conj M ≠ 0
```

**`HermitianMat.conj_ne_zero_iff`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L756).

```lean
lemma conj_ne_zero_iff {A : HermitianMat d 𝕜} {M : Matrix d₂ d 𝕜}
    (h : LinearMap.ker M.toEuclideanLin ≤ A.ker) : A.conj M ≠ 0 ↔ A ≠ 0
```

**`Matrix.IsHermitian.spectrum_rcLike`**, a lemma, [line 765](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L765).

```lean
lemma _root_.Matrix.IsHermitian.spectrum_rcLike {A : Matrix n n 𝕜} (hA : A.IsHermitian) :
    RCLike.ofReal '' spectrum ℝ A = spectrum 𝕜 A
```

**`HermitianMat.spectrum_rcLike`**, a theorem, [line 772](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L772). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> We fix a simp-normal form that, for HermitianMat, we always work in terms
> of the real spectrum.

```lean
theorem spectrum_rcLike (A : HermitianMat n 𝕜) :
    spectrum 𝕜 A.mat = RCLike.ofReal '' spectrum ℝ A.mat
```

**`HermitianMat.ne_zero_iff_ne_zero_spectrum`**, a lemma, [line 776](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L776).

```lean
lemma ne_zero_iff_ne_zero_spectrum (A : HermitianMat n 𝕜) :
    A ≠ 0 ↔ ∃ x ∈ spectrum ℝ A.mat, x ≠ 0
```

**`HermitianMat.spectrum_prod`**, a lemma, [line 792](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L792).

```lean
lemma spectrum_prod
  {A : HermitianMat m 𝕜} {B : HermitianMat n 𝕜} :
    spectrum ℝ (A ⊗ₖ B).mat = spectrum ℝ A.mat * spectrum ℝ B.mat
```

**An instance with no name**, [line 800](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean#L800).

```lean
noncomputable instance : AddCommMonoid (HermitianMat d ℂ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Continuous linear maps](../continuouslinearmap.md)
- [QuantumInfo.ForMathlib.Matrix](../matrix.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Basic.lean)
