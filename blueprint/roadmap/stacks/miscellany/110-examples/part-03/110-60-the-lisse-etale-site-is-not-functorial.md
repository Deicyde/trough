---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.LisseEtale.exists_not_isMorphismOfSites_pullback
statement: formalized
proof: formalized
---

# 110.60 The lisse-étale site is not functorial

Section 110.60 of the Stacks Project, [Tag 07BF](https://stacks.math.columbia.edu/tag/07BF). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07BG, a lemma

[Tag 07BG](https://stacks.math.columbia.edu/tag/07BG) in the Stacks Project.

**`AlgebraicGeometry.Stack.LisseEtale.exists_not_isMorphismOfSites_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/LisseEtaleNotFunctorial.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/LisseEtaleNotFunctorial.lean#L128).

> **Stacks 07BG.** *The lisse-étale site is not functorial, even for morphisms of schemes.*
>
> There is a morphism `f : X ⟶ Y` of schemes over `S` in a big fppf site for which the base-change
> functor `Y_{lisse,étale} ⥤ X_{lisse,étale}` — identified here by a natural isomorphism after
> forgetting smoothness, so that no particular choice of fibre products is asserted — is
> continuous, and yet does not define a morphism of sites: its pushforward on sheaves has no left
> exact left adjoint.
>
> See the module documentation for the counterexample.

```lean
theorem exists_not_isMorphismOfSites_pullback :
    ∃ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (X Y : BigFppfOver B S hS) (f : X ⟶ Y)
      (F : LisseEtale.{u, w} B S hS (schemeStack.{u, w} B S hS Y) ⥤
        LisseEtale.{u, w} B S hS (schemeStack.{u, w} B S hS X)),
      Nonempty (F ⋙ inclusion.{u, w} B S hS (schemeStack.{u, w} B S hS X) ≅
        inclusion.{u, w} B S hS (schemeStack.{u, w} B S hS Y) ⋙ Over.pullback f) ∧
      F.IsContinuous (topology.{u, w} B S hS (schemeStack.{u, w} B S hS Y))
        (topology.{u, w} B S hS (schemeStack.{u, w} B S hS X)) ∧
      ¬ IsMorphismOfSites.{u + 1} F
        (topology.{u, w} B S hS (schemeStack.{u, w} B S hS Y))
        (topology.{u, w} B S hS (schemeStack.{u, w} B S hS X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.60, Tag 07BF](https://stacks.math.columbia.edu/tag/07BF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
