---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePartGroupoid_spec, AlgebraicGeometry.Space.FinitePartUniversalOpen, AlgebraicGeometry.Space.finitePartUniversalOpen, AlgebraicGeometry.Space.FinitePartGroupoid, AlgebraicGeometry.Space.nonempty_finitePartGroupoid, AlgebraicGeometry.Space.finitePartGroupoid, AlgebraicGeometry.Space.finitePartGroupoidHom, AlgebraicGeometry.Space.finitePartGroupoid_objectProjection_spec
statement: formalized
proof: formalized
---

# 79.14 The finite part of a groupoid

Section 79.14 of the Stacks Project, [Tag 04RT](https://stacks.math.columbia.edu/tag/04RT). 2 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04RT, the section

[Tag 04RT](https://stacks.math.columbia.edu/tag/04RT) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePartGroupoid_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidSpec.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidSpec.lean#L110). The attribute's comment: “the finite part (U', Z\_univ, s', t', c', e', i') of the groupoid, with the rules for its structure morphisms and its morphism of groupoids to (U, R, s, t, c, e, i)”.

> **Stacks 04RT, the finite part of a groupoid.** Let `(U, R, s, t, c, e, i)` be a groupoid in
> algebraic spaces over `B` whose source morphism `s` is separated and locally of finite type. The
> construction of Stacks 04RT produces the following, all of which are recorded here for the finite
> part `fp = finitePart G hsep hft`, its groupoid `finitePartGroupoid hsep hft` and the canonical
> morphism `finitePartGroupoidHom hsep hft`.
>
> * The object space `U'` is `(R_s/U, e)_fin`: the inclusion of `U'` into `(R_s/U)_fin` is an open
>   immersion whose range is the subfunctor of pairs containing the unit.
> * The morphism `g : U' ⟶ U` is the projection of `(R_s/U)_fin` restricted to `U'`, and is étale.
> * `Z_univ` is the universal open subspace of the fibre product of `g` and `s`, finite over `U'`,
>   namely the pair which the inclusion of `U'` names under Stacks 04PE; it is closed as well as
>   open, and the base change of the unit factors through it.
> * The groupoid has object space `U'` and arrow space `Z_univ`, with
>   - `s' : (u, Z, z) ↦ (u, Z)`, the first projection;
>   - `t' : (u, Z, z) ↦ (t ∘ z, c(Z, i ∘ z))`: the pair that `t'` names is the translate of the
>     tautological pair by the tautological arrow, and its base morphism is `t ∘ z`;
>   - `e' : (u, Z) ↦ (u, Z, e ∘ u)`, the unit of the groupoid;
>   - `i' : (u, Z, z) ↦ (t ∘ z, c(Z, i ∘ z), i ∘ z)`, the inverse of the groupoid;
>   - `c' : ((u₁, Z₁, z₁), (u₂, Z₂, z₂)) ↦ (u₂, Z₂, z₁ ∘ z₂)`, the composition of the groupoid.
> * The canonical morphism of groupoids over `B` to `(U, R, s, t, c, e, i)` is `g` on objects and
>   `(u, Z, z) ↦ z` on arrows.
>
> The hypotheses are on `s` alone; the source also assumes `t` separated and locally of finite type,
> which the construction does not use. As in the rest of the formalization, the ambient fibre
> product of `Z_univ` is `U' ×_{g, U, s} R` rather than `R ×_{s, U, g} U'`.

```lean
theorem finitePartGroupoid_spec (hsep : Space.IsSeparated C S hS G.source.hom)
    (hft : Space.IsLocallyOfFiniteType C S hS G.source.hom) :
    -- `U' = (R_s/U, e)_fin`, an open subspace of `(R_s/U)_fin`
    Subfunctor.range (finitePart G hsep hft).inclusion =
        (Space.finitePartWithSection C S hS G.source (identityHom G)
          (identityHom_comp_source G)).toSubfunctor ∧
      Space.IsOpenImmersion C S hS (finitePart G hsep hft).inclusion ∧
      -- `g : U' ⟶ U` is the projection of the finite part, and is étale
      (finitePart G hsep hft).pair.toBase.hom =
        (finitePart G hsep hft).inclusion ≫
          (Space.finiteOpenSubspacePresheaf C S hS G.source).baseMap ∧
      Space.IsEtale C S hS (finitePart G hsep hft).pair.toBase.hom ∧
      -- `Z_univ` is universal, closed, and contains the base change of the unit
      (finitePart G hsep hft).pair =
        (Space.finiteOpenSubspaceEquiv C S hS G.source (finitePart G hsep hft).objects).1
          (finitePart G hsep hft).inclusion ∧
      Space.IsClosedSubspace C S hS (finitePart G hsep hft).pair.subspace ∧
      Space.ContainsSection C S hS G.source (identityHom G) (identityHom_comp_source G)
        (finitePart G hsep hft).pair ∧
      -- the groupoid has object space `U'` and arrow space `Z_univ`
      (finitePartGroupoid hsep hft).objects = (finitePart G hsep hft).objects ∧
      (finitePartGroupoid hsep hft).arrows = FinitePart.arrowSpace (finitePart G hsep hft) ∧
      -- `s' : (u, Z, z) ↦ (u, Z)`
      (finitePartGroupoid hsep hft).source.hom = FinitePart.sourceHom (finitePart G hsep hft) ∧
      -- `t' : (u, Z, z) ↦ (t ∘ z, c(Z, i ∘ z))`
      (finitePartGroupoid hsep hft).target.hom = targetHom hsep hft ∧
      (Space.finiteOpenSubspaceEquiv C S hS G.source
          (FinitePart.arrowSpace (finitePart G hsep hft))).1
          (targetHom hsep hft ≫ (finitePart G hsep hft).inclusion) =
        translatePair (FinitePart.sourcePair (finitePart G hsep hft))
          (FinitePart.arrowMap (finitePart G hsep hft))
          (FinitePart.arrowMap_comp_source (finitePart G hsep hft)) ∧
      targetHom hsep hft ≫ (finitePart G hsep hft).pair.toBase.hom =
        (finitePart G hsep hft).arrowHom ≫ G.target.hom ∧
      -- `e' : (u, Z) ↦ (u, Z, e ∘ u)`
      (identityHom (finitePartGroupoid hsep hft)).hom = unitHom hsep hft ∧
      unitHom hsep hft ≫ FinitePart.sourceHom (finitePart G hsep hft) =
        𝟙 (finitePart G hsep hft).objects.obj ∧
      unitHom hsep hft ≫ (finitePart G hsep hft).arrowHom =
        (finitePart G hsep hft).pair.toBase.hom ≫ (identityHom G).hom ∧
      -- `i' : (u, Z, z) ↦ (t ∘ z, c(Z, i ∘ z), i ∘ z)`
      (inverseHom (finitePartGroupoid hsep hft)).hom = invHom hsep hft ∧
      invHom hsep hft ≫ FinitePart.sourceHom (finitePart G hsep hft) = targetHom hsep hft ∧
      invHom hsep hft ≫ (finitePart G hsep hft).arrowHom =
        (finitePart G hsep hft).arrowHom ≫ (inverseHom G).hom ∧
      -- `c' : ((u₁, Z₁, z₁), (u₂, Z₂, z₂)) ↦ (u₂, Z₂, z₁ ∘ z₂)`
      (finitePartGroupoid hsep hft).comp.hom = compHom hsep hft ∧
      compHom hsep hft ≫ FinitePart.sourceHom (finitePart G hsep hft) =
        pullback.snd (FinitePart.sourceHom (finitePart G hsep hft)) (targetHom hsep hft) ≫
          FinitePart.sourceHom (finitePart G hsep hft) ∧
      compHom hsep hft ≫ (finitePart G hsep hft).arrowHom =
        composeHom
          (pullback.fst (FinitePart.sourceHom (finitePart G hsep hft)) (targetHom hsep hft) ≫
            (finitePart G hsep hft).arrowHom)
          (pullback.snd (FinitePart.sourceHom (finitePart G hsep hft)) (targetHom hsep hft) ≫
            (finitePart G hsep hft).arrowHom)
          (FinitePart.composable_compose (finitePart G hsep hft) (targetHom hsep hft)
            (targetHom_comp_inclusion hsep hft)) ∧
      -- the canonical morphism of groupoids: `g` on objects, `(u, Z, z) ↦ z` on arrows
      (finitePartGroupoidHom hsep hft).toGroupoidHom.mapObjects =
        (finitePart G hsep hft).pair.toBase.hom ∧
      (finitePartGroupoidHom hsep hft).toGroupoidHom.mapArrows =
        (finitePart G hsep hft).arrowHom
```

## Tag 04RU, a lemma

[Tag 04RU](https://stacks.math.columbia.edu/tag/04RU) in the Stacks Project.

**`AlgebraicGeometry.Space.FinitePartUniversalOpen`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 1845](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L1845). The attribute's comment: “clauses (1) and (2) stated; not the groupoid structure”.

> **Stacks 04RU, clauses (1) and (2).** The two structure spaces of the finite part of a
> groupoid in algebraic spaces over `B`: the object space `U'` with its étale projection
> `g : U' ⟶ U`, identified with `(R_s/U, e)_fin ⟶ U`, and the universal open and closed subspace
> `Z_univ ⊂ R ×_{s, U, g} U'` finite over `U'` which contains the base change of the unit.

```lean
public structure FinitePartUniversalOpen
    {C : AlgebraicGeometry.BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicGeometry.AlgebraicSpaces C S hS}
    (G : AlgebraicGeometry.GroupoidInAlgebraicSpaces C S hS B)
```

**`AlgebraicGeometry.Space.finitePartUniversalOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 1890](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L1890). The attribute's comment: “clauses (1) and (2); not the groupoid structure or its morphism”.

> **Stacks 04RU, clauses (1) and (2).** For a groupoid in algebraic spaces over `B` whose
> source and target are separated and locally of finite type, the object space `(R_s/U, e)_fin`
> with its étale projection to `U` and the universal open and closed subspace of
> `R ×_{s, U, g} U'` finite over `U'` containing the base change of the unit.

```lean
public noncomputable def finitePartUniversalOpen
    {C : AlgebraicGeometry.BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicGeometry.AlgebraicSpaces C S hS}
    (G : AlgebraicGeometry.GroupoidInAlgebraicSpaces C S hS B)
    (hs_sep : AlgebraicGeometry.Space.IsSeparated C S hS G.source.hom)
    (_ht_sep : AlgebraicGeometry.Space.IsSeparated C S hS G.target.hom)
    (hs_lft : AlgebraicGeometry.Space.IsLocallyOfFiniteType C S hS G.source.hom)
    (_ht_lft : AlgebraicGeometry.Space.IsLocallyOfFiniteType C S hS G.target.hom) :
    FinitePartUniversalOpen G
```

**`AlgebraicGeometry.Space.FinitePartGroupoid`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 1948](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L1948). The attribute's comment: “clause (3), the groupoid structure on the finite part and its morphism to R”.

> **Stacks 04RU, clause (3).** The groupoid in algebraic spaces
> `(U', Z_univ, s', t', c')` carried by the finite part of `(U, R, s, t, c)`, together with its
> canonical morphism of groupoids to `(U, R, s, t, c)` over `B`.

```lean
public structure FinitePartGroupoid
    {C : AlgebraicGeometry.BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicGeometry.AlgebraicSpaces C S hS}
    (G : AlgebraicGeometry.GroupoidInAlgebraicSpaces C S hS B)
```

**`AlgebraicGeometry.Space.nonempty_finitePartGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2007](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2007). The attribute's comment: “clause (3), the groupoid structure on the finite part and its morphism to R”.

> **Stacks 04RU, clause (3).** For a groupoid in algebraic spaces over `B` whose source and
> target are separated and locally of finite type, the finite part carries a groupoid
> `(U', Z_univ, s', t', c')` together with a morphism of groupoids to `(U, R, s, t, c)`.

```lean
public theorem nonempty_finitePartGroupoid
    {C : AlgebraicGeometry.BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicGeometry.AlgebraicSpaces C S hS}
    (G : AlgebraicGeometry.GroupoidInAlgebraicSpaces C S hS B)
    (hs_sep : AlgebraicGeometry.Space.IsSeparated C S hS G.source.hom)
    (_ht_sep : AlgebraicGeometry.Space.IsSeparated C S hS G.target.hom)
    (hs_lft : AlgebraicGeometry.Space.IsLocallyOfFiniteType C S hS G.source.hom)
    (_ht_lft : AlgebraicGeometry.Space.IsLocallyOfFiniteType C S hS G.target.hom) :
    Nonempty (FinitePartGroupoid G)
```

**`AlgebraicGeometry.Space.finitePartGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2728](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2728). The attribute's comment: “the groupoid (U', Z\_univ, s', t', c', e', i') on the finite part”.

> **Stacks 04RU.** The groupoid in algebraic spaces `(U', Z_univ, s', t', c', e', i')` over `B`
> carried by the finite part of `(U, R, s, t, c, e, i)`.

```lean
public noncomputable def finitePartGroupoid :
    AlgebraicGeometry.GroupoidInAlgebraicSpaces C S hS B
```

**`AlgebraicGeometry.Space.finitePartGroupoidHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2735](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2735). The attribute's comment: “the canonical morphism of groupoids over B to (U, R, s, t, c, e, i)”.

> **Stacks 04RU.** The canonical morphism of groupoids in algebraic spaces over `B`
> `(U', Z_univ, s', t', c', e', i') ⟶ (U, R, s, t, c, e, i)` whose existence the lemma asserts.

```lean
public noncomputable def finitePartGroupoidHom :
    AlgebraicGeometry.GroupoidInAlgebraicSpaces.Hom
      (finitePartGroupoid G hs_sep ht_sep hs_lft ht_lft) G
```

**`AlgebraicGeometry.Space.finitePartGroupoid_objectProjection_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2778](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2778). The attribute's comment: “clause (1), g : U' ⟶ U is identified with (R\_s/U, e)\_fin ⟶ U”.

> **Stacks 04RU, clause (1).** Under the identification of `U'` with `(R_s/U, e)_fin` the
> projection `g : U' ⟶ U` is the projection of the finite part.

```lean
public theorem finitePartGroupoid_objectProjection_spec :
    (finitePartGroupoidObjectProjection G hs_sep ht_sep hs_lft ht_lft).hom =
      (finitePartGroupoidObjectsEquiv G hs_sep ht_sep hs_lft ht_lft).hom ≫
        (finitePartWithSection C S hS G.source
          (finitePartGroupoidUnit G hs_sep ht_sep hs_lft ht_lft)
          (finitePartGroupoidUnit_source G hs_sep ht_sep hs_lft ht_lft)).toSubfunctor.ι ≫
        (AlgebraicGeometry.Space.finiteOpenSubspacePresheaf C S hS G.source).baseMap
```

**`AlgebraicGeometry.Space.finitePartGroupoidUniversalOpen_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2809](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2809). The attribute's comment: “clause (2), Z\_univ is the universal finite open subspace of R ×\_\{s, U, g} U'”.

> **Stacks 04RU, clause (2), universality.** `Z_univ` is the finite open subspace of
> `R ×_{s, U, g} U'` classified by the inclusion of `U'` into the finite part of `s`; this is what
> makes it the universal such subspace.

```lean
public theorem finitePartGroupoidUniversalOpen_spec :
    (finiteOpenSubspaceEquiv C S hS G.source
        (finitePartGroupoid G hs_sep ht_sep hs_lft ht_lft).objects).1
      ((finitePartGroupoidObjectsEquiv G hs_sep ht_sep hs_lft ht_lft).hom ≫
        (finitePartWithSection C S hS G.source
          (finitePartGroupoidUnit G hs_sep ht_sep hs_lft ht_lft)
          (finitePartGroupoidUnit_source G hs_sep ht_sep hs_lft ht_lft)).toSubfunctor.ι) =
      finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft
```

**`AlgebraicGeometry.Space.finitePartGroupoidUniversalOpen_containsUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2821](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2821). The attribute's comment: “clause (2), Z\_univ contains the base change of the unit e”.

> **Stacks 04RU, clause (2), the unit.** `Z_univ` contains the base change of the unit `e`.

```lean
public theorem finitePartGroupoidUniversalOpen_containsUnit :
    AlgebraicGeometry.Space.ContainsSection C S hS G.source
      (finitePartGroupoidUnit G hs_sep ht_sep hs_lft ht_lft)
      (finitePartGroupoidUnit_source G hs_sep ht_sep hs_lft ht_lft)
      (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft)
```

**`AlgebraicGeometry.Space.finitePartGroupoidUniversalOpen_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2831](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2831). The attribute's comment: “clause (2), Z\_univ is closed in R ×\_\{s, U, g} U' as well as open”.

> **Stacks 04RU, clause (2), closedness.** `Z_univ` is closed in `R ×_{s, U, g} U'` as well as
> open.

```lean
public theorem finitePartGroupoidUniversalOpen_closed :
    AlgebraicGeometry.Space.IsClosedSubspace C S hS
      (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft).subspace
```

**`AlgebraicGeometry.Space.finitePartGroupoid_arrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2839](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2839). The attribute's comment: “clause (2), the arrow space of the finite part is Z\_univ”.

> **Stacks 04RU, clause (2), the arrow space.** The space of arrows of the groupoid on the
> finite part *is* the universal finite open subspace `Z_univ`.

```lean
public theorem finitePartGroupoid_arrows :
    (finitePartGroupoid G hs_sep ht_sep hs_lft ht_lft).arrows.obj =
      (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft).subspace.toFunctor
```

**`AlgebraicGeometry.Space.finitePartGroupoidHom_mapArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2859](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2859). The attribute's comment: “the arrow map of the canonical morphism is Z\_univ ⊂ R ×\_\{s, U, g} U' ⟶ R”.

> **Stacks 04RU.** Under the identification of the arrow space with `Z_univ`, the canonical
> morphism of groupoids sends an arrow of the finite part to its underlying arrow of `R`, i.e. it is
> the second projection of `R ×_{s, U, g} U'`.

```lean
public theorem finitePartGroupoidHom_mapArrows :
    (finitePartGroupoidHom G hs_sep ht_sep hs_lft ht_lft).toGroupoidHom.mapArrows =
      eqToHom (finitePartGroupoid_arrows G hs_sep ht_sep hs_lft ht_lft) ≫
        (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft).subspace.ι ≫
        pullback.snd
          (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft).toBase.hom
          G.source.hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePartGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean#L641). The attribute's comment: “the groupoid structure on the finite part”.

> **Stacks 04RU, the groupoid structure.** For a groupoid in algebraic spaces over `B` whose
> source morphism is separated and locally of finite type, the finite part
> `(U', Z_univ, s', t', c', e', i')` is a groupoid in algebraic spaces over `B`.

```lean
noncomputable def finitePartGroupoid (hsep : Space.IsSeparated C S hS G.source.hom)
    (hft : Space.IsLocallyOfFiniteType C S hS G.source.hom) :
    GroupoidInAlgebraicSpaces C S hS B
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePartGroupoidHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean, line 653](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean#L653). The attribute's comment: “the canonical morphism of groupoids from the finite part to the given groupoid”.

> **Stacks 04RU, the canonical morphism of groupoids.** For a groupoid in algebraic spaces over
> `B` whose source morphism is separated and locally of finite type, the canonical morphism of
> groupoids in algebraic spaces over `B` from the finite part to the given groupoid: on objects it
> is the étale projection `g : U' ⟶ U` of Stacks 04RU, clause (1), and on arrows it is the rule
> `(u, Z, z) ↦ z`.

```lean
noncomputable def finitePartGroupoidHom (hsep : Space.IsSeparated C S hS G.source.hom)
    (hft : Space.IsLocallyOfFiniteType C S hS G.source.hom) :
    Hom (finitePartGroupoid hsep hft) G
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.14, Tag 04RT](https://stacks.math.columbia.edu/tag/04RT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
