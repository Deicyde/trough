---
declaration: section
origin: cited
lean: Stacks.DerivedHom.ExtensionOfScalars.derivedHomBaseChange, Stacks.DerivedHom.BaseChangeIso.isIso_derivedHomBaseChange, Stacks.DerivedHom.BaseChange.derivedHomRestrictScalarsNatIso
statement: formalized
proof: formalized
---

# 15.101 Base change for derived hom

Section 15.101 of the Stacks Project, [Tag 0E1V](https://stacks.math.columbia.edu/tag/0E1V). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E1V, the section

[Tag 0E1V](https://stacks.math.columbia.edu/tag/0E1V) in the Stacks Project.

**`Stacks.DerivedHom.ExtensionOfScalars.derivedHomBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom/BaseChange/BaseChangeMap.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/RHom/BaseChange/BaseChangeMap.lean#L247). The attribute's comment: “the derived base-change map for derived hom”.

> **Stacks 0E1X.** The canonical derived-module base-change map
> `RHom_R(K, M) ⊗ᴸ_R A ⟶ RHom_A(K ⊗ᴸ_R A, M ⊗ᴸ_R A)`.
> It is the mate of the unit-induced map under the adjunction of Stacks 0GMT, using
> exactly the change-of-rings identification of Stacks 0E1W.

```lean
public def derivedHomBaseChange
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A) :
    letI : (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    ∀ (F : DerivedCategory (ModuleCat.{max uR uA uM} R) ⥤
      DerivedCategory (ModuleCat.{max uR uA uM} A))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uR uA uM} R) (ComplexShape.up ℤ))]
    (K M : DerivedCategory (ModuleCat.{max uR uA uM} R)),
    F.obj ((_root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uR, max uR uA uM} R).obj
      (Opposite.op K, M)) ⟶
      (_root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uA, max uR uA uM} A).obj
        (Opposite.op (F.obj K), F.obj M)
```

**`Stacks.DerivedHom.BaseChangeIso.isIso_derivedHomBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom/BaseChange/Invertibility.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/RHom/BaseChange/Invertibility.lean#L618). The attribute's comment: “invertibility of the base-change map in each of the four cases”.

> **Stacks 0A6A.** The canonical derived-Hom base-change morphism
> `RHom_R(K, M) ⊗ᴸ_R A ⟶ RHom_A(K ⊗ᴸ_R A, M ⊗ᴸ_R A)` of Stacks 0E1X is an isomorphism in each of
> four cases: `K` is perfect; `A` is perfect as an `R`-module; the ring map is flat, `K` is
> pseudo-coherent and `M` is bounded below; or `A` has finite Tor dimension over `R`, `K` is
> pseudo-coherent and `M` is bounded below.

```lean
public theorem isIso_derivedHomBaseChange
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A) :
    letI : (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    ∀ (F : Functor (DerivedCategory (ModuleCat.{max uR uA uM} R))
      (DerivedCategory (ModuleCat.{max uR uA uM} A)))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uR uA uM} R) (ComplexShape.up ℤ))]
    (K M : DerivedCategory (ModuleCat.{max uR uA uM} R)),
    (StacksDraft.Perfect.IsPerfect K ∨
      StacksDraft.Perfect.IsPerfect
        ((DerivedCategory.singleFunctor (ModuleCat.{max uR uA uM} R) 0).obj
          ((ModuleCat.restrictScalars f).obj (ModuleCat.of A (ULift.{max uR uM} A)))) ∨
      (f.Flat ∧ StacksDraft.PseudoCoherence.IsPseudoCoherent K ∧
        ∃ b : ℤ, DerivedCategory.IsGE M b) ∨
      ((let e := moduleUniverseEquiv.{uR, max uA uM} R
        letI : e.functor.Additive :=
          inferInstanceAs (ModuleCat.restrictScalars.{max uR uA uM, max uR uA uM, uR}
            (ULift.ringEquiv : ULift.{max uA uM} R ≃+* R).toRingHom).Additive
        ∃ a : ℤ, ∀ (N : ModuleCat.{max uR uA uM} R) (i : ℤ), i < a →
          IsZero ((DerivedCategory.homologyFunctor
              (ModuleCat.{max uR uA uM} (ULift.{max uA uM} R)) i).obj
            ((canonTensorMod
                (e.functor.obj N)).obj
              (e.functor.mapDerivedCategory.obj
                ((DerivedCategory.singleFunctor (ModuleCat.{max uR uA uM} R) 0).obj
                  ((ModuleCat.restrictScalars f).obj
                    (ModuleCat.of A (ULift.{max uR uM} A)))))))) ∧
        StacksDraft.PseudoCoherence.IsPseudoCoherent K ∧
        ∃ b : ℤ, DerivedCategory.IsGE M b)) →
    IsIso (Stacks.DerivedHom.ExtensionOfScalars.derivedHomBaseChange.{uR, uA, uM} f F comparison K
      M)
```

**`Stacks.DerivedHom.BaseChange.derivedHomRestrictScalarsNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom/BaseChange/ModelRestrictScalars.lean, line 737](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/RHom/BaseChange/ModelRestrictScalars.lean#L737). The attribute's comment: “the change-of-rings isomorphism for derived hom”.

> **Stacks 0E1W.** The canonical change-of-rings isomorphism for derived Hom, natural in
> the object of `D(R)` in the contravariant variable and the object of `D(A)` in the covariant
> variable. Its right-hand side uses any total left-derived extension-of-scalars functor; such a
> functor is left adjoint to derived restriction of scalars by Stacks 0GMT.

```lean
public noncomputable def derivedHomRestrictScalarsNatIso
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A) :
    letI : (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    ∀ (F : DerivedCategory (ModuleCat.{max uR uA uM} R) ⥤
      DerivedCategory (ModuleCat.{max uR uA uM} A))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uR uA uM} R) (ComplexShape.up ℤ))],
    Functor.prod
        (Functor.id (DerivedCategory (ModuleCat.{max uR uA uM} R))ᵒᵖ)
        (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).mapDerivedCategory ⋙
        _root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uR, max uR uA uM} R ≅
      Functor.prod F.op (Functor.id (DerivedCategory (ModuleCat.{max uR uA uM} A))) ⋙
        _root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uA, max uR uA uM} A ⋙
        (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).mapDerivedCategory
```

## Tag 0E1W, a lemma

[Tag 0E1W](https://stacks.math.columbia.edu/tag/0E1W) in the Stacks Project.

**`Stacks.DerivedHom.BaseChange.derivedHomRestrictScalarsNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom/BaseChange/ModelRestrictScalars.lean, line 737](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/RHom/BaseChange/ModelRestrictScalars.lean#L737).

> **Stacks 0E1W.** The canonical change-of-rings isomorphism for derived Hom, natural in
> the object of `D(R)` in the contravariant variable and the object of `D(A)` in the covariant
> variable. Its right-hand side uses any total left-derived extension-of-scalars functor; such a
> functor is left adjoint to derived restriction of scalars by Stacks 0GMT.

```lean
public noncomputable def derivedHomRestrictScalarsNatIso
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A) :
    letI : (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    ∀ (F : DerivedCategory (ModuleCat.{max uR uA uM} R) ⥤
      DerivedCategory (ModuleCat.{max uR uA uM} A))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uR uA uM} R) (ComplexShape.up ℤ))],
    Functor.prod
        (Functor.id (DerivedCategory (ModuleCat.{max uR uA uM} R))ᵒᵖ)
        (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).mapDerivedCategory ⋙
        _root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uR, max uR uA uM} R ≅
      Functor.prod F.op (Functor.id (DerivedCategory (ModuleCat.{max uR uA uM} A))) ⋙
        _root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uA, max uR uA uM} A ⋙
        (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).mapDerivedCategory
```

## Tag 0E1X, an equation

[Tag 0E1X](https://stacks.math.columbia.edu/tag/0E1X) in the Stacks Project.

**`Stacks.DerivedHom.ExtensionOfScalars.derivedHomBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom/BaseChange/BaseChangeMap.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/RHom/BaseChange/BaseChangeMap.lean#L247).

> **Stacks 0E1X.** The canonical derived-module base-change map
> `RHom_R(K, M) ⊗ᴸ_R A ⟶ RHom_A(K ⊗ᴸ_R A, M ⊗ᴸ_R A)`.
> It is the mate of the unit-induced map under the adjunction of Stacks 0GMT, using
> exactly the change-of-rings identification of Stacks 0E1W.

```lean
public def derivedHomBaseChange
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A) :
    letI : (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    ∀ (F : DerivedCategory (ModuleCat.{max uR uA uM} R) ⥤
      DerivedCategory (ModuleCat.{max uR uA uM} A))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uR uA uM} R) (ComplexShape.up ℤ))]
    (K M : DerivedCategory (ModuleCat.{max uR uA uM} R)),
    F.obj ((_root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uR, max uR uA uM} R).obj
      (Opposite.op K, M)) ⟶
      (_root_.Stacks.DerivedHom.ScalarTransportedInternalHom.hom.{uA, max uR uA uM} A).obj
        (Opposite.op (F.obj K), F.obj M)
```

## Tag 0A6A, a lemma

[Tag 0A6A](https://stacks.math.columbia.edu/tag/0A6A) in the Stacks Project.

**`Stacks.DerivedHom.BaseChangeIso.isIso_derivedHomBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/HomComplex/RHom/BaseChange/Invertibility.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/HomComplex/RHom/BaseChange/Invertibility.lean#L618).

> **Stacks 0A6A.** The canonical derived-Hom base-change morphism
> `RHom_R(K, M) ⊗ᴸ_R A ⟶ RHom_A(K ⊗ᴸ_R A, M ⊗ᴸ_R A)` of Stacks 0E1X is an isomorphism in each of
> four cases: `K` is perfect; `A` is perfect as an `R`-module; the ring map is flat, `K` is
> pseudo-coherent and `M` is bounded below; or `A` has finite Tor dimension over `R`, `K` is
> pseudo-coherent and `M` is bounded below.

```lean
public theorem isIso_derivedHomBaseChange
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A) :
    letI : (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    ∀ (F : Functor (DerivedCategory (ModuleCat.{max uR uA uM} R))
      (DerivedCategory (ModuleCat.{max uR uA uM} A)))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uR uA uM} R) (ComplexShape.up ℤ))]
    (K M : DerivedCategory (ModuleCat.{max uR uA uM} R)),
    (StacksDraft.Perfect.IsPerfect K ∨
      StacksDraft.Perfect.IsPerfect
        ((DerivedCategory.singleFunctor (ModuleCat.{max uR uA uM} R) 0).obj
          ((ModuleCat.restrictScalars f).obj (ModuleCat.of A (ULift.{max uR uM} A)))) ∨
      (f.Flat ∧ StacksDraft.PseudoCoherence.IsPseudoCoherent K ∧
        ∃ b : ℤ, DerivedCategory.IsGE M b) ∨
      ((let e := moduleUniverseEquiv.{uR, max uA uM} R
        letI : e.functor.Additive :=
          inferInstanceAs (ModuleCat.restrictScalars.{max uR uA uM, max uR uA uM, uR}
            (ULift.ringEquiv : ULift.{max uA uM} R ≃+* R).toRingHom).Additive
        ∃ a : ℤ, ∀ (N : ModuleCat.{max uR uA uM} R) (i : ℤ), i < a →
          IsZero ((DerivedCategory.homologyFunctor
              (ModuleCat.{max uR uA uM} (ULift.{max uA uM} R)) i).obj
            ((canonTensorMod
                (e.functor.obj N)).obj
              (e.functor.mapDerivedCategory.obj
                ((DerivedCategory.singleFunctor (ModuleCat.{max uR uA uM} R) 0).obj
                  ((ModuleCat.restrictScalars f).obj
                    (ModuleCat.of A (ULift.{max uR uM} A)))))))) ∧
        StacksDraft.PseudoCoherence.IsPseudoCoherent K ∧
        ∃ b : ℤ, DerivedCategory.IsGE M b)) →
    IsIso (Stacks.DerivedHom.ExtensionOfScalars.derivedHomBaseChange.{uR, uA, uM} f F comparison K
      M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.101, Tag 0E1V](https://stacks.math.columbia.edu/tag/0E1V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
