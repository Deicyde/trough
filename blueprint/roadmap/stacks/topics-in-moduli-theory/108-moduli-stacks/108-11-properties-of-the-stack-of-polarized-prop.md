---
declaration: section
origin: cited
lean: AlgebraicGeometry.diagonal_polarizedStackUnconditional_isSeparated_isFinitePresentation, AlgebraicGeometry.isQuasiSeparated_and_isLocallyOfFinitePresentation_polarizedAlgebraicStack, AlgebraicGeometry.noetherianSpace_of_isHilbertPolarizedPoint
statement: formalized
proof: formalized
---

# 108.11 Properties of the stack of polarized proper schemes

Section 108.11 of the Stacks Project, [Tag 0DPS](https://stacks.math.columbia.edu/tag/0DPS). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DPT, a lemma

[Tag 0DPT](https://stacks.math.columbia.edu/tag/0DPT) in the Stacks Project.

**`AlgebraicGeometry.diagonal_polarizedStackUnconditional_isSeparated_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedDiagonalUnconditional.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedDiagonalUnconditional.lean#L281).

> **Stacks 0DPT.** The diagonal `Δ : 𝒫olarized ⟶ 𝒫olarized × 𝒫olarized` of the stack of
> polarized proper flat families of finite presentation, over the big fppf site of a terminal base
> scheme, is separated and of finite presentation, both read as in Properties of Stacks,
> Section 04XB: `Δ` is representable by algebraic spaces (Stacks 0D42), and every algebraic space
> representing its base change along a scheme-valued point over a scheme `U` is separated (Stacks
> 03HL) and of finite presentation (Stacks 03XP, part (3)) over `U`, read over the base (Stacks
> 04SG).

```lean
theorem diagonal_polarizedStackUnconditional_isSeparated_isFinitePresentation :
    Stack.HasRepresentableDiagonal B S hS (polarizedStackUnconditional B hS hT) ∧
      Stack.IsSeparated B S hS
        (Stack.diagonal.{u, u, u + 1} B S hS (polarizedStackUnconditional B hS hT)) ∧
      ∀ (U : BigFppfOver B S hS)
        (y : BigFppfOver B U.left.1 U.left.2 ⥤
          (CatFiberedInGroupoids.product (polarizedStackUnconditional B hS hT)
            (polarizedStackUnconditional B hS hT)).val.obj)
        (_hy : y ⋙ (CatFiberedInGroupoids.product (polarizedStackUnconditional B hS hT)
            (polarizedStackUnconditional B hS hT)).val.p = Over.map U.hom)
        (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) (polarizedStackUnconditional B hS hT).val.p
            (CatFiberedInGroupoids.product (polarizedStackUnconditional B hS hT)
              (polarizedStackUnconditional B hS hT)).val.p y
            (CatFiberedInGroupoids.homFunctor
              (Stack.diagonal.{u, u, u + 1} B S hS (polarizedStackUnconditional B hS hT))))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsFinitePresentation B S hS
          (algebraicSpaceMap B S hS U
            ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom
```

## Tag 0DPU, a lemma

[Tag 0DPU](https://stacks.math.columbia.edu/tag/0DPU) in the Stacks Project.

**`AlgebraicGeometry.isQuasiSeparated_and_isLocallyOfFinitePresentation_polarizedAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedQuasiSeparatedLocallyFinitePresentation.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedQuasiSeparatedLocallyFinitePresentation.lean#L94). The attribute's comment: “the morphism Polarized → Spec(Z) is quasi-separated and locally of finite presentation”.

> The morphism `𝒫olarized → Spec(ℤ)` is quasi-separated (Stacks 04YW) and locally of finite
> presentation (Stacks 06Q2).

```lean
theorem isQuasiSeparated_and_isLocallyOfFinitePresentation_polarizedAlgebraicStack :
    Stack.AlgebraicStacks.IsQuasiSeparated B _ hZ
        (Stack.structureMorphism B _ hZ (polarizedAlgebraicStack B hZ)) ∧
      Stack.AlgebraicStacks.IsLocallyOfFinitePresentation B _ hZ
        (Stack.structureMorphism B _ hZ (polarizedAlgebraicStack B hZ))
```

## Tag 0E96, a lemma

[Tag 0E96](https://stacks.math.columbia.edu/tag/0E96) in the Stacks Project.

**`AlgebraicGeometry.noetherianSpace_of_isHilbertPolarizedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PolarizedHilbertBoundedUnconditional.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PolarizedHilbertBoundedUnconditional.lean#L254).

> Let `n ∈ ℕ`, let `P ∈ ℚ[t]` and let `T ⊆ |𝒫olarized|` be a set of points each represented
> over a field by a polarized proper scheme `(X, ℒ)` satisfying conditions (1) and (2)
> (`AlgebraicGeometry.IsHilbertPolarizedOver`): the Hilbert polynomial of `ℒ` on `X` is `P`, and
> there is a closed immersion `i : X ⟶ ℙⁿ` over the base with `i^*𝒪(1) ≅ ℒ`. Then `T` is a
> Noetherian topological space, in particular quasi-compact. The source's hypotheses `n ≥ 1` and
> that `P` is numerical are not needed.

```lean
theorem noetherianSpace_of_isHilbertPolarizedPoint (hT : IsTerminal (B.obj hS)) (n : ℕ)
    (P : Polynomial ℚ)
    (T : Set (Stack.points B S hS (polarizedStackUnconditional B hS hT).val
      (polarizedStackUnconditional B hS hT).property))
    (hTP : ∀ ξ ∈ T, ∃ p, Stack.pointClass B S hS _ _ p = ξ ∧
      IsHilbertPolarizedPoint B hS hT n P p) :
    letI := Stack.pointTopology B S hS (polarizedStackUnconditional B hS hT)
    NoetherianSpace T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.11, Tag 0DPS](https://stacks.math.columbia.edu/tag/0DPS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
