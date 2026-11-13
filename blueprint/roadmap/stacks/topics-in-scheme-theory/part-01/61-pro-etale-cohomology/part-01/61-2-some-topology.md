---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.clopen_refinement_iff_closedPoints_bijective, AlgebraicGeometry.ProEtale.exists_finite_disjoint_clopen_refinement_of_unique_closed_specialization, AlgebraicGeometry.ProEtale.closedPoints_to_connectedComponents_bijective_of_unique_specialization, AlgebraicGeometry.ProEtale.WLocalSpace, AlgebraicGeometry.ProEtale.IsWLocalMap, AlgebraicGeometry.ProEtale.wLocalSpace_of_isClosed, AlgebraicGeometry.ProEtale.spectralSpace_pullback, AlgebraicGeometry.ProEtale.isHomeomorph_connectedComponentsLift_toT
statement: formalized
proof: formalized
---

# 61.2 Some topology

Section 61.2 of the Stacks Project, [Tag 0967](https://stacks.math.columbia.edu/tag/0967). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0968, a lemma

[Tag 0968](https://stacks.math.columbia.edu/tag/0968) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.clopen_refinement_iff_closedPoints_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ClopenRefinement.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ClopenRefinement.lean#L71). The attribute's comment: “clopen\_refinement\_equivalence”.

> **Stacks Project, Tag 0968.** For a spectral space, every open cover has a finite pairwise
> disjoint clopen refinement if and only if the canonical map from its closed points to its
> connected components is bijective.

```lean
theorem clopen_refinement_iff_closedPoints_bijective
    (X : Type*) [TopologicalSpace X] [SpectralSpace X] :
    (∀ {ι : Type*} (U : ι → Opens X), IsOpenCover U →
      ∃ (n : ℕ) (W : Fin n → Clopens X),
        (∀ j, ∃ i, (W j : Set X) ⊆ U i) ∧
        (Set.univ : Set X) ⊆ ⋃ j, (W j : Set X) ∧
        Pairwise (Disjoint on W)) ↔
    Function.Bijective (fun x : closedPoints X => (x.1 : ConnectedComponents X))
```

**`AlgebraicGeometry.ProEtale.exists_finite_disjoint_clopen_refinement_of_unique_closed_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ClopenRefinement.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ClopenRefinement.lean#L255). The attribute's comment: “unique\_specialization\_refinement”.

> **Stacks 0968, unique-specialization refinement.** If the closed points of a spectral space
> form a closed subset and every point specializes to a unique closed point, every open cover has a
> finite refinement by pairwise-disjoint clopen subsets.

```lean
theorem exists_finite_disjoint_clopen_refinement_of_unique_closed_specialization
    {ι X : Type*} [TopologicalSpace X] [SpectralSpace X]
    (hclosed : IsClosed (closedPoints X))
    (hunique : ∀ x : X, ∃! x₀ : closedPoints X, Specializes x x₀.1)
    {U : ι → Opens X} (hU : IsOpenCover U) :
    ∃ (n : ℕ) (W : Fin n → Clopens X),
      (∀ j, ∃ i, (W j : Set X) ⊆ U i) ∧
      (Set.univ : Set X) ⊆ ⋃ j, (W j : Set X) ∧
      Pairwise (Disjoint on W)
```

**`AlgebraicGeometry.ProEtale.closedPoints_to_connectedComponents_bijective_of_unique_specialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ClopenRefinement.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ClopenRefinement.lean#L271). The attribute's comment: “unique\_specialization\_refinement”.

> **Stacks 0968, unique-specialization refinement.** Under the same hypotheses, sending a
> closed point to its connected component is a bijection from the closed points of `X` to
> `π₀(X)`.

```lean
theorem closedPoints_to_connectedComponents_bijective_of_unique_specialization
    {X : Type*} [TopologicalSpace X] [SpectralSpace X]
    (hclosed : IsClosed (closedPoints X))
    (hunique : ∀ x : X, ∃! x₀ : closedPoints X, Specializes x x₀.1) :
    Function.Bijective
      (fun x₀ : closedPoints X ↦ ConnectedComponents.mk x₀.1)
```

## Tag 096A, a definition

[Tag 096A](https://stacks.math.columbia.edu/tag/096A) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.WLocalSpace`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Basic.lean#L63). The attribute's comment: “w-local spaces”.

> A spectral space is w-local if its closed points form a closed subset and every point has a
> unique closed specialization. Existence of a closed specialization is automatic for spectral
> spaces, so the class records its uniqueness.

```lean
class WLocalSpace (X : Type*) [TopologicalSpace X] : Prop extends SpectralSpace X
```

**`AlgebraicGeometry.ProEtale.IsWLocalMap`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Basic.lean#L84). The attribute's comment: “w-local maps”.

> A map is w-local if it is spectral and sends every closed point to a closed point.

```lean
structure IsWLocalMap {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y]
    (f : X → Y) : Prop extends IsSpectralMap f
```

## Tag 096B, a lemma

[Tag 096B](https://stacks.math.columbia.edu/tag/096B) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.wLocalSpace_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Basic.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/Basic.lean#L111).

> A closed subspace of a w-local space is w-local.

```lean
theorem wLocalSpace_of_isClosed {X : Type*} [TopologicalSpace X] [WLocalSpace X]
    {Y : Set X} (hY : IsClosed Y) : WLocalSpace Y
```

## Tag 096C, a lemma

[Tag 096C](https://stacks.math.columbia.edu/tag/096C) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.spectralSpace_pullback`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteBaseChange.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteBaseChange.lean#L117). The attribute's comment: “pullback\_spectral”.

> A profinite base change of the component map of a spectral space is spectral.

```lean
instance spectralSpace_pullback (S : ProfiniteBaseChangeOfComponentMap) :
    SpectralSpace S.Y
```

**`AlgebraicGeometry.ProEtale.isHomeomorph_connectedComponentsLift_toT`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteBaseChange.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/ProfiniteBaseChange.lean#L157). The attribute's comment: “pullback\_components”.

> The canonical map `π₀(Y) → T` induced by the pullback projection is a
> homeomorphism.

```lean
theorem isHomeomorph_connectedComponentsLift_toT
    (S : ProfiniteBaseChangeOfComponentMap.{u}) :
    IsHomeomorph S.toT.hom.continuous.connectedComponentsLift
```

**`AlgebraicGeometry.ProEtale.closedPoints_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/PullbackClosedPoints.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/PullbackClosedPoints.lean#L94). The attribute's comment: “pullback\_closed\_points”.

> Closed points in the profinite pullback of a w-local space are precisely those lying
> over closed points of the original space.

```lean
theorem closedPoints_pullback (S : ProfiniteBaseChangeOfComponentMap.{u})
    [WLocalSpace S.X] :
    closedPoints S.Y = S.toX ⁻¹' closedPoints S.X
```

**`AlgebraicGeometry.ProEtale.wLocalSpace_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/PullbackWLocal.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/PullbackWLocal.lean#L46). The attribute's comment: “pullback\_w\_local”.

> A profinite base change of the component map of a w-local space is w-local.

```lean
theorem wLocalSpace_pullback (S : ProfiniteBaseChangeOfComponentMap.{u})
    [WLocalSpace S.X] : WLocalSpace S.Y
```

**`AlgebraicGeometry.ProEtale.toX_isWLocalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/PullbackWLocal.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WLocal/PullbackWLocal.lean#L107). The attribute's comment: “pullback\_projection\_w\_local”.

> The projection to a w-local space from its profinite base change over the space of
> connected components is a w-local map.

```lean
theorem toX_isWLocalMap (S : ProfiniteBaseChangeOfComponentMap.{u})
    [WLocalSpace S.X] : IsWLocalMap S.toX
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.2, Tag 0967](https://stacks.math.columbia.edu/tag/0967)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
