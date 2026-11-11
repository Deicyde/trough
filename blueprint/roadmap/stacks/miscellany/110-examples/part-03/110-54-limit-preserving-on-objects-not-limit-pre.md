---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.ObjectwiseLimitPreserving.exists_stack_isLimitPreservingOnObjects_not_isLimitPreserving
statement: formalized
proof: formalized
---

# 110.54 Limit preserving on objects, not limit preserving

Section 110.54 of the Stacks Project, [Tag 07Z0](https://stacks.math.columbia.edu/tag/07Z0). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07Z1, a lemma

[Tag 07Z1](https://stacks.math.columbia.edu/tag/07Z1) in the Stacks Project.

**`AlgebraicGeometry.Stack.ObjectwiseLimitPreserving.exists_stack_isLimitPreservingOnObjects_not_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/ObjectwiseLimitPreserving.lean, line 2427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Stacks/ObjectwiseLimitPreserving.lean#L2427).

> **Stacks 07Z1.** Over a nonempty base there is a stack in groupoids whose structure
> morphism to the big fppf site is limit preserving on objects while the stack itself is not
> limit preserving. The stackiness of the category of torsors, Stacks 04UM, enters as the
> hypothesis `h04UM`.

```lean
public theorem exists_stack_isLimitPreservingOnObjects_not_isLimitPreserving
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [Nonempty S]
    (h04UM : ∀ {ℬ : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (𝒢 : Grp (Over ℬ)),
      Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) ℬ →
      Presheaf.IsSheaf (AlgebraicGeometry.BigFppfOver.topology B S hS) 𝒢.X.left →
      Functor.IsStackInGroupoids.{u + 1}
        (ClassifyingTorsors.torsorsProjection 𝒢)
        (AlgebraicGeometry.BigFppfOver.topology B S hS)) :
    ∃ 𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1}
        (AlgebraicGeometry.BigFppfOver B S hS),
      𝒳.val.p.IsStackInGroupoids.{u + 1}
          (AlgebraicGeometry.BigFppfOver.topology B S hS) ∧
        AlgebraicGeometry.BigFppfOver.IsLimitPreservingOnObjects.{u, v, w, u, u + 1} B S hS 𝒳
          (AlgebraicGeometry.Stack.terminalCFG B S hS)
          (Bicategory.InducedBicategory.mkHom
            (AlgebraicGeometry.Stack.toTerminalCFG B S hS 𝒳)) ∧
        ¬ Deformation.Artin.IsLimitPreserving.{u, v, w, u + 1, u} B S hS 𝒳
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.54, Tag 07Z0](https://stacks.math.columbia.edu/tag/07Z0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
