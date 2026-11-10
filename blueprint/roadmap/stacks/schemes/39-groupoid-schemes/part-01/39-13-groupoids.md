---
declaration: section
origin: cited
lean: CategoryTheory.Groupoid.eq_id_of_comp_eq, CategoryTheory.Groupoid.eq_inv_of_comp_eq_id, Prefunctor.map_id_of_map_comp, Prefunctor.map_inv_of_map_comp, CategoryTheory.Groupoid, CategoryTheory.Groupoid.invEquiv, Stacks.Groupoids.GroupoidScheme.evaluationGroupoid, AlgebraicGeometry.groupoidInverse_left_isIso
statement: formalized
proof: formalized
---

# 39.13 Groupoids

Section 39.13 of the Stacks Project, [Tag 0230](https://stacks.math.columbia.edu/tag/0230). 7 tags here are carried by 18 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0230, the section

[Tag 0230](https://stacks.math.columbia.edu/tag/0230) in the Stacks Project.

**`CategoryTheory.Groupoid.eq_id_of_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L52). The attribute's comment: “the identity map e is uniquely determined”.

> In a groupoid, a family of endomorphisms which is a right unit for composition is the family
> of identities.

```lean
theorem eq_id_of_comp_eq (e : ∀ X : C, X ⟶ X) (he : ∀ {X Y : C} (f : X ⟶ Y), f ≫ e Y = f)
    (X : C) : e X = 𝟙 X
```

**`CategoryTheory.Groupoid.eq_inv_of_comp_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L58). The attribute's comment: “the inverse map i is uniquely determined”.

> In a groupoid, a right inverse of a morphism is its inverse.

```lean
theorem eq_inv_of_comp_eq_id (i : ∀ {X Y : C}, (X ⟶ Y) → (Y ⟶ X))
    (hi : ∀ {X Y : C} (f : X ⟶ Y), f ≫ i f = 𝟙 X) {X Y : C} (f : X ⟶ Y) :
    i f = Groupoid.inv f
```

**`Prefunctor.map_id_of_map_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L72). The attribute's comment: “a map of groupoids compatible with composition preserves identities”.

> A map of groupoids compatible with composition preserves identities.

```lean
theorem map_id_of_map_comp (F : C ⥤q D)
    (hF : ∀ {X Y Z : C} (f : X ⟶ Y) (g : Y ⟶ Z), F.map (f ≫ g) = F.map f ≫ F.map g) (X : C) :
    F.map (𝟙 X) = 𝟙 (F.obj X)
```

**`Prefunctor.map_inv_of_map_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L90). The attribute's comment: “a map of groupoids compatible with composition preserves inverses”.

> A map of groupoids compatible with composition preserves inverses.

```lean
theorem map_inv_of_map_comp (F : C ⥤q D)
    (hF : ∀ {X Y Z : C} (f : X ⟶ Y) (g : Y ⟶ Z), F.map (f ≫ g) = F.map f ≫ F.map g)
    {X Y : C} (f : X ⟶ Y) : F.map (Groupoid.inv f) = Groupoid.inv (F.map f)
```

Declarations registered for the tag:

- [`CategoryTheory.Groupoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Groupoid#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L98) (StacksFrontier): “groupoid categories”. References: SGA 3 V (1.2), “partial”; SGA 4 I (6.5.1); SGA 4 I (6.5.2); SGA 4 XVIII (1.2.1), “partial”.
- [`CategoryTheory.Groupoid.invEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Groupoid.invEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L103) (StacksFrontier): “the inverse map i is a bijection”.
- [`Stacks.Groupoids.GroupoidScheme.evaluationGroupoid`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L69), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L104) (StacksFrontier): “the points of a groupoid scheme over a test scheme form a groupoid”.
- [`AlgebraicGeometry.groupoidInverse_left_isIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/GroupoidInverse.lean#L78), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L106) (StacksFrontier): “the inverse morphism of a groupoid scheme is an isomorphism”.
- [`Stacks.Groupoids.identity_left_comp_source_left`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean#L126), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L108) (StacksFrontier): “the identity morphism is a section of the source”.
- [`Stacks.Groupoids.identity_left_comp_target_left`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean#L131), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L110) (StacksFrontier): “the identity morphism is a section of the target”.
- [`AlgebraicGeometry.groupoidHom_map_inverse`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/GroupoidInverse.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupoidCategories.lean#L112) (StacksFrontier): “a morphism of groupoid schemes is compatible with the inverses”.

## Tag 0231, a definition

[Tag 0231](https://stacks.math.columbia.edu/tag/0231) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean#L70). The attribute's comment: “part (1): groupoid schemes”.

> A groupoid object in schemes over `S`.
>
> The fields `identity` and `inverse` are included as data, although they are uniquely determined
> by `source`, `target` and `comp`.

```lean
structure GroupoidScheme (S : Scheme.{u})
```

**`Stacks.Groupoids.GroupoidScheme.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Pullback.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Pullback.lean#L72). The attribute's comment: “part (2): morphisms of groupoid schemes”.

> A morphism of groupoid schemes.

```lean
structure Hom {S : Scheme.{u}} (G H : GroupoidScheme S)
```

## Tag 0232, a lemma

[Tag 0232](https://stacks.math.columbia.edu/tag/0232) in the Stacks Project.

**`AlgebraicGeometry.groupoidPreRelation_isPreEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidOfEquivalenceRelation.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidOfEquivalenceRelation.lean#L69).

> The pre-relation underlying a groupoid scheme is a pre-equivalence relation.

```lean
theorem groupoidPreRelation_isPreEquivalenceRelation {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsPreEquivalenceRelation (groupoidPreRelation G)
```

## Tag 0233, a lemma

[Tag 0233](https://stacks.math.columbia.edu/tag/0233) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_groupoidScheme_of_isEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidOfEquivalenceRelation.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidOfEquivalenceRelation.lean#L143).

> An equivalence relation on a scheme over `S` extends in a unique way to a groupoid scheme
> over `S`.

```lean
theorem existsUnique_groupoidScheme_of_isEquivalenceRelation (j : PreRelation R U)
    [IsEquivalenceRelation j.target j.source] :
    ∃! G : GroupoidScheme S, ExtendsRelation j G
```

## Tag 02YE, a lemma

[Tag 02YE](https://stacks.math.columbia.edu/tag/02YE) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.comp_source_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L148). The attribute's comment: “the lower-right square”.

> The square formed by composition, the second projection, and two copies of the source map
> is a pullback square: a composable pair of arrows is determined by its first member together
> with its composite.

```lean
theorem comp_source_isPullback {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsPullback G.comp (pullback.snd G.source G.target) G.source G.source
```

**`Stacks.Groupoids.GroupoidScheme.target_comp_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L197). The attribute's comment: “the upper square”.

> The upper triangle in the composition diagram, viewed as a square with two copies of its
> apex, is a pullback square: a pair of arrows with the same target is the same thing as a
> composable pair together with its composite.

```lean
theorem target_comp_isPullback {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsPullback (pullback.fst G.source G.target) G.comp G.target G.target
```

## Tag 03C6, a lemma

[Tag 03C6](https://stacks.math.columbia.edu/tag/03C6) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.comp_source_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L148). The attribute's comment: “the lower composition square of the diagram: top map the composition, verticals the second projection and the source, bottom map the source”.

> The square formed by composition, the second projection, and two copies of the source map
> is a pullback square: a composable pair of arrows is determined by its first member together
> with its composite.

```lean
theorem comp_source_isPullback {S : Scheme.{u}} (G : GroupoidScheme S) :
    IsPullback G.comp (pullback.snd G.source G.target) G.source G.source
```

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L81). The attribute's comment: “the vertical comparison”.

> The vertical map in the top left of the diagram: it sends a pair `(α, β)` with equal
> targets to the composable pair `(α, α⁻¹ ∘ β)`.

```lean
noncomputable def targetPullbackToComposable {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    pullback G.target G.target ⟶ pullback G.source G.target
```

**`AlgebraicGeometry.GroupoidScheme.fst_source_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L103). The attribute's comment: “the lower projection square”.

> The square formed by the two projections of the scheme of composable pairs together with
> the source and the target maps is a pullback square.  This is the lower-left square of the
> diagram taken with the lower horizontal maps, and it is cartesian because the scheme of
> composable pairs is by definition the fibre product of the source and the target.

```lean
theorem fst_source_isPullback {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) :
    IsPullback (pullback.fst G.source G.target) (pullback.snd G.source G.target)
      G.source G.target
```

**`AlgebraicGeometry.GroupoidScheme.id_target_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L114). The attribute's comment: “commutativity of the upper right square”.

> The upper-right square of the diagram commutes.  Both of its vertical maps are
> identities, of the arrow scheme and of the object scheme respectively, and both of its
> horizontal maps are the target map.

```lean
theorem id_target_comm {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S) :
    𝟙 G.arrows ≫ G.target = G.target ≫ 𝟙 G.objects
```

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L123). The attribute's comment: “commutativity with the first projection”.

> The comparison map preserves the first projection.  This is the lower of the two
> commutative triangles in the top left of the diagram.

```lean
theorem targetPullbackToComposable_fst {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    targetPullbackToComposable G ≫ pullback.fst G.source G.target =
      pullback.fst G.target G.target
```

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L142). The attribute's comment: “commutativity with composition”.

> Composing a pair after the change of coordinates recovers its second member.  This is
> the upper of the two commutative triangles in the top left of the diagram.

```lean
theorem targetPullbackToComposable_comp {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    targetPullbackToComposable G ≫ G.comp = pullback.snd G.target G.target
```

**`AlgebraicGeometry.GroupoidScheme.targetPullbackToComposable_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L213). The attribute's comment: “the top rows are isomorphic”.

> The vertical comparison between pairs with the same target and composable pairs is an
> isomorphism.

```lean
theorem targetPullbackToComposable_isIso {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) :
    IsIso (targetPullbackToComposable G)
```

Declarations registered for the tag:

- [`Stacks.Groupoids.GroupoidScheme.comp_source_isPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FieldExtensionEvaluation.lean#L148), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidPullbackDiagram.lean#L89) (StacksFrontier): “the lower composition square”.

## Tag 0DT8, a lemma

[Tag 0DT8](https://stacks.math.columbia.edu/tag/0DT8) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidBaseChange.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/GroupoidBaseChange.lean#L82).

> Base-changing the object and arrow schemes of a groupoid scheme, and all its structure
> maps, produces a groupoid scheme over the new base whose projections form a morphism of
> groupoid schemes.

```lean
theorem exists_baseChange {S S' : Scheme.{u}} (f : S' ⟶ S)
    (G : Stacks.Groupoids.GroupoidScheme S) : Nonempty (BaseChange f G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.13, Tag 0230](https://stacks.math.columbia.edu/tag/0230)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
