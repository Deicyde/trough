---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isGerbeOver_quotientStackMap, AlgebraicGeometry.Stack.isGerbeOver_quotientStackToBase_trivialAction
statement: formalized
proof: formalized
---

# 78.27 Gerbes and quotient stacks

Section 78.27 of the Stacks Project, [Tag 06PD](https://stacks.math.columbia.edu/tag/06PD). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06PE, a lemma

[Tag 06PE](https://stacks.math.columbia.edu/tag/06PE) in the Stacks Project.

**`AlgebraicGeometry.Stack.isGerbeOver_quotientStackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GerbeCriterion.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/GerbeCriterion.lean#L491).

> The induced morphism of quotient stacks `[f] : [U/R] ⟶ [U'/R']` makes `[U/R]` a gerbe over
> `[U'/R']` as soon as `f : U ⟶ U'` and `R ⟶ R'|_U` are surjective maps of fppf sheaves: the first
> hypothesis is local surjectivity of the map of object spaces, the second asks that an arrow of
> `R'` between the images of two local points of `U` lift, after an fppf covering, to an arrow of
> `R` between those points.

```lean
public theorem isGerbeOver_quotientStackMap
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
    {G H : GroupoidInAlgebraicSpaces C S hS B}
    (f : GroupoidInAlgebraicSpaces.Hom G H)
    (hobj : Presheaf.IsLocallySurjective
      (BigFppfOver.topology C S hS) f.toGroupoidHom.mapObjects)
    (harr : ∀ (T : BigFppfOver C S hS)
      (a b : G.objects.obj.obj (Opposite.op T))
      (r' : H.arrows.obj.obj (Opposite.op T)),
      H.source.hom.app (Opposite.op T) r' =
        f.toGroupoidHom.mapObjects.app (Opposite.op T) a →
      H.target.hom.app (Opposite.op T) r' =
        f.toGroupoidHom.mapObjects.app (Opposite.op T) b →
      ∃ R ∈ BigFppfOver.topology C S hS T,
        ∀ ⦃V : BigFppfOver C S hS⦄ (i : V ⟶ T), R i →
          ∃ r : G.arrows.obj.obj (Opposite.op V),
            G.source.hom.app (Opposite.op V) r =
              G.objects.obj.map i.op a ∧
            G.target.hom.app (Opposite.op V) r =
              G.objects.obj.map i.op b ∧
            f.toGroupoidHom.mapArrows.app (Opposite.op V) r =
              H.arrows.obj.map i.op r') :
    CategoryTheory.IsGerbeOver
      (BigFppfOver.topology C S hS)
      (quotientStack H).p
      (quotientStackMap f).toFunctor
```

## Tag 06PF, a lemma

[Tag 06PF](https://stacks.math.columbia.edu/tag/06PF) in the Stacks Project.

**`AlgebraicGeometry.Stack.isGerbeOver_quotientStackToBase_trivialAction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionGerbe.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/TrivialActionGerbe.lean#L76).

> **Stacks 06PF.** Let `G` be a group algebraic space over `B` and endow `B` with the trivial
> action of `G`. The structure arrow `[B/G] ⟶ B` turns `[B/G]` into a gerbe over `B`.

```lean
theorem isGerbeOver_quotientStackToBase_trivialAction
    (B : AlgebraicSpaces C S hS) (G : Over B.obj) [GrpObj G]
    (hG : IsAlgebraicSpace C S hS G.left)
    (A : Space.ActionGroupoidConstruction B G (𝟙_ (Over B.obj)) hG B.property) :
    CategoryTheory.IsGerbeOver (BigFppfOver.topology C S hS)
      (fibredCategory C S hS B.obj).val.p (quotientStackToBase A.groupoid).toFunctor
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.27, Tag 06PD](https://stacks.math.columbia.edu/tag/06PD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
