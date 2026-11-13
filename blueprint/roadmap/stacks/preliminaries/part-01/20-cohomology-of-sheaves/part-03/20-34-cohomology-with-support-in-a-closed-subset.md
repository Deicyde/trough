---
declaration: section
origin: cited
lean: Stacks.Cohomology.SupportedComplexes.derivedPushforwardAdjunction, Stacks.Cohomology.SupportedComplexes.derivedPushforwardCompDerivedSupportedSectionsIsoId, Stacks.Cohomology.SupportedComplexes.derivedPushforward_adj_derivedSupportedSectionsOnClosed, Stacks.Cohomology.SupportedComplexes.exists_isIso_unit_derivedPushforward_adj_derivedSupportedSectionsOnClosed, Stacks.Cohomology.SupportedComplexes.isZero_rightDerivedPlus_supportedSectionsOnClosed_modulePushforward, Stacks.Cohomology.SupportedComplexes.isIso_derivedPushforwardAdjunction_counit_app_of_supported, Stacks.Cohomology.SupportedComplexes.derivedPushforwardSupportedSectionsIso, Stacks.Cohomology.SupportedComplexes.closedSubsetDerivedPushforwardEquivalence
statement: formalized
proof: formalized
---

# 20.34 Cohomology with support in a closed subset, II

Section 20.34 of the Stacks Project, [Tag 0G6Y](https://stacks.math.columbia.edu/tag/0G6Y). 13 tags here are carried by 46 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A3B, a lemma

[Tag 0A3B](https://stacks.math.columbia.edu/tag/0A3B) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.derivedPushforwardAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean#L277). The attribute's comment: “the adjunction i\_*^D ⊣ RℋZ as a term, not an existence statement”.

> **Stacks 0A3B (1), as a term.** Let `Z` be a closed subset of a ringed space `X` and let
> `i : (Z, 𝒪_X|_Z) ⟶ (X, 𝒪_X)` be the inclusion. The functor `D(𝒪_X|_Z) ⥤ D(𝒪_X)` induced by
> `i_*` is left adjoint to the right derived functor `RH_Z : D(𝒪_X) ⥤ D(𝒪_X|_Z)` of sections
> supported on `Z`.
>
> This is the adjunction whose mere existence is
> `derivedPushforward_adj_derivedSupportedSectionsOnClosed`, and its unit is the canonical
> comparison by `derivedPushforwardAdjunction_unit_app`.

```lean
noncomputable def derivedPushforwardAdjunction (X : RingedSpace.{u, u}) (Z : Set X.carrier)
    (hZ : IsClosed Z) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory ⊣
      derivedSupportedSectionsOnClosed X Z hZ
```

**`Stacks.Cohomology.SupportedComplexes.derivedPushforwardCompDerivedSupportedSectionsIsoId`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean#L378). The attribute's comment: “RℋZ ∘ i\_*^D ≅ 𝟭, as a chosen natural isomorphism”.

> **Stacks 0A3B (2) as a natural isomorphism.** Composing `RH_Z` with the derived pushforward
> from the closed subset is the identity on `D(𝒪_X|_Z)`, the isomorphism being the inverse of the
> unit of `derivedPushforwardAdjunction`.

```lean
noncomputable def derivedPushforwardCompDerivedSupportedSectionsIsoId (X : RingedSpace.{u, u})
    (Z : Set X.carrier) (hZ : IsClosed Z) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory ⋙
        derivedSupportedSectionsOnClosed X Z hZ ≅
      𝟭 (DerivedCategory (_root_.SheafOfModules.{u}
        (structureSheafRing (closedSubsetRingedSpace X Z))))
```

**`Stacks.Cohomology.SupportedComplexes.derivedPushforward_adj_derivedSupportedSectionsOnClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedAdjunction.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedAdjunction.lean#L511). The attribute's comment: “adjunction”.

> **Stacks 0A3B (1).** Let `Z` be a closed subset of a ringed space `X` and let
> `i : (Z, 𝒪_X|_Z) ⟶ (X, 𝒪_X)` be the inclusion. The right derived functor
> `RH_Z : D(𝒪_X) ⥤ D(𝒪_X|_Z)` of sections supported on `Z` is right adjoint to the functor
> `D(𝒪_X|_Z) ⥤ D(𝒪_X)` induced by `i_*`.

```lean
theorem derivedPushforward_adj_derivedSupportedSectionsOnClosed (X : RingedSpace.{u, u})
    (Z : Set X.carrier) (hZ : IsClosed Z) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    Nonempty
      ((modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory ⊣
        derivedSupportedSectionsOnClosed X Z hZ)
```

**`Stacks.Cohomology.SupportedComplexes.exists_isIso_unit_derivedPushforward_adj_derivedSupportedSectionsOnClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedAdjunction.lean, line 526](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedAdjunction.lean#L526). The attribute's comment: “pushforward identity”.

> **Stacks 0A3B (2).** Let `Z` be a closed subset of a ringed space `X` and let
> `i : (Z, 𝒪_X|_Z) ⟶ (X, 𝒪_X)` be the inclusion. For `K` in `D(𝒪_X|_Z)` one has
> `RH_Z(i_* K) = K`: the unit of the derived adjunction of Stacks 0A3B (1) is an isomorphism. The
> adjunction is pinned down by the compatibility of its unit with the unit `M ⟶ H_Z(i_* M)` of the
> underived adjunction, which identifies the invertible map as the canonical comparison.

```lean
theorem exists_isIso_unit_derivedPushforward_adj_derivedSupportedSectionsOnClosed
    (X : RingedSpace.{u, u}) (Z : Set X.carrier) (hZ : IsClosed Z) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    ∃ Ad : (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory ⊣
        derivedSupportedSectionsOnClosed X Z hZ,
      (∀ M : HomotopyCategory (_root_.SheafOfModules.{u}
          (structureSheafRing (closedSubsetRingedSpace X Z))) (ComplexShape.up ℤ),
        Ad.unit.app (DerivedCategory.Qh.obj M) ≫
            (derivedSupportedSectionsOnClosed X Z hZ).map
              ((modulePushforward
                (closedSubsetInclusion X Z)).mapDerivedCategoryFactorsh.hom.app M) =
          DerivedCategory.Qh.map
              ((Adjunction.mapHomotopyCategoryAdjunction
                (modulePushforward_supportedSectionsOnClosed_adjunction X Z hZ)
                (ComplexShape.up ℤ)).unit.app M) ≫
            (derivedSupportedSectionsOnClosedUnit X Z hZ).app
              (((modulePushforward (closedSubsetInclusion X Z)).mapHomotopyCategory
                (ComplexShape.up ℤ)).obj M)) ∧ IsIso Ad.unit
```

**`Stacks.Cohomology.SupportedComplexes.isZero_rightDerivedPlus_supportedSectionsOnClosed_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedAdjunction.lean, line 576](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedAdjunction.lean#L576). The attribute's comment: “higher vanishing”.

> **Stacks 0A3B (3).** Let `Z` be a closed subset of a ringed space `X`, let
> `i : (Z, 𝒪_X|_Z) ⟶ (X, 𝒪_X)` be the inclusion and let `𝒢` be a sheaf of `𝒪_X|_Z`-modules on
> `Z`. Then the higher derived sheaves of sections supported on `Z` of the pushforward of `𝒢`
> vanish: `H^p_Z(i_* 𝒢) = 0` for `p > 0`.

```lean
theorem isZero_rightDerivedPlus_supportedSectionsOnClosed_modulePushforward
    (X : RingedSpace.{u, u}) (Z : Set X.carrier) (hZ : IsClosed Z)
    (G : _root_.SheafOfModules.{u} (structureSheafRing (closedSubsetRingedSpace X Z)))
    (p : ℤ) (hp : 0 < p) :
    letI : EnoughInjectives (_root_.SheafOfModules.{u} (structureSheafRing X)) :=
      IsGrothendieckAbelian.enoughInjectives
    IsZero (((supportedSectionsOnClosedFunctor X Z hZ).rightDerivedPlus p).obj
      ((modulePushforward (closedSubsetInclusion X Z)).obj G))
```

## Tag 0AEF, a lemma

[Tag 0AEF](https://stacks.math.columbia.edu/tag/0AEF) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.isIso_derivedPushforwardAdjunction_counit_app_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean#L228). The attribute's comment: “part (2): the counit i\_*RℋZ(K) ⟶ K is invertible at every K supported on Z, which is the essential-image content of the equivalence”.

> **Stacks 0AEF, part (2).** For `K` in `D(𝒪_X)` whose cohomology sheaves are supported on
> the closed subset `Z`, the canonical map `i_* RH_Z(K) ⟶ K` — the counit of the adjunction
> `i_*^D ⊣ RH_Z` of Stacks 0A3B (1) — is an isomorphism.

```lean
theorem isIso_derivedPushforwardAdjunction_counit_app_of_supported (X : RingedSpace.{u, u})
    (Z : Set X.carrier) (hZ : IsClosed Z)
    (K : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)))
    (hK : AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X) Z K) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    IsIso ((derivedPushforwardAdjunction X Z hZ).counit.app K)
```

**`Stacks.Cohomology.SupportedComplexes.derivedPushforwardSupportedSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean#L246). The attribute's comment: “part (2): the same invertible counit, as the isomorphism i\_*RℋZ(K) ≅ K”.

> **Stacks 0AEF, part (2), as an isomorphism.** For `K` in `D(𝒪_X)` with cohomology sheaves
> supported on `Z`, the canonical map `i_* RH_Z(K) ⟶ K` is an isomorphism `i_* RH_Z(K) ≅ K`.

```lean
def derivedPushforwardSupportedSectionsIso (X : RingedSpace.{u, u}) (Z : Set X.carrier)
    (hZ : IsClosed Z) (K : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)))
    (hK : AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X) Z K) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.obj
        ((derivedSupportedSectionsOnClosed X Z hZ).obj K) ≅ K
```

**`Stacks.Cohomology.SupportedComplexes.closedSubsetDerivedPushforwardEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean#L262). The attribute's comment: “part (2): i\_* : D(𝒪\_X|\_Z) ⥤ D\_Z(𝒪\_X) is an equivalence”.

> **Stacks 0AEF, part (2).** Derived pushforward along the inclusion of a closed subset `Z`
> is an equivalence of `D(𝒪_X|_Z)` with the full subcategory `D_Z(𝒪_X)` of `D(𝒪_X)` of complexes
> whose cohomology sheaves are supported on `Z`.

```lean
def closedSubsetDerivedPushforwardEquivalence (X : RingedSpace.{u, u}) (Z : Set X.carrier)
    (hZ : IsClosed Z) :
    DerivedCategory (_root_.SheafOfModules.{u}
        (structureSheafRing (closedSubsetRingedSpace X Z))) ≌
      SupportedDerivedCategory X Z
```

**`Stacks.Cohomology.SupportedComplexes.closedSubsetDerivedPushforwardEquivalence_functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean#L277). The attribute's comment: “part (2): the functor of the equivalence is i\_*”.

> **Stacks 0AEF, part (2).** The equivalence onto the supported complexes is induced by
> `i_*`: composed with the inclusion of `D_Z(𝒪_X)` into `D(𝒪_X)` it is `i_*^D`.

```lean
def closedSubsetDerivedPushforwardEquivalence_functor (X : RingedSpace.{u, u})
    (Z : Set X.carrier) (hZ : IsClosed Z) :
    (letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    (closedSubsetDerivedPushforwardEquivalence X Z hZ).functor ⋙
        (supportedDerivedProperty X Z).ι ≅
      (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory)
```

**`Stacks.Cohomology.SupportedComplexes.closedSubsetDerivedPushforwardEquivalence_inverse`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean#L295). The attribute's comment: “part (2): the quasi-inverse is RℋZ restricted to D\_Z”.

> **Stacks 0AEF, part (2).** The quasi-inverse of the equivalence is the derived functor
> `RH_Z` of sections supported on `Z`, restricted to `D_Z(𝒪_X)`.
>
> This is the `RH_Z` half of the source's `i^{-1}|_{D_Z(𝒪_X)} = RH_Z|_{D_Z(𝒪_X)}`; the `i^{-1}`
> half is `closedSubsetDerivedPushforwardEquivalence_inverse_iso_derivedModulePullback` in
> `ClosedSubsetDerivedPullback.lean`.

```lean
def closedSubsetDerivedPushforwardEquivalence_inverse (X : RingedSpace.{u, u})
    (Z : Set X.carrier) (hZ : IsClosed Z) :
    (closedSubsetDerivedPushforwardEquivalence X Z hZ).inverse ≅
      (supportedDerivedProperty X Z).ι ⋙ derivedSupportedSectionsOnClosed X Z hZ
```

**`Stacks.Cohomology.SupportedComplexes.derivedPushforwardSupportedSections_isRightAdjoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedEquivalence.lean#L312). The attribute's comment: “part (3)”.

> **Stacks 0AEF, part (3).** The functor `D(𝒪_X) ⥤ D_Z(𝒪_X)` given by `K ↦ i_* RH_Z(K)` —
> `RH_Z` followed by derived pushforward, which lands in `D_Z(𝒪_X)` by part (1) — is right adjoint
> to the inclusion `D_Z(𝒪_X) ⥤ D(𝒪_X)`.
>
> This is the formal consequence of part (2) and Stacks 0A3B (1) that [Stacks, Tag 0AEF] says it
> is: by part (2) the inclusion is the quasi-inverse of `i_*^D : D(𝒪_X|_Z) ≌ D_Z(𝒪_X)` followed by
> `i_*^D`, so composing that equivalence with the adjunction `i_*^D ⊣ RH_Z` of Stacks 0A3B (1)
> exhibits the inclusion as a left adjoint; see `iotaAdjunctionOfCounitIso`.

```lean
def derivedPushforwardSupportedSections_isRightAdjoint (X : RingedSpace.{u, u})
    (Z : Set X.carrier) (hZ : IsClosed Z) :
    (supportedDerivedProperty X Z).ι ⊣
      derivedSupportedSectionsOnClosed X Z hZ ⋙ derivedPushforwardToSupported X Z hZ
```

**`Stacks.Cohomology.SupportedComplexes.derivedSupportedSectionsIsoDerivedModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedPullback.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedPullback.lean#L128). The attribute's comment: “part (2): on D\_Z the quasi-inverse RℋZ agrees with i⁻¹”.

> On the full subcategory `D_Z(𝒪_X)` of complexes with cohomology sheaves supported on the closed
> subset `Z`, the right derived functor `RH_Z` of sections supported on `Z` agrees with inverse image
> `i^{-1}` along the inclusion.

```lean
def derivedSupportedSectionsIsoDerivedModulePullback (X : RingedSpace.{u, u})
    (Z : Set X.carrier) (hZ : IsClosed Z) :
    (letI := preservesFiniteLimits_modulePullback_closedSubsetInclusion X Z
    letI := preservesFiniteColimits_modulePullback (closedSubsetInclusion X Z)
    (supportedDerivedProperty X Z).ι ⋙ derivedSupportedSectionsOnClosed X Z hZ ≅
      (supportedDerivedProperty X Z).ι ⋙
        (modulePullback (closedSubsetInclusion X Z)).mapDerivedCategory)
```

**`Stacks.Cohomology.SupportedComplexes.closedSubsetDerivedPushforwardEquivalence_inverse_iso_derivedModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedPullback.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetDerivedPullback.lean#L152). The attribute's comment: “part (2): the quasi-inverse is i⁻¹ restricted to D\_Z”.

> The quasi-inverse of the equivalence `i_*^D : D(𝒪_X|_Z) ≌ D_Z(𝒪_X)` is inverse image `i^{-1}`
> restricted to `D_Z(𝒪_X)`.

```lean
def closedSubsetDerivedPushforwardEquivalence_inverse_iso_derivedModulePullback
    (X : RingedSpace.{u, u}) (Z : Set X.carrier) (hZ : IsClosed Z) :
    (letI := preservesFiniteLimits_modulePullback_closedSubsetInclusion X Z
    letI := preservesFiniteColimits_modulePullback (closedSubsetInclusion X Z)
    (closedSubsetDerivedPushforwardEquivalence X Z hZ).inverse ≅
      (supportedDerivedProperty X Z).ι ⋙
        (modulePullback (closedSubsetInclusion X Z)).mapDerivedCategory)
```

**`Stacks.Cohomology.SupportedComplexes.pushforward_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetPushforward.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ClosedSubsetPushforward.lean#L116). The attribute's comment: “part (1)”.

> **Stacks 0AEF, part (1).** For `K` in the derived category of `𝒪_X|_Z`-modules, the
> cohomology sheaves of `i_* K` are supported on `Z`.

```lean
theorem pushforward_supported (X : RingedSpace.{u, u}) (Z : Set X.carrier) (hZ : IsClosed Z)
    (K : DerivedCategory (Stacks.Cohomology.DerivedPushforwardComposition.ModuleSheaves
      (closedSubsetRingedSpace X Z))) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X) Z
      ((modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.obj K)
```

## Tag 0G6Z, a lemma

[Tag 0G6Z](https://stacks.math.columbia.edu/tag/0G6Z) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.isKInjective_supportedSectionsOnClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsKInjective.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsKInjective.lean#L62).

> **Stacks 0G6Z.** Let `Z` be a closed subset of a ringed space `X` and let
> `i : (Z, 𝒪_X|_Z) ⟶ (X, 𝒪_X)` be the inclusion. If `I` is a K-injective complex of
> `𝒪_X`-modules, then the complex `H_Z(I)` of sections supported on `Z` is a K-injective complex
> of `𝒪_X|_Z`-modules.

```lean
theorem isKInjective_supportedSectionsOnClosed (X : RingedSpace.{u, u}) (Z : Set X.carrier)
    (hZ : IsClosed Z) (I : CochainComplex (_root_.SheafOfModules.{u} (structureSheafRing X)) ℤ)
    [I.IsKInjective] :
    CochainComplex.IsKInjective
      (((Stacks.SheafOfModules.SupportedSections.supportedSectionsOnClosedFunctor
        X Z hZ).mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

## Tag 0G70, a lemma

[Tag 0G70](https://stacks.math.columbia.edu/tag/0G70) in the Stacks Project.

**`Stacks.Cohomology.LocalToGlobalSupport.derivedSectionsWithSupportIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/LocalToGlobalSectionsWithSupport.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/LocalToGlobalSectionsWithSupport.lean#L396).

> **Stacks 0G70.** Let `Z` be a closed subset of a ringed space `X` and let
> `i : (Z, 𝒪_X|_Z) ⟶ (X, 𝒪_X)` be the inclusion.  Then `RΓ(Z, -) ∘ RH_Z = RΓ_Z(X, -)` as functors
> `D(𝒪_X) ⥤ D(𝒪_X(X))`: for every right derived functor `RΓ(Z, -)` of global sections on `Z` and
> every right derived functor `RΓ_Z(X, -)` of global sections supported on `Z`, there is a
> canonical natural isomorphism from the composite of `RH_Z` with `RΓ(Z, -)` to `RΓ_Z(X, -)`.  It
> is canonical by uniqueness of right derived functors: it is the unique transformation compatible
> with the comparisons to the underived functors, by
> `derivedSectionsWithSupportIso_hom_fac` together with
> `derivedSectionsWithSupportIso_hom_unique`.

```lean
def derivedSectionsWithSupportIso
    [RΓZ'.IsRightDerivedFunctor αΓ
      (HomotopyCategory.quasiIso (ClosedModuleSheaves X Z) (ComplexShape.up ℤ))]
    [RΓZ.IsRightDerivedFunctor αZ
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))] :
    derivedSupportedSectionsOnClosed X Z hZ ⋙ RΓZ' ≅ RΓZ
```

**`Stacks.Cohomology.LocalToGlobalSupport.derivedSectionsWithSupportIso_hom_fac`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/LocalToGlobalSectionsWithSupport.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/LocalToGlobalSectionsWithSupport.lean#L410). The attribute's comment: “the comparison is the canonical one”.

> **Stacks 0G70, the normalization that makes the isomorphism the canonical one.** The
> isomorphism of Stacks 0G70 carries the comparison `localToGlobalUnit` of `RΓ(Z, -) ∘ RH_Z` to
> the comparison `αZ` of `RΓ_Z(X, -)`.

```lean
theorem derivedSectionsWithSupportIso_hom_fac
    [RΓZ'.IsRightDerivedFunctor αΓ
      (HomotopyCategory.quasiIso (ClosedModuleSheaves X Z) (ComplexShape.up ℤ))]
    [RΓZ.IsRightDerivedFunctor αZ
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))] :
    localToGlobalUnit X Z hZ RΓZ' αΓ ≫ Functor.whiskerLeft DerivedCategory.Qh
        (derivedSectionsWithSupportIso X Z hZ RΓZ' αΓ RΓZ αZ).hom =
      αZ
```

## Tag 0G71, a lemma

[Tag 0G71](https://stacks.math.columbia.edu/tag/0G71) in the Stacks Project.

**`Stacks.Cohomology.SectionsWithSupport.canonicalDerivedGlobalSections_isRightDerivedFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean#L124). The attribute's comment: “RΓ(X, -) on the unbounded derived category D(O\_X) exists: the middle term of the triangle is a genuine right derived functor of global sections”.

> `RΓ(X, -)`, with its unit, is a right derived functor of global sections along the
> quasi-isomorphisms of the unbounded homotopy category.

```lean
public instance canonicalDerivedGlobalSections_isRightDerivedFunctor :
    (canonicalDerivedGlobalSections X).IsRightDerivedFunctor
      (canonicalDerivedGlobalSectionsUnit X)
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
```

**`Stacks.Cohomology.SectionsWithSupport.canonicalDerivedSectionsWithSupport_isRightDerivedFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean#L159). The attribute's comment: “RΓ\_Z(X, -) on the unbounded derived category D(O\_X) exists: the first term of the triangle is a genuine right derived functor of sections with support in Z”.

> `RΓ_Z(X, -)`, with its unit, is a right derived functor of sections with support along
> the quasi-isomorphisms of the unbounded homotopy category.

```lean
public instance canonicalDerivedSectionsWithSupport_isRightDerivedFunctor :
    (canonicalDerivedSectionsWithSupport X Z hZ).IsRightDerivedFunctor
      (canonicalDerivedSectionsWithSupportUnit X Z hZ)
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
```

**`Stacks.Cohomology.SectionsWithSupport.canonicalDerivedSectionsOnComplement_isRightDerivedFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean#L191). The attribute's comment: “RΓ(U, -) for U = X ∖ Z on the unbounded derived category D(O\_X) exists: the third term of the triangle is a genuine right derived functor of sections on the complement”.

> `RΓ(U, -)`, with its unit, is a right derived functor of sections on the complement
> along the quasi-isomorphisms of the unbounded homotopy category.

```lean
public instance canonicalDerivedSectionsOnComplement_isRightDerivedFunctor :
    (canonicalDerivedSectionsOnComplement X Z hZ).IsRightDerivedFunctor
      (canonicalDerivedSectionsOnComplementUnit X Z hZ)
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))
```

**`Stacks.Cohomology.SectionsWithSupport.canonicalSectionsWithSupportTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/CanonicalSectionsWithSupportTriangle.lean#L262). The attribute's comment: “the distinguished triangle RΓ\_Z(X,K) → RΓ(X,K) → RΓ(U,K) → RΓ\_Z(X,K)[1] in D(O\_X(X)), at the three constructed derived functors, functorial for K in D(O\_X)”.

> **Stacks, Tag 0G71.**  Let `Z` be a closed subset of a ringed space `X` and let
> `U = X ∖ Z`.  The triangle
> `RΓ_Z(X, K) ⟶ RΓ(X, K) ⟶ RΓ(U, K) ⟶ RΓ_Z(X, K)[1]`
> is distinguished in `D(O_X(X))`, functorially in `K` in `D(O_X)`.  The three functors are
> the total right derived functors constructed above, the two forward arrows are the canonical
> ones, and the connecting morphism is a natural transformation independent of `K`; nothing is
> quantified over.

```lean
public theorem canonicalSectionsWithSupportTriangle_distinguished
    (K : DerivedModuleSheaves X) :
    canonicalSectionsWithSupportTriangle X Z hZ K ∈ distTriang (DerivedGlobalModules X)
```

**`Stacks.Cohomology.SectionsWithSupport.derivedSectionsWithSupportTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SectionsWithSupportTriangle.lean, line 868](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SectionsWithSupportTriangle.lean#L868).

> Derived sections with support, global derived sections, and derived
> sections on the open complement form a distinguished triangle, naturally in the object of
> the unbounded derived category.

```lean
public noncomputable def derivedSectionsWithSupportTriangle
    (X : RingedSpace.{u, u}) (Z : Set X) (hZ : IsClosed Z)
    (RΓZ RΓ RΓU : DerivedModuleSheaves X ⥤ DerivedGlobalModules X)
    (aZ : homotopyToDerived X (sectionsWithSupport X Z hZ) ⟶ DerivedCategory.Qh ⋙ RΓZ)
    (aX : homotopyToDerived X
      (SheafOfModules.evaluation (structureSheafRing X) (op ⊤)) ⟶
        DerivedCategory.Qh ⋙ RΓ)
    (aU : homotopyToDerived X (sectionsOnComplement X Z hZ) ⟶ DerivedCategory.Qh ⋙ RΓU)
    [RΓZ.IsRightDerivedFunctor aZ
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RΓ.IsRightDerivedFunctor aX
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RΓU.IsRightDerivedFunctor aU
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))] :
    SectionsWithSupportTriangleData X RΓZ RΓ RΓU
      (derivedSupportInclusion X Z hZ RΓZ RΓ aZ aX)
      (derivedRestrictionToComplement X Z hZ RΓ RΓU aX aU)
```

## Tag 0G72, a lemma

[Tag 0G72](https://stacks.math.columbia.edu/tag/0G72) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.derivedSupportedSectionsTriangleδ`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean#L457). The attribute's comment: “the connecting morphism δ of the triangle, as a term”.

> **The connecting map of Stacks 0G72, as a term.** For chosen right derived functors `RH` of
> `ℱ ↦ i_* ℋ_Z(ℱ)` and `RJ` of `ℱ ↦ j_*(ℱ|_U)`, this is the natural transformation
> `δ : RJ ⟶ RH⟦1⟧` completing the two canonical maps `RH ⟶ 𝟭` and `𝟭 ⟶ RJ` to a distinguished
> triangle, by `derivedSupportedSectionsTriangle_distinguished`.
>
> The existence statement `exists_derivedSupportedSectionsTriangle` is this map with the quantifier
> in front: the connecting map is constructed by
> `Stacks.Cohomology.RestrictionCover.derivedTriangleOfShortExactOnInjectives` as the connecting
> map of the short exact sequence of complexes obtained by applying the three functors to the
> functorial K-injective resolution, descended along the localization.

```lean
noncomputable def derivedSupportedSectionsTriangleδ :
    RJ ⟶ RH ⋙ shiftFunctor
      (DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X))) (1 : ℤ)
```

**`Stacks.Cohomology.SupportedComplexes.derivedSupportedSectionsTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean#L477). The attribute's comment: “the triangle i\_*RℋZ(K) ⟶ K ⟶ Rj\_*(K|\_U) ⟶ [1] is distinguished”.

> **Stacks 0G72.** The triangle of `derivedSupportedSectionsTriangle` is distinguished at every
> object `K` of `D(𝒪_X)`.

```lean
theorem derivedSupportedSectionsTriangle_distinguished
    (K : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X))) :
    derivedSupportedSectionsTriangle X Z hZ RH RJ aH aJ K ∈
      distTriang (DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)))
```

**`Stacks.Cohomology.SupportedComplexes.exists_derivedSupportedSectionsTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsSheafTriangle.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsSheafTriangle.lean#L337).

> **Stacks 0G72.** Let `Z` be a closed subset of a ringed space `X` and `j : U = X ∖ Z ⟶ X`
> the inclusion of the complement.  For arbitrary right derived functors `RH` of
> `ℱ ↦ i_* ℋ_Z(ℱ)` and `RJ` of `ℱ ↦ j_*(ℱ|_U)` on the unbounded derived category of
> `𝒪_X`-modules, the two canonical maps `RH ⟶ 𝟭` and `𝟭 ⟶ RJ` extend to a connecting map `δ`
> making `RH(K) ⟶ K ⟶ RJ(K) ⟶ RH(K)⟦1⟧` a distinguished triangle for every `K`.  All three maps
> are natural transformations of functors, so the triangle is functorial in `K`.

```lean
theorem exists_derivedSupportedSectionsTriangle (X : RingedSpace.{u, u}) (Z : Set X.carrier)
    (hZ : IsClosed Z)
    (RH RJ : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)))
    (aH : (supportedSectionsFunctor X Z).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RH)
    (aJ : (restrictPush (structureSheafRing X) (openComplement Z hZ)).mapHomotopyCategory
      (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RJ)
    [RH.IsRightDerivedFunctor aH
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (structureSheafRing X))
        (ComplexShape.up ℤ))]
    [RJ.IsRightDerivedFunctor aJ
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (structureSheafRing X))
        (ComplexShape.up ℤ))] :
    ∃ δ : RJ ⟶ RH ⋙ shiftFunctor
        (DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X))) (1 : ℤ),
      ∀ K, Triangle.mk ((derivedSupportedSectionsToId X Z RH aH).app K)
          ((idToDerivedRestrictPush X Z hZ RJ aJ).app K) (δ.app K) ∈
        distTriang (DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)))
```

## Tag 0G73, a lemma

[Tag 0G73](https://stacks.math.columbia.edu/tag/0G73) in the Stacks Project.

**`Stacks.SheafOfModules.SupportedSections.isZero_derivedSupportedSections_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/PushforwardFromDisjointOpen.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/PushforwardFromDisjointOpen.lean#L177).

> **Stacks 0G73.** Let `Z` be a closed subset of a ringed space `X` and let
> `j : (U, 𝒪_X|_U) ⟶ (X, 𝒪_X)` be the inclusion of an open subset with `U ∩ Z = ∅`. Then
> `R H_Z(Rj_* K) = 0` for every `K` in `D(𝒪_U)`.

```lean
theorem isZero_derivedSupportedSections_derivedPushforward
    (X : RingedSpace.{u, u}) (Z : Set X.carrier) (hZ : IsClosed Z) (U : Opens X.carrier)
    (hUZ : (U : Set X.carrier) ∩ Z = ∅)
    (Rj : DerivedCategory
        (_root_.SheafOfModules.{u} (structureSheafRing (X.restrict U.isOpenEmbedding))) ⥤
      DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)))
    (αj : (modulePushforward (X.ofRestrict U.isOpenEmbedding)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ Rj)
    [Rj.IsRightDerivedFunctor αj (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u} (structureSheafRing (X.restrict U.isOpenEmbedding)))
      (ComplexShape.up ℤ))]
    (RH : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing (RingedSpace.inverseImage X
        (ClosedImmersionSheaves.closedSubsetInclusion Z)))))
    (αH : (supportedSectionsOnClosedFunctor X Z hZ).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RH)
    [RH.IsRightDerivedFunctor αH (HomotopyCategory.quasiIso
      (_root_.SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ))]
    (K : DerivedCategory
      (_root_.SheafOfModules.{u} (structureSheafRing (X.restrict U.isOpenEmbedding)))) :
    IsZero (RH.obj (Rj.obj K))
```

## Tag 0G74, a lemma

[Tag 0G74](https://stacks.math.columbia.edu/tag/0G74) in the Stacks Project.

**`Stacks.Perfect.GysinAbelianSquare.pushforwardLocalCohomologyForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Gysin/GysinDifferentialSquare.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/Gysin/GysinDifferentialSquare.lean#L135). The attribute's comment: “part (2) at the GYSIN MAP'S TARGET: the underlying abelian sheaf of i\_*H^n\_T(F) is i\_*^ab H^n\_T(F\_ab), naturally in F, which is what lets H^n\_T act on a morphism that is additive but not O\_X-linear. No hypotheses beyond IsClosed T”.

> The underlying sheaf of abelian groups of `i_*ℋ ⁿ_T(ℱ[0])`, with the local cohomology sheaf
> taken as the degree-`n` cohomology sheaf of `R𝓗_T(ℱ[0])` in the unbounded derived category — the
> spelling of the target of `AlgebraicGeometry.Scheme.Hom.gysinMap` — is the abelian direct image of
> the abelian local cohomology sheaf `ℋ ⁿ_T(ℱ_ab)`, naturally in `ℱ`.

```lean
public def pushforwardLocalCohomologyForgetIso {T : Set X} (hT : IsClosed T) (n : ℕ) :
    GysinLocalCohomology.localCohomologyPushforwardFunctor hT (n : ℤ) ⋙ abelianSheaf X ≅
      abelianSheaf X ⋙ abelianLocalCohomologyPushforward X.toRingedSpace T hT n
```

**`Stacks.Cohomology.SupportedComplexes.localCohomologySheafForgetComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologyComparison.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologyComparison.lean#L251). The attribute's comment: “part (2), the canonical map; invertibility is proved in isIso\_localCohomologySheafForgetComparison\_of\_isRightDerivedFunctor”.

> **Stacks 0G74, part (2): the canonical map.** Let `Z` be a closed subset of a ringed space
> `X`, let `RH` be a right derived functor of the sections supported on `Z` of sheaves of
> `𝒪_X`-modules and `RHab` one of the sections supported on `Z` of abelian sheaves. This is the
> canonical map `RH_Z(K)_ab ⟶ RH_Z(K_ab)` in `D(Ab(Z))`, natural in `K`, induced through the
> universal property of `RH` by the underived comparison of supported sections.
>
> This map is an isomorphism: `isIso_localCohomologySheafForgetComparison_of_isRightDerivedFunctor`
> in `UnderlyingAbelianLocalCohomologyInvertible.lean` proves it, for `aHab` the derivation unit of
> a right derived functor of abelian supported sections.

```lean
def localCohomologySheafForgetComparison
    [RH.IsRightDerivedFunctor aH
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (structureSheafRing X))
        (ComplexShape.up ℤ))] :
    RH ⋙ underlyingDerivedSheaf (structureSheafRing (closedSubsetRingedSpace X Z)) ⟶
      underlyingDerivedSheaf (structureSheafRing X) ⋙ RHab
```

**`Stacks.Cohomology.SupportedComplexes.localCohomologySheafFunctorForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologyDegreewise.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologyDegreewise.lean#L123). The attribute's comment: “part (2) degreewise: ℋ ⁿ\_Z(ℱ)\_ab ≅ ℋ ⁿ\_Z(ℱ\_ab)”.

> **Stacks 0G74, part (2), on cohomology sheaves in every degree.** Let `Z` be a closed subset
> of a ringed space `X` and let `ℱ` be a sheaf of `𝒪_X`-modules with underlying abelian sheaf
> `ℱ_ab`. For every `n : ℕ` the degree-`n` local cohomology sheaf `ℋ ⁿ_Z(ℱ)`, an `𝒪_X|_Z`-module
> on `Z`, has underlying abelian sheaf the degree-`n` local cohomology sheaf `ℋ ⁿ_Z(ℱ_ab)` of the
> abelian sheaf `ℱ_ab`, naturally in `ℱ`.
>
> Both sides are Mathlib's `ℕ`-indexed `CategoryTheory.Functor.rightDerived`, of supported
> sections of `𝒪_X`-modules on the left and of abelian sheaves on the right. This is the statement
> a consumer needs in order to let `ℋ ⁿ_Z` act on a morphism of sheaves which is additive but not
> `𝒪_X`-linear — a de Rham differential, say: the morphism has no image under the module-level
> functor at all, but its underlying morphism of abelian sheaves has one under the abelian functor,
> and this isomorphism transports the result back.
>
> The proof passes from each `ℕ`-indexed derived functor to the degree-`n` cohomology of a total
> right derived functor on the unbounded derived category, where Stacks 0G74 part (2) applies, and
> back again; see the implementation notes.

```lean
def localCohomologySheafFunctorForgetIso (n : ℕ) :
    localCohomologySheafFunctor X Z hZ n ⋙
        _root_.SheafOfModules.toSheaf (structureSheafRing (closedSubsetRingedSpace X Z)) ≅
      _root_.SheafOfModules.toSheaf (structureSheafRing X) ⋙
        ClosedImmersionSheaves.localCohomologySheafFunctor Z hZ n
```

**`Stacks.Cohomology.SupportedComplexes.isIso_localCohomologySheafForgetComparison_of_isRightDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologyInvertible.lean, line 624](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologyInvertible.lean#L624). The attribute's comment: “part (2), invertibility of the canonical map”.

> **Stacks 0G74, part (2).** Let `Z` be a closed subset of a ringed space `X`, let `RH` be a
> right derived functor of the sections supported on `Z` of sheaves of `𝒪_X`-modules and let
> `RHab` be one of the sections supported on `Z` of abelian sheaves. The canonical map
>
> `RH_Z(K)_ab ⟶ RH_Z(K_ab)`
>
> of `localCohomologySheafForgetComparison` is an **isomorphism** in `D(Ab(Z))`, in all degrees.
>
> The proof is the source's. It is enough to check invertibility at the image of a K-injective
> complex `K` of `𝒪_X`-modules, and a K-injective resolution of `K` with injective terms has the
> same image in the derived category, so one may take the terms of `K` injective. There the
> derivation unit of `RH` is invertible because `K` is K-injective, and the transported unit is
> invertible by `abelianSupportedUnit_isIso_at_underlying_kInjective` — which is where flasqueness
> enters: the underlying abelian sheaf of an injective `𝒪_X`-module is flasque (Stacks 09SX), and
> supported sections of a flasque abelian sheaf are the kernel of a *surjection* between sections
> over two opens, so `K_ab` computes the derived functor even though it is neither K-injective nor
> a complex of injectives. The defining factorization
> `localCohomologySheafForgetComparison_fac` then forces the comparison itself to be
> invertible.

```lean
theorem isIso_localCohomologySheafForgetComparison_of_isRightDerivedFunctor
    (X : RingedSpace.{u, u}) (Z : Set X.carrier) (hZ : IsClosed Z)
    (RHab : DerivedCategory (Sheaf (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}) ⥤
      DerivedCategory (Sheaf (Opens.grothendieckTopology (TopCat.of Z)) AddCommGrpCat.{u}))
    (aHab : (abelianSupportedSectionsOnClosed X Z hZ).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RHab)
    [RHab.IsRightDerivedFunctor aHab
      (HomotopyCategory.quasiIso
        (Sheaf (Opens.grothendieckTopology X.carrier) AddCommGrpCat.{u}) (ComplexShape.up ℤ))]
    (RH : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory
        (_root_.SheafOfModules.{u} (structureSheafRing (closedSubsetRingedSpace X Z))))
    (aH : (supportedSectionsOnClosedFunctor X Z hZ).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RH)
    [RH.IsRightDerivedFunctor aH
      (HomotopyCategory.quasiIso (_root_.SheafOfModules.{u} (structureSheafRing X))
        (ComplexShape.up ℤ))] :
    IsIso (localCohomologySheafForgetComparison X Z hZ RHab aHab RH aH)
```

**`Stacks.Cohomology.SupportedComplexes.localCohomologySheafFunctorZeroForgetIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologySheaves.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianLocalCohomologySheaves.lean#L189). The attribute's comment: “part (2) in degree 0 only; the comparison in higher degrees is not proved here, see isIso\_localCohomologySheafForgetComparison\_of\_isRightDerivedFunctor for the derived form”.

> **Stacks 0G74, part (2), in degree zero.** Let `Z` be a closed subset of a ringed space `X`
> and let `ℱ` be a sheaf of `𝒪_X`-modules with underlying abelian sheaf `ℱ_ab`. The degree-zero
> local cohomology sheaf `ℋ ⁰_Z(ℱ)`, an `𝒪_X|_Z`-module on `Z`, has underlying abelian sheaf the
> degree-zero local cohomology sheaf `ℋ ⁰_Z(ℱ_ab)` of `ℱ_ab`, naturally in `ℱ`.
>
> In degree zero both sides are the supported-sections functor itself, `H_Z` being left exact, so
> this is `supportedSectionsOnClosedForgetIso` read through the two degree-zero
> identifications.

```lean
def localCohomologySheafFunctorZeroForgetIso (hZ : IsClosed Z) :
    localCohomologySheafFunctor X Z hZ 0 ⋙
        _root_.SheafOfModules.toSheaf (structureSheafRing (closedSubsetRingedSpace X Z)) ≅
      _root_.SheafOfModules.toSheaf (structureSheafRing X) ⋙
        ClosedImmersionSheaves.localCohomologySheafFunctor Z hZ 0
```

**`Stacks.Cohomology.UnderlyingAbelianSectionsWithSupport.sectionsWithSupportForgetComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianSectionsWithSupport.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianSectionsWithSupport.lean#L531). The attribute's comment: “part (1), the canonical map, for given right derived functors of sections with support”.

> **Stacks 0G74, part (1): the canonical map.**  Let `Z` be a closed subset of a ringed space
> `X`, let `RΓZ` be a right derived functor of sections with support in `Z` of sheaves of
> `O_X`-modules and `RΓZab` one of sections with support in `Z` of abelian sheaves.  This is the
> canonical map `RΓ_Z(X, K) ⟶ RΓ_Z(X, K_ab)` in `D(Ab)`, natural in `K`, induced through the
> universal property of `RΓZ` by the underived comparison of sections with support.

```lean
def sectionsWithSupportForgetComparison
    [RΓZ.IsRightDerivedFunctor aZ
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RΓZab.IsRightDerivedFunctor aZab
      (HomotopyCategory.quasiIso (AbelianSheavesOnSpace X) (ComplexShape.up ℤ))] :
    RΓZ ⋙ underlyingDerivedGlobalModules X ⟶
      underlyingDerivedSheaf (structureSheafRing X) ⋙ RΓZab
```

**`Stacks.Cohomology.UnderlyingAbelianSectionsWithSupport.sectionsWithSupportForgetComparison_isIso`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianSectionsWithSupport.lean, line 560](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/UnderlyingAbelianSectionsWithSupport.lean#L560). The attribute's comment: “part (1), the map is an isomorphism, for given right derived functors of Gamma\_Z”.

> **Stacks 0G74, part (1).**  Let `(X, O_X)` be a ringed space, `Z ⊆ X` a closed subset and
> `K` an object of `D(O_X)` with image `K_ab` in `D(ℤ_X)`.  The canonical map
> `RΓ_Z(X, K) ⟶ RΓ_Z(X, K_ab)` is an isomorphism in `D(Ab)`, naturally in `K`.

```lean
instance sectionsWithSupportForgetComparison_isIso
    [RΓZ.IsRightDerivedFunctor aZ
      (HomotopyCategory.quasiIso (ModuleSheaves X) (ComplexShape.up ℤ))]
    [RΓZab.IsRightDerivedFunctor aZab
      (HomotopyCategory.quasiIso (AbelianSheavesOnSpace X) (ComplexShape.up ℤ))] :
    IsIso (sectionsWithSupportForgetComparison X Z hZ RΓZab aZab RΓZ aZ)
```

## Tag 0G75, a remark

[Tag 0G75](https://stacks.math.columbia.edu/tag/0G75) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.supportedTensorMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean#L215). The attribute's comment: “the canonical map `K|_Z ⊗^L R𝓗_Z(M) ⟶ R𝓗_Z(K ⊗^L M)`; not functoriality in either complex”.

> **Stacks Project, Tag 0G75.** For `K` and `M` in `D(𝒪_X)` and `i : Z ⟶ X` the inclusion of
> a closed subset, the canonical map `K|_Z ⊗^L_{𝒪_X|_Z} R𝓗_Z(M) ⟶ R𝓗_Z(K ⊗^L_{𝒪_X} M)` in
> `D(𝒪_X|_Z)`: the map corresponding to `supportedTensorMateMap` under the adjunction
> `i_* ⊣ R𝓗_Z` of Tag 0A3B.

```lean
def supportedTensorMap
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    ((derivedTensorProductFunctor (closedSubsetRingedSpace X Z).sheaf).obj
        ((derivedPullback (closedSubsetInclusion X Z)).obj K)).obj
        ((derivedSupportedSectionsOnClosed X Z hZ).obj M) ⟶
      (derivedSupportedSectionsOnClosed X Z hZ).obj
        (((derivedTensorProductFunctor X.sheaf).obj K).obj M)
```

**`Stacks.Cohomology.SupportedComplexes.supportedTensorMap_mate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean#L228). The attribute's comment: “the adjunction equation characterizing the canonical map”.

> **Stacks Project, Tag 0G75.** The adjunction equation characterizing the canonical map:
> pushing it forward and composing with the counit of Tag 0A3B gives the displayed composite.
> This is what "by adjointness of `i_*` and `R𝓗_Z`" means in the source.

```lean
theorem supportedTensorMap_mate
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.map
          (supportedTensorMap X Z hZ K M) ≫
        (derivedPushforwardAdjunction X Z hZ).counit.app
          (((derivedTensorProductFunctor X.sheaf).obj K).obj M) =
      supportedTensorMateMap X Z hZ K M
```

## Tag 0G76, a remark

[Tag 0G76](https://stacks.math.columbia.edu/tag/0G76) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.supportedCupProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean#L298). The attribute's comment: “the cup product `H^a(X, K) × H^b_Z(X, M) ⟶ H^(a+b)_Z(X, K ⊗^L M)`, as the source's four-step composite over an arbitrary presentation of the three groups by corepresenting objects; the source's own presentation by shifted structure sheaves is `supportedCupProductOfClasses`”. References: SGA 4½ Cycle (1.2.2), “(1.2.2.3), special case”.

> **Stacks Project, Tag 0G76.** The cup product of a class `ξ` on `X` with a class `η`
> supported on `Z`: restrict `ξ` to `Z`, tensor the two on `Z`, and follow with the map of
> Tag 0G75. Reading `W = 𝒪_Z[-a-b]`, `U = 𝒪_X[-a]` and `V = 𝒪_Z[-b]`, and reading morphisms
> out of `𝒪_Z[-n]` into `R𝓗_Z(-)` as classes in `H^n_Z(X, -)` by Tag 0G70, this is the source's
> `H^a(X, K) × H^b_Z(X, M) ⟶ H^{a+b}_Z(X, K ⊗^L M)`. The source's identification
> `𝒪_Z[-a-b] = (𝒪_X[-a])|_Z ⊗^L 𝒪_Z[-b]` is the morphism `χ`.

```lean
def supportedCupProduct
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    {U : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))}
    {V W : DerivedCategory (SheafOfModules.{u}
      (structureSheafRing (closedSubsetRingedSpace X Z)))}
    (χ : W ⟶ ((derivedTensorProductFunctor (closedSubsetRingedSpace X Z).sheaf).obj
      ((derivedPullback (closedSubsetInclusion X Z)).obj U)).obj V)
    (ξ : U ⟶ K) (η : V ⟶ (derivedSupportedSectionsOnClosed X Z hZ).obj M) :
    W ⟶ (derivedSupportedSectionsOnClosed X Z hZ).obj
      (((derivedTensorProductFunctor X.sheaf).obj K).obj M)
```

**`Stacks.Cohomology.SupportedComplexes.supportedCupProductOfClasses`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean, line 356](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedTensor.lean#L356). The attribute's comment: “the cup product `H^a(X, K) × H^b_Z(X, M) ⟶ H^(a+b)_Z(X, K ⊗^L M)` on classes represented by morphisms out of shifted structure sheaves, in the source's degrees”. References: SGA 4½ Cycle (1.2.2), “(1.2.2.2)”.

> **Stacks Project, Tag 0G76.** The cup product of a class `ξ ∈ H^a(X, K)` and a class
> `η ∈ H^b_Z(X, M) = H^b(Z, R𝓗_Z(M))`, landing in
> `H^{a+b}_Z(X, K ⊗^L M) = H^{a+b}(Z, R𝓗_Z(K ⊗^L M))`: restrict `ξ` to `Z`, tensor the two classes
> on `Z` and follow with the map of Tag 0G75, after the identification
> `𝒪_Z[-a-b] = (𝒪_X[-a])|_Z ⊗^L 𝒪_Z[-b]` of the corepresenting objects.

```lean
def supportedCupProductOfClasses
    (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (a b : ℤ)
    (ξ : shiftedStructureSheaf X a ⟶ K)
    (η : shiftedStructureSheaf (closedSubsetRingedSpace X Z) b ⟶
      (derivedSupportedSectionsOnClosed X Z hZ).obj M) :
    shiftedStructureSheaf (closedSubsetRingedSpace X Z) (a + b) ⟶
      (derivedSupportedSectionsOnClosed X Z hZ).obj
        (((derivedTensorProductFunctor X.sheaf).obj K).obj M)
```

## Tag 0G77, a lemma

[Tag 0G77](https://stacks.math.columbia.edu/tag/0G77) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.forgetSupport_supportedCupProduct_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ForgetSupportCupProductComparison.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ForgetSupportCupProductComparison.lean#L244).

> **Stacks Project, Tag 0G77.** Let `Z` be a closed subset of a ringed space `(X, 𝒪_X)` and let
> `K`, `M` be objects of `D(𝒪_X)`. The square
>
> ```
> H^a(X, K) × H^b_Z(X, M) -----> H^{a+b}_Z(X, K ⊗^L M)
>     |                                  |
>     v                                  v
> H^a(X, K) × H^b(X, M) -------> H^{a+b}(X, K ⊗^L M)
> ```
>
> commutes, where the top arrow is the cup product of [Stacks, Tag 0G76], the bottom arrow is the
> cup product of [Stacks, Tag 0FP2] and the verticals forget support. A class of `H^a(X, K)` is a
> morphism `ξ : 𝒪_X[-a] ⟶ K` and a class of `H^b_Z(X, M) = H^b(Z, R𝓗_Z(M))` is a morphism
> `η : 𝒪_Z[-b] ⟶ R𝓗_Z(M)` ([Stacks, Tag 0G70]); forgetting support is precomposition with the
> comparison `𝒪_X[-p] ⟶ i_*𝒪_Z[-p]` followed by the counit `i_*R𝓗_Z(-) ⟶ -` of
> [Stacks, Tag 0A3B].

```lean
theorem forgetSupport_supportedCupProduct_square (X : RingedSpace.{u, u}) (Z : Set X.carrier)
    (hZ : IsClosed Z) (a b : ℤ) (K M : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (ξ : shiftedUnitObject X a ⟶ K)
    (η : shiftedUnitObject (closedSubsetRingedSpace X Z) b ⟶
      (derivedSupportedSectionsOnClosed X Z hZ).obj M) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    shiftedUnitToPushforward Z (a + b) ≫
        (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.map
          (supportedCupProductOfClasses X Z hZ K M a b ξ η) ≫
        (derivedPushforwardAdjunction X Z hZ).counit.app
          (((derivedTensorProductFunctor X.sheaf).obj K).obj M) =
      (shiftedUnitTensorIso X a b).hom ≫
        ((derivedTensorProductFunctor X.sheaf).map ξ).app (shiftedUnitObject X b) ≫
        ((derivedTensorProductFunctor X.sheaf).obj K).map
          (shiftedUnitToPushforward Z b ≫
            (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.map η ≫
            (derivedPushforwardAdjunction X Z hZ).counit.app M)
```

## Tag 0G78, a remark

[Tag 0G78](https://stacks.math.columbia.edu/tag/0G78) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.isIso_supportedPullbackMap_of_cohomologySupportedOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedPullbackInvertible.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedPullbackInvertible.lean#L234). The attribute's comment: “the canonical map is an isomorphism when K has cohomology sheaves supported on Z, for an arbitrary morphism of ringed spaces”.

> **The canonical map of [Stacks, Tag 0G78] is an isomorphism at a complex supported on `Z`.**
> If every cohomology sheaf of `K` is supported on `Z` then the adjunction map
> `ε_K : i_* R𝓗_Z(K) ⟶ K` is itself an isomorphism, by [Stacks, Tag 0AEF] part (2), so the
> hypothesis of `isIso_supportedPullbackMap_of_isIso_map_counit` is immediate.
>
> No hypothesis on `f` is used. This is the special case of the invertibility of Tag 0G78 that
> the library's Tag 0AEF already supplies, for an arbitrary morphism of ringed spaces; for an open
> immersion and an arbitrary `K` see `isIso_supportedPullbackMap_of_isOpenImmersion`.

```lean
theorem isIso_supportedPullbackMap_of_cohomologySupportedOn
    (hZ' : IsClosed (closedSubsetPreimage f Z))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (hK : AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X) Z K) :
    IsIso (supportedPullbackMap f Z hZ hZ' K)
```

**`Stacks.Cohomology.SupportedComplexes.isIso_supportedPullbackMap_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedPullbackOpenImmersion.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedPullbackOpenImmersion.lean#L241). The attribute's comment: “the canonical map is an isomorphism along an open immersion of ringed spaces, unconditionally”.

> **[Stacks, Tag 0G78] along an open immersion, unconditionally.**  For an open immersion of
> ringed spaces `f : X' ⟶ X`, a closed `Z ⊆ X` and `Z' = f^{-1}(Z)`, the canonical map
>
> `L(f|_{Z'})^* R𝓗_Z(K) ⟶ R𝓗_{Z'}(Lf^* K)`
>
> of [Stacks, Tag 0G78] is an isomorphism for every `K` in `D(𝒪_X)`.
>
> Nothing is assumed beyond `f` being an open immersion and `Z` being closed.  The proof is
> `isIso_supportedPullbackMap_of_natIso` applied to
> `derivedSupportedSectionsOnClosedPullbackNatIso`.

```lean
theorem isIso_supportedPullbackMap_of_isOpenImmersion (hZ : IsClosed Z)
    (hZ' : IsClosed (closedSubsetPreimage f Z))
    (K : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X))) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    letI := pushforward_preservesFiniteLimits X' (closedSubsetPreimage f Z)
    letI := pushforward_preservesFiniteColimits X' (closedSubsetPreimage f Z) hZ'
    IsIso (supportedPullbackMap f Z hZ hZ' K)
```

**`Stacks.Cohomology.SupportedComplexes.isIso_supportedPullbackBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean#L449). The attribute's comment: “the Remark's own assertion that the map of functors Lf^* i\_* -> i'\_* L(f|Z')^* of Remark 20.28.3 (Tag 08HY) is an isomorphism in this case, proved for every M in D(O\_X|Z), in particular at M = RHZ(K); the source's stalkwise justification is replaced by the essential-image half of Tag 0AEF part (2)”.

> **[Stacks, Tag 0G78]: the map of functors of [Stacks, Tag 08HY] is an isomorphism in this
> case**, for every object of `D(𝒪_X|_Z)`. The
> base-change transformation of [Stacks, Tag 08HY] for the square of the restriction,
>
> `Lf^*(Ri_*M) ⟶ Ri'_*(L(f|_{Z'})^*M)`,
>
> is an isomorphism for every `M`, in particular at `M = R𝓗_Z(K)`.
>
> This is the essential-image half of [Stacks, Tag 0AEF] part (2) applied twice. The base-change
> map is, by [Stacks, Tag 08HY]'s adjoint characterization, the unit of `Li'^* ⊣ Ri'_*` at
> `Lf^*(Ri_*M)` followed by `Ri'_*` of a composite of three isomorphisms: the two composition
> isomorphisms of [Stacks, Tag 0D5S], and the derived counit `Li^*(Ri_*M) ⟶ M`, which is
> invertible because `Ri_*` is fully faithful for a closed-subset inclusion. So only the unit is
> in question, and the unit of an adjunction with fully faithful right adjoint is invertible
> exactly on the essential image of that right adjoint. The source `Lf^*(Ri_*M)` lies there:
> `Ri_*M` has its cohomology supported on `Z`, derived pullback carries that to support on
> `Z' = f^{-1}(Z)` by `cohomologySupportedOn_derivedPullback`, and [Stacks, Tag 0AEF] part (2)
> puts every `Z'`-supported complex in the essential image of `Ri'_*`.

```lean
theorem isIso_supportedPullbackBaseChangeMap
    (M : DerivedCategory (SheafOfModules.{u}
      (structureSheafRing (closedSubsetRingedSpace X Z)))) :
    IsIso (supportedPullbackBaseChangeMap f Z M)
```

**`Stacks.Cohomology.SupportedComplexes.supportedPullbackMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean#L523). The attribute's comment: “the canonical map and the adjunction equation characterizing it; the invertibility of the base-change transformation of Tag 08HY, which is the stalkwise step of the source, is isIso\_supportedPullbackBaseChangeMap above”.

> **[Stacks, Tag 0G78].** Let `f : (X', 𝒪_{X'}) ⟶ (X, 𝒪_X)` be a morphism of ringed spaces,
> let `Z ⊆ X` be closed and let `Z' = f^{-1}(Z)`. For `K` in `D(𝒪_X)` the canonical map
>
> `L(f|_{Z'})^* R𝓗_Z(K) ⟶ R𝓗_{Z'}(Lf^* K)`
>
> in `D(𝒪_{X'}|_{Z'})`: the map corresponding to `supportedPullbackMateMap` under the adjunction
> `i'_* ⊣ R𝓗_{Z'}` of [Stacks, Tag 0A3B] part (1).

```lean
def supportedPullbackMap (hZ' : IsClosed (closedSubsetPreimage f Z))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    (derivedPullback (closedSubsetRestriction f Z)).obj
        ((derivedSupportedSectionsOnClosed X Z hZ).obj K) ⟶
      (derivedSupportedSectionsOnClosed X' (closedSubsetPreimage f Z) hZ').obj
        ((derivedPullback f).obj K)
```

**`Stacks.Cohomology.SupportedComplexes.supportedPullbackMap_mate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean#L538). The attribute's comment: “the factorization of the pulled-back adjunction map through the adjunction map on the preimage”.

> **[Stacks, Tag 0G78], the adjunction equation characterizing the canonical map.** Pushing the
> canonical map forward from `Z'` and composing with the adjunction map
> `i'_* R𝓗_{Z'}(Lf^* K) ⟶ Lf^* K` of [Stacks, Tag 0A3B] gives the displayed composite. This is the
> unique factorization that the source obtains from part (3) of [Stacks, Tag 0AEF].

```lean
theorem supportedPullbackMap_mate (hZ' : IsClosed (closedSubsetPreimage f Z))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    (modulePushforward
            (closedSubsetInclusion X' (closedSubsetPreimage f Z))).mapDerivedCategory.map
          (supportedPullbackMap f Z hZ hZ' K) ≫
        (derivedPushforwardAdjunction X' (closedSubsetPreimage f Z) hZ').counit.app
          ((derivedPullback f).obj K) =
      supportedPullbackMateMap f Z hZ K
```

**`Stacks.Cohomology.SupportedComplexes.supportedPullbackMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean, line 556](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean#L556). The attribute's comment: “the uniqueness the Remark asserts: 'we find that the south-east arrow factors UNIQUELY over the south-west arrow'. This is the half of the universality of Tag 0AEF part (3) that supportedPullbackMap\_mate does not state, and it is what makes the canonical map canonical -- neither the zero map nor the negative of it satisfies the characterization”.

> The adjunction equation determines the canonical map of [Stacks, Tag 0G78]: no other
> morphism of that type satisfies it. Together with `supportedPullbackMap_mate` this says the map
> is the unique solution of the characterization, so the construction is not under-determined.

```lean
theorem supportedPullbackMap_unique (hZ' : IsClosed (closedSubsetPreimage f Z))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (g : (derivedPullback (closedSubsetRestriction f Z)).obj
        ((derivedSupportedSectionsOnClosed X Z hZ).obj K) ⟶
      (derivedSupportedSectionsOnClosed X' (closedSubsetPreimage f Z) hZ').obj
        ((derivedPullback f).obj K))
    (hg : (modulePushforward
              (closedSubsetInclusion X' (closedSubsetPreimage f Z))).mapDerivedCategory.map g ≫
          (derivedPushforwardAdjunction X' (closedSubsetPreimage f Z) hZ').counit.app
            ((derivedPullback f).obj K) =
        supportedPullbackMateMap f Z hZ K) :
    g = supportedPullbackMap f Z hZ hZ' K
```

**`Stacks.Cohomology.SupportedComplexes.supportedPullbackMap_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean, line 587](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDerivedPullback.lean#L587). The attribute's comment: “the commutative triangle, with the base-change transformation of Tag 08HY on the left”.

> **[Stacks, Tag 0G78], the commutative triangle of the source.** Composing the base-change
> transformation of [Stacks, Tag 08HY] with the pushforward from `Z'` of the canonical map and the
> adjunction map `i'_* R𝓗_{Z'}(Lf^* K) ⟶ Lf^* K` gives the derived pullback along `f` of the
> adjunction map `i_* R𝓗_Z(K) ⟶ K`.
>
> This is `supportedPullbackMap_mate` with the inverse of the base-change transformation cleared
> from the statement, so it is the triangle of the source read literally: the diagonal arrow out
> of `Lf^*(i_* R𝓗_Z(K))` factors through the adjunction map on the preimage.

```lean
theorem supportedPullbackMap_triangle (hZ' : IsClosed (closedSubsetPreimage f Z))
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    supportedPullbackBaseChangeMap f Z ((derivedSupportedSectionsOnClosed X Z hZ).obj K) ≫
          (closedPushforwardComparison X' (closedSubsetPreimage f Z)).inv.app _ ≫
          (modulePushforward
              (closedSubsetInclusion X' (closedSubsetPreimage f Z))).mapDerivedCategory.map
            (supportedPullbackMap f Z hZ hZ' K) ≫
          (derivedPushforwardAdjunction X' (closedSubsetPreimage f Z) hZ').counit.app
            ((derivedPullback f).obj K) =
      (derivedPullback f).map ((closedPushforwardComparison X Z).inv.app _) ≫
        (derivedPullback f).map ((derivedPushforwardAdjunction X Z hZ).counit.app K)
```

## Tag 0G79, a lemma

[Tag 0G79](https://stacks.math.columbia.edu/tag/0G79) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.forgetSupport_pullbackSupportedClass_preimage_shiftedUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ForgetSupportAndPullback.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/ForgetSupportAndPullback.lean#L502). The attribute's comment: “the commuting square for the canonical map of Tag 0G78 itself, at the canonical corepresenting objects: the four groups are corepresented by the shifted structure sheaves of Tag 0G70, the four comparisons between them are the canonical ones, and their agreement across the square -- the pseudofunctoriality of the structure-sheaf comparison of Tag 01CD with respect to the composition isomorphism of derived pullbacks of Tag 0D5S -- is StacksDraft.UnitPullbackComposition.shiftedUnitIso\_square\_left. The binders are the degree p, the complex K and the class eta, which are the data of a class in H^p\_Z(X, K)”.

> **Stacks Project, Tag 0G79, at the canonical corepresenting objects.** The four groups are
> corepresented by the shifted structure sheaves of [Stacks, Tag 0G70] — `𝒪_X[-p]`, `𝒪_{X'}[-p]`,
> `𝒪_Z[-p]`, `𝒪_{Z'}[-p]` with `Z' = f^{-1}(Z)` — and the four comparisons between them are the
> canonical ones: `ρ`, `ρ'` are `shiftedUnitToPushforward`, and `c`, `d` are the identifications
> `Lf^*(𝒪_X[-p]) ≅ 𝒪_{X'}[-p]` of `Stacks.RingedSpace.derivedPullbackShiftedUnitIso`.
>
> Those four identifications agree across the square — that is the
> *pseudofunctoriality of the structure-sheaf comparison* of [Stacks, Tag 01CD] with respect to
> the composition isomorphism of [Stacks, Tag 0D5S], in which no derived pushforward, no
> base-change transformation of [Stacks, Tag 08HY], no `R𝓗_Z` and no adjunction map occur. It is
> proved in degree `0`
> (`StacksDraft.UnitPullbackComposition.derivedPullbackCompIsoCanonical_hom_app_singleUnit`), in
> an arbitrary degree `p`
> (`StacksDraft.UnitPullbackComposition.derivedPullbackCompIsoCanonical_hom_app_shiftedUnit`,
> which also needed the first `CategoryTheory.NatTrans.CommShift` for the composition comparison
> of [Stacks, Tag 0D5S],
> `StacksDraft.UnitPullbackComposition.commShift_derivedPullbackCompComparisonCanonical`), and
> around the square in the spelling this statement needs
> (`StacksDraft.UnitPullbackComposition.shiftedUnitIso_square_left`), which is what is supplied
> below.

```lean
theorem forgetSupport_pullbackSupportedClass_preimage_shiftedUnit (p : ℤ)
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)))
    (η : shiftedUnitObject (closedSubsetRingedSpace X Z) p ⟶
      (derivedSupportedSectionsOnClosed X Z hZ).obj K) :
    shiftedUnitToPushforward (X := X') (closedSubsetPreimage f Z) p ≫
        (modulePushforward
            (closedSubsetInclusion X' (closedSubsetPreimage f Z))).mapDerivedCategory.map
          ((derivedPullbackShiftedUnitIso (closedSubsetRestriction f Z) p).inv ≫
            (derivedPullback (closedSubsetRestriction f Z)).map η ≫
            supportedPullbackMap f Z hZ (isClosed_closedSubsetPreimage f Z hZ) K) ≫
        (derivedPushforwardAdjunction X' (closedSubsetPreimage f Z)
            (isClosed_closedSubsetPreimage f Z hZ)).counit.app ((derivedPullback f).obj K) =
      (derivedPullbackShiftedUnitIso f p).inv ≫ (derivedPullback f).map
        (shiftedUnitToPushforward Z p ≫
          (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.map η ≫
          (derivedPushforwardAdjunction X Z hZ).counit.app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.34, Tag 0G6Y](https://stacks.math.columbia.edu/tag/0G6Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
