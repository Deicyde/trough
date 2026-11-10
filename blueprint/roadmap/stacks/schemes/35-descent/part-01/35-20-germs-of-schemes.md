---
declaration: section
origin: cited
lean: AlgebraicGeometry.GermOfScheme, AlgebraicGeometry.MorphismOfGerms, AlgebraicGeometry.MorphismOfGerms.comp, AlgebraicGeometry.MorphismOfGerms.IsEtale, AlgebraicGeometry.MorphismOfGerms.IsSmooth
statement: formalized
proof: formalized
---

# 35.20 Germs of schemes

Section 35.20 of the Stacks Project, [Tag 04QQ](https://stacks.math.columbia.edu/tag/04QQ). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04QR, a definition

[Tag 04QR](https://stacks.math.columbia.edu/tag/04QR) in the Stacks Project.

**`AlgebraicGeometry.GermOfScheme`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Basic.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germ/Basic.lean#L58). The attribute's comment: “germ_of_scheme”.

> A germ of a scheme is a scheme together with a distinguished point.

```lean
structure GermOfScheme
```

**`AlgebraicGeometry.MorphismOfGerms`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Basic.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germ/Basic.lean#L111). The attribute's comment: “morphism_of_germs”.

> A morphism of germs of schemes is a representative defined on an open neighbourhood of the
> distinguished source point, modulo agreement on a possibly smaller such neighbourhood.

```lean
noncomputable def MorphismOfGerms (X S : GermOfScheme.{u}) : Type u
```

**`AlgebraicGeometry.MorphismOfGerms.comp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Basic.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germ/Basic.lean#L294). The attribute's comment: “composition_of_germs”.

> Composition of morphisms of germs, obtained by composing representatives after restricting
> the first one to the inverse image of the domain of the second.

```lean
noncomputable def comp {X Y Z : GermOfScheme.{u}} :
    MorphismOfGerms X Y → MorphismOfGerms Y Z → MorphismOfGerms X Z
```

## Tag 04QS, a definition

[Tag 04QS](https://stacks.math.columbia.edu/tag/04QS) in the Stacks Project.

**`AlgebraicGeometry.MorphismOfGerms.IsEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Etale.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germ/Etale.lean#L48). The attribute's comment: “etale”.

> A morphism of germs is étale if it is represented on some open neighbourhood by an étale
> morphism of schemes.

```lean
abbrev IsEtale {X S : GermOfScheme.{u}} (f : MorphismOfGerms X S) : Prop
```

**`AlgebraicGeometry.MorphismOfGerms.IsSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Etale.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/Germ/Etale.lean#L54). The attribute's comment: “smooth”.

> A morphism of germs is smooth if it is represented on some open neighbourhood by a smooth
> morphism of schemes.

```lean
abbrev IsSmooth {X S : GermOfScheme.{u}} (f : MorphismOfGerms X S) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.20, Tag 04QQ](https://stacks.math.columbia.edu/tag/04QQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
