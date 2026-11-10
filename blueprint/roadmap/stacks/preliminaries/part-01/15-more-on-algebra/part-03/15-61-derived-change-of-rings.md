---
declaration: section
origin: cited
lean: CochainComplex.DerivedTensor.canonicalDerivedTensorChangeOfRings, CochainComplex.DerivedTensor.exists_derivedTensorNatTrans_isIso_of_quasiIso, CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsAdjunction, CochainComplex.DerivedChangeOfRings.derivedTensorModuleStructuresDiffer, CochainComplex.DerivedTensor.IteratedChangeOfRings.derivedTensorProduct_doubleBaseChange
statement: formalized
proof: formalized
---

# 15.61 Derived change of rings

Section 15.61 of the Stacks Project, [Tag 06Y5](https://stacks.math.columbia.edu/tag/06Y5). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06Y6, a lemma

[Tag 06Y6](https://stacks.math.columbia.edu/tag/06Y6) in the Stacks Project.

**`CochainComplex.DerivedTensor.canonicalDerivedTensorChangeOfRings`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedChangeOfRings.lean, line 1057](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedChangeOfRings.lean#L1057).

> The derived tensor product `- ⊗ᴸ_R N` from `D(R)` to `D(A)`, with derived extension of
> scalars, derived tensoring over `A` and the change-of-rings isomorphism normalized by their
> counits.

```lean
public noncomputable def canonicalDerivedTensorChangeOfRings
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A)
    (N : CochainComplex (ModuleCat.{max v uR uA} A) ℤ)
    [HasDerivedCategory.{wR} (ModuleCat.{max v uR uA} R)]
    [HasDerivedCategory.{wA} (ModuleCat.{max v uR uA} A)] :
    DerivedTensorChangeOfRings f N
```

## Tag 0BYK, a lemma

[Tag 0BYK](https://stacks.math.columbia.edu/tag/0BYK) in the Stacks Project.

**`CochainComplex.DerivedTensor.exists_derivedTensorNatTrans_isIso_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedTensorFunctoriality.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedTensorFunctoriality.lean#L115).

> A map `f : L ⟶ N` of complexes of `A`-modules induces a natural
> transformation `1 ⊗ᴸ f` between any chosen left-derived models of the change-of-rings tensor
> functors `- ⊗ᴸ_R L` and `- ⊗ᴸ_R N`. The compatibility equation says that this is the
> transformation induced by the ordinary tensor map `1 ⊗ f`. If `f` is a quasi-isomorphism, the
> induced transformation is an isomorphism of functors.
>
> The source ring universe `uR`, the target ring universe `uA` and the module universe are
> mutually independent: the two rings are related by nothing but `φ`, and the modules of both
> rings have to fit in one category, so they live at `max v uR uA`.

```lean
public theorem exists_derivedTensorNatTrans_isIso_of_quasiIso
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (φ : R →+* A)
    {L N : CochainComplex (ModuleCat.{max v uR uA} A) ℤ}
    (f : L ⟶ N)
    (FL FN : DerivedCategory (ModuleCat.{max v uR uA} R) ⥤
      DerivedCategory (ModuleCat.{max v uR uA} A))
    (αL : DerivedCategory.Q ⋙ FL ⟶
      (extendScalarsLarge.{v, uR, uA} φ ⋙ tensorRightLarge.{uA, max v uR} L) ⋙
        DerivedCategory.Q)
    (αN : DerivedCategory.Q ⋙ FN ⟶
      (extendScalarsLarge.{v, uR, uA} φ ⋙ tensorRightLarge.{uA, max v uR} N) ⋙
        DerivedCategory.Q)
    [CategoryTheory.Functor.IsLeftDerivedFunctor FL αL
      (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA} R) (ComplexShape.up ℤ))]
    [CategoryTheory.Functor.IsLeftDerivedFunctor FN αN
      (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA} R) (ComplexShape.up ℤ))] :
    letI : MonoidalCategoryStruct (ModuleCat.{max v uR uA} A) :=
      ModuleCat.liftedModuleMonoidalStruct.{uA, max v uR}
    letI : MonoidalCategory (ModuleCat.{max v uR uA} A) :=
      ModuleCat.liftedModuleMonoidal.{uA, max v uR}
    let tensorMap :
        (extendScalarsLarge.{v, uR, uA} φ ⋙ tensorRightLarge.{uA, max v uR} L) ⋙
            DerivedCategory.Q ⟶
          (extendScalarsLarge.{v, uR, uA} φ ⋙ tensorRightLarge.{uA, max v uR} N) ⋙
            DerivedCategory.Q :=
      CategoryTheory.Functor.whiskerRight
        (CategoryTheory.Functor.whiskerLeft (extendScalarsLarge.{v, uR, uA} φ)
          ((CategoryTheory.MonoidalCategory.curriedTensor
            (ModuleCat.{max v uR uA} A)).map₂CochainComplex.flip.map f))
        DerivedCategory.Q
    ∃ t : FL ⟶ FN,
      CategoryTheory.Functor.whiskerLeft DerivedCategory.Q t ≫ αN = αL ≫ tensorMap ∧
        (HomologicalComplex.quasiIso (ModuleCat.{max v uR uA} A) (ComplexShape.up ℤ) f →
          IsIso t)
```

## Tag 0GMT, a lemma

[Tag 0GMT](https://stacks.math.columbia.edu/tag/0GMT) in the Stacks Project.

**`CochainComplex.DerivedExtensionScalars.derivedExtensionScalarsAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/DerivedChangeOfRingsAdjunction.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/DerivedChangeOfRingsAdjunction.lean#L99).

> **Stacks 0GMT.** Derived extension of scalars along a homomorphism of commutative rings is
> left adjoint to derived restriction of scalars. The extension functor may be any model equipped
> with the total-left-derived universal property, since uniqueness of left derived functors
> identifies it with the model computed by K-flat resolutions.

```lean
public def derivedExtensionScalarsAdjunction
    {R : Type uR} {A : Type uA} [CommRing R] [CommRing A] (f : R →+* A)
    [HasDerivedCategory.{wR} (ModuleCat.{max uR uA uM} R)]
    [HasDerivedCategory.{wA} (ModuleCat.{max uR uA uM} A)] :
    letI : (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).IsLeftAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsRightAdjoint :=
      (ModuleCat.extendRestrictScalarsAdj.{max uR uM, uR, uA} f).isRightAdjoint
    letI : (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).IsLeftAdjoint :=
      (ModuleCat.restrictCoextendScalarsAdj.{max uR uM, uR, uA} f).isLeftAdjoint
    ∀ (F : CategoryTheory.Functor (DerivedCategory (ModuleCat.{max uR uA uM} R))
      (DerivedCategory (ModuleCat.{max uR uA uM} A)))
    (comparison : DerivedCategory.Q ⋙ F ⟶
      (ModuleCat.extendScalars.{uR, uA, max uR uA uM} f).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
    [F.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max uR uA uM} R) (ComplexShape.up ℤ))],
    F ⊣ (ModuleCat.restrictScalars.{max uR uA uM, uR, uA} f).mapDerivedCategory
```

## Tag 08YT, a remark

[Tag 08YT](https://stacks.math.columbia.edu/tag/08YT) in the Stacks Project.

**`CochainComplex.DerivedChangeOfRings.derivedTensorModuleStructuresDiffer`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/ChangeOfRings.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/ChangeOfRings.lean#L574).

> In the example `R = k[x,y]`, `A = R/(xy)`, and `N = R/(x)`, the objects
> `N_R ⊗_R^ᴸ A` and `N ⊗_R^ᴸ A_R` of `D(A)` are not isomorphic. The returned data
> includes the two displayed K-flat resolutions and augmentations, their quasi-isomorphism
> certificates, and the canonical identifications with `A → A` and `N[1] ⊕ N`.

```lean
public noncomputable def derivedTensorModuleStructuresDiffer
    (k : Type u) [CommRing k] [Nontrivial k] :
    DerivedTensorComparison k
```

## Tag 08YU, a lemma

[Tag 08YU](https://stacks.math.columbia.edu/tag/08YU) in the Stacks Project.

**`CochainComplex.DerivedTensor.IteratedChangeOfRings.derivedTensorProduct_doubleBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Tor/IteratedDerivedChangeOfRings.lean, line 1174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Tor/IteratedDerivedChangeOfRings.lean#L1174).

> Canonical associativity of derived change of rings, with its signed interchange. The
> ordinary maps send `(x ⊗ n) ⊗ k` to `x ⊗ (n ⊗ k)` and to `(-1)^(deg n * deg k) (x ⊗ k) ⊗ n`,
> respectively. These equations and the specified counits of `DerivedTensorChangeOfRings` fix the
> derived comparisons, including for nonflat `N` and `K`.
>
> `rightFactor` identifies the complex used by `together` with `N ⊗ᴸ_B K`;
> `baseFactor` identifies the second signed factor with `N ⊗ᴸ_B C`. The final isomorphism
> to extension of scalars followed by tensoring is exactly the change-of-rings projection.
> All comparisons are natural in the object of `D(A)`.

```lean
public theorem derivedTensorProduct_doubleBaseChange
    {A : Type uA} {B : Type uB} {C : Type uC} [CommRing A] [CommRing B] [CommRing C]
    (f : A →+* B) (g : B →+* C)
    (N : CochainComplex (ModuleCat.{max v uA uB uC} B) ℤ)
    (K : CochainComplex (ModuleCat.{max v uA uB uC} C) ℤ) :
    let Q_A := DerivedCategory.Q (C := ModuleCat.{max v uA uB uC} A)
    let Q_B := DerivedCategory.Q (C := ModuleCat.{max v uA uB uC} B)
    let Q_C := DerivedCategory.Q (C := ModuleCat.{max v uA uB uC} C)
    let W_A := HomologicalComplex.quasiIso
      (ModuleCat.{max v uA uB uC} A) (ComplexShape.up ℤ)
    let PN := CochainComplex.KFlat.chosenResolution.{uB, max v uA uC} N
    let LK := CochainComplex.KFlat.chosenResolution.{uC, max v uA uB} K
    let AN := canonicalDerivedTensorChangeOfRings.{uA, uB, max v uA uB uC} f N
    let AP := canonicalDerivedTensorChangeOfRings.{uA, uB, max v uA uB uC} f PN.complex
    let BK := canonicalDerivedTensorChangeOfRings.{uB, uC, max v uA uB uC} g K
    let BL := canonicalDerivedTensorChangeOfRings.{uB, uC, max v uA uB uC} g LK.complex
    let AC := canonicalDerivedTensorChangeOfRings.{uA, uC, max v uA uB uC}
      (g.comp f) (BL.directTensor.obj PN.complex)
    let AL := canonicalDerivedTensorChangeOfRings.{uA, uC, max v uA uB uC}
      (g.comp f) LK.complex
    let AK := canonicalDerivedTensorChangeOfRings.{uA, uC, max v uA uB uC} (g.comp f) K
    let CP := canonicalDerivedTensorChangeOfRings.{uC, uC, max v uA uB uC}
      (RingHom.id C)
      ((extendScalarsLarge.{max v uA uB uC, uB, uC} g).obj PN.complex)
    let iterated := AN.F ⋙ BK.F
    let together := AC.F
    let signed := AK.F ⋙ CP.F
    ∃ (replaceN : AP.F ≅ AN.F) (replaceK : BL.F ≅ BK.F) (replaceAK : AL.F ≅ AK.F),
      replaceN.hom = AP.map AN PN.π ∧
      replaceK.hom = BL.map BK LK.π ∧
      replaceAK.hom = AL.map AK LK.π ∧
      ∃ (rightFactor : BK.F.obj (Q_B.obj N) ≅ Q_C.obj (BL.directTensor.obj PN.complex))
        (baseFactor : BK.B.obj (Q_B.obj N) ≅
          Q_C.obj ((extendScalarsLarge.{max v uA uB uC, uB, uC} g).obj PN.complex)),
        BL.F.map (Q_B.map PN.π) ≫ replaceK.hom.app (Q_B.obj N) ≫ rightFactor.hom =
          BL.alphaF.app PN.complex ∧
        BK.B.map (Q_B.map PN.π) ≫ baseFactor.hom = BK.alphaB.app PN.complex ∧
        ∃ (ordinaryAssociator : AP.directTensor ⋙ BL.directTensor ≅ AC.directTensor)
          (ordinaryInterchange : AP.directTensor ⋙ BL.directTensor ≅
            AL.directTensor ⋙ CP.directTensor),
          (∀ (M : CochainComplex (ModuleCat.{max v uA uB uC} A) ℤ)
              (i j k : ℤ) (x : M.X i) (n : PN.complex.X j) (l : LK.complex.X k),
            (ordinaryAssociator.hom.app M).f ((i + j) + k)
                (BL.tensorElement (AP.directTensor.obj M) (i + j) k ((i + j) + k) rfl
                  (AP.tensorElement M i j (i + j) rfl x n) l) =
              AC.tensorElement M i (j + k) ((i + j) + k) (by omega) x
                (BL.tensorElement PN.complex j k (j + k) rfl n l)) ∧
          (∀ (M : CochainComplex (ModuleCat.{max v uA uB uC} A) ℤ)
              (i j k : ℤ) (x : M.X i) (n : PN.complex.X j) (l : LK.complex.X k),
            (ordinaryInterchange.hom.app M).f ((i + j) + k)
                (BL.tensorElement (AP.directTensor.obj M) (i + j) k ((i + j) + k) rfl
                  (AP.tensorElement M i j (i + j) rfl x n) l) =
              (-1 : C) ^ (j * k).natAbs •
                CP.tensorElement (AL.directTensor.obj M) (i + k) j ((i + j) + k)
                  (by omega) (AL.tensorElement M i k (i + k) rfl x l)
                  ((1 : C) ⊗ₜ[B,g] n)) ∧
          let replaceIterated := Functor.isoWhiskerRight replaceN BL.F ≪≫
            Functor.isoWhiskerLeft AN.F replaceK
          let replaceSigned := Functor.isoWhiskerRight replaceAK CP.F
          let direct := (AP.directTensor ⋙ BL.directTensor) ⋙ Q_C
          let iteratedComparison : Q_A ⋙ iterated ⟶ direct :=
            Functor.whiskerLeft Q_A replaceIterated.inv ≫ compositeCounit.{uA, uB, uC, v} AP BL
          let togetherComparison : Q_A ⋙ together ⟶ direct :=
            AC.alphaF ≫ Functor.whiskerRight ordinaryAssociator.inv Q_C
          let signedCounit := Functor.whiskerLeft Q_A replaceSigned.inv ≫
            compositeCounit.{uA, uC, uC, max v uB} AL CP
          iterated.IsLeftDerivedFunctor iteratedComparison W_A ∧
          together.IsLeftDerivedFunctor togetherComparison W_A ∧
          ∃ (doubleBaseChange : iterated ≅ together)
            (signedComparison : iterated ≅ signed)
            (baseChangeComparison : iterated ≅ AC.B ⋙ AC.G),
            Functor.whiskerLeft Q_A doubleBaseChange.hom ≫ togetherComparison =
              iteratedComparison ∧
            (∀ e : iterated ≅ together,
              Functor.whiskerLeft Q_A e.hom ≫ togetherComparison = iteratedComparison →
                e = doubleBaseChange) ∧
            Functor.whiskerLeft Q_A signedComparison.hom ≫ signedCounit =
              iteratedComparison ≫ Functor.whiskerRight ordinaryInterchange.hom Q_C ∧
            (∀ e : iterated ≅ signed,
              Functor.whiskerLeft Q_A e.hom ≫ signedCounit =
                iteratedComparison ≫ Functor.whiskerRight ordinaryInterchange.hom Q_C →
                  e = signedComparison) ∧
            baseChangeComparison = doubleBaseChange ≪≫ AC.changeOfRings
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.61, Tag 06Y5](https://stacks.math.columbia.edu/tag/06Y5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
