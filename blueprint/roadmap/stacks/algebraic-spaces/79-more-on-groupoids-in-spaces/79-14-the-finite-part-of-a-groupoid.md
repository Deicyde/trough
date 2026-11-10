---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePart, AlgebraicGeometry.Space.FinitePartUniversalOpen, AlgebraicGeometry.Space.finitePartUniversalOpen, AlgebraicGeometry.Space.FinitePartGroupoid, AlgebraicGeometry.Space.nonempty_finitePartGroupoid, AlgebraicGeometry.Space.finitePartGroupoid, AlgebraicGeometry.Space.finitePartGroupoidHom, AlgebraicGeometry.Space.finitePartGroupoid_objectProjection_spec
statement: formalized
proof: formalized
---

# 79.14 The finite part of a groupoid

Section 79.14 of the Stacks Project, [Tag 04RT](https://stacks.math.columbia.edu/tag/04RT). 2 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04RT, the section

[Tag 04RT](https://stacks.math.columbia.edu/tag/04RT) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePart`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidFinitePart.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidFinitePart.lean#L299). The attribute's comment: “the object space and the arrow space of the finite part”.

> **Stacks 04RT.** The finite part of a groupoid in algebraic spaces whose source morphism is
> separated and locally of finite type.
>
> Its object space is `U' = (R_s/U, e)_fin`, the finite part of the source morphism containing the
> unit: an algebraic space by Stacks 04QH and Stacks 04RR, part (3), and an open subspace of
> `(R_s/U)_fin`. Its morphism `g : U' ⟶ U` is the projection of `(R_s/U)_fin` restricted to `U'`,
> and is étale because that projection is étale by Stacks 04QH and the inclusion of an open
> subspace is étale. Its arrow space is the open subspace `Z_univ` of `U' ×_{g, U, s} R` belonging
> to the pair which the inclusion names under Stacks 04PE, part (2); it is finite over `U'` by
> construction, closed by Stacks 04PH, and contains the base change of the unit because every
> pair named by a section of `U'` does.

```lean
noncomputable def finitePart (G : GroupoidInAlgebraicSpaces C S hS B)
    (hsep : Space.IsSeparated C S hS G.source.hom)
    (hft : Space.IsLocallyOfFiniteType C S hS G.source.hom) :
    FinitePart G
```

## Tag 04RU, a lemma

[Tag 04RU](https://stacks.math.columbia.edu/tag/04RU) in the Stacks Project.

**`AlgebraicGeometry.Space.FinitePartUniversalOpen`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 1845](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L1845). The attribute's comment: “clauses (1) and (2) stated; not the groupoid structure”.

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

**`AlgebraicGeometry.Space.finitePartUniversalOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 1890](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L1890). The attribute's comment: “clauses (1) and (2); not the groupoid structure or its morphism”.

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

**`AlgebraicGeometry.Space.FinitePartGroupoid`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 1948](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L1948). The attribute's comment: “clause (3), the groupoid structure on the finite part and its morphism to R”.

> **Stacks 04RU, clause (3).** The groupoid in algebraic spaces
> `(U', Z_univ, s', t', c')` carried by the finite part of `(U, R, s, t, c)`, together with its
> canonical morphism of groupoids to `(U, R, s, t, c)` over `B`.

```lean
public structure FinitePartGroupoid
    {C : AlgebraicGeometry.BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicGeometry.AlgebraicSpaces C S hS}
    (G : AlgebraicGeometry.GroupoidInAlgebraicSpaces C S hS B)
```

**`AlgebraicGeometry.Space.nonempty_finitePartGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2007](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2007). The attribute's comment: “clause (3), the groupoid structure on the finite part and its morphism to R”.

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

**`AlgebraicGeometry.Space.finitePartGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2728](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2728). The attribute's comment: “the groupoid (U', Z_univ, s', t', c', e', i') on the finite part”.

> **Stacks 04RU.** The groupoid in algebraic spaces `(U', Z_univ, s', t', c', e', i')` over `B`
> carried by the finite part of `(U, R, s, t, c, e, i)`.

```lean
public noncomputable def finitePartGroupoid :
    AlgebraicGeometry.GroupoidInAlgebraicSpaces C S hS B
```

**`AlgebraicGeometry.Space.finitePartGroupoidHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2735). The attribute's comment: “the canonical morphism of groupoids over B to (U, R, s, t, c, e, i)”.

> **Stacks 04RU.** The canonical morphism of groupoids in algebraic spaces over `B`
> `(U', Z_univ, s', t', c', e', i') ⟶ (U, R, s, t, c, e, i)` whose existence the lemma asserts.

```lean
public noncomputable def finitePartGroupoidHom :
    AlgebraicGeometry.GroupoidInAlgebraicSpaces.Hom
      (finitePartGroupoid G hs_sep ht_sep hs_lft ht_lft) G
```

**`AlgebraicGeometry.Space.finitePartGroupoid_objectProjection_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2778](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2778). The attribute's comment: “clause (1), g : U' ⟶ U is identified with (R_s/U, e)_fin ⟶ U”.

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

**`AlgebraicGeometry.Space.finitePartGroupoidUniversalOpen_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2809](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2809). The attribute's comment: “clause (2), Z_univ is the universal finite open subspace of R ×_{s, U, g} U'”.

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

**`AlgebraicGeometry.Space.finitePartGroupoidUniversalOpen_containsUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2821](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2821). The attribute's comment: “clause (2), Z_univ contains the base change of the unit e”.

> **Stacks 04RU, clause (2), the unit.** `Z_univ` contains the base change of the unit `e`.

```lean
public theorem finitePartGroupoidUniversalOpen_containsUnit :
    AlgebraicGeometry.Space.ContainsSection C S hS G.source
      (finitePartGroupoidUnit G hs_sep ht_sep hs_lft ht_lft)
      (finitePartGroupoidUnit_source G hs_sep ht_sep hs_lft ht_lft)
      (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft)
```

**`AlgebraicGeometry.Space.finitePartGroupoidUniversalOpen_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2831](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2831). The attribute's comment: “clause (2), Z_univ is closed in R ×_{s, U, g} U' as well as open”.

> **Stacks 04RU, clause (2), closedness.** `Z_univ` is closed in `R ×_{s, U, g} U'` as well as
> open.

```lean
public theorem finitePartGroupoidUniversalOpen_closed :
    AlgebraicGeometry.Space.IsClosedSubspace C S hS
      (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft).subspace
```

**`AlgebraicGeometry.Space.finitePartGroupoid_arrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2839](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2839). The attribute's comment: “clause (2), the arrow space of the finite part is Z_univ”.

> **Stacks 04RU, clause (2), the arrow space.** The space of arrows of the groupoid on the
> finite part *is* the universal finite open subspace `Z_univ`.

```lean
public theorem finitePartGroupoid_arrows :
    (finitePartGroupoid G hs_sep ht_sep hs_lft ht_lft).arrows.obj =
      (finitePartGroupoidUniversalOpen G hs_sep ht_sep hs_lft ht_lft).subspace.toFunctor
```

**`AlgebraicGeometry.Space.finitePartGroupoidHom_mapArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean, line 2859](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/Groupoid.lean#L2859). The attribute's comment: “the arrow map of the canonical morphism is Z_univ ⊂ R ×_{s, U, g} U' ⟶ R”.

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

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePartGroupoid`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean#L639). The attribute's comment: “the groupoid structure on the finite part”.

> **Stacks 04RU, the groupoid structure.** For a groupoid in algebraic spaces over `B` whose
> source morphism is separated and locally of finite type, the finite part
> `(U', Z_univ, s', t', c', e', i')` is a groupoid in algebraic spaces over `B`.

```lean
noncomputable def finitePartGroupoid (hsep : Space.IsSeparated C S hS G.source.hom)
    (hft : Space.IsLocallyOfFiniteType C S hS G.source.hom) :
    GroupoidInAlgebraicSpaces C S hS B
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.finitePartGroupoidHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean, line 651](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/FinitePart/GroupoidStructure.lean#L651). The attribute's comment: “the canonical morphism of groupoids from the finite part to the given groupoid”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
