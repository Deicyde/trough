---
declaration: section
origin: cited
lean: Stacks.LocalCohomologySequence.forall_lt_depth_add_ringKrullDim_iff_forall_isCoherent_rightDerived, Stacks.LocalCohomologySequence.isCoherent_rightDerived_of_isFiniteLocallyFree, AlgebraicGeometry.exists_pow_smul_derivedGlobalSections_eq_zero_of_isFiniteLocallyFree
statement: formalized
proof: formalized
---

# 51.12 Finiteness of pushforwards, II

Section 51.12 of the Stacks Project, [Tag 0BJX](https://stacks.math.columbia.edu/tag/0BJX). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BJY, a lemma

[Tag 0BJY](https://stacks.math.columbia.edu/tag/0BJY) in the Stacks Project.

**`Stacks.LocalCohomologySequence.forall_lt_depth_add_ringKrullDim_iff_forall_isCoherent_rightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/DepthDimensionCriterionGlobal.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/PushforwardCoherence/DepthDimensionCriterionGlobal.lean#L391). References: SGA 2 VIII (2.3), “(i) ⇔ (iv)”.

> **[Stacks, Tag 0BJY].** Let `X` be a locally Noetherian scheme, let `j : U → X` be the
> inclusion of an open subscheme with complement `Z`, let `ℱ` be a coherent `𝒪_U`-module and let
> `n ≥ 0` be an integer. Assume that `X` is universally catenary and that the formal fibres of
> `𝒪_{X,z}` are `(Sₙ)` for every `z ∈ Z`. Then the following are equivalent:
>
> * (a) for `x ∈ Supp(ℱ)` and `z ∈ Z ∩ closure {x}` we have
>   `depth_{𝒪_{X,x}}(ℱ_x) + dim(𝒪_{closure {x}, z}) > n`;
> * (b) `R^p j_* ℱ` is coherent for `0 ≤ p < n`.
>
> The closure `closure {j(x)}` carries its reduced induced scheme structure, the closed subscheme
> cut out by `Scheme.IdealSheafData.vanishingIdeal`, and a point `z ∈ Z ∩ closure {j(x)}` is a point
> `y` of that subscheme whose image lies outside `j(U)`, by
> `AlgebraicGeometry.range_subschemeι_vanishingIdeal_closure`. The depth is taken in the local ring
> of `U` at `x`, which is that of `X` at `j(x)`. The inclusion is an arbitrary open immersion `j`,
> which is the same statement: an open immersion is the inclusion of its open image composed with
> an isomorphism.
>
> The proof rewrites (a) pointwise by
> `AlgebraicGeometry.ringKrullDim_stalk_vanishingIdeal_closure_eq_topCodim` into the condition of
> `forall_lt_depth_add_topCodim_iff_forall_isCoherent_rightDerived`.

```lean
public theorem forall_lt_depth_add_ringKrullDim_iff_forall_isCoherent_rightDerived
    {U X : Scheme.{u}} [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j] (F : U.Modules)
    [F.IsCoherent] (n : ℕ) (hX : Scheme.IsUniversallyCatenary X)
    (hformal : ∀ z : X, z ∉ Set.range j.base →
      Stacks.LocalCohomology.FormalFibersHavePropertySk (X.presheaf.stalk z) n) :
    (∀ x : U, x ∈ SheafOfModules.supp F →
        ∀ y : (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({j.base x} : Set X))).subscheme,
          (Scheme.IdealSheafData.vanishingIdeal
            (Closeds.closure ({j.base x} : Set X))).subschemeι.base y ∉ Set.range j.base →
          (((n : ℕ∞) : WithBot ℕ∞) <
            (Module.depth (U.presheaf.stalk x) (IsLocalRing.maximalIdeal (U.presheaf.stalk x))
                (F.presheaf.stalk x) : WithBot ℕ∞) +
              ringKrullDim ((Scheme.IdealSheafData.vanishingIdeal
                (Closeds.closure ({j.base x} : Set X))).subscheme.presheaf.stalk y))) ↔
      ∀ p : ℕ, p < n →
        (((Scheme.Modules.pushforward j).rightDerived p).obj F).IsCoherent
```

## Tag 0BLT, a lemma

[Tag 0BLT](https://stacks.math.columbia.edu/tag/0BLT) in the Stacks Project.

**`Stacks.LocalCohomologySequence.isCoherent_rightDerived_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/FiniteLocallyFreeComplement.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/FiniteLocallyFreeComplement.lean#L183).

> **[Stacks, Tag 0BLT].** Let `X` be a locally Noetherian scheme, let `j : U → X` be the
> inclusion of an open subscheme and let `n ≥ 0`.  If `R^p j_* 𝒪_U` is coherent for `0 ≤ p < n`,
> then so is `R^p j_* ℱ` for `0 ≤ p < n` and every finite locally free `𝒪_U`-module `ℱ`.
>
> The inclusion is taken to be an arbitrary open immersion `j`, which is the same statement: an
> open immersion is the inclusion of its open image composed with an isomorphism.
>
> The question is local on `X`: coherence of a higher direct image along the quasi-compact
> quasi-separated `j` may be checked on every affine open `V` of `X`, for the restricted morphism
> `j ∣_ V` and the restricted module, by
> `…ProperCohomologyFinite.isCoherent_rightDerivedPlus_of_forall_isAffineOpen`.  That case is
> `isCoherent_rightDerived_of_isFiniteLocallyFree_affine`, `V.toScheme` being affine and locally
> Noetherian; its hypothesis on the structure sheaf is the tag's hypothesis restricted to `V` by
> [Stacks, Tag 01E5], and its finite local freeness is the restriction of `ℱ`.

```lean
public theorem isCoherent_rightDerived_of_isFiniteLocallyFree {U X : Scheme.{u}}
    [IsLocallyNoetherian X] (j : U ⟶ X) [IsOpenImmersion j] (n : ℕ)
    (hO : ∀ p : ℕ, p < n →
      (((Scheme.Modules.pushforward j).rightDerived p).obj
        (SheafOfModules.unit U.ringCatSheaf)).IsCoherent)
    (F : U.Modules) (hF : Scheme.Modules.IsFiniteLocallyFree F) :
    ∀ p : ℕ, p < n →
      (((Scheme.Modules.pushforward j).rightDerived p).obj F).IsCoherent
```

## Tag 0BM5, a lemma

[Tag 0BM5](https://stacks.math.columbia.edu/tag/0BM5) in the Stacks Project.

**`AlgebraicGeometry.exists_pow_smul_derivedGlobalSections_eq_zero_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/AnnihilatorsLocalCohomology/FiniteLocallyFree.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/AnnihilatorsLocalCohomology/FiniteLocallyFree.lean#L484).

> Let `I` be a finitely generated ideal of `A`, let `J ≤ I` and let `U` be the complement of
> `V(I)` in `Spec A`.  If a power of `J` annihilates the degree `p` cohomology of the structure
> sheaf of `U`, then for every finite locally free sheaf `F` on `U` some power of `J` annihilates
> the degree `p` cohomology of `F`.
>
> Cohomology is the right derived functor of global sections, and the `A`-action is the one
> induced by the canonical map `A ⟶ Γ(U, 𝒪_U)`.

```lean
theorem exists_pow_smul_derivedGlobalSections_eq_zero_of_isFiniteLocallyFree
    (A : Type u) [CommRing A] (I J : Ideal A) (hJI : J ≤ I) (hI : I.FG)
    (U : (Spec (.of A)).Opens)
    (hU : (U : Set (Spec (.of A))) = (PrimeSpectrum.zeroLocus (I : Set A))ᶜ) (p : ℕ)
    (hn : ∃ n : ℕ, ∀ a ∈ J ^ n,
      ∀ x : (ModuleCat.restrictScalars
          ((Scheme.ΓSpecIso (.of A)).inv ≫ U.ι.appTop).hom).obj
        (((SheafOfModules.evaluation (U : Scheme).ringCatSheaf
            (op (⊤ : (U : Scheme).Opens))).rightDerived p).obj
          (SheafOfModules.unit (U : Scheme).ringCatSheaf)), a • x = 0)
    (F : SheafOfModules (U : Scheme).ringCatSheaf)
    [SheafOfModules.IsFiniteLocallyFree.{u, u, u} F] :
    ∃ m : ℕ, ∀ a ∈ J ^ m,
      ∀ x : (ModuleCat.restrictScalars
          ((Scheme.ΓSpecIso (.of A)).inv ≫ U.ι.appTop).hom).obj
        (((SheafOfModules.evaluation (U : Scheme).ringCatSheaf
            (op (⊤ : (U : Scheme).Opens))).rightDerived p).obj F), a • x = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.12, Tag 0BJX](https://stacks.math.columbia.edu/tag/0BJX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
