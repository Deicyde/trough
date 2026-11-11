---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.isQuasiSplitAt_of_isLocallyArtinian_arrows, AlgebraicGeometry.GroupoidInAlgebraicSpaces.OpenFiniteSubgroupoid, AlgebraicGeometry.GroupoidInAlgebraicSpaces.identityPoint_hasCommonExtension, AlgebraicGeometry.GroupoidInAlgebraicSpaces.StrongSplitting, AlgebraicGeometry.GroupoidInAlgebraicSpaces.Splitting, AlgebraicGeometry.GroupoidInAlgebraicSpaces.QuasiSplitting, AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsStronglySplitAt, AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsSplitAt
statement: formalized
proof: formalized
---

# 79.15 Étale localization of groupoid schemes

Section 79.15 of the Stacks Project, [Tag 04RJ](https://stacks.math.columbia.edu/tag/04RJ). 13 tags here are carried by 31 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04RK, a definition

[Tag 04RK](https://stacks.math.columbia.edu/tag/04RK) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.isQuasiSplitAt_of_isLocallyArtinian_arrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IdentityArrowSubgroupoid.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/IdentityArrowSubgroupoid.lean#L427). The attribute's comment: “part (3): a groupoid scheme with a one-point object scheme and a zero-dimensional arrow scheme is quasi-split at every point of its object scheme, the quasi-splitting being the open and closed piece of the arrow scheme through the identity”.

> **A groupoid scheme with a one-point object scheme and a zero-dimensional arrow scheme is
> quasi-split at every point of its object scheme**, in the sense of part (3) of
> **Stacks 04RK**.

```lean
theorem isQuasiSplitAt_of_isLocallyArtinian_arrows (u : G.objects.left) : IsQuasiSplitAt G u
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.OpenFiniteSubgroupoid`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L88). The attribute's comment: “conditions (a) and (b) on the open subspace”.

> An open subspace of the arrow space of a groupoid in algebraic spaces which is itself a
> groupoid on the ambient object space, with the restricted source and target morphisms finite
> and with composition the restriction of the ambient composition.
>
> This is conditions (a) and (b) shared by the three splittings of **Stacks 04RK**.

```lean
structure OpenFiniteSubgroupoid (G : GroupoidInAlgebraicSpaces C S hS B)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.identityPoint_hasCommonExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L126). The attribute's comment: “part (3): the identity on points is well defined”.

> Taking the identity arrow at a field-valued point of the object space respects common
> extension, so it descends to the points of the two spaces.

```lean
theorem identityPoint_hasCommonExtension (G : GroupoidInAlgebraicSpaces C S hS B)
    {p q : Space.FieldValuedPoint C S hS G.objects.obj}
    (h : Space.FieldValuedPoint.HasCommonExtension C S hS G.objects.obj p q) :
    Space.FieldValuedPoint.HasCommonExtension C S hS G.arrows.obj
      (identityPoint G p) (identityPoint G q)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.StrongSplitting`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L163). The attribute's comment: “part (1): a strong splitting”.

> A strong splitting of a groupoid in algebraic spaces at a point `u` of its object space: an
> open finite subgroupoid containing every point of the arrow space whose source and target are
> both `u`.

```lean
structure StrongSplitting (G : GroupoidInAlgebraicSpaces C S hS B)
    (u : Space.points C S hS G.objects.obj) extends OpenFiniteSubgroupoid G
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.Splitting`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L175). The attribute's comment: “part (2): a splitting”.

> A splitting of a groupoid in algebraic spaces at a point `u` of its object space: an open
> finite subgroupoid containing every point of the stabilizer which lies over `u`.

```lean
structure Splitting (G : GroupoidInAlgebraicSpaces C S hS B)
    (u : Space.points C S hS G.objects.obj) extends OpenFiniteSubgroupoid G
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.QuasiSplitting`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L187). The attribute's comment: “part (3): a quasi-splitting”.

> A quasi-splitting of a groupoid in algebraic spaces at a point `u` of its object space: an
> open finite subgroupoid containing the identity arrow at `u`.

```lean
structure QuasiSplitting (G : GroupoidInAlgebraicSpaces C S hS B)
    (u : Space.points C S hS G.objects.obj) extends OpenFiniteSubgroupoid G
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsStronglySplitAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L196). The attribute's comment: “part (1): strongly split over a point”.

> A groupoid in algebraic spaces is *strongly split* at a point of its object space when a
> strong splitting there exists.

```lean
abbrev IsStronglySplitAt (G : GroupoidInAlgebraicSpaces C S hS B)
    (u : Space.points C S hS G.objects.obj) : Prop
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsSplitAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L202). The attribute's comment: “part (2): split over a point”.

> A groupoid in algebraic spaces is *split* at a point of its object space when a splitting
> there exists.

```lean
abbrev IsSplitAt (G : GroupoidInAlgebraicSpaces C S hS B)
    (u : Space.points C S hS G.objects.obj) : Prop
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsQuasiSplitAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Splittings.lean#L208). The attribute's comment: “part (3): quasi-split over a point”.

> A groupoid in algebraic spaces is *quasi-split* at a point of its object space when a
> quasi-splitting there exists.

```lean
abbrev IsQuasiSplitAt (G : GroupoidInAlgebraicSpaces C S hS B)
    (u : Space.points C S hS G.objects.obj) : Prop
```

**`Stacks.Groupoids.GroupoidScheme.OpenFiniteSubgroupoid`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean#L124). The attribute's comment: “conditions (a) and (b) on the open subscheme, for a groupoid scheme”.

> An open subscheme of the arrow scheme of a groupoid scheme which is itself a groupoid scheme
> on the ambient object scheme, with the restricted source and target morphisms finite and with
> composition the restriction of the ambient composition.
>
> This is conditions (a) and (b) shared by the three splittings of **Stacks 04RK**, read for a
> groupoid scheme.

```lean
structure OpenFiniteSubgroupoid (G : GroupoidScheme S)
```

**`Stacks.Groupoids.GroupoidScheme.QuasiSplitting`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean#L147). The attribute's comment: “part (3), for a groupoid scheme: a quasi-splitting of R over u”.

> A quasi-splitting of a groupoid scheme over a point `u` of its object scheme: an open finite
> subgroupoid whose scheme of arrows contains the identity arrow `e(u)`.

```lean
structure QuasiSplitting (G : GroupoidScheme S) (u : G.objects.left) extends
    OpenFiniteSubgroupoid G
```

**`Stacks.Groupoids.GroupoidScheme.IsQuasiSplitAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean#L157). The attribute's comment: “part (3), for a groupoid scheme: R is quasi-split over u”.

> A groupoid scheme is *quasi-split* over a point of its object scheme when a quasi-splitting
> there exists.

```lean
abbrev IsQuasiSplitAt (G : GroupoidScheme S) (u : G.objects.left) : Prop
```

**`Stacks.Groupoids.GroupoidScheme.OpenFiniteSubgroupoid.toQuasiSplitting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean#L166). The attribute's comment: “the footnote to part (3): condition (c) follows from condition (a)”.

> The footnote to part (3) of **Stacks 04RK**: condition (c) is implied by condition (a).
> An open finite subgroupoid of a groupoid scheme contains the identity arrow at every point of
> the object scheme, because the inclusion is a morphism of groupoid schemes which is the identity
> on objects, and so carries the identity section of the subgroupoid to that of the ambient
> groupoid.

```lean
def OpenFiniteSubgroupoid.toQuasiSplitting {G : GroupoidScheme S} (P : OpenFiniteSubgroupoid G)
    (u : G.objects.left) : QuasiSplitting G u
```

**`Stacks.Groupoids.GroupoidScheme.StrongSplitting`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean#L187). The attribute's comment: “part (1), for a groupoid scheme: a strong splitting of R over u”.

> A strong splitting of a groupoid scheme over a point `u` of its object scheme: an open
> finite subgroupoid whose scheme of arrows contains every arrow of `R` whose source and target
> are both `u`.
>
> This is part (1) of **Stacks 04RK**, read for a groupoid scheme.  It is strictly stronger than
> `Stacks.Groupoids.GroupoidScheme.QuasiSplitting`, whose condition (c) asks only for the identity
> arrow `e(u)`; see `Stacks.Groupoids.GroupoidScheme.StrongSplitting.toQuasiSplitting`.

```lean
structure StrongSplitting (G : GroupoidScheme S) (u : G.objects.left) extends
    OpenFiniteSubgroupoid G
```

**`Stacks.Groupoids.GroupoidScheme.IsStronglySplitAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SchemeSplittings.lean#L197). The attribute's comment: “part (1), for a groupoid scheme: R is strongly split over u”.

> A groupoid scheme is *strongly split* over a point of its object scheme when a strong
> splitting there exists.

```lean
abbrev IsStronglySplitAt (G : GroupoidScheme S) (u : G.objects.left) : Prop
```

## Tag 04RL, a situation

[Tag 04RL](https://stacks.math.columbia.edu/tag/04RL) in the Stacks Project.

**`AlgebraicGeometry.Space.StrongSplittingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingSituations.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingSituations.lean#L91).

> **Stacks Project, Tag 04RL.** The standing strong splitting situation for a groupoid
> scheme: a chosen object with finite stabilizer, at whose stabilizer points the source is
> quasi-finite.

```lean
structure StrongSplittingSituation
```

## Tag 0DTB, a situation

[Tag 0DTB](https://stacks.math.columbia.edu/tag/0DTB) in the Stacks Project.

**`AlgebraicGeometry.Space.SplittingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingSituations.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingSituations.lean#L122).

> **Stacks Project, Tag 0DTB.** The standing splitting situation for a groupoid scheme at
> a point of its object scheme.

```lean
structure SplittingSituation
```

## Tag 04RV, a situation

[Tag 04RV](https://stacks.math.columbia.edu/tag/04RV) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasiSplittingSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingSituations.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingSituations.lean#L63).

> **Stacks Project, Tag 04RV.** The standing quasi-splitting situation: a point `u` of
> the object scheme of a groupoid scheme whose source and target are separated and locally of
> finite type, with the source quasi-finite at the identity arrow `e(u)`.

```lean
structure QuasiSplittingSituation
```

## Tag 03FM, a lemma

[Tag 03FM](https://stacks.math.columbia.edu/tag/03FM) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_stronglySplit_of_strongSplittingSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EtaleLocalizationArrowContainment/StrongSplitting.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EtaleLocalizationArrowContainment/StrongSplitting.lean#L313). The attribute's comment: “all four assertions, in Situation 04RL: the algebraic space U', the étale g : U' ⟶ U and the point u' : Spec κ(u) ⟶ U' over u are PRODUCED, and R|\_\{U'} is strongly split over u'. Beyond Situation 04RL the only hypotheses are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec κ(u), which is this library's standing ambient requirement”.

> **Stacks Project, Tag 03FM.**  In the strong splitting situation of Stacks 04RL there are
> an algebraic space `U'`, an étale morphism `g : U' ⟶ U` of algebraic spaces and a point
> `u' : Spec κ(u) ⟶ U'` lying over `u : Spec κ(u) ⟶ U` such that the restriction `R' = R|_{U'}`
> of `R` to `U'` is strongly split over `u'`.
>
> `U'` is the object space of the finite part `(R_s/U, e)_fin` of Stacks 04RU, `g` its étale
> projection, `u'` the pair `(u, Z_u)` where `Z_u` is the open and closed piece of the fibre
> `F_u = R ×_{s, U} Spec κ(u)` supported on the arrows from `u` to itself, and the strong
> splitting is the universal open `Z_univ` read inside `R|_{U'}`.  Being strongly split is a
> condition on a point of `|U'|`, so it is asserted at the point of `|U'|` which the morphism
> `u' : Spec κ(u) ⟶ U'` determines.

```lean
theorem exists_stronglySplit_of_strongSplittingSituation
    (D : StrongSplittingSituation.{u})
    (C : BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u))) :
    ∃ (U' : AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      IsEtale C D.S hS g.hom ∧
      ∃ v : U'.obj.obj (Opposite.op
          (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK)),
        (yonedaSchemePointEquiv C hS hU (Opposite.op
            (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK))
            (g.hom.app _ v)).left =
          D.groupoid.objects.left.fromSpecResidueField D.u ∧
        GroupoidInAlgebraicSpaces.IsStronglySplitAt
          (GroupoidInAlgebraicSpaces.restrict (D.groupoid.realization C hS hU hR hP)
            g).groupoid
          ((residueSectionValuedPoint D.groupoid C hS D.u hK U' v).class C D.S hS U'.obj)
```

## Tag 0DTC, a lemma

[Tag 0DTC](https://stacks.math.columbia.edu/tag/0DTC) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_split_of_splittingSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EtaleLocalizationStabilizerContainment.lean, line 1016](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EtaleLocalizationStabilizerContainment.lean#L1016). The attribute's comment: “ALL FOUR ASSERTIONS, in Situation 0DTB: the algebraic space U', the etale morphism g : U' -> U, the point u' : Spec k(u) -> U' lying over u, and that the restriction R|\_\{U'} is SPLIT over u' -- all four PRODUCED, none assumed. The situation hypothesis is AlgebraicGeometry.Space.SplittingSituation, which carries the 0DTB attribute, and NOT the stronger StrongSplittingSituation of Tag 04RL. Beyond Situation 0DTB the only hypotheses are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec k(u), which is this library's standing ambient requirement. The supporting open of the fibre is the stabilizer-supported one of SplittingSituation.exists\_fiberOpens\_stabilizer, a proper subset in general of the target-condition open that Tag 03FM uses”.

> **Stacks Project, Tag 0DTC.**  In the splitting situation of Stacks 0DTB there are an
> algebraic space `U'`, an étale morphism `g : U' ⟶ U` of algebraic spaces and a point
> `u' : Spec κ(u) ⟶ U'` lying over `u : Spec κ(u) ⟶ U` such that the restriction `R' = R|_{U'}`
> of `R` to `U'` is split over `u'`.
>
> `U'` is the object space of the finite part `(R_s/U, e)_fin` of Stacks 04RU, `g` its étale
> projection, `u'` the pair `(u, Z_u)` where `Z_u` is the open and closed piece of the fibre
> `F_u = R ×_{s, U} Spec κ(u)` supported on the arrows underlying the points of the stabilizer
> group scheme over `u`, and the splitting is the universal open `Z_univ` read inside `R|_{U'}`.
> Being split is a condition on a point of `|U'|`, so it is asserted at the point of `|U'|` which
> the morphism `u' : Spec κ(u) ⟶ U'` determines.
>
> The standing hypothesis is `AlgebraicGeometry.Space.SplittingSituation`, Situation 0DTB, and not
> the strictly stronger `AlgebraicGeometry.Space.StrongSplittingSituation` of Stacks 04RL: the
> open `Z_u` is supported on the stabilizer, which is in general a proper subset of the arrows
> with both endpoints at `u`.  So this is not a formal consequence of Stacks 03FM,
> `AlgebraicGeometry.Space.exists_stronglySplit_of_strongSplittingSituation`.

```lean
theorem exists_split_of_splittingSituation
    (D : AlgebraicGeometry.Space.SplittingSituation.{u})
    (C : BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u))) :
    ∃ (U' : AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      IsEtale C D.S hS g.hom ∧
      ∃ v : U'.obj.obj (Opposite.op
          (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK)),
        (yonedaSchemePointEquiv C hS hU (Opposite.op
            (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK))
            (g.hom.app _ v)).left =
          D.groupoid.objects.left.fromSpecResidueField D.u ∧
        GroupoidInAlgebraicSpaces.IsSplitAt
          (GroupoidInAlgebraicSpaces.restrict (D.groupoid.realization C hS hU hR hP)
            g).groupoid
          ((residueSectionValuedPoint D.groupoid C hS D.u hK U' v).class C D.S hS U'.obj)
```

## Tag 04RW, a lemma

[Tag 04RW](https://stacks.math.columbia.edu/tag/04RW) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_etale_quasiSplitting_of_quasiSplittingSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EtaleLocalizationQuasiSplittingPoint.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EtaleLocalizationQuasiSplittingPoint.lean#L337).

> **Stacks Project, Tag 04RW.**
>
> In the quasi-splitting situation of Stacks 04RV there are an algebraic space `U'`, an étale
> morphism `g : U' ⟶ U` of algebraic spaces and a point `u' : Spec κ(u) ⟶ U'` lying over `u` such
> that the restriction `R|_{U'}` is quasi-split over `u'`.
>
> `U'` is the finite part `(R_s/U, e)_fin` of Stacks 04RU and `g` its étale projection; `u'` is
> the pair `(u, Z_u)` with `Z_u = {e(u)}`, which is an open and closed piece of the fibre
> `F_u = R ×_{s, U} Spec κ(u)` finite over `κ(u)` because the source is quasi-finite at `e(u)`;
> and the quasi-splitting is the universal open `Z_univ` of Stacks 04RU read inside `R|_{U'}`,
> which is a quasi-splitting at every point of `U'`.

```lean
theorem exists_etale_quasiSplitting_of_quasiSplittingSituation
    (D : AlgebraicGeometry.Space.QuasiSplittingSituation.{u})
    (C : BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u))) :
    ∃ (U' : AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      AlgebraicGeometry.Space.IsEtale C D.S hS g.hom ∧
      ∃ v : U'.obj.obj (Opposite.op
          (AlgebraicGeometry.Space.residueFieldSiteObject C hS
            (X := D.groupoid.objects) D.u hK)),
        (AlgebraicGeometry.Space.yonedaSchemePointEquiv C hS hU
            (Opposite.op (AlgebraicGeometry.Space.residueFieldSiteObject C hS
              (X := D.groupoid.objects) D.u hK))
            (g.hom.app _ v)).left =
              D.groupoid.objects.left.fromSpecResidueField D.u ∧
        IsQuasiSplitAt (restrict (D.groupoid.realization C hS hU hR hP) g).groupoid
          (AlgebraicGeometry.Space.pointsMap C D.S hS U'.obj
            (eqToHom (restrict (D.groupoid.realization C hS hU hR hP) g).objects_eq.symm).hom
            (AlgebraicGeometry.Space.FieldValuedPoint.class C D.S hS U'.obj
              { carrier := D.groupoid.objects.left.residueField D.u
                contained := hK
                toBase := D.groupoid.objects.left.fromSpecResidueField D.u ≫
                  D.groupoid.objects.hom
                value := v }))
```

**`Stacks.Groupoids.GroupoidScheme.exists_quasiSplit_of_quasiSplittingSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasiSplittingEtaleLocalization.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasiSplittingEtaleLocalization.lean#L484). The attribute's comment: “ALL FOUR ASSERTIONS, in Situation 04RV: the algebraic space U', the etale morphism g : U' -> U, the point u' : Spec k(u) -> U' lying over u, and that the restriction R|\_\{U'} is QUASI-SPLIT over u' -- all four PRODUCED, none assumed. The situation hypothesis is AlgebraicGeometry.Space.QuasiSplittingSituation, which carries the 04RV attribute. The open Z\_u of the fibre is the one supported on the identity arrow e(u), which is open and closed and finite over k(u) because s is quasi-finite at e(u), the one geometric hypothesis of Tag 04RV beyond separatedness and local finiteness of type. Beyond Situation 04RV the only hypotheses are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec k(u), which is this library's standing ambient requirement”.

> **Stacks Project, Tag 04RW.**  In the quasi-splitting situation of Stacks 04RV there are an
> algebraic space `U'`, an étale morphism `g : U' ⟶ U` of algebraic spaces and a point
> `u' : Spec κ(u) ⟶ U'` lying over `u : Spec κ(u) ⟶ U` such that the restriction `R' = R|_{U'}`
> of `R` to `U'` is quasi-split over `u'`.
>
> `U'` is the object space of the finite part `(R_s/U, e)_fin`, `g` its étale projection, `u'` the
> pair `(u, Z_u)` with `Z_u` the open and closed piece of the fibre `F_u = R ×_{s, U} Spec κ(u)`
> supported on the identity arrow `e(u)`, and the quasi-splitting is the universal open `Z_univ`
> read inside `R|_{U'}`.

```lean
theorem exists_quasiSplit_of_quasiSplittingSituation
    (D : AlgebraicGeometry.Space.QuasiSplittingSituation.{u})
    (C : BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u))) :
    ∃ (U' : AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      IsEtale C D.S hS g.hom ∧
      ∃ v : U'.obj.obj (Opposite.op
          (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK)),
        (yonedaSchemePointEquiv C hS hU (Opposite.op
            (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK))
            (g.hom.app _ v)).left =
          D.groupoid.objects.left.fromSpecResidueField D.u ∧
        GroupoidInAlgebraicSpaces.IsQuasiSplitAt
          (GroupoidInAlgebraicSpaces.restrict (D.groupoid.realization C hS hU hR hP)
            g).groupoid
          ((residueSectionValuedPoint D.groupoid C hS D.u hK U' v).class C D.S hS U'.obj)
```

## Tag 04RX, a lemma

[Tag 04RX](https://stacks.math.columbia.edu/tag/04RX) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.nonempty_etaleStrongSplitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/StrongSplittingEtaleScheme.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/StrongSplittingEtaleScheme.lean#L146). The attribute's comment: “in Situation 04RL with the source flat and locally of finite presentation: U' is a SCHEME (asserted as representability of the neighbourhood), U' ⟶ U is SEPARATED as well as étale, and R|\_\{U'} is strongly split over a Spec κ(u)-valued point of U' lying over u. The neighbourhood, its point and the splitting are Stacks 03FM, which this library proves as `AlgebraicGeometry.Space.exists_stronglySplit_of_strongSplittingSituation`; the scheme-ness and the separatedness are Stacks 04RI and Stacks 04RR applied to the finite part (R\_s/U, e)\_fin, through its identification with the neighbourhood recorded by `AlgebraicGeometry.Space.FinitePartUniversalOpen.objectsEquiv` and `objectProjection_spec`. Strong splitting is Stacks 04RK part (1) for the restriction of the REALIZATION of the groupoid scheme, as in this library's Stacks 03FM and Stacks 04RY; the scheme-level `Stacks.Groupoids.GroupoidScheme.StrongSplitting` is not used, the composition of the restricted realization not being compared with the composition of `AlgebraicGeometry.GroupoidScheme.restrict`. Only flatness and local finite presentation of the SOURCE are assumed, where the tag asks them of the target too, so the hypotheses are weaker than the tag's. Beyond Situation 04RL the remaining hypotheses are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec κ(u), this library's standing ambient requirement”.

> **Stacks Project, Tag 04RX.**
>
> In the strong splitting situation of Stacks 04RL, with the source in addition flat and locally
> of finite presentation, there are a scheme `U'`, a separated étale morphism `g : U' ⟶ U`, and a
> point `u'` of `U'` over `u` with `κ(u) = κ(u')`, such that the restriction `R' = R|_{U'}` is
> strongly split over `u'`.
>
> The neighbourhood is `U' = (R_s/U, e)_{fin}`, the finite part of Stacks 04RU containing the
> unit, with its étale projection; it is a scheme by Stacks 04RI part (2) and Stacks 04RR part
> (4), and the projection is separated by Stacks 04RI part (1) and Stacks 04RR part (1).  The
> point and the strong splitting are those of Stacks 03FM, the point being recorded as a section
> over `Spec κ(u)` whose image under `g` is the canonical morphism `Spec κ(u) ⟶ U`.

```lean
theorem nonempty_etaleStrongSplitting
    (D : AlgebraicGeometry.Space.StrongSplittingSituation.{u})
    (C : AlgebraicGeometry.BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u)))
    (hflat : AlgebraicGeometry.Flat D.groupoid.source.left)
    (hfp : AlgebraicGeometry.LocallyOfFinitePresentation D.groupoid.source.left) :
    ∃ (U' : AlgebraicGeometry.AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      U'.obj.IsRepresentable ∧
      AlgebraicGeometry.Space.IsEtale C D.S hS g.hom ∧
      AlgebraicGeometry.Space.IsSeparated C D.S hS g.hom ∧
      ∃ v : U'.obj.obj (Opposite.op
          (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK)),
        (yonedaSchemePointEquiv C hS hU (Opposite.op
            (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK))
            (g.hom.app _ v)).left =
          D.groupoid.objects.left.fromSpecResidueField D.u ∧
        IsStronglySplitAt
          (restrict (D.groupoid.realization C hS hU hR hP) g).groupoid
          ((residueSectionValuedPoint D.groupoid C hS D.u hK U' v).class C D.S hS U'.obj)
```

## Tag 0DTD, a lemma

[Tag 0DTD](https://stacks.math.columbia.edu/tag/0DTD) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_etale_separated_scheme_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingEtaleScheme.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingEtaleScheme.lean#L120). The attribute's comment: “in Situation 0DTB with the source flat and locally of finite presentation: U' is a SCHEME (asserted as representability of the neighbourhood), U' ⟶ U is SEPARATED as well as étale, and R|\_\{U'} is SPLIT over a Spec κ(u)-valued point of U' lying over u. The neighbourhood, its point and the splitting are Stacks 0DTC, which this library proves as `Stacks.Groupoids.GroupoidScheme.exists_split_of_splittingSituation`; the scheme-ness and the separatedness are Stacks 04RI and Stacks 04RR applied to the finite part (R\_s/U, e)\_fin, through its identification with the neighbourhood recorded by `AlgebraicGeometry.Space.FinitePartUniversalOpen.objectsEquiv` and `objectProjection_spec`. Splitting is Stacks 04RK part (2) for the restriction of the REALIZATION of the groupoid scheme, as in this library's Stacks 0DTC and Stacks 04RX; the scheme-level `Stacks.Groupoids.GroupoidScheme.Splitting` is not used, the composition of the restricted realization not being compared with the composition of `AlgebraicGeometry.GroupoidScheme.restrict`. The residue-field clause κ(u) = κ(u') is the section over Spec κ(u): a section of a representable U' is a point u' of U' over u together with a retraction of the residue field map at u', and a retraction forces that map to be an isomorphism by `AlgebraicGeometry.Scheme.Hom.isIso_residueFieldMap_of_retraction`. Only flatness and local finite presentation of the SOURCE are assumed, where the tag asks them of the target too, so the hypotheses are weaker than the tag's. Beyond Situation 0DTB the remaining hypotheses are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec κ(u), this library's standing ambient requirement”.

> **Stacks Project, Tag 0DTD.**
>
> In the splitting situation of Stacks 0DTB, with the source in addition flat and locally of finite
> presentation, there are a scheme `U'`, a separated étale morphism `g : U' ⟶ U`, and a point `u'`
> of `U'` over `u` with `κ(u) = κ(u')`, such that the restriction `R' = R|_{U'}` is split over
> `u'`.
>
> The neighbourhood is `U' = (R_s/U, e)_{fin}`, the finite part of Stacks 04RU containing the
> unit, with its étale projection; it is a scheme by Stacks 04RI part (2) and Stacks 04RR part
> (4), and the projection is separated by Stacks 04RI part (1) and Stacks 04RR part (1).  The
> point and the splitting are those of Stacks 0DTC, the point being recorded as a section over
> `Spec κ(u)` whose image under `g` is the canonical morphism `Spec κ(u) ⟶ U`.

```lean
theorem exists_etale_separated_scheme_split
    (D : AlgebraicGeometry.Space.SplittingSituation.{u})
    (C : AlgebraicGeometry.BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u)))
    (hflat : AlgebraicGeometry.Flat D.groupoid.source.left)
    (hfp : AlgebraicGeometry.LocallyOfFinitePresentation D.groupoid.source.left) :
    ∃ (U' : AlgebraicGeometry.AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      U'.obj.IsRepresentable ∧
      AlgebraicGeometry.Space.IsEtale C D.S hS g.hom ∧
      AlgebraicGeometry.Space.IsSeparated C D.S hS g.hom ∧
      ∃ v : U'.obj.obj (Opposite.op
          (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK)),
        (yonedaSchemePointEquiv C hS hU (Opposite.op
            (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK))
            (g.hom.app _ v)).left =
          D.groupoid.objects.left.fromSpecResidueField D.u ∧
        IsSplitAt
          (restrict (D.groupoid.realization C hS hU hR hP) g).groupoid
          ((residueSectionValuedPoint D.groupoid C hS D.u hK U' v).class C D.S hS U'.obj)
```

## Tag 04RY, a lemma

[Tag 04RY](https://stacks.math.columbia.edu/tag/04RY) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.exists_etale_separated_scheme_quasiSplitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FinitePartSchemeLocalization.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FinitePartSchemeLocalization.lean#L79). The attribute's comment: “U' is a scheme, U' ⟶ U is separated and étale, and R|\_\{U'} is quasi-split at every point of U'”.

> **Stacks Project, Tag 04RY**, for a groupoid in algebraic spaces whose object space is a
> scheme.
>
> Let `G = (U, R, s, t, c)` be a groupoid in algebraic spaces over `B` whose source and target are
> separated, whose source is flat and locally of finite presentation, whose target is locally of
> finite type and whose object space `U` is a scheme.  Then there is an algebraic space `U'` which
> is a *scheme*, a *separated* étale morphism `g : U' ⟶ U`, and `R|_{U'}` is quasi-split at every
> point of `U'`.

```lean
theorem exists_etale_separated_scheme_quasiSplitting
    (G : GroupoidInAlgebraicSpaces C S hS B)
    (hsep : Space.IsSeparated C S hS G.source.hom)
    (htsep : Space.IsSeparated C S hS G.target.hom)
    (hflat : Space.IsFlat C S hS G.source.hom)
    (hfp : Space.IsLocallyOfFinitePresentation C S hS G.source.hom)
    (htlft : Space.IsLocallyOfFiniteType C S hS G.target.hom)
    (hU : G.objects.obj.IsRepresentable) :
    ∃ (U' : AlgebraicSpaces C S hS) (g : U' ⟶ G.objects),
      U'.obj.IsRepresentable ∧
      Space.IsEtale C S hS g.hom ∧
      Space.IsSeparated C S hS g.hom ∧
      ∀ u' : Space.points C S hS (restrict G g).groupoid.objects.obj,
        IsQuasiSplitAt (restrict G g).groupoid u'
```

**`Stacks.Groupoids.GroupoidScheme.exists_etale_separated_scheme_quasiSplitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FinitePartSchemeLocalization.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FinitePartSchemeLocalization.lean#L146). The attribute's comment: “in Situation 04RV: U' is a scheme, U' ⟶ U is separated and étale, and R|\_\{U'} is quasi-split at every point of U'”.

> **Stacks Project, Tag 04RY**, in the quasi-splitting situation of Stacks 04RV.
>
> In Situation 04RV, assume in addition that the source of the groupoid scheme is flat and locally
> of finite presentation.  Then there is a *scheme* `U'`, a *separated* étale morphism
> `g : U' ⟶ U`, and `R|_{U'}` is quasi-split at every point of `U'`.
>
> Only the flatness and local finite presentation of the *source* are used; the tag assumes them of
> the target as well, so the hypotheses here are weaker than the tag's.  Separatedness and local
> finiteness of type of the source and of the target come from Situation 04RV itself.

```lean
theorem exists_etale_separated_scheme_quasiSplitting
    (D : AlgebraicGeometry.Space.QuasiSplittingSituation.{u})
    (C : AlgebraicGeometry.BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hflat : AlgebraicGeometry.Flat D.groupoid.source.left)
    (hfp : AlgebraicGeometry.LocallyOfFinitePresentation D.groupoid.source.left) :
    ∃ (U' : AlgebraicGeometry.AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      U'.obj.IsRepresentable ∧
      AlgebraicGeometry.Space.IsEtale C D.S hS g.hom ∧
      AlgebraicGeometry.Space.IsSeparated C D.S hS g.hom ∧
      ∀ u' : AlgebraicGeometry.Space.points C D.S hS
          (restrict (D.groupoid.realization C hS hU hR hP) g).groupoid.objects.obj,
        IsQuasiSplitAt (restrict (D.groupoid.realization C hS hU hR hP) g).groupoid u'
```

**`AlgebraicGeometry.Space.exists_finitePartGroupoid_isRepresentable_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SplittingSchemes.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/SplittingSchemes.lean#L85). The attribute's comment: “the finite part U' = (R\_s/U, e)\_fin is a scheme, U' ⟶ U is separated and étale, and R|\_\{U'} is quasi-split at every point of U'”.

> **Stacks 04RY**, three of the four clauses of its conclusion. For a groupoid in algebraic
> spaces whose source and target are separated, whose source is flat and locally of finite
> presentation, whose target is locally of finite type and whose object space is a scheme, the
> finite part is a scheme, its projection to the object space is separated and étale, and the
> restriction along that projection is quasi-split at every point.

```lean
theorem exists_finitePartGroupoid_isRepresentable_isSeparated
    {C : BigFppfSite.{u}} {S : Scheme.{u}} {hS : C.Contains S}
    {B : AlgebraicSpaces C S hS} (G : GroupoidInAlgebraicSpaces C S hS B)
    (hs_sep : IsSeparated C S hS G.source.hom)
    (ht_sep : IsSeparated C S hS G.target.hom)
    (hs_flat : IsFlat C S hS G.source.hom)
    (hs_fp : IsLocallyOfFinitePresentation C S hS G.source.hom)
    (ht_lft : IsLocallyOfFiniteType C S hS G.target.hom)
    (hU : G.objects.obj.IsRepresentable) :
    ∃ F : FinitePartGroupoid G,
      F.groupoid.objects.obj.IsRepresentable ∧
      IsSeparated C S hS F.objectProjection.hom ∧
      IsEtale C S hS F.objectProjection.hom ∧
      ∀ u' : points C S hS
          (GroupoidInAlgebraicSpaces.restrict G F.objectProjection).groupoid.objects.obj,
        GroupoidInAlgebraicSpaces.IsQuasiSplitAt
          (GroupoidInAlgebraicSpaces.restrict G F.objectProjection).groupoid u'
```

**`Stacks.Groupoids.GroupoidScheme.exists_quasiSplit_separated_scheme_of_quasiSplittingSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasiSplittingEtaleScheme.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasiSplittingEtaleScheme.lean#L139). The attribute's comment: “ALL FOUR ASSERTIONS PRODUCED, in Situation 04RV with the source flat and locally of finite presentation: U' is a SCHEME (delivered as representability of the neighbourhood), U' -> U is SEPARATED as well as etale, there is a point u' of U' over u with k(u) = k(u') -- recorded both as a Spec k(u)-valued section v of U' over the canonical Spec k(u) -> U, and, on any scheme X' representing U' with any morphism of schemes X' -> U inducing g, as a point u' of X' with image u at which the residue field map is an ISOMORPHISM -- and R|\_\{U'} is QUASI-SPLIT over u'. Each of the four is constructed, none of them an input. The neighbourhood, the point and the quasi-splitting are Tag 04RW, proved in StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasiSplittingEtaleLocalization.lean; the scheme-ness and the separatedness are Tags 04RI and 04RR applied to the finite part (R\_s/U, e)\_fin. Flatness and local finite presentation are required of the SOURCE alone, where the tag requires them of the target too, so these hypotheses are WEAKER than the tag's. Beyond Situation 04RV the remaining requirements are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec k(u), this library's standing ambient requirement”.

> **Stacks Project, Tag 04RY.**
>
> In the quasi-splitting situation of Stacks 04RV, with the source in addition flat and locally
> of finite presentation, there are a scheme `U'`, a separated étale morphism `g : U' ⟶ U`, and a
> point `u'` of `U'` over `u` with `κ(u) = κ(u')`, such that `R' = R|_{U'}` is quasi-split over
> `u'`.

```lean
theorem exists_quasiSplit_separated_scheme_of_quasiSplittingSituation
    (D : AlgebraicGeometry.Space.QuasiSplittingSituation.{u})
    (C : AlgebraicGeometry.BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u)))
    (hflat : AlgebraicGeometry.Flat D.groupoid.source.left)
    (hfp : AlgebraicGeometry.LocallyOfFinitePresentation D.groupoid.source.left) :
    ∃ (U' : AlgebraicGeometry.AlgebraicSpaces C D.S hS)
      (g : U' ⟶ (D.groupoid.realization C hS hU hR hP).objects),
      U'.obj.IsRepresentable ∧
      AlgebraicGeometry.Space.IsEtale C D.S hS g.hom ∧
      AlgebraicGeometry.Space.IsSeparated C D.S hS g.hom ∧
      ∃ v : U'.obj.obj (Opposite.op
          (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK)),
        (yonedaSchemePointEquiv C hS hU (Opposite.op
            (schemeSiteObject C hS (X := residueOver D.groupoid D.u) hK))
            (g.hom.app _ v)).left =
          D.groupoid.objects.left.fromSpecResidueField D.u ∧
        IsQuasiSplitAt
          (restrict (D.groupoid.realization C hS hU hR hP) g).groupoid
          ((residueSectionValuedPoint D.groupoid C hS D.u hK U' v).class C D.S hS U'.obj) ∧
        ∀ (X' : AlgebraicGeometry.BigFppfOver C D.S hS) (ε : U'.obj ≅ yoneda.obj X')
          (gS : X' ⟶ schemeSiteObject C hS hU), yoneda.map gS = ε.inv ≫ g.hom →
          ∃ u' : (AlgebraicGeometry.BigFppfOver.toScheme C D.S hS).obj X',
            ((AlgebraicGeometry.BigFppfOver.toScheme C D.S hS).map gS).base u' = D.u ∧
            IsIso (((AlgebraicGeometry.BigFppfOver.toScheme C D.S hS).map
              gS).residueFieldMap u')
```

## Tag 04RZ, a lemma

[Tag 04RZ](https://stacks.math.columbia.edu/tag/04RZ) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_isAffine_isStronglySplitAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/StrongSplittingAffineLocalization.lean, line 982](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/StrongSplittingAffineLocalization.lean#L982). The attribute's comment: “in Situation 04RL with s, t flat and locally of finite presentation and U affine: an affine scheme U'', an étale U'' ⟶ U and a point u'' over u with κ(u) = κ(u''), such that R|\_\{U''} is strongly split over u''. R|\_\{U''} is covered in its two-step reading, as the restriction to U'' of R' = R|\_\{U'} for the étale neighbourhood U' of Stacks 04RX, rather than as the restriction of R along the composite U'' ⟶ U' ⟶ U; the identification of the two is Stacks 04MW, which this library has as the comparison diagram `doubleRestrictionDiagram` and not as an identification of realizations. The conclusion is stronger than the tag in two respects: U'' ⟶ U' is an open immersion, not merely étale, and the strong splitting is produced for EVERY groupoid scheme realizing that restriction. Beyond Situation 04RL the hypotheses are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec κ(u), this library's standing ambient requirement”.

> **Stacks Project, Tag 04RZ.**
>
> In the strong splitting situation of Stacks 04RL, with `s` and `t` in addition flat and locally
> of finite presentation and with `U` affine, there are an affine scheme `U''`, an étale morphism
> `U'' ⟶ U` and a point `u''` of `U''` over `u` with `κ(u) = κ(u'')`, such that the restriction of
> `R` to `U''` is strongly split over `u''`.
>
> The étale neighbourhood `U'` of Stacks 04RX is shrunk to an affine one: `U''` is an invariant
> affine open of the object scheme of the strong splitting of `R' = R|_{U'}`, so `U'' ⟶ U'` is an
> open immersion and the restriction of that splitting to `U''` is a strong splitting of
> `R'|_{U''}` over `u''`.  The restriction is taken in two steps, as the restriction of `R'` to
> `U''`; its identification with the restriction of `R` along the composite `U'' ⟶ U' ⟶ U` is
> Stacks 04MW.

```lean
theorem exists_isAffine_isStronglySplitAt
    (D : AlgebraicGeometry.Space.StrongSplittingSituation.{u})
    (C : AlgebraicGeometry.BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left) (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u)))
    [IsAffine D.groupoid.objects.left]
    [Flat D.groupoid.source.left] [LocallyOfFinitePresentation D.groupoid.source.left]
    [Flat D.groupoid.target.left] [LocallyOfFinitePresentation D.groupoid.target.left] :
    ∃ (U' : Over D.S) (g : U' ⟶ D.groupoid.objects)
      (R' : AlgebraicGeometry.GroupoidScheme.Restriction D.groupoid g)
      (U'' : Over D.S) (j : U'' ⟶ R'.groupoid.objects) (u'' : U''.left),
      IsAffine U''.left ∧ IsOpenImmersion j.left ∧
      Etale (j ≫ R'.hom.mapObjects).left ∧
      (j ≫ R'.hom.mapObjects).left.base u'' = D.u ∧
      IsIso ((j ≫ R'.hom.mapObjects).left.residueFieldMap u'') ∧
      ∀ R'' : AlgebraicGeometry.GroupoidScheme.Restriction R'.groupoid j,
        IsStronglySplitAt R''.groupoid ((eqToHom R''.objects_eq.symm).left.base u'')
```

## Tag 0DTE, a lemma

[Tag 0DTE](https://stacks.math.columbia.edu/tag/0DTE) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_isAffine_isSplitAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingAffineLocalization.lean, line 789](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SplittingAffineLocalization.lean#L789). The attribute's comment: “in Situation 0DTB with s, t flat and locally of finite presentation and U affine: an affine scheme U'', an étale U'' ⟶ U and a point u'' over u with κ(u) = κ(u''), such that R|\_\{U''} is SPLIT over u'' -- all of it PRODUCED: the neighbourhood, the point and the splitting are conclusions of this theorem, never inputs to it. Splitting is Stacks 04RK part (2) read for a groupoid scheme, stated in this file as `Splitting`: an open subscheme P of the arrow scheme which (a) is a groupoid scheme on the same object scheme, with composition the restriction of the ambient one, (b) has s|\_P and t|\_P finite, and (c) contains the arrow underlying every point of the stabilizer group scheme `AlgebraicGeometry.stabilizer` lying over the point; (a) and (b) are `OpenFiniteSubgroupoid`, which carries the 04RK attribute, and (c) is the field `contains_stabilizer`. The situation hypothesis is `AlgebraicGeometry.Space.SplittingSituation`, which carries the 0DTB attribute, and not the stronger `StrongSplittingSituation` of Tag 04RL. R|\_\{U''} is covered in its two-step reading, as the restriction to U'' of R' = R|\_\{U'} for the étale neighbourhood U' of Stacks 0DTD, rather than as the restriction of R along the composite U'' ⟶ U' ⟶ U; the identification of the two is Stacks 04MW, which this library has as the comparison diagram `doubleRestrictionDiagram` and not as an identification of realizations. The conclusion is stronger than the tag in two respects: U'' ⟶ U' is an open immersion, not merely étale, and the splitting is produced for EVERY groupoid scheme realizing that restriction. Beyond Situation 0DTB the hypotheses are that the big fppf site contains the base, object, arrow and composable-pair schemes and Spec κ(u), this library's standing ambient requirement”.

> **Stacks Project, Tag 0DTE.**
>
> In the splitting situation of Stacks 0DTB, with `s` and `t` in addition flat and locally of
> finite presentation and with `U` affine, there are an affine scheme `U''`, an étale morphism
> `U'' ⟶ U` and a point `u''` of `U''` over `u` with `κ(u) = κ(u'')`, such that the restriction of
> `R` to `U''` is split over `u''`.
>
> The étale neighbourhood `U'` of Stacks 0DTD is shrunk to an affine one: `U''` is an invariant
> affine open of the object scheme of the splitting of `R' = R|_{U'}`, so `U'' ⟶ U'` is an open
> immersion and the restriction of that splitting to `U''` is a splitting of `R'|_{U''}` over
> `u''`.  The restriction is taken in two steps, as the restriction of `R'` to `U''`; its
> identification with the restriction of `R` along the composite `U'' ⟶ U' ⟶ U` is
> Stacks 04MW.

```lean
theorem exists_isAffine_isSplitAt
    (D : AlgebraicGeometry.Space.SplittingSituation.{u})
    (C : AlgebraicGeometry.BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left) (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u)))
    [IsAffine D.groupoid.objects.left]
    [Flat D.groupoid.source.left] [LocallyOfFinitePresentation D.groupoid.source.left]
    [Flat D.groupoid.target.left] [LocallyOfFinitePresentation D.groupoid.target.left] :
    ∃ (U' : Over D.S) (g : U' ⟶ D.groupoid.objects)
      (R' : AlgebraicGeometry.GroupoidScheme.Restriction D.groupoid g)
      (U'' : Over D.S) (j : U'' ⟶ R'.groupoid.objects) (u'' : U''.left),
      IsAffine U''.left ∧ IsOpenImmersion j.left ∧
      Etale (j ≫ R'.hom.mapObjects).left ∧
      (j ≫ R'.hom.mapObjects).left.base u'' = D.u ∧
      IsIso ((j ≫ R'.hom.mapObjects).left.residueFieldMap u'') ∧
      ∀ R'' : AlgebraicGeometry.GroupoidScheme.Restriction R'.groupoid j,
        IsSplitAt R''.groupoid ((eqToHom R''.objects_eq.symm).left.base u'')
```

## Tag 04S0, a lemma

[Tag 04S0](https://stacks.math.columbia.edu/tag/04S0) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_isAffine_isQuasiSplitAt_of_quasiSplittingSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasiSplittingAffineLocalization.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/QuasiSplittingAffineLocalization.lean#L92). The attribute's comment: “ALL ASSERTIONS, in Situation 04RV with U affine and with s and t flat and locally of finite presentation: the separated etale neighbourhood U' -> U, a groupoid scheme R' realizing R|\_\{U'}, an AFFINE open U'' of U' with a point u'' over u at which the residue field map is an ISOMORPHISM, and the QUASI-SPLITTING of R|\_\{U''} over u'' -- all PRODUCED. Stacks 04RY is invoked internally as exists\_quasiSplit\_separated\_scheme\_of\_quasiSplittingSituation; its quasi-splitting is AlgebraicGeometry.GroupoidInAlgebraicSpaces.QuasiSplitting of the restriction of the REALIZATION, and it is converted to the groupoid-scheme notion Stacks.Groupoids.GroupoidScheme.QuasiSplitting by nonempty\_openFiniteSubgroupoid\_of\_realization, which de-realizes the open finite subgroupoid. In two respects the conclusion is STRONGER than the tag: the morphism U'' -> U' is an open immersion, not merely etale, and the quasi-splitting is produced for EVERY groupoid scheme realizing the restriction. R|\_\{U''} is read both as the restriction of R along the composite U'' -> U' -> U, as the tag reads it, and as the restriction of R' to U''. Beyond Situation 04RV the only requirements are that the big fppf site contain the base, object, arrow and composable-pair schemes and Spec k(u), this library's standing ambient requirement”.

> **Stacks Project, Tag 04S0.**
>
> In the quasi-splitting situation of Stacks 04RV, with `U` affine and with `s` and `t` flat and
> locally of finite presentation, there are a separated étale neighbourhood `U' ⟶ U`, a groupoid
> scheme `R'` realizing the restriction `R|_{U'}`, an affine open `U'' ⊆ U'` and a point `u''` of
> `U''` over `u` with `κ(u) = κ(u'')`, such that `U'' ⟶ U` is étale and `R|_{U''}` is quasi-split
> over `u''` — both when `R|_{U''}` is read as the restriction of `R'` to `U''` and when it is
> read, as the tag reads it, as the restriction of `R` along the composite `U'' ⟶ U' ⟶ U`.
>
> Stacks 04RY supplies the neighbourhood and a quasi-splitting of the restriction of the
> *realization* of the groupoid scheme; the comparison with the groupoid-scheme notion is
> `Stacks.Groupoids.GroupoidScheme.nonempty_openFiniteSubgroupoid_of_realization`, and the
> shrinking to an affine neighbourhood is
> `Stacks.Groupoids.GroupoidScheme.exists_isAffine_isQuasiSplitAt`.

```lean
theorem exists_isAffine_isQuasiSplitAt_of_quasiSplittingSituation
    (D : AlgebraicGeometry.Space.QuasiSplittingSituation.{u})
    (C : AlgebraicGeometry.BigFppfSite.{u}) (hS : C.Contains D.S)
    (hU : C.Contains D.groupoid.objects.left)
    (hR : C.Contains D.groupoid.arrows.left)
    (hP : C.Contains (pullback D.groupoid.source D.groupoid.target).left)
    (hK : C.Contains (Spec (D.groupoid.objects.left.residueField D.u)))
    [IsAffine D.groupoid.objects.left]
    [Flat D.groupoid.source.left] [LocallyOfFinitePresentation D.groupoid.source.left]
    [Flat D.groupoid.target.left] [LocallyOfFinitePresentation D.groupoid.target.left]
    :
    ∃ (U' : Over D.S) (gp : U' ⟶ D.groupoid.objects)
      (R' : AlgebraicGeometry.GroupoidScheme.Restriction D.groupoid gp)
      (U'' : Over D.S) (j : U'' ⟶ R'.groupoid.objects) (u'' : U''.left),
      AlgebraicGeometry.IsSeparated gp.left ∧ Etale gp.left ∧
      IsAffine U''.left ∧ IsOpenImmersion j.left ∧
      Etale (j ≫ R'.hom.mapObjects).left ∧
      (j ≫ R'.hom.mapObjects).left.base u'' = D.u ∧
      IsIso ((j ≫ R'.hom.mapObjects).left.residueFieldMap u'') ∧
      (∀ R'' : AlgebraicGeometry.GroupoidScheme.Restriction R'.groupoid j,
        IsQuasiSplitAt R''.groupoid ((eqToHom R''.objects_eq.symm).left.base u'')) ∧
      ∀ R''' : AlgebraicGeometry.GroupoidScheme.Restriction D.groupoid
          (j ≫ R'.hom.mapObjects),
        IsQuasiSplitAt R'''.groupoid ((eqToHom R'''.objects_eq.symm).left.base u'')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.15, Tag 04RJ](https://stacks.math.columbia.edu/tag/04RJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
