---
declaration: section
origin: cited
lean: AlgebraicGeometry.affineDerivedPushforward_comparison, AlgebraicGeometry.affineRightDerivedPushforward_mem, AlgebraicGeometry.affinePushforwardPreservesFiniteLimits, AlgebraicGeometry.affinePushforwardPreservesFiniteColimits, AlgebraicGeometry.isRightDerivedFunctor_quasicoherentPushforward_mapDerivedCategory, AlgebraicGeometry.derivedQuasicoherentComparisonSquare, AlgebraicGeometry.flatPushforwardCoheratorIso, Stacks.DerivedQCoh.coheratorSpecIso
statement: formalized
proof: formalized
---

# 36.7 The coherator

Section 36.7 of the Stacks Project, [Tag 08D6](https://stacks.math.columbia.edu/tag/08D6). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08D7, a lemma

[Tag 08D7](https://stacks.math.columbia.edu/tag/08D7) in the Stacks Project.

**`AlgebraicGeometry.affineDerivedPushforward_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedPushforwardComparison.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedPushforwardComparison.lean#L61). The attribute's comment: “comparison square”.

> **Stacks Project, Tag 08D7.** Comparison with an arbitrary right derived pushforward of all
> sheaves of modules. This is the commutative square of the source, up to the unique natural
> isomorphism whose inverse agrees with the derivation unit `α` on every homotopy complex of
> quasi-coherent modules, after the canonical termwise identifications.

```lean
public theorem affineDerivedPushforward_comparison {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsAffineHom f]
    (RF : DerivedCategory X.Modules ⥤ DerivedCategory Y.Modules)
    (α : (Scheme.Modules.pushforward f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))] :
    let I : Scheme.QuasicoherentModules X ⥤ X.Modules :=
      (SheafOfModules.isQuasicoherent X.ringCatSheaf).ι
    let J : Scheme.QuasicoherentModules Y ⥤ Y.Modules :=
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf).ι
    letI : I.Additive := CategoryTheory.Functor.fullSubcategoryInclusion_additive _
    letI : J.Additive := CategoryTheory.Functor.fullSubcategoryInclusion_additive _
    letI : PreservesFiniteLimits I :=
      Stacks.AlgebraicGeometry.QuasicoherentDerived.isQuasicoherent_ι_preservesFiniteLimits X
    letI : PreservesFiniteColimits I :=
      Stacks.AlgebraicGeometry.QuasicoherentDerived.isQuasicoherent_ι_preservesFiniteColimits X
    letI : PreservesFiniteLimits J :=
      Stacks.AlgebraicGeometry.QuasicoherentDerived.isQuasicoherent_ι_preservesFiniteLimits Y
    letI : PreservesFiniteColimits J :=
      Stacks.AlgebraicGeometry.QuasicoherentDerived.isQuasicoherent_ι_preservesFiniteColimits Y
    let F := quasicoherentPushforward f
    let G := Scheme.Modules.pushforward f
    ∃! e : (Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparison X ⋙
          affineRightDerivedPushforward f RF α) ≅
        (F.mapDerivedCategory ⋙
          Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparison Y),
      ∀ K : HomotopyCategory (Scheme.QuasicoherentModules X) (ComplexShape.up ℤ),
        (e.inv.app (DerivedCategory.Qh.obj K)).hom ≫
            RF.map (I.mapDerivedCategoryFactorsh.hom.app K) =
          J.mapDerivedCategory.map (F.mapDerivedCategoryFactorsh.hom.app K) ≫
            J.mapDerivedCategoryFactorsh.hom.app
              ((F.mapHomotopyCategory (ComplexShape.up ℤ)).obj K) ≫
            DerivedCategory.Qh.map
              ((Functor.mapHomotopyCategoryCompIso (Iso.refl (F ⋙ J))
                  (ComplexShape.up ℤ)).hom.app K ≫
                (Functor.mapHomotopyCategoryCompIso (Iso.refl (I ⋙ G))
                  (ComplexShape.up ℤ)).inv.app K) ≫
            α.app ((I.mapHomotopyCategory (ComplexShape.up ℤ)).obj K)
```

**`AlgebraicGeometry.affineRightDerivedPushforward_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedPushforwardQcoh.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedPushforwardQcoh.lean#L52). The attribute's comment: “quasi-coherent cohomology of derived pushforward”.

> **Stacks Project, Tag 08D7.** The derived direct image along an affine morphism of schemes
> takes a complex of `𝒪_X`-modules with quasi-coherent cohomology to a complex of `𝒪_Y`-modules
> with quasi-coherent cohomology.

```lean
public theorem affineRightDerivedPushforward_mem {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsAffineHom f]
    (RF : DerivedCategory X.Modules ⥤ DerivedCategory Y.Modules)
    (α : (Scheme.Modules.pushforward f).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))]
    (E : QuasicoherentDerivedCategory X) :
    (DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent Y.ringCatSheaf)) (RF.obj E.obj)
```

**`AlgebraicGeometry.affinePushforwardPreservesFiniteLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffinePushforwardExact.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffinePushforwardExact.lean#L62). The attribute's comment: “exactness, kernels”.

> **Stacks Project, Tag 08D7.** Pushforward along an affine morphism preserves finite limits
> of quasi-coherent modules.

```lean
public instance affinePushforwardPreservesFiniteLimits {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsAffineHom f] : PreservesFiniteLimits (quasicoherentPushforward f)
```

**`AlgebraicGeometry.affinePushforwardPreservesFiniteColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffinePushforwardExact.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffinePushforwardExact.lean#L94). The attribute's comment: “exactness, cokernels”.

> **Stacks Project, Tag 08D7.** Pushforward along an affine morphism preserves finite colimits
> of quasi-coherent modules.

```lean
public instance affinePushforwardPreservesFiniteColimits {X Y : Scheme.{u}} (f : X ⟶ Y)
    [IsAffineHom f] : PreservesFiniteColimits (quasicoherentPushforward f)
```

**`AlgebraicGeometry.isRightDerivedFunctor_quasicoherentPushforward_mapDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean#L203). The attribute's comment: “the derived functor”.

> **Pushforward along an affine morphism defines a derived functor
> `D(QCoh(𝒪_X)) ⥤ D(QCoh(𝒪_Y))`.** This is the first assertion of [Stacks, Tag 08D7]: the functor
> induced on unbounded derived categories by the exact functor
> `AlgebraicGeometry.quasicoherentPushforward`, namely
> `CategoryTheory.Functor.mapDerivedCategory`, is a total right derived functor of it, so no
> resolutions are involved and the derived functor is computed by applying `f_*` to a representative
> complex.
>
> The structure map is `CategoryTheory.Functor.mapDerivedCategoryFactorsh.inv`, which exhibits the
> induced functor as a lift through the localization `DerivedCategory.Qh`; a lift of a functor that
> inverts the quasi-isomorphisms is a right derived functor for the inverse of the lifting
> isomorphism.

```lean
public theorem isRightDerivedFunctor_quasicoherentPushforward_mapDerivedCategory
    {X Y : Scheme.{u}} (f : X ⟶ Y) [IsAffineHom f] :
    (quasicoherentPushforward f).mapDerivedCategory.IsRightDerivedFunctor
      (quasicoherentPushforward f).mapDerivedCategoryFactorsh.inv
      (HomotopyCategory.quasiIso (Scheme.QuasicoherentModules X) (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.derivedQuasicoherentComparisonSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean#L316). The attribute's comment: “the commuting square”.

> **Stacks 08D7, the commuting square.** For `f : X ⟶ Y` an affine morphism of schemes the
> square
> `D(QCoh(𝒪_X)) ⟶ D_QCoh(𝒪_X) ⟶ D_QCoh(𝒪_Y)`, `D(QCoh(𝒪_X)) ⟶ D(QCoh(𝒪_Y)) ⟶ D_QCoh(𝒪_Y)`
> commutes: the comparison functor of [Stacks, Tag 06VT] carries the derived functor of direct image
> on quasi-coherent modules to the restriction of the unbounded derived direct image.
>
> The two edges are compared after the fully faithful inclusion `D_QCoh(𝒪_Y) ⥤ D(𝒪_Y)`, where the
> comparison functor becomes the derived inclusion
> (`Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparisonCompι`) and the
> square becomes `AlgebraicGeometry.mapDerivedCategoryQuasicoherentPushforwardCompιIso`, which is
> [Stacks, Tag 0G9N] for an affine morphism.

```lean
public def derivedQuasicoherentComparisonSquare {X Y : Scheme.{u}} (f : X ⟶ Y) [IsAffineHom f] :
    derivedQuasicoherentComparison.{u} X ⋙ derivedQuasicoherentPushforward f ≅
      (quasicoherentPushforward f).mapDerivedCategory ⋙ derivedQuasicoherentComparison.{u} Y
```

## Tag 08D8, a lemma

[Tag 08D8](https://stacks.math.columbia.edu/tag/08D8) in the Stacks Project.

**`AlgebraicGeometry.flatPushforwardCoheratorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/FlatPushforward.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/FlatPushforward.lean#L127).

> Let `f : X ⟶ Y` be a quasi-compact, quasi-separated and flat morphism of schemes. Let `Rf_*`
> be a total right derived functor of pushforward of all modules, let `RQ_X`, `RQ_Y` be total right
> derived functors of the coherators, and let `Φ` be a total right derived functor of pushforward
> restricted to quasi-coherent modules. Then `Rf_* ⋙ RQ_Y ≅ RQ_X ⋙ Φ`.

```lean
public noncomputable def flatPushforwardCoheratorIso : Rf ⋙ RQY ≅ RQX ⋙ Φ
```

## Tag 08D9, a lemma

[Tag 08D9](https://stacks.math.columbia.edu/tag/08D9) in the Stacks Project.

**`Stacks.DerivedQCoh.coheratorSpecIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineCoherator.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineCoherator.lean#L113). The attribute's comment: “part (1): the coherator on an affine scheme”.

> **[Stacks, Tag 08D9] part (1).** On the affine scheme `X = Spec R` the coherator
> `Q_X : Mod(𝒪_X) ⥤ QCoh(𝒪_X)` sends a module `F` to the quasi-coherent module `Γ(X, F)^~` attached
> to the `R`-module of global sections of `F`.
>
> Both `Q_X` and `Γ(X, -) ⋙ ~` are right adjoint to the inclusion of the quasi-coherent modules:
> for the second, compose the sheafification–sections adjunction `~ ⊣ Γ(X, -)` with the equivalence
> `Mod(R) ≌ QCoh(𝒪_X)` of `AlgebraicGeometry.tildeEquiv`. A right adjoint is unique up to a unique
> natural isomorphism.

```lean
def coheratorSpecIso :
    coherator (Spec R) ≅ moduleSpecΓFunctor (R := R) ⋙ (tildeEquiv (R := R)).functor
```

**`Stacks.DerivedQCoh.derivedCoheratorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineCoherator.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineCoherator.lean#L186). The attribute's comment: “part (2): the derived coherator”.

> **[Stacks, Tag 08D9] part (2).** On the affine scheme `X = Spec R` the derived coherator
> `RQ_X : D(𝒪_X) ⥤ D(QCoh(𝒪_X))` sends an object `E` to the complex of quasi-coherent modules
> attached to the object `RΓ(X, E)` of `D(R)`.
>
> Both sides are right derived functors of the two isomorphic functors of
> `Stacks.DerivedQCoh.coheratorSpecIso`: the right-hand side because derived sheafification
> `D(R) ≌ D(QCoh(𝒪_X))` is an equivalence, hence a left adjoint, and postcomposing a right derived
> functor with a left adjoint again gives a right derived functor. A right derived functor is unique
> up to a unique natural isomorphism.

```lean
def derivedCoheratorIso :
    derivedCoherator R ≅
      derivedGlobalSectionsOver (𝟙 (Spec R)) ⋙ (derivedTildeEquiv R).functor
```

**`Stacks.DerivedQCoh.derivedCoheratorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineCoherator.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineCoherator.lean#L283). The attribute's comment: “part (3): quasi-inverse to the comparison functor”.

> **[Stacks, Tag 08D9] part (3).** On the affine scheme `X = Spec R` the derived coherator,
> restricted to the complexes with quasi-coherent cohomology, is a quasi-inverse to the comparison
> functor `D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of [Stacks, Tag 06VT]: the two are the two halves of an
> equivalence of categories.
>
> The comparison functor is an equivalence by
> `Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence`, and
> `Stacks.DerivedQCoh.derivedCoheratorComparisonAdjunction` exhibits the restricted derived coherator
> as its right adjoint; a right adjoint of an equivalence is its quasi-inverse.

```lean
def derivedCoheratorEquivalence :
    DerivedCategory (Scheme.QuasicoherentModules (Spec R)) ≌
      (DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
        (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).FullSubcategory
```

## Tag 09T6, a lemma

[Tag 09T6](https://stacks.math.columbia.edu/tag/09T6) in the Stacks Project.

**`Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_compatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDiagonalEquivalence.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDiagonalEquivalence.lean#L139). The attribute's comment: “equivalence clause”.

> **[Stacks, Tag 09T6], equivalence clause.** Let `X` be a quasi-compact quasi-separated scheme
> satisfying `Stacks.DerivedQCoh.AffineOpenPushforwardCompatible`: for every affine open `U ⊆ X`
> the right derived functor `Φ` of `j_* : QCoh(𝒪_U) ⥤ QCoh(𝒪_X)` fits into the commutative square
> `i_X ∘ Φ ≅ Rj_* ∘ i_U`. Then the comparison functor `i_X` of [Stacks, Tag 06VT] is an
> equivalence.
>
> The hypothesis names arbitrary models of the two derived functors; a total right derived functor
> is unique up to a unique natural isomorphism, so
> `Stacks.DerivedQCoh.derivedPushforwardIsoOfCochainUnit` and
> `Stacks.DerivedQCoh.derivedQuasicoherentPushforwardIsoOfCochainUnit` move the square to the
> chosen models, where `Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_square`
> runs the dévissage of the source on the derived coherator
> `Stacks.DerivedQCoh.coheratorDerivedAdjunction`.

```lean
theorem derivedQuasicoherentComparison_isEquivalence_of_compatible (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X]
    (h : AffineOpenPushforwardCompatible.{u, u} X) :
    (derivedQuasicoherentComparison.{u} X).IsEquivalence
```

**`Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_affineOpenCompatible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/CoheratorEquivalence.lean, line 617](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/CoheratorEquivalence.lean#L617). The attribute's comment: “equivalence”.

> **[Stacks, Tag 09T6], the equivalence.** Let `X` be a quasi-compact quasi-separated scheme
> for which the right derived functor of direct image of quasi-coherent modules from every affine
> open fits into the commutative square of
> `Stacks.DerivedQCoh.AffineOpenPushforwardCompatible`. Then the comparison functor
> `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of [Stacks, Tag 06VT] is an equivalence.
>
> The proof is the source's induction. The comparison functor is left adjoint to the derived
> coherator restricted to the complexes with quasi-coherent cohomology, and it is conservative, so
> it suffices to see that the counit of the adjunction `ι_* ⊣ RQ_X` is invertible at every complex
> with quasi-coherent cohomology. The counit is a natural transformation of exact functors of
> triangulated categories, hence invertible at the first vertex of a distinguished triangle as soon
> as it is invertible at the other two, and it is invertible at a zero object; so it suffices to
> produce, for a complex `E` with quasi-coherent cohomology supported on a closed set `S` and an
> affine open `U`, a distinguished triangle on `E` whose second vertex has invertible counit and
> whose third vertex again has quasi-coherent cohomology but is supported on `S \ U`. Finitely many
> affine opens cover `X`, so the support is exhausted. The triangle is the recollement triangle
> `E ⟶ Rj_*(E|_U) ⟶ C`: its second vertex has invertible counit by
> `Stacks.DerivedQCoh.isIso_coheratorCounit_derivedPushforward`, which is where the commutative
> square of the hypothesis and the equivalence on the affine open `U` are used, and its third
> vertex is supported on `S \ U` because `E ⟶ Rj_*(E|_U)` becomes invertible on `U`.

```lean
theorem derivedQuasicoherentComparison_isEquivalence_of_affineOpenCompatible
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (hcompat : AffineOpenPushforwardCompatible.{u + 1} X) :
    (derivedQuasicoherentComparison.{u + 1} X).IsEquivalence
```

**`Stacks.DerivedQCoh.derivedCoherator_isoInv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/CoheratorQuasiInverse.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/CoheratorQuasiInverse.lean#L361). The attribute's comment: “quasi-inverse clause, given the equivalence”.

> **[Stacks, Tag 09T6], quasi-inverse clause.** Let `X` be a scheme whose comparison functor
> `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of [Stacks, Tag 06VT] is an equivalence, and let `RQ_X` be any
> total right derived functor of the coherator `Q_X`. Then the quasi-inverse of `i_X` is `RQ_X`
> restricted to the complexes with quasi-coherent cohomology.
>
> `Stacks.DerivedQCoh.comparisonDerivedCoheratorAdjunction` exhibits that restriction as a right
> adjoint of `i_X`, the inverse of an equivalence is another, and a right adjoint is unique up to a
> unique natural isomorphism.
>
> This is the second clause of the conclusion of [Stacks, Tag 09T6], deduced from the first clause
> rather than from the tag's affine-open hypothesis
> `Stacks.DerivedQCoh.AffineOpenPushforwardCompatible`; the first clause — that the comparison
> functor is an equivalence — is the source's induction on the number of affine opens covering the
> support, and is not proved here.

```lean
def derivedCoherator_isoInv [(derivedQuasicoherentComparison.{w} X).IsEquivalence] :
    (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι ⋙ RQ ≅
      (derivedQuasicoherentComparison.{w} X).inv
```

## Tag 08DB, a proposition

[Tag 08DB](https://stacks.math.columbia.edu/tag/08DB) in the Stacks Project.

**`Stacks.AmpleNonvanishing.exists_quasicoherentComplex_iso_of_isAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/AmpleAffineDiagonal.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AmpleNonvanishing/AmpleAffineDiagonal.lean#L93). The attribute's comment: “on a scheme carrying an ample invertible module, which is the form Tag 0BQR consumes: quasi-compactness and the affine diagonal both come from ampleness”.

> **[Stacks, Tag 08DB] at the hypotheses of [Stacks, Tag 0BQR].** On a scheme carrying an ample
> invertible `𝒪_X`-module every object `K` of `D_QCoh(𝒪_X)` is isomorphic in `D(𝒪_X)` to the class
> of a cochain complex `G` of quasi-coherent `𝒪_X`-modules.
>
> This is `Stacks.AmpleNonvanishing.exists_quasicoherentComplex_iso` with its two hypotheses — `X`
> quasi-compact and `X` of affine diagonal — supplied by ampleness, which is the first line of the
> proof of [Stacks, Tag 0BQR]. No hypothesis beyond the tag's is used.

```lean
theorem exists_quasicoherentComplex_iso_of_isAmple (X : Scheme.{u}) (L : X.Modules)
    [IsInvertibleModule X L] (hL : IsAmple X L)
    (K : (DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory) :
    ∃ G : CochainComplex
        (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ℤ,
      Nonempty (K.1 ≅ DerivedCategory.Q.obj
        (((SheafOfModules.isQuasicoherent X.ringCatSheaf).ι.mapHomologicalComplex
          (ComplexShape.up ℤ)).obj G))
```

**`Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_affineDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDiagonalEquivalence.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDiagonalEquivalence.lean#L164). The attribute's comment: “equivalence”.

> **[Stacks, Tag 08DB].** Let `X` be a quasi-compact scheme with affine diagonal. Then the
> comparison functor `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of [Stacks, Tag 06VT] is an equivalence.
>
> A scheme with affine diagonal is quasi-separated, and the inclusion of one of its affine opens is
> an affine morphism, so the square of [Stacks, Tag 09T6] is the square of [Stacks, Tag 08D7]; that
> is `Stacks.DerivedQCoh.affineOpenPushforwardCompatible`, which discharges the hypothesis of
> `Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_compatible`.

```lean
theorem derivedQuasicoherentComparison_isEquivalence_of_affineDiagonal (X : Scheme.{u})
    [CompactSpace X] [IsAffineHom (pullback.diagonal (terminal.from X))] :
    (derivedQuasicoherentComparison.{u} X).IsEquivalence
```

**`Stacks.DerivedQCoh.derivedCoherator_isoInv_of_affineDiagonal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDiagonalEquivalence.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDiagonalEquivalence.lean#L181). The attribute's comment: “quasi-inverse”.

> **[Stacks, Tag 08DB], the quasi-inverse.** On a quasi-compact scheme with affine diagonal the
> quasi-inverse of the comparison functor of [Stacks, Tag 06VT] is the derived coherator `RQ_X`,
> restricted to the complexes with quasi-coherent cohomology.
>
> The comparison functor is an equivalence by
> `Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_affineDiagonal`, and
> `Stacks.DerivedQCoh.derivedCoherator_isoInv` — the quasi-inverse clause of [Stacks, Tag 09T6] —
> identifies the inverse of an equivalent comparison functor with any total right derived functor
> of the coherator, here `Stacks.DerivedQCoh.derivedCoheratorOfScheme`.

```lean
def derivedCoherator_isoInv_of_affineDiagonal (X : Scheme.{u})
    [CompactSpace X] [IsAffineHom (pullback.diagonal (terminal.from X))] :
    letI := derivedQuasicoherentComparison_isEquivalence_of_affineDiagonal X
    (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).ι ⋙ derivedCoheratorOfScheme X ≅
      (derivedQuasicoherentComparison.{u} X).inv
```

## Tag 0CRX, a lemma

[Tag 0CRX](https://stacks.math.columbia.edu/tag/0CRX) in the Stacks Project.

**`AlgebraicGeometry.isIso_derivedPushforwardComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DirectImageCoherator.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DirectImageCoherator.lean#L336). The attribute's comment: “the canonical map Φ(K) ⟶ Rf\_*(K) is an isomorphism for every K”.

> **The canonical map `Φ(K) ⟶ Rf_*(K)` is an isomorphism for every `K`.** This is the content
> of [Stacks, Tag 0CRX]. Both functors are triangulated — `Φ` and `Rf_*` because they are right
> derived functors on Grothendieck abelian categories
> (`Stacks.DerivedAcyclic.isTriangulated_of_isRightDerivedFunctor`), and the derived inclusions
> because the inclusions are exact — so the dévissage
> `Stacks.DerivedQCoh.isIso_natTrans_of_isIso_app_quasicoherentPushforward` reduces the claim to
> complexes pushed forward from an affine open, where it is
> `AlgebraicGeometry.isIso_derivedPushforwardComparison_app_quasicoherentPushforward`.

```lean
theorem isIso_derivedPushforwardComparison : IsIso (derivedPushforwardComparison f Φ ηΦ)
```

**`AlgebraicGeometry.derivedQuasicoherentComparisonSquareOfAffineDiagonal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DirectImageCoherator.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DirectImageCoherator.lean#L380). The attribute's comment: “the commuting square, for any right derived functor (Φ, ηΦ) of f\_*”.

> **The square for quasi-compact schemes with affine diagonal.** Let `f : X ⟶ Y` be a morphism
> of schemes, with `X` and `Y` quasi-compact with affine diagonal, and let `Φ`, with derivation unit
> `ηΦ`, be a total right derived functor of `f_* : QCoh(𝒪_X) ⥤ QCoh(𝒪_Y)`. Then the square
>
> ```
> D(QCoh(𝒪_X)) --i_X--> D_QCoh(𝒪_X)
>      | Φ                  | Rf_*
>      v                     v
> D(QCoh(𝒪_Y)) --i_Y--> D_QCoh(𝒪_Y)
> ```
>
> commutes, the horizontal arrows being the comparison functors of [Stacks, Tag 06VT] and the right
> edge the restriction `AlgebraicGeometry.affineDiagonalDerivedQuasicoherentPushforward` of the
> unbounded derived direct image.
>
> The isomorphism is the canonical one: after the fully faithful inclusion of `D_QCoh(𝒪_Y)` it is
> `AlgebraicGeometry.derivedPushforwardComparison`, the map `Φ(K) ⟶ Rf_*(K)` induced by
> `f_* ⟶ Rf_*`, which is invertible by `AlgebraicGeometry.isIso_derivedPushforwardComparison`.

```lean
def derivedQuasicoherentComparisonSquareOfAffineDiagonal :
    derivedQuasicoherentComparison.{u} X ⋙ affineDiagonalDerivedQuasicoherentPushforward f ≅
      Φ ⋙ derivedQuasicoherentComparison.{u} Y
```

## Tag 0CRY, a remark

[Tag 0CRY](https://stacks.math.columbia.edu/tag/0CRY) in the Stacks Project.

**`AlgebraicGeometry.exists_injective_quasicoherentSections_rightDerived_ne_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DirectImageCoheratorWarning.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/DirectImageCoheratorWarning.lean#L57). The attribute's comment: “R^1\_QCoh Γ(U, ℱ) = 0 while H^1(U, ℱ) ≠ 0, for ℱ injective in QCoh(𝒪\_\{Spec A})”.

> On an affine scheme the comparison from derived sections computed inside `QCoh(𝒪_X)` to sheaf
> cohomology is not an isomorphism. There are a ring `A`, an injective object `ℱ` of
> `QCoh(𝒪_{Spec A})` and a quasi-compact open `U ⊆ Spec A` with `R^1_{QCoh}Γ(U, ℱ) = 0` and
> `H^1(U, ℱ) ≠ 0`; in particular no morphism from the first group to the second is an isomorphism,
> so the canonical `t^1` is not one.

```lean
theorem exists_injective_quasicoherentSections_rightDerived_ne_cohomology :
    ∃ (A : CommRingCat.{u})
      (F : (SheafOfModules.isQuasicoherent (Spec A).ringCatSheaf).FullSubcategory)
      (U : (Spec A).Opens),
      Injective F ∧ IsCompact (U : Set (Spec A)) ∧
        IsZero (((quasicoherentSections (Spec A) U).rightDerived 1).obj F) ∧
        ¬ IsZero (Hgroup (Spec A).ringCatSheaf U 1
            ((SheafOfModules.isQuasicoherent (Spec A).ringCatSheaf).ι.obj F)) ∧
        ∀ t : ((quasicoherentSections (Spec A) U).rightDerived 1).obj F ⟶
            Hgroup (Spec A).ringCatSheaf U 1
              ((SheafOfModules.isQuasicoherent (Spec A).ringCatSheaf).ι.obj F),
          ¬ IsIso t
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.7, Tag 08D6](https://stacks.math.columbia.edu/tag/08D6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
