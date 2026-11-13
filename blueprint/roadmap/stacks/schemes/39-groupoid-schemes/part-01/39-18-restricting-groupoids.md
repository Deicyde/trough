---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.restrict, AlgebraicGeometry.GroupoidScheme.restrictGroupoid_isRestriction, AlgebraicGeometry.restriction_groupoidScheme_agrees_restriction_preRelation, AlgebraicGeometry.restrictStabilizerIso
statement: formalized
proof: formalized
---

# 39.18 Restricting groupoids

Section 39.18 of the Stacks Project, [Tag 02VA](https://stacks.math.columbia.edu/tag/02VA). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02VB, a lemma

[Tag 02VB](https://stacks.math.columbia.edu/tag/02VB) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoid.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoid.lean#L69).

> Restriction of a groupoid scheme along a morphism to its scheme of objects.

```lean
noncomputable def restrict {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S)
    {U' : Over S} (g : U' ⟶ G.objects) : Restriction G g
```

**`AlgebraicGeometry.GroupoidScheme.restrictGroupoid_isRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoidDisplayed.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoidDisplayed.lean#L400).

> **Stacks Lemma 02VB.**  Let `(U, R, s, t, c)` be a groupoid scheme over `S` and
> `g : U' ⟶ U` a morphism.  With `R' = (U' ×_{g, U, t} R) ×_R (R ×_{s, U, g} U')` the iterated
> fibre product of the displayed diagram, `s' : R' ⟶ R ×_{s, U, g} U' ⟶ U'` and
> `t' : R' ⟶ U' ×_{g, U, t} R ⟶ U'`, the groupoid scheme `restrictGroupoid G g` is
> `(U', R', s', t', c')` for the canonical composition law
> `c' = Stacks.Groupoids.GroupoidScheme.restrictionComposition`, which is characterized as the
> morphism on composable pairs whose source, target and underlying arrow of `R` are those of the
> second factor, of the first factor, and the composite in `R`.  The morphism of groupoid schemes
> `restrictGroupoidHom G g` is `g` on objects and the projection `R' ⟶ R` on arrows.  Finally, on
> every scheme `T` over `S`, the functor of groupoids
> `(U'(T), R'(T), s', t', c') ⟶ (U(T), R(T), s, t, c)` is the restriction of
> `(U(T), R(T), s, t, c)` via `U'(T) ⟶ U(T)`: there is an isomorphism of categories to the
> induced groupoid `InducedCategory (U(T), R(T), s, t, c) (· ≫ g)`, the identity on objects,
> carrying the functor to the canonical functor `inducedFunctor` of the restriction.

```lean
theorem restrictGroupoid_isRestriction :
    (restrictGroupoid G g).objects = U' ∧
    (restrictGroupoid G g).arrows =
      pullback (pullback.snd g G.target) (pullback.fst G.source g) ∧
    (restrictGroupoid G g).source =
      pullback.snd (pullback.snd g G.target) (pullback.fst G.source g) ≫
        pullback.snd G.source g ∧
    (restrictGroupoid G g).target =
      pullback.fst (pullback.snd g G.target) (pullback.fst G.source g) ≫
        pullback.fst g G.target ∧
    (restrictGroupoid G g).comp = G.restrictionComposition g ∧
    (∀ {T : Over S} (a b : T ⟶ (restrictGroupoid G g).arrows)
        (w : a ≫ (restrictGroupoid G g).source = b ≫ (restrictGroupoid G g).target),
      (pullback.lift a b w ≫ (restrictGroupoid G g).comp) ≫ (restrictGroupoid G g).source =
          b ≫ (restrictGroupoid G g).source ∧
        (pullback.lift a b w ≫ (restrictGroupoid G g).comp) ≫ (restrictGroupoid G g).target =
          a ≫ (restrictGroupoid G g).target ∧
        (pullback.lift a b w ≫ (restrictGroupoid G g).comp) ≫
            (restrictGroupoidHom G g).mapArrows =
          G.compose (a ≫ (restrictGroupoidHom G g).mapArrows)
            (b ≫ (restrictGroupoidHom G g).mapArrows)
            (G.restriction_compose_condition g a b w)) ∧
    (restrictGroupoidHom G g).mapObjects = g ∧
    (restrictGroupoidHom G g).mapArrows =
      pullback.fst (pullback.snd g G.target) (pullback.fst G.source g) ≫
        pullback.snd g G.target ∧
    ∀ T : Over S,
      (∀ x, (restrictGroupoidEvaluationFunctor G g T).obj x = x) ∧
      restrictGroupoidEvaluationFunctor G g T ⋙ restrictGroupoidEvaluationInverse G g T =
        𝟭 _ ∧
      restrictGroupoidEvaluationInverse G g T ⋙ restrictGroupoidEvaluationFunctor G g T =
        𝟭 _ ∧
      restrictGroupoidEvaluationFunctor G g T ⋙
          inducedFunctor (restrictGroupoidEvaluationObj G g T) =
        (restrictGroupoidHom G g).evaluation T
```

## Tag 02VC, a definition

[Tag 02VC](https://stacks.math.columbia.edu/tag/02VC) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoid.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionGroupoid.lean#L69). The attribute's comment: “the restriction R|\_\{U'} of a groupoid scheme to U', with its morphism to the”.

> Restriction of a groupoid scheme along a morphism to its scheme of objects.

```lean
noncomputable def restrict {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S)
    {U' : Over S} (g : U' ⟶ G.objects) : Restriction G g
```

## Tag 02VD, a lemma

[Tag 02VD](https://stacks.math.columbia.edu/tag/02VD) in the Stacks Project.

**`AlgebraicGeometry.restriction_groupoidScheme_agrees_restriction_preRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionRelation.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionRelation.lean#L417).

> Restricting groupoid schemes and restricting (pre-)equivalence relations
> agree via the constructions of Tags 0232 and 0233.
>
> 1. For a groupoid scheme `G` and `g : U' ⟶ G.objects`, the pre-relation of the restriction
>    `G|_{U'}` (Tag 02VC) agrees with the restriction (Tag 02V9) of the pre-relation of `G`
>    (Tag 0232): there is a unique isomorphism of their schemes of arrows compatible with the
>    maps to `U' ×_S U'` and to the arrows of `G`.
> 2. For an equivalence relation `j : R ⟶ U ×_S U` and `g : U' ⟶ U`, the groupoid scheme of the
>    restricted relation `j|_{U'}` (Tag 0233) agrees with the restriction to `U'` of the groupoid
>    scheme of `j`: there is a unique isomorphism of groupoid schemes between them which is the
>    identity of `U'` on objects and commutes with the maps of arrows to `R`. Being a pair of
>    mutually inverse morphisms of groupoid schemes, it identifies the compositions, identities
>    and inverses of the two groupoid structures.

```lean
theorem restriction_groupoidScheme_agrees_restriction_preRelation {S : Scheme.{u}} :
    (∀ (G : GroupoidScheme S) {U' : Over S} (g : U' ⟶ G.objects),
      ∃! e : (GroupoidScheme.restrict G g).groupoid.arrows ≅
          PreRelation.restriction (groupoidPreRelation G) g,
        e.hom ≫ PreRelation.restrict (groupoidPreRelation G) g =
            groupoidPreRelation (GroupoidScheme.restrict G g).groupoid ≫
              prod.map (eqToHom (GroupoidScheme.restrict G g).objects_eq)
                (eqToHom (GroupoidScheme.restrict G g).objects_eq) ∧
          e.hom ≫ pullback.snd (prod.map g g) (groupoidPreRelation G) =
            (GroupoidScheme.restrict G g).hom.mapArrows) ∧
    (∀ {R U U' : Over S} (j : PreRelation R U) [IsEquivalenceRelation j.target j.source]
        (g : U' ⟶ U),
      ∃! e : GroupoidScheme.Isomorphism
          (groupoidSchemeOfIsEquivalenceRelation (PreRelation.restrict j g))
          (GroupoidScheme.restrict (groupoidSchemeOfIsEquivalenceRelation j)
            (g ≫ eqToHom
              (groupoidSchemeOfIsEquivalenceRelation_extendsRelation j).objects_eq.symm)).groupoid,
        e.hom.mapObjects = eqToHom
            ((groupoidSchemeOfIsEquivalenceRelation_extendsRelation
                (PreRelation.restrict j g)).objects_eq.trans
              (GroupoidScheme.restrict _ _).objects_eq.symm) ∧
          e.hom.mapArrows ≫ (GroupoidScheme.restrict _ _).hom.mapArrows ≫
              eqToHom (groupoidSchemeOfIsEquivalenceRelation_extendsRelation j).arrows_eq =
            eqToHom (groupoidSchemeOfIsEquivalenceRelation_extendsRelation
                (PreRelation.restrict j g)).arrows_eq ≫ pullback.snd (prod.map g g) j)
```

## Tag 04ML, a lemma

[Tag 04ML](https://stacks.math.columbia.edu/tag/04ML) in the Stacks Project.

**`AlgebraicGeometry.restrictStabilizerIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionStabilizer.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/RestrictionStabilizer.lean#L238).

> **Stacks Project, Tag 04ML.** The stabilizer of a restricted groupoid scheme is canonically
> the base change of the original stabilizer.

```lean
noncomputable def restrictStabilizerIso {S : Scheme.{u}} (G : GroupoidScheme S)
    {U' : Scheme.{u}} (g : U' ⟶ G.objects.left) :
    let U'_S : Over S := Over.mk (g ≫ G.objects.hom)
    let g' : U'_S ⟶ G.objects := Over.homMk g
    Over.mk ((stabilizer (GroupoidScheme.restrict G g').groupoid).hom ≫
      eqToHom (congrArg Over.left (GroupoidScheme.restrict G g').objects_eq)) ≅
      Over.mk (pullback.fst g (stabilizer G).hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.18, Tag 02VA](https://stacks.math.columbia.edu/tag/02VA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
