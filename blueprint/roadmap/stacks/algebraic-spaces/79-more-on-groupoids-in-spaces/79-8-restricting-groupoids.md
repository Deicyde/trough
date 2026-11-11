---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.restrict, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFiniteType_restrict_source, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFiniteType_restrict_target, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFinitePresentation_restrict_source, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFinitePresentation_restrict_target, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_restrict_source, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_restrict_target
statement: formalized
proof: formalized
---

# 79.8 Restricting groupoids

Section 79.8 of the Stacks Project, [Tag 04RM](https://stacks.math.columbia.edu/tag/04RM). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04RN, an equation

[Tag 04RN](https://stacks.math.columbia.edu/tag/04RN) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidRestriction/Restrict.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidRestriction/Restrict.lean#L59). The attribute's comment: “the fibre-product diagram defining R' with its source and target maps”.

> Restriction along an arbitrary map to the object space, with its canonical
> composition law and functor to the original groupoid.

```lean
public noncomputable def restrict
    {C : BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {U' : AlgebraicSpaces C S hS} (g : U' ⟶ G.objects) :
    Restriction G g
```

## Tag 04RP, a lemma

[Tag 04RP](https://stacks.math.columbia.edu/tag/04RP) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFiniteType_restrict_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean#L155). The attribute's comment: “part (1): the restricted source is locally of finite type”.

> **Stacks 04RP.** If the source of a groupoid in algebraic spaces over `B` and the morphism
> `g` along which it is restricted are locally of finite type, then so is the source of the
> restriction.

```lean
theorem isLocallyOfFiniteType_restrict_source
    (hs : Space.IsLocallyOfFiniteType C S hS G.source.hom)
    (hg : Space.IsLocallyOfFiniteType C S hS g.hom) :
    Space.IsLocallyOfFiniteType C S hS (restrict G g).groupoid.source.hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFiniteType_restrict_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean#L168). The attribute's comment: “part (1): the restricted target is locally of finite type”.

> **Stacks 04RP.** If the target of a groupoid in algebraic spaces over `B` and the morphism
> `g` along which it is restricted are locally of finite type, then so is the target of the
> restriction.

```lean
theorem isLocallyOfFiniteType_restrict_target
    (ht : Space.IsLocallyOfFiniteType C S hS G.target.hom)
    (hg : Space.IsLocallyOfFiniteType C S hS g.hom) :
    Space.IsLocallyOfFiniteType C S hS (restrict G g).groupoid.target.hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFinitePresentation_restrict_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean#L181). The attribute's comment: “part (2): the restricted source is locally of finite presentation”.

> **Stacks 04RP.** If the source of a groupoid in algebraic spaces over `B` and the morphism
> `g` along which it is restricted are locally of finite presentation, then so is the source of
> the restriction.

```lean
theorem isLocallyOfFinitePresentation_restrict_source
    (hs : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (hg : Space.IsLocallyOfFinitePresentation C S hS g.hom) :
    Space.IsLocallyOfFinitePresentation C S hS (restrict G g).groupoid.source.hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallyOfFinitePresentation_restrict_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean#L194). The attribute's comment: “part (2): the restricted target is locally of finite presentation”.

> **Stacks 04RP.** If the target of a groupoid in algebraic spaces over `B` and the morphism
> `g` along which it is restricted are locally of finite presentation, then so is the target of
> the restriction.

```lean
theorem isLocallyOfFinitePresentation_restrict_target
    (ht : Space.IsLocallyOfFinitePresentation C S hS G.target.hom)
    (hg : Space.IsLocallyOfFinitePresentation C S hS g.hom) :
    Space.IsLocallyOfFinitePresentation C S hS (restrict G g).groupoid.target.hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_restrict_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean#L206). The attribute's comment: “part (3): the restricted source is flat”.

> **Stacks 04RP.** If the source of a groupoid in algebraic spaces over `B` and the morphism
> `g` along which it is restricted are flat, then so is the source of the restriction.

```lean
theorem isFlat_restrict_source (hs : Space.IsFlat C S hS G.source.hom)
    (hg : Space.IsFlat C S hS g.hom) :
    Space.IsFlat C S hS (restrict G g).groupoid.source.hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isFlat_restrict_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/RestrictionProperties.lean#L216). The attribute's comment: “part (3): the restricted target is flat”.

> **Stacks 04RP.** If the target of a groupoid in algebraic spaces over `B` and the morphism
> `g` along which it is restricted are flat, then so is the target of the restriction.

```lean
theorem isFlat_restrict_target (ht : Space.IsFlat C S hS G.target.hom)
    (hg : Space.IsFlat C S hS g.hom) :
    Space.IsFlat C S hS (restrict G g).groupoid.target.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.8, Tag 04RM](https://stacks.math.columbia.edu/tag/04RM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
