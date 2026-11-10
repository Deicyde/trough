---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEtaleEquivalenceRelation_restrict, AlgebraicGeometry.GroupoidScheme.isOpenImmersion_restrictionQuotientMap_of_isInvariantSet, AlgebraicGeometry.isOpenImmersion_restrictedQuotientMap, AlgebraicGeometry.Space.isOpenImmersion_restrictedQuotientMap, AlgebraicGeometry.Space.quotientMap_isPullback, AlgebraicGeometry.Space.quotientMap_surjective, AlgebraicGeometry.Space.quotientMap_etale, AlgebraicGeometry.Space.quotientPresentation
statement: formalized
proof: formalized
---

# 65.10 Algebraic spaces and equivalence relations

Section 65.10 of the Stacks Project, [Tag 0264](https://stacks.math.columbia.edu/tag/0264). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02WT, a lemma

[Tag 02WT](https://stacks.math.columbia.edu/tag/02WT) in the Stacks Project.

**`AlgebraicGeometry.Space.isEtaleEquivalenceRelation_restrict`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Restriction.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Restriction.lean#L93).

> Restricting an étale equivalence relation along an étale morphism again gives an étale
> equivalence relation.

```lean
instance isEtaleEquivalenceRelation_restrict (j : Stacks.Groupoids.PreRelation R U)
    (g : U' ⟶ U) [Stacks.Groupoids.IsEtaleEquivalenceRelation j] [Etale g.left] :
    Stacks.Groupoids.IsEtaleEquivalenceRelation (AlgebraicGeometry.PreRelation.restrict j g)
```

## Tag 02WU, a lemma

[Tag 02WU](https://stacks.math.columbia.edu/tag/02WU) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.isOpenImmersion_restrictionQuotientMap_of_isInvariantSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/QuotientSheaf/OpenSaturation.lean, line 906](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/QuotientSheaf/OpenSaturation.lean#L906).

> **Stacks 02WU.** Let `(U, R, s, t, c)` be a groupoid scheme over `S` and let `i : V ⟶ U`
> be an open immersion of schemes over `S` whose range is invariant under the arrows of the
> groupoid.  Then the map of fppf quotient sheaves `V/R|_V ⟶ U/R` induced by the restriction of
> the groupoid along `i` is representable, and is an open immersion; so `V/R|_V` is an open
> subspace of `U/R`.
>
> The Stacks Project states this for a pre-relation `j = (s, t) : R → U ×_S U` which is an
> equivalence relation with `s, t` surjective, flat and locally of finite presentation, and an
> arbitrary flat, locally finitely presented `g : U' → U`.  Those hypotheses enter only to make
> the saturation `t(s^{-1}(g(U')))` an open subscheme of `U` over which `g` is an fppf covering.
> Here the saturation is the given invariant open itself and the covering is split by the
> identity arrow of the groupoid, so no flatness is needed of anything.

```lean
theorem isOpenImmersion_restrictionQuotientMap_of_isInvariantSet
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (G : GroupoidScheme S) {W : Over S} (i : W ⟶ G.objects) [IsOpenImmersion i.left]
    (hi : IsInvariantSet G (Set.range i.left.base)) :
    Space.IsOpenImmersion B S hS
      (restrictionQuotientMap (BigFppfOver.topology B S hS) (Over.post B.inclusion) G i
        (restrict G i)).1
```

**`AlgebraicGeometry.isOpenImmersion_restrictedQuotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafFppfOpenImmersion.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafFppfOpenImmersion.lean#L194).

> **Stacks 02WU.** Let `j = (t, s) : R ⟶ U ×_S U` be an equivalence relation of schemes over
> `S` whose source and target maps are surjective, flat and locally of finite presentation, and
> let `g : U' ⟶ U` be flat and locally of finite presentation. The induced map `U'/R' ⟶ U/R` of
> quotient sheaves on the big fppf site over `S` is representable and an open immersion.

```lean
theorem isOpenImmersion_restrictedQuotientMap (B : BigFppfSite.{u}) (hS : B.Contains S)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (j : PreRelation R U) (g : U' ⟶ U) [IsEquivalenceRelation j.target j.source]
    (hs_surj : Surjective j.source.left) (ht_surj : Surjective j.target.left)
    (hs_flat : Flat j.source.left) (ht_flat : Flat j.target.left)
    (hs_lfp : LocallyOfFinitePresentation j.source.left)
    (ht_lfp : LocallyOfFinitePresentation j.target.left)
    (hg_flat : Flat g.left) (hg_lfp : LocallyOfFinitePresentation g.left) :
    Space.IsOpenImmersion B S hS
      (restrictQuotientSheafMap (BigFppfOver.topology B S hS)
        (CategoryTheory.Over.post (X := B.obj hS) B.inclusion) j g).hom
```

**`AlgebraicGeometry.Space.isOpenImmersion_restrictedQuotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RestrictedQuotientOpenImmersion.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RestrictedQuotientOpenImmersion.lean#L292).

> **Stacks 02WU.** Let `j` be an equivalence relation on `U` over `S` whose source and
> target maps are surjective, flat and locally of finite presentation, and let `g : U' ⟶ U` be
> flat and locally of finite presentation. Then the induced map of fppf quotient sheaves
> `U'/R' ⟶ U/R` is representable by open immersions.

```lean
theorem isOpenImmersion_restrictedQuotientMap
    (B : BigFppfSite.{u}) (hS : B.Contains S)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (j : PreRelation R U) (g : U' ⟶ U)
    [IsEquivalenceRelation j.target j.source]
    (hs_surj : Surjective j.source.left)
    (ht_surj : Surjective j.target.left)
    (hs_flat : Flat j.source.left)
    (ht_flat : Flat j.target.left)
    (hs_lfp : LocallyOfFinitePresentation j.source.left)
    (ht_lfp : LocallyOfFinitePresentation j.target.left)
    (hg_flat : Flat g.left)
    (hg_lfp : LocallyOfFinitePresentation g.left) :
    IsOpenImmersion B S hS
      (restrictQuotientSheafMap (BigFppfOver.topology B S hS)
        (Over.post (X := B.obj hS) B.inclusion) j g).hom
```

## Tag 02WV, a lemma

[Tag 02WV](https://stacks.math.columbia.edu/tag/02WV) in the Stacks Project.

**`AlgebraicGeometry.Space.quotientMap_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean#L272). The attribute's comment: “kernel pair”.

> The relation is the fibre product `U ×_{U/R} U`. Nothing is assumed about the quotient.

```lean
theorem quotientMap_isPullback
    [IsEtaleEquivalenceRelation (relation B S hS s t)] :
    IsPullback (yoneda.map t) (yoneda.map s)
      (quotientMap B S hS s t) (quotientMap B S hS s t)
```

**`AlgebraicGeometry.Space.quotientMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean#L449). The attribute's comment: “surjective”.

> The quotient map of an étale equivalence relation is surjective after every representable
> base change, as soon as it is representable.

```lean
theorem quotientMap_surjective
    [IsEtaleEquivalenceRelation (relation B S hS s t)]
    (hrep : yoneda.relativelyRepresentable (quotientMap B S hS s t)) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)))
      (quotientMap B S hS s t)
```

**`AlgebraicGeometry.Space.quotientMap_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean#L462). The attribute's comment: “étale”.

> The quotient map of an étale equivalence relation is étale after every representable base
> change, as soon as it is representable.

```lean
theorem quotientMap_etale
    [IsEtaleEquivalenceRelation (relation B S hS s t)]
    (hrep : yoneda.relativelyRepresentable (quotientMap B S hS s t)) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)))
      (quotientMap B S hS s t)
```

**`AlgebraicGeometry.Space.quotientPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean#L479). The attribute's comment: “presentation”.

> An étale equivalence relation whose quotient sheaf is an algebraic space presents that
> algebraic space.

```lean
noncomputable def quotientPresentation
    [IsEtaleEquivalenceRelation (relation B S hS s t)]
    (hQ : IsAlgebraicSpace B S hS
      (quotientSheaf (BigFppfOver.topology B S hS)
        (Over.post B.inclusion) (relation B S hS s t)).obj) :
    Presentation B S hS _ hQ
```

## Tag 0265, a lemma

[Tag 0265](https://stacks.math.columbia.edu/tag/0265) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_affineBase_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean#L533). The attribute's comment: “the quotient sheaf is an algebraic space”.

> **Stacks 0265, the algebraic-space property.** The quotient sheaf of an étale equivalence
> relation on an object of the big fppf site of `S` is an algebraic space over `S`. Stacks 0265
> assumes the underlying scheme of `U` affine; the proof does not use it.
>
> This is `AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_quasiAffineDescent` with its
> hypothesis `h0247` discharged.

```lean
theorem isAlgebraicSpace_quotientSheaf_of_affineBase_unconditional :
    IsAlgebraicSpace B S hS
      (quotientSheaf (BigFppfOver.topology B S hS) (Over.post B.inclusion) j).obj
```

**`AlgebraicGeometry.Space.surjective_toQuotientSheaf_of_affineBase_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean#L544). The attribute's comment: “the quotient map is surjective”.

> **Stacks 0265, surjectivity of the quotient map.** This is
> `AlgebraicGeometry.Space.surjective_toQuotientSheaf_of_quasiAffineDescent` with its hypothesis
> `h0247` discharged.

```lean
theorem surjective_toQuotientSheaf_of_affineBase_unconditional :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)))
      (yonedaEquiv.symm
        ((toQuotientSheaf (BigFppfOver.topology B S hS)
          (Over.post B.inclusion) j).app (Opposite.op U)
          (𝟙 ((Over.post B.inclusion).obj U))))
```

**`AlgebraicGeometry.Space.etale_toQuotientSheaf_of_affineBase_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatChartDescent.lean#L560). The attribute's comment: “the quotient map is étale”.

> **Stacks 0265, étaleness of the quotient map.** This is
> `AlgebraicGeometry.Space.etale_toQuotientSheaf_of_quasiAffineDescent` with its hypothesis `h0247`
> discharged.

```lean
theorem etale_toQuotientSheaf_of_affineBase_unconditional :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)))
      (yonedaEquiv.symm
        ((toQuotientSheaf (BigFppfOver.topology B S hS)
          (Over.post B.inclusion) j).app (Opposite.op U)
          (𝟙 ((Over.post B.inclusion).obj U))))
```

## Tag 02WW, a theorem

[Tag 02WW](https://stacks.math.columbia.edu/tag/02WW) in the Stacks Project.

**`AlgebraicGeometry.Space.uliftQuotientMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleQuotientPresentation.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleQuotientPresentation.lean#L157). The attribute's comment: “canonical quotient map”.

> The canonical map from the lifted functor of points of the presenting
> scheme to the lifted quotient sheaf of its relation.

```lean
def uliftQuotientMap [HasSheafify (BigFppfOver.topology B S hS) (Type (max u v))] :
    uliftYoneda.{v}.obj U ⟶ (uliftQuotientSheaf.{u, v} B S hS s t).obj
```

**`AlgebraicGeometry.Space.quotientMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PresentationFromQuotient.lean#L147). The attribute's comment: “canonical quotient map”.

> The canonical map from the presenting scheme to the quotient sheaf of its relation.

```lean
public noncomputable def quotientMap :
    yoneda.obj U ⟶
      (quotientSheaf (BigFppfOver.topology B S hS)
        (Over.post B.inclusion) (relation B S hS s t)).obj
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_quotient_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean#L115). The attribute's comment: “the quotient sheaf is an algebraic space”.

> **Stacks 02WW, the algebraic-space property.** The quotient sheaf of an étale equivalence
> relation on an object of the big fppf site of `S` is an algebraic space over `S`.
>
> This is `AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_relation_of_diagDescent` with
> its descent hypothesis discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft`.

```lean
theorem isAlgebraicSpace_quotient_unconditional
    [IsEtaleEquivalenceRelation (relation B S hS s t)] :
    IsAlgebraicSpace B S hS
      (quotientSheaf (BigFppfOver.topology B S hS)
        (Over.post B.inclusion) (relation B S hS s t)).obj
```

**`AlgebraicGeometry.Space.quotientMap_surjective_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean#L126). The attribute's comment: “the quotient map is surjective”.

> **Stacks 02WW, surjectivity of the quotient map.** The canonical map `U ⟶ U/R` is
> surjective after every representable base change.

```lean
theorem quotientMap_surjective_unconditional
    [IsEtaleEquivalenceRelation (relation B S hS s t)] :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)))
      (quotientMap B S hS s t)
```

**`AlgebraicGeometry.Space.quotientMap_etale_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean#L138). The attribute's comment: “the quotient map is étale”.

> **Stacks 02WW, étaleness of the quotient map.** The canonical map `U ⟶ U/R` is étale after
> every representable base change.

```lean
theorem quotientMap_etale_unconditional
    [IsEtaleEquivalenceRelation (relation B S hS s t)] :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)))
      (quotientMap B S hS s t)
```

**`AlgebraicGeometry.Space.quotientPresentation_unconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuotientSheafPresentationUnconditional.lean#L150). The attribute's comment: “the presentation”.

> **Stacks 02WW, the presentation.** An étale equivalence relation presents its quotient
> sheaf: `(U, R, U ⟶ U/R)` is a presentation of the algebraic space `U/R`.

```lean
noncomputable def quotientPresentation_unconditional
    [IsEtaleEquivalenceRelation (relation B S hS s t)] :
    Presentation B S hS _ (isAlgebraicSpace_quotient_unconditional B S hS s t)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.10, Tag 0264](https://stacks.math.columbia.edu/tag/0264)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
