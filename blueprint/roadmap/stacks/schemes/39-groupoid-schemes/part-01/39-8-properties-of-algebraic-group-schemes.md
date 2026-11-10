---
declaration: section
origin: cited
lean: AlgebraicGeometry.equidimensional_of_groupScheme, AlgebraicGeometry.topologicalKrullDim_eq_topologicalKrullDimAt_of_groupScheme, AlgebraicGeometry.topologicalKrullDim_eq_ringKrullDim_stalk_of_groupScheme, AlgebraicGeometry.smooth_of_groupScheme_of_charZero, AlgebraicGeometry.Space.GroupAlgebraicSpace.isSmooth_of_charZero, AlgebraicGeometry.isReduced_of_grpObj_of_charZero, AlgebraicGeometry.isReduced_of_groupScheme_of_charZero, AlgebraicGeometry.isReduced_of_groupScheme_of_charZero_of_isAffine
statement: formalized
proof: formalized
---

# 39.8 Properties of algebraic group schemes

Section 39.8 of the Stacks Project, [Tag 0BF6](https://stacks.math.columbia.edu/tag/0BF6). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 045X, a lemma

[Tag 045X](https://stacks.math.columbia.edu/tag/045X) in the Stacks Project.

**`AlgebraicGeometry.equidimensional_of_groupScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Dimension.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Dimension.lean#L78). The attribute's comment: “equidimensionality”. References: SGA 3 VIA (2.4.1), “special case”; SGA 3 VIB (1.5).

> **Stacks Project, Tag 045X.** A group scheme locally of finite type over a field is
> equidimensional.

```lean
theorem equidimensional_of_groupScheme (k : Type u) [Field k] (G : Scheme.{u})
    [G.Over (Spec (.of k))] [GrpObj (G.asOver (Spec (.of k)))]
    [LocallyOfFiniteType (G ↘ Spec (.of k))] :
    Equidimensional G
```

**`AlgebraicGeometry.topologicalKrullDim_eq_topologicalKrullDimAt_of_groupScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Dimension.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Dimension.lean#L92). The attribute's comment: “dimension at every point”. References: EGA IV (15.6.10), “dim(G\_y^0) = dim(G\_y)”; SGA 3 VIB (1.2), “partial”; SGA 3 VIB (1.5).

> **Stacks Project, Tag 045X.** The dimension of a group scheme locally of finite type over a
> field is its dimension at every point.

```lean
theorem topologicalKrullDim_eq_topologicalKrullDimAt_of_groupScheme (k : Type u) [Field k]
    (G : Scheme.{u}) [G.Over (Spec (.of k))] [GrpObj (G.asOver (Spec (.of k)))]
    [LocallyOfFiniteType (G ↘ Spec (.of k))] (g : G) :
    topologicalKrullDim G = topologicalKrullDimAt G g
```

**`AlgebraicGeometry.topologicalKrullDim_eq_ringKrullDim_stalk_of_groupScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Dimension.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/Dimension.lean#L105). The attribute's comment: “dimension at a closed point”.

> **Stacks Project, Tag 045X.** At a closed point of a group scheme locally of finite type
> over a field, the dimension of the scheme is the Krull dimension of the local ring.

```lean
theorem topologicalKrullDim_eq_ringKrullDim_stalk_of_groupScheme (k : Type u) [Field k]
    (G : Scheme.{u}) [G.Over (Spec (.of k))] [GrpObj (G.asOver (Spec (.of k)))]
    [LocallyOfFiniteType (G ↘ Spec (.of k))] (g : G) (hg : IsClosed ({g} : Set G)) :
    topologicalKrullDim G = ringKrullDim (G.presheaf.stalk g)
```

## Tag 047N, a lemma

[Tag 047N](https://stacks.math.columbia.edu/tag/047N) in the Stacks Project.

**`AlgebraicGeometry.smooth_of_groupScheme_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/SmoothCharacteristicZero.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/SmoothCharacteristicZero.lean#L118). References: SGA 3 VIA (1.1); SGA 3 VIA (6.9), “special case”; SGA 3 VIB (1.6), “Case S = Spec k”; SGA 3 VIB (1.6.1); SGA 3 VIIA (8.4), “more general”; SGA 3 VIIA (8.5.1), “more general”; SGA 3 XV (6.5), “partial”; SGA 3 XVII (5.5), “partial”.

> **Stacks Project, Tag 047N.**  Let `k` be a field of characteristic `0` and let `G` be a
> locally algebraic group scheme over `k`, i.e. a scheme whose structure morphism
> `f : G ⟶ Spec k` is locally of finite type and which is a group object over `Spec k`.  Then `f`
> is smooth, i.e. `G` is a smooth group scheme.
>
> By [Stacks, Tag 047I] the sheaf of relative differentials of `f` is free, hence locally free,
> and [Stacks, Tag 04QN] turns that into smoothness over a field of characteristic `0`.

```lean
theorem smooth_of_groupScheme_of_charZero (k : Type u) [Field k] [CharZero k] (G : Scheme.{u})
    (f : G ⟶ Spec (CommRingCat.of k)) [GrpObj (Over.mk f)] [LocallyOfFiniteType f] :
    Smooth f
```

**`AlgebraicGeometry.Space.GroupAlgebraicSpace.isSmooth_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/OverField/SmoothCharacteristicZero.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpaces/OverField/SmoothCharacteristicZero.lean#L227). The attribute's comment: “group algebraic spaces over `Spec k` which are schemes locally of finite type over `k`”. References: SGA 3 VIA (1.1), “special case”; SGA 3 VIA (6.9), “special case”; SGA 3 VIB (1.6.1), “special case”; SGA 3 VIIA (8.4), “more general”; SGA 3 XV (6.5), “special case”; SGA 3 XVII (5.5), “more general”.

> **Stacks 047N.** Let `k` be a field of characteristic `0` and let `G` be a group algebraic
> space over `Spec k` which is a scheme locally of finite type over `k`. Then the structure
> morphism `G ⟶ Spec k` is smooth.
>
> The group scheme structure on the representing scheme is obtained from the group structure of
> `G` by `AlgebraicGeometry.Space.grpObjOfIsoYoneda`, and the smoothness of the scheme is
> `AlgebraicGeometry.smooth_of_groupScheme_of_charZero`.

```lean
theorem GroupAlgebraicSpace.isSmooth_of_charZero
    (G : GroupAlgebraicSpace C (Spec (.of k)) hk (terminalSpace C (Spec (.of k)) hk).obj
      (terminalSpace C (Spec (.of k)) hk).property)
    [G.obj.X.left.IsRepresentable]
    (hlft : IsLocallyOfFiniteType C (Spec (.of k)) hk G.obj.X.hom) :
    IsSmooth C (Spec (.of k)) hk G.obj.X.hom
```

## Tag 047O, a remark

[Tag 047O](https://stacks.math.columbia.edu/tag/047O) in the Stacks Project.

**`AlgebraicGeometry.isReduced_of_grpObj_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/ReducedCharacteristicZeroGeneral.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/ReducedCharacteristicZeroGeneral.lean#L46). References: SGA 3 VIA (6.9), “partial”; SGA 3 VIIA (8.5.1), “more general”; SGA 3 VIII (7.1), “more general”.

> **Stacks Project, Tag 047O.**  Any group scheme over a field of characteristic `0` is
> reduced (Perrin, thèse I 1.1, I 3.9, II 2.4; Bull. SMF 104, Prop. 4.2.8): a scheme `G` with a
> group object structure on `f : G ⟶ Spec k` over `Spec k`, for `k` a field of characteristic
> `0`, is reduced.  No finiteness assumption on `f` is made; the locally finite type case is
> `AlgebraicGeometry.isReduced_of_groupScheme_of_charZero` ([Stacks, Tag 047N]).

```lean
theorem isReduced_of_grpObj_of_charZero (k : Type u) [Field k] [CharZero k] (G : Scheme.{u})
    (f : G ⟶ Spec (CommRingCat.of k)) [GrpObj (Over.mk f)] : IsReduced G
```

**`AlgebraicGeometry.isReduced_of_groupScheme_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/SmoothCharacteristicZero.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/SmoothCharacteristicZero.lean#L138). The attribute's comment: “locally of finite type case; the general case is cited to Perrin”. References: SGA 3 VIA (6.9), “partial”; SGA 3 VIIA (8.5.1), “more general”; SGA 3 VIII (7.1), “more general”.

> **Stacks Project, Tag 047O**, the case the source proves.  A locally algebraic group scheme
> over a field `k` of characteristic `0` is reduced: it is smooth over `k` by [Stacks, Tag 047N],
> `Spec k` is a reduced affine scheme, and a scheme smooth over a reduced affine scheme is
> reduced.
>
> The source states reducedness for an arbitrary group scheme over a field of characteristic `0`,
> citing Perrin for that generality, and records that the locally finite type case is the
> consequence of [Stacks, Tag 047N] proved here.

```lean
theorem isReduced_of_groupScheme_of_charZero (k : Type u) [Field k] [CharZero k] (G : Scheme.{u})
    (f : G ⟶ Spec (CommRingCat.of k)) [GrpObj (Over.mk f)] [LocallyOfFiniteType f] :
    IsReduced G
```

**`AlgebraicGeometry.isReduced_of_groupScheme_of_charZero_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HopfAlgebra/ReducedCharacteristicZero.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HopfAlgebra/ReducedCharacteristicZero.lean#L90). The attribute's comment: “for affine group schemes”. References: SGA 3 VIA (6.9), “partial”; SGA 3 VIIA (8.5.1), “more general”; SGA 3 VIII (7.1), “affine group schemes”.

> **Stacks Project, Tag 047O**, for affine group schemes.  An affine group scheme over a field
> of characteristic `0` is reduced, with no finiteness hypothesis: its ring of global sections is a
> commutative Hopf algebra, reduced by `HopfAlgebra.isReduced_of_charZero`.

```lean
theorem isReduced_of_groupScheme_of_charZero_of_isAffine (k : Type u) [Field k] [CharZero k]
    (G : Scheme.{u}) (f : G ⟶ Spec (CommRingCat.of k)) [GrpObj (Over.mk f)] [IsAffine G] :
    IsReduced G
```

## Tag 047P, a lemma

[Tag 047P](https://stacks.math.columbia.edu/tag/047P) in the Stacks Project.

**`AlgebraicGeometry.smooth_of_isReduced_groupScheme_of_perfectField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/SmoothPerfectField.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/SmoothPerfectField.lean#L48). References: EGA IV (15.6.10), “special case”; SGA 3 VIIA (8.3), “Smoothness clause”; SGA 3 XII (1.0), “partial”; SGA 3 XV (4.6), “(2), special case”.

> Let `k` be a perfect field and let `G` be a reduced locally algebraic group scheme over `k`,
> that is, a reduced scheme whose structure morphism `f : G ⟶ Spec k` is locally of finite type and
> which is a group object over `Spec k`. Then `f` is smooth.

```lean
theorem smooth_of_isReduced_groupScheme_of_perfectField (k : Type u) [Field k] [PerfectField k]
    (G : Scheme.{u}) (f : G ⟶ Spec (CommRingCat.of k)) [GrpObj (Over.mk f)]
    [LocallyOfFiniteType f] [IsReduced G] :
    Smooth f
```

## Tag 0B7S, a lemma

[Tag 0B7S](https://stacks.math.columbia.edu/tag/0B7S) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpen_containing_rational_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/RationalPointsAffineOpen.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/RationalPointsAffineOpen.lean#L287). References: SGA 3 XII (6.1).

> A finite family of rational points of a group scheme locally of finite type over an
> algebraically closed field lies in an affine open.

```lean
theorem exists_affineOpen_containing_rational_points (k : Type u) [Field k] [IsAlgClosed k]
    (G : Grp (Over (Spec (.of k)))) [LocallyOfFiniteType G.X.hom] {σ : Type v} [Finite σ]
    (g : σ → (Over.mk (𝟙 (Spec (.of k))) ⟶ G.X)) :
    ∃ U : G.X.left.Opens, IsAffineOpen U ∧
      ∀ i, (g i).left.base (⊥ : PrimeSpectrum k) ∈ U
```

## Tag 0BF7, a lemma

[Tag 0BF7](https://stacks.math.columbia.edu/tag/0BF7) in the Stacks Project.

**`AlgebraicGeometry.isQuasiProjective_of_groupScheme_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/QuasiProjective.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/QuasiProjective.lean#L168). References: SGA 3 VIB (5.5), “special case”.

> Let `k` be a field and `G` an algebraic group scheme over `k`. Then `G` is quasi-projective
> over `k`.

```lean
theorem isQuasiProjective_of_groupScheme_over_field
    (G : Grp (Over (Spec (CommRingCat.of k)))) [LocallyOfFiniteType G.X.hom]
    [QuasiCompact G.X.hom] :
    IsQuasiProjective G.X.hom
```

## Tag 0BF8, a lemma

[Tag 0BF8](https://stacks.math.columbia.edu/tag/0BF8) in the Stacks Project.

**`Stacks.Groupoids.IsCentralPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Center.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Center.lean#L91). The attribute's comment: “the functorial centre”. References: SGA 3 I (2.3.6), “center”; SGA 3 VIII (6.5).

> A relative point of a group scheme lies in its functorial centre if it commutes with every
> point after every base change of its domain.

```lean
def IsCentralPoint {S : Scheme.{u}} (G : Grp (Over S)) {T : Over S} (h : T ⟶ G.X) : Prop
```

**`Stacks.Groupoids.exists_closedSubgroupScheme_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Center.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/OverField/Center.lean#L391). The attribute's comment: “representability of the centre by a closed subgroup scheme”. References: SGA 3 VIB (6.2.4), “special case”; SGA 3 VIB (6.2.5), “(i), special case”; SGA 3 VIB (6.2.6), “more general”; SGA 3 VIB (6.5.5), “Clause a), special case”; SGA 3 VIB (7.3.0), “special case”; SGA 3 VIII (6.5), “special case”; SGA 3 VIII (6.7), “first item, special case”.

> **Stacks Project, Tag 0BF8.** The centre of a locally algebraic group scheme over a field is
> a closed subgroup scheme: the functorial centre `Stacks.Groupoids.IsCentralPoint` is represented
> by a closed subgroup scheme of `G`.
>
> The group scheme is separated over the field by Tag 047L, so for each chart `A` of the affine
> open cover of `G` the locus where a point of `A` and a point of `G` commute is a closed subscheme
> of `A ⊗ G`; its Weil restriction `W` along the projection to `G`, which exists by
> `Stacks.Groupoids.hasWeilRestrictionAffineOverField`, universally cuts out "commutes with every
> point of `A`".  The intersection of the `W` over all charts represents the centre by
> `isCentralPoint_iff_affineCover`.

```lean
theorem exists_closedSubgroupScheme_center {k : Type u} [Field k]
    (G : Grp (Over (Spec (.of k))))
    [LocallyOfFiniteType G.X.hom] :
    ∃ Z : ClosedSubgroupScheme G,
      ∀ (T : Over (Spec (.of k))) (h : T ⟶ G.X),
        (∃ z : T ⟶ Z.carrier.X, z ≫ Z.ι.hom.hom = h) ↔ IsCentralPoint G h
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.8, Tag 0BF6](https://stacks.math.columbia.edu/tag/0BF6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
