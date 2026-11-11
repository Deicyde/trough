---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.FiniteSurjectiveCoherentSupport.exists_isCoherent_supp_pushforward_eq_range, Stacks.AlgebraicGeometry.AffineIdealPushforward.ideal_smul_pushforward_sections_eq, Stacks.AlgebraicGeometry.Tag01YQClauseThree.isAffine_of_isFinite_surjective
statement: formalized
proof: formalized
---

# 30.13 Finite morphisms and affines

Section 30.13 of the Stacks Project, [Tag 01YN](https://stacks.math.columbia.edu/tag/01YN). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01YO, a lemma

[Tag 01YO](https://stacks.math.columbia.edu/tag/01YO) in the Stacks Project.

**`Stacks.AlgebraicGeometry.FiniteSurjectiveCoherentSupport.exists_isCoherent_supp_pushforward_eq_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteSurjectiveCoherentSupport/Basic.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteSurjectiveCoherentSupport/Basic.lean#L341).

> **[Stacks, Tag 01YO].** Let `f : Y ⟶ X` be finite and surjective with `X` locally Noetherian
> and let `i : Z ⟶ X` be an integral closed subscheme with generic point `ξ`. Then there is a
> coherent module `ℱ` on `Y` whose direct image `f_* ℱ` has support exactly `Z` and whose stalk at
> `ξ` is annihilated by the maximal ideal of `𝒪_{X,ξ}`.

```lean
theorem exists_isCoherent_supp_pushforward_eq_range
    {X Y Z : Scheme.{u}} (f : Y ⟶ X) [IsFinite f] [Surjective f]
    [IsLocallyNoetherian X] (i : Z ⟶ X) [IsClosedImmersion i] [IsIntegral Z] :
    ∃ F : Y.Modules, F.IsCoherent ∧
      SheafOfModules.supp ((Scheme.Modules.pushforward f).obj F) = Set.range i ∧
      (let G := (Scheme.Modules.pushforward f).obj F
       let x := i (genericPoint Z)
       letI : Module (X.presheaf.stalk x)
           (TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x) :=
         PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
           (R := X.presheaf) G.val x
       ∀ a : X.presheaf.stalk x,
         a ∈ IsLocalRing.maximalIdeal (X.presheaf.stalk x) →
         ∀ s : TopCat.Presheaf.stalk (C := Ab.{u}) G.val.presheaf x, a • s = 0)
```

## Tag 01YP, a lemma

[Tag 01YP](https://stacks.math.columbia.edu/tag/01YP) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AffineIdealPushforward.ideal_smul_pushforward_sections_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/IdealPushforwardAffine.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/IdealPushforwardAffine.lean#L145).

> **Stacks Project, Tag 01YP.** If `f : Y ⟶ X` is affine, `F` is a quasi-coherent
> `𝒪_Y`-module, and `I` is a quasi-coherent ideal sheaf on `X`, then `I · f₊ F = f₊((f⁻¹ I) · F)`.
>
> The equality is stated on every affine open, using the affine-open presentation of
> quasi-coherent ideal sheaves.

```lean
theorem ideal_smul_pushforward_sections_eq (f : Y ⟶ X) [IsAffineHom f]
    (I : X.IdealSheafData) (F : Y.Modules) [F.IsQuasicoherent]
    (U : X.affineOpens) :
    pushforwardIdealMultipleSections f I F U =
      pullbackIdealMultiplePushforwardSections f I F U
```

## Tag 01YQ, a lemma

[Tag 01YQ](https://stacks.math.columbia.edu/tag/01YQ) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Tag01YQClauseThree.isAffine_of_isFinite_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClauseThree/GenericStalkInput.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ClauseThree/GenericStalkInput.lean#L61).

> A Noetherian scheme admitting a finite surjective morphism from an affine scheme is affine.

```lean
theorem isAffine_of_isFinite_surjective {X Y : Scheme.{u}} (f : Y ⟶ X)
    [IsFinite f] [Surjective f] [IsAffine Y] [IsNoetherian X] :
    IsAffine X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.13, Tag 01YN](https://stacks.math.columbia.edu/tag/01YN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
