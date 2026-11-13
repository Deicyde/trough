---
declaration: section
origin: cited
lean: Deformation.GroupoidInFunctors, Deformation.GroupoidInFunctors.Hom, Deformation.GroupoidInFunctors.evaluationEquivalence, Deformation.existsUnique_identity, Deformation.existsUnique_inverse, Deformation.IsRepresentable, Deformation.GroupoidInFunctors.restrict, Deformation.GroupoidInFunctors.restrict_source
statement: formalized
proof: formalized
---

# 90.21 Groupoids in functors on an arbitrary category

Section 90.21 of the Stacks Project, [Tag 06K2](https://stacks.math.columbia.edu/tag/06K2). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06K3, a definition

[Tag 06K3](https://stacks.math.columbia.edu/tag/06K3) in the Stacks Project.

**`Deformation.GroupoidInFunctors`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L178). The attribute's comment: “objects”.

> A groupoid in functors on `C`: functors of objects and arrows with natural source, target,
> and composition maps which give a groupoid after evaluation at every object of `C`.

```lean
structure GroupoidInFunctors (C : Type u) [Category.{v} C]
```

**`Deformation.GroupoidInFunctors.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L252). The attribute's comment: “morphisms”.

> A morphism of groupoids in functors.

```lean
structure Hom {C : Type u} [Category.{v} C]
    (G H : GroupoidInFunctors C)
```

## Tag 06K4, a remark

[Tag 06K4](https://stacks.math.columbia.edu/tag/06K4) in the Stacks Project.

**`Deformation.GroupoidInFunctors.evaluationEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/GroupoidQuotient/EvaluationEquivalence.lean, line 557](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/GroupoidQuotient/EvaluationEquivalence.lean#L557).

> A groupoid in functors on `C` is the same data as a functor `C ⥤ Grpd`, and a morphism of
> groupoids in functors is the same data as a morphism of the associated functors: evaluation is
> an equivalence of categories.

```lean
noncomputable def evaluationEquivalence :
    GroupoidInFunctors.{u, v, w} C ≌ (C ⥤ Grpd.{w, w})
```

## Tag 06K5, a remark

[Tag 06K5](https://stacks.math.columbia.edu/tag/06K5) in the Stacks Project.

**`Deformation.existsUnique_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L540). The attribute's comment: “identity”.

> Pointwise identities uniquely assemble into a natural transformation from objects
> to arrows.

```lean
public theorem existsUnique_identity {C : Type u} [Category.{v} C]
    (G : GroupoidInFunctors.{u, v, w} C) :
    ∃! e : G.objects ⟶ G.arrows,
      ∀ (T : C) (x : G.Evaluation T), e.app T x = G.identity T x
```

**`Deformation.existsUnique_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 558](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L558). The attribute's comment: “inverse”.

> Pointwise inverses uniquely assemble into a natural transformation of the arrow
> functor.

```lean
public theorem existsUnique_inverse {C : Type u} [Category.{v} C]
    (G : GroupoidInFunctors.{u, v, w} C) :
    ∃! i : G.arrows ⟶ G.arrows,
      ∀ (T : C) (a : G.arrows.obj T), i.app T a = inverseArrow G T a
```

## Tag 06K6, a definition

[Tag 06K6](https://stacks.math.columbia.edu/tag/06K6) in the Stacks Project.

**`Deformation.IsRepresentable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 622](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L622).

> A groupoid in functors is representable if it is isomorphic to one presented by
> covariant representable functors of objects and arrows, and the pushout of the two morphisms
> representing source and target exists.

```lean
public def IsRepresentable {C : Type u} [Category.{v} C] (G : GroupoidInFunctors.{u,
  v, max w v} C) : Prop
```

## Tag 06K9, a definition

[Tag 06K9](https://stacks.math.columbia.edu/tag/06K9) in the Stacks Project.

**`Deformation.GroupoidInFunctors.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/BaseCategory.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/BaseCategory.lean#L74).

> Restriction of a groupoid in functors along a functor of source categories. The restriction
> `(U, R, s, t, c)|_{C'}` of a groupoid in functors to a subcategory `C' ⊆ C` is the case where the
> functor is the inclusion of `C'`.

```lean
public def restrict {C : Type u} {D : Type v} [Category.{w} C] [Category.{x} D]
    (G : GroupoidInFunctors.{v, x, y} D) (F : C ⥤ D) :
    GroupoidInFunctors.{u, w, y} C
```

## Tag 06KA, a remark

[Tag 06KA](https://stacks.math.columbia.edu/tag/06KA) in the Stacks Project.

**`Deformation.GroupoidInFunctors.restrict_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Restriction.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Restriction.lean#L57). The attribute's comment: “source”.

> The source of a restriction is the source of the original groupoid in functors,
> whiskered by the restricting functor.

```lean
public theorem restrict_source : (G.restrict F).source = F.whiskerLeft G.source
```

**`Deformation.GroupoidInFunctors.restrict_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Restriction.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Restriction.lean#L62). The attribute's comment: “target”.

> The target of a restriction is the target of the original groupoid in functors,
> whiskered by the restricting functor.

```lean
public theorem restrict_target : (G.restrict F).target = F.whiskerLeft G.target
```

**`Deformation.GroupoidInFunctors.restrict_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Restriction.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Restriction.lean#L67). The attribute's comment: “composition”.

> The composition of a restriction is the composition of the original groupoid in functors,
> whiskered by the restricting functor.

```lean
public theorem restrict_comp : (G.restrict F).comp = F.whiskerLeft G.comp
```

## Tag 06KB, a definition

[Tag 06KB](https://stacks.math.columbia.edu/tag/06KB) in the Stacks Project.

**`Deformation.evaluationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 712](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L712). The attribute's comment: “evaluation functor”.

> The covariant functor of groupoids obtained by evaluating a groupoid in
> functors at each object of the base category.

```lean
public noncomputable def evaluationFunctor {C : Type u} [Category.{v} C]
    (G : GroupoidInFunctors.{u, v, w} C) : C ⥤ Cat.{w, w}
```

**`Deformation.quotientMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 781](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L781). The attribute's comment: “quotient morphism”.

> The canonical quotient map from the category of elements of the object
> functor to the Grothendieck construction of the evaluated groupoids.

```lean
public noncomputable def quotientMorphism {C : Type u} [Category.{v} C]
    (G : GroupoidInFunctors.{u, v, w} C) :
    G.objects.Elements ⥤ Grothendieck (evaluationFunctor G)
```

**`Deformation.quotientProjection_cofibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 996](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L996). The attribute's comment: “cofibered property”. References: SGA 7 VI (1.1(a)), “groupoid in functors”.

> The projection of the Grothendieck construction of a groupoid in functors
> is cofibered in groupoids.

```lean
public theorem quotientProjection_cofibered {C : Type u} [Category.{v} C]
    (G : GroupoidInFunctors.{u, v, w} C) :
    IsCofiberedInGroupoids
      (Grothendieck.forget (evaluationFunctor G))
```

Declarations registered for the tag:

- [`CategoryTheory.Grothendieck`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Grothendieck#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 771](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L771) (StacksFrontier): “quotient category”. References: SGA 7 VI (1.1(a)).
- [`CategoryTheory.Grothendieck.forget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Grothendieck.forget#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/Groupoid/Basic.lean, line 773](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Groupoid/Basic.lean#L773) (StacksFrontier): “projection”. References: SGA 4 I (8.3.2), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.21, Tag 06K2](https://stacks.math.columbia.edu/tag/06K2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
