---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.isFlat_componentModulesRestrictionComplex_X, CategoryTheory.SimplicialSiteSituation.kFlat_componentModulesRestrictionComplex, Stacks.Sheaves.RingedToposModules.pullbackModules_preservesZeroMorphisms, Stacks.Sheaves.DerivedPullback.KFlatPullback.pullbackTopos_preservesZeroMorphisms, Stacks.Sheaves.DerivedPullback.KFlatPullbackOfToposHom.isKFlat_pullbackMapHomotopy, Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedPullbackCommShift, Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedPullback_isTriangulated_of_isMorphismOfSites, Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedPullbackComparison_isIso_of_kFlat_of_flat
statement: formalized
proof: formalized
---

# 21.18 Derived pullback

Section 21.18 of the Stacks Project, [Tag 06YV](https://stacks.math.columbia.edu/tag/06YV). 8 tags here are carried by 39 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G7E, a lemma

[Tag 0G7E](https://stacks.math.columbia.edu/tag/0G7E) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.isFlat_componentModulesRestrictionComplex_X`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean#L195). The attribute's comment: “the flat-terms clause, for restriction to a simplicial component”.

> **The flat-terms clause of Stacks 0G7E at `g_n`.** The restriction to a component of a
> complex of `O`-modules with flat terms has flat terms.

```lean
theorem isFlat_componentModulesRestrictionComplex_X
    (K : CochainComplex (S.totalRingedTopos O).Modules ℤ)
    (hflatK : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
      (O := (S.totalRingedTopos O).O) (K.X i)) (i : ℤ) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
      (O := (S.componentRingedTopos O n).O)
      (((S.componentModulesRestrictionComplex O n).obj K).X i)
```

**`CategoryTheory.SimplicialSiteSituation.kFlat_componentModulesRestrictionComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentTensorComplex.lean#L210). The attribute's comment: “the K-flatness clause, for restriction to a simplicial component”.

> **The K-flatness clause of Stacks 0G7E at `g_n`.** The restriction to a component of a
> K-flat complex of `O`-modules with flat terms is K-flat.

```lean
theorem kFlat_componentModulesRestrictionComplex
    (K : CochainComplex (S.totalRingedTopos O).Modules ℤ)
    (hK : Stacks.SheafOfModules.KFlat (S.totalRingedTopos O).O K)
    (hflatK : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
      (O := (S.totalRingedTopos O).O) (K.X i)) :
    Stacks.SheafOfModules.KFlat (S.componentRingedTopos O n).O
      ((S.componentModulesRestrictionComplex O n).obj K)
```

**`Stacks.Sheaves.RingedToposModules.pullbackModules_preservesZeroMorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DegreewisePullbackOfComplexes.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DegreewisePullbackOfComplexes.lean#L60). The attribute's comment: “degreewise pullback”.

> Pullback of sheaves of modules along a morphism of ringed topoi preserves zero
> morphisms: it is a left adjoint by Stacks 03D7, and a left adjoint between categories with
> zero morphisms carries zero morphisms to zero morphisms. This is what lets `f^*` be applied
> degreewise to a complex of modules, as in Stacks 0G7E.

```lean
instance pullbackModules_preservesZeroMorphisms (f : RingedToposHom X Y) :
    (f.pullbackModules).PreservesZeroMorphisms
```

**`Stacks.Sheaves.DerivedPullback.KFlatPullback.pullbackTopos_preservesZeroMorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/KFlatPullbackAlongRingedTopoi.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/KFlatPullbackAlongRingedTopoi.lean#L185). The attribute's comment: “degreewise pullback”.

> Pullback of sheaves of modules preserves zero morphisms, being additive.  This is what
> makes the degreewise pullback functor on complexes available.

```lean
instance pullbackTopos_preservesZeroMorphisms
    (f : AlgebraicGeometry.RingedToposSiteHom X Y) :
    (show SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) ⥤
      SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O) from
        f.pullbackTopos).PreservesZeroMorphisms
```

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackOfToposHom.isKFlat_pullbackMapHomotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/KFlatPullbackOfToposHom.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/KFlatPullbackOfToposHom.lean#L307). The attribute's comment: “K-flat with flat terms is preserved, for an arbitrary morphism of ringed topoi”.

> **Stacks 0G7E for an arbitrary morphism of ringed topoi, on the homotopy category.**
> Degreewise pullback along `f` carries the class of K-flat complexes of `O`-modules with flat
> terms into the same class for `O'`.
>
> Nothing happens on passage to the homotopy category: the underlying complex of `K(f^*)K` is `f^*`
> of the underlying complex of `K`.  The K-flatness clause is `kFlat_pullbackComplex` and the
> flat-terms clause is `isFlat_pullbackComplex_X`, i.e. Stacks 05VD alone.

```lean
theorem isKFlat_pullbackMapHomotopy (f : RingedToposHom X Y)
    (K : HomotopyCategory (SheafOfModules.{w'} (SheafOfModules.Tensor.ringSheaf Y.O))
      (ComplexShape.up ℤ))
    (hK : Stacks.Cohomology.DerivedPullbackPushforwardAdjunction.IsKFlat (Y := Y) K) :
    Stacks.Cohomology.DerivedPullbackPushforwardAdjunction.IsKFlat (Y := X)
      ((Stacks.Cohomology.DerivedPushforward.pullbackMapHomotopy f).obj K)
```

## Tag 06YY, a lemma

[Tag 06YY](https://stacks.math.columbia.edu/tag/06YY) in the Stacks Project.

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedPullbackCommShift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean#L97). The attribute's comment: “compatibility with shifts, for a morphism of ringed topoi presented by a morphism of the underlying sites, at RingedTopos.\{u, u, u}”.

> **Tag 06YY, compatibility with shifts.**  `Lf^*` commutes with the shift functors of the two
> derived categories.  Together with `derivedPullback_isTriangulated_of_isMorphismOfSites` this is
> the assertion that `Lf^*` is *exact* as a functor of triangulated categories.
>
> This is `Stacks.Sheaves.RingedToposDerivedPullback.derivedPullback_commShift` with its instance
> binder discharged; that instance never needed the exactness clause, only the existence of the
> derived functor.

```lean
def derivedPullbackCommShift :
    haveI := hasLeftDerivedFunctor_pullbackOnHomotopy f hmos
    (derivedPullback f).CommShift ℤ
```

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedPullback_isTriangulated_of_isMorphismOfSites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean#L112). The attribute's comment: “exactness, for a morphism of ringed topoi presented by a morphism of the underlying sites, at RingedTopos.\{u, u, u}”.

> **Tag 06YY, exactness.**  `Lf^*` is an exact functor of triangulated categories: it carries a
> distinguished triangle of `D(O')` to a distinguished triangle of `D(O)`.
>
> This is `Stacks.Sheaves.RingedToposDerivedPullback.derivedPullback_isTriangulated` with both of
> its inputs discharged — the exactness clause by `pullbackInvertsQuasiIso_isKFlat` and the
> instance binder by `hasLeftDerivedFunctor_pullbackOnHomotopy`.

```lean
theorem derivedPullback_isTriangulated_of_isMorphismOfSites :
    haveI := hasLeftDerivedFunctor_pullbackOnHomotopy f hmos
    (derivedPullback f).IsTriangulated
```

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedPullbackComparison_isIso_of_kFlat_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean#L130). The attribute's comment: “computation on K-flat complexes with flat terms, for a morphism of ringed topoi presented by a morphism of the underlying sites, at RingedTopos.\{u, u, u}”.

> **Tag 06YY, the computation `Lf^* K^• = f^* K^•`.**  The canonical comparison
> `Lf^* K^• ⟶ f^* K^•` is invertible at a K-flat complex `K^•` of `O'`-modules with flat terms: the
> derived pullback of such a complex is computed by degreewise pullback.
>
> This is
> `Stacks.Sheaves.RingedToposDerivedPullback.isIso_derivedPullbackComparison_app_of_kFlat_of_flat`
> with both of its inputs discharged.  Both hypotheses on `K^•` are the source's, and both are
> used: they are the two clauses of the resolving class
> `Stacks.Cohomology.DerivedPullbackPushforwardAdjunction.IsKFlat`.

```lean
theorem derivedPullbackComparison_isIso_of_kFlat_of_flat
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ)
    (hK : CochainComplex.KFlatBifunctor.KFlat
      (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} Y.O) K)
    (hflat : ∀ i : ℤ, SheafOfModules.IsFlat.{u, u, u, u} (O := Y.O) (K.X i)) :
    haveI := hasLeftDerivedFunctor_pullbackOnHomotopy f hmos
    IsIso ((derivedPullbackComparison f).app
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K))
```

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.derivedPullbackComparison_isIso_of_boundedAbove_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackAsATriangulatedFunctor.lean#L151). The attribute's comment: “computation on bounded above complexes of flat modules, for a morphism of ringed topoi presented by a morphism of the underlying sites, at RingedTopos.\{u, u, u}”.

> **Tag 06YY, the computation on a bounded above complex of flat modules.**  A bounded above
> complex of flat `O'`-modules is K-flat by Tag 06YQ, so the canonical comparison is invertible
> there too.  This is the "in particular" of the source's statement.
>
> This is `isIso_derivedPullbackComparison_app_of_boundedAbove_of_flat` of
> `Stacks.Sheaves.RingedToposDerivedPullback` with both of its inputs discharged.

```lean
theorem derivedPullbackComparison_isIso_of_boundedAbove_of_flat
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ)
    (hbound : ∃ n : ℤ, K.IsStrictlyLE n)
    (hflat : ∀ i : ℤ, SheafOfModules.IsFlat.{u, u, u, u} (O := Y.O) (K.X i)) :
    haveI := hasLeftDerivedFunctor_pullbackOnHomotopy f hmos
    IsIso ((derivedPullbackComparison f).app
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K))
```

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.isTriangulated_derivedPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean#L172). The attribute's comment: “exactness”.

> **Tag 06YY, exactness.**  The derived pullback along a morphism of ringed topoi is an exact
> functor of triangulated categories.

```lean
theorem isTriangulated_derivedPullback : (derivedPullback f).IsTriangulated
```

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.isIso_derivedPullbackComparison_app_kFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean#L180). The attribute's comment: “computation on K-flat complexes with flat terms”.

> **Tag 06YY, the computation.**  The canonical comparison `Lf^* K^• ⟶ f^* K^•` is invertible
> at a K-flat complex of `O'`-modules with flat terms: the derived pullback of such a complex is
> computed by degreewise pullback.

```lean
theorem isIso_derivedPullbackComparison_app_kFlat
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ)
    (hK :
      letI := Stacks.SheafOfModules.Tensor.sheafTensor_obj_additive.{u, u, u, u, u} Y.O
      @CochainComplex.KFlatBifunctor.KFlat
        (_root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
        (_root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
        (_root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
        inferInstance inferInstance inferInstance inferInstance inferInstance inferInstance
        (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} Y.O)
        (Stacks.SheafOfModules.Tensor.sheafTensor_additive.{u, u, u, u, u} Y.O)
        (Stacks.SheafOfModules.Tensor.sheafTensor_obj_additive.{u, u, u, u, u} Y.O)
        inferInstance K)
    (hflat : ∀ i : ℤ, SheafOfModules.IsFlat.{u, u, u, u} (O := Y.O) (K.X i)) :
    IsIso ((derivedPullbackComparison f).app
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K))
```

**`Stacks.Cohomology.DerivedPullbackOnRingedTopoi.isIso_derivedPullbackComparison_app_boundedAbove`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackExistence.lean#L204). The attribute's comment: “computation on bounded above flat complexes”.

> **Tag 06YY, the computation on bounded above complexes of flat modules.**  A bounded above
> complex of flat `O'`-modules is K-flat by Tag 06YQ, so its derived pullback is computed by
> degreewise pullback.

```lean
theorem isIso_derivedPullbackComparison_app_boundedAbove
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ)
    (hbound : ∃ n : ℤ, K.IsStrictlyLE n)
    (hflat : ∀ i : ℤ, SheafOfModules.IsFlat.{u, u, u, u} (O := Y.O) (K.X i)) :
    IsIso ((derivedPullbackComparison f).app
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K))
```

**`Stacks.Sheaves.RingedToposDerivedPullback.derivedPullback_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfRingedTopoi.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfRingedTopoi.lean#L283). The attribute's comment: “compatibility with shifts”.

> **Tag 06YY, compatibility with shifts.**  The derived pullback commutes with the shift
> functors of the two derived categories.

```lean
noncomputable instance derivedPullback_commShift :
    (Stacks.Cohomology.DerivedPullbackPushforwardAdjunction.derivedPullback f).CommShift ℤ
```

**`Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean#L217). The attribute's comment: “the derived pullback functor, for a morphism of ringed topoi whose two ringed topoi have their object, morphism and structure-ring universes free and unrelated, and whose geometric datum is a morphism of the underlying topoi rather than of the underlying sites”.

> **Tag 06YY, the derived pullback functor, at independent universes.**  The derived pullback
> `Lf^* : D(𝒪') ⥤ D(𝒪)` along a morphism of ringed topoi, the total left derived functor of
> degreewise pullback followed by localization.
>
> The two ringed topoi have all six of their universes free, and the geometric datum is the
> two-field morphism of ringed topoi of Stacks 01D3, part (2); in particular this applies to the
> small étale ringed topos `AlgebraicGeometry.RingedTopos.{u, u + 1, u}` of an algebraic space,
> which `Stacks.Cohomology.DerivedPullbackPushforwardAdjunction.derivedPullback` does not.
>
> The instance argument is `Prop`-valued and is supplied by
> `pullbackOnHomotopy_hasLeftDerivedFunctor` from a resolving datum for `f^*`.

```lean
noncomputable abbrev derivedPullback :
    DerivedCategory (SheafOfModules.{w'} (SheafOfModules.Tensor.ringSheaf Y.O)) ⥤
      DerivedCategory (SheafOfModules.{w} (SheafOfModules.Tensor.ringSheaf X.O))
```

**`Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullbackComparison`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean#L227). The attribute's comment: “the canonical comparison `Lf^* ⟶ f^*`, at free and unrelated universes for the two ringed topoi and for a geometric datum which is a morphism of the underlying topoi”.

> **Tag 06YY, the canonical comparison, at independent universes.**  The comparison
> `Lf^* ⟶ f^*` from the derived pullback to degreewise pullback, whose invertibility on a
> resolving class is the computation assertion of Tag 06YY.

```lean
noncomputable abbrev derivedPullbackComparison :
    DerivedCategory.Qh ⋙ derivedPullback f ⟶ pullbackOnHomotopy f
```

**`Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean#L235). The attribute's comment: “compatibility of `Lf^*` with the shift, at free and unrelated universes for the two ringed topoi”.

> **Tag 06YY, compatibility with shifts, at independent universes.**  The derived pullback
> commutes with the shift functors of the two derived categories.

```lean
noncomputable instance derivedPullback_commShift : (derivedPullback f).CommShift ℤ
```

**`Stacks.Cohomology.DerivedPullbackOfToposHom.isIso_derivedPullbackComparison_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHom.lean#L247). The attribute's comment: “the computation `Lf^*𝒦 = f^*𝒦` on a resolving class, at free and unrelated universes for the two ringed topoi”.

> **Tag 06YY, the computation, at independent universes.**  The canonical comparison
> `Lf^* 𝒦^• ⟶ f^* 𝒦^•` is invertible at an object of a resolving class for `f^*`: the derived
> pullback of such a complex is computed by degreewise pullback.
>
> At the class of K-flat complexes with flat terms, which is the class the source resolves by,
> this is the computation assertion of Tag 06YY in the form it states.

```lean
theorem isIso_derivedPullbackComparison_app
    (P : ObjectProperty
      (HomotopyCategory (SheafOfModules.{w'} (SheafOfModules.Tensor.ringSheaf Y.O))
        (ComplexShape.up ℤ)))
    (hP : HasResolutions (Y := Y) P) (hinv : PullbackInvertsQuasiIso f P)
    (K : HomotopyCategory (SheafOfModules.{w'} (SheafOfModules.Tensor.ringSheaf Y.O))
      (ComplexShape.up ℤ))
    (hK : P K) :
    IsIso ((derivedPullbackComparison f).app K)
```

**`Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHomTriangulated.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackOfToposHomTriangulated.lean#L87). The attribute's comment: “exactness of the derived pullback, for a morphism of ringed topoi whose geometric datum is a morphism of the underlying topoi”.

> **[Stacks, Tag 06YY], exactness, for a morphism of ringed topoi.** The derived pullback
> `Lf^* : D(𝒪_D) ⟶ D(𝒪_C)` is a triangulated functor. Every morphism of `D(𝒪_D)` is, up to
> isomorphism, the image of a morphism between K-flat complexes with flat terms; its mapping cone
> is again such a complex, and on such complexes `Lf^*` is computed by the degreewise pullback,
> which carries the mapping-cone triangle to a distinguished triangle.

```lean
theorem derivedPullback_isTriangulated :
    (Stacks.Cohomology.DerivedPullbackOfToposHom.derivedPullback f).IsTriangulated
```

**`Stacks.Cohomology.DerivedPullbackPushforwardAdjunction.derivedPullback`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/AdjunctionForRingedTopoi.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/AdjunctionForRingedTopoi.lean#L426). The attribute's comment: “the derived pullback functor”.

> **Tag 06YY, the derived pullback functor.**  The derived pullback `Lf^* : D(𝒪') ⥤ D(𝒪)`, the
> total left derived functor of degreewise pullback followed by localization.
>
> The instance argument is discharged for every morphism of ringed topoi by
> `Stacks.Cohomology.DerivedPullbackOnRingedTopoi.hasLeftDerivedFunctor_pullbackOnHomotopy`, so
> this is the functor Tag 06YY asserts to exist.

```lean
noncomputable abbrev derivedPullback :
    DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ⥤
      DerivedCategory (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
```

**`Stacks.Cohomology.DerivedPullbackPushforwardAdjunction.derivedPullbackComparison`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/AdjunctionForRingedTopoi.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/AdjunctionForRingedTopoi.lean#L437). The attribute's comment: “canonical comparison”.

> **Tag 06YY, the canonical comparison.**  The comparison `Lf^* ⟶ f^*` from the derived
> pullback to degreewise pullback, whose invertibility on K-flat complexes with flat terms is the
> computation assertion of Tag 06YY.

```lean
noncomputable abbrev derivedPullbackComparison :
    DerivedCategory.Qh ⋙ derivedPullback f ⟶ pullbackOnHomotopy f
```

**`Stacks.Cohomology.DerivedPullbackOfToposHom.pullbackInvertsQuasiIso_isKFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/PullbackInvertsQuasiIsoOfToposHom.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPushforward/PullbackInvertsQuasiIsoOfToposHom.lean#L144). The attribute's comment: “exactness on K-flat complexes with flat terms, for an arbitrary morphism of ringed topoi”.

> **The exactness clause of Stacks 06YY for an arbitrary morphism of ringed topoi.**
> Degreewise pullback along `f` carries a quasi-isomorphism between K-flat complexes of
> `O`-modules with flat terms to an isomorphism of `D(O')`.
>
> The cone of such a quasi-isomorphism is acyclic and is again K-flat with flat terms, so its
> degreewise pullback is acyclic; the conclusion is then read off the image of the mapping-cone
> triangle under the triangulated functor `K(f^*)`.

```lean
theorem pullbackInvertsQuasiIso_isKFlat (f : RingedToposHom X Y) :
    PullbackInvertsQuasiIso f (IsKFlat (Y := Y))
```

## Tag 0D6D, a lemma

[Tag 0D6D](https://stacks.math.columbia.edu/tag/0D6D) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.isIso_derivedTransitionCompComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedPullbackComposition.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedPullbackComposition.lean#L164). The attribute's comment: “for the transition morphisms of a simplicial-site situation”.

> The canonical comparison from the composite of the derived pullbacks along the transitions
> of `ψ` and `φ` to the derived pullback along the transition of `ψ ≫ φ` is an isomorphism, so
> `Lf_ψ^* ∘ Lf_φ^* = Lf_{ψ ≫ φ}^*`.

```lean
theorem isIso_derivedTransitionCompComparison {l m n : SimplexCategory} (ψ : l ⟶ m)
    (φ : m ⟶ n) :
    IsIso (S.derivedTransitionCompComparison O ψ φ)
```

**`CategoryTheory.SimplicialSiteSituation.derivedTransitionCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedPullbackComposition.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/DerivedPullbackComposition.lean#L177). The attribute's comment: “for the transition morphisms of a simplicial-site situation, as a natural isomorphism”.

> The natural isomorphism `Lf_ψ^* ⋙ Lf_φ^* ≅ Lf_{ψ ≫ φ}^*` given by the canonical
> comparison.

```lean
noncomputable def derivedTransitionCompIso {l m n : SimplexCategory} (ψ : l ⟶ m) (φ : m ⟶ n) :
    S.derivedTransitionPullback O ψ ⋙ S.derivedTransitionPullback O φ ≅
      S.derivedTransitionPullback O (ψ ≫ φ)
```

**`Stacks.Cohomology.DerivedPullbackCompositionOfToposHom.isIso_derivedPullbackCompComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOfToposHom.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOfToposHom.lean#L351). The attribute's comment: “for a morphism of ringed topoi whose geometric datum is a morphism of the underlying topoi rather than a continuous functor between the underlying sites, with no morphism-of-sites hypothesis”.

> **Stacks 0D6D.** For composable morphisms of ringed topoi `f` and `g`, the canonical
> comparison from the composite of the derived pullbacks to the derived pullback along `g ∘ f` is
> an isomorphism, so `Lf^* ∘ Lg^* = L(g ∘ f)^*`.
>
> There is no hypothesis: the geometric datum is the two-field morphism of ringed topoi of
> Stacks 01D3, part (2), with no continuous functor between underlying sites and no
> morphism-of-sites condition. Both functors are left derived functors of degreewise pullback
> along `g ∘ f`, and a map between left derived functors induced by the universal property is
> invertible exactly then.

```lean
theorem isIso_derivedPullbackCompComparison :
    IsIso (derivedPullbackCompComparison f g)
```

**`Stacks.Cohomology.DerivedPullbackCompositionOfToposHom.derivedPullbackCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOfToposHom.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOfToposHom.lean#L363). The attribute's comment: “as a natural isomorphism, for a morphism of ringed topoi whose geometric datum is a morphism of the underlying topoi rather than a continuous functor between the underlying sites, with no morphism-of-sites hypothesis”.

> **Stacks 0D6D as a natural isomorphism** `Lg^* ⋙ Lf^* ≅ L(g ∘ f)^*`, for morphisms of
> ringed topoi and with no hypothesis, obtained by inverting the canonical comparison.

```lean
def derivedPullbackCompIso :
    derivedPullback g ⋙ derivedPullback f ≅ derivedPullback (g.comp f)
```

**`Stacks.Cohomology.DerivedPullbackCompositionOnTopoi.isIso_derivedPullbackCompComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOnRingedTopoi.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOnRingedTopoi.lean#L381).

> **Stacks 0D6D.**  For composable morphisms of ringed topoi `f` and `g`, the canonical
> comparison from the composite of the derived pullbacks to the derived pullback along `g ∘ f` is
> an isomorphism, so `Lf^* ∘ Lg^* = L(g ∘ f)^*`.
>
> Both functors are left derived functors of degreewise pullback along `g ∘ f`, and a map between
> left derived functors induced by the universal property is invertible exactly then.

```lean
theorem isIso_derivedPullbackCompComparison :
    IsIso (derivedPullbackCompComparison f g)
```

**`Stacks.Cohomology.DerivedPullbackCompositionOnTopoi.derivedPullbackCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOnRingedTopoi.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/CompositionOnRingedTopoi.lean#L394). The attribute's comment: “as a natural isomorphism”.

> **Stacks 0D6D as a natural isomorphism** `Lg^* ⋙ Lf^* ≅ L(g ∘ f)^*`, obtained by inverting
> the canonical comparison.

```lean
def derivedPullbackCompIso :
    derivedPullback g ⋙ derivedPullback f ≅ derivedPullback (g.comp f)
```

## Tag 07A4, a lemma

[Tag 07A4](https://stacks.math.columbia.edu/tag/07A4) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.componentDerivedTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentDerivedTensor.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ComponentDerivedTensor.lean#L94). The attribute's comment: “the canonical bifunctorial isomorphism, for the component inverse image”.

> **The derived tensor comparison at the inclusion of a simplicial component.** The canonical
> bifunctorial isomorphism
>
> `g_n^*(A ⊗^L_O B) ≅ g_n^*A ⊗^L_{O_n} g_n^*B`
>
> for the derived restriction `Lg_n^*` of sheaves of modules to the degree-`n` component of a
> simplicial-site situation, stated between the two uncurried bifunctors on `D(O) × D(O)`, so that
> naturality in both variables is part of its type.
>
> Its value on a pair of K-flat complexes with flat terms is
> `Stacks.DerivedTensor.ExactFunctorTensor.modelIso`, and the passage to arbitrary objects of `D(O)`
> is the descent of that value along the localization of pairs of models.

```lean
def componentDerivedTensorIso :
    Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
          (S.totalRingedTopos O).O) ⋙
        S.derivedComponentModuleRestriction O n ≅
      (S.derivedComponentModuleRestriction O n).prod
          (S.derivedComponentModuleRestriction O n) ⋙
        Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor
          (S.componentRingedTopos O n).O)
```

**`Stacks.Sheaves.DerivedPullback.derivedPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorComparison.lean, line 652](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorComparison.lean#L652). The attribute's comment: “the canonical bifunctorial isomorphism”.

> **Stacks 07A4.** The canonical bifunctorial isomorphism
>
> `Lf^*(K ⊗^L_{O'} L) ≅ Lf^*K ⊗^L_O Lf^*L`
>
> for a morphism of ringed topoi `f : (Sh(C), O) ⟶ (Sh(D), O')`, stated between the two uncurried
> bifunctors on `D(O') × D(O')`, so that naturality in both variables is part of its type.
>
> Its value on a pair of K-flat complexes with flat terms is the five-step composite of the source
> (`derivedPullbackTensorModelIso`), and the passage to arbitrary objects of `D(O')` is the
> descent of that value along the localization of pairs of models.

```lean
def derivedPullbackTensorIso :
    Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.O) ⋙
        derivedPullback f ≅
      (derivedPullback f).prod (derivedPullback f) ⋙
        Functor.uncurry.obj
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.O)
```

**`Stacks.Sheaves.DerivedPullback.OfToposHom.derivedPullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorComparisonOfToposHom.lean, line 555](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorComparisonOfToposHom.lean#L555). The attribute's comment: “the canonical bifunctorial isomorphism, for a morphism of ringed topoi whose geometric datum is a morphism of the underlying topoi rather than of the underlying sites”.

> **Stacks 07A4.** The canonical bifunctorial isomorphism
>
> `Lf^*(K ⊗^L_{O'} L) ≅ Lf^*K ⊗^L_O Lf^*L`
>
> for a morphism of ringed topoi `f : (Sh(C), O) ⟶ (Sh(D), O')` — a morphism of the underlying
> topoi together with the structure map, with no hypothesis on the underlying sites — stated
> between the two uncurried bifunctors on `D(O') × D(O')`, so that naturality in both variables
> is part of its type.
>
> Its value on a pair of K-flat complexes with flat terms is the five-step composite of the source
> (`derivedPullbackTensorModelIso`), and the passage to arbitrary objects of `D(O')` is the
> descent of that value along the localization of pairs of models.

```lean
def derivedPullbackTensorIso :
    Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.O) ⋙
        derivedPullback f ≅
      (derivedPullback f).prod (derivedPullback f) ⋙
        Functor.uncurry.obj
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.O)
```

**`Stacks.DerivedTensor.ExactFunctorTensor.derivedTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExactFunctorDerivedTensor.lean, line 467](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExactFunctorDerivedTensor.lean#L467). The attribute's comment: “for an exact functor of sheaves of modules commuting with the total tensor complex”.

> **Stacks 07A4 for an exact functor commuting with the total tensor complex.** The canonical
> bifunctorial isomorphism
>
> `LF(A ⊗^L_{O'} B) ≅ LF A ⊗^L_O LF B`,
>
> stated between the two uncurried bifunctors on `D(O') × D(O')`, so that naturality in both
> variables is part of its type.
>
> Its value on a pair of K-flat complexes with flat terms is
> `Stacks.DerivedTensor.ExactFunctorTensor.modelIso`, and the passage to arbitrary objects of
> `D(O')` is the descent of that value along the localization of pairs of models.

```lean
def derivedTensorIso :
    Functor.uncurry.obj (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor Y.O) ⋙
        F.mapDerivedCategory ≅
      F.mapDerivedCategory.prod F.mapDerivedCategory ⋙
        Functor.uncurry.obj
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.O)
```

## Tag 08I6, a lemma

[Tag 08I6](https://stacks.math.columbia.edu/tag/08I6) in the Stacks Project.

**`Stacks.Cohomology.MixedDerivedTensor.derivedMixedTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/MixedDerivedTensor/DerivedMixedTensor.lean, line 607](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/MixedDerivedTensor/DerivedMixedTensor.lean#L607). The attribute's comment: “variant: the isomorphism read in D(f⁻¹O') after restriction of scalars, for a site-presented morphism; the tag in D(O) for an arbitrary morphism of ringed topoi is Stacks.Cohomology.MixedDerivedTensor.OfToposHom.derivedMixedTensorIso”.

> **Stacks 08I6, read after restriction of scalars to `f⁻¹O'`.**  The bifunctorial
> isomorphism
>
> `(F ⊗^L_O Lf^*G)|_{f⁻¹O'} ≅ F|_{f⁻¹O'} ⊗^L_{f⁻¹O'} f⁻¹G`
>
> in `D(f⁻¹O')`, for a site-presented morphism of ringed topoi `f : (Sh(C), O) ⟶ (Sh(C'), O')`,
> `F` in `D(O)` and `G` in `D(O')`.  It is stated between the two uncurried bifunctors on
> `D(O) × D(O')`, so that naturality in both variables is part of its type.  The tag itself, in
> `D(O)` and for an arbitrary morphism of ringed topoi, is
> `Stacks.Cohomology.MixedDerivedTensor.OfToposHom.derivedMixedTensorIso`.
>
> Its value at a complex of `O`-modules and a K-flat complex of `O'`-modules with flat terms is
> the chain of the source (`derivedMixedTensorModelIso`): there both sides are computed by total
> tensor complexes and the identity is the underived one of the source, applied in each bidegree.
> The passage to arbitrary objects is the descent of that value along the localization of pairs
> of models.

```lean
def derivedMixedTensorIso :
    mixedDerivedTensorPullback f ≅ mixedDerivedTensorInverseImage f
```

**`Stacks.Cohomology.MixedDerivedTensor.OfToposHom.derivedMixedTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/MixedDerivedTensor/DerivedMixedTensorOfToposHom.lean, line 624](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/MixedDerivedTensor/DerivedMixedTensorOfToposHom.lean#L624). The attribute's comment: “the canonical bifunctorial isomorphism in D(O), for an arbitrary morphism of ringed topoi”.

> **Stacks 08I6.**  For a morphism of ringed topoi `f : (Sh(C), O) ⟶ (Sh(C'), O')` — a
> morphism of the underlying topoi together with the structure map, with no hypothesis on the
> underlying sites — the canonical bifunctorial isomorphism
>
> `F ⊗^L_O Lf^*G ≅ F ⊗^L_{f⁻¹O'} f⁻¹G`
>
> in `D(O)`, for `F` in `D(O)` and `G` in `D(O')`.  The right-hand side is the derived tensor
> product over `f⁻¹O'` (`coeffMixedDerivedTensor` along the structure map `f⁻¹O' ⟶ O`) of `F` and
> the inverse image `f⁻¹G` (`derivedInverseImage`), an object of `D(O)` through `F`.  It is stated
> between the two uncurried bifunctors on `D(O) × D(O')`, so that bifunctoriality is part of its
> type.
>
> At a complex `F` of `O`-modules and a K-flat complex `G` of `O'`-modules with flat terms both
> sides are total complexes and the isomorphism is the underived identity
> `F ⊗_{f⁻¹O'} f⁻¹G ≅ F ⊗_O f^*G` in each bidegree (`modelIso`); the passage to arbitrary objects
> is the descent along the localization of pairs of models.

```lean
def derivedMixedTensorIso :
    derivedTensorPullback f ≅ derivedMixedTensorInverseImage f
```

## Tag 0DEN, a lemma

[Tag 0DEN](https://stacks.math.columbia.edu/tag/0DEN) in the Stacks Project.

**`Stacks.SheafOfModules.SitePointStalkSheafify.kFlat_of_stalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SitePointStalkTensorSheafify.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SitePointStalkTensorSheafify.lean#L80). The attribute's comment: “part (2)”.

> **Stacks 0DEN, part (2), with no extra hypothesis.** On a ringed site whose underlying site
> has enough points, a complex of `O`-modules whose stalk at every point is a K-flat complex of
> modules over the stalk of `O` is itself K-flat.
>
> This is `Stacks.Sheaves.KFlatStalkCriterion.kFlat_of_stalks` with its
> `Stacks.Sheaves.KFlatStalkCriterion.StalkTensorData` argument supplied by `stalkTensorData`.

```lean
theorem kFlat_of_stalks (hJ : J.HasConservativeFamily.{u})
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)) ℤ)
    (hK : ∀ Ψ : J.Point.{u},
      CochainComplex.KFlat.{u, u} (Stacks.Sheaves.KFlatStalkCriterion.stalkComplex O Ψ K)) :
    Stacks.SheafOfModules.IsKFlat O K
```

**`Stacks.Sheaves.KFlatStalkCriterion.kFlatStalk_of_kFlat_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkRetractFromFreeModules.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkRetractFromFreeModules.lean#L246). The attribute's comment: “part (1)”.

> **Stacks 0DEN, part (1).**  On a ringed site, a K-flat complex of `O`-modules has K-flat
> stalk complex at every point of the site.
>
> This is `Stacks.Sheaves.KFlatStalkCriterion.kFlatStalk_of_kFlat_of_stalkRetract` with its one
> remaining obligation discharged by `stalkRetractFinitelyPresented`, so the hypotheses are
> exactly those of the source.  Part (2), the converse under the hypothesis that the site has
> enough points, is `Stacks.SheafOfModules.SitePointStalkSheafify.kFlat_of_stalks`.

```lean
theorem kFlatStalk_of_kFlat_unconditional (Φ : J.Point.{u})
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O)) ℤ)
    (hK : Stacks.SheafOfModules.IsKFlat O K) :
    CochainComplex.KFlat.{u, u} (stalkComplex O Φ K)
```

## Tag 0DEP, a lemma

[Tag 0DEP](https://stacks.math.columbia.edu/tag/0DEP) in the Stacks Project.

**`Stacks.Sheaves.DerivedPullback.KFlatPullbackMorphismOfSites.kFlat_pullbackComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeAtTheTargetPoint.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeAtTheTargetPoint.lean#L332).

> **Stacks 0DEP.**  Let `f : (Sh(C), O) ⟶ (Sh(C'), O')` be a morphism of ringed topoi whose
> underlying functor of the sites is a morphism of sites, and suppose the site `C` has a
> conservative family of points.  Then the degreewise pullback along `f` of a K-flat complex of
> `O'`-modules is a K-flat complex of `O`-modules.
>
> The proof is the source's.  K-flatness of `f^*K` is tested at the points of `C` by part (2) of
> Stacks 0DEN, which applies because `C` has a conservative family of points.  At a point `Φ` of
> `C` the stalk complex of `f^*K` is the extension of scalars, along a map `O'_Ψ ⟶ O_Φ` of stalk
> rings, of the stalk complex of `K` at the point `Ψ = f ∘ Φ` of `C'` produced by part (2) of
> Stacks 00YA; that is `stalkComplexIso`, which is Stacks 05V5 at the level of complexes, built
> from Stacks 05V1 for the inverse image and the stalkwise formula for the extension of scalars
> along `f⁻¹O' ⟶ O`.  The stalk complexes of `K` are K-flat by part (1) of Stacks 0DEN on the
> target, and extension of scalars preserves K-flatness by Stacks 06Y1.

```lean
theorem kFlat_pullbackComplex (hX : X.J.HasConservativeFamily.{u})
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ)
    (hK : Stacks.SheafOfModules.IsKFlat Y.O K) :
    Stacks.SheafOfModules.IsKFlat X.O ((KFlatPullback.pullbackComplex f).obj K)
```

**`Stacks.Sheaves.DerivedPullback.StalkBaseChangeOfToposHom.kFlat_pullbackComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeOfToposHom.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/StalkBaseChangeOfToposHom.lean#L372).

> **Stacks 0DEP.**  Let `f : (Sh(C), O) ⟶ (Sh(C'), O')` be a morphism of ringed topoi and
> suppose the site `C` has a conservative family of points.  Then the degreewise pullback along
> `f` of a K-flat complex of `O'`-modules is a K-flat complex of `O`-modules.
>
> The proof is the source's.  K-flatness of `f^*K` is tested at the points of `C` by part (2) of
> Stacks 0DEN, which applies because `C` has a conservative family of points.  At a point `Φ` of
> `C` the stalk complex of `f^*K` is the extension of scalars, along the map `O'_Ψ ⟶ O_Φ` of stalk
> rings, of the stalk complex of `K` at the point `Ψ = f ∘ Φ` of `C'` produced by part (2) of
> Stacks 00YA; that is `stalkComplexIso`, which is Stacks 05V5 at the level of complexes.  The
> stalk complexes of `K` are K-flat by part (1) of Stacks 0DEN on the target, and extension of
> scalars preserves K-flatness by Stacks 06Y1.

```lean
theorem kFlat_pullbackComplex (hX : X.J.HasConservativeFamily.{u})
    (K : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ)
    (hK : Stacks.SheafOfModules.IsKFlat Y.O K) :
    Stacks.SheafOfModules.IsKFlat X.O ((KFlatPullbackOfToposHom.pullbackComplex f).obj K)
```

## Tag 0FPH, a lemma

[Tag 0FPH](https://stacks.math.columbia.edu/tag/0FPH) in the Stacks Project.

**`Stacks.Sheaves.DerivedPullback.OfToposHom.derivedPullback_toTensor_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorTotalSquareOfToposHom.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorTotalSquareOfToposHom.lean#L172). The attribute's comment: “for an arbitrary morphism of ringed topoi in the two-field sense of Tag 01D3, part (2) (a morphism of the underlying topoi with its structure map, no functor between the underlying sites and no morphism-of-sites hypothesis), at RingedTopos.\{u, u, u}, for all complexes K, M; the statement carries no hypothesis or class argument”.

> **Stacks 0FPH, for a morphism of ringed topoi.**  For a morphism of ringed topoi
> `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` — a morphism of the underlying topoi together with the
> structure map — and cochain complexes `K`, `M` of `O_D`-modules, the square formed by the
> canonical maps from the derived tensor product to the ordinary total tensor complex, the
> comparison `Lf^*(K ⊗^L_{O_D} M) ≅ Lf^*K ⊗^L_{O_C} Lf^*M` of Stacks 07A4 followed by the
> comparison `Lf^* ⟶ f^*` in each tensor factor, and that same comparison at `Tot(K ⊗ M)`
> followed by the identification `f^*Tot(K ⊗_{O_D} M) ≅ Tot(f^*K ⊗_{O_C} f^*M)` of Stacks 03EL,
> commutes.
>
> The statement has no hypothesis and no class argument of its own: instance search supplies
> every class argument of `derivedPullback_toTensor_square_of_instances`.

```lean
theorem derivedPullback_toTensor_square {X Y : RingedTopos.{u, u, u}}
    (f : AlgebraicGeometry.RingedToposHom X Y)
    (K M : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ) :
    (derivedPullback f).map
          ((Stacks.DerivedTensor.RingedSite.canonicalDerivedTensorProduct Y.O).toTensor K M) ≫
        pullbackComparisonQ f
            (((Stacks.SheafOfModules.Tensor.tensorComplex Y.O).obj K).obj M) ≫
        DerivedCategory.Q.map (pullbackTensorComplexIso f K M).hom =
      (derivedPullbackTensorIso f).hom.app (DerivedCategory.Q.obj K, DerivedCategory.Q.obj M) ≫
        bifunctorMap (Stacks.DerivedTensor.RingedSite.canonicalDerivedTensorProduct X.O).tensor
            (pullbackComparisonQ f K) (pullbackComparisonQ f M) ≫
        (Stacks.DerivedTensor.RingedSite.canonicalDerivedTensorProduct X.O).toTensor
          ((pullbackComplex f).obj K) ((pullbackComplex f).obj M)
```

**`Stacks.Sheaves.DerivedPullback.derivedPullback_toTensor_square_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorTotalSquareUnconditional.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/DerivedPullbackTensorTotalSquareUnconditional.lean#L113). The attribute's comment: “for a morphism of ringed topoi presented by a morphism of the underlying sites, at RingedTopos.\{u, u, u}”.

> **Stacks 0FPH.** For a morphism of ringed topoi `f : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and cochain
> complexes `K`, `M` of `O_D`-modules, the square formed by the canonical maps from the derived
> tensor product to the ordinary total tensor complex, the comparison
> `Lf^*(K ⊗^L_{O_D} M) ⟶ Lf^*K ⊗^L_{O_C} Lf^*M` of Stacks 07A4 followed by the derived-to-degreewise
> pullback comparison in each tensor factor, and that same comparison followed by the
> identification `f^*Tot(K ⊗_{O_D} M) ≅ Tot(f^*K ⊗_{O_C} f^*M)`, commutes.
>
> The complexes are arbitrary and the only inputs are `f` and `hmos`. `hmos` is not a hypothesis
> beyond the source's: it is this development's encoding of "`f` is a morphism of ringed topoi".
> `AlgebraicGeometry.RingedToposSiteHom` presents the geometric morphism by a functor `f.u` between
> the underlying sites and asks only that it be *continuous*; exactness of `f^{-1}` is not a field
> of it, and along a merely continuous functor the inverse image need not be exact, so such an `f`
> need not present a morphism of topoi at all. `CategoryTheory.Functor.IsMorphismOfSites` is
> continuity together with that exactness — it is Stacks 00X1 — and it is exactly what
> `AlgebraicGeometry.RingedToposSiteHom.toToposHom` consumes to produce the underlying morphism of
> topoi.
>
> The existence of `Lf^*` is not assumed: it is `hasLeftDerivedFunctor_pullbackOnHomotopy`, the
> existence assertion of Stacks 06YY, which holds along every morphism of ringed topoi.

```lean
theorem derivedPullback_toTensor_square_unconditional
    (K M : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ) :
    haveI := hasLeftDerivedFunctor_pullbackOnHomotopy f hmos
    (derivedPullback f).map
          ((Stacks.DerivedTensor.RingedSite.canonicalDerivedTensorProduct Y.O).toTensor K M) ≫
        pullbackComparisonQ f
            (((Stacks.SheafOfModules.Tensor.tensorComplex Y.O).obj K).obj M) ≫
        DerivedCategory.Q.map (pullbackTensorComplexIso f hmos K M).hom =
      derivedPullbackTensorComparison f hmos (DerivedCategory.Q.obj K)
            (DerivedCategory.Q.obj M) ≫
        bifunctorMap (Stacks.DerivedTensor.RingedSite.canonicalDerivedTensorProduct X.O).tensor
            (pullbackComparisonQ f K) (pullbackComparisonQ f M) ≫
        (Stacks.DerivedTensor.RingedSite.canonicalDerivedTensorProduct X.O).toTensor
          ((pullbackComplex f).obj K) ((pullbackComplex f).obj M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.18, Tag 06YV](https://stacks.math.columbia.edu/tag/06YV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
