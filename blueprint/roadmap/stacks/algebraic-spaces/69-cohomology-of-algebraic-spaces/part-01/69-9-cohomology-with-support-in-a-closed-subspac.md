---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_abutsTo_sectionsWithSupportSpectralSequence, AlgebraicGeometry.Space.derivedGlobalSectionsWithSupport, AlgebraicGeometry.Space.derivedCohomologyWithSupport, AlgebraicGeometry.Space.derivedCohomologyWithSupportSingleIso, AlgebraicGeometry.Space.exists_distTriang_derivedGlobalSectionsWithSupport, AlgebraicGeometry.Space.derivedSectionsWithSupportOnClosedSubspace, AlgebraicGeometry.Space.closedGlobalSectionsWithSupport, AlgebraicGeometry.Space.closedCohomologyWithSupport
statement: formalized
proof: formalized
---

# 69.9 Cohomology with support in a closed subspace

Section 69.9 of the Stacks Project, [Tag 0A4L](https://stacks.math.columbia.edu/tag/0A4L). 5 tags here are carried by 31 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A4L, the section

[Tag 0A4L](https://stacks.math.columbia.edu/tag/0A4L) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_abutsTo_sectionsWithSupportSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportSpectralSequence.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportSpectralSequence.lean#L133). The attribute's comment: “the spectral sequence E\_2^\{p,q} = H^p(Z, 𝓗^q\_Z(F)) ⇒ H^\{p+q}\_Z(X, F)”.

> **The spectral sequence of Stacks 0A4L.**  Let `i : Z ⟶ X` be a closed immersion of
> algebraic spaces over `S` and let `F` be an abelian sheaf on `X_étale`.  There is a
> cohomological spectral sequence with second page
>
> `E_2^{p,q} ≅ H^p(Z, 𝓗^q_Z(F))`
>
> abutting to the cohomology with support `n ↦ H^n_Z(X, F)`: some finite decreasing filtration of
> each `H^n_Z(X, F)` has the terms `E_∞^{p, n-p}` as its graded pieces.
>
> Here `H^p(Z, -)` is the `p`-th right derived functor of global sections on `Z_étale`, `𝓗^q_Z` is
> `AlgebraicGeometry.Space.higherSectionsWithSupportInClosedSubspace`, the `q`-th right derived
> functor of `𝓗_Z`, and `H^n_Z(X, -)` is the `n`-th right derived functor of `Γ_Z(X, -)`, all in the
> `ℤ`-indexed convention `CategoryTheory.Functor.rightDerivedPlus`.
>
> It is the Grothendieck spectral sequence of the composite `Γ(Z, -) ∘ 𝓗_Z = Γ_Z(X, -)`
> (`AlgebraicGeometry.Space.closedGlobalSectionsWithSupportIsoComp`), whose acyclicity hypothesis
> is Stacks 0A4M: `𝓗_Z` sends injective abelian sheaves on `X_étale` to injective abelian sheaves
> on `Z_étale`, which are acyclic for `Γ(Z, -)`.

```lean
theorem exists_abutsTo_sectionsWithSupportSpectralSequence
    [HasDerivedCategory (Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory (Sheaf (SmallEtale.topology B S hS Z.1) AddCommGrpCat.{u + 1})]
    [HasDerivedCategory AddCommGrpCat.{u + 1}]
    (F : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 1} 0,
      (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
        ((Sheaf.Γ (SmallEtale.topology B S hS Z.1) AddCommGrpCat.{u + 1}).rightDerivedPlus p).obj
          ((higherSectionsWithSupportInClosedSubspace B S hS i hi q).obj F))) ∧
      SpectralSequence.AbutsTo E (fun n =>
        ((closedGlobalSectionsWithSupport B S hS i).rightDerivedPlus n).obj F)
```

**`AlgebraicGeometry.Space.derivedGlobalSectionsWithSupport`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean#L388). The attribute's comment: “the derived functor RΓ\_Z(X, -) : D(X\_étale) → D(Ab)”.

> **The derived functor `RΓ_Z(X, -) : D(X_étale) ⥤ D(Ab)`** of the sections with support in
> the closed subspace `Z` (Stacks 0A4L), on unbounded derived categories: the total right derived
> functor of the left exact functor `Γ_Z(X, -)`.

```lean
abbrev derivedGlobalSectionsWithSupport :
    smallEtaleDerivedCategory.{u + 1} B S hS X ⥤ DerivedCategory AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.derivedCohomologyWithSupport`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean#L408). The attribute's comment: “the cohomology with support H^q\_Z(X, K) of a complex K in D(X\_étale)”.

> **The cohomology with support `H^q_Z(X, K)` of a complex `K` in `D(X_étale)`**: the `q`-th
> cohomology group of `RΓ_Z(X, K)`.

```lean
abbrev derivedCohomologyWithSupport (K : smallEtaleDerivedCategory.{u + 1} B S hS X) (q : ℤ) :
    AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.derivedCohomologyWithSupportSingleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean, line 418](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean#L418). The attribute's comment: “H^q\_Z(X, F) = R^q Γ\_Z(X, F) is the cohomology of RΓ\_Z(X, F)”.

> **`H^q_Z(X, F) = R^q Γ_Z(X, F)`.** For an abelian sheaf `F` on `X_étale` placed in degree
> `0`, the `q`-th cohomology group of `RΓ_Z(X, F)` is the `q`-th classical right derived functor
> `AlgebraicGeometry.Space.closedCohomologyWithSupport` of `Γ_Z(X, -)` at `F`, naturally in `F`. So
> the cohomology with support of a complex extends the cohomology with support of a sheaf.

```lean
def derivedCohomologyWithSupportSingleIso (q : ℕ) :
    DerivedCategory.singleFunctor (abelianSheaves.{u + 1} B S hS X) 0 ⋙
        derivedGlobalSectionsWithSupport B S hS i ⋙
          DerivedCategory.homologyFunctor AddCommGrpCat.{u + 1} (q : ℤ) ≅
      closedCohomologyWithSupport B S hS i q
```

**`AlgebraicGeometry.Space.exists_distTriang_derivedGlobalSectionsWithSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CohomologyWithSupportTriangle.lean#L452). The attribute's comment: “the distinguished triangle RΓ\_Z(X, K) → RΓ(X, K) → RΓ(U, K) → RΓ\_Z(X, K)[1] and the long exact sequence of cohomology with support, for every K in D(X\_étale)”.

> **The distinguished triangle `RΓ_Z(X, K) ⟶ RΓ(X, K) ⟶ RΓ(U, K) ⟶ RΓ_Z(X, K)[1]`** of
> Stacks 0A4L, with its long exact cohomology sequence.
>
> Let `i : Z ⟶ X` be a closed immersion of algebraic spaces over `S` and let `U` be the open
> complement of `Z`.  The inclusion `Γ_Z(X, -) ⟶ Γ(X, -)` and the restriction
> `Γ(X, -) ⟶ Γ(U, (-)|_U)` descend to maps `rf : RΓ_Z(X, -) ⟶ RΓ(X, -)` and
> `rg : RΓ(X, -) ⟶ RΓ(U, -)` of derived functors on the unbounded derived category `D(X_étale)`
> (pinned down as the derived maps by their composites with the derivation units), and there is
> a connecting map `δ : RΓ(U, -) ⟶ RΓ_Z(X, -)[1]` such that for every `K` in `D(X_étale)`
>
> `RΓ_Z(X, K) ⟶ RΓ(X, K) ⟶ RΓ(U, K) ⟶ RΓ_Z(X, K)[1]`
>
> is a distinguished triangle in `D(Ab)`, and consequently the cohomology sequence
>
> `… ⟶ H^i_Z(X, K) ⟶ H^i(X, K) ⟶ H^i(U, K) ⟶ H^{i+1}_Z(X, K) ⟶ …`
>
> is exact, every six-term window of it being exact.
>
> The source's argument is the proof: for an injective abelian sheaf `I` the restriction
> `I(X) ⟶ I(U)` is surjective (Cohomology on Sites, Lemma 093X) with kernel `Γ_Z(X, I)`, so the
> three functors applied to a K-injective resolution with injective terms give a short exact
> sequence of complexes.

```lean
theorem exists_distTriang_derivedGlobalSectionsWithSupport :
    ∃ (rf : derivedGlobalSectionsWithSupport B S hS i ⟶ derivedSmallEtaleGlobalSections B S hS)
      (rg : derivedSmallEtaleGlobalSections B S hS ⟶ derivedSectionsOnComplement B S hS i hi)
      (δ : derivedSectionsOnComplement B S hS i hi ⟶
        derivedGlobalSectionsWithSupport B S hS i ⋙
          shiftFunctor (DerivedCategory AddCommGrpCat.{u + 1}) (1 : ℤ)),
      Functor.whiskerRight (NatTrans.mapHomotopyCategory
            (globalSectionsWithSupportInclusion B S hS X.1
              (Set.range (pointsMap B S hS Z.1 i.hom))) (ComplexShape.up ℤ))
          DerivedCategory.Qh ≫
          smallEtaleSectionsDerivedUnit B S hS
            (Sheaf.Γ (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}) =
        smallEtaleSectionsDerivedUnit B S hS (closedGlobalSectionsWithSupport B S hS i) ≫
          Functor.whiskerLeft DerivedCategory.Qh rf ∧
      Functor.whiskerRight (NatTrans.mapHomotopyCategory
            (restrictionToComplement B S hS i hi) (ComplexShape.up ℤ)) DerivedCategory.Qh ≫
          smallEtaleSectionsDerivedUnit B S hS (sectionsOnComplement B S hS i hi) =
        smallEtaleSectionsDerivedUnit B S hS
            (Sheaf.Γ (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}) ≫
          Functor.whiskerLeft DerivedCategory.Qh rg ∧
      ∀ K, Triangle.mk (rf.app K) (rg.app K) (δ.app K) ∈
          distTriang (DerivedCategory AddCommGrpCat.{u + 1}) ∧
        ∀ (n₀ n₁ : ℤ) (h : n₀ + 1 = n₁),
          (Functor.homologySequenceComposableArrows₅
            (DerivedCategory.homologyFunctor AddCommGrpCat.{u + 1} 0)
            (Triangle.mk (rf.app K) (rg.app K) (δ.app K)) n₀ n₁ h).Exact
```

**`AlgebraicGeometry.Space.derivedSectionsWithSupportOnClosedSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean#L131). The attribute's comment: “the derived functor R𝓗\_Z on unbounded derived categories”.

> **The derived functor `R𝓗_Z : D(X_étale) ⥤ D(Z_étale)`**, on the unbounded derived
> categories of abelian sheaves on small étale sites: the total right derived functor of the functor
> `𝓗_Z` of sections with support in the point set of a closed immersion `i : Z ⟶ X`.
>
> The bounded below version is
> `AlgebraicGeometry.Space.derivedSectionsWithSupportInClosedSubspace`.

```lean
def derivedSectionsWithSupportOnClosedSubspace :
    smallEtaleDerivedCategory.{u + 1} B S hS X ⥤ smallEtaleDerivedCategory.{u + 1} B S hS Z
```

**`AlgebraicGeometry.Space.closedGlobalSectionsWithSupport`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean#L378). The attribute's comment: “the sections with support Γ\_Z(X, F) = \{s ∈ F(X) : Supp(s) ⊆ Z}”. References: SGA 2 XIV (1.0), “more general”.

> **The sections with support `Γ_Z(X, -)` of Stacks 0A4L**, for a closed immersion
> `i : Z ⟶ X` of algebraic spaces over `S`: the global sections of an abelian sheaf on the small
> étale site of `X` whose support maps into the point set of `i`.
>
> That its value at `F` is the source's group `{s ∈ F(X) : Supp(s) ⊆ Z}` is
> `AlgebraicGeometry.Space.sectionSupportedOn_ΓRes_globalSectionsWithSupportι`,
> `AlgebraicGeometry.Space.exists_globalSectionsWithSupport` and
> `AlgebraicGeometry.Space.globalSectionsWithSupportι_mono`.

```lean
abbrev closedGlobalSectionsWithSupport (i : Z ⟶ X) :
    Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1} ⥤ AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.closedCohomologyWithSupport`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean#L391). The attribute's comment: “the cohomology with support H^q\_Z(X, F) = R^q Γ\_Z(X, F)”.

> **The cohomology with support `H^q_Z(X, -)` of Stacks 0A4L**, for a closed immersion
> `i : Z ⟶ X` of algebraic spaces over `S`: the `q`-th right derived functor of
> `AlgebraicGeometry.Space.closedGlobalSectionsWithSupport`.
>
> Its vanishing in degrees `> d` is clause (3) of Stacks 0A4R, for `X` of dimension at most `d`
> and `Z` with quasi-compact complement. That it is the cohomology in degree `q` of the derived
> functor `RΓ_Z(X, -)` on the unbounded derived category, applied to `F` placed in degree `0`, is
> `AlgebraicGeometry.Space.derivedCohomologyWithSupportSingleIso`.

```lean
abbrev closedCohomologyWithSupport (i : Z ⟶ X) (q : ℕ) :
    Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1} ⥤ AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.derivedSectionsWithSupportInClosedSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean#L410). The attribute's comment: “the derived functor R𝓗\_Z on bounded below derived categories”.

> **The derived functor `R H_Z` of Stacks 0A4L**, from the bounded below derived category of
> abelian sheaves on the small étale site of `X` to that of `Z`.
>
> The same derived functor on the unbounded derived categories is
> `AlgebraicGeometry.Space.derivedSectionsWithSupportOnClosedSubspace`.

```lean
def derivedSectionsWithSupportInClosedSubspace (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    DerivedCategory.Plus (Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}) ⥤
      DerivedCategory.Plus (Sheaf (SmallEtale.topology B S hS Z.1) AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.Space.higherSectionsWithSupportInClosedSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupport.lean#L425). The attribute's comment: “the higher sections with support 𝓗^q\_Z(F) = R^q 𝓗\_Z(F)”.

> **The higher sections with support `H^q_Z` of Stacks 0A4L**: the `q`-th right derived
> functor of `H_Z`, with values in abelian sheaves on the small étale site of `Z`.
>
> This is the functor whose vanishing on a direct image of an injective sheaf is Stacks 0A4N,
> `AlgebraicGeometry.Space.isZero_rightDerivedPlus_sectionsWithSupportInClosedSubspace`, and
> whose values are the `E_2`-terms of the spectral sequence of Stacks 0A4L,
> `AlgebraicGeometry.Space.exists_abutsTo_sectionsWithSupportSpectralSequence`. In degree `0` it is
> `H_Z` itself, by `AlgebraicGeometry.Space.higherSectionsWithSupportZeroIso`.

```lean
def higherSectionsWithSupportInClosedSubspace (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) (q : ℤ) :
    Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1} ⥤
      Sheaf (SmallEtale.topology B S hS Z.1) AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.sectionsWithSupportSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupport.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupport.lean#L284). The attribute's comment: “the subsheaf of sections with support in a closed subspace”.

> **Stacks 0A4L.** The abelian subsheaf of sections supported on a set `T` of points: over
> an étale chart it consists of the sections of `F` whose support maps into `T`.
>
> For `T` the point set of a closed immersion `i : Z ⟶ X` this is the sheaf `H_Z(F)` of the
> source, before it is viewed on the small étale site of `Z`.

```lean
def sectionsWithSupportSheaf (T : Set (points B S hS X))
    (F : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}) :
    Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}
```

**`AlgebraicGeometry.Space.sectionsWithSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupport.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupport.lean#L366). The attribute's comment: “sections with support in a closed subspace, functorially”.

> **Stacks 0A4L.** Sections with support on a fixed set of points, as an endofunctor of the
> abelian sheaves on the small étale site of `X`.

```lean
def sectionsWithSupport (T : Set (points B S hS X)) :
    Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v} ⥤
      Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}
```

**`AlgebraicGeometry.Space.sectionsWithSupportInClosedSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupport.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupport.lean#L493). The attribute's comment: “the functor H\_Z on abelian sheaves of the small étale site”.

> **Stacks 0A4L.** The functor `H_Z` of a closed immersion `i : Z ⟶ X` of algebraic spaces:
> the sections with support in `|Z|`, viewed on the small étale site of `Z` through the inverse
> image along `i`.
>
> The first factor is the subsheaf of `F` of sections whose support maps into the point set of
> `i`, which is the source's `H_Z(F)`; the second is the inverse image along `i`, which is what
> the source means by viewing that subsheaf on `Z_étale`.

```lean
def sectionsWithSupportInClosedSubspace (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom) :
    Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1} ⥤
      Sheaf (SmallEtale.topology B S hS Z.1) AddCommGrpCat.{u + 1}
```

**`AlgebraicGeometry.Space.preservesFiniteLimits_sectionsWithSupportInClosedSubspace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportLeftExact.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportLeftExact.lean#L60). The attribute's comment: “the functor 𝓗\_Z : Ab(X\_étale) → Ab(Z\_étale) is left exact”.

> **`𝓗_Z` is left exact**: it is right adjoint to the direct image along the closed immersion
> `i`, which is the adjunction `i_* ⊣ 𝓗_Z` of Stacks 0A4M.

```lean
instance preservesFiniteLimits_sectionsWithSupportInClosedSubspace :
    PreservesFiniteLimits (sectionsWithSupportInClosedSubspace B S hS i hi)
```

**`AlgebraicGeometry.Space.preservesFiniteLimits_closedGlobalSectionsWithSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportLeftExact.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportLeftExact.lean#L93). The attribute's comment: “the functor Γ\_Z(X, -) is left exact”.

> **The sections with support `Γ_Z(X, -)` are left exact** (Stacks 0A4L): the composite of the
> left exact subsheaf of sections supported on `|Z|` with global sections, a right adjoint.

```lean
theorem preservesFiniteLimits_closedGlobalSectionsWithSupport :
    PreservesFiniteLimits (closedGlobalSectionsWithSupport B S hS i)
```

**`AlgebraicGeometry.Space.higherSectionsWithSupportZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportLeftExact.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportLeftExact.lean#L116). The attribute's comment: “𝓗^0\_Z(F) = 𝓗\_Z(F)”.

> **`𝓗^0_Z = 𝓗_Z`.** The zeroth right derived functor of the left exact functor `𝓗_Z` is the
> functor itself, as the source records after defining `𝓗^q_Z = R^q 𝓗_Z`.

```lean
def higherSectionsWithSupportZeroIso :
    higherSectionsWithSupportInClosedSubspace B S hS i hi 0 ≅
      sectionsWithSupportInClosedSubspace B S hS i hi
```

## Tag 0A4M, a lemma

[Tag 0A4M](https://stacks.math.columbia.edu/tag/0A4M) in the Stacks Project.

**`AlgebraicGeometry.Space.injective_sectionsWithSupportInClosedSubspace_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InjectiveSectionsWithSupport.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InjectiveSectionsWithSupport.lean#L62).

> **Stacks 0A4M.** Let `S` be a scheme, let `i : Z ⟶ X` be a closed immersion of algebraic
> spaces over `S` and let `I` be an injective abelian sheaf on the small étale site of `X`. Then
> the sections of `I` with support in `|Z|` form an injective abelian sheaf on the small étale
> site of `Z`.

```lean
theorem injective_sectionsWithSupportInClosedSubspace_of_isClosedImmersion
    (I : Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1}) [Injective I] :
    Injective ((sectionsWithSupportInClosedSubspace B S hS i hi).obj I)
```

## Tag 0A4N, a lemma

[Tag 0A4N](https://stacks.math.columbia.edu/tag/0A4N) in the Stacks Project.

**`AlgebraicGeometry.Space.isZero_rightDerivedPlus_sectionsWithSupportInClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportVanishing.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportVanishing.lean#L115).

> **Stacks 0A4N.** Let `S` be a scheme, let `i : Z ⟶ X` be a closed immersion of algebraic
> spaces over `S` and let `G` be an injective abelian sheaf on the small étale site of `Z`. Then
> the higher sections with support in `|Z|` of the direct image `i_*G` vanish:
> `H^p_Z(i_*G) = 0` for `p > 0`.
>
> The direct image of an injective abelian sheaf is injective, and the higher right derived
> functors of an additive functor vanish on an injective object.

```lean
theorem isZero_rightDerivedPlus_sectionsWithSupportInClosedSubspace (i : Z ⟶ X)
    (hi : IsClosedImmersion B S hS i.hom)
    (G : Sheaf (SmallEtale.topology B S hS Z.1) AddCommGrpCat.{u + 1}) [Injective G]
    (p : ℤ) (hp : 0 < p) :
    IsZero (((sectionsWithSupportInClosedSubspace B S hS i hi).rightDerivedPlus p).obj
      ((smallEtaleAbelianPushforward.{u + 1} B S hS i hi.rep).obj G))
```

## Tag 0A4P, a lemma

[Tag 0A4P](https://stacks.math.columbia.edu/tag/0A4P) in the Stacks Project.

**`AlgebraicGeometry.Space.closedCohomologyWithSupportEtaleExcisionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupportEtaleExcision.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GlobalSectionsWithSupportEtaleExcision.lean#L368). The attribute's comment: “conclusion (2), every degree q: H^q\_Z(Y, F) = H^q\_\{f⁻¹Z}(X, f⁻¹F) for f étale and f⁻¹Z ≅ Z”.

> **Stacks 0A4P, conclusion (2): the global cohomology-with-support identity, in every
> degree.**  Let `f : X ⟶ Y` be an étale morphism of algebraic spaces over `S`, let `iY : Z ⟶ Y`
> be a closed subspace and let `iX : W ⟶ X` be its inverse image, presented by the cartesian
> square `hk` and carried isomorphically onto `Z` by `k`.  Then for every abelian sheaf `F` on the
> small étale site of `Y` and every degree `q`,
>
> `H^q_Z(Y, F) = H^q_{f⁻¹Z}(X, f⁻¹F)`,
>
> naturally in `F`.
>
> In degree zero this is
> `AlgebraicGeometry.Space.closedGlobalSectionsWithSupportEtaleExcisionIso`, the source's excision
> argument on the spaces-étale site.  The passage to all degrees is the source's own reasoning,
> Stacks 015Z: inverse image along an étale morphism is exact and preserves injective abelian
> sheaves, so it comes out of the right derived functor of the composite.

```lean
def closedCohomologyWithSupportEtaleExcisionIso (f : X ⟶ Y) (hf : IsEtale B S hS f.hom)
    (iY : Z ⟶ Y) (hiY : IsClosedImmersion B S hS iY.hom) (iX : W ⟶ X) (k : W ⟶ Z) [IsIso k]
    (hk : IsPullback k.hom iX.hom iY.hom f.hom) (q : ℕ) :
    closedCohomologyWithSupport B S hS iY q ≅
      etaleAbelianRestriction.{u + 1} B S hS f hf ⋙
        closedCohomologyWithSupport B S hS iX q
```

**`AlgebraicGeometry.Space.closedSectionsWithSupportEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportEtaleLocal.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportEtaleLocal.lean#L192). The attribute's comment: “degree zero, on the ambient site: f⁻¹ H\_Z(F) = H\_\{f⁻¹Z}(f⁻¹F)”.

> Let `f : X ⟶ Y` be an étale morphism of algebraic spaces over `S`, let `Z ⟶ Y` be a
> subspace and let `f⁻¹Z ⟶ X` be its inverse image, presented by the cartesian square `hk`. Then
> inverse image along `f` identifies the sections with support in `Z` of an abelian sheaf `F` on
> `Y_étale` with the sections with support in `f⁻¹Z` of `f⁻¹F`:
> `f⁻¹ ℋ_Z(F) = ℋ_{f⁻¹Z}(f⁻¹F)` as subsheaves of `f⁻¹F` on `X_étale`.

```lean
def closedSectionsWithSupportEtaleRestrictionIso {W Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) (iY : Z ⟶ Y) (iX : W ⟶ X) (k : W ⟶ Z)
    (hk : IsPullback k.hom iX.hom iY.hom f.hom) :
    closedSectionsWithSupport.{v} B S hS iY ⋙ etaleAbelianRestriction.{v} B S hS f hf ≅
      etaleAbelianRestriction.{v} B S hS f hf ⋙ closedSectionsWithSupport.{v} B S hS iX
```

**`AlgebraicGeometry.Space.closedHigherSectionsWithSupportEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportEtaleLocalHigher.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionsWithSupportEtaleLocalHigher.lean#L465). The attribute's comment: “every degree q, on the ambient site: f⁻¹ H^q\_Z(F) = H^q\_\{f⁻¹Z}(f⁻¹F)”.

> **Stacks 0A4P, the sheaf-level conclusion in every degree, for a subspace.** Let
> `f : X ⟶ Y` be an étale morphism of algebraic spaces over `S`, let `iY : Z ⟶ Y` be a subspace
> and let `iX : W ⟶ X` be its inverse image, presented by the cartesian square `hk`. Then inverse
> image along `f` identifies the higher sections with support in `Z` with the higher sections
> with support in `f⁻¹Z`, in every degree `q`:
> `f⁻¹ H^q_Z(F) = H^q_{f⁻¹Z}(f⁻¹F)` as abelian sheaves on `X_étale`.
>
> As in degree zero, the point sets match by Stacks 03H4, and the source's further hypothesis
> that `f⁻¹Z → Z` is an isomorphism — which is what lets the source read both sides as sheaves on
> `Z` itself — plays no part in the identification of the ambient sheaves proved here.

```lean
def closedHigherSectionsWithSupportEtaleRestrictionIso {W Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) (iY : Z ⟶ Y) (iX : W ⟶ X) (k : W ⟶ Z)
    (hk : IsPullback k.hom iX.hom iY.hom f.hom) (q : ℕ) :
    (closedSectionsWithSupport.{u + 1} B S hS iY).rightDerived q ⋙
        etaleAbelianRestriction.{u + 1} B S hS f hf ≅
      etaleAbelianRestriction.{u + 1} B S hS f hf ⋙
        (closedSectionsWithSupport.{u + 1} B S hS iX).rightDerived q
```

**`AlgebraicGeometry.Space.closedHigherSectionsWithSupportOnSubspaceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean, line 355](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean#L355). The attribute's comment: “every degree q, read on the subspaces: k⁻¹(H^q\_Z(F)|\_Z) = H^q\_\{f⁻¹Z}(f⁻¹F)|\_\{f⁻¹Z}”.

> **Stacks 0A4P, in every degree, read on the subspaces.**  Let `f : X ⟶ Y` be an étale
> morphism of algebraic spaces over `S`, let `iY : Z ⟶ Y` be a subspace and let `iX : W ⟶ X` be
> its inverse image, presented by the cartesian square `hk` with `k : W ⟶ Z`.  Then, in every
> degree `q` and naturally in the abelian sheaf `F` on `Y_étale`,
>
> `k⁻¹(H^q_Z(F)|_Z) = H^q_{f⁻¹Z}(f⁻¹F)|_{f⁻¹Z}`
>
> as abelian sheaves on `W = f⁻¹Z`.  This is the form of the conclusion the source states — the
> sheaf identity read on the subspace rather than on the ambient small étale site — with the
> source's hypothesis that `k` is an isomorphism *removed*: under that hypothesis `k⁻¹` is an
> equivalence and the left-hand side is the source's `H^q_Z(F)` read on `Z`.
>
> The ambient-site statement is
> `AlgebraicGeometry.Space.closedHigherSectionsWithSupportEtaleRestrictionIso`.  What is added is
> one whiskering by inverse image along `iX`, after which
> `AlgebraicGeometry.Space.smallToposMorphism_abelianInverseImageIso` — Stacks 03LQ at abelian
> coefficients — turns restriction along postcomposition with `f` into the inverse image of the
> morphism of small étale topoi, and
> `AlgebraicGeometry.Space.smallEtaleAbelianInverseImageSquareIsoOfComm` exchanges the two routes
> around the square.  Only commutativity of `hk` is used, through
> `CategoryTheory.ObjectProperty.hom_ext`.

```lean
def closedHigherSectionsWithSupportOnSubspaceIso {W Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) (iY : Z ⟶ Y) (iX : W ⟶ X) (k : W ⟶ Z)
    (hk : IsPullback k.hom iX.hom iY.hom f.hom) (q : ℕ) :
    (closedSectionsWithSupport.{u + 1} B S hS iY).rightDerived q ⋙
        (Sites.abelianInverseImage (smallToposMorphism B S hS iY) ⋙
          Sites.abelianInverseImage (smallToposMorphism B S hS k)) ≅
      etaleAbelianRestriction.{u + 1} B S hS f hf ⋙
        ((closedSectionsWithSupport.{u + 1} B S hS iX).rightDerived q ⋙
          Sites.abelianInverseImage (smallToposMorphism B S hS iX))
```

**`AlgebraicGeometry.Space.closedHigherSectionsWithSupportOnZIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleAbelianInverseImageSquare.lean#L405). The attribute's comment: “every degree q, on Z itself, with the source's hypothesis that k is an iso”.

> **Stacks 0A4P, in every degree, on `Z` itself**, with the source's hypothesis that
> `k : f⁻¹Z ⟶ Z` is an isomorphism.  Let `f : X ⟶ Y` be an étale morphism of algebraic spaces
> over `S`, let `iY : Z ⟶ Y` be a subspace and let `iX : W ⟶ X` be its inverse image, presented
> by the cartesian square `hk` with `k : W ⟶ Z` an isomorphism.  Then, in every degree `q` and
> naturally in the abelian sheaf `F` on `Y_étale`,
>
> `H^q_Z(F)|_Z = H^q_{f⁻¹Z}(f⁻¹F)|_{f⁻¹Z}`
>
> as abelian sheaves on `Z`, the right-hand side read on `Z` through `k` — that is, pulled back
> along `inv k : Z ⟶ f⁻¹Z`.  This is the reading of the conclusion that the source states.
>
> It is `AlgebraicGeometry.Space.closedHigherSectionsWithSupportOnSubspaceIso`, which states the
> same identity on `f⁻¹Z` and assumes nothing about `k`, with
> `AlgebraicGeometry.Space.smallToposMorphism_comp_abelianInverseImage` used twice to cancel
> `k⁻¹` against `(inv k)⁻¹`: once at `inv k ≫ k = 𝟙 Z`, which turns the composite into the
> inverse image along `𝟙 Z`, and once at `𝟙 Z ≫ iY = iY`, which absorbs that into the inverse
> image along `iY`.  No unit law for `AlgebraicGeometry.Space.smallToposMorphism` is needed: the
> composition isomorphism at the second of those two identities does the cancelling without the
> inverse image along `𝟙 Z` ever being identified with the identity functor.
>
> Every intermediate isomorphism is named with its type written out and every reassociation is an
> explicit `CategoryTheory.Functor.associator`, for the reason recorded in
> `StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleRestrictionInverseImage.lean`: although
> `CategoryTheory.Functor.assoc` is an equality, leaving a functor composition to definitional
> unfolding here hands the unifier the small étale inverse image to whnf and the elaboration runs
> out of heartbeats.

```lean
def closedHigherSectionsWithSupportOnZIso {W Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hf : IsEtale B S hS f.hom) (iY : Z ⟶ Y) (iX : W ⟶ X) (k : W ⟶ Z) [IsIso k]
    (hk : IsPullback k.hom iX.hom iY.hom f.hom) (q : ℕ) :
    (closedSectionsWithSupport.{u + 1} B S hS iY).rightDerived q ⋙
        Sites.abelianInverseImage (smallToposMorphism B S hS iY) ≅
      etaleAbelianRestriction.{u + 1} B S hS f hf ⋙
        ((closedSectionsWithSupport.{u + 1} B S hS iX).rightDerived q ⋙
          (Sites.abelianInverseImage (smallToposMorphism B S hS iX) ⋙
            Sites.abelianInverseImage (smallToposMorphism B S hS (inv k))))
```

## Tag 0AEI, a lemma

[Tag 0AEI](https://stacks.math.columbia.edu/tag/0AEI) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedSmallEtalePushforwardSupportedEquivalence_inverse_derivedSectionsWithSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean#L224). The attribute's comment: “the identification of the quasi-inverse with the derived sections with support R𝓗\_Z, the second description in the displayed formula”.

> **The quasi-inverse is the derived sections with support.** The quasi-inverse of the
> equivalence `D(Z_étale) ≌ D_{|Z|}(X_étale)` induced by the direct image along a closed immersion
> `i : Z ⟶ X` of algebraic spaces over `S` is the derived functor `R𝓗_Z` of sections with support
> in `|Z|`, restricted to `D_{|Z|}(X_étale)`.

```lean
def derivedSmallEtalePushforwardSupportedEquivalence_inverse_derivedSectionsWithSupport :
    (derivedSmallEtalePushforwardSupportedEquivalence B S hS i hi).inverse ≅
      (cohomologySupportedOn.{u + 1} B S hS X
          (Set.range (pointsMap B S hS Z.1 i.hom))).ι ⋙
        derivedSectionsWithSupportOnClosedSubspace B S hS i hi
```

**`AlgebraicGeometry.Space.derivedSmallEtaleInverseImage_iso_derivedSectionsWithSupport_of_supported`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean#L258). The attribute's comment: “the displayed equality i^\{-1}|\_\{D\_Z} = R𝓗\_Z|\_\{D\_\{|Z|}} of the two descriptions of the quasi-inverse”.

> **The inverse image agrees with the derived sections with support.** On the subcategory
> `D_{|Z|}(X_étale)` of complexes of abelian sheaves whose cohomology sheaves are supported on the
> point set of a closed immersion `i : Z ⟶ X`, the inverse image `i^{-1}` and the derived functor
> `R𝓗_Z` of sections with support in `|Z|` agree:
>
> `i^{-1}|_{D_Z(X_étale)} = R𝓗_Z|_{D_{|Z|}(X_étale)}`.
>
> Both are the quasi-inverse of the equivalence
> `AlgebraicGeometry.Space.derivedSmallEtalePushforwardSupportedEquivalence`.

```lean
def derivedSmallEtaleInverseImage_iso_derivedSectionsWithSupport_of_supported :
    letI := additive_smallEtaleAbelianInverseImage B S hS i hi.rep
    letI := preservesFiniteLimits_smallEtaleAbelianInverseImage B S hS i hi.rep
    letI := preservesFiniteColimits_smallEtaleAbelianInverseImage B S hS i hi.rep
    (cohomologySupportedOn.{u + 1} B S hS X
          (Set.range (pointsMap B S hS Z.1 i.hom))).ι ⋙
        (smallEtaleAbelianInverseImage B S hS i hi.rep).mapDerivedCategory ≅
      (cohomologySupportedOn.{u + 1} B S hS X
          (Set.range (pointsMap B S hS Z.1 i.hom))).ι ⋙
        derivedSectionsWithSupportOnClosedSubspace B S hS i hi
```

**`AlgebraicGeometry.Space.isRightDerivedFunctor_mapDerivedCategory_smallEtaleAbelianPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DerivedSectionsWithSupportEquivalence.lean#L279). The attribute's comment: “Ri\_* = i\_*, the pushforward along a closed immersion being its own right derived functor”.

> **`Ri_* = i_*`.** For a closed immersion `i`, the degreewise action of the direct image
> `i_*` on unbounded derived categories is the right derived functor `Ri_*`.

```lean
theorem isRightDerivedFunctor_mapDerivedCategory_smallEtaleAbelianPushforward :
    letI := preservesFiniteColimits_smallEtaleAbelianPushforward_of_isClosedImmersion B S hS i hi
    (smallEtaleAbelianPushforward.{u + 1} B S hS i hi.rep).mapDerivedCategory.IsRightDerivedFunctor
      (smallEtaleAbelianPushforward.{u + 1} B S hS i hi.rep).mapDerivedCategoryFactorsh.inv
      (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))
```

**`AlgebraicGeometry.Space.fullyFaithfulDerivedSmallEtaleAbelianPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean#L113). The attribute's comment: “full faithfulness of the pushforward”.

> **Stacks 0AEI: the pushforward is fully faithful.** For a closed immersion `i : Z ⟶ X` of
> algebraic spaces over `S` the functor `D(Z_étale) ⥤ D(X_étale)` induced by the exact direct
> image `i_*` of abelian sheaves is fully faithful.

```lean
def fullyFaithfulDerivedSmallEtaleAbelianPushforward :
    letI := additive_smallEtaleAbelianInverseImage B S hS i hi.rep
    letI := preservesFiniteColimits_smallEtaleAbelianPushforward_of_isClosedImmersion B S hS i hi
    (smallEtaleAbelianPushforward.{u + 1} B S hS i hi.rep).mapDerivedCategory.FullyFaithful
```

**`AlgebraicGeometry.Space.essImage_mapDerivedCategory_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean#L189). The attribute's comment: “essential surjectivity onto the supported subcategory”.

> **Stacks 0AEI: essential surjectivity onto the supported subcategory.** A complex of abelian
> sheaves on the small étale site of `X` all of whose cohomology sheaves are supported on the
> point set of a closed immersion `i : Z ⟶ X` is isomorphic in `D(X_étale)` to the direct image of
> a complex on `Z_étale`.

```lean
theorem essImage_mapDerivedCategory_of_cohomologySupportedOn
    (K : smallEtaleDerivedCategory.{u + 1} B S hS X)
    (hK : cohomologySupportedOn.{u + 1} B S hS X
      (Set.range (pointsMap B S hS Z.1 i.hom)) K) :
    letI := preservesFiniteColimits_smallEtaleAbelianPushforward_of_isClosedImmersion B S hS i hi
    (smallEtaleAbelianPushforward.{u + 1} B S hS i hi.rep).mapDerivedCategory.essImage K
```

**`AlgebraicGeometry.Space.derivedSmallEtalePushforwardSupportedEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean#L208). The attribute's comment: “the equivalence of D(Z\_étale) with D\_\{|Z|}(X\_étale)”.

> **Stacks 0AEI: the equivalence.** Direct image along a closed immersion `i : Z ⟶ X` of
> algebraic spaces over `S` induces an equivalence of `D(Z_étale)` with the full subcategory
> `D_{|Z|}(X_étale)` of `D(X_étale)` of complexes whose cohomology sheaves are all supported on
> the point set of `Z`.

```lean
def derivedSmallEtalePushforwardSupportedEquivalence :
    smallEtaleDerivedCategory.{u + 1} B S hS Z ≌
      smallEtaleDerivedCategoryOnClosedSubspace.{u + 1} B S hS i
```

**`AlgebraicGeometry.Space.derivedSmallEtalePushforwardSupportedEquivalence_functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean#L230). The attribute's comment: “the equivalence is induced by the pushforward”.

> **Stacks 0AEI: the equivalence is induced by the pushforward.** Composed with the inclusion
> of `D_{|Z|}(X_étale)` into `D(X_étale)`, the forward functor of the equivalence is the functor
> induced by the exact direct image `i_*`.

```lean
def derivedSmallEtalePushforwardSupportedEquivalence_functor :
    letI := preservesFiniteColimits_smallEtaleAbelianPushforward_of_isClosedImmersion B S hS i hi
    (derivedSmallEtalePushforwardSupportedEquivalence B S hS i hi).functor ⋙
        (cohomologySupportedOn.{u + 1} B S hS X (Set.range (pointsMap B S hS Z.1 i.hom))).ι ≅
      (smallEtaleAbelianPushforward.{u + 1} B S hS i hi.rep).mapDerivedCategory
```

**`AlgebraicGeometry.Space.derivedSmallEtalePushforwardSupportedEquivalence_inverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SupportedComplexesEquivalence.lean#L245). The attribute's comment: “the identification of the quasi-inverse with the inverse image”.

> **Stacks 0AEI: the quasi-inverse is the inverse image.** The quasi-inverse of the
> equivalence is the functor induced by the exact inverse image `i^{-1}`, restricted to
> `D_{|Z|}(X_étale)`.

```lean
def derivedSmallEtalePushforwardSupportedEquivalence_inverse :
    letI := additive_smallEtaleAbelianInverseImage B S hS i hi.rep
    letI := preservesFiniteLimits_smallEtaleAbelianInverseImage B S hS i hi.rep
    letI := preservesFiniteColimits_smallEtaleAbelianInverseImage B S hS i hi.rep
    (derivedSmallEtalePushforwardSupportedEquivalence B S hS i hi).inverse ≅
      (cohomologySupportedOn.{u + 1} B S hS X
          (Set.range (pointsMap B S hS Z.1 i.hom))).ι ⋙
        (smallEtaleAbelianInverseImage B S hS i hi.rep).mapDerivedCategory
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.9, Tag 0A4L](https://stacks.math.columbia.edu/tag/0A4L)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
