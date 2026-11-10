---
declaration: section
origin: cited
lean: AlgebraicGeometry.injective_supportedSections_obj, AlgebraicGeometry.isZero_rightDerivedPlus_supportedSections_pushforward, AlgebraicGeometry.mono_supportedSectionsPushforwardInclusion_app, AlgebraicGeometry.supportedSectionsShortComplex_exact, AlgebraicGeometry.cohomologyWithSupportSequences, AlgebraicGeometry.closedImmersionSupportedDerivedEquivalence, AlgebraicGeometry.smallEtalePushforward_exact_ab, AlgebraicGeometry.smallEtalePushforwardSupportedEquivalence
statement: formalized
proof: formalized
---

# 59.79 Cohomology with support in a closed subscheme

Section 59.79 of the Stacks Project, [Tag 09XP](https://stacks.math.columbia.edu/tag/09XP). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09XQ, a lemma

[Tag 09XQ](https://stacks.math.columbia.edu/tag/09XQ) in the Stacks Project.

**`AlgebraicGeometry.injective_supportedSections_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedSectionsInjective.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedSectionsInjective.lean#L313).

> **Stacks 09XQ.** The sections with support in a closed subscheme of an injective abelian
> sheaf on the small étale site of the ambient scheme form an injective abelian sheaf on the
> small étale site of that subscheme.

```lean
public theorem injective_supportedSections_obj (I : SmallEtaleAbelianSheaf B X) [Injective I] :
    Injective ((supportedSections B i).obj I)
```

## Tag 09XR, a lemma

[Tag 09XR](https://stacks.math.columbia.edu/tag/09XR) in the Stacks Project.

**`AlgebraicGeometry.isZero_rightDerivedPlus_supportedSections_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupport.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupport.lean#L230).

> **Stacks 09XR.** The cohomology sheaves with support in a closed subscheme of the direct
> image of an injective abelian sheaf on that subscheme vanish in positive degrees.

```lean
public theorem isZero_rightDerivedPlus_supportedSections_pushforward
    (G : SmallEtaleAbelianSheaf B Z) [Injective G] (p : ℤ) (hp : 0 < p) :
    IsZero (((supportedSections B i).rightDerivedPlus p).obj
      (((smallEtaleBaseChange B i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.obj X.property)
        (SmallEtale.topology B Z.obj Z.property)).obj G))
```

## Tag 0A45, a lemma

[Tag 0A45](https://stacks.math.columbia.edu/tag/0A45) in the Stacks Project.

**`AlgebraicGeometry.mono_supportedSectionsPushforwardInclusion_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportSequence.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportSequence.lean#L211). The attribute's comment: “exactness of 0 ⟶ i\_*ℋ\_Z(F) ⟶ F ⟶ j\_*(F|\_U): the first map is a monomorphism”.

> **Stacks 0A45.** The sections with support in the closed subscheme include into an abelian
> sheaf: the first map of the sequence `0 ⟶ i_*ℋ_Z(F) ⟶ F ⟶ j_*(F|_U)` is a monomorphism.

```lean
public theorem mono_supportedSectionsPushforwardInclusion_app
    (F : SmallEtaleAbelianSheaf B X) :
    Mono ((supportedSectionsPushforwardInclusion B i).app F)
```

**`AlgebraicGeometry.supportedSectionsShortComplex_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportSequence.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportSequence.lean#L223). The attribute's comment: “exactness of 0 ⟶ i\_*ℋ\_Z(F) ⟶ F ⟶ j\_*(F|\_U): exactness at F”.

> **Stacks 0A45.** The sequence `0 ⟶ i_*ℋ_Z(F) ⟶ F ⟶ j_*(F|_U)` is exact at `F`: a section
> restricting to zero on the open complement has support in the closed subscheme.  Together with
> `mono_supportedSectionsPushforwardInclusion_app` this is the exactness of that sequence.

```lean
public theorem supportedSectionsShortComplex_exact (F : SmallEtaleAbelianSheaf B X) :
    (supportedSectionsShortComplex B i F).Exact
```

**`AlgebraicGeometry.cohomologyWithSupportSequences`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportTriangle.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportTriangle.lean#L369).

> **Stacks 0A45.**  Let `i : Z ⟶ X` be a closed immersion of schemes and let `j : U ⟶ X` be
> the inclusion of the complement of `Z`.  For an abelian sheaf `F` on `X_étale` there is a
> distinguished triangle
>
> `i_*Rℋ_Z(F) ⟶ F ⟶ Rj_*(F|_U) ⟶ i_*Rℋ_Z(F)⟦1⟧`
>
> in `D(X_étale)`, hence a four-term exact sequence
>
> `0 ⟶ i_*ℋ_Z(F) ⟶ F ⟶ j_*(F|_U) ⟶ i_*ℋ¹_Z(F) ⟶ 0`
>
> and isomorphisms `R^p j_*(F|_U) ≅ i_*ℋ^{p+1}_Z(F)` for `p ≥ 1`.
>
> All three assertions are stated at once, as the three fields of
> `AlgebraicGeometry.CohomologyWithSupportSequences`.  The triangle is given for an arbitrary
> triple of right derived functors of `i_*ℋ_Z`, of the identity and of `j_*(-|_U)` on the whole
> unbounded derived category, so it applies to every model of `i_*Rℋ_Z` and `Rj_*(-|_U)` and is
> functorial in the object; the other two assertions are given at every abelian sheaf, naturally
> in it.  The open complement `U` and its inclusion `j` are constructed from `i` rather than
> assumed.
>
> `R^p` is Mathlib's `ℕ`-indexed `CategoryTheory.Functor.rightDerived`; the comparison with the
> `ℤ`-indexed `CategoryTheory.Functor.rightDerivedPlus` of
> `AlgebraicGeometry.isZero_rightDerivedPlus_supportedSections_pushforward` ([Stacks, Tag 09XR])
> is `Stacks.DerivedIndexing.rightDerivedIso`.

```lean
public def cohomologyWithSupportSequences : CohomologyWithSupportSequences B i
```

## Tag 0AEG, a lemma

[Tag 0AEG](https://stacks.math.columbia.edu/tag/0AEG) in the Stacks Project.

**`AlgebraicGeometry.closedImmersionSupportedDerivedEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionSupportedDerivedEquivalence.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionSupportedDerivedEquivalence.lean#L341).

> **Stacks 0AEG.** Let `i : Z ⟶ X` be a closed immersion of schemes.  Direct image of abelian
> sheaves along `i` is exact, so `Ri_{small,*} = i_{small,*} : D(Z_étale) ⟶ D(X_étale)`, and it
> induces an equivalence of `D(Z_étale)` with the full subcategory `D_Z(X_étale)` of `D(X_étale)`
> of complexes whose cohomology sheaves are supported on `Z`.  A quasi-inverse of that equivalence
> is given on `D_Z(X_étale)` by the exact inverse image `i_{small}^{-1}`, and also by the right
> derived functor `Rℋ_Z` of sections with support in `Z`.

```lean
public def closedImmersionSupportedDerivedEquivalence :
    ClosedImmersionSupportedDerivedEquivalence.{w₁, w₂} B i
```

**`AlgebraicGeometry.smallEtalePushforward_exact_ab`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean#L359). The attribute's comment: “Ri\_* = i\_* : direct image is exact, hence equal to its right derived functor”.

> **Stacks 0AEG.** Direct image of abelian sheaves along a closed immersion is exact, so it
> coincides with its own right derived functor: `Ri_{small,*} = i_{small,*}`.

```lean
public theorem smallEtalePushforward_exact_ab :
    exactFunctor (SmallEtaleAbelianSheaf B Z) (SmallEtaleAbelianSheaf B X)
      ((smallEtaleBaseChange B i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Z.1 Z.property))
```

**`AlgebraicGeometry.smallEtalePushforwardSupportedEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean#L464). The attribute's comment: “i\_* induces an equivalence D(Z\_étale) → D\_Z(X\_étale)”.

> **Stacks 0AEG.** Direct image along a closed immersion induces an equivalence of
> `D(Z_étale)` with the full subcategory `D_Z(X_étale)` of `D(X_étale)` of complexes whose
> cohomology sheaves are supported on `Z`.

```lean
public def smallEtalePushforwardSupportedEquivalence :
    DerivedCategory (SmallEtaleAbelianSheaf B Z) ≌ SupportedDerivedCategory.{w₂} B i
```

**`AlgebraicGeometry.smallEtalePushforwardSupportedEquivalence_functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean#L473). The attribute's comment: “the equivalence is induced by i\_*”.

> **Stacks 0AEG.** The equivalence is given by direct image: composed with the inclusion of
> `D_Z(X_étale)` into `D(X_étale)` it is the functor induced by `i_*`.

```lean
public def smallEtalePushforwardSupportedEquivalence_functor :
    (smallEtalePushforwardSupportedEquivalence.{w₁, w₂} B i).functor ⋙
        (supportedDerivedProperty.{w₂} B i).ι ≅
      ((smallEtaleBaseChange B i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.obj X.property)
        (SmallEtale.topology B Z.obj Z.property)).mapDerivedCategory
```

**`AlgebraicGeometry.smallEtalePushforwardSupportedEquivalence_inverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean#L484). The attribute's comment: “the quasi-inverse is i^\{-1} restricted to D\_Z(X\_étale)”.

> **Stacks 0AEG.** The quasi-inverse of the equivalence is inverse image restricted to
> `D_Z(X_étale)`: `i^{-1}|_{D_Z(X_étale)}`.

```lean
public def smallEtalePushforwardSupportedEquivalence_inverse :
    (smallEtalePushforwardSupportedEquivalence.{w₁, w₂} B i).inverse ≅
      (supportedDerivedProperty.{w₂} B i).ι ⋙
        ((smallEtaleBaseChange B i).sheafPullback AddCommGrpCat.{u + 1}
          (SmallEtale.topology B X.obj X.property)
          (SmallEtale.topology B Z.obj Z.property)).mapDerivedCategory
```

## Tag 0A46, a lemma

[Tag 0A46](https://stacks.math.columbia.edu/tag/0A46) in the Stacks Project.

**`AlgebraicGeometry.supportedCohomologyEtaleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportEtaleZariski.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportEtaleZariski.lean#L226). The attribute's comment: “clause (1): cohomology with support in a closed subset agrees between the small etale site and the Zariski site, for a quasi-coherent module, in every degree, with no hypothesis beyond the source's. Clause (2) is supportedCohomology\_isQuasicoherent\_and\_associatedSheaf, on the size-bounded small etale site”.

> **Stacks 0A46, clause (1).**  For a quasi-coherent `𝒪_X`-module `F` and a closed subset `Z`
> of a scheme `X`, cohomology with support in `Z` of the associated sheaf `Fᵃ` on the small étale
> site of `X` agrees, in every degree, with cohomology with support in `Z` of `F` on the small
> Zariski site.
>
> Both sides are right derived functors of the functor of global sections vanishing on the open
> complement of `Z`, taken on the respective site.  There is no hypothesis beyond those of the
> source: the vanishing of the higher direct images `R^nε_*(Fᵃ)` for `n > 0` is
> `AlgebraicGeometry.isZero_rightDerived_pushforward_opensToEtale` and the identification of
> `ε_*(Fᵃ)` with `F` is `AlgebraicGeometry.smallEtaleSectionsUnitIso`, those two being the two
> halves of Stacks 03P2 for `𝒞 = X_étale`.

```lean
public def supportedCohomologyEtaleIso (F : X.Modules) [F.IsQuasicoherent] (q : ℕ) :
    ((smallEtaleSectionsWithSupport X Z hZ).rightDerived q).obj
        (smallEtaleAssociatedSheaf X F) ≅
      ((SmallEtale.zariskiSectionsWithSupport X Z hZ).rightDerived q).obj
        ((SheafOfModules.toSheaf X.ringCatSheaf).obj F)
```

**`AlgebraicGeometry.supportedCohomology_isQuasicoherent_and_associatedSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportQuasicoherent.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/CohomologyWithSupportQuasicoherent.lean#L181). The attribute's comment: “clause (2): for a closed immersion with retrocompact open complement and a quasi-coherent module F, i\_*H^q\_Z(F) is quasi-coherent and i\_*H^q\_Z(F^a) = (i\_*H^q\_Z(F))^a on the small etale site, for every q”.

> Let `i : Z ⟶ X` be a closed immersion whose open complement is retrocompact in `X`, and let
> `𝓕` be a quasi-coherent `𝒪_X`-module.  Then for every `q` the Zariski sheaf `i_*ℋ^q_Z(𝓕)` is a
> quasi-coherent `𝒪_X`-module, and the étale sheaf `i_*ℋ^q_Z(𝓕ᵃ)` is its associated sheaf
> `(i_*ℋ^q_Z(𝓕))ᵃ`.
>
> The étale `i_*ℋ^q_Z` is the library's, on abelian sheaves of the small étale site with
> coefficients in the universe after that of the schemes, and `𝓕ᵃ` is
> `AlgebraicGeometry.SmallEtale.associatedModuleOfSheaf`, read as an abelian sheaf and then by the
> universe lift, which is fully faithful and exact; see the implementation notes.  The first half
> is [Stacks, Tag 0G7G] (1) in one degree, the second
> `AlgebraicGeometry.supportedCohomologyAssociatedSheafIso`.

```lean
public theorem supportedCohomology_isQuasicoherent_and_associatedSheaf
    (hU : IsRetrocompact (Set.range (B.inclusion.map i).base)ᶜ) (𝓕 : X.obj.Modules)
    [𝓕.IsQuasicoherent] (q : ℕ) :
    (((supportedSectionsFunctor X.obj.toRingedSpace
        (Set.range (B.inclusion.map i).base)).rightDerived q).obj 𝓕).IsQuasicoherent ∧
      Nonempty (((supportedSectionsPushforward B i).rightDerived q).obj
          ((Stacks.Sheaves.UniverseLift.uliftSheafFunctor.{u + 1, u}
            (SmallEtale.topology B X.obj X.property)).obj
            ((SheafOfModules.toSheaf.{u} (SmallEtale.structureSheaf B X.obj X.property)).obj
              ((SmallEtale.associatedModuleOfSheaf B X.obj X.property).obj 𝓕))) ≅
        (Stacks.Sheaves.UniverseLift.uliftSheafFunctor.{u + 1, u}
          (SmallEtale.topology B X.obj X.property)).obj
          ((SheafOfModules.toSheaf.{u} (SmallEtale.structureSheaf B X.obj X.property)).obj
            ((SmallEtale.associatedModuleOfSheaf B X.obj X.property).obj
              (((supportedSectionsFunctor X.obj.toRingedSpace
                (Set.range (B.inclusion.map i).base)).rightDerived q).obj 𝓕))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.79, Tag 09XP](https://stacks.math.columbia.edu/tag/09XP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
