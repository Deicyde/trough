---
declaration: section
origin: cited
lean: Stacks.Chow.isRegularImmersion_diagonal_of_smooth, Stacks.Chow.gysinMapExists_diagonal_of_smooth, Stacks.Chow.diagonalGysinClass, Stacks.Chow.isFiniteLocallyFreeOfRank_diagonalVirtualNormalBundle, Stacks.Chow.diagonalGysinMap_comp_eq_completedIdentityClass, Stacks.Chow.smoothRelativeDimensionShiftEquiv
statement: formalized
proof: formalized
---

# 42.60 Gysin maps for diagonals

Section 42.60 of the Stacks Project, [Tag 0FBR](https://stacks.math.columbia.edu/tag/0FBR). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FBR, the section

[Tag 0FBR](https://stacks.math.columbia.edu/tag/0FBR) in the Stacks Project.

**`Stacks.Chow.isRegularImmersion_diagonal_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean#L50). The attribute's comment: “the diagonal of a smooth morphism is a regular immersion”. References: SGA 6 VII (1.10), “special case”; SGA 6 VIII (1.3), “special case”.

> The diagonal `Δ : X ⟶ X ×_Y X` of a smooth morphism is a regular immersion.

```lean
theorem isRegularImmersion_diagonal_of_smooth [Smooth f] :
    Stacks.AlgebraicGeometry.RegularIdealSheaf.IsRegularImmersion (pullback.diagonal f)
```

**`Stacks.Chow.gysinMapExists_diagonal_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysin.lean#L57). The attribute's comment: “the Gysin map Δ^! is available for the diagonal”.

> The Gysin map exists for the diagonal of a smooth morphism, in the sense of Stacks 0FF3.

```lean
theorem gysinMapExists_diagonal_of_smooth [Smooth f] :
    GysinMapExists (pullback.diagonal f)
```

**`Stacks.Chow.diagonalGysinClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClass.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinClass.lean#L158). The attribute's comment: “the Gysin class Δ^! ∈ A^d(X → X ×\_Y X) of the diagonal of a smooth morphism of constant relative dimension d”.

> **Stacks 0FBR, the Gysin class `Δ^! ∈ A^d(Y ⟶ Y ×_Z Y)`** of the diagonal of a smooth
> morphism `g : Y ⟶ Z` of constant relative dimension `d`: the class `c(Y ⟶ Y ×_Z Y, 𝒩)` of Stacks
> 0FBQ (3) of the normal bundle `𝒩` of the diagonal (Stacks 0FEZ), at the open subscheme
> `U = (pullback.diagonal g).coborderRange` in which the diagonal is closed. It is
> `c(Y ⟶ U, 𝒩) ∘ ι^*` by `Stacks.Chow.diagonalGysinClass_eq_bivariantCompositeOfInvertible`.

```lean
def diagonalGysinClass :
    BivariantClass C (gysinSystemOfInvertible C)
      (pullback.diagonal g ≫ (pullback.fst g g ≫ sY)) (pullback.fst g g ≫ sY)
      (pullback.diagonal g) rfl d
```

**`Stacks.Chow.isFiniteLocallyFreeOfRank_diagonalVirtualNormalBundle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalVirtualNormalBundle.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DiagonalVirtualNormalBundle.lean#L286). The attribute's comment: “constant relative dimension d: the normal bundle of the diagonal has rank d”.

> **Stacks Project, Section 42.60 (Tag 0FBR), the degree.** For `f` smooth of constant relative
> dimension `d`, the normal bundle of the diagonal is finite locally free of rank `d`; this is why
> the Gysin class `Δ^!` lies in `A^d(Y ⟶ Y ×_Z Y)`.

```lean
theorem isFiniteLocallyFreeOfRank_diagonalVirtualNormalBundle [Smooth f] {d : ℕ}
    (hd : RelativeDimension f d) :
    AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u}
      (diagonalVirtualNormalBundle f).bundle d
```

## Tag 0FBS, a lemma

[Tag 0FBS](https://stacks.math.columbia.edu/tag/0FBS) in the Stacks Project.

**`Stacks.Chow.diagonalGysinMap_comp_eq_completedIdentityClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinMap.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DiagonalGysinMap.lean#L138). The attribute's comment: “Δ^! ∘ pr\_i^! = 1 for both projections i = 1, 2, Δ^! and pr\_i^! the Gysin maps of Stacks 0FF3, in the completed ring A^*(X)^∧, for any smooth X → Y”.

> **Stacks 0FBS: `Δ^! ∘ pr_i^! = 1` in `A^0(X)`, for `i = 1, 2`.** Let `f : X ⟶ Y` be a smooth
> morphism of schemes locally of finite type over the base, let `Δ : X ⟶ X ×_Y X` be its diagonal
> and `pr_1, pr_2 : X ×_Y X ⟶ X` the projections. Write `Δ^! ∈ A^*(X ⟶ X ×_Y X)^∧` and
> `pr_i^! ∈ A^*(X ×_Y X ⟶ X)^∧` for their Gysin maps (Stacks 0FF3), which exist since `Δ` is a
> regular immersion (Stacks 0FBR) and the projections are smooth. Then for both projections the
> composite `Δ^! ∘ pr_i^!` (Stacks 0FE0), read as a class for `𝟙 X` through `Δ ≫ pr_i = 𝟙 X`, is
> the unit `1 ∈ A^0(X) ⊆ A^*(X)^∧`. No constancy of the relative dimension of `f` is assumed.

```lean
theorem diagonalGysinMap_comp_eq_completedIdentityClass :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    haveI : IsLocallyNoetherian (pullback f f) :=
      LocallyOfFiniteType.isLocallyNoetherian (pullback.fst f f ≫ sX)
    completedBivariantGroup.copy C (pullback.diagonal_fst f)
        (comp_comp_structureMorphism_eq (by simp) rfl) (Category.id_comp sX)
        (completedBivariantCompositeOfInvertible C sX (pullback.fst f f ≫ sX) sX
          (pullback.diagonal f) (pullback.fst f f) (by simp) rfl
          (lciGysinMap C sX (pullback.fst f f ≫ sX) (by simp)
            (isLocalCompleteIntersectionMorphism_of_isRegularImmersion _
              (isRegularImmersion_diagonal_of_smooth f))
            (gysinMapExists_diagonal_of_smooth f))
          (lciGysinMap C (pullback.fst f f ≫ sX) sX rfl
            (isLocalCompleteIntersectionMorphism_of_syntomic (syntomic_of_smooth _))
            (GysinMapExists.of_smooth _))) =
        completedIdentityClass C sX ∧
      completedBivariantGroup.copy C (pullback.diagonal_snd f)
        (comp_comp_structureMorphism_eq (by simp)
          (pullback_snd_comp_structureMorphism_of_comp_eq C sX sY f hf)) (Category.id_comp sX)
        (completedBivariantCompositeOfInvertible C sX (pullback.fst f f ≫ sX) sX
          (pullback.diagonal f) (pullback.snd f f) (by simp)
          (pullback_snd_comp_structureMorphism_of_comp_eq C sX sY f hf)
          (lciGysinMap C sX (pullback.fst f f ≫ sX) (by simp)
            (isLocalCompleteIntersectionMorphism_of_isRegularImmersion _
              (isRegularImmersion_diagonal_of_smooth f))
            (gysinMapExists_diagonal_of_smooth f))
          (lciGysinMap C (pullback.fst f f ≫ sX) sX
            (pullback_snd_comp_structureMorphism_of_comp_eq C sX sY f hf)
            (isLocalCompleteIntersectionMorphism_of_syntomic (syntomic_of_smooth _))
            (GysinMapExists.of_smooth _))) =
        completedIdentityClass C sX
```

## Tag 0FBT, a proposition

[Tag 0FBT](https://stacks.math.columbia.edu/tag/0FBT) in the Stacks Project.

**`Stacks.Chow.smoothRelativeDimensionShiftEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SmoothChowCohomology.lean#L79). The attribute's comment: “g^! read as the flat pullback g^* of the smooth morphism g; bivariant classes are those of the Gysin system of invertible modules, `Stacks.Chow.gysinSystemOfInvertible`”.

> **Stacks 0FBT.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of schemes locally of finite
> type over `S`, with `g` smooth of relative dimension `d`. Then `c ↦ c ∘ g^*` is an isomorphism
>
>   `A^p(X ⟶ Y) ≃ A^{p-d}(X ⟶ Z)`,
>
> with inverse `c' ↦ res(Δ^!) ∘ res(c')`, where `Δ^!` is the Gysin class of the diagonal of `g`
> (Stacks 0FBR). For a smooth `g` the Gysin map `g^!` of Stacks 0FEZ is the flat pullback `g^*`.

```lean
def smoothRelativeDimensionShiftEquiv :
    BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p ≃+
      BivariantClass C (gysinSystemOfInvertible C) sX sZ (f ≫ g)
        (comp_comp_structureMorphism_eq hf hg) (p - d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.60, Tag 0FBR](https://stacks.math.columbia.edu/tag/0FBR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
