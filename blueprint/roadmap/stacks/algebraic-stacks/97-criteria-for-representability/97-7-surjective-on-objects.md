---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isSurjectiveOnObjects_twoFibreProductSnd, AlgebraicGeometry.Stack.isSurjectiveOnObjects_comp, AlgebraicGeometry.Stack.isSurjectiveOnObjects_iff_isRelativelySurjective
statement: formalized
proof: formalized
---

# 97.7 Surjective on objects

Section 97.7 of the Stacks Project, [Tag 06D4](https://stacks.math.columbia.edu/tag/06D4). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06D5, a lemma

[Tag 06D5](https://stacks.math.columbia.edu/tag/06D5) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjectiveOnObjects_twoFibreProductSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveOnObjects.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveOnObjects.lean#L94).

> **Stacks 06D5.** Surjectivity on objects is preserved by base change: if `p : 𝒳 ⟶ 𝒴` is
> surjective on objects then so is the second projection `𝒳 ×_𝒴 𝒵 ⟶ 𝒵` of its base change along
> any `q : 𝒵 ⟶ 𝒴`.

```lean
theorem isSurjectiveOnObjects_twoFibreProductSnd
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (u + 1) v w}
      (BigFppfOver B S hS))
    (p : 𝒳 ⟶ 𝒴) (q : 𝒵 ⟶ 𝒴)
    (h : IsSurjectiveOnObjects B S hS 𝒳.val.p 𝒴.val.p
      (CatFiberedInGroupoids.homFunctor p)) :
    IsSurjectiveOnObjects B S hS
      (CatFiberedInGroupoids.twoFibreProductSquare p q).pt.val.p 𝒵.val.p
      (CatFiberedInGroupoids.homFunctor
        (CatFiberedInGroupoids.twoFibreProductSquare p q).snd)
```

## Tag 06D6, a lemma

[Tag 06D6](https://stacks.math.columbia.edu/tag/06D6) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjectiveOnObjects_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveOnObjects.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveOnObjects.lean#L140).

> **Stacks 06D6.** A composite of two 1-morphisms surjective on objects is surjective on
> objects: compose the two field extensions.

```lean
theorem isSurjectiveOnObjects_comp
    {X : Type uX} [Category.{vX} X] {Y : Type uY} [Category.{vY} Y]
    {Z : Type uZ} [Category.{vZ} Z]
    (pX : X ⥤ BigFppfOver B S hS) (pY : Y ⥤ BigFppfOver B S hS)
    (pZ : Z ⥤ BigFppfOver B S hS) (F : X ⥤ Y) (G : Y ⥤ Z) (hG : G ⋙ pZ = pY)
    (hFsurj : IsSurjectiveOnObjects B S hS pX pY F)
    (hGsurj : IsSurjectiveOnObjects B S hS pY pZ G) :
    IsSurjectiveOnObjects B S hS pX pZ (F ⋙ G)
```

## Tag 06D7, a lemma

[Tag 06D7](https://stacks.math.columbia.edu/tag/06D7) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSurjectiveOnObjects_iff_isRelativelySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveOnObjectsRelative.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SurjectiveOnObjectsRelative.lean#L388).

> **Stacks 06D7.** A 1-morphism of categories fibred in groupoids over the big fppf site of `S`
> which is representable by algebraic spaces is surjective on objects in the sense of Stacks 06D4
> exactly when it has the relative property of Stacks 03YK for surjectivity of morphisms of
> algebraic spaces.

```lean
theorem isSurjectiveOnObjects_iff_isRelativelySurjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)}
    (p : 𝒳 ⟶ 𝒴) (hp : IsRepresentableByAlgebraicSpaces B S hS p.hom) :
    IsSurjectiveOnObjects B S hS 𝒳.val.p 𝒴.val.p (CatFiberedInGroupoids.homFunctor p) ↔
      HasRelativeProperty B S hS (Space.surjectiveMorphismProperty B S hS) p hp
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.7, Tag 06D4](https://stacks.math.columbia.edu/tag/06D4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
