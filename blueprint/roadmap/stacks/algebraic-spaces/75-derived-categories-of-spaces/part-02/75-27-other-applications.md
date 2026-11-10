---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.countable_cohomology_derivedTensor_and_ext_of_qcqs_etale, AlgebraicGeometry.Space.hasCountableCohomology_derivedTensor_restrict_of_isPerfect, AlgebraicGeometry.Space.countable_ext_of_qcqs_etale, AlgebraicGeometry.Space.countable_ext_etaleRestrict_of_countable_sections_of_isPerfect, AlgebraicGeometry.Space.exists_isHomotopyColimit_isPerfect_iff_countable, AlgebraicGeometry.Space.exists_isHomotopyColimitCocone_derivedSections_tensor_of_isFlat, AlgebraicGeometry.Space.exists_isHomotopyColimitCocone_derivedHom_of_isFlat
statement: formalized
proof: formalized
---

# 75.27 Other applications

Section 75.27 of the Stacks Project, [Tag 0CRT](https://stacks.math.columbia.edu/tag/0CRT). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CRU, a lemma

[Tag 0CRU](https://stacks.math.columbia.edu/tag/0CRU) in the Stacks Project.

**`AlgebraicGeometry.Space.countable_cohomology_derivedTensor_and_ext_of_qcqs_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountableCohomologyAndExtQcqsEtale.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountableCohomologyAndExtQcqsEtale.lean#L76).

> **Stacks 0CRU.** Let `X` be a quasi-compact quasi-separated algebraic space over `S`, let `K`
> be an object of `D_QCoh(𝒪_X)` such that the cohomology sheaves `H^q(K)` have countable sets of
> sections over the affine schemes étale over `X`, and let `E` be a perfect object of `D(𝒪_X)`.
> Then for every quasi-compact quasi-separated étale `U ⟶ X` and every `i : ℤ` the sets
> `H^i(U, K ⊗^𝐋 E)` and `Ext^i(E|_U, K|_U)` are countable.
>
> Here `U` is an object of the spaces-étale site of `X`, and quasi-compactness and
> quasi-separatedness are those of `U` itself; since `X` is quasi-compact and quasi-separated these
> are equivalent to quasi-compactness and quasi-separatedness of the morphism `U ⟶ X`.
> `H^i(U, K ⊗^𝐋 E)` is the `i`-th cohomology of the derived global sections over `U` of the
> restriction of `K ⊗^𝐋 E` to `U`, and `(-)|_U` is restriction of modules along the étale
> `U ⟶ X`, read on derived categories.
>
> The cohomology clause is
> `AlgebraicGeometry.Space.hasCountableCohomology_derivedTensor_restrict_of_isPerfect` at the
> canonical derived tensor product of the small étale site, and the `Ext` clause is
> `AlgebraicGeometry.Space.countable_ext_of_qcqs_etale_of_countable_sections`.

```lean
theorem countable_cohomology_derivedTensor_and_ext_of_qcqs_etale
    (X : AlgebraicSpaces B S hS) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    letI := HasDerivedCategory.standard (Modules.{u, u} B S hS X.1 X.2)
    (∀ v : SmallEtale B S hS X.1, IsAffineChart B S hS X.1 v → ∀ q : ℤ,
      Countable (((DerivedCategory.homologyFunctor
        (Modules.{u, u} B S hS X.1 X.2) q).obj K.obj).val.obj (op v))) →
    ∀ E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2),
      RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E →
    ∀ U : SpacesEtale B S hS X, IsQuasiCompactSpace B S hS U.1.left.1 →
      IsAbsolutelyQuasiSeparated B S hS B.contains_terminal U.1.left.1 → ∀ i : ℤ,
      letI := HasDerivedCategory.standard (Modules.{u, u} B S hS U.1.left.1 U.1.left.2)
      letI := HasDerivedCategory.standard AddCommGrpCat.{u + 1}
      Countable ((DerivedCategory.homologyFunctor AddCommGrpCat.{u + 1} i).obj
          ((derivedGlobalSectionsAb B S hS U.1.left).obj
            ((etaleModulePullback.{u, u} B S hS U.1.hom U.2).mapDerivedCategory.obj
              (((smallEtaleDerivedTensor B S hS X).obj K.obj).obj E)))) ∧
        Countable (DerivedCategory.Ext
          ((etaleModulePullback.{u, u} B S hS U.1.hom U.2).mapDerivedCategory.obj E)
          ((etaleModulePullback.{u, u} B S hS U.1.hom U.2).mapDerivedCategory.obj K.obj) i)
```

**`AlgebraicGeometry.Space.hasCountableCohomology_derivedTensor_restrict_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountableSectionsDerivedTensorPerfect.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountableSectionsDerivedTensorPerfect.lean#L405). The attribute's comment: “the sets H^i(U, K ⊗^𝐋 E)”.

> Let `X` be a quasi-compact quasi-separated algebraic space over `S`, let `K` be an object of
> `D_QCoh(𝒪_X)` whose cohomology sheaves have countable sets of sections over the affine schemes
> étale over `X`, and let `E` be a perfect object of `D(𝒪_X)`.  Then `H^i(U, (K ⊗^𝐋_{𝒪_X} E)|_U)`
> is countable for every quasi-compact quasi-separated `U` étale over `X` and every `i`.

```lean
theorem hasCountableCohomology_derivedTensor_restrict_of_isPerfect
    (hZ : B.Contains (⊤_ Scheme.{u})) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (T : Stacks.SheafOfModules.DerivedTensorProduct.{u + 1, u, u, u + 1}
      (smallEtaleRingedSite B S hS X.1 X.2))
    (K : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hqcK : ∀ q : ℤ, ((DerivedCategory.homologyFunctor
      (Modules.{u, u} B S hS X.1 X.2) q).obj K).IsQuasicoherentOnSite)
    (hcountK : ∀ v : SmallEtale B S hS X.1, IsAffineChart B S hS X.1 v → ∀ q : ℤ,
      Countable (((DerivedCategory.homologyFunctor
        (Modules.{u, u} B S hS X.1 X.2) q).obj K).val.obj (op v)))
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect.{u + 1, u, u, u, u + 1} E)
    (U : SpacesEtale B S hS X) (hUqc : IsQuasiCompactSpace B S hS U.1.left.1)
    (hUqs : IsAbsolutelyQuasiSeparated B S hS hZ U.1.left.1) :
    HasCountableCohomology ((derivedGlobalSectionsAb B S hS U.1.left).obj
      ((etaleModulePullback.{u, u} B S hS U.1.hom U.2).mapDerivedCategory.obj
        ((T.tensor.obj K).obj E)))
```

**`AlgebraicGeometry.Space.countable_ext_of_qcqs_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountableSectionsEtale.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountableSectionsEtale.lean#L161). The attribute's comment: “the sets Ext^i(E|_U, K|_U)”.

> **Stacks 0CRU, the clause on `Ext^i(E|_U, K|_U)`.** Let `X` be a quasi-compact
> quasi-separated algebraic space over `S`, let `K` be an object of `D_QCoh(𝒪_X)` and let `E` be a
> perfect object of `D(𝒪_X)`. Then for every quasi-compact quasi-separated étale `U ⟶ X` the set
> `Ext^i(E|_U, K|_U)` is countable.
>
> The three hypotheses are the three inputs the source proof takes from elsewhere, and they are the
> three this library does not supply:
>
> * `hExt` identifies `Ext^i(E|_Y, K|_Y)` with the `i`-th cohomology of a derived-sections object
>   `RΓ Y`. This is the content of Stacks 08JJ that the library lacks: the carrier of 08JJ in this
>   repository, `Stacks.SheafOfModules.isIso_tensorDualToSheafHom_of_localSummand`, proves only the
>   undergived sheaf isomorphism `F ⊗ E^∨ ≅ SheafHom(E, F)`, not the derived identity
>   `K ⊗^𝐋 E^∨ ≅ RSheafHom(E, K)` that turns `Ext` into cohomology.
> * `haff` is the affine case, i.e. Stacks 0CRP transported to the spaces-étale site. The 0CRP
>   carrier in this repository is about quasi-compact opens of a *scheme* and assumes its own
>   affine case, so it does not supply this.
> * `hMV` is the Mayer–Vietoris triangle of an elementary distinguished square, i.e. Stacks 0CRS.
>   The 0CRS carrier here is conditional on part (1) of Stacks 08GW, which is itself unproved.
>
> Granted those, the devissage is `hasCountableCohomology_of_qcqs_etale`.
>
> Perfectness of `E` is part of the statement of Stacks 0CRU and is kept here, but it is not
> consumed by this proof: in the source argument perfectness is used exactly inside the affine case
> and inside the reduction of `Ext` to cohomology, and both of those are the hypotheses `haff` and
> `hExt`. The binder is therefore written `_hE`.

```lean
theorem countable_ext_of_qcqs_etale (hZ : B.Contains (⊤_ Scheme.{u}))
    (hXqc : IsQuasiCompactSpace B S hS X.obj)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.obj)
    (K : QuasicoherentDerivedCategory.{u, u} B S hS X.obj X.property)
    (E : DerivedCategory (Modules.{u, u} B S hS X.obj X.property))
    (_hE : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.obj X.property) E)
    (RΓ : (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) → (Y ⟶ X.obj) →
      DerivedCategory AddCommGrpCat.{u})
    (hExt : ∀ (Y : SpacesEtale B S hS X) (hY : IsEtale B S hS Y.obj.hom.hom) (j : ℤ),
      Nonempty (DerivedCategory.Ext
        ((etaleModulePullback.{u, u} B S hS (Y := X) ⟨Y.obj.hom.hom⟩ hY).mapDerivedCategory.obj E)
        ((etaleModulePullback.{u, u} B S hS (Y := X) ⟨Y.obj.hom.hom⟩ hY).mapDerivedCategory.obj
          K.obj) j ≃
        (DerivedCategory.homologyFunctor AddCommGrpCat.{u} j).obj
          (RΓ Y.obj.left.obj Y.obj.hom.hom)))
    (haff : ∀ V : SpacesEtale B S hS X, IsAffineSpace B S hS V.obj.left.obj →
      HasCountableCohomology (RΓ V.obj.left.obj V.obj.hom.hom))
    (hMV : ∀ (W V : SpacesEtale B S hS X) (U : Subfunctor W.obj.left.obj)
      (f : V.obj.left.obj ⟶ W.obj.left.obj), f ≫ W.obj.hom.hom = V.obj.hom.hom →
      IsElementaryDistinguishedSquare B S hS W.obj.left.property U f →
      ∃ (fU : RΓ W.obj.left.obj W.obj.hom.hom ⟶ RΓ U.toFunctor (U.ι ≫ W.obj.hom.hom))
        (fV : RΓ W.obj.left.obj W.obj.hom.hom ⟶ RΓ V.obj.left.obj V.obj.hom.hom)
        (gU : RΓ U.toFunctor (U.ι ≫ W.obj.hom.hom) ⟶
          RΓ (pullback U.ι f) (pullback.fst U.ι f ≫ U.ι ≫ W.obj.hom.hom))
        (gV : RΓ V.obj.left.obj V.obj.hom.hom ⟶
          RΓ (pullback U.ι f) (pullback.fst U.ι f ≫ U.ι ≫ W.obj.hom.hom))
        (δ : RΓ (pullback U.ι f) (pullback.fst U.ι f ≫ U.ι ≫ W.obj.hom.hom) ⟶
          (RΓ W.obj.left.obj W.obj.hom.hom)⟦(1 : ℤ)⟧),
        Triangle.mk (biprod.lift fU fV) (biprod.desc gU (-gV)) δ ∈
          distTriang (DerivedCategory AddCommGrpCat.{u}))
    (U : SpacesEtale B S hS X) (hU : IsEtale B S hS U.obj.hom.hom)
    (hUqc : IsQuasiCompactSpace B S hS U.obj.left.obj)
    (hUqs : IsAbsolutelyQuasiSeparated B S hS hZ U.obj.left.obj) (i : ℤ) :
    Countable (DerivedCategory.Ext
      ((etaleModulePullback.{u, u} B S hS (Y := X) ⟨U.obj.hom.hom⟩ hU).mapDerivedCategory.obj E)
      ((etaleModulePullback.{u, u} B S hS (Y := X) ⟨U.obj.hom.hom⟩ hU).mapDerivedCategory.obj K.obj)
      i)
```

**`AlgebraicGeometry.Space.countable_ext_etaleRestrict_of_countable_sections_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtRestrictCountableSectionsPerfect.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ExtRestrictCountableSectionsPerfect.lean#L152). The attribute's comment: “the sets Ext^i(E|_U, K|_U), at the tag's own hypotheses; the H^i(U, K ⊗^𝐋 E) clause is `AlgebraicGeometry.Space.hasCountableCohomology_derivedTensor_restrict_of_isPerfect`”.

> **The `Ext` clause of [Stacks, Tag 0CRU].**  Let `X` be a quasi-compact absolutely
> quasi-separated algebraic space over `S`, let `K` be an object of `D_QCoh(𝒪_X)` whose cohomology
> sheaves have countable sets of sections over the affine schemes étale over `X`, and let `E` be a
> perfect object of `D(𝒪_X)`.  Then `Ext^i_{𝒪_U}(E|_U, K|_U)` is countable for every quasi-compact
> absolutely quasi-separated object `U` of the spaces-étale site of `X`.
>
> Every hypothesis is the tag's own.  This is
> `countable_ext_etaleRestrict_of_countable_sections_derivedDualTensor_of_qcohDerived`, in this
> namespace, with its remaining input — countability of the sections of the cohomology sheaves of
> `E^∨ ⊗^𝐋 K` — supplied by
> `AlgebraicGeometry.Space.countable_sections_homology_derivedDualTensor_of_isPerfect`.
>
> This is one half of the tag's covering set; the other is the `H^i(U, K ⊗^𝐋 E)` clause,
> `AlgebraicGeometry.Space.hasCountableCohomology_derivedTensor_restrict_of_isPerfect`.

```lean
theorem countable_ext_etaleRestrict_of_countable_sections_of_isPerfect
    (X : AlgebraicSpaces B S hS) (hZ : B.Contains (⊤_ Scheme.{u}))
    (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    (K : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hqcK : ∀ q : ℤ, ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) q).obj
      K).IsQuasicoherentOnSite)
    (hcountK : ∀ v : SmallEtale B S hS X.1, IsAffineChart B S hS X.1 v → ∀ q : ℤ,
      Countable (((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X.1 X.2) q).obj
        K).val.obj (op v)))
    (E : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hE : RingedSite.IsPerfect (smallEtaleRingedSite B S hS X.1 X.2) E)
    (U : SpacesEtale B S hS X) (hUqc : IsQuasiCompactSpace B S hS U.1.left.1)
    (hUqs : IsAbsolutelyQuasiSeparated B S hS hZ U.1.left.1) (i : ℤ) :
    Countable (DerivedCategory.Ext
      ((etaleModulePullback.{u, u} B S hS U.1.hom U.2).mapDerivedCategory.obj E)
      ((etaleModulePullback.{u, u} B S hS U.1.hom U.2).mapDerivedCategory.obj K) i)
```

## Tag 0CRV, a lemma

[Tag 0CRV](https://stacks.math.columbia.edu/tag/0CRV) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.exists_isHomotopyColimit_isPerfect_iff_countable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountableHomotopyColimit.lean#L379), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountablePseudoCoherentDualityTags.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/CountablePseudoCoherentDualityTags.lean#L34) (StacksFrontier).

## Tag 0CRW, a lemma

[Tag 0CRW](https://stacks.math.columbia.edu/tag/0CRW) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isHomotopyColimitCocone_derivedSections_tensor_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FlatPullbackSectionsHomotopyColimit.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FlatPullbackSectionsHomotopyColimit.lean#L77). The attribute's comment: “part (2)”.

> **Stacks 0CRW (2).** Let `A` be a ring and `f : U ⟶ X` a flat morphism of algebraic spaces
> of finite presentation over `A`. There is a system `(Eₙ)` of perfect objects of `D(𝒪_X)` with
> `RΓ(U, Lf^*K) = hocolim RΓ(X, Eₙ ⊗^L K)` in `D(A)` functorially in `K ∈ D_QCoh(𝒪_X)`: natural
> maps `RΓ(X, Eₙ ⊗^L -) ⟶ RΓ(U, Lf^* -)` exhibit the homotopy colimit at every such `K`.

```lean
theorem exists_isHomotopyColimitCocone_derivedSections_tensor_of_isFlat
    {U X : AlgebraicSpaces B (Spec (.of A)) hA} (f : U ⟶ X)
    (hX : IsFinitePresentation B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X).hom)
    (hU : IsFinitePresentation B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA U).hom)
    (hf : IsFlat B (Spec (.of A)) hA f.hom) :
    ∃ E : ℕ ⥤ DerivedCategory (Modules.{u, u} B (Spec (.of A)) hA X.1 X.2),
      (∀ n, (smallEtaleRingedSite B (Spec (.of A)) hA X.1 X.2).IsPerfect (E.obj n)) ∧
      ∃ ι : ∀ n, (smallEtaleDerivedTensor B (Spec (.of A)) hA X).obj (E.obj n) ⋙
          derivedModulePushforward B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X) ⋙
            representedAffineDerivedSections B (Spec (.of A)) hA
              (baseSiteObj B (Spec (.of A)) hA) ⟶
          smallEtaleDerivedModulePullback B (Spec (.of A)) hA f ⋙
            derivedModulePushforward B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA U) ⋙
              representedAffineDerivedSections B (Spec (.of A)) hA
                (baseSiteObj B (Spec (.of A)) hA),
        ∀ K, QcohDerived B (Spec (.of A)) hA X K →
          IsHomotopyColimitCocone
            (E ⋙ (smallEtaleDerivedTensor B (Spec (.of A)) hA X).flip.obj K ⋙
              derivedModulePushforward B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X) ⋙
                representedAffineDerivedSections B (Spec (.of A)) hA
                  (baseSiteObj B (Spec (.of A)) hA))
            fun n ↦ (ι n).app K
```

**`AlgebraicGeometry.Space.exists_isHomotopyColimitCocone_derivedHom_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FlatPullbackSectionsHomotopyColimit.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/FlatPullbackSectionsHomotopyColimit.lean#L114). The attribute's comment: “part (1)”.

> **Stacks 0CRW (1).** Let `A` be a ring and `f : U ⟶ X` a flat morphism of algebraic spaces
> of finite presentation over `A`. There is an inverse system `(Lₙ)` of perfect objects of
> `D(𝒪_X)` with `RΓ(U, Lf^*K) = hocolim RHom_X(Lₙ, K)` in `D(A)` functorially in
> `K ∈ D_QCoh(𝒪_X)`, where `RHom_X(L, K) = RΓ(X, R𝓗om(L, K))`: natural maps
> `RHom_X(Lₙ, -) ⟶ RΓ(U, Lf^* -)` exhibit the homotopy colimit at every such `K`.

```lean
theorem exists_isHomotopyColimitCocone_derivedHom_of_isFlat
    {U X : AlgebraicSpaces B (Spec (.of A)) hA} (f : U ⟶ X)
    (hX : IsFinitePresentation B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X).hom)
    (hU : IsFinitePresentation B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA U).hom)
    (hf : IsFlat B (Spec (.of A)) hA f.hom) :
    ∃ L : ℕᵒᵖ ⥤ DerivedCategory (Modules.{u, u} B (Spec (.of A)) hA X.1 X.2),
      (∀ n, (smallEtaleRingedSite B (Spec (.of A)) hA X.1 X.2).IsPerfect (L.obj n)) ∧
      ∃ ι : ∀ n, (smallEtaleDerivedSheafHom B (Spec (.of A)) hA X).obj (op (L.obj (op n))) ⋙
          derivedModulePushforward B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X) ⋙
            representedAffineDerivedSections B (Spec (.of A)) hA
              (baseSiteObj B (Spec (.of A)) hA) ⟶
          smallEtaleDerivedModulePullback B (Spec (.of A)) hA f ⋙
            derivedModulePushforward B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA U) ⋙
              representedAffineDerivedSections B (Spec (.of A)) hA
                (baseSiteObj B (Spec (.of A)) hA),
        ∀ K, QcohDerived B (Spec (.of A)) hA X K →
          IsHomotopyColimitCocone
            (L.rightOp ⋙ (smallEtaleDerivedSheafHom B (Spec (.of A)) hA X).flip.obj K ⋙
              derivedModulePushforward B (Spec (.of A)) hA (toBase B (Spec (.of A)) hA X) ⋙
                representedAffineDerivedSections B (Spec (.of A)) hA
                  (baseSiteObj B (Spec (.of A)) hA))
            fun n ↦ (ι n).app K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.27, Tag 0CRT](https://stacks.math.columbia.edu/tag/0CRT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
