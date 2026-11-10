---
declaration: section
origin: cited
lean: StacksDraft.Perfect.hasFiniteTotalCohomology_iff_isCompactObject, Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.hasFiniteTotalTwistCohomology_of_hasFiniteTotalTensorCohomology, Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.tfae_isBoundedCoherent, Stacks.AlgebraicGeometry.ProperSupportCoherent.cardinalSum_rank_ext_lt_aleph0, Stacks.AlgebraicGeometry.ProperSupportCoherent.cardinalSum_rank_ext_lt_aleph0_general, Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterization.cardinalSum_rank_ext_lt_aleph0_of_derivedCategoryBBounded, Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterization.hasFiniteTotalExt_of_derivedCategoryBBounded, Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterizationConverse.derivedCategoryBBounded_of_hasFiniteTotalExt
statement: formalized
proof: formalized
---

# 57.5 Characterizing coherent modules

Section 57.5 of the Stacks Project, [Tag 0FY9](https://stacks.math.columbia.edu/tag/0FY9). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FYA, a lemma

[Tag 0FYA](https://stacks.math.columbia.edu/tag/0FYA) in the Stacks Project.

**`StacksDraft.Perfect.hasFiniteTotalCohomology_iff_isCompactObject`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BeilinsonAlgebra.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Perfect/BeilinsonAlgebra.lean#L1180).

> **Stacks Project, Tag 0FYA.** An object of the derived category of right
> modules over the Beilinson algebra has finite-dimensional total cohomology if
> and only if it is compact.

```lean
lemma hasFiniteTotalCohomology_iff_isCompactObject
    (k : Type u) [Field k] (n : ℕ)
    (K : DerivedCategory (ModuleCat.{v} (beilinsonAlgebra k n)ᵐᵒᵖ)) :
    HasFiniteTotalCohomology (k := k) K ↔ IsCompactObject.{v} K
```

## Tag 0FYB, a lemma

[Tag 0FYB](https://stacks.math.columbia.edu/tag/0FYB) in the Stacks Project.

**`Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.hasFiniteTotalTwistCohomology_of_hasFiniteTotalTensorCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterization.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterization.lean#L300). The attribute's comment: “part (2) ⟹ part (4)”.

> **[Stacks, Tag 0FYB], (2) ⟹ (4).**  Let `k` be a field, let `n ≥ 0` and let `K` be an object
> of `D(𝒪_{ℙⁿ_k})`.  If `∑_{i ∈ ℤ} dim_k H^i(ℙⁿ_k, E ⊗^𝐋 K)` is finite for every perfect object
> `E`, then `∑_{i ∈ ℤ} dim_k H^i(ℙⁿ_k, K ⊗^𝐋 𝒪(d))` is finite for `d = 0, 1, …, n`.
>
> The source's proof is *"this is immediate, as `𝒪(d)` is a perfect object"*: apply the hypothesis
> at `E = 𝒪(d)[0]`, which is perfect by
> `Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.isPerfect_singleFunctor_twistOver`,
> and move the twist past `K` with the commutativity constraint of the derived tensor product
> ([Stacks, Tag 0FPT]).  No condition on `d` beyond the source's `0 ≤ d ≤ n` is used, and the
> conclusion holds for every `d ∈ ℤ`; it is stated for `d = 0, …, n` because that is the source's
> condition (4).

```lean
theorem hasFiniteTotalTwistCohomology_of_hasFiniteTotalTensorCohomology
    (k : Type u) [Field k] (n : ℕ)
    (K : DerivedCategory (projectiveSpaceOverRing n (CommRingCat.of k)).Modules)
    (hK : HasFiniteTotalTensorCohomology k n K) :
    HasFiniteTotalTwistCohomology k n K
```

**`Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.tfae_isBoundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterizationTFAE.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterizationTFAE.lean#L369).

> **[Stacks, Tag 0FYB].** Let `k` be a field, let `n ≥ 0` and let `K` be an object of
> `D_QCoh(𝒪_{ℙⁿ_k})`, that is, an object of `D(𝒪_{ℙⁿ_k})` whose cohomology sheaves are
> quasi-coherent. The following are equivalent:
>
> 1. `K` is in `D^b_{Coh}(𝒪_{ℙⁿ_k})`;
> 2. `∑_{i ∈ ℤ} dim_k H^i(ℙⁿ_k, E ⊗^𝐋 K) < ∞` for each perfect object `E` of `D(𝒪_{ℙⁿ_k})`;
> 3. `∑_{i ∈ ℤ} dim_k Ext^i_{ℙⁿ_k}(E, K) < ∞` for each perfect object `E` of `D(𝒪_{ℙⁿ_k})`;
> 4. `∑_{i ∈ ℤ} dim_k H^i(ℙⁿ_k, K ⊗^𝐋 𝒪_{ℙⁿ_k}(d)) < ∞` for `d = 0, 1, …, n`.
>
> The four conditions are `IsBoundedCoherent`, `HasFiniteTotalTensorCohomology`,
> `HasFiniteTotalPerfectExt` and `HasFiniteTotalTwistCohomology`; a finite sum of dimensions over
> `k` is expressed as every term being a finite `k`-module and only finitely many being nonzero.
> See the module documentation for the argument.

```lean
theorem tfae_isBoundedCoherent
    (K : DerivedCategory (projectiveSpaceOverRing n (CommRingCat.of k)).Modules)
    (hqc : ∀ i, ((DerivedCategory.homologyFunctor _ i).obj K).IsQuasicoherent) :
    List.TFAE [IsBoundedCoherent k n K, HasFiniteTotalTensorCohomology k n K,
      HasFiniteTotalPerfectExt k n K, HasFiniteTotalTwistCohomology k n K]
```

## Tag 0FYC, a lemma

[Tag 0FYC](https://stacks.math.columbia.edu/tag/0FYC) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.cardinalSum_rank_ext_lt_aleph0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TotalExtDimensionOverAField.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TotalExtDimensionOverAField.lean#L210). The attribute's comment: “granted hExtFinite (substantive degrees of 0D0D) and the cited dual complex 08DQ”.

> **Stacks Project, Tag 0FYC.** Let `X` be a scheme proper over a field `k`, let `K` be an
> object of `D^b_Coh(𝒪_X)` and let `E` be a perfect object of `D(𝒪_X)`. Then
>
> `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞`,
>
> the dimensions being taken for the canonical `k`-structure induced by the structure morphism
> `X ⟶ Spec k`, the sum being the cardinal sum over all of `ℤ` and `< ∞` being `< ℵ₀`.
>
> The total sum is finite exactly when every summand is finite and only finitely many summands are
> nonzero. The second condition is `finite_setOf_not_subsingleton_ext_of_isPerfect`, proved from
> [Stacks, Tags 09M4 and 0FXU]. The first condition is the hypothesis `hExtFinite`: it is
> [Stacks, Tag 0D0D], now a theorem of this library as
> `Stacks.AlgebraicGeometry.ProperSupportCoherent.moduleFinite_ext_of_proper` of
> `StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/ExtFinitenessUnconditional.lean`, so this
> hypothesis is dischargeable; see the module documentation. The hypothesis `D` is the dual perfect
> complex of [Stacks, Tag 08DQ], carried as data because there is no absolute derived internal hom
> on `D(𝒪_X)` in this library.
>
> So what is proved is the tag's conclusion in full, the finiteness of the total sum, from the
> finiteness of the individual summands. Both named hypotheses stand for cited results and neither
> asserts the conclusion: `hExtFinite` is finiteness of each `Ext^i_X(E, K)` separately, which
> leaves the number of nonzero degrees unbounded and so does not imply finiteness of the sum.

```lean
theorem cardinalSum_rank_ext_lt_aleph0
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E)
    (D : Stacks.DerivedQCoh.DualPerfectComplexData X.left RΓ E)
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules => M.IsCoherent) K)
    (hExtFinite : ∀ n : ℤ, Module.Finite k (DerivedCategory.Ext E K n)) :
    Cardinal.sum (fun n : ℤ => Module.rank k (DerivedCategory.Ext E K n)) <
      Cardinal.aleph0
```

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.cardinalSum_rank_ext_lt_aleph0_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TotalExtDimensionOverAFieldGeneral.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TotalExtDimensionOverAFieldGeneral.lean#L96).

> **The total dimension of the Ext groups is finite.** Let `X` be a scheme proper over a field
> `k`, let `K` be an object of `D^b_Coh(𝒪_X)` and let `E` be a perfect object of `D(𝒪_X)`. Then
>
> `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞`,
>
> the dimensions being taken for the canonical `k`-structure induced by the structure morphism
> `X ⟶ Spec k`, the sum being the cardinal sum over all of `ℤ` and `< ∞` being `< ℵ₀`.

```lean
theorem cardinalSum_rank_ext_lt_aleph0_general
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E)
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules => M.IsCoherent) K) :
    Cardinal.sum (fun n : ℤ => Module.rank k (DerivedCategory.Ext E K n)) <
      Cardinal.aleph0
```

## Tag 0FYD, a lemma

[Tag 0FYD](https://stacks.math.columbia.edu/tag/0FYD) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterization.cardinalSum_rank_ext_lt_aleph0_of_derivedCategoryBBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterization.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterization.lean#L223). The attribute's comment: “(1) ⇒ (2) ONLY, for X proper over a field; the converse (2) ⇒ (1) is NOT proved. Granted 0FYC's own hExtFinite (0D0D) and DualPerfectComplexData (08DQ), quantified over E.”.

> **Stacks Project, Tag 0FYD, the implication (1) ⇒ (2).** Let `X` be a scheme proper over a
> field `k` and let `K` be an object of `D^b_Coh(𝒪_X)`. Then
>
> `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞`
>
> for every perfect object `E` of `D(𝒪_X)`, the dimensions being taken for the canonical
> `k`-structure induced by the structure morphism `X ⟶ Spec k`, the sum being the cardinal sum over
> all of `ℤ` and `< ∞` being `< ℵ₀`.
>
> **This is ONE DIRECTION of the equivalence of [Stacks, Tag 0FYD] and is therefore WEAKER THAN THE
> TAG.** The converse, (2) ⇒ (1), is not proved here and is not available in this library; the
> module docstring says which four results are missing, and no statement in this file permits the
> inference from finite total `Ext` to bounded coherent cohomology.
>
> The source proves this direction by [Stacks, Tag 0FYC], which is exactly what is applied, once
> for each perfect `E`. Its two hypotheses are inherited from it and are quantified over `E` here,
> 0FYD's condition (2) being a statement about every perfect object:
>
> * `hExtFinite`, finite-dimensionality over `k` of each `Ext^i_X(E, K)`, is [Stacks, Tag 0D0D], of
>   which this library carries only the degrees in which the `Ext` modules vanish; the substantive
>   degrees need the clause of [Stacks, Tag 0D0C] that is absent. It does not assert the
>   conclusion: finiteness of each summand leaves the number of nonzero degrees unbounded.
> * `D`, the dual perfect complex of [Stacks, Tag 08DQ], travels as data because there is no
>   absolute derived internal hom on `D(𝒪_X)` here.

```lean
theorem cardinalSum_rank_ext_lt_aleph0_of_derivedCategoryBBounded
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules => M.IsCoherent) K)
    (D : ∀ E : DerivedCategory X.left.Modules,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E →
        Stacks.DerivedQCoh.DualPerfectComplexData X.left RΓ E)
    (hExtFinite : ∀ E : DerivedCategory X.left.Modules,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E →
        ∀ n : ℤ, Module.Finite k (DerivedCategory.Ext E K n))
    (E : DerivedCategory X.left.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E) :
    Cardinal.sum (fun n : ℤ => Module.rank k (DerivedCategory.Ext E K n)) < Cardinal.aleph0
```

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterization.hasFiniteTotalExt_of_derivedCategoryBBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterization.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterization.lean#L252). The attribute's comment: “(1) ⇒ (2) ONLY, as HasFiniteTotalExt; the converse (2) ⇒ (1) is NOT proved. Granted 0FYC's own hExtFinite (0D0D) and DualPerfectComplexData (08DQ), quantified over E.”.

> **Stacks Project, Tag 0FYD, the implication (1) ⇒ (2), in the `HasFiniteTotalExt`
> spelling.** Let `X` be a scheme proper over a field `k` and let `K` be an object of
> `D^b_Coh(𝒪_X)`. Then `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K)` is finite for every perfect object `E` of
> `D(𝒪_X)`, in the conjunction form
> `Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.HasFiniteTotalExt` — condition (3) of
> [Stacks, Tag 0FYB] — which `cardinalSum_rank_ext_lt_aleph0_iff_hasFiniteTotalExt` shows is the
> same condition as the finiteness of the cardinal sum.
>
> **Like `cardinalSum_rank_ext_lt_aleph0_of_derivedCategoryBBounded`, this is ONE DIRECTION of the
> equivalence of [Stacks, Tag 0FYD] and is therefore WEAKER THAN THE TAG**; the hypotheses
> `hExtFinite` and `D` are inherited from [Stacks, Tag 0FYC], as described there.

```lean
theorem hasFiniteTotalExt_of_derivedCategoryBBounded
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules => M.IsCoherent) K)
    (D : ∀ E : DerivedCategory X.left.Modules,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E →
        Stacks.DerivedQCoh.DualPerfectComplexData X.left RΓ E)
    (hExtFinite : ∀ E : DerivedCategory X.left.Modules,
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E →
        ∀ n : ℤ, Module.Finite k (DerivedCategory.Ext E K n))
    (E : DerivedCategory X.left.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E) :
    BeilinsonCoherentCharacterization.HasFiniteTotalExt k X E K
```

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterizationConverse.derivedCategoryBBounded_of_hasFiniteTotalExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean#L69). The attribute's comment: “the implication (2) ⇒ (1), for X proper over a field and K in D_QCoh(O_X), with condition (2) as HasFiniteTotalExt; at the standard model, in the form 0FYH's h0FYD consumes”.

> **Stacks Project, Tag 0FYD, the implication (2) ⇒ (1).** Let `X` be a scheme proper over a
> field `k` and let `K ∈ D_QCoh(𝒪_X)` satisfy `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞` for every
> perfect `E`. Then `K ∈ D^b_Coh(𝒪_X)`.
>
> Stated at the standard model, exactly as the hypothesis `h0FYD` of
> `Stacks.AlgebraicGeometry.DerivedVarieties.Representability.exists_iso_linearYoneda_of_converse`
> ([Stacks, Tag 0FYH]) asks.

```lean
theorem derivedCategoryBBounded_of_hasFiniteTotalExt :
    ∀ K : @DerivedCategory X.left.Modules _ _ (HasDerivedCategory.standard X.left.Modules),
      @DerivedCategoryB.derivedCategoryB X.left.Modules _ _
        (HasDerivedCategory.standard X.left.Modules)
        (SheafOfModules.isQuasicoherent X.left.ringCatSheaf) K →
      (∀ E : @DerivedCategory X.left.Modules _ _ (HasDerivedCategory.standard X.left.Modules),
        @Stacks.Cohomology.PerfectComplexes.IsPerfect.{u, u, u + 1} X.left.toRingedSpace
          (HasDerivedCategory.standard X.left.Modules) E →
        BeilinsonCoherentCharacterization.HasFiniteTotalExt k X E K) →
      @DerivedCategoryB.derivedCategoryBBounded X.left.Modules _ _
        (HasDerivedCategory.standard X.left.Modules) (fun M : X.left.Modules => M.IsCoherent) K
```

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterizationConverse.derivedCategoryBBounded_iff_hasFiniteTotalExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean#L90). The attribute's comment: “both implications, for X proper over a field and K in D_QCoh(O_X), with condition (2) as HasFiniteTotalExt (each Ext^i finite-dimensional, finitely many nonzero)”.

> **Stacks Project, Tag 0FYD.** Let `X` be a scheme proper over a field `k` and let `K` be an
> object of `D_QCoh(𝒪_X)`. Then `K ∈ D^b_Coh(𝒪_X)` if and only if
> `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞` for every perfect object `E` of `D(𝒪_X)`; the finiteness is
> spelled `HasFiniteTotalExt`: every `Ext^i_X(E, K)` is finite-dimensional and only finitely many
> are nonzero.

```lean
theorem derivedCategoryBBounded_iff_hasFiniteTotalExt (K : DerivedCategory X.left.Modules)
    (hK : DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent X.left.ringCatSheaf) K) :
    DerivedCategoryB.derivedCategoryBBounded (fun M : X.left.Modules => M.IsCoherent) K ↔
      ∀ E : DerivedCategory X.left.Modules,
        Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E →
          BeilinsonCoherentCharacterization.HasFiniteTotalExt k X E K
```

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterizationConverse.derivedCategoryBBounded_iff_cardinalSum_rank_ext_lt_aleph0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean#L108). The attribute's comment: “both implications, for X proper over a field and K in D_QCoh(O_X), with condition (2) as the source's sum of dimensions, a cardinal sum below aleph0”.

> **Stacks Project, Tag 0FYD, in the source's form.** Let `X` be a scheme proper over a field `k`
> and let `K` be an object of `D_QCoh(𝒪_X)`. Then `K ∈ D^b_Coh(𝒪_X)` if and only if
> `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞` for every perfect object `E` of `D(𝒪_X)`, the dimensions
> being taken for the `k`-linear structure induced by `X ⟶ Spec k`.

```lean
theorem derivedCategoryBBounded_iff_cardinalSum_rank_ext_lt_aleph0
    (K : DerivedCategory X.left.Modules)
    (hK : DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent X.left.ringCatSheaf) K) :
    DerivedCategoryB.derivedCategoryBBounded (fun M : X.left.Modules => M.IsCoherent) K ↔
      ∀ E : DerivedCategory X.left.Modules,
        Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E →
          Cardinal.sum (fun n : ℤ => Module.rank k (DerivedCategory.Ext E K n)) <
            Cardinal.aleph0
```

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterization.cardinalSum_rank_ext_lt_aleph0_of_derivedCategoryBBounded'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationFiniteExt.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationFiniteExt.lean#L522). The attribute's comment: “the implication (1) ⇒ (2), for X proper over a field; no model of RΓ in the statement”.

> **Stacks Project, Tag 0FYD, the implication (1) ⇒ (2).** Let `X` be a scheme proper over a
> field `k` and let `K` be an object of `D^b_Coh(𝒪_X)`. Then
>
> `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞`
>
> for every perfect object `E` of `D(𝒪_X)`.
>
> The hypotheses are the source's and no others: `X` proper over the field `k`, and `K` bounded
> with coherent cohomology. In particular no model of derived global sections appears — this is
> `cardinalSum_rank_ext_lt_aleph0_of_derivedCategoryBBounded_of_model` at the canonical model
> `canonicalDerivedSections`, whose existence is instance search.

```lean
theorem cardinalSum_rank_ext_lt_aleph0_of_derivedCategoryBBounded'
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules => M.IsCoherent) K)
    (E : DerivedCategory X.left.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E) :
    Cardinal.sum (fun n : ℤ => Module.rank k (DerivedCategory.Ext E K n)) < Cardinal.aleph0
```

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterization.hasFiniteTotalExt_of_derivedCategoryBBounded'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationFiniteExt.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationFiniteExt.lean#L535). The attribute's comment: “the implication (1) ⇒ (2), as HasFiniteTotalExt, for X proper over a field; no model of RΓ in the statement”.

> **Stacks Project, Tag 0FYD, the implication (1) ⇒ (2), in the `HasFiniteTotalExt`
> spelling**, with no model of derived global sections in the statement.

```lean
theorem hasFiniteTotalExt_of_derivedCategoryBBounded'
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules => M.IsCoherent) K)
    (E : DerivedCategory X.left.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E) :
    BeilinsonCoherentCharacterization.HasFiniteTotalExt k X E K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.5, Tag 0FY9](https://stacks.math.columbia.edu/tag/0FY9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
