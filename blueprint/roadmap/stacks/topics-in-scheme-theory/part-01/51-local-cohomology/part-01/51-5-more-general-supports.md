---
declaration: section
origin: cited
lean: Stacks.LocalCohomology.sectionsWithSupportIn_eq_top_iff, Stacks.LocalCohomology.supportModuleProperty_isSerreClass, Stacks.LocalCohomology.supportModuleProperty_isClosedUnderCoproducts, Stacks.LocalCohomology.derivedInclusion_adj_derivedSupportedSections, Stacks.LocalCohomology.derivedSupportedSections_comp_inclusion_iso, Stacks.LocalCohomology.colimitClosedSupportComparison_isIso, Module.exists_supportedModulesDerivedPlusEquivalence, Stacks.LocalCohomology.supportedModulesComparison_isEquivalence
statement: formalized
proof: formalized
---

# 51.5 More general supports

Section 51.5 of the Stacks Project, [Tag 0EEY](https://stacks.math.columbia.edu/tag/0EEY). 9 tags here are carried by 29 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EEZ, a lemma

[Tag 0EEZ](https://stacks.math.columbia.edu/tag/0EEZ) in the Stacks Project.

**`Stacks.LocalCohomology.sectionsWithSupportIn_eq_top_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModulesSupportedIn.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModulesSupportedIn.lean#L113). The attribute's comment: “equivalence”. References: EGA IV (5.9.12), “affine module case”.

> Degree-zero sections with support in `T` fill `M` if and only if the support of `M` is
> contained in `T`.

```lean
theorem sectionsWithSupportIn_eq_top_iff (A : Type u) [CommRing A]
    (T : Set (PrimeSpectrum A)) (M : Type v) [AddCommGroup M] [Module A M] :
    sectionsWithSupportIn A T M = ⊤ ↔ Module.support A M ⊆ T
```

**`Stacks.LocalCohomology.supportModuleProperty_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModulesSupportedIn.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModulesSupportedIn.lean#L126). The attribute's comment: “Serre subcategory”. References: EGA IV (5.9.12), “(i) C\_Z is Serre, affine”.

> Modules whose support is contained in `T` form a Serre subcategory of `A`-modules.

```lean
instance supportModuleProperty_isSerreClass (A : Type u) [CommRing A]
    (T : Set (PrimeSpectrum A)) :
    (supportModuleProperty A T : ObjectProperty (ModuleCat.{v} A)).IsSerreClass
```

**`Stacks.LocalCohomology.supportModuleProperty_isClosedUnderCoproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/ModulesSupportedIn.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/ModulesSupportedIn.lean#L183). The attribute's comment: “closed under direct sums”.

> Modules whose support is contained in `T` are closed under arbitrary direct sums.

```lean
instance supportModuleProperty_isClosedUnderCoproducts (A : Type u) [CommRing A]
    (T : Set (PrimeSpectrum A)) (J : Type w) :
    (supportModuleProperty A T : ObjectProperty (ModuleCat.{v} A)).IsClosedUnderColimitsOfShape
      (Discrete J)
```

## Tag 0EF0, a lemma

[Tag 0EF0](https://stacks.math.columbia.edu/tag/0EF0) in the Stacks Project.

**`Stacks.LocalCohomology.derivedInclusion_adj_derivedSupportedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SupportedSectionsAdjunction.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SupportedSectionsAdjunction.lean#L173). The attribute's comment: “adjunction”.

> Let `A` be a Noetherian ring and `T ⊆ Spec A` be stable under specialization. Then
> `RH⁰_T : D(A) ⥤ D(Mod_{A,T})` is right adjoint to the functor `D(Mod_{A,T}) ⥤ D(A)` induced by
> the inclusion.

```lean
theorem derivedInclusion_adj_derivedSupportedSections (A : Type u) [CommRing A]
    [IsNoetherianRing A] (T : Set (PrimeSpectrum A)) (_hT : StableUnderSpecialization T) :
    Nonempty
      ((supportModuleProperty A T :
          ObjectProperty (ModuleCat.{max u v} A)).ι.mapDerivedCategory ⊣
        derivedSupportedSections.{u, v} A T)
```

**`Stacks.LocalCohomology.derivedSupportedSections_comp_inclusion_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SupportedSectionsAdjunction.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SupportedSectionsAdjunction.lean#L280). The attribute's comment: “comparison with ambient derived sections”.

> Let `A` be a Noetherian ring and `T ⊆ Spec A` be stable under specialization. Composing
> `RH⁰_T : D(A) ⥤ D(Mod_{A,T})` with the derived inclusion recovers the derived sections with
> support in `T` taken in `D(A)`.

```lean
theorem derivedSupportedSections_comp_inclusion_iso (A : Type u) [CommRing A]
    [IsNoetherianRing A] (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T) :
    Nonempty
      (derivedSupportedSections.{u, v} A T ⋙
        (supportModuleProperty A T :
            ObjectProperty (ModuleCat.{max u v} A)).ι.mapDerivedCategory ≅
          derivedSectionsWithSupportIn.{u, v} A T)
```

## Tag 0EF1, a lemma

[Tag 0EF1](https://stacks.math.columbia.edu/tag/0EF1) in the Stacks Project.

**`Stacks.LocalCohomology.colimitClosedSupportComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/ClosedSupportColimit.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/ClosedSupportColimit.lean#L699).

> **Stacks Project, Tag 0EF1.** For a Noetherian ring `A` and a specialization-stable subset
> `T` of its spectrum, the canonical comparison from the filtered colimit of local cohomology with
> closed support contained in `T` to the cohomology of derived sections with support in `T` is an
> isomorphism, naturally in the derived object.

```lean
theorem colimitClosedSupportComparison_isIso (A : Type u) [CommRing A] [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (_hT : StableUnderSpecialization T) (i : ℤ) :
    IsIso (colimitClosedSupportComparison.{u, v} A T i)
```

## Tag 0EF2, a lemma

[Tag 0EF2](https://stacks.math.columbia.edu/tag/0EF2) in the Stacks Project.

**`Module.exists_supportedModulesDerivedPlusEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/GeneralSupports/SupportedDerivedCategory.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/GeneralSupports/SupportedDerivedCategory.lean#L380).

> **Stacks Project, Tag 0EF2.** For a specialization-closed subset `T` of the spectrum of a
> Noetherian ring `A`, the canonical functor from the bounded-below derived category of modules
> supported in `T` to the bounded-below derived category with cohomology supported in `T` is an
> equivalence.

```lean
public theorem exists_supportedModulesDerivedPlusEquivalence
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (T : Set (PrimeSpectrum A)) (_hT : StableUnderSpecialization T) :
    ∃ (e : DerivedCategory.Plus (ModulesSupportedIn A T) ≌
        (DerivedCategoryB.derivedCategoryBPlus
          (supportModuleProperty A T)).FullSubcategory),
      Nonempty
        (e.functor ⋙
            (DerivedCategoryB.derivedCategoryBPlus
              (supportModuleProperty A T)).ι ≅
          DerivedCategory.Plus.ι ⋙
            (supportModuleProperty A T).ι.mapDerivedCategory)
```

## Tag 0EF3, a lemma

[Tag 0EF3](https://stacks.math.columbia.edu/tag/0EF3) in the Stacks Project.

**`Stacks.LocalCohomology.supportedModulesComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedModulesEquivalence.lean, line 862](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedModulesEquivalence.lean#L862).

> **Stacks Project, Tag 0EF3.** Let `A` be a Noetherian ring of finite Krull dimension and let
> `T ⊆ Spec(A)` be stable under specialization. The canonical functor from the derived category of
> the modules supported in `T` to the full subcategory of `D(A)` on the objects whose cohomology is
> supported in `T` is an equivalence.

```lean
theorem supportedModulesComparison_isEquivalence (A : Type u) [CommRing A]
    [IsNoetherianRing A] (T : Set (PrimeSpectrum A))
    (hT : StableUnderSpecialization T) (hdim : ringKrullDim A < ⊤) :
    (supportedModulesComparison.{u, v} A T).IsEquivalence
```

## Tag 0EF4, a remark

[Tag 0EF4](https://stacks.math.columbia.edu/tag/0EF4) in the Stacks Project.

**`Stacks.LocalCohomology.nonempty_derivedSectionsWithSupportInPlus_comp_inclusion_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/BoundedComparison.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/BoundedComparison.lean#L101). The attribute's comment: “cohomology\_calculation”. References: SGA 4 XVII (1.2.4), “special case”.

> The bounded-below and unbounded right derived functors of sections with support in `T` agree
> after including bounded-below complexes in the unbounded derived category.

```lean
theorem nonempty_derivedSectionsWithSupportInPlus_comp_inclusion_iso :
    Nonempty
      (derivedSectionsWithSupportInPlus.{u, v} A T ⋙ DerivedCategory.Plus.ι ≅
        DerivedCategory.Plus.ι ⋙ derivedSectionsWithSupportIn.{u, v} A T)
```

**`Stacks.LocalCohomology.sectionsWithSupportInFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean#L80). The attribute's comment: “local\_cohomology\_with\_support\_in\_t”.

> Degree-zero sections with support in `T`, functorial in the module: on objects, the
> filtered colimit of the `I`-power-torsion submodules over ideals whose zero locus is contained
> in `T`.

```lean
def sectionsWithSupportInFunctor (A : Type u) [CommRing A]
    (T : Set (PrimeSpectrum A)) : ModuleCat.{max u v} A ⥤ ModuleCat.{max u v} A
```

**`Stacks.LocalCohomology.derivedSectionsWithSupportInPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean#L115). The attribute's comment: “local\_cohomology\_with\_support\_in\_t”.

> The total right derived functor of degree-zero sections with support in `T`, on bounded-below
> derived objects.

```lean
noncomputable def derivedSectionsWithSupportInPlus (A : Type u) [CommRing A]
    (T : Set (PrimeSpectrum A)) :
    DerivedCategory.Plus (ModuleCat.{max u v} A) ⥤
      DerivedCategory.Plus (ModuleCat.{max u v} A)
```

**`Stacks.LocalCohomology.derivedSectionsWithSupportIn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean#L143). The attribute's comment: “local\_cohomology\_with\_support\_in\_t”.

> The total right derived functor of degree-zero sections with support in `T`, on the unbounded
> derived category.

```lean
noncomputable def derivedSectionsWithSupportIn (A : Type u) [CommRing A]
    (T : Set (PrimeSpectrum A)) :
    DerivedCategory (ModuleCat.{max u v} A) ⥤
      DerivedCategory (ModuleCat.{max u v} A)
```

**`Stacks.LocalCohomology.localCohomologyWithSupportInPlus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean#L181). The attribute's comment: “local\_cohomology\_with\_support\_in\_t”.

> The `i`-th local cohomology module with support in `T` of a bounded-below derived object.

```lean
noncomputable abbrev localCohomologyWithSupportInPlus
    (A : Type u) [CommRing A] (T : Set (PrimeSpectrum A))
    (K : DerivedCategory.Plus (ModuleCat.{max u v} A)) (i : ℤ) :
    ModuleCat.{max u v} A
```

**`Stacks.LocalCohomology.localCohomologyWithSupportIn`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SectionsWithSupport.lean#L190). The attribute's comment: “local\_cohomology\_with\_support\_in\_t”.

> The `i`-th local cohomology module with support in `T` of an unbounded derived object.

```lean
noncomputable abbrev localCohomologyWithSupportIn
    (A : Type u) [CommRing A] (T : Set (PrimeSpectrum A))
    (K : DerivedCategory (ModuleCat.{max u v} A)) (i : ℤ) : ModuleCat.{max u v} A
```

**`Stacks.LocalCohomology.isColimitClosedSupportCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedCohomologyColimit.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedCohomologyColimit.lean#L81). The attribute's comment: “cohomology\_colimit”.

> **Stacks Project, Tag 0EF4, the colimit formula.** Let `A` be a Noetherian ring and
> `T ⊆ Spec(A)` stable under specialization. For every `K` in `D(A)` and every `i`, the canonical
> cocone on the diagram of local cohomology `H^i_Z(K)` indexed by the closed subsets `Z ⊆ T` is a
> colimit cocone with vertex `H^i_T(K) = H^i(RΓ_T(K))`. That is,
> `H^i_T(K) = colim_{Z ⊆ T closed} H^i_Z(K)`, the index category being filtered.

```lean
def isColimitClosedSupportCocone [IsNoetherianRing A]
    (hT : StableUnderSpecialization T) (i : ℤ)
    (K : DerivedCategory (ModuleCat.{max u v} A)) :
    IsColimit (closedSupportCocone.{u, v} A T i K)
```

**`Stacks.LocalCohomology.colimitClosedSupportIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedCohomologyColimit.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedCohomologyColimit.lean#L95). The attribute's comment: “cohomology\_colimit”.

> **Stacks Project, Tag 0EF4, the colimit formula.** The isomorphism
> `colim_{Z ⊆ T closed} H^i_Z(K) ≅ H^i_T(K)` for `K` in `D(A)`, induced by the canonical maps
> `H^i_Z(K) ⟶ H^i_T(K)`.

```lean
def colimitClosedSupportIso [IsNoetherianRing A]
    (hT : StableUnderSpecialization T) (i : ℤ)
    (K : DerivedCategory (ModuleCat.{max u v} A)) :
    colimit ((closedSupportDiagram.{u, v} A T i).obj K) ≅
      localCohomologyWithSupportIn A T K i
```

**`Stacks.LocalCohomology.nonempty_colimitClosedSupportIsoPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedCohomologyColimit.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedCohomologyColimit.lean#L119). The attribute's comment: “cohomology\_colimit”.

> **Stacks Project, Tag 0EF4, the colimit formula on `D^+(A)`.** Let `A` be a Noetherian ring
> and `T ⊆ Spec(A)` stable under specialization. For `K` in `D^+(A)`, local cohomology with support
> in `T` computed by the bounded-below derived functor is again the filtered colimit of `H^i_Z(K)`
> over the closed subsets `Z ⊆ T`.

```lean
theorem nonempty_colimitClosedSupportIsoPlus [IsNoetherianRing A]
    (hT : StableUnderSpecialization T) (i : ℤ)
    (K : DerivedCategory.Plus (ModuleCat.{max u v} A)) :
    Nonempty
      (colimit ((closedSupportDiagram.{u, v} A T i).obj (DerivedCategory.Plus.ι.obj K)) ≅
        localCohomologyWithSupportInPlus A T K i)
```

**`Stacks.LocalCohomology.inclusion_adj_derivedSupportedSectionsComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedDerivedAdjunction.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedDerivedAdjunction.lean#L69). The attribute's comment: “unbounded\_adjunction”.

> **Stacks Project, Tag 0EF4, unbounded adjunction.** Let `A` be a Noetherian ring of finite
> Krull dimension and `T ⊆ Spec(A)` stable under specialization. The composite of `RH⁰_T` with the
> comparison into `D_T(A)` is right adjoint to the inclusion `D_T(A) ⥤ D(A)`.

```lean
theorem inclusion_adj_derivedSupportedSectionsComparison [IsNoetherianRing A]
    (hT : StableUnderSpecialization T) (hdim : ringKrullDim A < ⊤) :
    Nonempty
      ((DerivedCategoryB.derivedCategoryB
          (supportModuleProperty A T : ObjectProperty (ModuleCat.{max u v} A))).ι ⊣
        (derivedSupportedSections.{u, v} A T ⋙
          supportedModulesComparison.{u, max u v} A T))
```

**`Stacks.LocalCohomology.inclusion_adj_derivedSupportedSectionsPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedDerivedAdjunction.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedDerivedAdjunction.lean#L200). The attribute's comment: “bounded\_adjunction”.

> **Stacks Project, Tag 0EF4, bounded adjunction.** Let `A` be a Noetherian ring and
> `T ⊆ Spec(A)` stable under specialization. The composite of the bounded-below derived functor of
> sections with support in `T` with the comparison into `supportedPlusProperty` is right adjoint
> to the inclusion of that subcategory into `D^+(A)`.

```lean
theorem inclusion_adj_derivedSupportedSectionsPlus [IsNoetherianRing A]
    (hT : StableUnderSpecialization T) :
    Nonempty
      ((supportedPlusProperty.{u, v} A T).ι ⊣
        ((supportedSectionsFunctor.{u, v} A T).rightDerivedFunctorPlus ⋙
          comparisonPlus.{u, v} A T hT))
```

**`Stacks.LocalCohomology.nonempty_inclusion_adj_and_localCohomologyWithSupportIn_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedUpshot.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/SupportedUpshot.lean#L126).

> **Stacks Project, Tag 0EF4.** Let `A` be a Noetherian ring and `T ⊆ Spec(A)` a subset
> stable under specialization. Write `RΓ_T` for `RH^0_T` followed by the comparison
> `D(Mod_{A,T}) ⥤ D_T(A)`, on `D^+(A)` and on `D(A)`. Then:
>
> * `RΓ_T : D^+(A) ⥤ D_T^+(A)` is right adjoint to the inclusion `D_T^+(A) ⥤ D^+(A)`;
> * if `dim(A) < ∞`, then `RΓ_T : D(A) ⥤ D_T(A)` is right adjoint to the inclusion
>   `D_T(A) ⥤ D(A)`;
> * in both cases `H^i_T(K) = H^i(RΓ_T(K)) = R^iH^0_T(K) = colim_{Z ⊆ T closed} H^i_Z(K)`.
>
> Here `H^i_T(K)` is `localCohomologyWithSupportInPlus` (for `K` in `D^+(A)`) or
> `localCohomologyWithSupportIn` (for `K` in `D(A)`), the cohomology of the derived functor of
> `H^0_T : Mod_A ⥤ Mod_A`. For each of the two cases the theorem states: the adjunction; that the
> adjoint `RΓ_T`, followed by the inclusion of `D_T(A)`, is isomorphic to that derived functor; and,
> for every `K` and `i`, that `H^i(RΓ_T(K))`, `R^iH^0_T(K) = H^i(RH^0_T(K))` (the `i`-th
> cohomology in `Mod_{A,T}`, viewed as an `A`-module) and the filtered colimit of `H^i_Z(K)` over
> the closed subsets `Z ⊆ T` (`closedSupportIdeal_isFiltered`) are each isomorphic to `H^i_T(K)`.
> Only the adjunction on `D(A)` uses `dim(A) < ∞`.

```lean
theorem nonempty_inclusion_adj_and_localCohomologyWithSupportIn_colimit
    (A : Type u) [CommRing A] [IsNoetherianRing A] (T : Set (PrimeSpectrum A))
    (hT : StableUnderSpecialization T) :
    Nonempty
        ((supportedPlusProperty.{u, v} A T).ι ⊣
          ((supportedSectionsFunctor.{u, v} A T).rightDerivedFunctorPlus ⋙
            comparisonPlus.{u, v} A T hT)) ∧
      Nonempty
        (((supportedSectionsFunctor.{u, v} A T).rightDerivedFunctorPlus ⋙
            comparisonPlus.{u, v} A T hT) ⋙ (supportedPlusProperty.{u, v} A T).ι ≅
          derivedSectionsWithSupportInPlus.{u, v} A T) ∧
      (∀ (i : ℤ) (K : DerivedCategory.Plus (ModuleCat.{max u v} A)),
        Nonempty
            ((DerivedCategory.Plus.homologyFunctor (ModuleCat.{max u v} A) i).obj
                ((supportedPlusProperty.{u, v} A T).ι.obj
                  (((supportedSectionsFunctor.{u, v} A T).rightDerivedFunctorPlus ⋙
                    comparisonPlus.{u, v} A T hT).obj K)) ≅
              localCohomologyWithSupportInPlus A T K i) ∧
          Nonempty
            (((DerivedCategory.Plus.homologyFunctor (ModulesSupportedIn.{u, max u v} A T) i).obj
                ((supportedSectionsFunctor.{u, v} A T).rightDerivedFunctorPlus.obj K)).obj ≅
              localCohomologyWithSupportInPlus A T K i) ∧
          Nonempty
            (colimit ((closedSupportDiagram.{u, v} A T i).obj (DerivedCategory.Plus.ι.obj K)) ≅
              localCohomologyWithSupportInPlus A T K i)) ∧
      (ringKrullDim A < ⊤ →
        Nonempty
          ((DerivedCategoryB.derivedCategoryB
              (supportModuleProperty A T : ObjectProperty (ModuleCat.{max u v} A))).ι ⊣
            (derivedSupportedSections.{u, v} A T ⋙
              supportedModulesComparison.{u, max u v} A T))) ∧
      Nonempty
        ((derivedSupportedSections.{u, v} A T ⋙ supportedModulesComparison.{u, max u v} A T) ⋙
            (DerivedCategoryB.derivedCategoryB
              (supportModuleProperty A T : ObjectProperty (ModuleCat.{max u v} A))).ι ≅
          derivedSectionsWithSupportIn.{u, v} A T) ∧
      (∀ (i : ℤ) (K : DerivedCategory (ModuleCat.{max u v} A)),
        Nonempty
            ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} A) i).obj
                ((DerivedCategoryB.derivedCategoryB
                  (supportModuleProperty A T : ObjectProperty (ModuleCat.{max u v} A))).ι.obj
                  ((derivedSupportedSections.{u, v} A T ⋙
                    supportedModulesComparison.{u, max u v} A T).obj K)) ≅
              localCohomologyWithSupportIn A T K i) ∧
          Nonempty
            (((DerivedCategory.homologyFunctor (ModulesSupportedIn.{u, max u v} A T) i).obj
                ((derivedSupportedSections.{u, v} A T).obj K)).obj ≅
              localCohomologyWithSupportIn A T K i) ∧
          Nonempty
            (colimit ((closedSupportDiagram.{u, v} A T i).obj K) ≅
              localCohomologyWithSupportIn A T K i))
```

Declarations registered for the tag:

- [`colimitClosedSupportComparison_isIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=colimitClosedSupportComparison_isIso#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/LocalCohomology/BoundedComparison.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/BoundedComparison.lean#L108) (StacksFrontier): “cohomology\_calculation”.

## Tag 0EF5, a lemma

[Tag 0EF5](https://stacks.math.columbia.edu/tag/0EF5) in the Stacks Project.

**`Stacks.LocalCohomology.derivedSectionsWithSupportInPlusBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/BaseChangeGeneralSupport/BaseChangeIso.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/BaseChangeGeneralSupport/BaseChangeIso.lean#L388). The attribute's comment: “bounded-below case”. References: EGA IV (5.9.4), “affine case”.

> **Stacks Project, Tag 0EF5, the bounded-below case.** Let `f : A →+* B` be a flat
> homomorphism of Noetherian rings, let `T ⊆ Spec A` be stable under specialization and put
> `T' = (Spec f)⁻¹(T)`. Then local cohomology with support in `T` of a bounded-below complex
> commutes with derived extension of scalars along `f`:
> `RΓ_T(K) ⊗ᴸ_A B ≅ RΓ_{T'}(K ⊗ᴸ_A B)`, naturally in `K ∈ D⁺(A)` and compatibly with the
> augmentations to the identity. No hypothesis on the Krull dimensions is needed.

```lean
def derivedSectionsWithSupportInPlusBaseChangeIso (f : A →+* B) (hf : f.Flat)
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T) :
    { e : derivedSectionsWithSupportInPlus.{u, max uB v} A T ⋙ DerivedCategory.Plus.ι ⋙
          (derivedExtensionScalarsGeneral.{u, v, uB} f).functor ≅
        DerivedCategory.Plus.ι ⋙ (derivedExtensionScalarsGeneral.{u, v, uB} f).functor ⋙
          derivedSectionsWithSupportIn.{uB, max u v} B ((PrimeSpectrum.comap f) ⁻¹' T) //
      ∀ K : DerivedCategory.Plus (ModuleCat.{max u uB v} A),
        e.hom.app K ≫
            (derivedSectionsWithSupportInAugmentation.{uB, max u v} B
              ((PrimeSpectrum.comap f) ⁻¹' T)).app
              ((derivedExtensionScalarsGeneral.{u, v, uB} f).functor.obj
                (DerivedCategory.Plus.ι.obj K)) =
          (derivedExtensionScalarsGeneral.{u, v, uB} f).functor.map
            (DerivedCategory.Plus.ι.map
              ((derivedSectionsWithSupportInPlusAugmentation.{u, max uB v} A T).app K)) }
```

**`Stacks.LocalCohomology.derivedSectionsWithSupportInBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/BaseChangeGeneralSupport/BaseChangeIso.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/BaseChangeGeneralSupport/BaseChangeIso.lean#L432). The attribute's comment: “unbounded case”. References: EGA IV (5.9.4), “affine, finite dim”.

> **Stacks Project, Tag 0EF5, the unbounded case.** Let `f : A →+* B` be a flat homomorphism
> of Noetherian rings of finite Krull dimension, let `T ⊆ Spec A` be stable under specialization
> and put `T' = (Spec f)⁻¹(T)`. Then local cohomology with support in `T` of an arbitrary complex
> commutes with derived extension of scalars along `f`:
> `RΓ_T(K) ⊗ᴸ_A B ≅ RΓ_{T'}(K ⊗ᴸ_A B)`, naturally in `K ∈ D(A)` and compatibly with the
> augmentations to the identity.

```lean
def derivedSectionsWithSupportInBaseChangeIso (f : A →+* B) (hf : f.Flat)
    (T : Set (PrimeSpectrum A)) (hT : StableUnderSpecialization T)
    (_hA : ringKrullDim A < ⊤) (_hB : ringKrullDim B < ⊤) :
    { e : derivedSectionsWithSupportIn.{u, max uB v} A T ⋙
          (derivedExtensionScalarsGeneral.{u, v, uB} f).functor ≅
        (derivedExtensionScalarsGeneral.{u, v, uB} f).functor ⋙
          derivedSectionsWithSupportIn.{uB, max u v} B ((PrimeSpectrum.comap f) ⁻¹' T) //
      ∀ K : DerivedCategory (ModuleCat.{max u uB v} A),
        e.hom.app K ≫
            (derivedSectionsWithSupportInAugmentation.{uB, max u v} B
              ((PrimeSpectrum.comap f) ⁻¹' T)).app
              ((derivedExtensionScalarsGeneral.{u, v, uB} f).functor.obj K) =
          (derivedExtensionScalarsGeneral.{u, v, uB} f).functor.map
            ((derivedSectionsWithSupportInAugmentation.{u, max uB v} A T).app K) }
```

## Tag 0EF6, a lemma

[Tag 0EF6](https://stacks.math.columbia.edu/tag/0EF6) in the Stacks Project.

**`Stacks.LocalCohomology.exists_localCohomologySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/SpectralSequence.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/SpectralSequence.lean#L156).

> **Stacks 0EF6.** The Grothendieck spectral sequence for local cohomology with two
> supports: for specialization-closed subsets `T` and `T'` of the spectrum of a Noetherian
> ring and a bounded-below derived object `X`, there is a spectral sequence with second page
> `H^p_T(H^q_{T'}(X))` converging to `H^{p+q}_{T ∩ T'}(X)`.
>
> Two points where this departs from the printed form of the tag. Its hypothesis reads
> "let `A` be a ring", but `H^0_T` is introduced in that section only for a Noetherian ring,
> every other statement of the section carries the hypothesis, and the tag's own proof invokes
> the adjointness of `RΓ_T`, established only over a Noetherian ring (Tags 0EF2, 0EF3, 0EF4).
> Noetherianity is what the proof below needs too: it is Baer's criterion that makes sections
> with support in `T` of an injective module injective, and that is the acyclicity input of
> Tag 015N. Second, the displayed second page of the tag is `H^p_T(H^p_{T'}(K))`, where the
> inner `p` is a slip — its own abutment `H^{p + q}` exhibits two independent indices — and the
> Grothendieck form `H^q_{T'}` is the one proved here.

```lean
theorem exists_localCohomologySpectralSequence
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (T T' : Set (PrimeSpectrum A))
    (_hT : StableUnderSpecialization T) (_hT' : StableUnderSpecialization T')
    (X : DerivedCategory.Plus (ModuleCat.{max u v} A)) :
    ∃ K : FilteredObject (CochainComplex (ModuleCat.{max u v} A) ℤ) ℤᵒᵖ,
      (∀ n : ℤ, Nonempty (K.X.homology n ≅
        localCohomologyWithSupportInPlus A (T ∩ T') X n)) ∧
      ∀ (Fil : ∀ (_p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ p n : ℤ, Fil p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
        (Z : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, Z r p n =
          Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)))
        (D : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
          (Subobject.«exists» (K.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
        (FH : ∀ (n _p : ℤ), Subobject (K.X.homology n))
        (_ : ∀ n p : ℤ, FH n p =
          imageSubobject (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n)),
      ∃ (E : CohomologicalSpectralSequence (ModuleCat.{max u v} A) 0)
        (_ : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))),
        (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
          localCohomologyWithSupportInPlus A T
            ((DerivedCategory.Plus.singleFunctor (ModuleCat.{max u v} A) 0).obj
              (localCohomologyWithSupportInPlus A T' X q)) p)) ∧
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0).X (p, n - p))}.Finite) ∧
        (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
        (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
          (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
        (∀ p n : ℤ,
          IsGLB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)) ⊔
                Fil (p + 1) n)
            (kernelSubobject (K.X.d n (n + 1)) ⊓ Fil p n ⊔ Fil (p + 1) n) ∧
          IsLUB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (Fil (p - r) (n - 1)) ⊔
                Fil (p + 1) n)
            (imageSubobject (K.X.d (n - 1) n) ⊓ Fil p n ⊔ Fil (p + 1) n))
```

## Tag 0EF7, a lemma

[Tag 0EF7](https://stacks.math.columbia.edu/tag/0EF7) in the Stacks Project.

**`Stacks.LocalCohomology.derivedCategoryB_tensor_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean#L750). The attribute's comment: “support, left factor”.

> **Stacks 0EF7.** Over a Noetherian ring of finite dimension, the derived tensor product of
> an object of `D_T(A)` with an arbitrary object of `D(A)` again lies in `D_T(A)`.

```lean
theorem derivedCategoryB_tensor_left (hT : StableUnderSpecialization T)
    (hdim : ringKrullDim A < ⊤) (K L : DerivedCategory (ModuleCat.{u} A))
    (hK : DerivedCategoryB.derivedCategoryB
      (supportModuleProperty A T : ObjectProperty (ModuleCat.{u} A)) K) :
    DerivedCategoryB.derivedCategoryB
      (supportModuleProperty A T : ObjectProperty (ModuleCat.{u} A))
      ((CechFormula.derivedTensorProductBifunctor A).obj (K, L))
```

**`Stacks.LocalCohomology.derivedCategoryB_tensor_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean#L764). The attribute's comment: “support, right factor”.

> **Stacks 0EF7.** Over a Noetherian ring of finite dimension, the derived tensor product of
> an arbitrary object of `D(A)` with an object of `D_T(A)` again lies in `D_T(A)`.

```lean
theorem derivedCategoryB_tensor_right (hT : StableUnderSpecialization T)
    (hdim : ringKrullDim A < ⊤) (K L : DerivedCategory (ModuleCat.{u} A))
    (hL : DerivedCategoryB.derivedCategoryB
      (supportModuleProperty A T : ObjectProperty (ModuleCat.{u} A)) L) :
    DerivedCategoryB.derivedCategoryB
      (supportModuleProperty A T : ObjectProperty (ModuleCat.{u} A))
      ((CechFormula.derivedTensorProductBifunctor A).obj (K, L))
```

**`Stacks.LocalCohomology.exists_derivedSectionsWithSupportIn_tensorIso_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean, line 781](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean#L781). The attribute's comment: “tensor formula, left factor”.

> **Stacks 0EF7.** Local cohomology with support in `T` of a derived tensor product is the
> derived tensor product with local cohomology taken in the left factor, by an isomorphism of
> bifunctors carrying the augmentation of the tensor product to the augmentation of the left
> factor tensored with the identity.

```lean
theorem exists_derivedSectionsWithSupportIn_tensorIso_left
    (hT : StableUnderSpecialization T) (hdim : ringKrullDim A < ⊤) :
    ∃ e : CechFormula.derivedTensorProductBifunctor A ⋙
          derivedSectionsWithSupportIn.{u, u} A T ≅
        Functor.prod (derivedSectionsWithSupportIn.{u, u} A T) (𝟭 _) ⋙
          CechFormula.derivedTensorProductBifunctor A,
      ∀ K L : DerivedCategory (ModuleCat.{u} A),
        e.hom.app (K, L) ≫ (CechFormula.derivedTensorProductBifunctor A).map
            (((derivedSectionsWithSupportInAugmentation.{u, u} A T).app K, 𝟙 L) :
              ((derivedSectionsWithSupportIn.{u, u} A T).obj K, L) ⟶ (K, L)) =
          (derivedSectionsWithSupportInAugmentation.{u, u} A T).app
            ((CechFormula.derivedTensorProductBifunctor A).obj (K, L))
```

**`Stacks.LocalCohomology.exists_derivedSectionsWithSupportIn_tensorIso_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean, line 807](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean#L807). The attribute's comment: “tensor formula, right factor”.

> **Stacks 0EF7.** Local cohomology with support in `T` of a derived tensor product is the
> derived tensor product with local cohomology taken in the right factor, by an isomorphism of
> bifunctors carrying the augmentation of the tensor product to the identity tensored with the
> augmentation of the right factor.

```lean
theorem exists_derivedSectionsWithSupportIn_tensorIso_right
    (hT : StableUnderSpecialization T) (hdim : ringKrullDim A < ⊤) :
    ∃ e : CechFormula.derivedTensorProductBifunctor A ⋙
          derivedSectionsWithSupportIn.{u, u} A T ≅
        Functor.prod (𝟭 _) (derivedSectionsWithSupportIn.{u, u} A T) ⋙
          CechFormula.derivedTensorProductBifunctor A,
      ∀ K L : DerivedCategory (ModuleCat.{u} A),
        e.hom.app (K, L) ≫ (CechFormula.derivedTensorProductBifunctor A).map
            ((𝟙 K, (derivedSectionsWithSupportInAugmentation.{u, u} A T).app L) :
              (K, (derivedSectionsWithSupportIn.{u, u} A T).obj L) ⟶ (K, L)) =
          (derivedSectionsWithSupportInAugmentation.{u, u} A T).app
            ((CechFormula.derivedTensorProductBifunctor A).obj (K, L))
```

**`Stacks.LocalCohomology.exists_derivedSectionsWithSupportIn_tensorIso_both`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean, line 831](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean#L831). The attribute's comment: “tensor formula, both factors”.

> **Stacks 0EF7.** Applying local cohomology with support in `T` in both tensor factors agrees
> with applying it to the tensor product, again compatibly with the augmentations.

```lean
theorem exists_derivedSectionsWithSupportIn_tensorIso_both
    (hT : StableUnderSpecialization T) (hdim : ringKrullDim A < ⊤) :
    ∃ e : CechFormula.derivedTensorProductBifunctor A ⋙
          derivedSectionsWithSupportIn.{u, u} A T ≅
        Functor.prod (derivedSectionsWithSupportIn.{u, u} A T)
          (derivedSectionsWithSupportIn.{u, u} A T) ⋙
          CechFormula.derivedTensorProductBifunctor A,
      ∀ K L : DerivedCategory (ModuleCat.{u} A),
        e.hom.app (K, L) ≫ (CechFormula.derivedTensorProductBifunctor A).map
            (((derivedSectionsWithSupportInAugmentation.{u, u} A T).app K,
                (derivedSectionsWithSupportInAugmentation.{u, u} A T).app L) :
              ((derivedSectionsWithSupportIn.{u, u} A T).obj K,
                (derivedSectionsWithSupportIn.{u, u} A T).obj L) ⟶ (K, L)) =
          (derivedSectionsWithSupportInAugmentation.{u, u} A T).app
            ((CechFormula.derivedTensorProductBifunctor A).obj (K, L))
```

**`Stacks.LocalCohomology.exists_derivedSectionsWithSupportIn_isoTensorUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean, line 921](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/Sweep/TensorFormula.lean#L921). The attribute's comment: “tensor formula”.

> **Stacks 0EF7.** Local cohomology with support in `T` is the derived tensor product with the
> local cohomology of the ring, by an isomorphism whose inverse is the canonical map
> `RΓ_T(A) ⊗^L_A K ⟶ A ⊗^L_A K ⟶ K`.

```lean
theorem exists_derivedSectionsWithSupportIn_isoTensorUnit
    (hT : StableUnderSpecialization T) (hdim : ringKrullDim A < ⊤) :
    ∃ e : derivedSectionsWithSupportIn.{u, u} A T ≅
        (canonicalDerivedTensorProductFunctor A).obj
          ((derivedSectionsWithSupportIn.{u, u} A T).obj (CechFormula.unitObject A)),
      ∀ K : DerivedCategory (ModuleCat.{u} A),
        e.hom.app K ≫
            (((canonicalDerivedTensorProductFunctor A).map
                ((derivedSectionsWithSupportInAugmentation.{u, u} A T).app
                  (CechFormula.unitObject A))).app K ≫
              (CechFormula.derivedTensorLeftUnitor A).hom.app K) =
          (derivedSectionsWithSupportInAugmentation.{u, u} A T).app K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.5, Tag 0EEY](https://stacks.math.columbia.edu/tag/0EEY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
