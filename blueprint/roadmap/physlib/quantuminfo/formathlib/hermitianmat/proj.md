---
declaration: module
origin: cited
lean: HermitianMat.projector_eq_sum_rankOne, HermitianMat.posPart_eq_posPart_toMat, HermitianMat.negPart_eq_negPart_toMat, HermitianMat.posPart_eq_cfc_lt, HermitianMat.negPart_eq_cfc_lt, HermitianMat.nonneg_iff_inner_nonneg, HermitianMat.projector, HermitianMat.projector_add_orthogonal
statement: formalized
proof: formalized
---

# Projectors associated to Hermitian matrices

The module `QuantumInfo.ForMathlib.HermitianMat.Proj`, [QuantumInfo/ForMathlib/HermitianMat/Proj.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean): 64 declarations (2 instances with no name), 14 with a docstring, 6 listed as significant.

> * `projector`: The `HermitianMat` that projects onto a given submodule
>  * `supportProj`: The `HermitianMat` that projects onto the range (nonzero eigenvalues)
>  * `kerProj`: The `HermitianMat` that projects onto the kernel
>  * `projLE`: With notation `{A ≤ₚ B}`, `projLE A B` is the projector onto the nonnegative
>    eigenspace of `B - A`.
>  * `projLT`: With notation `{A <ₚ B}`, `projLT A B` is the projector onto the positive
>    eigenspace of `B - A`.
>  * Positive and negative part, written `A⁺` and `A⁻`, give the restriction of a HermitianMat
>    onto its positive (resp. negative) eigenvalues; equivalently, it's nonnegative (resp.
>    nonpositive) eigenvalues.

**`HermitianMat.projector`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L46).

> Given a Submodule (EuclideanSpace ...) to HermitianMat, this gives the projector onto that subspace,
> i.e. a matrix that squares to itself, preserves vectors in the submodule, and zeroes out anything
> in the orthogonal complement of that submodule.

```lean
noncomputable def projector (S : Submodule 𝕜 (EuclideanSpace 𝕜 n)) : HermitianMat n 𝕜
```

**`HermitianMat.projector_add_orthogonal`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L54).

```lean
lemma projector_add_orthogonal : projector S + projector Sᗮ = 1
```

**`HermitianMat.projector_nonneg`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L60).

```lean
lemma projector_nonneg : 0 ≤ projector S
```

**`HermitianMat.projector_ker`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L71).

```lean
lemma projector_ker : (projector S).ker = Sᗮ
```

**`HermitianMat.trace_projector`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L82).

```lean
lemma trace_projector : (projector S).trace = (Module.finrank 𝕜 S : ℝ)
```

**`HermitianMat.supportProj`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L95).

> The `HermitianMat.projector` for the `HermitianMat.support` submodule.

```lean
noncomputable def supportProj (A : HermitianMat n 𝕜) : HermitianMat n 𝕜
```

**`HermitianMat.kerProj`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L100).

> The `HermitianMat.projector` for the `HermitianMat.ker` submodule.

```lean
noncomputable def kerProj (A : HermitianMat n 𝕜) : HermitianMat n 𝕜
```

**`HermitianMat.supportProj_ker`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L103).

```lean
lemma supportProj_ker : A.supportProj.ker = A.ker
```

**`HermitianMat.kerProj_ker`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L107).

```lean
lemma kerProj_ker : A.kerProj.ker = A.support
```

**`HermitianMat.kerProj_add_supportProj`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L111).

```lean
lemma kerProj_add_supportProj : A.kerProj + A.supportProj = 1
```

**`HermitianMat.kerProj_of_nonSingular`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L115).

```lean
lemma kerProj_of_nonSingular [NonSingular A] : A.kerProj = 0
```

**`HermitianMat.supportProj_of_nonSingular`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L120).

```lean
lemma supportProj_of_nonSingular [NonSingular A] : A.supportProj = 1
```

**`HermitianMat.projector_eq_sum_rankOne`**, a theorem, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L126). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The projector onto a submodule S is the sum of the outer products of the vectors in an orthonormal basis of S.

```lean
theorem projector_eq_sum_rankOne (b : OrthonormalBasis ι 𝕜 S) :
    (projector S).mat = ∑ i, Matrix.vecMulVec (S.subtype (b i)) (star (S.subtype (b i)))
```

**`HermitianMat.projector_support_eq_sum`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L146).

> The projector onto the support of A is the sum of the projections onto the eigenvectors with non-zero eigenvalues.

```lean
lemma projector_support_eq_sum : A.supportProj.mat =
    ∑ i, (if A.H.eigenvalues i = 0 then 0 else 1) •
      Matrix.vecMulVec (A.H.eigenvectorBasis i) (star (A.H.eigenvectorBasis i))
```

**`HermitianMat.supportProj_eq_cfc`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L200).

```lean
lemma supportProj_eq_cfc : A.supportProj = A.cfc (if · = 0 then 0 else 1)
```

**`HermitianMat.projLE`**, a def, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L214).

> Projector onto the non-negative eigenspace of `B - A`. Accessible by the notation
> `{A ≤ₚ B}`, which is scoped to `HermitianMat`. This is the unique maximum operator `P`
> such that `P^2 = P` and `P * A * P ≤ P * B * P` in the Loewner order.

```lean
def projLE (A B : HermitianMat n 𝕜) : HermitianMat n 𝕜
```

**`HermitianMat.projLT`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L219).

> Projector onto the positive eigenspace of `B - A`. Accessible by the notation
> `{A <ₚ B}`, which is scoped to `HermitianMat`. Compare with `proj_le`.

```lean
noncomputable def projLT (A B : HermitianMat n 𝕜) : HermitianMat n 𝕜
```

**`HermitianMat.projLE_def`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L232).

```lean
lemma projLE_def : {A ≤ₚ B} = (B - A).cfc (fun x ↦ if 0 ≤ x then 1 else 0)
```

**`HermitianMat.projLT_def`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L235).

```lean
lemma projLT_def : {A <ₚ B} = (B - A).cfc (fun x ↦ if 0 < x then 1 else 0)
```

**`HermitianMat.projLE_sq`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L238).

```lean
lemma projLE_sq : {A ≤ₚ B}^2 = {A ≤ₚ B}
```

**`HermitianMat.projLT_sq`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L243).

```lean
lemma projLT_sq : {A <ₚ B}^2 = {A <ₚ B}
```

**`HermitianMat.projLE_zero_cfc`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L248).

```lean
lemma projLE_zero_cfc : {0 ≤ₚ A} = A.cfc (fun x ↦ if 0 ≤ x then 1 else 0)
```

**`HermitianMat.projLT_zero_cfc`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L251).

```lean
lemma projLT_zero_cfc : {0 <ₚ A} = A.cfc (fun x ↦ if 0 < x then 1 else 0)
```

**`HermitianMat.projLE_zero_cfc'`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L254).

```lean
lemma projLE_zero_cfc' : {A ≤ₚ 0} = A.cfc (fun x ↦ if x ≤ 0 then 1 else 0)
```

**`HermitianMat.projLT_zero_cfc'`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L262).

```lean
lemma projLT_zero_cfc' : {A <ₚ 0} = A.cfc (fun x ↦ if x < 0 then 1 else 0)
```

**`HermitianMat.projLE_nonneg`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L270).

```lean
lemma projLE_nonneg : 0 ≤ {A ≤ₚ B}
```

**`HermitianMat.projLT_nonneg`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L275).

```lean
lemma projLT_nonneg : 0 ≤ {A <ₚ B}
```

**`HermitianMat.projLE_le_one`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L281).

```lean
lemma projLE_le_one : {A ≤ₚ B} ≤ 1
```

**`HermitianMat.projLE_mul_nonneg`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L290).

```lean
lemma projLE_mul_nonneg : 0 ≤ {A ≤ₚ B}.mat * (B - A).mat
```

**`HermitianMat.projLE_mul_le`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L298).

```lean
lemma projLE_mul_le : {A ≤ₚ B}.mat * A.mat ≤ {A ≤ₚ B}.mat * B.mat
```

**`HermitianMat.proj_le_add_lt`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L303).

```lean
lemma proj_le_add_lt : {A <ₚ B} + {B ≤ₚ A} = 1
```

**`HermitianMat.conj_lt_add_conj_le`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L312).

```lean
lemma conj_lt_add_conj_le : A.conj {A <ₚ 0} + A.conj {0 ≤ₚ A} = A
```

**`HermitianMat.supportProj_eq_proj_lt_add_proj_lt`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L322).

```lean
lemma supportProj_eq_proj_lt_add_proj_lt (A : HermitianMat n 𝕜) :
    A.supportProj = {A <ₚ 0} + {0 <ₚ A}
```

**An instance with no name**, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L329).

> The positive part of a Hermitian matrix: the projection onto its positive eigenvalues.

```lean
instance : PosPart (HermitianMat n 𝕜)
```

**An instance with no name**, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L333).

> The negative part of a Hermitian matrix: the projection onto its negative eigenvalues.

```lean
instance : NegPart (HermitianMat n 𝕜)
```

**`HermitianMat.posPart_eq_cfc_max`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L336).

```lean
lemma posPart_eq_cfc_max : A⁺ = A.cfc (fun x ↦ x ⊔ 0)
```

**`HermitianMat.negPart_eq_cfc_min`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L339).

```lean
lemma negPart_eq_cfc_min : A⁻ = A.cfc (fun x ↦ -x ⊔ 0)
```

**`HermitianMat.posPart_eq_cfc_ite`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L342).

```lean
lemma posPart_eq_cfc_ite : A⁺ = A.cfc (fun x ↦ if 0 ≤ x then x else 0)
```

**`HermitianMat.negPart_eq_cfc_ite`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L345).

```lean
lemma negPart_eq_cfc_ite : A⁻ = A.cfc (fun x ↦ if x ≤ 0 then -x else 0)
```

**`HermitianMat.posPart_eq_posPart_toMat`**, a theorem, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L352). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> There is an existing (very slow) `PosPart` instance on `Matrix n n 𝕜`, this shows
> that this is equal.

```lean
theorem posPart_eq_posPart_toMat : A⁺ = A.mat⁺
```

**`HermitianMat.negPart_eq_negPart_toMat`**, a theorem, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L358). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> There is an existing (very slow) `PosPart` instance on `Matrix n n 𝕜`, this shows
> that this is equal.

```lean
theorem negPart_eq_negPart_toMat : A⁻ = A.mat⁻
```

**`HermitianMat.posPart_eq_cfc_lt`**, a theorem, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L363). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The positive part can be equivalently described as the nonnegative part.

```lean
theorem posPart_eq_cfc_lt : A⁺ = A.cfc (fun x ↦ if 0 < x then x else 0)
```

**`HermitianMat.negPart_eq_cfc_lt`**, a theorem, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L369). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The negative part can be equivalently described as the nonpositive part.

```lean
theorem negPart_eq_cfc_lt : A⁻ = A.cfc (fun x ↦ if x < 0 then -x else 0)
```

**`HermitianMat.posPart_add_negPart`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L374).

```lean
lemma posPart_add_negPart : A⁺ - A⁻ = A
```

**`HermitianMat.posPart_eq_self`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L379).

```lean
lemma posPart_eq_self {A : HermitianMat n 𝕜} (hA : 0 ≤ A) :
    A⁺ = A
```

**`HermitianMat.posPart_nonneg`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L385).

```lean
lemma posPart_nonneg : 0 ≤ A⁺
```

**`HermitianMat.negPart_nonneg`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L389).

```lean
lemma negPart_nonneg : 0 ≤ A⁻
```

**`HermitianMat.posPart_le`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L393).

```lean
lemma posPart_le : A ≤ A⁺
```

**`HermitianMat.posPart_mul_negPart`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L398).

```lean
lemma posPart_mul_negPart : A⁺.mat * A⁻.mat = 0
```

**`HermitianMat.projLE_inner_nonneg`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L406).

```lean
lemma projLE_inner_nonneg  : 0 ≤ ⟪{A ≤ₚ B}, (B - A)⟫
```

**`HermitianMat.projLE_inner_le`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L410).

```lean
lemma projLE_inner_le : ⟪{A ≤ₚ B}, A⟫ ≤ ⟪{A ≤ₚ B}, B⟫
```

**`HermitianMat.inner_projLE_nonneg`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L415).

```lean
lemma inner_projLE_nonneg : 0 ≤ ⟪{A ≤ₚ B}, (B - A)⟫
```

**`HermitianMat.inner_projLE_le`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L419).

```lean
lemma inner_projLE_le : ⟪{A ≤ₚ B}, A⟫ ≤ ⟪{A ≤ₚ B}, B⟫
```

**`HermitianMat.posPart_Continuous`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L424).

```lean
lemma posPart_Continuous : Continuous (·⁺ : HermitianMat n ℂ → _)
```

**`HermitianMat.negPart_Continuous`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L429).

```lean
lemma negPart_Continuous : Continuous (·⁻ : HermitianMat n ℂ → _)
```

**`HermitianMat.one_sub_projLT`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L449).

```lean
lemma one_sub_projLT : 1 - {B ≤ₚ A} = {A <ₚ B}
```

**`HermitianMat.projLT_mul_nonneg`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L453).

```lean
lemma projLT_mul_nonneg : 0 ≤ {A <ₚ B}.mat * (B - A).mat
```

**`HermitianMat.proj_lt_mul_lt`**, a lemma, [line 463](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L463).

```lean
lemma proj_lt_mul_lt : {A <ₚ B}.mat * A.mat ≤ {A <ₚ B}.mat * B.mat
```

**`HermitianMat.inner_negPart_nonpos`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L467).

```lean
lemma inner_negPart_nonpos : ⟪A, A⁻⟫ ≤ 0
```

**`HermitianMat.posPart_inner_negPart_zero`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L484).

```lean
lemma posPart_inner_negPart_zero : ⟪A⁺, A⁻⟫ = 0
```

**`HermitianMat.inner_negPart_zero_iff`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L489).

```lean
lemma inner_negPart_zero_iff : ⟪A, A⁻⟫ = 0 ↔ 0 ≤ A
```

**`HermitianMat.posPart_eq_zero_iff`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L507).

```lean
lemma posPart_eq_zero_iff : A⁺ = 0 ↔ A ≤ 0
```

**`HermitianMat.inner_negPart_neg_iff`**, a lemma, [line 525](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L525).

```lean
lemma inner_negPart_neg_iff : ⟪A, A⁻⟫ < 0 ↔ ¬0 ≤ A
```

**`HermitianMat.nonneg_iff_inner_nonneg`**, a theorem, [line 530](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean#L530). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The self-duality of the PSD cone: a matrix is PSD iff its inner product with all
> nonnegative matrices is non-negative.

```lean
theorem nonneg_iff_inner_nonneg (A : HermitianMat n 𝕜) :
    0 ≤ A ↔ ∀ B, 0 ≤ B → 0 ≤ ⟪A, B⟫
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.CFC](cfc.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Proj.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Proj.lean)
