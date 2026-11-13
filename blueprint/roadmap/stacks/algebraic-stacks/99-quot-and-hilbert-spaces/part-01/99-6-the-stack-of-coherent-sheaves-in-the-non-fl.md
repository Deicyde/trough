---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicStack_coherentCFG
statement: formalized
proof: formalized
---

# 99.6 The stack of coherent sheaves in the non-flat case

Section 99.6 of the Stacks Project, [Tag 08WB](https://stacks.math.columbia.edu/tag/08WB). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09DS, a theorem

[Tag 09DS](https://stacks.math.columbia.edu/tag/09DS) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicStack_coherentCFG`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CoherentStackIsAlgebraic.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CoherentStackIsAlgebraic.lean#L35).

> **Algebraicity of the stack of coherent sheaves.** Let `S` be a scheme and let `f : X ⟶ Y` be a
> morphism of algebraic spaces over `S`, of finite presentation (part of the standing datum `D` of
> Situation 08KB) and separated. Then `Coh_{X/Y}` is an algebraic stack over `S`.

```lean
theorem isAlgebraicStack_coherentCFG.{w} {B : BigFppfSite.{u}} {S : Scheme.{u}}
    {hS : B.Contains S} (D : CoherentSituation B S hS) (hsep : IsSeparated B S hS D.f.hom) :
    Stack.IsAlgebraicStack.{u, w} B S hS (coherentCFG D).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.6, Tag 08WB](https://stacks.math.columbia.edu/tag/08WB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
