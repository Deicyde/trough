---
declaration: section
origin: cited
lean: Stacks.Groupoids.GroupoidScheme.exists_restriction_locallyQuasiFinite_isIso_quotientMap, AlgebraicGeometry.GroupoidScheme.exists_locallyQuasiFinite_refinement_isIso_quotientMap, AlgebraicGeometry.exists_slice_locallyQuasiFinite
statement: formalized
proof: formalized
---

# 80.8 Slicing equivalence relations

Section 80.8 of the Stacks Project, [Tag 046L](https://stacks.math.columbia.edu/tag/046L). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0489, a lemma

[Tag 0489](https://stacks.math.columbia.edu/tag/0489) in the Stacks Project.

**`Stacks.Groupoids.GroupoidScheme.exists_restriction_locallyQuasiFinite_isIso_quotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationQuasiFiniteRefinement.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationQuasiFiniteRefinement.lean#L225). The attribute's comment: “the refinement with locally quasi-finite source and target and the same quotient sheaf, given the refinement data as `QuasiFiniteRefinement`. The tag itself, with nothing carried, is `AlgebraicGeometry.exists_locallyQuasiFinite_groupoid_quotientSheaf_iso` of `StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/CohenMacaulayQuotientUnchanged.lean`, which builds that data from the Cohen-Macaulay restriction and the reach map”.

> **Stacks Project, Tag 0489**, conditional on Steps 1 to 3 of its proof.
>
> Let `R` be a groupoid scheme over `S` whose target and source are an equivalence relation.
> Given a refinement in the sense of
> `Stacks.Groupoids.GroupoidScheme.QuasiFiniteRefinement` — a morphism `g : U' ⟶ U` whose reach
> map is flat, locally of finite presentation and locally quasi-finite and is a singleton covering
> of the site — the restriction `R' = R|_{U'}` is again an equivalence relation, its source and
> target are flat, locally of finite presentation, locally of finite type and locally
> quasi-finite, and the induced map `U'/R' ⟶ U/R` of quotient sheaves is an isomorphism.
>
> The conclusion is stated for *every* groupoid scheme realizing the restriction, which is
> stronger than producing one and avoids any appeal to the realization
> `AlgebraicGeometry.GroupoidScheme.restrict` built by `Classical.choice`.  The morphism
> `U' ⟶ U` carrying `R'` into `R` is the one recorded by
> `AlgebraicGeometry.GroupoidScheme.Restriction.hom`, so the clause of the tag that the
> isomorphism of quotient sheaves is induced by a morphism `U' ⟶ U` mapping `R'` into `R` is part
> of the statement rather than an afterthought.
>
> The flatness and local finite presentation hypotheses which the tag places on `s` and `t` are
> not assumed; see the module docstring.

```lean
theorem exists_restriction_locallyQuasiFinite_isIso_quotientMap
    (J : GrothendieckTopology C) [HasSheafify J (Type u)] (F : C ⥤ Over S) (hF : F.Full)
    (G : GroupoidScheme S) [IsEquivalenceRelation G.target G.source]
    (N : QuasiFiniteRefinement J F G) :
    ∃ (U' : Over S) (g : U' ⟶ G.objects),
      ∀ R' : AlgebraicGeometry.GroupoidScheme.Restriction G g,
      IsEquivalenceRelation R'.groupoid.target R'.groupoid.source ∧
      Flat R'.groupoid.source.left ∧
      LocallyOfFinitePresentation R'.groupoid.source.left ∧
      LocallyOfFiniteType R'.groupoid.source.left ∧
      LocallyQuasiFinite R'.groupoid.source.left ∧
      Flat R'.groupoid.target.left ∧
      LocallyOfFinitePresentation R'.groupoid.target.left ∧
      LocallyOfFiniteType R'.groupoid.target.left ∧
      LocallyQuasiFinite R'.groupoid.target.left ∧
      IsIso (restrictionQuotientMap J F G g R')
```

**`AlgebraicGeometry.GroupoidScheme.exists_locallyQuasiFinite_refinement_isIso_quotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationQuasiFiniteRefinementFppf.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationQuasiFiniteRefinementFppf.lean#L154). The attribute's comment: “unconditionally, with no assumed input: the hypotheses are exactly the tag's, that the source and target of the groupoid scheme are an equivalence relation and are flat and locally of finite presentation. The refined equivalence relation R' is the restriction H' along the second stage g' of the restriction H₁ along the first stage g₁ of the two-stage refinement that `exists_cohenMacaulay_and_quasiFinite_refinement` produces -- the Cohen-Macaulay open of Stacks 0460, then the disjoint union of the affine slices of Stacks 04N0 over the finite type points -- and the morphism U' ⟶ U of the tag is the composite g, over which the composite of the two restrictions' canonical morphisms carries R' into R. Its source and target are flat, locally of finite presentation, locally of finite type and locally quasi-finite, being base changes of the second stage's reach map by Stacks 04MV; it is an equivalence relation by `restriction_isEquivalenceRelation`; and U'/R' ⟶ U/R, the composite of the two stages' maps of quotient sheaves, is an isomorphism because each stage's reach map is flat, locally of finite presentation and surjective and therefore locally surjective on the functors of points of the big fppf site by `isLocallySurjective_points_map_of_fppf`, which Stacks 02VH turns into an isomorphism of quotient sheaves. No covering datum is assumed: on this site a flat, locally finitely presented, surjective morphism of Over S is locally surjective on points whatever the sizes of its source and target, so neither the disjoint union of Step 3 nor the source of either reach map has to be exhibited as an object of the site. The two stages are not collapsed into one morphism whose reach map is a covering, because the reach map of the composite factors through the base change of an immersion and so is not flat; the final conclusion instead gives the isomorphism of quotient sheaves for the restriction along the composite as well, by `isIso_restrictionQuotientMap_of_comp_reach`”.

> **Stacks Project, Tag 0489.**
>
> Let `(U, R, s, t, c, e, i)` be a groupoid scheme over `S` whose target and source maps form an
> equivalence relation and are flat and locally of finite presentation.  Then there are a scheme
> `U'` over `S`, a morphism `U' ⟶ U`, and an equivalence relation `R'` on `U'` mapping into `R`
> over it, whose source and target maps are flat, locally of finite presentation, locally of finite
> type and locally quasi-finite, and for which the induced map `U'/R' ⟶ U/R` of quotient sheaves on
> the big fppf site over `S` is an isomorphism.
>
> The refinement is produced in the two stages of the source proof: `g₁ : U₁ ⟶ U` is the inclusion
> of the Cohen-Macaulay open of Stacks 0460, `H₁` is the restriction of `R` along it,
> `g' : U' ⟶ U₁` is the disjoint union of the affine slices of Stacks 04N0 over the finite type
> points of `U₁`, and `R'` is the restriction `H'` of `H₁` along `g'`.  The morphism `U' ⟶ U` is the
> composite `g`, and the morphism of `R'` into `R` is the composite of the two restrictions'
> canonical morphisms, which lies over `g` by the second conclusion below.
>
> The last conclusion is more than the tag asks: the map of quotient sheaves induced by the
> restriction of `R` along the single morphism `g` is an isomorphism for *every* groupoid scheme
> realizing that restriction.  Together with the isomorphism for `R'` it says that the two
> descriptions of the refined relation — the restriction of the restriction, and the restriction
> along the composite — have the same quotient; that they are the same relation is Stacks 04MW,
> which is not used here.
>
> The last two conclusions are the size estimates of the two stages, also more than the tag asks:
> the first stage is an open of `U`, and the second is a disjoint union of affine immersions
> locally of finite presentation indexed by the points of the first, so
> `size U₁ ≤ size U` and `size U' ≤ 2 ^ size U`.  They are not used for the isomorphism of
> quotient sheaves — that needs no cardinality hypothesis at all, see the implementation notes —
> but they are what a later consumer needs in order to exhibit `U'` and the arrow scheme of `R'`
> as *objects of the site*, which the engine of Stacks 02WW requires and which the existential
> form of this statement would otherwise destroy.

```lean
theorem exists_locallyQuasiFinite_refinement_isIso_quotientMap
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (G : GroupoidScheme S) [IsEquivalenceRelation G.target G.source]
    [Flat G.source.left] [Flat G.target.left]
    [LocallyOfFinitePresentation G.source.left] [LocallyOfFinitePresentation G.target.left] :
    letI := BigFppfOver.hasSheafify_type B S hS
    ∃ (U₁ : Over S) (g₁ : U₁ ⟶ G.objects) (H₁ : Restriction G g₁) (U' : Over S)
      (g' : U' ⟶ H₁.groupoid.objects) (H' : Restriction H₁.groupoid g')
      (g : U' ⟶ G.objects),
      g = g' ≫ H₁.hom.mapObjects ∧
      H'.hom.mapObjects ≫ H₁.hom.mapObjects = eqToHom H'.objects_eq ≫ g ∧
      IsEquivalenceRelation H'.groupoid.target H'.groupoid.source ∧
      Flat H'.groupoid.source.left ∧
      LocallyOfFinitePresentation H'.groupoid.source.left ∧
      LocallyOfFiniteType H'.groupoid.source.left ∧
      LocallyQuasiFinite H'.groupoid.source.left ∧
      Flat H'.groupoid.target.left ∧
      LocallyOfFinitePresentation H'.groupoid.target.left ∧
      LocallyOfFiniteType H'.groupoid.target.left ∧
      LocallyQuasiFinite H'.groupoid.target.left ∧
      IsIso (restrictionQuotientMap (BigFppfOver.topology B S hS) (Over.post B.inclusion)
          H₁.groupoid g' H' ≫
        restrictionQuotientMap (BigFppfOver.topology B S hS) (Over.post B.inclusion) G g₁ H₁) ∧
      (∀ H : Restriction G g,
        IsIso (restrictionQuotientMap (BigFppfOver.topology B S hS)
          (Over.post B.inclusion) G g H)) ∧
      U₁.left.size ≤ G.objects.left.size ∧
      U'.left.size ≤ 2 ^ G.objects.left.size
```

**`AlgebraicGeometry.exists_slice_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationQuasiFiniteSlice.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/EquivalenceRelationQuasiFiniteSlice.lean#L722).

> An equivalence relation on schemes over `S` with flat, locally finitely
> presented source and target maps admits a slice: an equivalence relation whose
> source and target maps are flat, locally of finite presentation and locally
> quasi-finite, together with a morphism `g` of object schemes and a morphism `r`
> of arrow schemes over it, inducing an isomorphism of fppf quotient sheaves.

```lean
public theorem exists_slice_locallyQuasiFinite
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (AlgebraicGeometry.BigFppfOver.topology B S hS) (Type u)]
    {R U : AlgebraicGeometry.BigFppfOver B S hS}
    (j : Stacks.Groupoids.PreRelation (S := S) ((Over.post B.inclusion).obj R)
      ((Over.post B.inclusion).obj U))
    [IsEquivalenceRelation j.target j.source]
    [Flat j.source.left] [LocallyOfFinitePresentation j.source.left]
    [Flat j.target.left] [LocallyOfFinitePresentation j.target.left] :
    ∃ (U' R' : AlgebraicGeometry.BigFppfOver B S hS)
      (j' : Stacks.Groupoids.PreRelation (S := S) ((Over.post B.inclusion).obj R')
        ((Over.post B.inclusion).obj U'))
      (g : U' ⟶ U) (r : R' ⟶ R)
      (hs : (Over.post B.inclusion).map r ≫ j.source =
        j'.source ≫ (Over.post B.inclusion).map g)
      (ht : (Over.post B.inclusion).map r ≫ j.target =
        j'.target ≫ (Over.post B.inclusion).map g),
      IsEquivalenceRelation j'.target j'.source ∧
        Flat j'.source.left ∧ LocallyOfFinitePresentation j'.source.left ∧
        LocallyQuasiFinite j'.source.left ∧
        Flat j'.target.left ∧ LocallyOfFinitePresentation j'.target.left ∧
        LocallyQuasiFinite j'.target.left ∧
      IsIso (Stacks.Groupoids.quotientSheafMap
          (AlgebraicGeometry.BigFppfOver.topology B S hS) (Over.post B.inclusion) j' j
          ((Over.post B.inclusion).map r) ((Over.post B.inclusion).map g)
          hs ht)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.8, Tag 046L](https://stacks.math.columbia.edu/tag/046L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
