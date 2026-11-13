---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.restrict_isRestriction, AlgebraicGeometry.GroupoidInAlgebraicSpaces.restrict, AlgebraicGeometry.GroupoidInAlgebraicSpaces.existsUnique_iso_restriction_groupoidPreRelation, AlgebraicGeometry.Space.existsUnique_isomorphism_restrict_groupoidOfIsEquivalenceRelation
statement: formalized
proof: formalized
---

# 78.17 Restricting groupoids

Section 78.17 of the Stacks Project, [Tag 044A](https://stacks.math.columbia.edu/tag/044A). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 044B, a lemma

[Tag 044B](https://stacks.math.columbia.edu/tag/044B) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.restrict_isRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidRestriction/Restrict.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidRestriction/Restrict.lean#L588).

> **Stacks 044B.** Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over `B` and let
> `g : U' ⟶ U` be a morphism of algebraic spaces. Form the fibre product squares
> `P₁ = U' ×_{g, U, t} R` (projections `pU`, `pR`), `P₂ = R ×_{s, U, g} U'` (projections `qR`,
> `qU`), and `R' = P₁ ×_{pR, R, qR} P₂` (projections `a`, `b`), and put `t' = a ≫ pU`,
> `s' = b ≫ qU`. Then the restriction `(restrict G g).groupoid` is a groupoid in algebraic spaces
> over `B` whose space of objects is `U'` (over `B` through `g`), whose space of arrows is `R'`
> (over `B` through `R`), whose source and target are `s'` and `t'`, and whose composition law
> `c' : R' ×_{s', U', t'} R' ⟶ R'` keeps the target of the first arrow and the source of the second
> and composes the two underlying arrows by `c`. The maps `g : U' ⟶ U` and `a ≫ pR : R' ⟶ R` are
> the two components of the morphism `(restrict G g).hom` of groupoids in algebraic spaces over `B`.
>
> Moreover, for every scheme `T` of the site, the functor of groupoids
> `(U'(T), R'(T), s', t', c') ⟶ (U(T), R(T), s, t, c)` is the restriction of `(U(T), R(T), s, t, c)`
> via `U'(T) ⟶ U(T)`: an element of `R'(T)` is exactly a triple `(x, r, y)` with `x, y ∈ U'(T)`,
> `r ∈ R(T)`, `t(r) = g(x)` and `s(r) = g(y)`, with `t'` and `s'` the outer projections and the
> composite of `(x, r, y)` and `(y, r'', z)` equal to `(x, c(r, r''), z)`; the functor is `g` on
> objects and is fully faithful.
>
> The same holds for the `T`-points over `B`, in the source's sense of a scheme `T` over `B`: for a
> scheme `T` of the site and a point `b ∈ B(T)`, the groupoid `(U'(T), R'(T), s', t', c')` of
> `T`-points of the restriction lying over `b` maps to the groupoid `(U(T), R(T), s, t, c)` of
> `T`-points of `G` lying over `b`, and this functor is the restriction along `U'(T) ⟶ U(T)`: an
> arrow over `b` is exactly a triple `(x, r, y)` over `b` as above, the composite of two arrows over
> `b` lies over `b` and is computed as above, and the functor, which is `g` on objects and the
> functor on all `T`-points on arrows, is fully faithful.

```lean
public theorem restrict_isRestriction
    {C : BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicSpaces C S hS}
    (G : GroupoidInAlgebraicSpaces C S hS B)
    {U' : AlgebraicSpaces C S hS} (g : U' ⟶ G.objects) :
    let H := (restrict G g).groupoid
    let φ := (restrict G g).hom
    ∃ (P₁ : AlgebraicSpaces C S hS) (pU : P₁ ⟶ U') (pR : P₁ ⟶ G.arrows)
      (P₂ : AlgebraicSpaces C S hS) (qR : P₂ ⟶ G.arrows) (qU : P₂ ⟶ U')
      (a : H.arrows ⟶ P₁) (b : H.arrows ⟶ P₂),
      IsPullback pU pR g G.target ∧ IsPullback qR qU G.source g ∧ IsPullback a b pR qR ∧
      H.objects = U' ∧ H.target = a ≫ pU ∧ H.source = b ≫ qU ∧
      H.objectsToBase = g ≫ G.objectsToBase ∧
      H.arrowsToBase = (a ≫ pR) ≫ G.arrowsToBase ∧
      H.comp ≫ H.target = fiberProductFst H.source H.target ≫ H.target ∧
      H.comp ≫ H.source = fiberProductSnd H.source H.target ≫ H.source ∧
      (∃ m : AlgebraicSpaces.fiberProduct C S hS H.source H.target ⟶
          AlgebraicSpaces.fiberProduct C S hS G.source G.target,
        m ≫ fiberProductFst G.source G.target = fiberProductFst H.source H.target ≫ a ≫ pR ∧
        m ≫ fiberProductSnd G.source G.target = fiberProductSnd H.source H.target ≫ a ≫ pR ∧
        H.comp ≫ a ≫ pR = m ≫ G.comp) ∧
      φ.toGroupoidHom.mapObjects = g.hom ∧
      φ.toGroupoidHom.mapArrows = (a ≫ pR).hom ∧
      (∀ T : (BigFppfOver C S hS)ᵒᵖ,
        (∀ (x y : U'.obj.obj T) (r : G.arrows.obj.obj T),
          G.target.hom.app T r = g.hom.app T x → G.source.hom.app T r = g.hom.app T y →
          ∃! z : H.arrows.obj.obj T, H.target.hom.app T z = x ∧
            (a ≫ pR).hom.app T z = r ∧ H.source.hom.app T z = y) ∧
        (∀ (z w : H.arrows.obj.obj T) (h : H.source.hom.app T z = H.target.hom.app T w)
          (h' : G.source.hom.app T ((a ≫ pR).hom.app T z) =
            G.target.hom.app T ((a ≫ pR).hom.app T w)),
          H.target.hom.app T (H.toGroupoidInFunctors.compose T z w h) =
              H.target.hom.app T z ∧
            (a ≫ pR).hom.app T (H.toGroupoidInFunctors.compose T z w h) =
              G.toGroupoidInFunctors.compose T ((a ≫ pR).hom.app T z)
                ((a ≫ pR).hom.app T w) h' ∧
            H.source.hom.app T (H.toGroupoidInFunctors.compose T z w h) =
              H.source.hom.app T w) ∧
        (∀ x : U'.obj.obj T, (φ.toGroupoidHom.evaluation T).obj x = g.hom.app T x) ∧
        Nonempty (φ.toGroupoidHom.evaluation T).FullyFaithful) ∧
      ∀ (T : (BigFppfOver C S hS)ᵒᵖ) (b : B.obj.obj T),
        (∀ (x y : U'.obj.obj T) (r : G.arrows.obj.obj T),
          H.objectsToBase.hom.app T x = b → H.objectsToBase.hom.app T y = b →
          G.arrowsToBase.hom.app T r = b →
          G.target.hom.app T r = g.hom.app T x → G.source.hom.app T r = g.hom.app T y →
          ∃! z : H.arrows.obj.obj T, H.arrowsToBase.hom.app T z = b ∧
            H.target.hom.app T z = x ∧ (a ≫ pR).hom.app T z = r ∧
            H.source.hom.app T z = y) ∧
        (∀ (z w : H.arrows.obj.obj T) (h : H.source.hom.app T z = H.target.hom.app T w)
          (h' : G.source.hom.app T ((a ≫ pR).hom.app T z) =
            G.target.hom.app T ((a ≫ pR).hom.app T w)),
          H.arrowsToBase.hom.app T z = b → H.arrowsToBase.hom.app T w = b →
          H.arrowsToBase.hom.app T (H.toGroupoidInFunctors.compose T z w h) = b ∧
          H.target.hom.app T (H.toGroupoidInFunctors.compose T z w h) =
              H.target.hom.app T z ∧
            (a ≫ pR).hom.app T (H.toGroupoidInFunctors.compose T z w h) =
              G.toGroupoidInFunctors.compose T ((a ≫ pR).hom.app T z)
                ((a ≫ pR).hom.app T w) h' ∧
            H.source.hom.app T (H.toGroupoidInFunctors.compose T z w h) =
              H.source.hom.app T w) ∧
        ∃ F : ObjectProperty.FullSubcategory
              (fun x : H.toGroupoidInFunctors.Evaluation T => H.objectsToBase.hom.app T x = b) ⥤
            ObjectProperty.FullSubcategory
              (fun x : G.toGroupoidInFunctors.Evaluation T => G.objectsToBase.hom.app T x = b),
          (∀ x, (F.obj x).obj = g.hom.app T x.obj) ∧
          F ⋙ ObjectProperty.ι _ = ObjectProperty.ι _ ⋙ φ.toGroupoidHom.evaluation T ∧
          Nonempty F.FullyFaithful
```

## Tag 044C, a definition

[Tag 044C](https://stacks.math.columbia.edu/tag/044C) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.restrict`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidRestriction/Restrict.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupoidRestriction/Restrict.lean#L59). The attribute's comment: “the restriction of the groupoid to U'”.

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

## Tag 044D, a lemma

[Tag 044D](https://stacks.math.columbia.edu/tag/044D) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.existsUnique_iso_restriction_groupoidPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionComparison.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionComparison.lean#L368). The attribute's comment: “restricting a groupoid, then taking its pre-relation”.

> **Stacks 044D**, restricting a groupoid and then taking its pre-relation. Let `G` be a
> groupoid in algebraic spaces over `B` and `g : U' ⟶ U` a morphism to its space of objects. The
> pre-relation `j' = (t', s') : R' ⟶ U' ×_B U'` of the restriction `G|_{U'}` of **Stacks 044C**,
> whose arrow space is `R' = U' ×_{g, U, t} R ×_{s, U, g} U'`, is the restriction along `g`, in the
> sense of **Stacks 043D**, of the pre-relation `j = (t, s) : R ⟶ U ×_B U` of `G` (**Stacks 043X**):
> `R' = (U' ×_B U') ×_{U ×_B U} R`. Precisely, there is exactly one isomorphism from the arrow space
> of `G|_{U'}` to the restricted pre-relation's arrow space taking the restricted pre-relation to
> `j'` and its projection to `R` to the map on arrows of the morphism `G|_{U'} ⟶ G`.

```lean
theorem existsUnique_iso_restriction_groupoidPreRelation (G : GroupoidInAlgebraicSpaces C S hS B)
    {U' : AlgebraicSpaces C S hS} (g : U' ⟶ G.objects) :
    ∃! e : (Over.mk (G.restrict g).groupoid.arrowsToBase.hom : Over B.obj) ≅
        Space.PreRelation.restriction (Space.groupoidPreRelation G) (restrictionObjectsHom G g),
      e.hom ≫ Space.PreRelation.restrict (Space.groupoidPreRelation G)
          (restrictionObjectsHom G g) = Space.groupoidPreRelation (G.restrict g).groupoid ∧
        e.hom ≫ pullback.snd (prod.map (restrictionObjectsHom G g) (restrictionObjectsHom G g))
            (Space.groupoidPreRelation G) =
          Over.homMk (G.restrict g).hom.toGroupoidHom.mapArrows (G.restrict g).hom.mapArrows_over
```

**`AlgebraicGeometry.Space.existsUnique_isomorphism_restrict_groupoidOfIsEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionComparison.lean, line 581](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Quotient/RestrictionComparison.lean#L581). The attribute's comment: “restricting an equivalence relation, then taking its groupoid”.

> **Stacks 044D**, restricting an equivalence relation and then taking its groupoid. Let
> `j : R ⟶ U ×_B U` be an equivalence relation of algebraic spaces over `B`, let
> `(U, R, s, t, c)` be the groupoid in algebraic spaces it extends to (**Stacks 043Y**), and let
> `g : U' ⟶ U` be a morphism of algebraic spaces. The groupoid in algebraic spaces of the
> restricted equivalence relation `j' : R' = (U' ×_B U') ×_{U ×_B U} R ⟶ U' ×_B U'`
> (**Stacks 043D**) is the restriction `(U, R, s, t, c)|_{U'}` of **Stacks 044C**: there is exactly
> one isomorphism of groupoids in algebraic spaces between them which is the identity of `U'` on
> objects, and it takes the projection `R' ⟶ R` to the map on arrows of the morphism
> `(U, R, s, t, c)|_{U'} ⟶ (U, R, s, t, c)` of **Stacks 044B**.

```lean
theorem existsUnique_isomorphism_restrict_groupoidOfIsEquivalenceRelation
    (j : PreRelation (Over.mk qR.hom) (Over.mk qU.hom)) [IsEquivalenceRelation j.target j.source]
    (g : U' ⟶ U) :
    ∃! e : Isomorphism (groupoidOfIsEquivalenceRelation (restrictSpace j g))
        ((groupoidOfIsEquivalenceRelation j).restrict g).groupoid,
      e.hom.toGroupoidHom.mapObjects = 𝟙 U'.obj ∧
        e.hom.toGroupoidHom.mapArrows ≫
            ((groupoidOfIsEquivalenceRelation j).restrict g).hom.toGroupoidHom.mapArrows =
          (pullback.snd (prod.map (overHomOfComp qU g) (overHomOfComp qU g)) j).left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.17, Tag 044A](https://stacks.math.columbia.edu/tag/044A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
