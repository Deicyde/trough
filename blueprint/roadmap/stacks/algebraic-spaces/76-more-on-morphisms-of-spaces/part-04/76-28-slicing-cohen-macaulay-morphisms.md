---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isOpenSubspace_isFlat_vanishingSubfunctor_of_isRegular_geometricFiber, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_vanishingSubfunctor_comp, AlgebraicGeometry.Space.exists_openSubspace_isFlat_isLocallyOfFinitePresentation_vanishingSubfunctor
statement: formalized
proof: formalized
---

# 76.28 Slicing Cohen-Macaulay morphisms

Section 76.28 of the Stacks Project, [Tag 06LV](https://stacks.math.columbia.edu/tag/06LV). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06LW, a lemma

[Tag 06LW](https://stacks.math.columbia.edu/tag/06LW) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isFlat_vanishingSubfunctor_of_isRegular_geometricFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSliceFlatnessEnlargement.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FibreSliceFlatnessEnlargement.lean#L117). The attribute's comment: “the flatness half of the conclusion”.

> **Stacks 06LW, the flatness half of the conclusion.**  Let `g : X ⟶ Y` be a morphism of
> algebraic spaces over `S` which is flat and locally of finite presentation, let
> `f₁, …, f_r ∈ Γ(X, 𝒪_X)`, let `Spec k ⟶ Y` be a field-valued point of the target, let
> `ξ : F ⟶ X` and `π : F ⟶ Spec k` present `F` as the fibre `X ×_Y Spec k` and let `z` be a
> geometric point of `F` at which the images of the `f_i` in the étale local ring `𝒪_{F, z̄}` form
> a regular sequence.
>
> Then there is an open subspace `W ⊆ X` containing the image of `z` such that
> `V(f₁, …, f_r) ∩ W ⟶ Y` is flat.
>
> The hypothesis is taken in the form the source's conclusion is used in — quantified over the
> small étale neighbourhoods of the image of `z` in `X` — which is the same condition for one
> neighbourhood as for all, the image of a germ of a global function under the comparison
> homomorphism of Stacks 04NG not depending on the neighbourhood.  It is the form in which
> Stacks 06MD states it, `AlgebraicGeometry.Stack.FibreIsRegularSequenceAt`.

```lean
theorem exists_isOpenSubspace_isFlat_vanishingSubfunctor_of_isRegular_geometricFiber
    (X Y F : AlgebraicSpaces B S hS) (g : X.1 ⟶ Y.1)
    (hgflat : IsFlat B S hS g) (hglfp : IsLocallyOfFinitePresentation B S hS g)
    {r : ℕ} (fs : Fin r → (SheafOfModules.unit (structureRingSheaf B S hS X)).sections)
    {k : Type u} [Field k] (hk : B.Contains (Spec (.of k))) (b : Spec (.of k) ⟶ S)
    (t : yoneda.obj (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS)) ⟶ Y.1)
    (ξ : F ⟶ X) {π : F.1 ⟶ yoneda.obj (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS))}
    (sq : IsPullback ξ.hom π g t)
    (z : GeometricPoint B S hS F.1)
    (hreg : ∀ Nx : SmallEtaleNeighborhood (geometricPointMap ξ.hom z),
      RingTheory.Sequence.IsRegular (etaleLocalRing B S hS F.1 z)
        (List.ofFn fun i : Fin r => etaleLocalRingMap F.2 ξ.hom z
          (etaleLocalRingGerm B S hS X.1 (geometricPointMap ξ.hom z) (op Nx)
            ((fs i).eval (op Nx.chart))))) :
    ∃ (W : Subfunctor X.1) (_ : IsOpenSubspace B S hS W),
      pointsMap B S hS F.1 ξ.hom z.image ∈
          Set.range (pointsMap B S hS W.toFunctor W.ι) ∧
        IsFlat B S hS (((vanishingSubfunctor B S hS X fs).preimage W.ι).ι ≫ W.ι ≫ g)
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_vanishingSubfunctor_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulaySlice.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulaySlice.lean#L229). The attribute's comment: “locally of finite presentation, given it for V(f₁,…,f\_r) ⟶ X”.

> If `X ⟶ Y` is locally of finite presentation and the closed immersion of the subspace
> `V(f₁, …, f_r) ⊆ X` cut out by global regular functions `f₁, …, f_r` is locally of finite
> presentation, then so is `V(f₁, …, f_r) ⟶ Y`.

```lean
theorem isLocallyOfFinitePresentation_vanishingSubfunctor_comp (X Y : AlgebraicSpaces B S hS)
    (g : X.1 ⟶ Y.1) {r : ℕ}
    (f : Fin r → (SheafOfModules.unit (structureRingSheaf B S hS X)).sections)
    (hslice : IsLocallyOfFinitePresentation B S hS (vanishingSubfunctor B S hS X f).ι)
    (hg : IsLocallyOfFinitePresentation B S hS g) :
    IsLocallyOfFinitePresentation B S hS ((vanishingSubfunctor B S hS X f).ι ≫ g)
```

**`AlgebraicGeometry.Space.exists_openSubspace_isFlat_isLocallyOfFinitePresentation_vanishingSubfunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulaySlice.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/CohenMacaulaySlice.lean#L281).

> Let `X ⟶ Y` be flat and locally of finite presentation, let a cartesian square exhibit `F`
> as the fibre `X ×_Y Spec(k)` over a field-valued point of `Y`, and let `z` be a geometric point of
> `F` at which the `f_i` map to a regular sequence in `𝒪_{F, z̄}`.  Then there is an open subspace
> `V ⊆ X` containing `p(z)` over which `V(f₁, …, f_r) ⟶ Y` is flat and locally of finite
> presentation.

```lean
theorem exists_openSubspace_isFlat_isLocallyOfFinitePresentation_vanishingSubfunctor
    (X Y : AlgebraicSpaces B S hS) (g : X.1 ⟶ Y.1) (pt : FieldValuedPoint B S hS Y.1)
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F) (p : F ⟶ X.1)
    (q : F ⟶ yoneda.obj (FieldValuedPoint.siteObject B S hS Y.1 pt))
    (hcart : IsPullback p q g (yonedaEquiv.symm pt.value)) {r : ℕ}
    (f : Fin r → (SheafOfModules.unit (structureRingSheaf B S hS X)).sections)
    (hflat : IsFlat B S hS g) (hg : IsLocallyOfFinitePresentation B S hS g)
    (z : GeometricPoint B S hS F)
    (hreg : FibreIsRegularSequenceAt B S hS X f hF p z) :
    ∃ (V : Subfunctor X.1) (_ : IsOpenSubspace B S hS V),
      pointsMap B S hS F p z.image ∈ Set.range (pointsMap B S hS V.toFunctor V.ι) ∧
        IsFlat B S hS (((vanishingSubfunctor B S hS X f).preimage V.ι).ι ≫ V.ι ≫ g) ∧
          IsLocallyOfFinitePresentation B S hS
            (((vanishingSubfunctor B S hS X f).preimage V.ι).ι ≫ V.ι ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.28, Tag 06LV](https://stacks.math.columbia.edu/tag/06LV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
