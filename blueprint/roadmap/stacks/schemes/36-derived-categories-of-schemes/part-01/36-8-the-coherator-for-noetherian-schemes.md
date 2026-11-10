---
declaration: section
origin: cited
lean: AlgebraicGeometry.isFlasque_of_injective_quasicoherent, AlgebraicGeometry.noetherianPushforwardExtension, AlgebraicGeometry.noetherianPushforwardExtension_isRightDerivedFunctor, AlgebraicGeometry.noetherianPushforwardExtensionComparison, Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_isNoetherian, Stacks.DerivedQCoh.derivedCoherator_isoInv_of_isNoetherian, Stacks.DerivedQCoh.derivedCoherator_isoInv_of_isNoetherian'
statement: formalized
proof: formalized
---

# 36.8 The coherator for Noetherian schemes

Section 36.8 of the Stacks Project, [Tag 09T1](https://stacks.math.columbia.edu/tag/09T1). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09T2, a lemma

[Tag 09T2](https://stacks.math.columbia.edu/tag/09T2) in the Stacks Project.

**`AlgebraicGeometry.isFlasque_of_injective_quasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/SectionExtension.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/InjectiveQcoh/SectionExtension.lean#L373).

> Let `X` be a Noetherian scheme and let `𝒥` be an injective
> object of the category of quasi-coherent `𝒪_X`-modules. Then `𝒥` is a flasque sheaf of
> `𝒪_X`-modules.

```lean
public theorem isFlasque_of_injective_quasicoherent (X : Scheme.{u}) [IsNoetherian X]
    (J : (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) [Injective J] :
    TopCat.Sheaf.IsFlasque ((SheafOfModules.toSheaf X.ringCatSheaf).obj J.obj)
```

## Tag 09T3, a lemma

[Tag 09T3](https://stacks.math.columbia.edu/tag/09T3) in the Stacks Project.

**`AlgebraicGeometry.noetherianPushforwardExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Basic.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Basic.lean#L138).

> The right derived extension `Φ : D(QCoh(𝒪_X)) ⥤ D(QCoh(𝒪_Y))` of direct image on
> quasi-coherent modules, for a morphism of Noetherian schemes: the total right derived functor
> of termwise direct image.
>
> This is the functor of [Stacks, Tag 09T3]; the compatibility with derived direct image that
> the source asserts of it is
> `AlgebraicGeometry.noetherianPushforwardExtensionComparison`.

```lean
def noetherianPushforwardExtension {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsNoetherian X] [IsNoetherian Y] :
    DerivedCategory (Scheme.QuasicoherentModules X) ⥤
      DerivedCategory (Scheme.QuasicoherentModules Y)
```

**`AlgebraicGeometry.noetherianPushforwardExtension_isRightDerivedFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Basic.lean#L159).

> `AlgebraicGeometry.noetherianPushforwardExtension` is a total right derived functor of
> direct image on quasi-coherent modules, with
> `AlgebraicGeometry.noetherianPushforwardExtensionUnit` as its derivation unit.

```lean
instance noetherianPushforwardExtension_isRightDerivedFunctor {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsNoetherian X] [IsNoetherian Y] :
    (noetherianPushforwardExtension f).IsRightDerivedFunctor
      (noetherianPushforwardExtensionUnit f)
      (HomotopyCategory.quasiIso (Scheme.QuasicoherentModules X) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.noetherianPushforwardExtensionComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Basic.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Basic.lean#L248).

> **The commuting square of [Stacks, Tag 09T3].** For a morphism of Noetherian schemes the
> derived extension of direct image on quasi-coherent modules agrees, under the comparison
> functors `D(QCoh(𝒪_•)) ⥤ D_QCoh(𝒪_•)`, with any right derived direct image of all modules.
>
> The isomorphism is the canonical one: both composites are right derived functors of the single
> functor `K(QCoh(𝒪_X)) ⥤ D(𝒪_Y)` given by termwise direct image followed by forgetting
> quasi-coherence, so they are identified by the uniqueness of right derived functors.

```lean
def noetherianPushforwardExtensionComparison :
    derivedQuasicoherentComparison X ⋙
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι ⋙ RF ≅
      noetherianPushforwardExtension f ⋙ derivedQuasicoherentComparison Y ⋙
        (DerivedCategoryB.derivedCategoryB
          (SheafOfModules.isQuasicoherent Y.ringCatSheaf)).ι
```

## Tag 09T4, a proposition

[Tag 09T4](https://stacks.math.columbia.edu/tag/09T4) in the Stacks Project.

**`Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Equivalence.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Equivalence.lean#L124). The attribute's comment: “equivalence”.

> On a Noetherian scheme the comparison functor `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of
> [Stacks, Tag 06VT] is an equivalence.

```lean
theorem derivedQuasicoherentComparison_isEquivalence_of_isNoetherian (X : Scheme.{u})
    [IsNoetherian X] : (derivedQuasicoherentComparison.{u + 1} X).IsEquivalence
```

**`Stacks.DerivedQCoh.derivedCoherator_isoInv_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Equivalence.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Equivalence.lean#L133). The attribute's comment: “identification of the quasi-inverse”.

> On a Noetherian scheme the quasi-inverse of the comparison functor of [Stacks, Tag 06VT] is
> `RQ_X`: any total right derived functor of the coherator `Q_X : Mod(𝒪_X) ⥤ QCoh(𝒪_X)` of
> [Stacks, Tag 077P], restricted to the complexes with quasi-coherent cohomology.

```lean
theorem derivedCoherator_isoInv_of_isNoetherian (X : Scheme.{u}) [IsNoetherian X]
    (RQ : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf) ⥤
      DerivedCategory (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory)
    (RQUnit : (modulesCoherator X).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q
          (C := (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory) ⟶
      DerivedCategory.Q (C := SheafOfModules.{u} X.ringCatSheaf) ⋙ RQ)
    [RQ.IsRightDerivedFunctor RQUnit
      (HomologicalComplex.quasiIso (SheafOfModules.{u} X.ringCatSheaf) (ComplexShape.up ℤ))] :
    letI := derivedQuasicoherentComparison_isEquivalence_of_isNoetherian X
    Nonempty ((DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι ⋙ RQ ≅
      (derivedQuasicoherentComparison.{u + 1} X).inv)
```

**`Stacks.DerivedQCoh.derivedCoherator_isoInv_of_isNoetherian'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Equivalence.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/NoetherianExtension/Equivalence.lean#L153). The attribute's comment: “identification of the quasi-inverse”.

> On a Noetherian scheme the quasi-inverse of the comparison functor of [Stacks, Tag 06VT] is
> the restriction of the total right derived functor `Stacks.DerivedQCoh.schemeDerivedCoherator` of
> the coherator to the complexes with quasi-coherent cohomology.

```lean
theorem derivedCoherator_isoInv_of_isNoetherian' (X : Scheme.{u}) [IsNoetherian X] :
    letI := derivedQuasicoherentComparison_isEquivalence_of_isNoetherian X
    Nonempty ((DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι ⋙ schemeDerivedCoherator.{u + 1} X ≅
      (derivedQuasicoherentComparison.{u + 1} X).inv)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.8, Tag 09T1](https://stacks.math.columbia.edu/tag/09T1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
