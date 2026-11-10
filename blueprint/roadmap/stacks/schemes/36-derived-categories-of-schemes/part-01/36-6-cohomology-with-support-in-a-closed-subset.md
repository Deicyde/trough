---
declaration: section
origin: cited
lean: AlgebraicGeometry.CohomologySupportedOn, Stacks.Perfect.SupportedQuasicoherent.quasiCoherentSupported_derivedSupportedPushforward, Stacks.Perfect.SupportedQuasicoherent.quasiCoherentSupportedInclusionAdj, Stacks.Cohomology.SupportedComplexes.preservesColimitsOfShape_discrete_derivedSupportedSectionsOnClosed, AlgebraicGeometry.ExtendedAlternatingCech.equationsClosedSubscheme, AlgebraicGeometry.ExtendedAlternatingCech.equationsOpen, AlgebraicGeometry.ExtendedAlternatingCech.restrictedModule, AlgebraicGeometry.ExtendedAlternatingCech.functor
statement: formalized
proof: formalized
---

# 36.6 Cohomology with support in a closed subset

Section 36.6 of the Stacks Project, [Tag 0G7F](https://stacks.math.columbia.edu/tag/0G7F). 14 tags here are carried by 71 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08DA, a definition

[Tag 08DA](https://stacks.math.columbia.edu/tag/08DA) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.CohomologySupportedOn`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportedCohomology.lean#L50), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Perfect/SupportedCohomology.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportedCohomology.lean#L59) (StacksFrontier).

## Tag 0G7G, a lemma

[Tag 0G7G](https://stacks.math.columbia.edu/tag/0G7G) in the Stacks Project.

**`Stacks.Perfect.SupportedQuasicoherent.quasiCoherentSupported_derivedSupportedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/QuasicoherentSupportedComplexes.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/QuasicoherentSupportedComplexes.lean#L508). The attribute's comment: “part (1)”.

> **Stacks 0G7G (1).** Let `X` be a scheme, let `T ⊆ X` be a closed subset whose open
> complement `X ∖ T` is retrocompact, and let `i : T → X` be the inclusion. For `E` in
> `D_QCoh(𝒪_X)` the complex `i_* R𝓗_T(E)` lies in `D_{QCoh, T}(𝒪_X)`: its cohomology sheaves
> are quasi-coherent and supported on `T`.

```lean
theorem quasiCoherentSupported_derivedSupportedPushforward (hTc : IsRetrocompact Tᶜ)
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing X.toRingedSpace)))
    (hE : DerivedCategoryB.derivedCategoryB (SheafOfModules.isQuasicoherent X.ringCatSheaf) E) :
    Stacks.Duality.quasiCoherentSupported X T
      ((derivedSupportedPushforward X.toRingedSpace T hT).obj E)
```

**`Stacks.Perfect.SupportedQuasicoherent.quasiCoherentSupportedInclusionAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/QuasicoherentSupportedComplexes.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/QuasicoherentSupportedComplexes.lean#L571). The attribute's comment: “part (2)”.

> **Stacks 0G7G (2).** Let `X` be a scheme, let `T ⊆ X` be a closed subset whose open
> complement is retrocompact, and let `i : T → X` be the inclusion. The functor
> `i_* ∘ R𝓗_T : D_QCoh(𝒪_X) ⥤ D_{QCoh,T}(𝒪_X)` is right adjoint to the inclusion functor
> `D_{QCoh,T}(𝒪_X) ⥤ D_QCoh(𝒪_X)`.
>
> The adjunction is the restriction of the ambient adjunction `i_* ⊣ R𝓗_T` of Stacks 0A3B along
> the two fully faithful inclusions: on the left `R𝓗_T` identifies `D_{QCoh,T}(𝒪_X)` with a full
> subcategory of `D(𝒪_X|_T)`, because the counit `i_* R𝓗_T(A) ⟶ A` is invertible there, and on
> the right `D_QCoh(𝒪_X)` is a full subcategory of `D(𝒪_X)`.

```lean
def quasiCoherentSupportedInclusionAdj (hTc : IsRetrocompact Tᶜ) :
    quasiCoherentSupportedInclusion X T ⊣ quasiCoherentDerivedSupport X T hT hTc
```

## Tag 0G7H, a lemma

[Tag 0G7H](https://stacks.math.columbia.edu/tag/0G7H) in the Stacks Project.

**`Stacks.Cohomology.SupportedComplexes.preservesColimitsOfShape_discrete_derivedSupportedSectionsOnClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDirectSums.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsDirectSums.lean#L317). The attribute's comment: “for families indexed by a type of the scheme universe, the only index universe at which `D_QCoh(𝒪_X)` has direct sums”.

> Let `X` be a scheme and let `T ⊆ X` be a closed subset such that `X ∖ T` is a retrocompact
> open of `X`.  Then for a family `Eᵢ`, `i ∈ I`, of objects of `D_QCoh(𝒪_X)` we have
> `R𝓗_T(⊕ Eᵢ) = ⊕ R𝓗_T(Eᵢ)`: the derived functor `R𝓗_T` of sections supported on `T`, restricted
> to `D_QCoh(𝒪_X)`, preserves `I`-indexed direct sums.

```lean
theorem preservesColimitsOfShape_discrete_derivedSupportedSectionsOnClosed
    (hTc : IsRetrocompact (Tᶜ : Set X)) :
    PreservesColimitsOfShape (Discrete I)
      ((quasicoherentDerivedProperty X).ι ⋙
        derivedSupportedSectionsOnClosed X.toRingedSpace T hT)
```

## Tag 0G7I, a remark

[Tag 0G7I](https://stacks.math.columbia.edu/tag/0G7I) in the Stacks Project.

**`AlgebraicGeometry.ExtendedAlternatingCech.equationsClosedSubscheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean#L89). The attribute's comment: “closed subscheme cut out by the equations”.

> The closed subscheme cut out by the given equations.

```lean
public def equationsClosedSubscheme : Scheme.{u}
```

**`AlgebraicGeometry.ExtendedAlternatingCech.equationsOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean#L94). The attribute's comment: “principal-open intersections”.

> The intersection of the principal opens belonging to an increasing tuple.

```lean
public def equationsOpen (p : ℕ) (s : CechCochains.OrdIndex (I := Fin c) p) : X.Opens
```

**`AlgebraicGeometry.ExtendedAlternatingCech.restrictedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean#L99). The attribute's comment: “direct images of restrictions”.

> The direct image to `X` of a module restricted to a principal intersection.

```lean
public def restrictedModule (F : X.Modules) (p : ℕ)
    (s : CechCochains.OrdIndex (I := Fin c) p) : X.Modules
```

**`AlgebraicGeometry.ExtendedAlternatingCech.functor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean, line 999](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCech.lean#L999). The attribute's comment: “extended alternating Čech complex and signed differentials”.

> **Stacks Project, Tag 0G7I.** The extended alternating Čech complex of a
> module with respect to finitely many global equations, including its canonical
> augmentation, signed restriction differentials, and functoriality.

```lean
public def functor : FunctorData f
```

**`Stacks.Perfect.CechComparison.complexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCechComparison.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCechComparison.lean#L181). The attribute's comment: “the complex is determined by the data specifying it”.

> **Stacks Project, Tag 0G7I.** The two constructions of the extended alternating Čech complex
> of a family of global equations and a coefficient module are isomorphic: in degree `0` by the two
> identifications with the coefficient module, and in degree `p + 1` by the two identifications
> with the product of the direct images of its restrictions to the principal intersections.

```lean
def complexIso : (data f F).complex ≅ (extendedAlternatingCech f F).complex
```

**`Stacks.Perfect.ExtendedAlternatingCech.equationsClosedSubscheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean#L75). The attribute's comment: “closed subscheme cut out by the equations”.

> The closed subscheme cut out by the given equations.

```lean
public def equationsClosedSubscheme : Scheme.{u}
```

**`Stacks.Perfect.ExtendedAlternatingCech.equationsOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean#L80). The attribute's comment: “principal-open intersections”.

> The intersection of the principal opens belonging to an increasing tuple.

```lean
public def equationsOpen (p : ℕ) (s : CechCochains.OrdIndex (I := Fin c) p) : X.Opens
```

**`Stacks.Perfect.ExtendedAlternatingCech.restrictedModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean#L85). The attribute's comment: “direct images of restrictions”.

> The direct image to `X` of a module restricted to a principal intersection.

```lean
public def restrictedModule (F : X.Modules) (p : ℕ)
    (s : CechCochains.OrdIndex (I := Fin c) p) : X.Modules
```

**`Stacks.Perfect.ExtendedAlternatingCech.extendedAlternatingCechFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean, line 870](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/GlobalEquationsComplexData.lean#L870). The attribute's comment: “extended alternating Čech complex and signed differentials”.

> **Stacks Project, Tag 0G7I.** The extended alternating Čech complex of a
> module with respect to finitely many global equations, including its canonical
> augmentation, signed restriction differentials, and functoriality.

```lean
public def extendedAlternatingCechFunctor :
    ExtendedAlternatingCechFunctorData f
```

## Tag 0G7K, a lemma

[Tag 0G7K](https://stacks.math.columbia.edu/tag/0G7K) in the Stacks Project.

**`AlgebraicGeometry.ExtendedAlternatingCech.acyclic_on_equationsComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/Acyclicity.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/Acyclicity.lean#L243).

> The extended alternating Čech complex is acyclic off the common zero locus
> of the global equations.

```lean
public theorem acyclic_on_equationsComplement
    {X : Scheme.{u}} {c : ℕ} (f : Fin c → Γ(X, ⊤)) (F : X.Modules) :
    (((Scheme.Modules.pullback (⨆ i, X.basicOpen (f i)).ι).mapHomologicalComplex
      (ComplexShape.up ℕ)).obj (data f F).complex).Acyclic
```

**`Stacks.Perfect.CechLocalCohomology.cohomologySupportedOn_extendedAlternatingCech`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechLocalCohomology.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechLocalCohomology.lean#L162). The attribute's comment: “the cohomology sheaves are supported on the common zero locus”.

> **Stacks Project, Tag 0G7K**, as a support statement.  The cohomology sheaves of the
> extended alternating Čech complex of the equations `f₁, …, f_c` are supported on their common
> zero locus: the complex is acyclic on the complement, which is the union of the principal opens
> of the equations.
>
> This is the hypothesis under which [Stacks, Tag 0AEF] part (2) applies to the complex.

```lean
theorem cohomologySupportedOn_extendedAlternatingCech :
    AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X.toRingedSpace)
      (equationsClosedSet f)
      (DerivedCategory.Q.obj ((data f F).complex.extend ComplexShape.embeddingUpNat))
```

**`Stacks.Cech.extendedCechComplex_acyclic_restrict_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Cech/ExtendedAlternatingRingedSpace.lean, line 775](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Cech/ExtendedAlternatingRingedSpace.lean#L775).

> **Stacks 0G7K for an arbitrary ringed space.** Let `Y` be a ringed space, let
> `g 0, …, g (c-1)` be global sections of its structure sheaf, let `Z` be their common zero
> locus and let `F` be a sheaf of `𝒪_Y`-modules. Then the extended alternating Čech complex of
> `F` for the opens `Y.basicOpen (g i)` restricts to an acyclic complex over `Y ∖ Z`, which is
> the open `⨆ i, Y.basicOpen (g i)` by `Stacks.Cech.coe_iSup_basicOpen`.
>
> The proof is `Stacks.Cech.sectionComplex_acyclic`: over an open contained in one of the
> `Y.basicOpen (g i)` the complex of sections is the extended ordered Čech complex of a covering
> one of whose members is the whole open, hence is contractible by Stacks 0G6T; exactness of a
> complex of sheaves of modules is checked on stalks, and every point of `Y ∖ Z` has arbitrarily
> small neighbourhoods inside some `Y.basicOpen (g i)`.

```lean
theorem extendedCechComplex_acyclic_restrict_basicOpen
    (F : OXMod.{u, u} Y) :
    (((restrictModules.{u, u, u} Y (⨆ i, Y.basicOpen (g i))).mapHomologicalComplex
      (ComplexShape.up ℕ)).obj
      (extendedCechComplex (fun i => Y.basicOpen (g i)) F)).Acyclic
```

## Tag 0G7L, a remark

[Tag 0G7L](https://stacks.math.columbia.edu/tag/0G7L) in the Stacks Project.

**`AlgebraicGeometry.ExtendedAlternatingCech.augmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/Augmentation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/Augmentation.lean#L59). The attribute's comment: “augmentation”.

> The canonical map from the extended alternating Čech complex to its
> degree-zero module, in the unbounded derived category.

```lean
public def augmentation (F : X.Modules) :
    DerivedCategory.Q.obj
        ((data f F).complex.extend ComplexShape.embeddingUpNat) ⟶
      (DerivedCategory.singleFunctor X.Modules 0).obj F
```

**`AlgebraicGeometry.ExtendedAlternatingCech.augmentation_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/Augmentation.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/Augmentation.lean#L70). The attribute's comment: “augmentation”.

> The canonical augmentation is natural in the coefficient module.

```lean
public theorem augmentation_natural {F G : X.Modules} (φ : F ⟶ G) :
    DerivedCategory.Q.map
        (HomologicalComplex.extendMap ((functor f).map φ)
          ComplexShape.embeddingUpNat) ≫
      augmentation f G =
      augmentation f F ≫ (DerivedCategory.singleFunctor X.Modules 0).map φ
```

**`Stacks.Perfect.ExtendedAlternatingCech.Augmentation.augmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AugmentationDerivedMap.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AugmentationDerivedMap.lean#L97). The attribute's comment: “augmentation”.

> **Stacks Project, Tag 0G7L.** The canonical map from the extended alternating Čech complex
> to its coefficient module placed in degree `0`, in the unbounded derived category.

```lean
public def augmentation (F : X.Modules) :
    DerivedCategory.Q.obj
        ((extendedAlternatingCech f F).complex.extend ComplexShape.embeddingUpNat) ⟶
      (DerivedCategory.singleFunctor X.Modules 0).obj F
```

**`Stacks.Perfect.ExtendedAlternatingCech.Augmentation.augmentation_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AugmentationDerivedMap.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AugmentationDerivedMap.lean#L108). The attribute's comment: “augmentation”.

> **Stacks Project, Tag 0G7L.** The canonical augmentation is natural in the coefficient
> module.

```lean
public theorem augmentation_natural {F G : X.Modules} (φ : F ⟶ G) :
    DerivedCategory.Q.map
        (HomologicalComplex.extendMap ((extendedAlternatingCechFunctor f).map φ)
          ComplexShape.embeddingUpNat) ≫
      augmentation f G =
    augmentation f F ≫ (DerivedCategory.singleFunctor X.Modules 0).map φ
```

**`Stacks.Perfect.SupportedFraction.cohomologySupportedOn_cech`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean#L319). The attribute's comment: “the first assertion of the remark: the cohomology sheaves of 𝓕^• are supported on the common zero locus, hence 𝓕^• is an object of D\_Z(𝒪\_X). Deduced from Stacks 0G7K, stated at the derived-category spelling the remark's diagram uses, for an arbitrary 𝒪\_X-module ℱ”.

> **The extended alternating Čech complex is supported on the common zero locus.** Every
> cohomology sheaf of `𝓕^•` has vanishing stalks outside the common zero locus of the equations,
> because `𝓕^•` restricted to the union of the principal opens is acyclic (Stacks 0G7K).
>
> This is the first assertion of Remark 0G7L, `𝓕^• ∈ D_Z(𝒪_X)`: `CohomologySupportedOn` is the
> property cutting out `D_Z(𝒪_X)` inside `D(𝒪_X)`, so membership in the supported derived category
> *is* this statement, and it is what makes the adjunction of Stacks 0AEF applicable to `𝓕^•` in
> the rest of the remark.  The remark deduces it from Stacks 0G7K, whose own carrier is
> `cohomologySupportedOn_extendedAlternatingCech`; what is registered here is the deduction, at
> the derived-category spelling that the remark's diagram and the comparison
> `cechToDerivedSupport` below are stated at.  No hypothesis beyond the remark's is carried: `ℱ`
> is an arbitrary `𝒪_X`-module and the equations are arbitrary.

```lean
public theorem cohomologySupportedOn_cech :
    AlgebraicGeometry.CohomologySupportedOn (structureSheafRing X.toRingedSpace)
      (equationsClosedSet e)
      (DerivedCategory.Q.obj ((cplx e F).extend ComplexShape.embeddingUpNat))
```

**`Stacks.Perfect.SupportedFraction.cechToDerivedSupport`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean#L400). The attribute's comment: “the canonical comparison 𝓕^• ⟶ i\_*RℋT(ℱ), built from the counit of Stacks 0G72 and the augmentation, for an arbitrary 𝒪\_X-module ℱ”.

> **The canonical comparison of Stacks 0G7L**, `𝓕^• ⟶ i_* R𝓗_T(ℱ)`.
>
> It is the inverse of the counit `i_* R𝓗_T(𝓕^•) ⟶ 𝓕^•`, invertible by
> `isIso_derivedSupportedSectionsToId_cech`, followed by `i_* R𝓗_T` applied to the augmentation
> `𝓕^• ⟶ ℱ[0]` of Stacks 0G7L.  This is the map whose degree-`c` cohomology sheaf Stacks 0G7Q
> uses to define `c_{f₁,…,f_c}`.
>
> As in the source, `ℱ` is an arbitrary `𝒪_X`-module: the counit is invertible at `𝓕^•` because
> `𝓕^•` is supported on the common zero locus of the equations, which is Stacks 0G7K and holds
> for every `ℱ`.  Quasi-coherence enters only later, in Stacks 0G7M, where the *other* leg of the
> triangle — `i_* R𝓗_T` applied to the augmentation — is shown to be invertible.

```lean
public def cechToDerivedSupport (hTe : equationsClosedSet e ⊆ T) :
    DerivedCategory.Q.obj ((cplx e F).extend ComplexShape.embeddingUpNat) ⟶
      (supportPush hT).obj ((DerivedCategory.singleFunctor X.Modules 0).obj F)
```

**`Stacks.Perfect.SupportedFraction.cechToDerivedSupport_comp_derivedSupportedSectionsToId`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean#L433). The attribute's comment: “the commuting triangle 𝓕^• ⟶ ℱ, 𝓕^• ⟶ i\_*RℋT(ℱ), i\_*RℋT(ℱ) ⟶ ℱ of the remark's diagram, for an arbitrary 𝒪\_X-module ℱ”.

> **The commuting triangle of Stacks 0G7L**, in the shape the remark displays:
>
> `𝓕^• ⟶ ℱ`, `𝓕^• ⟶ i_* R𝓗_T(ℱ)` and `i_* R𝓗_T(ℱ) ⟶ ℱ`
>
> commute, the third edge being the counit of Stacks 0G72 at `ℱ[0]`.  So the canonical map
> `𝓕^• ⟶ ℱ` of the remark — the augmentation, coming from the equality `𝓕^0 = ℱ` — factors
> through `i_* R𝓗_T(ℱ)`, which is what the adjunction of Stacks 0A3B provides and what the remark
> asserts.

```lean
public theorem cechToDerivedSupport_comp_derivedSupportedSectionsToId
    (hTe : equationsClosedSet e ⊆ T) :
    cechToDerivedSupport e F hT hTe ≫
        (supportPushCounit hT).app ((DerivedCategory.singleFunctor X.Modules 0).obj F) =
      augmentation e F
```

**`Stacks.Perfect.CechComparison.augmentation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCechComparison.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCechComparison.lean#L238). The attribute's comment: “the augmentations of the two constructions agree”.

> **Stacks Project, Tag 0G7L.** The augmentations of the two constructions of the extended
> alternating Čech complex correspond under the comparison isomorphism.

```lean
theorem augmentation_eq :
    AlgebraicGeometry.ExtendedAlternatingCech.augmentation f F =
      DerivedCategory.Q.map (extendBridge f F).hom ≫
        Stacks.Perfect.ExtendedAlternatingCech.Augmentation.augmentation f F
```

**`Stacks.Perfect.SupportedFraction.derivedSupportedSectionsToId_single_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionNaturality.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionNaturality.lean#L154). The attribute's comment: “functoriality in the 𝒪\_X-module ℱ, the edge i\_*RℋT(ℱ) ⟶ ℱ of the diagram”.

> **The edge `i_* R𝓗_T(ℱ) ⟶ ℱ` of the diagram of Stacks 0G7L is natural in the coefficient
> module.**  It is the counit of Stacks 0G72 evaluated at `ℱ[0]`, hence a component of a natural
> transformation, so its naturality square is `NatTrans.naturality`; it is stated here because the
> remark asserts its diagram functorial in `ℱ`, and that assertion is the naturality of all three
> edges.

```lean
public theorem derivedSupportedSectionsToId_single_naturality {T : Set X} (hT : IsClosed T)
    {F G : X.Modules} (φ : F ⟶ G) :
    (supportPush hT).map ((DerivedCategory.singleFunctor X.Modules 0).map φ) ≫
        (supportPushCounit hT).app ((DerivedCategory.singleFunctor X.Modules 0).obj G) =
      (supportPushCounit hT).app ((DerivedCategory.singleFunctor X.Modules 0).obj F) ≫
        (DerivedCategory.singleFunctor X.Modules 0).map φ
```

**`Stacks.Perfect.SupportedFraction.Q_map_extendMap_cplxMap_comp_cechToDerivedSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionNaturality.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionNaturality.lean#L175). The attribute's comment: “functoriality in the 𝒪\_X-module ℱ, the edge 𝓕^• ⟶ i\_*RℋT(ℱ) of the diagram”.

> **The canonical comparison `𝓕^• ⟶ i_* R𝓗_T(ℱ)` of Stacks 0G7L is natural in the coefficient
> module.**  Both sides become, after the invertible counit of Stacks 0G72, the functor
> `i_* R𝓗_T` applied to a naturality square for the augmentation.
>
> This is the second of the three edges of the remark's diagram; with
> `Q_map_extendMap_cplxMap_comp_augmentation` for the edge `𝓕^• ⟶ ℱ` and
> `derivedSupportedSectionsToId_single_naturality` for the edge `i_* R𝓗_T(ℱ) ⟶ ℱ` it is the
> remark's closing clause, that the diagram is "functorial in the `𝒪_X`-module `ℱ`".
>
> As in the source, `φ` is a morphism of arbitrary `𝒪_X`-modules: quasi-coherence is nowhere used,
> the counit being invertible at the extended alternating Čech complex of any module by
> Stacks 0G7K.

```lean
public theorem Q_map_extendMap_cplxMap_comp_cechToDerivedSupport {m : ℕ} (e : Fin m → Γ(X, ⊤))
    {F G : X.Modules} (φ : F ⟶ G) {T : Set X}
    (hT : IsClosed T) (hTe : equationsClosedSet e ⊆ T) :
    DerivedCategory.Q.map (HomologicalComplex.extendMap (cplxMap e φ)
          ComplexShape.embeddingUpNat) ≫ cechToDerivedSupport e G hT hTe =
      cechToDerivedSupport e F hT hTe ≫
        (supportPush hT).map ((DerivedCategory.singleFunctor X.Modules 0).map φ)
```

**`Stacks.Cohomology.SupportedComplexes.derivedSupportedSectionsLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean#L498). The attribute's comment: “the canonical factorisation through derived supported sections”.

> **The canonical factorization of Stacks 0G7L.** A map `i_* L ⟶ K` in `D(𝒪_X)` out of a
> complex pushed forward from `Z` has a canonical lift `L ⟶ RH_Z(K)`, its adjoint transpose under
> `derivedPushforwardAdjunction`. Pushing the lift forward and composing with the counit
> `i_* RH_Z(K) ⟶ K` returns the original map, by
> `modulePushforward_map_derivedSupportedSectionsLift_comp_counit`: this is the commutative
> triangle of Stacks 0G7L, for the chosen adjunction.

```lean
noncomputable def derivedSupportedSectionsLift
    {L : DerivedCategory (_root_.SheafOfModules.{u}
      (structureSheafRing (closedSubsetRingedSpace X Z)))}
    {K : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X))}
    (u : letI := pushforward_preservesFiniteLimits X Z
      letI := pushforward_preservesFiniteColimits X Z hZ
      (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.obj L ⟶ K) :
    L ⟶ (derivedSupportedSectionsOnClosed X Z hZ).obj K
```

**`Stacks.Cohomology.SupportedComplexes.modulePushforward_map_derivedSupportedSectionsLift_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/SupportedComplexes/SupportedSectionsCanonicalMaps.lean#L513). The attribute's comment: “the commuting triangle of the factorisation”.

> **The triangle of Stacks 0G7L commutes.** The canonical lift of `u : i_* L ⟶ K` through
> `i_* RH_Z(K)`, pushed forward and followed by the counit of the adjunction, is `u` again.

```lean
theorem modulePushforward_map_derivedSupportedSectionsLift_comp_counit
    {L : DerivedCategory (_root_.SheafOfModules.{u}
      (structureSheafRing (closedSubsetRingedSpace X Z)))}
    {K : DerivedCategory (_root_.SheafOfModules.{u} (structureSheafRing X))}
    (u : letI := pushforward_preservesFiniteLimits X Z
      letI := pushforward_preservesFiniteColimits X Z hZ
      (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.obj L ⟶ K) :
    letI := pushforward_preservesFiniteLimits X Z
    letI := pushforward_preservesFiniteColimits X Z hZ
    (modulePushforward (closedSubsetInclusion X Z)).mapDerivedCategory.map
          (derivedSupportedSectionsLift X Z hZ u) ≫
        (derivedPushforwardAdjunction X Z hZ).counit.app K = u
```

## Tag 0G7M, a lemma

[Tag 0G7M](https://stacks.math.columbia.edu/tag/0G7M) in the Stacks Project.

**`Stacks.Perfect.CechLocalCohomology.pushforwardLocalCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechLocalCohomology.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechLocalCohomology.lean#L196). The attribute's comment: “the complex computes the local cohomology sheaves”.

> **The extended alternating Čech complex computes the local cohomology sheaves.**  For a
> quasi-coherent `𝒪_X`-module `F` and the common zero locus `Z` of the equations, the direct image
> of the local cohomology sheaf `𝓗 ⁿ_Z(F)` along the inclusion of `Z` is the degree-`n` cohomology
> sheaf of the extended alternating Čech complex of `F`.
>
> In the top degree the right-hand side is the cokernel of the last Čech differential, the module
> in which the fraction class of [Stacks, Tag 0G7Q] takes its values.

```lean
def pushforwardLocalCohomologyIso [F.IsQuasicoherent] (n : ℕ) :
    letI := pushforward_preservesFiniteLimits X.toRingedSpace (equationsClosedSet f)
    letI := pushforward_preservesFiniteColimits X.toRingedSpace (equationsClosedSet f)
      (isClosed_equationsClosedSet f)
    (modulePushforward (closedSubsetInclusion X.toRingedSpace (equationsClosedSet f))).obj
        (localCohomologySheafOfComplex X.toRingedSpace (equationsClosedSet f)
          (isClosed_equationsClosedSet f) (n : ℤ)
          ((DerivedCategory.singleFunctor X.Modules 0).obj F)) ≅
      (data f F).complex.homology n
```

**`Stacks.Perfect.CechDerivedSupport.isIso_map_augmentation_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DerivedSupportInvertsAugmentation.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DerivedSupportInvertsAugmentation.lean#L357). The attribute's comment: “the derived sections with support invert the augmentation”.

> **Stacks Project, Tag 0G7M**, the step of the proof that uses the quasi-coherence of the
> coefficient module.  With `X`, `f₁, …, f_c ∈ Γ(X, 𝒪_X)` and `F` as in Stacks 0G7I, and `F`
> quasi-coherent, **a derived functor `R𝓗_Z` of sections supported on the common zero locus `Z` of
> the equations inverts the augmentation `𝓕^• ⟶ F[0]` of Stacks 0G7L**.
>
> The augmentation is the comparison between the extended alternating Čech complex and its
> coefficient module, so this says that the complex and the module have the same derived sections
> with support on `Z`.

```lean
public theorem isIso_map_augmentation_of_isQuasicoherent (F : X.Modules) [F.IsQuasicoherent]
    (RH : DerivedCategory X.Modules ⥤
      DerivedCategory (SheafOfModules.{u}
        (structureSheafRing (closedSubsetRingedSpace X.toRingedSpace (equationsClosedSet f)))))
    (αH : (schemeSupportedSectionsFunctor X (equationsClosedSet f)
        (isClosed_equationsClosedSet f)).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
      DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RH)
    (hRH : RH.IsRightDerivedFunctor αH
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))) :
    IsIso (RH.map (Stacks.Perfect.ExtendedAlternatingCech.Augmentation.augmentation f F))
```

**`Stacks.Perfect.CechDerivedSupport.nonempty_cechIso_derivedSupportedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DerivedSupportInvertsAugmentation.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DerivedSupportInvertsAugmentation.lean#L407). The attribute's comment: “the extended alternating Čech complex represents i\_*RℋZ(F)”.

> **Stacks Project, Tag 0G7M.**  With `X`, `f₁, …, f_c ∈ Γ(X, 𝒪_X)` and `F` as in Stacks 0G7I
> and `F` quasi-coherent, the extended alternating Čech complex `𝓕^•` **represents
> `i_* R𝓗_Z(F)`**, the comparison being the augmentation `𝓕^• ⟶ F[0]` of Stacks 0G7L.
>
> Two halves combine.  The augmentation is inverted by `R𝓗_Z`, which is
> `isIso_derivedSupportedSectionsOnClosed_map_augmentation` and is where quasi-coherence is used;
> and `𝓕^•` is its own derived sections with support, which is
> `Stacks.Perfect.CechSupportRepresentation.nonempty_pushforwardDerivedSupportCechIso` and is
> where the acyclicity of Stacks 0G7K is used.  The K-injective resolution entering the second
> half is not canonical, so the conclusion is stated as the existence of the isomorphism, in the
> form the neighbouring existence statements of Stacks 0A3B take.

```lean
public theorem nonempty_cechIso_derivedSupportedSections (F : X.Modules) [F.IsQuasicoherent] :
    letI := pushforward_preservesFiniteLimits X.toRingedSpace (equationsClosedSet f)
    letI := pushforward_preservesFiniteColimits X.toRingedSpace (equationsClosedSet f)
      (isClosed_equationsClosedSet f)
    Nonempty
      (DerivedCategory.Q.obj
          ((Stacks.Perfect.ExtendedAlternatingCech.extendedAlternatingCech f F).complex.extend
            ComplexShape.embeddingUpNat) ≅
        (modulePushforward (closedSubsetInclusion X.toRingedSpace
            (equationsClosedSet f))).mapDerivedCategory.obj
          ((derivedSupportedSectionsOnClosed X.toRingedSpace (equationsClosedSet f)
              (isClosed_equationsClosedSet f)).obj
            ((DerivedCategory.singleFunctor X.Modules 0).obj F)))
```

**`Stacks.Perfect.SupportedFraction.isIso_derivedSupportedSectionsToId_cech`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Subfamily.lean#L381). The attribute's comment: “the canonical counit i\_*RℋT(𝓕^•) ⟶ 𝓕^• of Stacks 0G72 is invertible at the extended alternating Čech complex, for every closed T containing the common zero locus of the equations. The theorem nonempty\_pushforwardDerivedSupportCechIso asserts the same isomorphism without naming it, because it is produced on a chosen K-injective resolution; here only invertibility of the canonical map is asserted, and invertibility is a proposition, so nothing is chosen”.

> **Stacks 0G7M, the acyclicity half, with the comparison as a canonical term.** The counit
> `i_* R𝓗_T(𝓕^•) ⟶ 𝓕^•` of Stacks 0G72 is invertible at the extended alternating Čech complex of
> a family of equations whose common zero locus is contained in `T`: the complex is supported
> there, so the third vertex `Rj_*(𝓕^•|_U)` of the triangle vanishes.
>
> This is the content of `nonempty_pushforwardDerivedSupportCechIso`, with the isomorphism being
> the canonical map rather than one produced on a chosen K-injective resolution; only the
> invertibility is asserted, and invertibility is a proposition, so nothing is chosen.

```lean
public theorem isIso_derivedSupportedSectionsToId_cech (hTe : equationsClosedSet e ⊆ T) :
    IsIso ((supportPushCounit hT).app
      (DerivedCategory.Q.obj ((cplx e F).extend ComplexShape.embeddingUpNat)))
```

**`Stacks.Perfect.CechComparison.isIso_derivedSupportedSectionsOnClosed_map_augmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCechComparison.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ExtendedAlternatingCechComparison.lean#L261). The attribute's comment: “the derived sections with support invert the augmentation”.

> **Stacks Project, Tag 0G7M.** With `X` a scheme, `f₁, …, f_c ∈ Γ(X, 𝒪_X)` global functions,
> `Z` their common zero locus and `F` a quasi-coherent `𝒪_X`-module, the chosen derived functor of
> sections supported on `Z` inverts the augmentation of
> `AlgebraicGeometry.ExtendedAlternatingCech.data`.
>
> This is `Stacks.Perfect.CechDerivedSupport.isIso_derivedSupportedSectionsOnClosed_map_augmentation`
> for the construction of the complex on which [Stacks, Tag 0G7K] and the well-definedness of the
> fraction class of [Stacks, Tag 0G7Q] are stated.

```lean
theorem isIso_derivedSupportedSectionsOnClosed_map_augmentation [F.IsQuasicoherent] :
    IsIso ((Stacks.Cohomology.SupportedComplexes.derivedSupportedSectionsOnClosed
      X.toRingedSpace (Stacks.Perfect.CechDerivedSupport.equationsClosedSet f)
      (Stacks.Perfect.CechDerivedSupport.isClosed_equationsClosedSet f)).map
        (AlgebraicGeometry.ExtendedAlternatingCech.augmentation f F))
```

## Tag 0G7N, a lemma

[Tag 0G7N](https://stacks.math.columbia.edu/tag/0G7N) in the Stacks Project.

**`Stacks.Perfect.LocalCohomologyDegrees.isZero_homology_derivedSupportedSections_of_locallyCutOut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/LocalCohomologyVanishingDegrees.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/LocalCohomologyVanishingDegrees.lean#L119). The attribute's comment: “stated for the closed subset T; the source writes ℋ^i\_Z for it, a slip”.

> **Stacks Project, Tag 0G7N.**  Let `X` be a scheme and let `T ⊆ X` be a closed subset which
> can locally be cut out by `c` elements of the structure sheaf.  Then the local cohomology sheaves
> of a quasi-coherent `𝒪_X`-module vanish above degree `c`:
>
> `ℋ ^i_T(ℱ) = 0` for `i > c`.
>
> The hypothesis is that every point has an open neighbourhood `U` on which the part of `T` lying
> in `U` is the common zero locus of `c` functions on `U`.

```lean
public theorem isZero_homology_derivedSupportedSections_of_locallyCutOut {X : Scheme.{u}}
    (T : Set X) (hT : IsClosed T) (c : ℕ)
    (hcut : ∀ x : X, ∃ U : X.Opens, x ∈ U ∧ ∃ f : Fin c → Γ(U.toScheme, ⊤),
      U.ι ⁻¹' T = Stacks.Perfect.CechDerivedSupport.equationsClosedSet f)
    (F : X.Modules) [F.IsQuasicoherent] (i : ℤ) (hi : (c : ℤ) < i) :
    IsZero ((DerivedCategory.homologyFunctor
        (SheafOfModules.{u} (structureSheafRing (closedSubsetRingedSpace X.toRingedSpace T))) i).obj
      ((derivedSupportedSectionsOnClosed X.toRingedSpace T hT).obj
        ((DerivedCategory.singleFunctor X.Modules 0).obj F)))
```

## Tag 0G7P, a lemma

[Tag 0G7P](https://stacks.math.columbia.edu/tag/0G7P) in the Stacks Project.

**`Stacks.Perfect.LocalCohomologyDegrees.isZero_homology_derivedSupportedSections_of_locallyKoszulRegular_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/KoszulFlatVanishingLocal.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/KoszulFlatVanishingLocal.lean#L250). The attribute's comment: “the whole statement: for a closed subset locally cut out by a Koszul-regular sequence of c elements and a flat quasi-coherent module, the vanishing of the local cohomology sheaf in every degree other than c; exactly the source's conditions, with locally read over affine open neighbourhoods, which Stacks 063G shows is the same condition”.

> **Stacks Project, Tag 0G7P.**  Let `X` be a scheme.  Let `Z ⊆ X` be a closed subset which can
> locally be cut out by a Koszul-regular sequence having `c` elements.  Then
>
> `ℋ ^i_Z(ℱ) = 0` for `i ≠ c`
>
> for every flat, quasi-coherent `𝒪_X`-module `ℱ`.
>
> Above degree `c` this is Stacks 0G7N, which needs neither the Koszul-regularity of the equations
> nor the flatness of `ℱ`
> (`isZero_homology_derivedSupportedSections_of_locallyKoszulRegular`); below degree `c` it needs
> both and is
> `isZero_homology_derivedSupportedSections_of_locallyKoszulRegular_of_lt`.
>
> "Locally" is read with affine open neighbourhoods, which by Stacks 063G is the same condition as
> the source's; see the implementation notes of this file.

```lean
public theorem isZero_homology_derivedSupportedSections_of_locallyKoszulRegular_of_ne
    {X : Scheme.{u}} (Z : Set X) (hZ : IsClosed Z) (c : ℕ)
    (hcut : ∀ x : X, ∃ U : X.Opens, x ∈ U ∧ IsAffineOpen U ∧
      ∃ f : Fin c → Γ(U.toScheme, ⊤), Koszul.IsKoszulRegular f ∧
        U.ι ⁻¹' Z = equationsClosedSet f)
    (F : X.Modules) [F.IsQuasicoherent]
    (hflat : AlgebraicGeometry.SheafOfModules.IsFlat
      (C := TopologicalSpace.Opens X.toTopCat)
      (J := Opens.grothendieckTopology X.toTopCat) (O := X.sheaf) F)
    (i : ℤ) (hi : i ≠ (c : ℤ)) :
    IsZero ((DerivedCategory.homologyFunctor
        (SheafOfModules.{u} (structureSheafRing (closedSubsetRingedSpace X.toRingedSpace Z))) i).obj
      ((derivedSupportedSectionsOnClosed X.toRingedSpace Z hZ).obj
        ((DerivedCategory.singleFunctor X.Modules 0).obj F)))
```

## Tag 0G7Q, a remark

[Tag 0G7Q](https://stacks.math.columbia.edu/tag/0G7Q) in the Stacks Project.

**`Stacks.Perfect.GysinLocalCohomology.fractionClassOnClosed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Gysin/GysinDifferentialCompatibility.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Gysin/GysinDifferentialCompatibility.lean#L194). The attribute's comment: “the remark's conclusion: the canonical O\_X|\_Z-linear map c\_\{f₁,…,f\_c} : i^*ℱ ⟶ ℋ^c\_Z(ℱ) on Z, together with its functoriality in the 𝒪\_X-module ℱ, as a natural transformation of the two functors of ℱ into 𝒪\_X|\_Z-modules; obtained from the transformation on X by the remark's last step, the transposition along i^* ⊣ i\_* that full faithfulness of i\_* provides”.

> With `X` a scheme, `f₁, …, f_c ∈ Γ(X, 𝒪_X)` and `Z ⊆ X` the closed subscheme they cut out,
> the canonical map `c_{f₁, …, f_c} : i^*ℱ ⟶ ℋ^c_Z(ℱ)` of `𝒪_X|_Z`-modules on `Z`, as a natural
> transformation of functors of the `𝒪_X`-module `ℱ`: from `ℱ ↦ i^*(ℱ/(f₁, …, f_c)ℱ)`, the inverse
> image along the inclusion of `Z` of the cokernel of `(f₁, …, f_c) : ℱ^{⊕c} ⟶ ℱ`, to
> `ℱ ↦ ℋ^c_Z(ℱ)`. Its component at `ℱ` is the transpose under `i^* ⊣ i_*` of the component of
> `fractionClassPushTrans`.

```lean
public def fractionClassOnClosed {d : ℕ} (f : Fin (d + 1) → Γ(X, ⊤)) :
    equationsQuotientFunctor f ⋙
        modulePullback (closedSubsetInclusion X.toRingedSpace (equationsClosedSet f)) ⟶
      DerivedCategory.singleFunctor X.Modules 0 ⋙
        derivedSupportedSectionsOnClosed X.toRingedSpace (equationsClosedSet f)
            (isClosed_equationsClosedSet f) ⋙
          DerivedCategory.homologyFunctor _ ((d + 1 : ℕ) : ℤ)
```

**`AlgebraicGeometry.ExtendedAlternatingCech.eq_of_eq_mod_equations_empty`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClass.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClass.lean#L312). The attribute's comment: “fraction\_class\_well\_defined”.

> For no equations, the fraction is just the numerator itself, and the
> quotient by the zero ideal changes nothing.

```lean
public lemma eq_of_eq_mod_equations_empty
    {X : Scheme.{u}} (f : Fin 0 → Γ(X, ⊤)) (F : X.Modules) (V : X.Opens)
    (s t : Γ(F, V))
    (x y : Γ((data f F).complex.X 0, V))
    (hmod : s - t = ∑ i : Fin 0,
      (X.presheaf.map (homOfLE le_top : V ⟶ ⊤).op (f i)) •
        (0 : Γ(F, V)))
    (hx : ((data f F).zeroIso.hom).app V x = s)
    (hy : ((data f F).zeroIso.hom).app V y = t) :
    x = y
```

**`AlgebraicGeometry.ExtendedAlternatingCech.cokernel_π_app_eq_of_eq_mod_equations`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClass.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClass.lean#L526). The attribute's comment: “fraction\_class\_well\_defined”.

> Fractions with congruent numerators have the same class in the final
> Čech cokernel.

```lean
public lemma cokernel_π_app_eq_of_eq_mod_equations
    {X : Scheme.{u}} {c : ℕ} {ι : Type*} (f : Fin (c + 1) → Γ(X, ⊤))
    (F : X.Modules) (V : X.Opens) (U : ι → X.Opens)
    (hU : ∀ i, U i ≤ V) (hcover : ⨆ i, U i = V)
    (s t : Γ(F, V))
    (x y : Γ((data f F).complex.X (c + 1), V))
    (a : ∀ j : ι, Fin (c + 1) → Γ(F, U j))
    (hmod : ∀ j,
      (Scheme.Modules.presheaf F).map (homOfLE (hU j)).op (s - t) =
        ∑ i, (X.presheaf.map (homOfLE le_top : U j ⟶ ⊤).op (f i)) • a j i)
    (hx : ∀ q : CechCochains.OrdIndex (I := Fin (c + 1)) c,
      (X.presheaf.map (homOfLE le_top :
        CechCochains.inter (fun i => V ⊓ X.basicOpen (f i)) q.1 ⟶ ⊤).op
        (∏ i, f i)) •
        ((data f F).sectionsIso c V x q) =
      (Scheme.Modules.presheaf F).map
        (homOfLE (show
          CechCochains.inter (fun i => V ⊓ X.basicOpen (f i)) q.1 ≤ V from
            (iInf_le _ (0 : Fin (c + 1))).trans inf_le_left)).op s)
    (hy : ∀ q : CechCochains.OrdIndex (I := Fin (c + 1)) c,
      (X.presheaf.map (homOfLE le_top :
        CechCochains.inter (fun i => V ⊓ X.basicOpen (f i)) q.1 ⟶ ⊤).op
        (∏ i, f i)) •
        ((data f F).sectionsIso c V y q) =
      (Scheme.Modules.presheaf F).map
        (homOfLE (show
          CechCochains.inter (fun i => V ⊓ X.basicOpen (f i)) q.1 ≤ V from
            (iInf_le _ (0 : Fin (c + 1))).trans inf_le_left)).op t) :
    (cokernel.π ((data f F).complex.d c (c + 1))).app V x =
      (cokernel.π ((data f F).complex.d c (c + 1))).app V y
```

**`Stacks.Perfect.FractionClass.classMapToPushforward_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L197). The attribute's comment: “functoriality in the 𝒪\_X-module ℱ, with the direct image taken outside the cohomology sheaf, for an arbitrary 𝒪\_X-module and any number of equations”.

> **Stacks Project, Tag 0G7Q, functoriality in `ℱ`**, in the spelling of `i_*ℋ ᶜ_T(ℱ)` with the
> direct image outside: `classMapToSupport_natural`, with its carried numerator hypothesis
> discharged by `fracTermTop_naturality`, carried across the comparison of the two spellings, which
> is natural.

```lean
public theorem classMapToPushforward_natural {c : ℕ} (f : Fin c → Γ(X, ⊤)) {F G : X.Modules}
    (φ : F ⟶ G) {T : Set X} (hT : IsClosed T) (hTf : equationsClosedSet f ⊆ T) :
    φ ≫ classMapToPushforward f G hT hTf =
      classMapToPushforward f F hT hTf ≫ (localCohomologyPushforwardFunctor hT (c : ℤ)).map φ
```

**`Stacks.Perfect.FractionClass.quotientClassMapToPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L274). The attribute's comment: “i\_* of the remark's map c\_\{f₁,…,f\_c}, between its two presentations, for an arbitrary 𝒪\_X-module ℱ and any number of equations”.

> **Stacks Project, Tag 0G7Q, for an arbitrary `𝒪_X`-module.**  The `𝒪_X`-module map
>
> `i_*i^*ℱ = ℱ/(f₁, …, f_c)ℱ ⟶ i_*ℋ ᶜ_T(ℱ)`
>
> carrying the class of a local section `s` of `ℱ` to the class of the fraction `s / (f₁ ⋯ f_c)`.
> The remark builds exactly this map and then descends it along the fully faithful `i_*`; here the
> descent is `fractionClassAnyModule`.
>
> No quasi-coherence and no hypothesis on the number of equations: the class of the fraction lands
> in the degree-`c` cohomology sheaf of the extended alternating Čech complex, which the comparison
> of [Stacks, Tag 0G7L] carries into `i_*ℋ ᶜ_T(ℱ)` for every `𝒪_X`-module `ℱ`.

```lean
public def quotientClassMapToPushforward {c : ℕ} (f : Fin c → Γ(X, ⊤)) (F : X.Modules)
    {T : Set X} (hT : IsClosed T) (hTf : equationsClosedSet f ⊆ T) :
    equationsQuotient f F ⟶ (localCohomologyPushforwardFunctor hT (c : ℤ)).obj F
```

**`Stacks.Perfect.FractionClass.cokernelπ_comp_quotientClassMapToPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L284). The attribute's comment: “the value on the class of a local section is the class of its fraction, for an arbitrary 𝒪\_X-module ℱ”.

> **Stacks Project, Tag 0G7Q.**  The map out of the quotient sends the class of a local section
> `s` of `ℱ` to the class of the fraction `s / (f₁ ⋯ f_c)`.

```lean
public theorem cokernelπ_comp_quotientClassMapToPushforward {c : ℕ} (f : Fin c → Γ(X, ⊤))
    (F : X.Modules) {T : Set X} (hT : IsClosed T) (hTf : equationsClosedSet f ⊆ T) :
    cokernel.π (equationsMap f F) ≫ quotientClassMapToPushforward f F hT hTf =
      classMapToPushforward f F hT hTf
```

**`Stacks.Perfect.FractionClass.quotientClassMapToPushforward_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L298). The attribute's comment: “functoriality in the 𝒪\_X-module ℱ of i\_* of the remark's map, for an arbitrary 𝒪\_X-module ℱ and any number of equations”.

> **Stacks Project, Tag 0G7Q, functoriality in `ℱ` of the map out of the quotient.**  The
> square commutes for every morphism `φ : ℱ ⟶ 𝒢` of `𝒪_X`-modules, the left vertical arrow being
> `i_*i^*φ` in the presentation `equationsQuotientMap`.
>
> The projection onto the quotient is an epimorphism, so this is
> `classMapToPushforward_natural`.

```lean
public theorem quotientClassMapToPushforward_natural {c : ℕ} (f : Fin c → Γ(X, ⊤))
    {F G : X.Modules} (φ : F ⟶ G) {T : Set X} (hT : IsClosed T)
    (hTf : equationsClosedSet f ⊆ T) :
    equationsQuotientMap f φ ≫ quotientClassMapToPushforward f G hT hTf =
      quotientClassMapToPushforward f F hT hTf ≫
        (localCohomologyPushforwardFunctor hT (c : ℤ)).map φ
```

**`Stacks.Perfect.FractionClass.fractionClassAnyModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L332). The attribute's comment: “the canonical map c\_\{f\_1, …, f\_c}, for an arbitrary 𝒪\_X-module ℱ and any number of equations”.

> **Stacks Project, Tag 0G7Q, for every `𝒪_X`-module.**  The canonical `𝒪_X|_T`-linear map
>
> `c_{f₁, …, f_c} : i^*(ℱ/(f₁, …, f_c)ℱ) ⟶ ℋ ᶜ_T(ℱ)`
>
> on a closed subset `T` containing the common zero locus of `f₁, …, f_c`, for an **arbitrary**
> `𝒪_X`-module `ℱ` and an arbitrary number of equations.  It is the transpose, under the adjunction
> `i^* ⊣ i_*` between inverse image and direct image along the inclusion of `T`, of the map
> `quotientClassMapToPushforward` carrying the class of a local section `s` of `ℱ` to the class of
> the fraction `s / (f₁ ⋯ f_c)`.
>
> This is the remark's own construction: the `𝒪_X`-module map `i_*i^*ℱ ⟶ i_*ℋ ᶜ_T(ℱ)` followed by
> the descent along `i_*`.  Only the comparison of [Stacks, Tag 0G7L] is used, and that holds for
> every `𝒪_X`-module; `Stacks.Perfect.FractionClass.fractionClass` is this map on a quasi-coherent
> module, by `fractionClassAnyModule_eq`.

```lean
public def fractionClassAnyModule {c : ℕ} (f : Fin c → Γ(X, ⊤)) (F : X.Modules) {T : Set X}
    (hT : IsClosed T) (hTf : equationsClosedSet f ⊆ T) :
    (modulePullback (closedSubsetInclusion X.toRingedSpace T)).obj (equationsQuotient f F) ⟶
      localCohomologySheafOfComplex X.toRingedSpace T hT (c : ℤ)
        ((DerivedCategory.singleFunctor X.Modules 0).obj F)
```

**`Stacks.Perfect.FractionClass.homEquiv_fractionClassAnyModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L344). The attribute's comment: “c\_\{f\_1, …, f\_c} is the transpose of the map out of the quotient, for an arbitrary 𝒪\_X-module ℱ”.

> **Stacks Project, Tag 0G7Q.**  The map `c_{f₁, …, f_c}` is the transpose of the map
> `i_*i^*ℱ ⟶ i_*ℋ ᶜ_T(ℱ)` out of the quotient by the equations.

```lean
public theorem homEquiv_fractionClassAnyModule {c : ℕ} (f : Fin c → Γ(X, ⊤)) (F : X.Modules)
    {T : Set X} (hT : IsClosed T) (hTf : equationsClosedSet f ⊆ T) :
    homEquiv (closedSubsetInclusion X.toRingedSpace T) _ (equationsQuotient f F)
        (fractionClassAnyModule f F hT hTf) =
      quotientClassMapToPushforward f F hT hTf
```

**`Stacks.Perfect.FractionClass.fractionClassAnyModule_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L364). The attribute's comment: “functoriality in the 𝒪\_X-module ℱ of c\_\{f\_1, …, f\_c} itself, for an arbitrary 𝒪\_X-module ℱ and any number of equations”.

> **Stacks Project, Tag 0G7Q, functoriality in `ℱ` of `c_{f₁, …, f_c}` itself.**  For every
> morphism `φ : ℱ ⟶ 𝒢` of `𝒪_X`-modules the square
>
> `i^*(ℱ/(f)ℱ) ⟶ ℋ ᶜ_T(ℱ)`, `i^*(𝒢/(f)𝒢) ⟶ ℋ ᶜ_T(𝒢)`
>
> commutes, the vertical arrows being `i^*` of `equationsQuotientMap` and `ℋ ᶜ_T(φ)`.  This is the
> functoriality the remark asserts, read on `c_{f₁, …, f_c}` rather than on its direct image.
>
> It is `quotientClassMapToPushforward_natural` transposed: both sides become maps out of
> `ℱ/(f)ℱ` under the bijection of the adjunction `i^* ⊣ i_*`, by its naturality in each variable,
> and there the square is the one already proved.

```lean
public theorem fractionClassAnyModule_natural {c : ℕ} (f : Fin c → Γ(X, ⊤)) {F G : X.Modules}
    (φ : F ⟶ G) {T : Set X} (hT : IsClosed T) (hTf : equationsClosedSet f ⊆ T) :
    (modulePullback (closedSubsetInclusion X.toRingedSpace T)).map (equationsQuotientMap f φ) ≫
        fractionClassAnyModule f G hT hTf =
      fractionClassAnyModule f F hT hTf ≫
        (localCohomologySheafOfComplexFunctor X.toRingedSpace T hT (c : ℤ)).map φ
```

**`Stacks.Perfect.FractionClass.fractionClassAnyModule_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassAnyModule.lean#L419). The attribute's comment: “the quasi-coherent construction of c\_\{f\_1, …, f\_c} is the arbitrary-module one specialised”.

> **Stacks Project, Tag 0G7Q: the quasi-coherent construction is this one specialised.**  On a
> quasi-coherent `𝒪_X`-module the map `c_{f₁, …, f_c}` built here through [Stacks, Tag 0G7L] alone
> is `Stacks.Perfect.FractionClass.fractionClass`, which is built through [Stacks, Tag 0G7M].  Both
> are transposes along `i^* ⊣ i_*`, and their transposes agree by
> `quotientClassMapToPushforward_eq`.

```lean
public theorem fractionClassAnyModule_eq {c : ℕ} (f : Fin c → Γ(X, ⊤)) (F : X.Modules)
    [F.IsQuasicoherent] :
    fractionClassAnyModule f F (isClosed_equationsClosedSet f) subset_rfl = fractionClass f F
```

**`Stacks.Perfect.FractionClass.smulHom_comp_classMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean, line 526](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean#L526). The attribute's comment: “the class of the fraction depends only on the numerator modulo the equations”.

> **The fraction class only depends on the numerator modulo the equations.** Multiplying the
> numerator by one of the equations kills the class of the fraction, because the result is the image
> of a cochain under the last Čech differential. An equation to multiply by is itself a witness
> that there is at least one, which is what the descent of the product needs.

```lean
public theorem smulHom_comp_classMap (j : Fin c) :
    smulHom (f j) F ≫ classMap f F = 0
```

**`Stacks.Perfect.FractionClass.cokernelπ_comp_quotientClassMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean#L564). The attribute's comment: “the value on the class of a local section is the class of its fraction”.

> The map out of the quotient sends the class of a section to the class of its fraction.

```lean
public theorem cokernelπ_comp_quotientClassMap :
    cokernel.π (equationsMap f F) ≫ quotientClassMap f F = classMap f F
```

**`Stacks.Perfect.FractionClass.fractionClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean, line 663](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean#L663). The attribute's comment: “the canonical map c\_\{f\_1, …, f\_c}”.

> **Stacks Project, Tag 0G7Q.** The canonical map
> `c_{f₁, …, f_c} : i^{-1}(ℱ/(f₁, …, f_c)ℱ) ⟶ 𝓗ᶜ_Z(ℱ)`
> of `𝒪_X|_Z`-modules on the common zero locus `Z` of `f₁, …, f_c`, for a quasi-coherent
> `𝒪_X`-module `ℱ`: it is the transpose, under the adjunction between inverse image and direct
> image along the inclusion of `Z`, of the map carrying the class of a local section `s` of `ℱ` to
> the class of the fraction `s / (f₁ ⋯ f_c)` in the degree-`c` cohomology sheaf of the extended
> alternating Čech complex of the equations, which is the direct image of `𝓗ᶜ_Z(ℱ)`.

```lean
public def fractionClass [F.IsQuasicoherent] :
    (modulePullback (closedSubsetInclusion X.toRingedSpace (equationsClosedSet f))).obj
        (equationsQuotient f F) ⟶
      localCohomologySheafOfComplex X.toRingedSpace (equationsClosedSet f)
        (isClosed_equationsClosedSet f) (c : ℤ)
        ((DerivedCategory.singleFunctor X.Modules 0).obj F)
```

**`Stacks.Perfect.FractionClass.pushforwardFractionClass_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean#L686). The attribute's comment: “the fraction class followed by the identifications”.

> **Stacks Project, Tag 0G7Q.** The map to the direct image of the local cohomology sheaf is
> the fraction class followed by the two identifications: the comparison of the two constructions
> of the extended alternating Čech complex, and the identification of the degree-`c` cohomology
> sheaf of that complex with the direct image of `𝓗ᶜ_Z(ℱ)`.

```lean
public theorem pushforwardFractionClass_eq [F.IsQuasicoherent] :
    pushforwardFractionClass f F =
      (quotientClassMap f F ≫ HomologicalComplex.homologyMap
          (Stacks.Perfect.CechComparison.complexIso f F).inv c) ≫
        (Stacks.Perfect.CechLocalCohomology.pushforwardLocalCohomologyIso f F c).inv
```

**`Stacks.Perfect.FractionClass.homEquiv_fractionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean, line 695](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/FractionClassMap.lean#L695). The attribute's comment: “c\_\{f\_1, …, f\_c} is the transpose of the fraction class”.

> **Stacks Project, Tag 0G7Q.** The map `c_{f₁, …, f_c}` is the transpose of the map from the
> quotient `ℱ/(f₁, …, f_c)ℱ` to the direct image of the degree-`c` local cohomology sheaf.

```lean
public theorem homEquiv_fractionClass [F.IsQuasicoherent] :
    homEquiv (closedSubsetInclusion X.toRingedSpace (equationsClosedSet f)) _
        (equationsQuotient f F) (fractionClass f F) =
      pushforwardFractionClass f F
```

**`Stacks.Perfect.SupportedFraction.supportedFractionClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionMap.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionMap.lean#L738). The attribute's comment: “i\_* of the remark's map c\_\{f₁,…,f\_c}, between its two presentations; no descent”.

> **Stacks Project, Tag 0G7Q**, the class of the fraction `s / (f₁ ⋯ f_c)`.  With `X`,
> `f₁, …, f_c ∈ Γ(X, 𝒪_X)` and `ℱ` as in Tag 0G7I, this is the map
>
> `Coker((f₁, …, f_c) : ℱ^{⊕c} ⟶ ℱ) ⟶ Coker(⨁ᵢ ℱ_{1…î…c} ⟶ ℱ_{1…c})`
>
> carrying the class of a local section `s` of `ℱ` to the class of the fraction
> `s / (f₁ ⋯ f_c)`, by `supportedFractionClass_mk`.  It is the direct image along the closed
> immersion `i : Z → X` of the map `c_{f₁,…,f_c} : i^*ℱ ⟶ ℋ^c_Z(ℱ)` of the remark: its source is
> `i_* i^*ℱ`, presented as the cokernel of `(f₁, …, f_c)` as the remark does, and its target is
> `i_* ℋ^c_Z(ℱ)`, presented as the cokernel of the last differential of the extended alternating
> Čech complex as the remark does, the two being identified by Tag 0G7M.

```lean
public def supportedFractionClass {d : ℕ} (f : Fin (d + 1) → Γ(X, ⊤)) (F : X.Modules) :
    cokernel (equationsMultiplication f F) ⟶ cokernel (lastDif f F)
```

**`Stacks.Perfect.SupportedFraction.supportedFractionClass_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionMap.lean, line 748](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionMap.lean#L748). The attribute's comment: “the value of the class map on the class of a section”.

> **Stacks Project, Tag 0G7Q.**  The class map sends the class of a local section `s` of `ℱ`
> to the class of the fraction `s / (f₁ ⋯ f_c)` in the cokernel of the last differential of the
> extended alternating Čech complex.

```lean
public theorem supportedFractionClass_mk {d : ℕ} (f : Fin (d + 1) → Γ(X, ⊤))
    (F : X.Modules) (V : X.Opens) (s : Γ(F, V)) :
    (supportedFractionClass f F).app V
        ((cokernel.π (equationsMultiplication f F)).app V s) =
      (cokernel.π (lastDif f F)).app V ((fractionHom f F d).app V s)
```

**`Stacks.Perfect.SupportedFraction.fractionClassTrans`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionNaturality.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/SupportedFractionNaturality.lean#L489). The attribute's comment: “the canonical map c\_\{f₁,…,f\_c} : i^*ℱ ⟶ ℋ^c\_Z(ℱ) together with its functoriality in the 𝒪\_X-module ℱ, as a natural transformation between the two functors of ℱ: from ℱ ↦ i\_*i^*ℱ, the cokernel of (f₁,…,f\_c) as the remark presents it, to ℱ ↦ i\_*ℋ^c\_Z(ℱ); read on X along the fully faithful i\_*, as the remark's last step and as Stacks 0G7T does for the twisted map”.

> **Stacks Project, Tag 0G7Q.**  With `X` a scheme, `f₁, …, f_c ∈ Γ(X, 𝒪_X)` global functions
> and `Z ⊆ X` the closed subscheme they cut out, there is a canonical map
>
> `c_{f₁, …, f_c} : i^*ℱ ⟶ ℋ^c_Z(ℱ)`
>
> of `𝒪_X|_Z`-modules, functorial in the `𝒪_X`-module `ℱ`.  Here it is that functoriality: a
> natural transformation between the two functors of `ℱ`, from `ℱ ↦ i_*i^*ℱ`
> (`equationsQuotientFunctor`, the cokernel of `(f₁, …, f_c) : ℱ^{⊕c} ⟶ ℱ`, which is how the remark
> presents the source) to `ℱ ↦ i_*ℋ^c_Z(ℱ)` (`supportCohomologySheafFunctor`).  Both functors are
> direct images along the inclusion of `Z`, which is fully faithful, so the transformation is the
> map of `𝒪_X|_Z`-modules of the statement — this is the last step of the remark's construction and
> the form in which Stacks 0G7T states the analogous twisted map
> (`Stacks.Perfect.ConormalClass.conormalTwistClass`).
>
> Its component at `ℱ` is the map `supportedFractionClass` of the remark, between the two
> presentations, followed by the canonical identification `General.cokernelLastDifToSupport` of its
> target with `i_*ℋ^c_Z(ℱ)`; on the class of a local section `s` of `ℱ` it is the class of the
> fraction `s / (f₁ ⋯ f_c)`, by `cokernelπ_comp_fractionClassTrans_app`.  As in Remark 0G7I, which
> fixes the setting of this remark, `ℱ` is an arbitrary `𝒪_X`-module and the morphisms of the
> naturality square are arbitrary morphisms of `𝒪_X`-modules: quasi-coherence is used neither by
> the map nor by its functoriality, which is why the two factors and the naturality square are
> taken from the namespace `General` above, and the source adds it only in Stacks 0G7S and
> Stacks 0G7U.
>
> The target is the spelling of `i_*ℋ^c_Z(ℱ)` in which Stacks 0G7Q and Stacks 0G7S are stated here,
> with the direct image taken before the cohomology sheaf.  The other spelling, with the cohomology
> sheaf taken on `Z` first — the one `Stacks.Perfect.FractionClass.fractionClass` lands in — is
> identified with this one, naturally in `ℱ` and with no hypothesis on `ℱ`, by
> `Stacks.Perfect.GysinLocalCohomology.supportCohomologySheafFunctorIso`.

```lean
public def fractionClassTrans {d : ℕ} (f : Fin (d + 1) → Γ(X, ⊤)) :
    equationsQuotientFunctor f ⟶
      supportCohomologySheafFunctor (isClosed_equationsClosedSet f) ((d + 1 : ℕ) : ℤ)
```

## Tag 0G7R, an example

[Tag 0G7R](https://stacks.math.columbia.edu/tag/0G7R) in the Stacks Project.

**`Stacks.Perfect.AffineFractionClass.supportedFraction_eq_conj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AffineFractionClassBijective.lean, line 673](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AffineFractionClassBijective.lean#L673). The attribute's comment: “the description itself: Γ(Spec A, -) of Tag 0G7Q's map c\_\{f₁,…,f\_c} for ℱ = M~, conjugated by the two canonical isomorphisms affineSourceEquiv and targetEquiv, IS the map Cech.supportedFraction of Tag 0G7R”.

> **Clause 3 of Tag 0G7R.**  Let `A` be a commutative ring, let `f₁, …, f_c ∈ A` be a finite
> nonempty family and let `M` be an `A`-module.  The map `c_{f₁,…,f_c}` of Tag 0G7Q for
> `X = Spec A` and `ℱ = M~`, in the cokernel-to-cokernel presentation
> `Coker((f₁,…,f_c) : ℱ^{⊕c} ⟶ ℱ) ⟶ Coker(lastDif)` of
> `Stacks.Perfect.SupportedFraction.supportedFractionClass`, read on global sections through the
> two canonical isomorphisms
>
> `M/(f₁,…,f_c)M ≅ Γ(Spec A, Coker((f₁,…,f_c) : (M~)^{⊕c} ⟶ M~))`  (`affineSourceEquiv`) and
> `Coker(⨁ᵢ M_{f₁⋯f̂ᵢ⋯f_c} ⟶ M_{f₁⋯f_c}) ≅ Γ(Spec A, Coker(lastDif))`  (`targetEquiv`),
>
> **is** the map `Cech.supportedFraction` by which the example describes it.  Both comparisons are
> isomorphisms (`bijective_affineSourceComparison` and `bijective_targetComparison`).

```lean
public theorem supportedFraction_eq_conj (f : Fin (d + 1) → R) (M : ModuleCat.{u} R) :
    Cech.supportedFraction f (M : Type u) =
      (targetEquiv f M).symm.toLinearMap ∘ₗ
        ((moduleSpecΓFunctor.map (supportedFractionClass (specFun f) (tilde M))).hom ∘ₗ
          (affineSourceEquiv f M).toLinearMap)
```

**`Stacks.Perfect.AffineFractionClass.targetEquiv_symm_Γ_supportedFractionClass_affineSourceEquiv_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AffineFractionClassBijective.lean, line 715](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AffineFractionClassBijective.lean#L715). The attribute's comment: “the example in one statement: for X = Spec A and ℱ = M~, Tag 0G7Q's map c\_\{f₁,…,f\_c} on global sections, conjugated by the canonical isomorphisms affineSourceEquiv and targetEquiv, sends the class of s ∈ M to the class of the fraction s/(f₁⋯f\_c) in Coker(⨁ᵢ M\_\{f₁⋯f̂ᵢ⋯f\_c} ⟶ M\_\{f₁⋯f\_c})”.

> **Tag 0G7R.**  Let `A` be a commutative ring, let `f₁, …, f_c ∈ A` and let `M` be an
> `A`-module.  Take `X = Spec A` and `ℱ = M~`.  Then the map `c_{f₁,…,f_c}` of Tag 0G7Q, read on
> global sections through the two canonical `A`-linear isomorphisms
>
> `M/(f₁,…,f_c)M ≅ Γ(Spec A, Coker((f₁,…,f_c) : ℱ^{⊕c} ⟶ ℱ))`  (`affineSourceEquiv`) and
> `Coker(⨁ᵢ M_{f₁⋯f̂ᵢ⋯f_c} ⟶ M_{f₁⋯f_c}) ≅ Γ(Spec A, Coker(lastDif))`  (`targetEquiv`),
>
> is the map `M/(f₁,…,f_c)M ⟶ Coker(⨁ᵢ M_{f₁⋯f̂ᵢ⋯f_c} ⟶ M_{f₁⋯f_c})` carrying the class of
> `s ∈ M` to the class of the fraction `s/(f₁⋯f_c)`.
>
> This is the example's description, source and target modules, map and formula together, in one
> statement, for a nonempty family; the empty family is
> `Stacks.Perfect.AffineFractionClassEmpty.targetIsoEmpty_inv_Γ_quotientClassMap_sourceIsoEmpty`.
> The classes of sections exhaust `M/(f₁,…,f_c)M`, so the formula below determines the
> conjugated map; the map-level equality is `supportedFraction_eq_conj` and the formula alone is
> `Cech.supportedFraction_mk`.
>
> The ring and the module are taken in a *single* universe, as `tilde` requires, whereas
> `Cech.supportedFraction` itself is stated for a ring and a module in independent universes.
> That is a restriction of spelling only: a ring and a module in independent
> universes are moved into a common universe by `ULift`.

```lean
public theorem targetEquiv_symm_Γ_supportedFractionClass_affineSourceEquiv_mk
    (f : Fin (d + 1) → R) (M : ModuleCat.{u} R) (s : M) :
    (targetEquiv f M).symm
        ((moduleSpecΓFunctor.map (supportedFractionClass (specFun f) (tilde M))).hom
          (affineSourceEquiv f M (Submodule.Quotient.mk s))) =
      Submodule.Quotient.mk
        (DirectSum.lof R {t : Finset (Fin (d + 1)) // t.card = d + 1}
          (fun t => Cech.cechMod f (M : Type u) t.1) ⟨Finset.univ, Finset.card_fin _⟩
          (LocalizedModule.mk s ⟨∏ i, f i, Submonoid.mem_powers _⟩))
```

**`Stacks.Perfect.AffineFractionClassEmpty.targetIsoEmpty_inv_Γ_quotientClassMap_sourceIsoEmpty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AffineFractionClassEmpty.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/AffineFractionClassEmpty.lean#L145). The attribute's comment: “the case c = 0: for X = Spec A, ℱ = M~ and the empty family, Tag 0G7Q's map on global sections, conjugated by the canonical isomorphisms sourceIsoEmpty and targetIsoEmpty, sends the class of s ∈ M to s/(f₁⋯f\_c) = s/1”.

> For the empty family (`c = 0`), let `A` be a commutative ring, let `M` be an `A`-module and
> take `X = Spec A`, `ℱ = M~` and the empty family of equations. Then the map `c_{f₁, …, f_c}` of
> Tag 0G7Q, read on global sections through the canonical isomorphisms
> `M/(f₁, …, f_c)M ≅ Γ(Spec A, ℱ/(f₁, …, f_c)ℱ)` (`sourceIsoEmpty`) and
> `M_{f₁⋯f_c} ≅ Γ(Spec A, H⁰(ℱ^•))` (`targetIsoEmpty`), sends the class of `s ∈ M` to the fraction
> `s/(f₁⋯f_c)`; here `f₁⋯f_c = 1`, the cokernel of the map out of the empty direct sum is
> `M_{f₁⋯f_c}` itself, and the map is `s ↦ s/1`.

```lean
theorem targetIsoEmpty_inv_Γ_quotientClassMap_sourceIsoEmpty (s : M) :
    (targetIsoEmpty f M).inv
        ((moduleSpecΓFunctor.map (quotientClassMap (specFunEmpty f) (tilde M))).hom
          ((sourceIsoEmpty f M).hom (Submodule.Quotient.mk s))) =
      LocalizedModule.mk s ⟨∏ i, f i, Submonoid.mem_powers _⟩
```

## Tag 0G7S, a lemma

[Tag 0G7S](https://stacks.math.columbia.edu/tag/0G7S) in the Stacks Project.

**`Stacks.Perfect.SupportedFraction.supportedFractionClass_eq_det_smul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/ClassTarget.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/ClassTarget.lean#L391). The attribute's comment: “the determinant identity c\_\{f₁,…,f\_c} = det(a\_\{ji})·c\_\{g₁,…,g\_c} as ONE equation of maps into the common target i\_*ℋ^c\_Z(ℱ), together with the invertibility of the two identifications it is read through. The 0G7Q class maps of the f- and the g-complex are composed with cokernelLastDifToSupport -- cokernel of the last differential ≅ H^c of the complex ≅ i\_*ℋ^c\_Z(ℱ), the last step by the canonical comparison of Stacks 0G7L and its invertibility, which is Stacks 0G7M -- and are read on the common source ℱ through the two canonical epimorphisms ℱ ↠ i\_*i^*ℱ; those are epimorphisms, so this is equivalent to the equality of the class maps and needs no chosen isomorphism between the two presentations of i\_*i^*ℱ. The hypothesis used in place of the source's 'g₁,…,g\_c cut out Z scheme theoretically' is the weaker set-level equality of the two common zero loci, so this is a GENERALIZATION and not a weakening: it suffices because RℋT depends only on the closed set T, so no scheme structure on Z enters the identification of the two targets”.

> **Stacks Project, Tag 0G7S**, the determinant identity as a single equation in a common
> target.
>
> With `X`, `f₁, …, f_c ∈ Γ(X, 𝒪_X)` and `ℱ` as in Stacks 0G7I, let `a_{ji} ∈ Γ(X, 𝒪_X)` and
> `g_j = ∑_i a_{ji} f_i`, let `ℱ` be quasi-coherent and let `g₁, …, g_c` cut out the same closed
> subset `Z` as `f₁, …, f_c`.  Then
>
> `c_{f₁,…,f_c} = det(a_{ji}) c_{g₁,…,g_c}`
>
> as maps into the single object `i_*ℋ^c_Z(ℱ)`.
>
> The two class maps `supportedFractionClass f F` and `supportedFractionClass g F` of Stacks 0G7Q
> land in the cokernels of the last differentials of the `f`- and the `g`-complex.  Each of those
> cokernels is identified with `i_*ℋ^c_Z(ℱ)` by `cokernelLastDifToSupport`, the composite of
> `cokernelLastDifIsoHomology` (the cokernel of the last differential is the degree-`c` cohomology
> of the complex) with the degree-`c` cohomology of the canonical comparison `cechToDerivedSupport`
> of Stacks 0G7L; both identifications are isomorphisms, which is the first two conjuncts and is
> Stacks 0G7M.  Both class maps are then read on the common source `ℱ` through the canonical
> epimorphisms `cokernel.π (equationsMultiplication f F)` and
> `cokernel.π (equationsMultiplication g F)` presenting `i_* i^*ℱ` in the two ways the remark does;
> since those are epimorphisms, the displayed equation is equivalent to the equality of the class
> maps themselves, and no choice of isomorphism between the two presentations of `i_* i^*ℱ` is
> needed.
>
> The proof is the source's: both sides are the image of the single degree-`c` cohomology class of
> the mixed cocycle `mixedFractionHom` on the complex of the `2c` equations `f₁, …, f_c, g₁, …, g_c`
> (`subfamily_comp_cokernelπ_comp_cokernelLastDifToSupport` applied to the two projections
> `mixedFractionHom_subfamilyProd_castAdd` and `mixedFractionHom_subfamilyProd_natAdd`).
>
> The hypothesis `hZ` replaces the source's "`g₁, …, g_c` cut out `Z` scheme theoretically" by the
> equality of the two common zero loci as closed *subsets*.  That is implied by the
> scheme-theoretic condition, so the statement is a generalisation of the source's and not a
> weakening of it.  It suffices because `R𝓗_T` depends only on the closed subset `T`: no scheme
> structure on `Z` enters the identification of the two targets.

```lean
public theorem supportedFractionClass_eq_det_smul {d : ℕ} (f g : Fin (d + 1) → Γ(X, ⊤))
    (a : Matrix (Fin (d + 1)) (Fin (d + 1)) Γ(X, ⊤)) (F : X.Modules) [F.IsQuasicoherent]
    (hg : ∀ j, g j = ∑ i, a j i * f i)
    (hZ : equationsClosedSet g = equationsClosedSet f) :
    IsIso (cokernelLastDifToSupport f F (isClosed_equationsClosedSet f) subset_rfl) ∧
      IsIso (cokernelLastDifToSupport g F (isClosed_equationsClosedSet f) hZ.le) ∧
      cokernel.π (equationsMultiplication f F) ≫ supportedFractionClass f F ≫
          cokernelLastDifToSupport f F (isClosed_equationsClosedSet f) subset_rfl =
        globalSmul a.det F ≫ cokernel.π (equationsMultiplication g F) ≫
          supportedFractionClass g F ≫
            cokernelLastDifToSupport g F (isClosed_equationsClosedSet f) hZ.le
```

**`Stacks.Perfect.SupportedFraction.mixedFractionHom_projections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Cocycle.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Cocycle.lean#L361). The attribute's comment: “the source's own construction: the explicit degree-c cocycle on the mixed extended alternating Čech complex of f₁,…,f\_c,g₁,…,g\_c is a cocycle, and projects to s/(f₁⋯f\_c) and to det(a)·s/(g₁⋯g\_c). Stated at the level of the complexes, i.e. before the identification of the degree-c cohomology of the three complexes with i\_*ℋ^c\_Z(ℱ); that identification is Stacks 0G7M, and composing it with this statement to obtain the single equation c\_\{f₁,…,f\_c} = det(a\_\{ji})·c\_\{g₁,…,g\_c} is carried out in this module, in supportedFractionClass\_eq\_det\_smul”.

> **Stacks Project, Tag 0G7S**, the determinant identity on the mixed extended alternating
> Čech complex.
>
> With `X`, `f₁, …, f_c ∈ Γ(X, 𝒪_X)` and `ℱ` as in Stacks 0G7I, let `a_{ji} ∈ Γ(X, 𝒪_X)` and
> `g_j = ∑_i a_{ji} f_i`.  Write `𝓕''^•` for the extended alternating Čech complex of the mixed
> family `f₁, …, f_c, g₁, …, g_c` of `2c` equations, which is the complex the source's proof
> introduces.  Projecting away the components involving a `g`, respectively an `f`, gives the two
> morphisms of complexes `𝓕''^• ⟶ 𝓕^•` and `𝓕''^• ⟶ (𝓕')^•` of the source, both the identity in
> degree `0` (`subfamilyCplxMap`, whose degree-`(c)` component is `subfamilyProd`).
>
> The content of the lemma is the explicit degree-`c` cocycle `σ = mixedFractionHom` of the
> source, whose component at an increasing `c`-tuple `q` of the `2c` indices is
> `det(minor of (a_{ji}) selected by q) · s / (product of the equations of q)`:
>
> * `σ` is a cocycle;
> * its projection to `𝓕^•` is `s / (f₁ ⋯ f_c)`, i.e. `c_{f₁,…,f_c}`;
> * its projection to `(𝓕')^•` is `det(a_{ji}) s / (g₁ ⋯ g_c)`, i.e. `det(a_{ji}) c_{g₁,…,g_c}`.
>
> What is **not** carried out here is the last step of the source's proof: passing from these
> two projections of `σ` to the single equation `c_{f₁,…,f_c} = det(a_{ji}) c_{g₁,…,g_c}` of
> sheaf maps `i^*ℱ ⟶ ℋ^c_Z(ℱ)`.  That step is the identification of the degree-`c` cohomology of
> each of the three complexes with `i_*ℋ^c_Z(ℱ)`, which is Stacks 0G7M and **is** available in
> this library — `Stacks.Perfect.CechDerivedSupport.isIso_map_augmentation_of_isQuasicoherent`
> for the half that uses the quasi-coherence of `ℱ`, and
> `isIso_derivedSupportedSectionsToId_cech` above for the canonical form of the other half.  What
> is missing is only the bookkeeping that composes the two statements below with those
> identifications: the comparison `cechToDerivedSupport` of Stacks 0G7L above, its degree-`c`
> cohomology sheaf, and the identification of `H^c` of each complex with the cokernel of its last
> differential.  The hypothesis that `g₁, …, g_c` cut out `Z` scheme theoretically is likewise
> needed only for that step — it is what makes the two identifications land in the same
> `i_*ℋ^c_Z(ℱ)` — and so does not appear below.

```lean
public theorem mixedFractionHom_projections (hg : ∀ j, g j = ∑ i, a j i * f i) :
    mixedFractionHom (mixedEquations f g) a F ≫ difSucc (mixedEquations f g) F d = 0 ∧
      mixedFractionHom (mixedEquations f g) a F ≫
          subfamilyProd (mixedEquations f g) (Fin.castAddOrderEmb (d + 1) :
            Fin (d + 1) ↪o Fin ((d + 1) + (d + 1))) F d ≫
          prodTermCongr (mixedEquations_comp_castAdd f g) F d =
        fractionHom f F d ∧
      mixedFractionHom (mixedEquations f g) a F ≫
          subfamilyProd (mixedEquations f g) (Fin.natAddOrderEmb (d + 1) :
            Fin (d + 1) ↪o Fin ((d + 1) + (d + 1))) F d ≫
          prodTermCongr (mixedEquations_comp_natAdd f g) F d =
        globalSmul a.det F ≫ fractionHom g F d
```

**`Stacks.Perfect.SupportedFraction.mixedFractionHom_comp_cokernelπ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Cocycle.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/DeterminantChangeOfEquations/Cocycle.lean#L396). The attribute's comment: “the same identity read on the two class maps c\_\{f₁,…,f\_c} and c\_\{g₁,…,g\_c} of Stacks 0G7Q, with the two sides in the cokernels of the last differentials of the two complexes rather than in a common i\_*ℋ^c\_Z(ℱ); the identification of those cokernels with i\_*ℋ^c\_Z(ℱ) is Stacks 0G7M, and composing it with this statement to obtain the single equation is supportedFractionClass\_eq\_det\_smul in this module”.

> **Stacks Project, Tag 0G7S**, read on the classes of Stacks 0G7Q.
>
> The class map `c_{f₁,…,f_c}` of Stacks 0G7Q is `supportedFractionClass f F`, carrying the class
> of a local section `s` to the class of `s / (f₁ ⋯ f_c)` in the cokernel of the last differential
> of the extended alternating Čech complex of `f₁, …, f_c`.  Both `c_{f₁,…,f_c}` and
> `det(a_{ji}) c_{g₁,…,g_c}` are the image of the single degree-`c` class `σ` of the mixed complex
> under the two projections.  This is the equality in the form the source proves it, with the two
> sides still living in the cokernels of the last differentials of the `f`- and the `g`-complex
> rather than in a common `i_*ℋ^c_Z(ℱ)`; the identification of those two cokernels with
> `i_*ℋ^c_Z(ℱ)` is Stacks 0G7M, and composing it with this statement to obtain the single
> equation is `supportedFractionClass_eq_det_smul` below.

```lean
public theorem mixedFractionHom_comp_cokernelπ (hg : ∀ j, g j = ∑ i, a j i * f i) :
    mixedFractionHom (mixedEquations f g) a F ≫
          subfamilyProd (mixedEquations f g) (Fin.castAddOrderEmb (d + 1) :
            Fin (d + 1) ↪o Fin ((d + 1) + (d + 1))) F d ≫
          prodTermCongr (mixedEquations_comp_castAdd f g) F d ≫
          cokernel.π (lastDif f F) =
        cokernel.π (equationsMultiplication f F) ≫ supportedFractionClass f F ∧
      mixedFractionHom (mixedEquations f g) a F ≫
          subfamilyProd (mixedEquations f g) (Fin.natAddOrderEmb (d + 1) :
            Fin (d + 1) ↪o Fin ((d + 1) + (d + 1))) F d ≫
          prodTermCongr (mixedEquations_comp_natAdd f g) F d ≫
          cokernel.π (lastDif g F) =
        globalSmul a.det F ≫
          cokernel.π (equationsMultiplication g F) ≫ supportedFractionClass g F
```

## Tag 0G7T, a lemma

[Tag 0G7T](https://stacks.math.columbia.edu/tag/0G7T) in the Stacks Project.

**`Stacks.Perfect.ConormalClass.conormalTwistClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ConormalClass/Main.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ConormalClass/Main.lean#L103). The attribute's comment: “the canonical map, as a natural transformation of functors of the module F; its value on a chart is conormalTwistClass\_app\_tmul”.

> The canonical map `⋀^c(𝒞_{Z/X})^∨ ⊗_{𝒪_Z} i^*ℱ ⟶ ℋ^c_Z(ℱ)`, functorial in `ℱ`, for a closed
> immersion `i : Z ⟶ X` of finite presentation whose conormal sheaf `𝒞_{Z/X}` is finite locally
> free of rank `c`.  The source is `i_*` of the tensor product over `𝒪_Z` (Stacks 01CA) of the dual
> `SheafHom(⋀^c 𝒞_{Z/X}, 𝒪_Z)` of the `c`-th exterior power of the conormal sheaf with `i^*ℱ`, and
> the target is `ℋ^c_Z(ℱ)` read on `X`; the direct image along `i` is fully faithful, so this is the
> map of `𝒪_X|_Z`-modules of the statement.  On a chart it is the map of
> `conormalTwistClass_app_tmul`.

```lean
def conormalTwistClass :
    twistFunctor i c ⟶ supportCohomologySheafFunctor (isClosed_zeroLocus i) (c : ℤ)
```

**`Stacks.Perfect.ConormalClass.conormalTwistClass_app_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ConormalClass/Main.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/ConormalClass/Main.lean#L117). The attribute's comment: “canonicity: on every chart the map is the twisted fraction class of Stacks 0G7Q, λ ⊗ s ↦ c\_\{f₁, …, f\_c}(λ(f₁ ∧ ⋯ ∧ f\_c) s)”.

> The value of `conormalTwistClass` on a chart.  Let `W ⊆ X` be an open on which
> `f₁, …, f_c` generate the ideal sheaf of `Z`, let `U ⊆ W` be open, `λ` a local section of
> `(⋀^c 𝒞_{Z/X})^∨` over `Z ∩ U`, `s` a local section of `ℱ` over `U` and `r` a function on `U`
> restricting on `Z ∩ U` to `λ(f₁ ∧ ⋯ ∧ f_c)`.  Then `c(λ ⊗ s)`, read in `ℋ^c_{T}(ℱ)` for the
> closed subset `T ⊇ Z` of the chart (over `W` the change of support `ℋ^c_Z ⟶ ℋ^c_T` is an
> isomorphism), is the class `c_{f₁, …, f_c}(r s)` of the fraction `r s / (f₁ ⋯ f_c)` of
> Stacks 0G7Q.  In particular the map does not depend on the chart.

```lean
theorem conormalTwistClass_app_tmul {W : X.Opens} {f : Fin c → Γ(X, W)}
    (hgen : IsGeneratedByOn X.toRingedSpace (definingIdealOfHom i) W f) (U : X.Opens) (hU : U ≤ W)
    (lam : (dualSheaf Z.toRingedSpace (line i c)).val.obj (op (i ⁻¹ᵁ U))) (s : Γ(F, U))
    (r : Γ(X, U))
    (hr : (i.app U).hom r = dualEval Z.toRingedSpace (line i c) lam
      ((line i c).presheaf.map (homOfLE (i.preimage_mono hU)).op
        (wedge i f (app_chart_eq_zero W f hgen)))) :
    (supportChangeH (isClosed_zeroLocus i) (isClosed_chartSupport W (chartEq W f))
        (zeroLocus_subset_chartSupport W f hgen) F (c : ℤ)).app U
        (((conormalTwistClass i c).app F).app U
          (tensorObjTmul Z.toRingedSpace (dualModule (line i c)) ((Scheme.Modules.pullback i).obj F)
            (op (i ⁻¹ᵁ U)) lam
            (((Scheme.Modules.pullbackPushforwardAdjunction i).unit.app F).app U s))) =
      (topClass W F (isClosed_chartSupport W (chartEq W f)) (chartEq W f) subset_rfl).app U
        (r • s)
```

## Tag 0G7U, a remark

[Tag 0G7U](https://stacks.math.columbia.edu/tag/0G7U) in the Stacks Project.

**`Stacks.Perfect.CechBaseChangeCounterexample.isEmpty_iso_cplx`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechBaseChangeCounterexample.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechBaseChangeCounterexample.lean#L494). The attribute's comment: “refutes the note `(F')^• = g^*F^•` for a non-quasi-coherent `F`: for the diagonal `A^1 → A^2`, `f_1 = x` and `F` the extension by zero of `O` from `D(y)`, the two complexes are not isomorphic at all; the quasi-coherent form is `isIso_cplxBaseChange`”.

> **No isomorphism at all between the extended alternating Čech complexes**
> `g^*(ℱ^•)` and `(g^*ℱ)^•` of the counterexample: their degree-one terms are a single
> `g^*(j_*(ℱ|_U))`, resp. `j'_*((g^*ℱ)|_{U'})`, and these are not isomorphic
> (`isEmpty_iso_restrictedModule`).  This refutes the note `(ℱ')^• = g^*ℱ^•` of
> [Stacks, Tag 0G7U] for non-quasi-coherent `ℱ` in its strongest reading, with no comparison map
> fixed in advance.

```lean
theorem isEmpty_iso_cplx :
    IsEmpty (((Scheme.Modules.pullback (diag k)).mapHomologicalComplex (ComplexShape.up ℕ)).obj
        (cplx (eqns k) (coeff k)) ≅
      cplx (fun j => (diag k).appTop (eqns k j)) ((Scheme.Modules.pullback (diag k)).obj
        (coeff k)))
```

**`Stacks.Perfect.CechBaseChangeCounterexample.not_isIso_cplxBaseChange_f_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechBaseChangeCounterexample.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechBaseChangeCounterexample.lean#L511). The attribute's comment: “refutes the note `(F')^• = g^*F^•` for a non-quasi-coherent `F`: the comparison `cplxBaseChange` is not an isomorphism in degree 1 for the diagonal `A^1 → A^2`, `f_1 = x` and `F` the extension by zero of `O` from `D(y)`; the quasi-coherent form is `isIso_cplxBaseChange`”.

> **The base-change comparison of complexes of [Stacks, Tag 0G7U] is not an isomorphism for
> the non-quasi-coherent module `ℱ = coeff k`**, already in degree `1`.  Here `k` is any field,
> `g : 𝔸¹_k ⟶ 𝔸²_k` is the diagonal, the single equation is `x`, and `ℱ` is the sheaf of functions
> with vanishing germ at the generic point of the line `y = 0` (the extension by zero of `𝒪` from
> `D(y)`).  So the note `(ℱ')^• = g^*ℱ^•` of the remark, read through the comparison map
> `cplxBaseChange`, is false for an arbitrary `𝒪_X`-module; for quasi-coherent `ℱ` it holds
> (`Stacks.Perfect.CechBaseChange.isIso_cplxBaseChange`).

```lean
theorem not_isIso_cplxBaseChange_f_one :
    ¬ IsIso ((cplxBaseChange (diag k) (eqns k) (coeff k)).f 1)
```

**`Stacks.Perfect.CechDegreeCBaseChange.supportedFractionSource_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChange.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChange.lean#L302). The attribute's comment: “the first diagram of the remark: the class map c\_\{f\_1,...,f\_c} of Tag 0G7Q commutes with base change, for quasi-coherent F, read on X in i\_*H^c\_Z(F) -- the spelling supportedFractionSource, which is the one Tag 0G7Q is itself registered at in SupportedFractionMap. Its top horizontal arrow IS the map of Cohomology Remark 0G78 on cohomology sheaves in degree c, which the remark's own sentence asserts: that identification is degreeCBaseChange\_eq\_homology\_zeroG78 below, prefixed by the comparison the remark suppresses”.

> **The first diagram of [Stacks, Tag 0G7U]**: the class map `c_{f₁,…,f_c}` of
> [Stacks, Tag 0G7Q], read on the coefficient module and in `i_*ℋ^c_Z(ℱ)`, commutes with base
> change.  The inverse image of the class map for `f` and `ℱ`, followed by the degree-`c`
> comparison `degreeCBaseChange`, is the class map for the pulled-back equations `f'` and the
> inverse-image module `ℱ'`.
>
> Unfolding both class maps, the inverse of the identification of [Stacks, Tag 0G7M] sitting in
> `degreeCBaseChange` cancels against its occurrence in the class map, and what is left is the
> class of the fraction `s / (f₁ ⋯ f_c)`: the characterizing property of the preserved-cokernel
> comparison turns the inverse image of the class of a top-degree cochain into the class of its
> inverse image, and the remaining identity is the compatibility of the fraction with base change,
> `Stacks.Perfect.CechFractionBaseChange.cplxBaseChange_comp_fracTermTop`.

```lean
public theorem supportedFractionSource_baseChange [F.IsQuasicoherent] :
    (Scheme.Modules.pullback g).map
          (supportedFractionSource f F (isClosed_equationsClosedSet f) le_rfl) ≫
        degreeCBaseChange g f F =
      supportedFractionSource (fun j => g.appTop (f j)) ((Scheme.Modules.pullback g).obj F)
        (isClosed_equationsClosedSet (fun j => g.appTop (f j))) le_rfl
```

**`Stacks.Perfect.CechDegreeCBaseChange.degreeCBaseChange_eq_homology_zeroG78`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChange.lean, line 686](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChange.lean#L686). The attribute's comment: “the top horizontal arrow of the first diagram is the map of Cohomology Remark 0G78 on cohomology sheaves in degree c: the degree-c cohomology of the upper route of the derived diagram, preceded by the canonical comparison of H^c(Lg^*(-)) with g^*H^c(-) that the remark leaves implicit”.

> **The top arrow of the first diagram of [Stacks, Tag 0G7U] is the map of [Stacks, Tag 0G78]
> read on cohomology sheaves in degree `c`.**  This is what the remark asserts verbatim: the top
> horizontal arrow of its first diagram "is the map of Cohomology, Remark 0G78 on cohomology
> sheaves in degree `c`".
>
> The arrow of [Stacks, Tag 0G78] is the upper route
> `Stacks.Perfect.SupportedDerivedBaseChange.supportedPullbackRoute` of the remark's derived
> diagram — its left-hand equal sign followed by its top horizontal arrow — followed by
> `i'_* R𝓗_{Z'}` of the down arrow `Lg^*ℱ ⟶ ℱ'`; it is the whole left-to-right passage of the
> derived diagram above the Čech complexes, and it is the composite that stands to the left of
> `Lg^*` of the comparison of [Stacks, Tag 0G7L] in
> `Stacks.Perfect.CechDerivedBaseChange.derivedBaseChangeSquare_cech`.  Its degree-`c` cohomology
> starts at `ℋ^c(Lg^* i_* R𝓗_Z(ℱ))`, not at `g^*ℋ^c_Z(ℱ)` where `degreeCBaseChange` starts, so the
> canonical comparison `derivedPullbackDegreeCComparison` of the two is prefixed; and it ends at
> `i'_*ℋ^c_{Z'}(ℱ')` spelled at the preimage `g^{-1}(Z)`, so the identification
> `supportCohomologySheafPullbackIso` of the two spellings of `Z'` is appended.
>
> The proof is the source's own: take the degree-`c` cohomology of the derived diagram
> `derivedBaseChangeSquare_cech`, and cancel `ℋ^c(Lg^*(ℱ^• ⟶ i_* R𝓗_Z(ℱ)))`, which is invertible
> because the comparison of [Stacks, Tag 0G7L] is ([Stacks, Tag 0G7M], as
> `Stacks.Perfect.SupportedFraction.isIso_cechToSupport`).  What is left on the other side is
> `ℋ^c` of the lower horizontal arrow `Lg^*(ℱ^•) ⟶ (ℱ')^•` followed by `ℋ^c` of the comparison of
> [Stacks, Tag 0G7L] for `f'` and `ℱ'`, and that is `cokernelLastDifBaseChange` followed by the
> identification of [Stacks, Tag 0G7M] — which is `degreeCBaseChange` — by
> `homologyMap_extendBaseChange`.

```lean
public theorem degreeCBaseChange_eq_homology_zeroG78 [F.IsQuasicoherent] :
    derivedPullbackDegreeCComparison g f F ≫ degreeCBaseChange g f F =
      (DerivedCategory.homologyFunctor X'.Modules ((d + 1 : ℕ) : ℤ)).map
          (supportedPullbackRoute g.toLRSHom.toShHom (equationsClosedSet f)
              (isClosed_equationsClosedSet f)
              ((DerivedCategory.singleFunctor X.Modules 0).obj F) ≫
            (supportPush (isClosed_equationsClosedSet_pullback g f)).map
              (derivedPullbackSingleObj g.toLRSHom.toShHom F)) ≫
        (supportCohomologySheafPullbackIso g f F).hom
```

**`Stacks.Perfect.CechDegreeCBaseChange.fractionClassTrans_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChange.lean, line 922](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChange.lean#L922). The attribute's comment: “the first diagram of the remark with all four arrows, for quasi-coherent F: the components of the Tag 0G7Q transformation c\_\{f\_1,...,f\_c} at F and at F' = g^*F on the quotients i\_*i^*F = F/(f\_1,...,f\_c)F, the comparison of the two quotients as bottom arrow, and the degree-c comparison (the Tag 0G78 map in degree c) as top arrow; read on X' along the fully faithful i'\_*”.

> **The first diagram of [Stacks, Tag 0G7U], with all four of its arrows**, read on `X'` along
> the fully faithful direct image `i'_*` along the inclusion of `Z'`: for a quasi-coherent
> `𝒪_X`-module `ℱ` the square
>
> ```
> g^*(i_*ℋ^c_Z(ℱ))  --degreeCBaseChange-->  i'_*ℋ^c_{Z'}(ℱ')
>       ^                                          ^
>  g^*(c_{f₁,…,f_c})                         c_{f'₁,…,f'_c}
>       |                                          |
> g^*(i_*i^*ℱ)  --equationsQuotientBaseChange-->  i'_*(i')^*ℱ'
> ```
>
> commutes, where the vertical arrows are the components at `ℱ` and at `ℱ' = g^*ℱ` of the natural
> transformation `Stacks.Perfect.SupportedFraction.fractionClassTrans` that [Stacks, Tag 0G7Q] is
> registered at — `c_{f₁,…,f_c}` read on `X` along the fully faithful `i_*`, with source the
> quotient `ℱ/(f₁, …, f_c)ℱ = i_*i^*ℱ` that the remark presents it on — the bottom arrow is the
> comparison of the two quotients, and the top arrow is the degree-`c` comparison, which is the map
> of Cohomology, Remark 0G78 on cohomology sheaves in degree `c` by
> `degreeCBaseChange_eq_homology_zeroG78`.
>
> **Why this is the remark's diagram.**  The remark's diagram lives on `Z'`, with corners
> `h^*i^*ℱ`, `(i')^*ℱ'`, `(i')^{-1}𝒪_{X'} ⊗_{h^{-1}i^{-1}𝒪_X} h^{-1}ℋ^c_Z(ℱ) = h^*ℋ^c_Z(ℱ)` and
> `ℋ^c_{Z'}(ℱ')`.  Applying the fully faithful `i'_*` does not change whether it commutes, and
> `i'_*h^* = g^*i_*` for the cartesian square `Z' = Z ×_X X'` of the setting
> (`AlgebraicGeometry.ExtendedAlternatingCech.isPullback_equationsClosedSubscheme`) carries its
> left-hand corners to `g^*(i_*i^*ℱ)` and `g^*(i_*ℋ^c_Z(ℱ))`; this is the form in which the library
> states the class map of [Stacks, Tag 0G7Q] itself.
>
> The proof cancels the epimorphism `g^*` of the projection `ℱ ⟶ i_*i^*ℱ` and is then
> `supportedFractionSource_baseChange`.

```lean
public theorem fractionClassTrans_baseChange [F.IsQuasicoherent] :
    (Scheme.Modules.pullback g).map ((fractionClassTrans f).app F) ≫
        degreeCBaseChange g f F =
      equationsQuotientBaseChange g f F ≫
        (fractionClassTrans (fun j => g.appTop (f j))).app
          ((Scheme.Modules.pullback g).obj F)
```

**`Stacks.Perfect.CechDegreeCBaseChangeOnClosed.fractionClassOnClosed_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChangeOnClosed.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDegreeCBaseChangeOnClosed.lean#L344). The attribute's comment: “the first diagram of the remark on the closed subscheme Z', for quasi-coherent F: h^*c\_\{f\_1,...,f\_c} followed by the top arrow h^*H^c\_Z(F) -> H^c\_\{Z'}(F') equals the canonical h^*i^*F -> (i')^*F' followed by c\_\{f'\_1,...,f'\_c}, with c the Tag 0G7Q map on the closed subset”.

> **[Stacks, Tag 0G7U], the first diagram, on the closed subscheme `Z'`.**  Let `g : X' ⟶ X` be
> a morphism of schemes, `f₁, …, f_c ∈ Γ(X, 𝒪_X)`, `f'ⱼ = g^♯(fⱼ)`, `Z ⊆ X` and `Z' ⊆ X'` the
> closed subsets cut out by them, made into ringed spaces `(Z, i^{-1}𝒪_X)` and
> `(Z', (i')^{-1}𝒪_{X'})`, and `h : Z' ⟶ Z` the induced morphism (`closedRestriction`).  For a
> quasi-coherent `𝒪_X`-module `ℱ`, with `ℱ' = g^*ℱ`, the diagram
>
> ```
> h^*ℋ^c_Z(ℱ)   --topArrow-->   ℋ^c_{Z'}(ℱ')
>      ^                              ^
> h^*c_{f₁,…,f_c}               c_{f'₁,…,f'_c}
>      |                              |
> h^*i^*ℱ      --bottomArrow-->   (i')^*ℱ'
> ```
>
> commutes.  Here `c_{f₁,…,f_c}` and `c_{f'₁,…,f'_c}` are the components at `ℱ` and at `ℱ'` of
> `Stacks.Perfect.GysinLocalCohomology.fractionClassOnClosed`, the map of [Stacks, Tag 0G7Q] on the
> closed subset, with source the remark's presentation `i^*(ℱ/(f₁, …, f_c)ℱ)` of `i^*ℱ`; the
> left-hand top corner is `h^*ℋ^c_Z(ℱ) = (i')^{-1}𝒪_{X'} ⊗_{h^{-1}i^{-1}𝒪_X} h^{-1}ℋ^c_Z(ℱ)`, the
> inverse image of modules along the morphism of ringed spaces `h`; the bottom arrow is the
> canonical comparison `h^*i^*ℱ ≅ (i')^*g^*ℱ = (i')^*ℱ'`; and the top arrow is the one determined by
> the degree-`c` comparison `degreeCBaseChange`, which is the map of Cohomology, Remark 0G78 on
> cohomology sheaves in degree `c`
> (`Stacks.Perfect.CechDegreeCBaseChange.degreeCBaseChange_eq_homology_zeroG78`).
>
> The proof is the remark's: the diagram read on `X'` is
> `Stacks.Perfect.CechDegreeCBaseChange.fractionClassTrans_baseChange`, and `comp_transposeTop`
> descends it to `Z'`, the comparison of inverse images being conjugate to the comparison of direct
> images by `Stacks.Cohomology.conjugateEquiv_pullbackCompSquare`.

```lean
theorem fractionClassOnClosed_baseChange [F.IsQuasicoherent] :
    (modulePullback (closedRestriction g f)).map ((fractionClassOnClosed f).app F) ≫
        topArrow g f F =
      bottomArrow g f F ≫
        (fractionClassOnClosed (fun j => g.appTop (f j))).app
          ((Scheme.Modules.pullback g).obj F)
```

**`Stacks.Perfect.CechDerivedBaseChange.derivedBaseChangeSquare_cech`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDerivedBaseChange.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/CechDerivedBaseChange.lean#L375). The attribute's comment: “the derived diagram of the remark, with the remark's own lower horizontal arrow Lg^*F^bullet -> g^*F^bullet -> (F')^bullet and its own down arrow induced by Lg^*F -> g^*F = F', for an arbitrary O\_X-module F”.

> **The derived diagram of [Stacks, Tag 0G7U] commutes**, for the lower horizontal arrow and
> the down arrow the remark itself writes down.  This is
> `Stacks.Perfect.SupportedDerivedBaseChange.derivedBaseChangeSquare` instantiated at
> `cechDerivedBaseChange` and `AlgebraicGeometry.RingedSpaceThickening.derivedPullbackSingleObj`,
> whose compatibility with the augmentations of [Stacks, Tag 0G7L] is
> `cechDerivedBaseChange_comp_augmentation`.

```lean
public theorem derivedBaseChangeSquare_cech :
    (derivedPullback g.toLRSHom.toShHom).map
          (cechToDerivedSupport f F (isClosed_equationsClosedSet f) le_rfl) ≫
        supportedPullbackRoute g.toLRSHom.toShHom (equationsClosedSet f)
            (isClosed_equationsClosedSet f)
            ((DerivedCategory.singleFunctor X.Modules 0).obj F) ≫
        (supportPush (isClosed_equationsClosedSet_pullback g f)).map
          (derivedPullbackSingleObj g.toLRSHom.toShHom F) =
      cechDerivedBaseChange g f F ≫
        cechToDerivedSupport (fun j => g.appTop (f j)) ((Scheme.Modules.pullback g).obj F)
          (isClosed_equationsClosedSet_pullback g f) (equationsClosedSet_pullback_subset g f)
```

**`AlgebraicGeometry.ExtendedAlternatingCech.isPullback_equationsClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/EquationsBaseChange.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/EquationsBaseChange.lean#L276). The attribute's comment: “Z' = Z ×\_X X' of the setting, as a pullback square of schemes”.

> **Stacks Project, Tag 0G7U**, the assertion `Z' = Z ×_X X'` of the setting: the closed
> subscheme cut out by the pulled-back equations `f'ᵢ = g^♯(fᵢ)` is the base change along `g` of
> the closed subscheme cut out by `f₁, …, f_c`, the induced morphism of schemes being
> `equationsClosedSubschemeBaseChange`.
>
> The set-theoretic form of the same assertion, which is the shape [Stacks, Tag 0G78] and hence
> the remark's diagrams are stated at, is
> `Stacks.Perfect.SupportedDerivedBaseChange.equationsClosedSet_pullback`.

```lean
public theorem isPullback_equationsClosedSubscheme :
    IsPullback (equationsClosedSubschemeι (fun j => g.appTop (f j)))
      (equationsClosedSubschemeBaseChange g f) g (equationsClosedSubschemeι f)
```

**`AlgebraicGeometry.ExtendedAlternatingCech.equationsClosedSubschemePullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/EquationsBaseChange.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/EquationsBaseChange.lean#L291). The attribute's comment: “the identification Z' ≅ Z ×\_X X' of the setting”.

> **Stacks Project, Tag 0G7U**, the identification `Z' = Z ×_X X'` of the setting, as an
> isomorphism of schemes.

```lean
public def equationsClosedSubschemePullbackIso :
    equationsClosedSubscheme (fun j => g.appTop (f j)) ≅
      pullback g (equationsClosedSubschemeι f)
```

**`Stacks.Perfect.CechBaseChange.isIso_cplxBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/OpenDirectImagePullback.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/SupportClosedSubset/OpenDirectImagePullback.lean#L174). The attribute's comment: “the note `(F')^• = g^*F^•`, corrected to quasi-coherent `F` and read through the comparison map; for an arbitrary `F` it is false, see `CechBaseChangeCounterexample.not_isIso_cplxBaseChange_f_one`”.

> **The comparison of the two extended alternating Čech complexes is an isomorphism for
> quasi-coherent `ℱ`.** This is the corrected form of the note `(ℱ')^• = g^*ℱ^•` of
> [Stacks, Tag 0G7U], as an isomorphism of complexes rather than only a morphism — which is what
> the remark's first diagram needs, and what lets its top arrow be identified with the
> [Stacks, Tag 0G78] map in degree `c` rather than with a Čech-level comparison.
>
> The remark states the note for an arbitrary `𝒪_X`-module `ℱ`, and in that generality it is
> false: `Stacks.Perfect.CechBaseChangeCounterexample.not_isIso_cplxBaseChange_f_one` takes `k` a
> field, `g : 𝔸¹_k ⟶ 𝔸²_k` the diagonal, the single equation `x`, and `ℱ` the extension by zero
> of `𝒪` from `D(y)`, and shows that this comparison is not an isomorphism in degree `1`
> (`Stacks.Perfect.CechBaseChangeCounterexample.isEmpty_iso_cplx`: the two complexes are not
> isomorphic by any isomorphism).  The quasi-coherence hypothesis is therefore needed here; it is
> the hypothesis under which the remark's first diagram is asserted.
>
> A morphism of complexes is invertible as soon as every component is
> (`HomologicalComplex.Hom.isIso_of_components`); here the degree-`0` component is the identity and
> the rest is `isIso_prodTermBaseChange`. No flatness on `g`.

```lean
public theorem isIso_cplxBaseChange (F : X.Modules) [F.IsQuasicoherent] :
    IsIso (cplxBaseChange g f F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.6, Tag 0G7F](https://stacks.math.columbia.edu/tag/0G7F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
