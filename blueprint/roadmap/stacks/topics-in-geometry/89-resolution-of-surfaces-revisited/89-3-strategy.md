---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ClosedPointNeighborhoods.modificationsAwayFromPoints, AlgebraicGeometry.Space.ClosedPointNeighborhoods.modificationsAt, AlgebraicGeometry.Space.ClosedPointNeighborhoods.restrictionFunctor, AlgebraicGeometry.Space.ClosedPointNeighborhoods.restrictionFunctorCompιIso, AlgebraicGeometry.Space.ClosedPointNeighborhoods.isEquivalence_restrictionFunctor, AlgebraicGeometry.Space.ClosedPointNeighborhoods.essSurj_restrictionFunctor_of_essSurj, AlgebraicGeometry.Space.ClosedPointNeighborhoods.isQuasiCompact_iff_forall_restrictionComponent, AlgebraicGeometry.Space.ClosedPointNeighborhoods.isQuasiSeparated_iff_forall_restrictionComponent
statement: formalized
proof: formalized
---

# 89.3 Strategy

Section 89.3 of the Stacks Project, [Tag 0BH9](https://stacks.math.columbia.edu/tag/0BH9). 4 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BHA, an equation

[Tag 0BHA](https://stacks.math.columbia.edu/tag/0BHA) in the Stacks Project.

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.modificationsAwayFromPoints`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean#L274). The attribute's comment: “the source category of the functor”.

> **Stacks 0BHA.** The category `C_{X, {x₁, …, xₙ}}` of algebraic spaces over `X` which are
> unchanged over `X ∖ {x₁, …, xₙ}`.

```lean
abbrev modificationsAwayFromPoints
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.modificationsAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean#L279). The attribute's comment: “the factors of the target category of the functor”.

> **Stacks 0BHA.** The category `C_{Uᵢ, uᵢ}` of algebraic spaces over the `i`th neighborhood
> which are unchanged over `Uᵢ ∖ {uᵢ}`.

```lean
abbrev modificationsAt (i : Fin n)
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.restrictionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean#L300). The attribute's comment: “the functor given by base change”.

> **Stacks 0BHA.** The functor `F : C_{X, {x₁, …, xₙ}} ⟶ C_{U₁, u₁} × … × C_{Uₙ, uₙ}` given by
> base change along the chosen elementary étale neighborhoods.

```lean
def restrictionFunctor :
    D.modificationsAwayFromPoints ⥤ ∀ i : Fin n, D.modificationsAt i
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.restrictionFunctorCompιIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPoints.lean#L306). The attribute's comment: “base change computes the functor”.

> **Stacks 0BHA.** The `i`th component of `F` is base change along `Uᵢ ⟶ X`.

```lean
def restrictionFunctorCompιIso (i : Fin n) :
    D.restrictionFunctor ⋙ Pi.eval _ i ⋙
        ObjectProperty.ι (IsModification B S hS (D.openAwayFromPoint i)) ≅
      ObjectProperty.ι (IsModification B S hS D.openAwayFromPoints) ⋙
        Over.pullback (D.toSpaceHom i).hom
```

## Tag 0BHB, a lemma

[Tag 0BHB](https://stacks.math.columbia.edu/tag/0BHB) in the Stacks Project.

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isEquivalence_restrictionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionEssSurj.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationExcisionEssSurj.lean#L97).

> **Stacks 0BHB.** The functor `F` of Stacks 0BHA, base change of the modifications of `X`
> away from the chosen closed points to the chosen elementary étale neighborhoods, is an
> equivalence of categories.

```lean
theorem isEquivalence_restrictionFunctor : D.restrictionFunctor.IsEquivalence
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.essSurj_restrictionFunctor_of_essSurj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsSinglePoint.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsSinglePoint.lean#L152). The attribute's comment: “essential surjectivity of the functor, granted the case n = 1 of Stacks 0BGY”.

> **Stacks 0BHB**, the essential surjectivity of `F`, granted the case `n = 1`. If the
> base-change functor of Stacks 0BGY along `Uᵢ ⟶ X`, taken outside `X ∖ {xᵢ}`, is essentially
> surjective for every `i`, then the functor `F` of Stacks 0BHA is essentially surjective.

```lean
theorem essSurj_restrictionFunctor_of_essSurj
    (hES : ∀ i : Fin n,
      (baseChangeFunctor B S hS (D.toSpaceHom i) (D.openAwayFromSinglePoint i)).1.EssSurj) :
    D.restrictionFunctor.EssSurj
```

## Tag 0BHC, a lemma

[Tag 0BHC](https://stacks.math.columbia.edu/tag/0BHC) in the Stacks Project.

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isQuasiCompact_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L379). The attribute's comment: “quasi-compactness”.

> **Stacks 0BHC, quasi-compactness.** A modification of `X` away from `{x₁, …, xₙ}` is
> quasi-compact exactly when each of its restrictions under the functor `F` of Stacks 0BHA is.

```lean
theorem isQuasiCompact_iff_forall_restrictionComponent :
    IsQuasiCompact B S hS M.obj.hom ↔
      ∀ i, IsQuasiCompact B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isQuasiSeparated_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 402](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L402). The attribute's comment: “quasi-separatedness”.

> **Stacks 0BHC, quasi-separatedness.** A modification of `X` away from `{x₁, …, xₙ}` is
> quasi-separated exactly when each of its restrictions under the functor `F` of Stacks 0BHA
> is.

```lean
theorem isQuasiSeparated_iff_forall_restrictionComponent :
    IsQuasiSeparated B S hS M.obj.hom ↔
      ∀ i, IsQuasiSeparated B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isSeparated_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L425). The attribute's comment: “separatedness”.

> **Stacks 0BHC, separatedness.** A modification of `X` away from `{x₁, …, xₙ}` is separated
> exactly when each of its restrictions under the functor `F` of Stacks 0BHA is.

```lean
theorem isSeparated_iff_forall_restrictionComponent :
    IsSeparated B S hS M.obj.hom ↔
      ∀ i, IsSeparated B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isLocallyOfFinitePresentation_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L453). The attribute's comment: “local finite presentation”.

> **Stacks 0BHC, local finite presentation.** A modification of `X` away from `{x₁, …, xₙ}`
> is locally of finite presentation exactly when each of its restrictions under the functor `F`
> of Stacks 0BHA is.

```lean
theorem isLocallyOfFinitePresentation_iff_forall_restrictionComponent :
    IsLocallyOfFinitePresentation B S hS M.obj.hom ↔
      ∀ i, IsLocallyOfFinitePresentation B S hS
        ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isLocallyOfFiniteType_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L485). The attribute's comment: “local finite type”.

> **Stacks 0BHC, local finite type.** A modification of `X` away from `{x₁, …, xₙ}` is
> locally of finite type exactly when each of its restrictions under the functor `F` of
> Stacks 0BHA is.

```lean
theorem isLocallyOfFiniteType_iff_forall_restrictionComponent :
    IsLocallyOfFiniteType B S hS M.obj.hom ↔
      ∀ i, IsLocallyOfFiniteType B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isFiniteType_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L517). The attribute's comment: “finite type”.

> **Stacks 0BHC, finite type.** A modification of `X` away from `{x₁, …, xₙ}` is of finite
> type exactly when each of its restrictions under the functor `F` of Stacks 0BHA is.

```lean
theorem isFiniteType_iff_forall_restrictionComponent :
    IsFiniteType B S hS M.obj.hom ↔
      ∀ i, IsFiniteType B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isFinitePresentation_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L529). The attribute's comment: “finite presentation”.

> **Stacks 0BHC, finite presentation.** A modification of `X` away from `{x₁, …, xₙ}` is of
> finite presentation exactly when each of its restrictions under the functor `F` of
> Stacks 0BHA is.

```lean
theorem isFinitePresentation_iff_forall_restrictionComponent :
    IsFinitePresentation B S hS M.obj.hom ↔
      ∀ i, IsFinitePresentation B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isProper_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L542). The attribute's comment: “properness”.

> **Stacks 0BHC, properness.** A modification of `X` away from `{x₁, …, xₙ}` is proper
> exactly when each of its restrictions under the functor `F` of Stacks 0BHA is.

```lean
theorem isProper_iff_forall_restrictionComponent :
    IsProper B S hS M.obj.hom ↔
      ∀ i, IsProper B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isIntegralHom_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L564). The attribute's comment: “integrality”.

> **Stacks 0BHC, integrality.** A modification of `X` away from `{x₁, …, xₙ}` is integral
> exactly when each of its restrictions under the functor `F` of Stacks 0BHA is.

```lean
theorem isIntegralHom_iff_forall_restrictionComponent :
    IsIntegralHom B S hS M.obj.hom ↔
      ∀ i, IsIntegralHom B S hS ((D.restrictionComponent i).obj M).obj.hom
```

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.isFinite_iff_forall_restrictionComponent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L582). The attribute's comment: “finiteness”.

> **Stacks 0BHC, finiteness.** A modification of `X` away from `{x₁, …, xₙ}` is finite
> exactly when each of its restrictions under the functor `F` of Stacks 0BHA is.

```lean
theorem isFinite_iff_forall_restrictionComponent :
    IsFinite B S hS M.obj.hom ↔
      ∀ i, IsFinite B S hS ((D.restrictionComponent i).obj M).obj.hom
```

## Tag 0BHD, a lemma

[Tag 0BHD](https://stacks.math.columbia.edu/tag/0BHD) in the Stacks Project.

**`AlgebraicGeometry.Space.ClosedPointNeighborhoods.fibreAtPointIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationsAtClosedPointsProperties.lean#L222). The attribute's comment: “the fibres agree”.

> **Stacks 0BHD.** If `f : Y ⟶ X` corresponds to `gᵢ : Yᵢ ⟶ Uᵢ` under the functor `F` of
> Stacks 0BHA, then `Y_{xᵢ} ≅ (Yᵢ)_{uᵢ}` as algebraic spaces: both are the fibre product of `f`
> with the monomorphism `Spec κ(uᵢ) ⟶ X`.

```lean
def fibreAtPointIso (M : D.modificationsAwayFromPoints) (i : Fin n) :
    fibreAtPoint M i ≅ fibreAtNeighborhoodPoint M i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.3, Tag 0BH9](https://stacks.math.columbia.edu/tag/0BH9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
