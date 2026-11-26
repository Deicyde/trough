---
declaration: module
origin: cited
lean: GlobalGaugeGroup.truncationKer, GlobalGaugeGroup.mem_truncationKer_zero_iff_evalGaugeJet, GlobalGaugeGroup.adjointCoeff_eq_zero_of_mem_truncationKer, GlobalGaugeGroup.adjointDualCoeff_eq_zero_of_mem_truncationKer, GlobalGaugeGroup.adjointCoeff_mul_of_mem_truncationKer_right, GlobalGaugeGroup.adjointCoeff_conj_of_mem_truncationKer, GlobalGaugeGroup.evalLie_iteratedDerivJ_adjoint_conj_of_mem_truncationKer, GlobalGaugeGroup.truncationKer_normal
statement: formalized
proof: formalized
---

# The truncation filtration of the jet gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.Truncation`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean): 28 declarations, 26 with a docstring.

> The normal subgroups of gauge jets that are trivial up to a given order.

## i. Overview

> A jet of gauge transformations is *trivial to order `n`* when it agrees with the identity up to and
> including its `n`-th derivatives. For a matrix group this is a statement about Taylor coefficients
> of matrix entries. It is phrased here through two things given at the base point, the value
> `G.evalGaugeJet U` and the Maurer–Cartan form: `U` is trivial to order `n` when
> `G.evalGaugeJet U = 1` and the base-point Taylor coefficients of `ω_μ(U)` vanish below order
> `n`. The Taylor–Leibniz theorem makes these jets a subgroup `truncationKer n`, normal in
> `G.gaugeJetGroup`, and the subgroups decrease with `n`.
>
> The zeroth member, the *pure jets* with `G.evalGaugeJet U = 1`, is the complement of the constant
> jets. Every jet factors uniquely as a pure jet times the constant jet of its value,
> `truncationProjZero` and `eq_truncationProjZero_mul_ofConstant`. A pure jet is determined by its
> Maurer–Cartan form, and hence by the base-point values of the symmetrized Maurer–Cartan form,
> `symmetrizedMaurerCartanCoeff`. Membership in `truncationKer n` is exactly the vanishing of those
> symmetrized data up to order `n`.
>
> What a jet trivial to order `n` does to the fields is the point of the filtration: all its
> adjoint Taylor coefficients of order between `1` and `n` vanish,
> `adjointCoeff_eq_zero_of_mem_truncationKer`, so it acts on the gauge-field symbols with at
> most `n` derivatives by a pure translation.

## ii. Key results

> - `GlobalGaugeGroup.truncationKer` : the jets trivial to order `n`, as a subgroup.
> - `GlobalGaugeGroup.mem_truncationKer_zero_iff_evalGaugeJet` : the pure jets.
> - `GlobalGaugeGroup.adjointCoeff_eq_zero_of_mem_truncationKer` : deep jets kill the positive
>   adjoint coefficients.
> - `GlobalGaugeGroup.truncationKer_normal` : the filtration is by normal subgroups.
> - `GlobalGaugeGroup.truncationProjZero` : the projection of a jet onto the pure jets.
> - `GlobalGaugeGroup.maurerCartan_injOn_truncationKer_zero` : a pure jet is determined by its
>   Maurer–Cartan form.
> - `GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_injective` : and by its symmetrized
>   Maurer–Cartan data.
> - `GlobalGaugeGroup.mem_truncationKer_iff_symmetrizedMaurerCartanCoeff_eq_zero` : the
>   filtration through the symmetrized data.
> - `GlobalGaugeGroup.radial` : the radial component `−∑_μ x_μ ω_μ` of the Maurer–Cartan form,
>   whose Taylor data are the symmetrized data.
> - `GlobalGaugeGroup.exists_radial_eq` : radial integrability, which with the realisation of
>   Taylor data makes the symmetrized data free coordinates on the pure jets,
>   `GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_bijective`.
> - `GlobalGaugeGroup.truncation` : the `n`-th truncation of a gauge jet, a matrix of
>   polynomials.
> - `GlobalGaugeGroup.truncation_eq_one_of_mem_truncationKer` : jets trivial to order `n`
>   truncate to the identity.

## iv. References

> * None.

## A. The truncation filtration

**`GlobalGaugeGroup.truncationKer`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L95).

> The jets trivial to order `n`, with value the identity and with the base-point Taylor
> coefficients of the Maurer–Cartan form vanishing below order `n`. Closure under products and
> inverses is the cocycle law together with the Taylor–Leibniz theorem for the adjoint action.

```lean
noncomputable def truncationKer (n : ℕ) : Subgroup G.gaugeJetGroup
```

**`GlobalGaugeGroup.mem_truncationKer_zero_iff_evalGaugeJet`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L114).

> The zeroth truncation kernel is the group of pure jets, those with identity value.

```lean
lemma mem_truncationKer_zero_iff_evalGaugeJet {U : G.gaugeJetGroup} : U ∈ G.truncationKer 0 ↔
    G.evalGaugeJet U = 1
```

## B. The adjoint coefficients of a deep jet

**`GlobalGaugeGroup.adjointCoeff_eq_zero_of_mem_truncationKer`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L127).

> Deep jets kill the positive adjoint coefficients. For a jet trivial to order `n`, the
> adjoint coefficients of order between `1` and `n` vanish. One derivative of the adjoint
> is `ad` of the Maurer–Cartan form, whose base-point data vanish below order `n`.

```lean
lemma adjointCoeff_eq_zero_of_mem_truncationKer {n : ℕ} {U : G.gaugeJetGroup}
    (hU : U ∈ G.truncationKer n)
    {x : Multiset (Fin 1 ⊕ Fin 3)} (hx : x ≠ 0) (hxn : x.card ≤ n) :
    G.adjointCoeff U x = 0
```

**`GlobalGaugeGroup.adjointDualCoeff_eq_zero_of_mem_truncationKer`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L140).

> The dual form of `adjointCoeff_eq_zero_of_mem_truncationKer`.

```lean
lemma adjointDualCoeff_eq_zero_of_mem_truncationKer {n : ℕ} {U : G.gaugeJetGroup}
    (hU : U ∈ G.truncationKer n) {x : Multiset (Fin 1 ⊕ Fin 3)} (hx : x ≠ 0)
    (hxn : x.card ≤ n) : G.adjointDualCoeff U x = 0
```

**`GlobalGaugeGroup.adjointCoeff_mul_of_mem_truncationKer_right`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L147).

> Up to order `n`, a jet trivial to order `n` is invisible on the right of a product.

```lean
lemma adjointCoeff_mul_of_mem_truncationKer_right (g : G.gaugeJetGroup) {n : ℕ}
    {U : G.gaugeJetGroup}
    (hU : U ∈ G.truncationKer n) {x : Multiset (Fin 1 ⊕ Fin 3)} (hxn : x.card ≤ n) :
    G.adjointCoeff (g * U) x = G.adjointCoeff g x
```

**`GlobalGaugeGroup.adjointCoeff_conj_of_mem_truncationKer`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L159).

> Up to order `n`, a conjugate of a jet trivial to order `n` has the adjoint
> coefficients of the identity.

```lean
lemma adjointCoeff_conj_of_mem_truncationKer (g : G.gaugeJetGroup) {n : ℕ} {U : G.gaugeJetGroup}
    (hU : U ∈ G.truncationKer n) {x : Multiset (Fin 1 ⊕ Fin 3)} (hxn : x.card ≤ n) :
    G.adjointCoeff (g * U * g⁻¹) x = G.adjointCoeff 1 x
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_adjoint_conj_of_mem_truncationKer`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L169).

> Up to order `n`, a conjugate of a jet trivial to order `n` acts trivially on the
> base-point Taylor data of the jet Lie algebra.

```lean
lemma evalLie_iteratedDerivJ_adjoint_conj_of_mem_truncationKer (g : G.gaugeJetGroup) {n : ℕ}
    {U : G.gaugeJetGroup}
    (hU : U ∈ G.truncationKer n) {s : Multiset (Fin 1 ⊕ Fin 3)} (hs : s.card ≤ n)
    (Y : G.jetLieSubalgebra) : G.evalLie
      (G.iteratedDerivJ s (G.adjointJ (g * U * g⁻¹) Y)) =
      G.evalLie (G.iteratedDerivJ s Y)
```

## C. Normality

**`GlobalGaugeGroup.truncationKer_normal`**, an instance, [line 191](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L191).

> The truncation kernels are normal subgroups, since conjugating a jet trivial to order `n`
> gives a jet trivial to order `n`.

```lean
instance truncationKer_normal (n : ℕ) : (G.truncationKer n).Normal
```

## D. The projection onto the pure jets

**`GlobalGaugeGroup.truncationProjZero`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L209).

> The projection `U ↦ U · (U₀)⁻¹` of a jet onto the pure jets, stripping its value.
> This is not a group homomorphism. It is the cocycle of the splitting of `G.gaugeJetGroup` by
> the constant jets.

```lean
noncomputable def truncationProjZero (U : G.gaugeJetGroup) : G.truncationKer 0
```

**`GlobalGaugeGroup.coe_truncationProjZero`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L214).

```lean
lemma coe_truncationProjZero (U : G.gaugeJetGroup) :
    (G.truncationProjZero U : G.gaugeJetGroup) = U *
      (G.gaugeJetOfConstant (G.evalGaugeJet U))⁻¹
```

**`GlobalGaugeGroup.eq_truncationProjZero_mul_ofConstant`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L219).

> Every jet is its pure part times the constant jet of its value.

```lean
lemma eq_truncationProjZero_mul_ofConstant (U : G.gaugeJetGroup) :
    U = G.truncationProjZero U * G.gaugeJetOfConstant (G.evalGaugeJet U)
```

## E. Pure jets and their Maurer–Cartan data

**`GlobalGaugeGroup.symmetrizedMaurerCartanCoeff`**, a def, [line 232](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L232).

> The symmetrized Maurer–Cartan data of a pure jet, the base-point values of its
> symmetrized Maurer–Cartan forms, indexed by nonempty multisets of directions. Total
> symmetry is automatic from the multiset indexing.

```lean
noncomputable def symmetrizedMaurerCartanCoeff (U : G.truncationKer 0)
    (r : {r : Multiset (Fin 1 ⊕ Fin 3) // r ≠ 0}) : G.lieSubalgebra
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_apply`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L236).

```lean
lemma symmetrizedMaurerCartanCoeff_apply (U : G.truncationKer 0)
    (r : {r : Multiset (Fin 1 ⊕ Fin 3) // r ≠ 0}) :
    G.symmetrizedMaurerCartanCoeff U r =
      G.evalLie (G.symmetrizedMaurerCartanForm U.1 r.1)
```

**`GlobalGaugeGroup.mem_truncationKer_of_symmetrizedMaurerCartanCoeff_eq_zero`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L244).

> Maurer–Cartan triangularity. A pure jet whose symmetrized Maurer–Cartan data vanish
> up to order `n` is trivial to order `n`. The symmetrized data control the Taylor data of
> the Maurer–Cartan form through the symmetrization defect.

```lean
lemma mem_truncationKer_of_symmetrizedMaurerCartanCoeff_eq_zero (U : G.truncationKer 0)
    (n : ℕ) (h : ∀ (r : Multiset (Fin 1 ⊕ Fin 3)) (hr : r ≠ 0), r.card ≤ n →
      G.symmetrizedMaurerCartanCoeff U ⟨r, hr⟩ = 0) :
    U.1 ∈ G.truncationKer n
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_eq_zero_of_mem_truncationKer`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L256).

> Conversely, the symmetrized Maurer–Cartan data of a jet trivial to order `n` vanish
> up to order `n`, since each term of the symmetrized form carries fewer than `n`
> derivatives.

```lean
lemma symmetrizedMaurerCartanCoeff_eq_zero_of_mem_truncationKer {U : G.truncationKer 0}
    {n : ℕ} (hU : U.1 ∈ G.truncationKer n) {r : Multiset (Fin 1 ⊕ Fin 3)} (hr : r ≠ 0)
    (hrn : r.card ≤ n) : G.symmetrizedMaurerCartanCoeff U ⟨r, hr⟩ = 0
```

**`GlobalGaugeGroup.mem_truncationKer_iff_symmetrizedMaurerCartanCoeff_eq_zero`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L272).

> The truncation filtration through the symmetrized Maurer–Cartan data. A pure jet is
> trivial to order `n` exactly when its symmetrized data vanish up to order `n`.

```lean
lemma mem_truncationKer_iff_symmetrizedMaurerCartanCoeff_eq_zero (U : G.truncationKer 0)
    (n : ℕ) : U.1 ∈ G.truncationKer n ↔
      ∀ (r : Multiset (Fin 1 ⊕ Fin 3)) (hr : r ≠ 0), r.card ≤ n →
        G.symmetrizedMaurerCartanCoeff U ⟨r, hr⟩ = 0
```

**`GlobalGaugeGroup.maurerCartan_injOn_truncationKer_zero`**, a lemma, [line 282](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L282).

> A pure jet is determined by its Maurer–Cartan form. By the
> cocycle and inverse laws `ω(V⁻¹ U) = Ad_{V⁻¹}(ω(U) − ω(V)) = 0`, so `V⁻¹ U` is the
> constant jet of its value, which is the identity.

```lean
lemma maurerCartan_injOn_truncationKer_zero {U V : G.gaugeJetGroup} (hU : U ∈ G.truncationKer 0)
    (hV : V ∈ G.truncationKer 0) (h : G.maurerCartan U = G.maurerCartan V) :
    U = V
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_injective`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L298).

> A pure jet is determined by its symmetrized Maurer–Cartan data. The symmetrized data determine
> all base-point Taylor data of the Maurer–Cartan form
> (`evalLie_iteratedDerivJ_maurerCartan_eq_of_symmetrized_eq_all`), hence the form
> itself by Taylor determinacy, hence the jet by `maurerCartan_injOn_truncationKer_zero`.

```lean
lemma symmetrizedMaurerCartanCoeff_injective :
    Function.Injective G.symmetrizedMaurerCartanCoeff
```

## F. The radial component of the Maurer–Cartan form

> The symmetrized Maurer–Cartan data of a pure jet are, up to the normalization by the
> order, the base-point Taylor data of a single element of `G.jetLieSubalgebra`, the radial
> component `ρ(U) = −∑_μ x_μ ω_μ(U)` of the Maurer–Cartan form. This is the Euler identity applied
> to each summand.

**`GlobalGaugeGroup.radial`**, a def, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L328).

> The radial component `−∑_μ x_μ ω_μ(U)` of the Maurer–Cartan form of a jet. It collects the
> Maurer–Cartan forms in all directions into a single Lie algebra jet, whose base-point Taylor
> data are the symmetrized Maurer–Cartan data. A pure jet is reconstructed from its
> Maurer–Cartan form by solving the radial system for this jet, and `exists_radial_eq` shows
> that every Lie algebra jet vanishing at the base point arises this way.

```lean
noncomputable def radial (U : G.gaugeJetGroup) : G.jetLieSubalgebra
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_eq_evalLie_iteratedDeriv_radial`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L333).

> The symmetrized Maurer–Cartan data are the Taylor data of the radial component,
> `sym(ω(U))_r|₀ = (1/|r|) (∂_r ρ(U))|₀`.

```lean
lemma symmetrizedMaurerCartanCoeff_eq_evalLie_iteratedDeriv_radial (U : G.truncationKer 0)
    (r : {r : Multiset (Fin 1 ⊕ Fin 3) // r ≠ 0}) :
    G.symmetrizedMaurerCartanCoeff U r =
      (1 / (r.1.card : ℝ)) • G.evalLie
        (G.iteratedDerivJ r.1 (G.radial U.1))
```

## G. Radial integrability

> Every Lie algebra jet vanishing at the base point is the radial component of the
> Maurer–Cartan form of a pure jet, the jet `U` solving `E U = −A U` with `U(0) = 1`, from
> `GlobalGaugeGroup.exists_sum_X_smul_maurerCartan_eq`. With the realisation of Taylor data,
> `GlobalGaugeGroup.exists_evalLie_iteratedDerivJ_eq`, this makes the symmetrized Maurer–Cartan
> data free coordinates on the pure jets.

**`GlobalGaugeGroup.radial_val`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L362).

> The radial component `−∑_μ x_μ ω_μ` of the Maurer–Cartan form of a gauge jet, as a matrix,
> `−∑_μ x_μ (∂_μ U) U⁻¹`.

```lean
lemma radial_val (U : G.gaugeJetGroup) :
    (G.radial U).1 =
      ∑ μ, (X μ : SpaceTimeAlgebra) • -((U.1 : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) *
        (U.1⁻¹).1)
```

**`GlobalGaugeGroup.exists_radial_eq`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L371).

> Every Lie algebra jet vanishing at the base point is the radial component of the
> Maurer–Cartan form of a pure jet.

```lean
lemma exists_radial_eq {A : G.jetLieSubalgebra} (hA : G.evalLie A = 0) :
    ∃ U : G.truncationKer 0, G.radial U.1 = A
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_surjective`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L385).

> Every family of symmetrized Maurer–Cartan data is realized by a pure jet. Realize the
> data, rescaled by the order, as the Taylor data of an element `ρ` vanishing at the base
> point, and integrate `ρ` to a pure jet.

```lean
lemma symmetrizedMaurerCartanCoeff_surjective :
    Function.Surjective G.symmetrizedMaurerCartanCoeff
```

**`GlobalGaugeGroup.symmetrizedMaurerCartanCoeff_bijective`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L399).

> The symmetrized Maurer–Cartan data are free coordinates on the pure jets.

```lean
lemma symmetrizedMaurerCartanCoeff_bijective :
    Function.Bijective G.symmetrizedMaurerCartanCoeff
```

## H. Truncation of a gauge jet

> Truncating a gauge jet at order `n` sets to zero, in every matrix entry, the Taylor
> coefficients of total degree above `n`. This is a plain function into matrices, not a
> homomorphism, since deleting the coefficients above order `n` breaks multiplicativity
> between orders `n + 1` and `2n`. A jet trivial to order `n` in the sense of `truncationKer`
> truncates to the identity, by the Euler vanishing principle applied to
> `∂_ρ U = ω_ρ(U) U`.

**`GlobalGaugeGroup.truncation`**, a def, [line 418](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L418).

> The `n`-th truncation of a gauge jet, entrywise, all Taylor coefficients of total degree
> greater than `n` are set to zero.

```lean
noncomputable def truncation (n : ℕ) (U : G.gaugeJetGroup) : Matrix κ κ SpaceTimeAlgebra
```

**`GlobalGaugeGroup.truncation_one`**, a lemma, [line 423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L423).

> Truncation of the identity jet is the identity matrix.

```lean
lemma truncation_one (n : ℕ) : G.truncation n 1 = 1
```

**`GlobalGaugeGroup.coeff_maurerCartan_eq_zero_of_mem_truncationKer`**, a lemma, [line 428](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L428).

> The base-point Taylor coefficients of the Maurer–Cartan form of a jet trivial to order
> `n` vanish below degree `n`.

```lean
lemma coeff_maurerCartan_eq_zero_of_mem_truncationKer {n : ℕ} {U : G.gaugeJetGroup}
    (hU : U ∈ G.truncationKer n) (ρ : Fin 1 ⊕ Fin 3) {m : (Fin 1 ⊕ Fin 3) →₀ ℕ}
    (hm : Finsupp.degree m < n) (i j : κ) :
    coeff m ((G.maurerCartan U ρ : Matrix κ κ SpaceTimeAlgebra) i j) = 0
```

**`GlobalGaugeGroup.truncation_eq_one_of_mem_truncationKer`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean#L446).

> A jet trivial to order `n` in the sense of the truncation filtration truncates to the
> identity at order `n`. The radial relation `∂_ρ U = ω_ρ(U) U` and the Euler vanishing
> principle propagate the vanishing of the Maurer–Cartan coefficients below degree `n` to
> the vanishing of the coefficients of `U` in nonzero degree up to `n`.

```lean
lemma truncation_eq_one_of_mem_truncationKer {n : ℕ} {U : G.gaugeJetGroup}
    (hU : U ∈ G.truncationKer n) : G.truncation n U = 1
```

## Depends on

- [The Taylor coefficients of the adjoint action](globalgaugegroup-adjointcoeff.md)
- [The symmetrized Maurer–Cartan form of a global gauge group](globalgaugegroup-symmetrizedmaurercartan.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/Truncation.lean)
