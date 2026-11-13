---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.ObjectwiseLimitPreserving.exists_isStackInGroupoids_isLimitPreservingOnObjects_not_isLimitPreserving
statement: formalized
proof: formalized
---

# 110.54 Limit preserving on objects, not limit preserving

Section 110.54 of the Stacks Project, [Tag 07Z0](https://stacks.math.columbia.edu/tag/07Z0). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07Z1, a lemma

[Tag 07Z1](https://stacks.math.columbia.edu/tag/07Z1) in the Stacks Project.

**`AlgebraicGeometry.Stack.ObjectwiseLimitPreserving.exists_isStackInGroupoids_isLimitPreservingOnObjects_not_isLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Stacks/ObjectwiseLimitPreservingTorsors.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Stacks/ObjectwiseLimitPreservingTorsors.lean#L96).

> **Stacks 07Z1.** Let `S` be a nonempty scheme. There exists a stack in groupoids
> `p : 𝒳 ⥤ (Sch/S)_fppf` such that `p` is limit preserving on objects (Stacks 06CU), but `𝒳`
> is not limit preserving (Stacks 07XL). The stack is the stack of torsors under a countable
> product of copies of a nonzero injective abelian sheaf, a stack in groupoids by Stacks 04UM.

```lean
theorem exists_isStackInGroupoids_isLimitPreservingOnObjects_not_isLimitPreserving
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [Nonempty S] :
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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
