---
declaration: section
origin: cited
lean: AlgebraicGeometry.spaceHomEquivPullbackHom, AlgebraicGeometry.spacesProjection_isStronglyCartesian_iff, AlgebraicGeometry.spacesProjection_isFibered, AlgebraicGeometry.spacesProjection_isMorSheaf
statement: formalized
proof: formalized
---

# 95.7 Algebraic spaces

Section 95.7 of the Stacks Project, [Tag 04SP](https://stacks.math.columbia.edu/tag/04SP). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04U8, an equation

[Tag 04U8](https://stacks.math.columbia.edu/tag/04U8) in the Stacks Project.

**`AlgebraicGeometry.spaceHomEquivPullbackHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/VaryingBaseHom.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/VaryingBaseHom.lean#L82).

> The hom-set equation for algebraic spaces over varying representable bases.

```lean
noncomputable def spaceHomEquivPullbackHom
    (A C : Comma
      (ObjectProperty.ι (fun F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u =>
        IsAlgebraicSpace B S hS F))
      (yoneda : BigFppfOver B S hS ⥤
        (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)) :
    { e : (A ⟶ C) ≃
        Σ g : A.right ⟶ C.right,
          (Over.mk (ObjectProperty.homMk A.hom : A.left ⟶
            schemeSpace A.right) ⟶ pullbackOver A C g) //
      ∀ m : A ⟶ C, (e m).1 = m.right ∧
        ((e m).2).left ≫
          (ObjectProperty.homMk
            (pullback.snd (schemeSpaceMap (e m).1).hom C.hom) :
              AlgebraicSpaces.fiberProduct B S hS
                (schemeSpaceMap (e m).1) (ObjectProperty.homMk C.hom) ⟶
                C.left) = m.left }
```

## Tag 04U9, a lemma

[Tag 04U9](https://stacks.math.columbia.edu/tag/04U9) in the Stacks Project.

**`AlgebraicGeometry.spacesProjection_isStronglyCartesian_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StronglyCartesian.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/StronglyCartesian.lean#L80).

> **Stacks 04U9.** A morphism of algebraic spaces over varying schemes is strongly
> cartesian if and only if its canonical comparison with the base change of its target is an
> isomorphism.

```lean
theorem spacesProjection_isStronglyCartesian_iff
    {A C : Comma
      (ObjectProperty.ι (fun F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u =>
        IsAlgebraicSpace B S hS F))
      (yoneda : BigFppfOver B S hS ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)} (m : A ⟶ C) :
    (spacesProjection B S hS).IsStronglyCartesian m.right m ↔
      IsIso (ObjectProperty.homMk (pullback.lift A.hom m.left.hom m.w.symm) :
        A.left ⟶ AlgebraicSpaces.fiberProduct B S hS
          (schemeSpaceMap m.right) (ObjectProperty.homMk C.hom))
```

## Tag 04UA, a lemma

[Tag 04UA](https://stacks.math.columbia.edu/tag/04UA) in the Stacks Project.

**`AlgebraicGeometry.spacesProjection_isFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Prestack.lean, line 1089](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Prestack.lean#L1089). The attribute's comment: “condition (1)”.

> The projection from algebraic spaces over schemes is a fibred category.

```lean
theorem spacesProjection_isFibered :
    (spacesProjection B S hS).IsFibered
```

**`AlgebraicGeometry.spacesProjection_isMorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Prestack.lean, line 1097](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Prestack.lean#L1097). The attribute's comment: “condition (2)”.

> Morphisms of algebraic spaces over a fixed scheme satisfy fppf descent.

```lean
theorem spacesProjection_isMorSheaf :
    haveI : (spacesProjection B S hS).IsFibered :=
      spacesProjection_isFibered B S hS
    ∀ (U : BigFppfOver B S hS)
      (X Y : (spacesProjection B S hS).Fiber U),
      (spacesProjection B S hS).IsMorSheaf
        (BigFppfOver.topology B S hS) U X Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.7, Tag 04SP](https://stacks.math.columbia.edu/tag/04SP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
