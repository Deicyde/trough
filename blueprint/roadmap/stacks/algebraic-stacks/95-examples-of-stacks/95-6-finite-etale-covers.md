---
declaration: section
origin: cited
lean: AlgebraicGeometry.FiniteEtaleCovers, AlgebraicGeometry.finiteEtaleProjection, AlgebraicGeometry.finiteEtaleProjection_isFibered, AlgebraicGeometry.finiteEtaleProjection_isStack, AlgebraicGeometry.finiteEtaleProjection_isMorSheaf
statement: formalized
proof: formalized
---

# 95.6 Finite étale covers

Section 95.6 of the Stacks Project, [Tag 0BLY](https://stacks.math.columbia.edu/tag/0BLY). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BLY, the section

[Tag 0BLY](https://stacks.math.columbia.edu/tag/0BLY) in the Stacks Project.

**`AlgebraicGeometry.FiniteEtaleCovers`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCovers.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCovers.lean#L78). The attribute's comment: “the category FÉt of the section: objects are the finite étale morphisms of the big fppf category over S, morphisms are the commutative squares”.

> The category `FÉt` of Stacks 0BLY over a big fppf site: an object is a finite étale
> morphism `U ⟶ T` of the big fppf category over `S`, and a morphism is a commutative square.

```lean
abbrev FiniteEtaleCovers : Type _
```

**`AlgebraicGeometry.finiteEtaleProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCovers.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCovers.lean#L84). The attribute's comment: “the functor p of the section, sending a finite étale cover to its base”.

> The functor `p : FÉt ⟶ (Sch/S)_fppf` of Stacks 0BLY, sending a finite étale morphism
> `U ⟶ T` to its base `T`.

```lean
def finiteEtaleProjection : FiniteEtaleCovers B S hS ⥤ BigFppfOver B S hS
```

## Tag 0BLZ, a lemma

[Tag 0BLZ](https://stacks.math.columbia.edu/tag/0BLZ) in the Stacks Project.

**`AlgebraicGeometry.finiteEtaleProjection_isFibered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCovers.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCovers.lean#L121). The attribute's comment: “condition (1) of Stacks 026F: `p` is a fibred category. Condition (2), that the presheaves Mor(x, y) are fppf sheaves, is `AlgebraicGeometry.finiteEtaleProjection_isMorSheaf`.”.

> **Condition (1) of Stacks 026F for `FÉt`.** The functor `p : FÉt ⟶ (Sch/S)_fppf` is a
> fibred category: the strongly cartesian lift of a morphism `f : T ⟶ T'` with target the finite
> étale cover `U ⟶ T'` is the base change `U ×_{T'} T ⟶ T`, again finite étale.

```lean
instance finiteEtaleProjection_isFibered :
    (finiteEtaleProjection B S hS).IsFibered
```

**`AlgebraicGeometry.finiteEtaleProjection_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCoversDescent.lean, line 749](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCoversDescent.lean#L749).

> **Stacks 0BLZ.** The functor `p : FÉt ⟶ (Sch/S)_fppf` of Stacks 0BLY defines a stack over
> the big fppf site of `S`: it satisfies the three conditions of Stacks 026F.
>
> Condition (1) is `AlgebraicGeometry.finiteEtaleProjection_isFibered`, condition (2) is
> `AlgebraicGeometry.finiteEtaleProjection_isMorSheaf` and condition (3) is
> `AlgebraicGeometry.finiteEtaleProjection_hasEffectiveDescent`.

```lean
theorem finiteEtaleProjection_isStack :
    Functor.IsStack (finiteEtaleProjection B S hS) (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.finiteEtaleProjection_isMorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCoversStack.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/FiniteEtaleCoversStack.lean#L316). The attribute's comment: “condition (2) of Stacks 026F: the presheaves Mor(x, y) are fppf sheaves, so locally equal morphisms of `FÉt` are equal and morphisms given compatibly over a covering sieve glue. Condition (1) is `AlgebraicGeometry.finiteEtaleProjection_isFibered`.”.

> **Condition (2) of Stacks 026F for `FÉt`.** The presheaves `Mor(x, y)` of Stacks 02ZB
> attached to two finite étale covers of one and the same base are sheaves for the fppf
> topology: locally equal morphisms of `FÉt` are equal, and morphisms of `FÉt` given
> compatibly over a covering sieve of the base glue.

```lean
theorem finiteEtaleProjection_isMorSheaf (U : BigFppfOver B S hS)
    (x y : (finiteEtaleProjection B S hS).Fiber U) :
    Functor.IsMorSheaf (finiteEtaleProjection B S hS) (BigFppfOver.topology B S hS) U x y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.6, Tag 0BLY](https://stacks.math.columbia.edu/tag/0BLY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
