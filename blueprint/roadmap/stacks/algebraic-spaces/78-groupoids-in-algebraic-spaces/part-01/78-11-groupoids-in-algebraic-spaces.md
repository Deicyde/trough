---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces, AlgebraicGeometry.GroupoidInAlgebraicSpaces.points_isGroupoid, AlgebraicGeometry.GroupoidInAlgebraicSpaces.Hom, AlgebraicGeometry.Space.groupoidPreRelation_isPreEquivalenceRelation, AlgebraicGeometry.Space.existsUnique_groupoid_of_isEquivalenceRelation, AlgebraicGeometry.Space.isPullback_comp_source, AlgebraicGeometry.Space.isPullback_fst_comp, AlgebraicGeometry.AlgebraicSpaces.isPullback_fiberProduct
statement: formalized
proof: formalized
---

# 78.11 Groupoids in algebraic spaces

Section 78.11 of the Stacks Project, [Tag 043V](https://stacks.math.columbia.edu/tag/043V). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 043W, a definition

[Tag 043W](https://stacks.math.columbia.edu/tag/043W) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean#L55). The attribute's comment: “part (1): groupoid in algebraic spaces”.

> **Stacks 043W, part (1).** A groupoid in algebraic spaces over an algebraic space `B` over
> `S`: algebraic spaces of objects and of arrows, both over `B`, with source, target and
> composition over `B`, whose evaluation at every test scheme is a groupoid.

```lean
structure GroupoidInAlgebraicSpaces
    (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.points_isGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean#L108). The attribute's comment: “part (1): the T-points of the quintuple are a groupoid category”.

> **Stacks 043W, part (1), as a statement about the quintuple.** The defining property of the
> quintuple `(U, R, s, t, c)` of a groupoid in algebraic spaces over `B`: the source and the target
> are morphisms over `B`, and at every test scheme `T` the quintuple of `T`-points is a groupoid
> category. The latter is spelled out as: the `T`-points of the object space `U` are the objects of
> a groupoid, an arrow `x ⟶ y` of that groupoid is the same thing as a `T`-point `a` of the arrow
> space `R` with `s(a) = x` and `t(a) = y`, and the composite of two such arrows is the `T`-point
> of `R` produced by the composition morphism `c`.

```lean
theorem points_isGroupoid {C : BigFppfSite.{u}} {S : Scheme.{u}}
    {hS : C.Contains S} {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B) (T : (BigFppfOver C S hS)ᵒᵖ) :
    G.source ≫ G.objectsToBase = G.arrowsToBase ∧
      G.target ≫ G.objectsToBase = G.arrowsToBase ∧
      ∀ (x y z : G.toGroupoidInFunctors.Evaluation T) (g : x ⟶ y) (f : y ⟶ z),
        (G.toGroupoidInFunctors.evaluationArrowEquiv T x z (g ≫ f)).1 =
          (composableToPullback G.source.hom G.target.hom ≫ G.comp.hom).app T
            ⟨((G.toGroupoidInFunctors.evaluationArrowEquiv T y z f).1,
                (G.toGroupoidInFunctors.evaluationArrowEquiv T x y g).1),
              (G.toGroupoidInFunctors.evaluationArrowEquiv T y z f).2.1.trans
                (G.toGroupoidInFunctors.evaluationArrowEquiv T x y g).2.2.symm⟩
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean#L127). The attribute's comment: “part (2): morphism of groupoids in algebraic spaces”.

> **Stacks 043W, part (2).** A morphism of groupoids in algebraic spaces over the same base: a
> morphism of the underlying groupoids in presheaves whose maps on objects and on arrows are
> morphisms over the base.

```lean
structure Hom {C : BigFppfSite.{u}} {S : Scheme.{u}}
    {hS : C.Contains S} {B : AlgebraicSpaces C S hS}
    (G H : GroupoidInAlgebraicSpaces C S hS B)
```

## Tag 043X, a lemma

[Tag 043X](https://stacks.math.columbia.edu/tag/043X) in the Stacks Project.

**`AlgebraicGeometry.Space.groupoidPreRelation_isPreEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/Basic.lean#L208).

> **Stacks 043X.** The pre-relation cut out by the target and source morphisms of a groupoid
> in algebraic spaces is a pre-equivalence relation: on the points of every test scheme over the
> base it is reflexive, symmetric and transitive, because those points and the arrows between
> them form a groupoid.

```lean
theorem groupoidPreRelation_isPreEquivalenceRelation
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsPreEquivalenceRelation (groupoidPreRelation G)
```

## Tag 043Y, a lemma

[Tag 043Y](https://stacks.math.columbia.edu/tag/043Y) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_groupoid_of_isEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationGroupoid.lean, line 548](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationGroupoid.lean#L548).

> **Stacks 043Y.** An equivalence relation `j : R ⟶ U ×_B U` of algebraic spaces over an
> algebraic space `B` extends to a groupoid in algebraic spaces over `B`, and in exactly one way:
> the source and the target of the groupoid are the two components of `j`, and its composition
> law is then forced, an arrow being determined by its source and its target.

```lean
theorem existsUnique_groupoid_of_isEquivalenceRelation
    (j : PreRelation (Over.mk qR.hom) (Over.mk qU.hom))
    [IsEquivalenceRelation j.target j.source] :
    ∃! G : GroupoidInAlgebraicSpaces C S hS B, ExtendsRelation j G
```

## Tag 043Z, a lemma

[Tag 043Z](https://stacks.math.columbia.edu/tag/043Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_comp_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean#L476). The attribute's comment: “lower\_right”.

> For a groupoid in algebraic spaces, composition and the second projection out of the space of
> composable pairs of arrows form a cartesian square with two copies of the source map: a
> composable pair is determined by its second arrow together with its composite, and every arrow
> and composite with matching sources arise from one, the first arrow of the pair being the
> composite preceded by the inverse of the second.

```lean
theorem isPullback_comp_source {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsPullback G.comp
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      G.source G.source
```

**`AlgebraicGeometry.Space.isPullback_fst_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean, line 503](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean#L503). The attribute's comment: “top\_square”.

> For a groupoid in algebraic spaces, the first projection out of the space of composable pairs
> of arrows and composition form a cartesian square with two copies of the target map: a
> composable pair is determined by its first arrow together with its composite, and every arrow
> and composite with matching targets arise from one, the second arrow of the pair being the
> composite preceded by the inverse of the first.

```lean
theorem isPullback_fst_comp {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsPullback
      (ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      G.comp G.target G.target
```

Declarations registered for the tag:

- [`AlgebraicGeometry.AlgebraicSpaces.isPullback_fiberProduct`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L403), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean#L468) (StacksFrontier): “lower\_left”.

## Tag 0450, a lemma

[Tag 0450](https://stacks.math.columbia.edu/tag/0450) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L108). The attribute's comment: “the comparison of the two upper rows”.

> **Stacks 0450.** The canonical comparison `(α, β) ↦ (α, α⁻¹ ∘ β)` of the space of pairs of
> arrows of a groupoid in algebraic spaces with a common target with the space of composable pairs
> of arrows.

```lean
noncomputable def commonTargetPairsIso (G : GroupoidInAlgebraicSpaces C S hS B) :
    AlgebraicSpaces.fiberProduct C S hS G.target G.target ≅
      AlgebraicSpaces.fiberProduct C S hS G.source G.target
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso_hom_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L117). The attribute's comment: “commutativity for the first projection”.

> **Stacks 0450.** The comparison of pairs with a common target with composable pairs
> preserves the first arrow.

```lean
theorem commonTargetPairsIso_hom_fst (G : GroupoidInAlgebraicSpaces C S hS B) :
    (commonTargetPairsIso G).hom ≫
        (ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom) :
          AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows) =
      ObjectProperty.homMk (pullback.fst G.target.hom G.target.hom)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L129). The attribute's comment: “commutativity for composition”.

> **Stacks 0450.** Composing the comparison of pairs with a common target with composable pairs
> and the composition of the groupoid recovers the second arrow.

```lean
theorem commonTargetPairsIso_hom_comp (G : GroupoidInAlgebraicSpaces C S hS B) :
    (commonTargetPairsIso G).hom ≫ G.comp =
      ObjectProperty.homMk (pullback.snd G.target.hom G.target.hom)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso_inv_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L139). The attribute's comment: “the inverse comparison on the first projection”.

> **Stacks 0450.** The inverse comparison, from composable pairs to pairs with a common target,
> preserves the first arrow.

```lean
theorem commonTargetPairsIso_inv_fst (G : GroupoidInAlgebraicSpaces C S hS B) :
    (commonTargetPairsIso G).inv ≫
        (ObjectProperty.homMk (pullback.fst G.target.hom G.target.hom) :
          AlgebraicSpaces.fiberProduct C S hS G.target G.target ⟶ G.arrows) =
      ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.commonTargetPairsIso_inv_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L151). The attribute's comment: “the inverse comparison on the second projection”.

> **Stacks 0450.** The inverse comparison, from composable pairs to pairs with a common target,
> sends the second arrow to the composite.

```lean
theorem commonTargetPairsIso_inv_snd (G : GroupoidInAlgebraicSpaces C S hS B) :
    (commonTargetPairsIso G).inv ≫
        (ObjectProperty.homMk (pullback.snd G.target.hom G.target.hom) :
          AlgebraicSpaces.fiberProduct C S hS G.target G.target ⟶ G.arrows) =
      G.comp
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.comp_source_eq_snd_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L165). The attribute's comment: “commutativity of the lower square for composition, c ≫ s = pr₁ ≫ s”.

> **Stacks 0450**, the commutativity of the lower square for composition: `c ≫ s = pr₁ ≫ s`.
> The composite of a composable pair of arrows of a groupoid in algebraic spaces has the same
> source as the second arrow of the pair.

```lean
theorem comp_source_eq_snd_source (G : GroupoidInAlgebraicSpaces C S hS B) :
    G.comp ≫ G.source =
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows) ≫ G.source
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.fst_source_eq_snd_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L176). The attribute's comment: “commutativity of the lower square for the projections, pr₀ ≫ s = pr₁ ≫ t”.

> **Stacks 0450**, the commutativity of the lower square for the projections:
> `pr₀ ≫ s = pr₁ ≫ t`. The first arrow of a composable pair of arrows of a groupoid in algebraic
> spaces has as its source the target of the second arrow of the pair.

```lean
theorem fst_source_eq_snd_target (G : GroupoidInAlgebraicSpaces C S hS B) :
    (ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows) ≫ G.source =
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows) ≫ G.target
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isPullback_fst_snd_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L190). The attribute's comment: “the lower-left square for the projections is cartesian”.

> **Stacks 0450**, the lower-left square for the projections. The two projections out of the
> space of composable pairs of arrows of a groupoid in algebraic spaces form a cartesian square
> with the source and the target morphisms: a composable pair is exactly a pair of arrows whose
> first arrow has as its source the target of the second.

```lean
theorem isPullback_fst_snd_source_target (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsPullback
      (ObjectProperty.homMk (pullback.fst G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      (ObjectProperty.homMk (pullback.snd G.source.hom G.target.hom) :
        AlgebraicSpaces.fiberProduct C S hS G.source G.target ⟶ G.arrows)
      G.source G.target
```

Declarations registered for the tag:

- [`AlgebraicGeometry.AlgebraicSpaces.isPullback_fiberProduct`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Category.lean#L403), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L371) (StacksFrontier): “the lower-left square for the projections”.
- [`AlgebraicGeometry.Space.isPullback_comp_source`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpacesOfComposable.lean#L476), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/CommonTargetPairs.lean#L374) (StacksFrontier): “the lower-left square for composition”.

## Tag 0DTA, a lemma

[Tag 0DTA](https://stacks.math.columbia.edu/tag/0DTA) in the Stacks Project.

**`AlgebraicGeometry.Space.baseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/BaseChange.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidInSpaces/BaseChange.lean#L71).

> Pull back a groupoid in algebraic spaces along a morphism of bases.

```lean
noncomputable def baseChange {C : BigFppfSite.{u}} {S : Scheme.{u}}
    {hS : C.Contains S} {B B' : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B) (f : B' ⟶ B) :
    BaseChange G f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.11, Tag 043V](https://stacks.math.columbia.edu/tag/043V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
