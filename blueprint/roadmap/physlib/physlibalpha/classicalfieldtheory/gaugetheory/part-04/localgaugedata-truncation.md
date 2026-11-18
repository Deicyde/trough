---
declaration: module
origin: cited
lean: LocalGaugeData.truncationKer, LocalGaugeData.mem_truncationKer_zero_iff, LocalGaugeData.adjointCoeff_eq_zero_of_mem_truncationKer, LocalGaugeData.adjointDualCoeff_eq_zero_of_mem_truncationKer, LocalGaugeData.adjointCoeff_mul_of_mem_truncationKer_right, LocalGaugeData.adjointCoeff_conj_of_mem_truncationKer, LocalGaugeData.evalLie_iteratedDeriv_adjoint_conj_of_mem_truncationKer, LocalGaugeData.maurerCartan_conj
statement: formalized
proof: formalized
---

# The truncation filtration of the jet gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.Truncation`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean): 29 declarations, 26 with a docstring.

## i. Overview

> A jet of gauge transformations is *trivial to order `n`* when it agrees with the identity
> up to and including its `n`-th derivatives. For a matrix group this is a statement about
> Taylor coefficients of matrix entries; for an abstract package `jets` it is phrased through
> the two things the package provides at the base point, the value `eval U` and the
> Maurer–Cartan form: `U` is trivial to order `n` when `eval U = 1` and the base-point Taylor
> coefficients of `ω_μ(U)` vanish below order `n`. The Taylor–Leibniz theorem makes these
> jets a subgroup `truncationKer n`, normal in `GJ`, and the subgroups decrease with `n`.
>
> The zeroth member, the *pure jets* with `eval U = 1`, is the complement of the constant
> jets: every jet factors uniquely as a pure jet times the constant jet of its value,
> `truncationProjZero`. When the package is `Faithful`, a pure jet is determined by its
> Maurer–Cartan form, and hence by the base-point values of the symmetrized Maurer–Cartan
> form, `symmetrizedMaurerCartanCoeff`; and membership in `truncationKer n` is exactly the
> vanishing of those symmetrized data up to order `n`.
>
> What a jet trivial to order `n` does to the fields is the point of the filtration: all its
> adjoint Taylor coefficients of order between `1` and `n` vanish,
> `adjointCoeff_eq_zero_of_mem_truncationKer`, so it acts on the gauge-field symbols with at
> most `n` derivatives by a pure translation.

## ii. Key results

> - `LocalGaugeData.truncationKer` : the jets trivial to order `n`, as a subgroup.
> - `LocalGaugeData.mem_truncationKer_zero_iff` : the pure jets.
> - `LocalGaugeData.adjointCoeff_eq_zero_of_mem_truncationKer` : deep jets kill the positive
>   adjoint coefficients.
> - `LocalGaugeData.truncationKer_normal` : the filtration is by normal subgroups.
> - `LocalGaugeData.truncationProjZero` : the projection of a jet onto the pure jets.
> - `LocalGaugeData.maurerCartan_injOn_truncationKer_zero` : a pure jet of a faithful package
>   is determined by its Maurer–Cartan form.
> - `LocalGaugeData.symmetrizedMaurerCartanCoeff_injective` : and by its symmetrized
>   Maurer–Cartan data.
> - `LocalGaugeData.mem_truncationKer_iff_symmetrizedMaurerCartanCoeff_eq_zero` : the
>   filtration through the symmetrized data.
> - `LocalGaugeData.radial` : the radial component `∑_μ x_μ ω_μ` of the Maurer–Cartan form,
>   whose Taylor data are the symmetrized data.
> - `LocalGaugeData.Free` : Taylor completeness and radial integrability, which make the
>   symmetrized data free coordinates on the pure jets,
>   `LocalGaugeData.symmetrizedMaurerCartanCoeff_surjective`.

## iv. References

> * None.

## A. The truncation filtration

**`LocalGaugeData.truncationKer`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L88).

> The jets trivial to order `n`: value the identity, and base-point Taylor coefficients
> of the Maurer–Cartan form vanishing below order `n`. Closure under products and inverses
> is the cocycle law together with the Taylor–Leibniz theorem for the adjoint action.

```lean
noncomputable def truncationKer (n : ℕ) : Subgroup GJ
```

**`LocalGaugeData.mem_truncationKer_zero_iff`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L106).

> The zeroth truncation kernel is the group of pure jets, those with identity value.

```lean
lemma mem_truncationKer_zero_iff {U : GJ} : U ∈ jets.truncationKer 0 ↔ jets.eval U = 1
```

## B. The adjoint coefficients of a deep jet

**`LocalGaugeData.adjointCoeff_eq_zero_of_mem_truncationKer`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L118).

> Deep jets kill the positive adjoint coefficients: for a jet trivial to order `n`, the
> adjoint coefficients of order between `1` and `n` vanish. One derivative of the adjoint
> is `ad` of the Maurer–Cartan form, whose base-point data vanish below order `n`.

```lean
lemma adjointCoeff_eq_zero_of_mem_truncationKer {n : ℕ} {U : GJ} (hU : U ∈ jets.truncationKer n)
    {x : Multiset (Fin 1 ⊕ Fin 3)} (hx : x ≠ 0) (hxn : x.card ≤ n) :
    jets.adjointCoeff U x = 0
```

**`LocalGaugeData.adjointDualCoeff_eq_zero_of_mem_truncationKer`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L130).

> The dual form of `adjointCoeff_eq_zero_of_mem_truncationKer`.

```lean
lemma adjointDualCoeff_eq_zero_of_mem_truncationKer {n : ℕ} {U : GJ}
    (hU : U ∈ jets.truncationKer n) {x : Multiset (Fin 1 ⊕ Fin 3)} (hx : x ≠ 0)
    (hxn : x.card ≤ n) : jets.adjointDualCoeff U x = 0
```

**`LocalGaugeData.adjointCoeff_mul_of_mem_truncationKer_right`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L137).

> Up to order `n`, a jet trivial to order `n` is invisible on the right of a product.

```lean
lemma adjointCoeff_mul_of_mem_truncationKer_right (g : GJ) {n : ℕ} {U : GJ}
    (hU : U ∈ jets.truncationKer n) {x : Multiset (Fin 1 ⊕ Fin 3)} (hxn : x.card ≤ n) :
    jets.adjointCoeff (g * U) x = jets.adjointCoeff g x
```

**`LocalGaugeData.adjointCoeff_conj_of_mem_truncationKer`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L148).

> Up to order `n`, a conjugate of a jet trivial to order `n` has the adjoint
> coefficients of the identity.

```lean
lemma adjointCoeff_conj_of_mem_truncationKer (g : GJ) {n : ℕ} {U : GJ}
    (hU : U ∈ jets.truncationKer n) {x : Multiset (Fin 1 ⊕ Fin 3)} (hxn : x.card ≤ n) :
    jets.adjointCoeff (g * U * g⁻¹) x = jets.adjointCoeff 1 x
```

**`LocalGaugeData.evalLie_iteratedDeriv_adjoint_conj_of_mem_truncationKer`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L158).

> Up to order `n`, a conjugate of a jet trivial to order `n` acts trivially on the
> base-point Taylor data of the jet Lie algebra.

```lean
lemma evalLie_iteratedDeriv_adjoint_conj_of_mem_truncationKer (g : GJ) {n : ℕ} {U : GJ}
    (hU : U ∈ jets.truncationKer n) {s : Multiset (Fin 1 ⊕ Fin 3)} (hs : s.card ≤ n)
    (Y : 𝔤J) : jets.evalLie (jets.iteratedDeriv s (jets.adjointJ (g * U * g⁻¹) Y)) =
      jets.evalLie (jets.iteratedDeriv s Y)
```

## C. Normality

**`LocalGaugeData.maurerCartan_conj`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L178).

> The Maurer–Cartan form of a conjugate, by the cocycle law: the conjugating jet
> contributes its own form and its transport by the conjugate.

```lean
lemma maurerCartan_conj (g U : GJ) (μ : Fin 1 ⊕ Fin 3) :
    jets.maurerCartan (g * U * g⁻¹) μ =
      jets.maurerCartan g μ + jets.adjointJ g (jets.maurerCartan U μ)
        - jets.adjointJ (g * U * g⁻¹) (jets.maurerCartan g μ)
```

**`LocalGaugeData.truncationKer_normal`**, an instance, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L187).

> The truncation kernels are normal subgroups: conjugating a jet trivial to order `n`
> gives a jet trivial to order `n`.

```lean
instance truncationKer_normal (n : ℕ) : (jets.truncationKer n).Normal
```

## D. The projection onto the pure jets

**`LocalGaugeData.truncationProjZero`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L205).

> The projection of a jet onto the pure jets, stripping its value: `U ↦ U · (U₀)⁻¹`.
> This is not a group homomorphism; it is the cocycle of the splitting of `GJ` by the
> constant jets.

```lean
noncomputable def truncationProjZero (U : GJ) : jets.truncationKer 0
```

**`LocalGaugeData.coe_truncationProjZero`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L210).

```lean
lemma coe_truncationProjZero (U : GJ) :
    (jets.truncationProjZero U : GJ) = U * (jets.ofConstant (jets.eval U))⁻¹
```

**`LocalGaugeData.eq_truncationProjZero_mul_ofConstant`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L214).

> Every jet is its pure part times the constant jet of its value.

```lean
lemma eq_truncationProjZero_mul_ofConstant (U : GJ) :
    U = jets.truncationProjZero U * jets.ofConstant (jets.eval U)
```

**`LocalGaugeData.truncationProjZero_eq_one_iff`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L219).

> The pure part of a jet is trivial exactly when the jet is constant.

```lean
lemma truncationProjZero_eq_one_iff {U : GJ} :
    jets.truncationProjZero U = 1 ↔ U = jets.ofConstant (jets.eval U)
```

**`LocalGaugeData.truncationProjZero_ofConstant`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L224).

```lean
lemma truncationProjZero_ofConstant (g : G₀) :
    jets.truncationProjZero (jets.ofConstant g) = 1
```

**`LocalGaugeData.maurerCartan_truncationProjZero`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L230).

> Stripping the value of a jet does not change its Maurer–Cartan form: by the cocycle
> law, right multiplication by a constant jet drops out.

```lean
lemma maurerCartan_truncationProjZero (U : GJ) (μ : Fin 1 ⊕ Fin 3) :
    jets.maurerCartan (jets.truncationProjZero U) μ = jets.maurerCartan U μ
```

## E. Pure jets and their Maurer–Cartan data

**`LocalGaugeData.symmetrizedMaurerCartanCoeff`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L244).

> The symmetrized Maurer–Cartan data of a pure jet: the base-point values of its
> symmetrized Maurer–Cartan forms, indexed by nonempty multisets of directions. Total
> symmetry is automatic from the multiset indexing.

```lean
noncomputable def symmetrizedMaurerCartanCoeff (U : jets.truncationKer 0)
    (r : {r : Multiset (Fin 1 ⊕ Fin 3) // r ≠ 0}) : 𝔤
```

**`LocalGaugeData.symmetrizedMaurerCartanCoeff_apply`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L248).

```lean
lemma symmetrizedMaurerCartanCoeff_apply (U : jets.truncationKer 0)
    (r : {r : Multiset (Fin 1 ⊕ Fin 3) // r ≠ 0}) :
    jets.symmetrizedMaurerCartanCoeff U r =
      jets.evalLie (jets.symmetrizedMaurerCartanForm U.1 r.1)
```

**`LocalGaugeData.mem_truncationKer_of_symmetrizedMaurerCartanCoeff_eq_zero`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L256).

> Maurer–Cartan triangularity: a pure jet whose symmetrized Maurer–Cartan data vanish
> up to order `n` is trivial to order `n`. The symmetrized data control the Taylor data of
> the Maurer–Cartan form through the symmetrization defect.

```lean
lemma mem_truncationKer_of_symmetrizedMaurerCartanCoeff_eq_zero (U : jets.truncationKer 0)
    (n : ℕ) (h : ∀ (r : Multiset (Fin 1 ⊕ Fin 3)) (hr : r ≠ 0), r.card ≤ n →
      jets.symmetrizedMaurerCartanCoeff U ⟨r, hr⟩ = 0) :
    U.1 ∈ jets.truncationKer n
```

**`LocalGaugeData.symmetrizedMaurerCartanCoeff_eq_zero_of_mem_truncationKer`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L265).

> Conversely, the symmetrized Maurer–Cartan data of a jet trivial to order `n` vanish
> up to order `n`: each term of the symmetrized form carries fewer than `n` derivatives.

```lean
lemma symmetrizedMaurerCartanCoeff_eq_zero_of_mem_truncationKer {U : jets.truncationKer 0}
    {n : ℕ} (hU : U.1 ∈ jets.truncationKer n) {r : Multiset (Fin 1 ⊕ Fin 3)} (hr : r ≠ 0)
    (hrn : r.card ≤ n) : jets.symmetrizedMaurerCartanCoeff U ⟨r, hr⟩ = 0
```

**`LocalGaugeData.mem_truncationKer_iff_symmetrizedMaurerCartanCoeff_eq_zero`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L279).

> The truncation filtration through the symmetrized Maurer–Cartan data: a pure jet is
> trivial to order `n` exactly when its symmetrized data vanish up to order `n`.

```lean
lemma mem_truncationKer_iff_symmetrizedMaurerCartanCoeff_eq_zero (U : jets.truncationKer 0)
    (n : ℕ) : U.1 ∈ jets.truncationKer n ↔
      ∀ (r : Multiset (Fin 1 ⊕ Fin 3)) (hr : r ≠ 0), r.card ≤ n →
        jets.symmetrizedMaurerCartanCoeff U ⟨r, hr⟩ = 0
```

**`LocalGaugeData.maurerCartan_injOn_truncationKer_zero`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L293).

> A pure jet of a faithful package is determined by its Maurer–Cartan form. By the
> cocycle and inverse laws `ω(V⁻¹ U) = Ad_{V⁻¹}(ω(U) − ω(V)) = 0`, so `V⁻¹ U` is the
> constant jet of its value, which is the identity.

```lean
lemma maurerCartan_injOn_truncationKer_zero {U V : GJ} (hU : U ∈ jets.truncationKer 0)
    (hV : V ∈ jets.truncationKer 0) (h : jets.maurerCartan U = jets.maurerCartan V) :
    U = V
```

**`LocalGaugeData.symmetrizedMaurerCartanCoeff_injective`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L308).

> A pure jet of a faithful package is determined by its symmetrized Maurer–Cartan data.
> The symmetrized data determine all base-point Taylor data of the Maurer–Cartan form
> (`evalLie_iteratedDeriv_maurerCartan_eq_of_symmetrized_eq_all`), hence the form itself by
> Taylor determinacy, hence the jet by `maurerCartan_injOn_truncationKer_zero`.

```lean
lemma symmetrizedMaurerCartanCoeff_injective :
    Function.Injective jets.symmetrizedMaurerCartanCoeff
```

## F. The radial component of the Maurer–Cartan form

> The symmetrized Maurer–Cartan data of a pure jet are, up to the normalization by the
> order, the base-point Taylor data of a single element of `𝔤J`: the radial component
> `ρ(U) = ∑_μ x_μ ω_μ(U)` of the Maurer–Cartan form. This is the Euler identity applied
> to each summand.

**`LocalGaugeData.radial`**, a def, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L335).

> The radial component `∑_μ x_μ ω_μ(U)` of the Maurer–Cartan form of a jet.

```lean
noncomputable def radial (U : GJ) : 𝔤J
```

**`LocalGaugeData.symmetrizedMaurerCartanCoeff_eq_evalLie_iteratedDeriv_radial`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L340).

> The symmetrized Maurer–Cartan data are the Taylor data of the radial component:
> `sym(ω(U))_r|₀ = (1/|r|) (∂_r ρ(U))|₀`.

```lean
lemma symmetrizedMaurerCartanCoeff_eq_evalLie_iteratedDeriv_radial (U : jets.truncationKer 0)
    (r : {r : Multiset (Fin 1 ⊕ Fin 3) // r ≠ 0}) :
    jets.symmetrizedMaurerCartanCoeff U r =
      (1 / (r.1.card : ℝ)) • jets.evalLie (jets.iteratedDeriv r.1 (jets.radial U.1))
```

## G. Free packages

**`LocalGaugeData.Free`**, a class, [line 369](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L369).

> A package is free when it is faithful and its jets are honest formal power series in
> the coordinates: every family of base-point Taylor data is realized by an element of
> `𝔤J` (Taylor completeness), and every element vanishing at the base point is the radial
> component of the Maurer–Cartan form of a pure jet (radial integrability, the solution of
> the Euler equation `∑_μ x_μ ∂_μ U = −i ρ U` with `U(0) = 1`). Both hold for the full jet
> group of any matrix group. Freeness makes the symmetrized Maurer–Cartan data free
> coordinates on the pure jets, `symmetrizedMaurerCartanCoeff_bijective`; like `Faithful`
> it is recorded separately from the structure because the covariance theory does not
> need it, only the classification of invariants does.

```lean
class Free (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) : Prop extends Faithful jets where
  exists_evalLie_iteratedDeriv_eq : ∀ c : Multiset (Fin 1 ⊕ Fin 3) → 𝔤,
    ∃ Y : 𝔤J, ∀ s, jets.evalLie (jets.iteratedDeriv s Y) = c s
  exists_radial_eq : ∀ ρ : 𝔤J, jets.evalLie ρ = 0 → ∃ U : jets.truncationKer 0, jets.radial U.1 = ρ
```

**`LocalGaugeData.exists_evalLie_iteratedDeriv_eq`**, a lemma, [line 379](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L379).

> Taylor completeness of a free package.

```lean
lemma exists_evalLie_iteratedDeriv_eq (c : Multiset (Fin 1 ⊕ Fin 3) → 𝔤) :
    ∃ Y : 𝔤J, ∀ s, jets.evalLie (jets.iteratedDeriv s Y) = c s
```

**`LocalGaugeData.exists_radial_eq`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L384).

> Radial integrability of a free package.

```lean
lemma exists_radial_eq {ρ : 𝔤J} (hρ : jets.evalLie ρ = 0) :
    ∃ U : jets.truncationKer 0, jets.radial U.1 = ρ
```

**`LocalGaugeData.symmetrizedMaurerCartanCoeff_surjective`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L391).

> Every family of symmetrized Maurer–Cartan data is realized by a pure jet: realize the
> data, rescaled by the order, as the Taylor data of an element `ρ` vanishing at the base
> point, and integrate `ρ` to a pure jet.

```lean
lemma symmetrizedMaurerCartanCoeff_surjective :
    Function.Surjective jets.symmetrizedMaurerCartanCoeff
```

**`LocalGaugeData.symmetrizedMaurerCartanCoeff_bijective`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean#L406).

> The symmetrized Maurer–Cartan data are free coordinates on the pure jets of a free
> package.

```lean
lemma symmetrizedMaurerCartanCoeff_bijective :
    Function.Bijective jets.symmetrizedMaurerCartanCoeff
```

## Depends on

- [The Taylor coefficients of the adjoint action](localgaugedata-adjointcoeff.md)
- [The Maurer–Cartan form of a local gauge data package](localgaugedata-maurercartan.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/Truncation.lean)
