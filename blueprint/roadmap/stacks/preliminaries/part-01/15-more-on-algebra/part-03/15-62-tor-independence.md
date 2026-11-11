---
declaration: section
origin: cited
lean: RingTheory.TorIndependence.canonicalBaseChangeComparison_paste, RingTheory.TorIndependence.canonicalBaseChangeComparison_localization, RingTheory.TorIndependence.derivedBaseChangeComparison, RingTheory.TorIndependence.TorIndependent, RingTheory.TorIndependence.derivedBaseChangeComparison_isIso_of_torIndependent, RingTheory.TorIndependence.isIso_torExtensionMap_of_flat, RingTheory.TorIndependence.torIndependent_tensorProduct_of_flat, RingTheory.TorIndependence.derivedBaseChangeHomologyIso_of_flat
statement: formalized
proof: formalized
---

# 15.62 Tor independence

Section 15.62 of the Stacks Project, [Tag 065Y](https://stacks.math.columbia.edu/tag/065Y). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 065Z, an equation

[Tag 065Z](https://stacks.math.columbia.edu/tag/065Z) in the Stacks Project.

**`RingTheory.TorIndependence.canonicalBaseChangeComparison_paste`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/BaseChangeIndependence/ComparisonPasting.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/BaseChangeIndependence/ComparisonPasting.lean#L457). The attribute's comment: “the comparison of a horizontal composite of two commutative squares of rings is the composite of the two comparisons, read through the composition isomorphisms of derived extension of scalars; this is what compatibility of the comparison with localizing a square amounts to”.

> **The pasting law of Tag 065Z.** For two commutative squares of commutative rings stacked on
> top of one another, the comparison of the outer square agrees with the comparison of the lower
> square, extended along the upper left map, followed by the comparison of the upper square — both
> read through the composition isomorphisms of derived extension of scalars.
>
> Both sides are determined by the same counit equation at K-flat complexes, so the identity
> reduces to the underived comparison on pure tensors.

```lean
public theorem canonicalBaseChangeComparison_paste
    (f : R →+* A) (g₁ : R →+* R') (h₁ : A →+* A') (i₁ : R' →+* A')
    (g₂ : R' →+* R'') (h₂ : A' →+* A'') (i₂ : R'' →+* A'')
    (sq₁ : h₁.comp f = i₁.comp g₁) (sq₂ : h₂.comp i₁ = i₂.comp g₂)
    (X : DerivedCategory (ModuleCat.{u} A)) :
    (totalDerivedExtensionScalarsComp.{u, u} g₁ g₂).hom.app
        ((ModuleCat.restrictScalars.{u} f).mapDerivedCategory.obj X) ≫
      (canonicalBaseChangeComparison.{u, w} f (g₂.comp g₁) (h₂.comp h₁) i₂
        (comp_comp_eq_comp_comp f g₁ h₁ i₁ g₂ h₂ i₂ sq₁ sq₂)).app X =
    (totalDerivedExtensionScalars.{u, u, u} g₂).functor.map
        ((canonicalBaseChangeComparison.{u, w} f g₁ h₁ i₁ sq₁).app X) ≫
      (canonicalBaseChangeComparison.{u, w} i₁ g₂ h₂ i₂ sq₂).app
        ((totalDerivedExtensionScalars.{u, u, u} h₁).functor.obj X) ≫
      (ModuleCat.restrictScalars.{u} i₂).mapDerivedCategory.map
        ((totalDerivedExtensionScalarsComp.{u, u} h₁ h₂).hom.app X)
```

**`RingTheory.TorIndependence.canonicalBaseChangeComparison_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/BaseChangeIndependence/ComparisonPasting.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/BaseChangeIndependence/ComparisonPasting.lean#L511). The attribute's comment: “the comparison is compatible with localizing a square at a prime: pasting a square with the localization square of its right-hand column composes the two comparisons”.

> **Tag 065Z is compatible with localizing a square at a prime.** Pasting a commutative square
> of rings with the localization square of its right-hand column at a prime `y` of `A'` composes
> the two comparisons: the comparison of the square
>
> `R → A`, `R → R'_{y ∩ R'}`, `A → A'_y`, `R'_{y ∩ R'} → A'_y`
>
> is the comparison of the given square, extended along `R' → R'_{y ∩ R'}`, followed by the
> comparison of the localization square.  This is
> `RingTheory.TorIndependence.canonicalBaseChangeComparison_paste` with the localization square as
> its second floor.
>
> Note that the localization square is *not* a pushout square; Tag 065Z attaches a comparison to
> every commutative square, and that is all this uses.

```lean
public theorem canonicalBaseChangeComparison_localization
    (f : R →+* A) (g : R →+* R') (h : A →+* A') (i : R' →+* A')
    (sq : h.comp f = i.comp g) (y : Ideal A') [y.IsPrime]
    [HasDerivedCategory.{w} (ModuleCat.{u} (Localization.AtPrime (y.comap i)))]
    [HasDerivedCategory.{w} (ModuleCat.{u} (Localization.AtPrime y))]
    (X : DerivedCategory (ModuleCat.{u} A)) :
    (totalDerivedExtensionScalarsComp.{u, u} g
          (algebraMap R' (Localization.AtPrime (y.comap i)))).hom.app
        ((ModuleCat.restrictScalars.{u} f).mapDerivedCategory.obj X) ≫
      (canonicalBaseChangeComparison.{u, w} f
        ((algebraMap R' (Localization.AtPrime (y.comap i))).comp g)
        ((algebraMap A' (Localization.AtPrime y)).comp h)
        (Localization.localRingHom (y.comap i) y i rfl)
        (comp_comp_eq_comp_comp f g h i (algebraMap R' (Localization.AtPrime (y.comap i)))
          (algebraMap A' (Localization.AtPrime y))
          (Localization.localRingHom (y.comap i) y i rfl) sq
          (comp_algebraMap_eq_localRingHom_comp i y))).app X =
    (totalDerivedExtensionScalars.{u, u, u}
          (algebraMap R' (Localization.AtPrime (y.comap i)))).functor.map
        ((canonicalBaseChangeComparison.{u, w} f g h i sq).app X) ≫
      (canonicalBaseChangeComparison.{u, w} i
          (algebraMap R' (Localization.AtPrime (y.comap i)))
          (algebraMap A' (Localization.AtPrime y))
          (Localization.localRingHom (y.comap i) y i rfl)
          (comp_algebraMap_eq_localRingHom_comp i y)).app
        ((totalDerivedExtensionScalars.{u, u, u} h).functor.obj X) ≫
      (ModuleCat.restrictScalars.{u}
            (Localization.localRingHom (y.comap i) y i rfl)).mapDerivedCategory.map
        ((totalDerivedExtensionScalarsComp.{u, u} h
          (algebraMap A' (Localization.AtPrime y))).hom.app X)
```

**`RingTheory.TorIndependence.derivedBaseChangeComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/Independence.lean, line 1049](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/Independence.lean#L1049).

> Let `R → A`, `R → R'`, `A → A'`, and `R' → A'` be a commutative square of
> commutative rings. There is a natural comparison
> `K ⊗ᴸ_R R' ⟶ K ⊗ᴸ_A A'` in `D(R')`.
>
> The first component of the result is the underived comparison, normalized on pure tensors.
> The second is its canonical lift between any chosen models of the two total left-derived
> functors; the displayed factorization records canonicity as well as functoriality in `K`.

```lean
public noncomputable def derivedBaseChangeComparison
    {R : Type uR} {A : Type uA} {R' : Type uRp} {A' : Type uAp}
    [CommRing R] [CommRing A] [CommRing R'] [CommRing A']
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} R)]
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} A)]
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} R')]
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} A')]
    (f : R →+* A) (g : R →+* R') (h : A →+* A') (i : R' →+* A')
    (sq : h.comp f = i.comp g) :
    let Res_f := ModuleCat.restrictScalars.{max v uR uA uRp uAp} f
    let Res_i := ModuleCat.restrictScalars.{max v uR uA uRp uAp} i
    let Ext_g := ModuleCat.extendScalars.{uR, uRp, max v uR uA uRp uAp} g
    let Ext_h := ModuleCat.extendScalars.{uA, uAp, max v uR uA uRp uAp} h
    letI : (ModuleCat.restrictScalars.{max v uR uA uRp uAp} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max v uR uA uRp uAp, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max v uR uA uRp uAp} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max v uR uA uRp uAp, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max v uR uA uRp uAp} i).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max v uR uA uRp uAp, uRp, uAp} i).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max v uR uA uRp uAp} i).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max v uR uA uRp uAp, uRp, uAp} i).isRightAdjoint
    let F_R := Res_f ⋙ Ext_g
    let F_A := Ext_h ⋙ Res_i
    let U_g := Ext_g.mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R')
    let U_h := Ext_h.mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} A')
    ∀ (L_g : DerivedCategory (ModuleCat.{max v uR uA uRp uAp} R) ⥤
          DerivedCategory (ModuleCat.{max v uR uA uRp uAp} R'))
      (L_h : DerivedCategory (ModuleCat.{max v uR uA uRp uAp} A) ⥤
          DerivedCategory (ModuleCat.{max v uR uA uRp uAp} A'))
      (alpha_g : DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R) ⋙ L_g ⟶ U_g)
      (alpha_h : DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} A) ⋙ L_h ⟶ U_h),
      [L_g.IsLeftDerivedFunctor alpha_g
        (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA uRp uAp} R) (ComplexShape.up ℤ))] →
      [L_h.IsLeftDerivedFunctor alpha_h
        (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA uRp uAp} A) (ComplexShape.up ℤ))] →
      let DRes_f := Res_f.mapDerivedCategory
      let DRes_i := Res_i.mapDerivedCategory
      let beta_R :
          DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} A) ⋙ (DRes_f ⋙ L_g) ⟶
            F_R.mapHomologicalComplex (ComplexShape.up ℤ) ⋙
              DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R') :=
        (Functor.associator _ _ _).inv ≫
          Functor.whiskerRight Res_f.mapDerivedCategoryFactors.hom L_g ≫
          (Functor.associator _ _ _).hom ≫
          Functor.whiskerLeft (Res_f.mapHomologicalComplex (ComplexShape.up ℤ)) alpha_g ≫
          (Functor.associator _ _ _).inv ≫
          Functor.whiskerRight
            (Functor.mapHomologicalComplexCompIso (Iso.refl F_R)
              (ComplexShape.up ℤ)).hom
            (DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R'))
      let beta_A :
          DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} A) ⋙ (L_h ⋙ DRes_i) ⟶
            F_A.mapHomologicalComplex (ComplexShape.up ℤ) ⋙
              DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R') :=
        (Functor.associator _ _ _).inv ≫
          Functor.whiskerRight alpha_h DRes_i ≫
          (Functor.associator _ _ _).hom ≫
          Functor.whiskerLeft (Ext_h.mapHomologicalComplex (ComplexShape.up ℤ))
            Res_i.mapDerivedCategoryFactors.hom ≫
          (Functor.associator _ _ _).inv ≫
          Functor.whiskerRight
            (Functor.mapHomologicalComplexCompIso (Iso.refl F_A)
              (ComplexShape.up ℤ)).hom
            (DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R'))
      Σ' (tau0 : F_R ⟶ F_A),
        {tau : DRes_f ⋙ L_g ⟶ L_h ⋙ DRes_i //
          (∀ (M : ModuleCat.{max v uR uA uRp uAp} A) (r' : R') (m : M),
            tau0.app M (r' ⊗ₜ[R,g] m) = (i r') ⊗ₜ[A,h] m) ∧
          Functor.whiskerLeft (DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} A)) tau ≫
            beta_A =
            beta_R ≫ Functor.whiskerRight
                (NatTrans.mapHomologicalComplex tau0 (ComplexShape.up ℤ))
                (DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R'))}
```

## Tag 0660, a definition

[Tag 0660](https://stacks.math.columbia.edu/tag/0660) in the Stacks Project.

**`RingTheory.TorIndependence.TorIndependent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/Independence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/Independence.lean#L94). References: SGA 6 III (1.5), “affine case”.

> Two `R`-algebras are Tor independent over `R` when their positive-degree
> Tor modules over `R` vanish.

```lean
public def TorIndependent (R : Type uR) (A : Type uA) (B : Type uB)
    [CommRing R] [CommRing A] [CommRing B] [Algebra R A] [Algebra R B] : Prop
```

## Tag 0661, a lemma

[Tag 0661](https://stacks.math.columbia.edu/tag/0661) in the Stacks Project.

**`RingTheory.TorIndependence.derivedBaseChangeComparison_isIso_of_torIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/IndependenceBaseChange.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/IndependenceBaseChange.lean#L768).

> **Stacks 0661.** If `A` and `R'` are Tor independent over `R`, then the canonical comparison
> from derived base change over `R` to derived base change over `A` is an isomorphism, for every
> pushout square with upper-right corner `A'`.

```lean
public theorem derivedBaseChangeComparison_isIso_of_torIndependent
    {R : Type uR} {A : Type uA} {R' : Type uRp} {A' : Type uAp}
    [CommRing R] [CommRing A] [CommRing R'] [CommRing A']
    [Algebra R A] [Algebra R R'] [Algebra R A'] [Algebra A A'] [Algebra R' A']
    [IsScalarTower R A A'] [IsScalarTower R R' A'] [Algebra.IsPushout R A R' A']
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} R)]
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} A)]
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} R')]
    [HasDerivedCategory (ModuleCat.{max v uR uA uRp uAp} A')]
    (hTor : TorIndependent R A R') :
    let f : R →+* A := algebraMap R A
    let g : R →+* R' := algebraMap R R'
    let h : A →+* A' := algebraMap A A'
    let i : R' →+* A' := algebraMap R' A'
    let sq : h.comp f = i.comp g := by
      exact (IsScalarTower.algebraMap_eq R A A').symm.trans
        (IsScalarTower.algebraMap_eq R R' A')
    let Ext_g := ModuleCat.extendScalars.{uR, uRp, max v uR uA uRp uAp} g
    let Ext_h := ModuleCat.extendScalars.{uA, uAp, max v uR uA uRp uAp} h
    letI : Ext_g.IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max v uR uA uRp uAp, uR, uRp}
        g).isLeftAdjoint
    letI : Ext_h.IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max v uR uA uRp uAp, uA, uAp}
        h).isLeftAdjoint
    let U_g := Ext_g.mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R')
    let U_h := Ext_h.mapHomologicalComplex (ComplexShape.up ℤ) ⋙
      DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} A')
    ∀ (L_g : DerivedCategory (ModuleCat.{max v uR uA uRp uAp} R) ⥤
          DerivedCategory (ModuleCat.{max v uR uA uRp uAp} R'))
      (L_h : DerivedCategory (ModuleCat.{max v uR uA uRp uAp} A) ⥤
          DerivedCategory (ModuleCat.{max v uR uA uRp uAp} A'))
      (alpha_g : DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} R) ⋙ L_g ⟶ U_g)
      (alpha_h : DerivedCategory.Q (C := ModuleCat.{max v uR uA uRp uAp} A) ⋙ L_h ⟶ U_h),
      [L_g.IsLeftDerivedFunctor alpha_g
        (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA uRp uAp} R)
          (ComplexShape.up ℤ))] →
      [L_h.IsLeftDerivedFunctor alpha_h
        (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA uRp uAp} A)
          (ComplexShape.up ℤ))] →
      let comparison := derivedBaseChangeComparison f g h i sq
        L_g L_h alpha_g alpha_h
      IsIso comparison.2.1
```

## Tag 08HW, a lemma

[Tag 08HW](https://stacks.math.columbia.edu/tag/08HW) in the Stacks Project.

**`RingTheory.TorIndependence.isIso_torExtensionMap_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/Independence.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/Independence.lean#L352).

> **Stacks 08HW.** If `R'` is flat over `R`, `A'` is flat over `A ⊗[R] R'`, and
> `B'` is flat over `R' ⊗[R] B`, the canonical scalar-extended change-of-rings map on
> ordinary Tor is an isomorphism. The diagram is lifted to the maximum of its six independent
> universes so that Mathlib's categorical Tor and extension-of-scalars constructions apply.

```lean
public theorem isIso_torExtensionMap_of_flat
    (R : Type uR) (R' : Type uS) (A : Type uA) (B : Type uB)
    (A' : Type uC) (B' : Type uD)
    [CommRing R] [CommRing R'] [CommRing A] [CommRing B] [CommRing A'] [CommRing B']
    [Algebra R R'] [Algebra R A] [Algebra R B] [Algebra R A'] [Algebra R B']
    [Algebra R' A'] [Algebra R' B'] [IsScalarTower R R' A'] [IsScalarTower R R' B']
    (fA : A →ₐ[R] A') (fB : B →ₐ[R] B')
    (hR' : RingHom.Flat (algebraMap R R'))
    (hA' : RingHom.Flat (Algebra.TensorProduct.lift fA
      (IsScalarTower.toAlgHom R R' A') (fun _ _ ↦ Commute.all _ _)).toRingHom)
    (hB' : RingHom.Flat (Algebra.TensorProduct.lift
      (IsScalarTower.toAlgHom R R' B') fB (fun _ _ ↦ Commute.all _ _)).toRingHom)
    (i : ℕ) :
    IsIso (TorChangeOfRings.extensionMap TorChangeOfRings.canonicalSystem_nonempty
      (ULift.{max uR uS uA uB uC uD} R) (ULift.{max uR uS uA uB uC uD} R')
      (ULift.{max uR uS uA uB uC uD} A) (ULift.{max uR uS uA uB uC uD} B)
      (ULift.{max uR uS uA uB uC uD} A') (ULift.{max uR uS uA uB uC uD} B')
      i fA.ulift fB.ulift)
```

## Tag 0FXF, a lemma

[Tag 0FXF](https://stacks.math.columbia.edu/tag/0FXF) in the Stacks Project.

**`RingTheory.TorIndependence.torIndependent_tensorProduct_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/Independence.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/Independence.lean#L566).

> **Stacks 0FXF.** Tor independence of two algebras is preserved by extension of scalars along
> a flat map of commutative rings.

```lean
public theorem torIndependent_tensorProduct_of_flat
    (R : Type uR) (R' : Type uS) (A : Type uA) (B : Type uB)
    [CommRing R] [CommRing R'] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra R B] [Algebra R R']
    (h : TorIndependent R A B)
    (hR' : RingHom.Flat (algebraMap R R')) :
    let _ : Algebra R' (A ⊗[R] R') := Algebra.TensorProduct.rightAlgebra
    let _ : Algebra R' (B ⊗[R] R') := Algebra.TensorProduct.rightAlgebra
    TorIndependent R' (A ⊗[R] R') (B ⊗[R] R')
```

## Tag 0DJD, a lemma

[Tag 0DJD](https://stacks.math.columbia.edu/tag/0DJD) in the Stacks Project.

**`RingTheory.TorIndependence.derivedBaseChangeHomologyIso_of_flat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/FlatBaseChangeHomology.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/FlatBaseChangeHomology.lean#L200).

> **Stacks 0DJD.** Under the flatness hypotheses of Tag 08HW, the cohomology of
> `(M ⊗ᴸ_A A') ⊗ᴸ_{R'} B'` is canonically and naturally isomorphic, as a module over
> `A' ⊗[R'] B'`, to the extension of scalars of the cohomology of `M ⊗ᴸ_R B` along
> `A ⊗[R] B → A' ⊗[R'] B'`.

```lean
public def derivedBaseChangeHomologyIso_of_flat
    (R R' A B A' B' : Type u)
    [CommRing R] [CommRing R'] [CommRing A] [CommRing B] [CommRing A'] [CommRing B']
    [Algebra R R'] [Algebra R A] [Algebra R B] [Algebra R A'] [Algebra R B']
    [Algebra R' A'] [Algebra R' B'] [IsScalarTower R R' A'] [IsScalarTower R R' B']
    (fA : A →ₐ[R] A') (fB : B →ₐ[R] B')
    (hR' : RingHom.Flat (algebraMap R R'))
    (hA' : RingHom.Flat (Algebra.TensorProduct.lift fA
      (IsScalarTower.toAlgHom R R' A') (fun _ _ ↦ Commute.all _ _)).toRingHom)
    (hB' : RingHom.Flat (Algebra.TensorProduct.lift
      (IsScalarTower.toAlgHom R R' B') fB (fun _ _ ↦ Commute.all _ _)).toRingHom)
    (i : ℤ) :
    let C := A ⊗[R] B
    let C' := A' ⊗[R'] B'
    let extAA' := (totalDerivedExtensionScalars.{u, u, u} fA.toRingHom).functor
    let extAC := (totalDerivedExtensionScalars.{u, u, u}
      (Algebra.TensorProduct.includeLeftRingHom : A →+* C)).functor
    let extA'C' := (totalDerivedExtensionScalars.{u, u, u}
      (Algebra.TensorProduct.includeLeftRingHom : A' →+* C')).functor
    let g : C →+* C' :=
      TorChangeOfRings.tensorProductMap R R' A B A' B' fA fB
    extAA' ⋙ extA'C' ⋙ DerivedCategory.homologyFunctor (ModuleCat.{u} C') i ≅
      extAC ⋙ DerivedCategory.homologyFunctor (ModuleCat.{u} C) i ⋙
        ModuleCat.extendScalars g
```

## Tag 08HX, a lemma

[Tag 08HX](https://stacks.math.columbia.edu/tag/08HX) in the Stacks Project.

**`RingTheory.TorIndependence.torIndependent_localizations_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/Independence.lean, line 706](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/Independence.lean#L706).

> **Stacks 08HX.** For `R`-algebras `A` and `B`, the following are equivalent:
>
> 1. `A` and `B` are Tor independent over `R`;
> 2. `A_p` and `B_q` are Tor independent over `R_r` whenever `p` and `q` lie over `r`;
> 3. every positive-degree Tor module of `A` and `B` vanishes after localization at every
>    prime of `A ⊗[R] B`.

```lean
public theorem torIndependent_localizations_tfae
    (R A B : Type u) [CommRing R] [CommRing A] [CommRing B]
    [Algebra R A] [Algebra R B] :
    List.TFAE [
      TorIndependent R A B,
      (∀ (r : PrimeSpectrum R) (p : PrimeSpectrum A) (q : PrimeSpectrum B)
        (hp : r.asIdeal = p.asIdeal.comap (algebraMap R A))
        (hq : r.asIdeal = q.asIdeal.comap (algebraMap R B)),
        letI : p.asIdeal.LiesOver r.asIdeal := ⟨hp⟩
        letI : q.asIdeal.LiesOver r.asIdeal := ⟨hq⟩
        letI : Algebra (Localization.AtPrime r.asIdeal)
            (Localization.AtPrime p.asIdeal) :=
          Localization.AtPrime.algebraOfLiesOver r.asIdeal p.asIdeal
        letI : Algebra (Localization.AtPrime r.asIdeal)
            (Localization.AtPrime q.asIdeal) :=
          Localization.AtPrime.algebraOfLiesOver r.asIdeal q.asIdeal
        TorIndependent (Localization.AtPrime r.asIdeal)
          (Localization.AtPrime p.asIdeal) (Localization.AtPrime q.asIdeal)),
      (∀ (i : ℕ), 0 < i → ∀ s : PrimeSpectrum (A ⊗[R] B),
        letI := TorChangeOfRings.moduleStructure
          TorChangeOfRings.canonicalSystem_nonempty R A B i
        Subsingleton
          (LocalizedModule s.asIdeal.primeCompl (TorChangeOfRings.torObj R i A B)))]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.62, Tag 065Y](https://stacks.math.columbia.edu/tag/065Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
