---
declaration: section
origin: cited
lean: StacksDraft.Perfect.hasFiniteTotalCohomology_iff_isCompactObject, Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.hasFiniteTotalTwistCohomology_of_hasFiniteTotalTensorCohomology, Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.tfae_isBoundedCoherent, Stacks.AlgebraicGeometry.ProperSupportCoherent.cardinalSum_rank_ext_lt_aleph0_of_isProper, Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterizationConverse.derivedCategoryBBounded_iff_cardinalSum_rank_ext_lt_aleph0
statement: formalized
proof: formalized
---

# 57.5 Characterizing coherent modules

Section 57.5 of the Stacks Project, [Tag 0FY9](https://stacks.math.columbia.edu/tag/0FY9). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FYA, a lemma

[Tag 0FYA](https://stacks.math.columbia.edu/tag/0FYA) in the Stacks Project.

**`StacksDraft.Perfect.hasFiniteTotalCohomology_iff_isCompactObject`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BeilinsonAlgebra.lean, line 1180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/BeilinsonAlgebra.lean#L1180).

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

**`Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.hasFiniteTotalTwistCohomology_of_hasFiniteTotalTensorCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterization.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterization.lean#L300). The attribute's comment: “part (2) ⟹ part (4)”.

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

**`Stacks.AlgebraicGeometry.BeilinsonCoherentCharacterization.tfae_isBoundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterizationTFAE.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/BeilinsonCoherentCharacterizationTFAE.lean#L369).

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

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.cardinalSum_rank_ext_lt_aleph0_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TotalExtDimensionOverAFieldGeneral.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/TotalExtDimensionOverAFieldGeneral.lean#L136).

> **Stacks Project, Tag 0FYC.** Let `X` be a scheme proper over a field `k`, let
> `K ∈ D^b_Coh(𝒪_X)` and let `E ∈ D(𝒪_X)` be perfect. Then
>
> `∑_{i ∈ ℤ} dim_k Ext^i_X(E, K) < ∞`,
>
> the dimensions being taken for the canonical `k`-structure induced by the structure morphism
> `X ⟶ Spec k`, the sum being the cardinal sum over all of `ℤ` and `< ∞` being `< ℵ₀`.
>
> The hypotheses are exactly those of the source. The derived global sections functor `RΓ(X, -)`
> used in the proof is the total right derived functor of global sections, which exists because
> `𝒪_X`-modules form a Grothendieck abelian category
> (`Stacks.Duality.hasRightDerivedFunctor_of_isGrothendieckAbelian`); the theorem is then
> `cardinalSum_rank_ext_lt_aleph0_general` at that functor.

```lean
theorem cardinalSum_rank_ext_lt_aleph0_of_isProper {k : Type u} [Field k]
    (X : Over (Spec (.of k))) [IsProper X.hom] (E K : DerivedCategory X.left.Modules)
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.left.toRingedSpace) E)
    (hK : DerivedCategoryB.derivedCategoryBBounded
      (fun M : X.left.Modules => M.IsCoherent) K) :
    Cardinal.sum (fun n : ℤ => Module.rank k (DerivedCategory.Ext E K n)) <
      Cardinal.aleph0
```

## Tag 0FYD, a lemma

[Tag 0FYD](https://stacks.math.columbia.edu/tag/0FYD) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.CoherentCharacterizationConverse.derivedCategoryBBounded_iff_cardinalSum_rank_ext_lt_aleph0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/CoherentCharacterizationConverse.lean#L106). The attribute's comment: “both implications, for X proper over a field and K in D\_QCoh(O\_X), with condition (2) as the source's sum of dimensions, a cardinal sum below aleph0”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.5, Tag 0FY9](https://stacks.math.columbia.edu/tag/0FY9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
