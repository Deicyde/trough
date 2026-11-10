---
declaration: section
origin: cited
lean: AlgebraicGeometry.GeometricPoint, AlgebraicGeometry.GeometricPoint.LiesOver, AlgebraicGeometry.GeometricPoint.EtaleNeighborhood, AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.Hom, AlgebraicGeometry.Etale.instHasOfPostcompPropertyScheme, AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.toEtaleNeighborhood, AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.geometricPoint_liesOver_iff, AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.toEtaleNeighborhood_surjective
statement: formalized
proof: formalized
---

# 59.29 Neighborhoods, stalks and points

Section 59.29 of the Stacks Project, [Tag 03PN](https://stacks.math.columbia.edu/tag/03PN). 11 tags here are carried by 43 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03PO, a definition

[Tag 03PO](https://stacks.math.columbia.edu/tag/03PO) in the Stacks Project.

**`AlgebraicGeometry.GeometricPoint`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean#L47). The attribute's comment: “part (1)”. References: SGA 4½ Arcata (2.3.1), “special case”; SGA 7 XIX (1.4).

> A geometric point of a scheme is a morphism from the spectrum of an algebraically closed field.

```lean
structure GeometricPoint (S : Scheme.{u})
```

**`AlgebraicGeometry.GeometricPoint.LiesOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean#L66). The attribute's comment: “part (2)”.

> A geometric point lies over the point which is its image in the underlying topological space.

```lean
abbrev LiesOver {S : Scheme.{u}} (s : GeometricPoint S) (x : S) : Prop
```

**`AlgebraicGeometry.GeometricPoint.EtaleNeighborhood`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean#L77). The attribute's comment: “part (3)”. References: SGA 4 VIII (3.9), “objects of C_ξ”.

> An étale neighborhood of a geometric point consists of an étale scheme over the base together
> with a lift of the geometric point.

```lean
structure EtaleNeighborhood {S : Scheme.{u}} (s : GeometricPoint S)
```

**`AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/Basic.lean#L95). The attribute's comment: “part (4)”.

> A morphism of étale neighborhoods is a morphism over the base which carries the chosen lift to
> the chosen lift.

```lean
structure Hom {S : Scheme.{u}} {s : GeometricPoint S} (U V : EtaleNeighborhood s)
```

## Tag 03PP, a remark

[Tag 03PP](https://stacks.math.columbia.edu/tag/03PP) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Etale.instHasOfPostcompPropertyScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Etale.instHasOfPostcompPropertyScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L163) (StacksFrontier): “an S-morphism between étale S-schemes is étale”. References: EGA IV (17.1.5), “special case”; EGA IV (17.3.5), “étale clause”; SGA 1 V (3.3), “special case”; SGA 4 VII (1.2), “more general”; SGA 4½ Arcata (2.1.3); SGA 4½ Arcata (2.1.4), “more general”.

## Tag 04HT, a remark

[Tag 04HT](https://stacks.math.columbia.edu/tag/04HT) in the Stacks Project.

**`AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.toEtaleNeighborhood`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/PointNeighborhood.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/PointNeighborhood.lean#L59). The attribute's comment: “first direction”.

> An étale neighbourhood `(U, ū)` of a geometric point `σ` lying over `s` gives the étale
> neighbourhood `(U, u)` of `(S, s)`, where `u` is the image of `ū`.

```lean
def toEtaleNeighborhood (U : σ.EtaleNeighborhood) (h : σ.LiesOver s) :
    AlgebraicGeometry.EtaleNeighborhood S s
```

**`AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.geometricPoint_liesOver_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/PointNeighborhood.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/PointNeighborhood.lean#L88). The attribute's comment: “first direction: u is the unique point under ū”.

> The distinguished point `u` of the étale neighbourhood `(U, u)` attached to `(U, ū)` is the
> unique point of `U` over which the geometric point `ū` lies.

```lean
theorem geometricPoint_liesOver_iff (U : σ.EtaleNeighborhood) (h : σ.LiesOver s)
    (x : U.scheme) : U.geometricPoint.LiesOver x ↔ x = (U.toEtaleNeighborhood h).point
```

**`AlgebraicGeometry.GeometricPoint.EtaleNeighborhood.toEtaleNeighborhood_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/PointNeighborhood.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/PointNeighborhood.lean#L96). The attribute's comment: “converse direction”.

> Conversely, every étale neighbourhood `(U, u)` of `(S, s)` comes from an étale neighbourhood
> of a geometric point `σ` lying over `s`: there is a geometric point `ū` of `U` lying over `u`
> such that `(U, ū)` is an étale neighbourhood of `(S, σ)`.

```lean
theorem toEtaleNeighborhood_surjective (h : σ.LiesOver s) :
    Function.Surjective fun U : σ.EtaleNeighborhood ↦ U.toEtaleNeighborhood h
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.exists_fac_of_etale_of_isSepClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.exists_fac_of_etale_of_isSepClosed#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L318) (StacksFrontier): “converse: a geometric point ū of U over u with (U, ū) → (S, s̄)”. References: EGA IV (18.8.1), “(a)⇒(c), special case”; SGA 4 VIII (3.2), “partial”.

## Tag 03PQ, a lemma

[Tag 03PQ](https://stacks.math.columbia.edu/tag/03PQ) in the Stacks Project.

Declarations registered for the tag:

- [`instIsCofilteredElementsEtaleCompOverForgetObjOppositeFunctorTypeCoyonedaOpMk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instIsCofilteredElementsEtaleCompOverForgetObjOppositeFunctorTypeCoyonedaOpMk#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch59.lean#L166) (StacksFrontier): “the étale neighborhoods of a geometric point s : Spec Ω → S (Ω separably closed) form a cofiltered category”.

## Tag 03PR, a lemma

[Tag 03PR](https://stacks.math.columbia.edu/tag/03PR) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Cover.exists_etaleNeighborhood_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/CoverLift.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/CoverLift.lean#L44).

> Let `s : Spec Ω ⟶ S` be a geometric point of `S`, with `Ω` separably closed, and let
> `(U, u)` be an étale neighborhood of `s`, that is `f : U ⟶ S` is étale and `u ≫ f = s`. Then
> for every étale covering `𝒰` of `U` there are an index `i` and a lift `uᵢ` of `u` to `𝒰.X i`,
> so that `(𝒰.X i, uᵢ)` is an étale neighborhood of `s` and `𝒰.f i` is a morphism of étale
> neighborhoods `(𝒰.X i, uᵢ) ⟶ (U, u)`.

```lean
theorem exists_etaleNeighborhood_lift {S U : Scheme.{u}} {Ω : Type u} [Field Ω] [IsSepClosed Ω]
    (s : Spec (.of Ω) ⟶ S) (f : U ⟶ S) [Etale f] (u : Spec (.of Ω) ⟶ U) (hu : u ≫ f = s)
    (𝒰 : U.Cover.{v} etalePrecoverage) :
    ∃ (i : 𝒰.I₀) (uᵢ : Spec (.of Ω) ⟶ 𝒰.X i),
      Etale (𝒰.f i ≫ f) ∧ uᵢ ≫ 𝒰.f i ≫ f = s ∧ uᵢ ≫ 𝒰.f i = u
```

## Tag 040R, a definition

[Tag 040R](https://stacks.math.columbia.edu/tag/040R) in the Stacks Project.

**`AlgebraicGeometry.geometricPointFiber_initiallySmall`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointFiber.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointFiber.lean#L156). The attribute's comment: “small neighborhood basis”.

> The neighborhoods of a geometric point in the chosen small étale site admit a
> universe-`u` cofinal subcategory.

```lean
public instance geometricPointFiber_initiallySmall :
    InitiallySmall.{u} (geometricPointFiber B S hS s).Elements
```

**`AlgebraicGeometry.etaleStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointFiber.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointFiber.lean#L178).

> The stalk of a presheaf on the small étale site at a geometric point, as the colimit over
> its étale neighborhoods.

```lean
public def etaleStalk {A : Type v} [Category.{w} A] (F : (SmallEtale B S hS)ᵒᵖ ⥤ A)
    [HasColimit ((CategoryOfElements.π (geometricPointFiber B S hS s)).op ⋙ F)] : A
```

## Tag 04FM, a lemma

[Tag 04FM](https://stacks.math.columbia.edu/tag/04FM) in the Stacks Project.

**`AlgebraicGeometry.etaleStalkSkyscraperAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/GeometricSkyscraper.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/GeometricSkyscraper.lean#L73). The attribute's comment: “the stalk at a geometric point is left adjoint to the skyscraper there”.

> **Stacks 04FM.** The stalk functor at a geometric point `s̄` of `S` is left adjoint to the
> skyscraper functor at `s̄`: a map `F_s̄ ⟶ M` is the same as a map `F ⟶ s̄_* M`.

```lean
public def etaleStalkSkyscraperAdjunction [HasColimitsOfSize.{u, u} A] :
    (geometricPointSitePoint B S hS s).sheafFiber (A := A) ⊣
      etaleSkyscraperFunctor B S hS s A
```

**`AlgebraicGeometry.geometricPointFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointFiber.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointFiber.lean#L81). The attribute's comment: “the functor `u : U ↦ |U_s̄|`”.

> The lifts of a geometric point to objects of the small étale site, i.e. the functor
>
> `u : S_étale ⟶ Sets`, `U ↦ {ū such that (U, ū) is an étale neighbourhood of s̄}`
>
> sending `U` to the morphisms `s̄ ⟶ U` over `S`.

```lean
public def geometricPointFiber : SmallEtale B S hS ⥤ Type u
```

**`AlgebraicGeometry.geometricPointFiberObjEquivGeometricFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/GeometricFibre.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/GeometricFibre.lean#L128). The attribute's comment: “the two descriptions of `u(U)`: the geometric fibre and the étale neighbourhoods”.

> **Stacks Project, Tag 04FM**, the identification of the two descriptions of the value of the
> fibre functor. For an object `U` of the small étale site of `S`, the set
> `(geometricPointFiber B S hS s).obj U` of lifts of the geometric point `s` to `U` — the set
> `{ū : (U, ū) is an étale neighbourhood of s̄}` of the source — is in bijection with the
> underlying set `|U_s̄|` of the geometric fibre of `U` at `s`.

```lean
def geometricPointFiberObjEquivGeometricFibre (U : SmallEtale B S hS) :
    (geometricPointFiber B S hS s).obj U ≃
      ↥(pullback (B.inclusion.map U.obj.hom) s.hom)
```

**`AlgebraicGeometry.geometricPointSitePoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SitePoint.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SitePoint.lean#L157). The attribute's comment: “the functor `u` defines a point of the small étale site”.

> **Stacks Project, Tag 04FM.** The functor `u` of
> `AlgebraicGeometry.geometricPointFiber` defines a point `p` of the site `S_étale`: a geometric
> point of `S`, viewed as a point of the small étale site of `S`, with fiber functor `u`.
>
> The source obtains this from the criterion of Sites, Proposition 00YC, checking that `u(S)` is
> a singleton, that `u` preserves fibre products, and that `∐ u(U_i) ⟶ u(U)` is surjective for a
> covering. Mathlib's `CategoryTheory.GrothendieckTopology.Point` asks instead for
> cofilteredness of the category of elements of `u`, which for this `u` is the cofilteredness of
> the category of étale neighbourhoods of the geometric point
> (`AlgebraicGeometry.isCofiltered_geometricPointFiber_elements`), together with the joint
> surjectivity, which is `AlgebraicGeometry.geometricPointFiber_jointly_surjective`. The two
> descriptions of a point agree on a site with finite limits by
> `CategoryTheory.GrothendieckTopology.Point.equivFiber`, the formalization of Tag 00YC.

```lean
public def geometricPointSitePoint :
    (SmallEtale.topology B S hS).Point
```

**`AlgebraicGeometry.etaleStalk_eq_presheafFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SitePoint.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/SitePoint.lean#L178). The attribute's comment: “the stalk functor of `p` is the stalk at the geometric point”.

> **Stacks Project, Tag 04FM**, the final assertion: the stalk functor `F ↦ F_p` attached to
> the point `p = AlgebraicGeometry.geometricPointSitePoint` by Sites, Equation 04EH — which is
> `CategoryTheory.GrothendieckTopology.Point.presheafFiber` — is the stalk functor
> `F ↦ F_s̄` at the geometric point of Tag 040R, which is `AlgebraicGeometry.etaleStalk`. Both
> are given by the same colimit over the category of étale neighbourhoods, so the general theory
> of points of a site — exactness, invariance under sheafification, commutation with colimits —
> applies to the stalk at a geometric point.

```lean
public theorem etaleStalk_eq_presheafFiber {A : Type v} [Category.{w} A]
    [HasColimitsOfSize.{u, u} A] (F : (SmallEtale B S hS)ᵒᵖ ⥤ A) :
    etaleStalk B S hS s F = (geometricPointSitePoint B S hS s).presheafFiber.obj F
```

## Tag 04FN, a remark

[Tag 04FN](https://stacks.math.columbia.edu/tag/04FN) in the Stacks Project.

**`AlgebraicGeometry.GeometricPoint.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L432). The attribute's comment: “morphism of geometric points”.

> A morphism of geometric points over the same scheme.

```lean
public structure Hom {S : Scheme.{u}}
    (s t : GeometricPoint S)
```

**`AlgebraicGeometry.geometricPointFiberMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L444). The attribute's comment: “map of geometric fibers”.

> A lift of `t` to an étale scheme yields a lift of `s` by precomposition.

```lean
public def geometricPointFiberMap (a : GeometricPoint.Hom s t) :
    geometricPointFiber B S hS t ⟶
      geometricPointFiber B S hS s
```

**`AlgebraicGeometry.geometricPointFiberMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L494). The attribute's comment: “isomorphism of site points”.

> For a morphism `a : s ⟶ t` of geometric points of `S`, the map of geometric fibres
> `geometricPointFiberMap B S hS a`, given by precomposition with `a`, is an isomorphism.

```lean
public theorem geometricPointFiberMap_isIso :
    IsIso (geometricPointFiberMap B S hS a)
```

**`AlgebraicGeometry.neighborhoodFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L509). The attribute's comment: “functor on neighborhoods”.

> Restriction of an étale neighborhood of `t` along `a`.

```lean
public def neighborhoodFunctor (a : GeometricPoint.Hom s t) :
    (geometricPointFiber B S hS t).Elements ⥤
      (geometricPointFiber B S hS s).Elements
```

**`AlgebraicGeometry.neighborhoodFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L516). The attribute's comment: “equivalence of neighborhoods”.

> Restriction along `a` is an equivalence of étale-neighborhood categories.

```lean
public theorem neighborhoodFunctor_isEquivalence :
    (neighborhoodFunctor B S hS a).IsEquivalence
```

**`AlgebraicGeometry.geometricPointStalkMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L529). The attribute's comment: “canonical map of stalk functors”.

> The canonical map from the stalk at `t` to the stalk at `s`, natural in
> the presheaf.

```lean
public def geometricPointStalkMap (A : Type v) [Category.{w} A]
    [HasColimitsOfShape (geometricPointFiber B S hS t).Elementsᵒᵖ A]
    [HasColimitsOfShape (geometricPointFiber B S hS s).Elementsᵒᵖ A] :
    etaleStalkPresheafFunctor B S hS t A ⟶
      etaleStalkPresheafFunctor B S hS s A
```

**`AlgebraicGeometry.geometricPointStalkMap_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L548). The attribute's comment: “action on represented sections”.

> The canonical map takes the germ of `(U, u', σ)` to the germ of
> `(U, u' ∘ a, σ)`.

```lean
public theorem geometricPointStalkMap_germ
    (F : (SmallEtale B S hS)ᵒᵖ ⥤ Type u)
    (U : (geometricPointFiber B S hS t).Elementsᵒᵖ)
    (σ : F.obj (Opposite.op U.unop.1)) :
    (geometricPointStalkMap B S hS a (Type u)).app F
        ((colimit.ι
          ((CategoryOfElements.π (geometricPointFiber B S hS t)).op ⋙ F) U) σ) =
      (colimit.ι
        ((CategoryOfElements.π (geometricPointFiber B S hS s)).op ⋙ F)
        ((neighborhoodFunctor B S hS a).op.obj U)) σ
```

**`AlgebraicGeometry.geometricPointStalkMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L566). The attribute's comment: “isomorphism of stalk functors”.

> A morphism of geometric points induces a canonical natural isomorphism
> of étale stalk functors.

```lean
public theorem geometricPointStalkMap_isIso (A : Type v) [Category.{w} A]
    [HasColimitsOfShape (geometricPointFiber B S hS t).Elementsᵒᵖ A]
    [HasColimitsOfShape (geometricPointFiber B S hS s).Elementsᵒᵖ A] :
    IsIso (geometricPointStalkMap B S hS a A)
```

**`AlgebraicGeometry.smallEtalePointHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 587](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L587). The attribute's comment: “morphism of associated site points”.

> The morphism of points of the unrestricted small étale site induced by
> `a`. Its fiber component sends a lift `u'` to `u' ∘ a`.

```lean
public def smallEtalePointHom :
    Scheme.pointSmallEtale s.hom ⟶ Scheme.pointSmallEtale t.hom
```

**`AlgebraicGeometry.smallEtalePointHom_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean, line 605](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/GeometricPointStalkMap.lean#L605). The attribute's comment: “isomorphism of associated site points”.

> A morphism of geometric points induces an isomorphism of their associated
> points of the small étale site.

```lean
public theorem smallEtalePointHom_isIso : IsIso (smallEtalePointHom S a)
```

## Tag 03PT, a lemma

[Tag 03PT](https://stacks.math.columbia.edu/tag/03PT) in the Stacks Project.

**`AlgebraicGeometry.Scheme.pointSmallEtale_presheafFiber_ab_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean#L65). The attribute's comment: “(1) the stalk functor on abelian presheaves is exact”.

> **The stalk functor on abelian presheaves is exact.** For a geometric point `s` of `S`, the
> stalk functor `PAb(S_et) ⥤ Ab`, `𝓕 ↦ 𝓕_s̄`, commutes with finite limits and finite colimits.

```lean
theorem pointSmallEtale_presheafFiber_ab_exact :
    PreservesFiniteLimits ((pointSmallEtale s).presheafFiber (A := AddCommGrpCat.{max u v})) ∧
      PreservesFiniteColimits
        ((pointSmallEtale s).presheafFiber (A := AddCommGrpCat.{max u v}))
```

**`AlgebraicGeometry.Scheme.isIso_pointSmallEtale_presheafFiber_map_toSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean#L77). The attribute's comment: “(2) the stalk of a presheaf of sets equals the stalk of its sheafification”.

> **Stalks of a presheaf of sets and of its sheafification agree.** For a geometric point `s` of
> `S` and a presheaf of sets `𝓕` on `S_et`, the map `𝓕_s̄ ⟶ (𝓕^#)_s̄` induced by `𝓕 ⟶ 𝓕^#` is an
> isomorphism.

```lean
theorem isIso_pointSmallEtale_presheafFiber_map_toSheafify
    (F : S.Etaleᵒᵖ ⥤ Type u) :
    IsIso ((pointSmallEtale s).presheafFiber.map (toSheafify (smallEtaleTopology S) F))
```

**`AlgebraicGeometry.Scheme.isIso_pointSmallEtale_presheafFiber_map_toSheafify'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean#L86). The attribute's comment: “(2) the stalk of a presheaf of sets equals the stalk of its sheafification”.

> **Stalks of a presheaf of sets and of its sheafification agree**, for presheaves of sets in
> `Type (max (u + 1) v)`. For a geometric point `s` of `S` and a presheaf of sets `𝓕` on `S_et`, the
> map `𝓕_s̄ ⟶ (𝓕^#)_s̄` induced by `𝓕 ⟶ 𝓕^#` is an isomorphism.

```lean
theorem isIso_pointSmallEtale_presheafFiber_map_toSheafify'
    (F : S.Etaleᵒᵖ ⥤ Type (max (u + 1) v)) :
    IsIso ((pointSmallEtale s).presheafFiber.map (toSheafify (smallEtaleTopology S) F))
```

**`AlgebraicGeometry.Scheme.pointSmallEtale_sheafFiber_ab_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean#L94). The attribute's comment: “(3) the stalk functor on abelian sheaves is exact”.

> **The stalk functor on abelian sheaves is exact.** For a geometric point `s` of `S`, the stalk
> functor `Ab(S_et) ⥤ Ab`, `𝓕 ↦ 𝓕_s̄`, commutes with finite limits and finite colimits.

```lean
theorem pointSmallEtale_sheafFiber_ab_exact :
    PreservesFiniteLimits ((pointSmallEtale s).sheafFiber (A := AddCommGrpCat.{max u v})) ∧
      PreservesFiniteColimits ((pointSmallEtale s).sheafFiber (A := AddCommGrpCat.{max u v}))
```

**`AlgebraicGeometry.Scheme.pointSmallEtale_presheafFiber_type_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean#L105). The attribute's comment: “(4) the stalk functor on presheaves of sets is exact and commutes with colimits”.

> **The stalk functor on presheaves of sets is exact and commutes with colimits.** For a
> geometric point `s` of `S`, the stalk functor `PSh(S_et) ⥤ Sets`, `𝓕 ↦ 𝓕_s̄`, commutes with
> finite limits, with finite colimits, and with colimits of any size.

```lean
theorem pointSmallEtale_presheafFiber_type_exact :
    PreservesFiniteLimits ((pointSmallEtale s).presheafFiber (A := Type (max u v))) ∧
      PreservesFiniteColimits ((pointSmallEtale s).presheafFiber (A := Type (max u v))) ∧
      PreservesColimitsOfSize.{w₁, w₂}
        ((pointSmallEtale s).presheafFiber (A := Type (max u v)))
```

**`AlgebraicGeometry.Scheme.pointSmallEtale_sheafFiber_type_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PointSmallEtaleStalkExact.lean#L119). The attribute's comment: “(4) the stalk functor on sheaves of sets is exact and commutes with colimits”.

> **The stalk functor on sheaves of sets is exact and commutes with colimits.** For a geometric
> point `s` of `S`, the stalk functor `Sh(S_et) ⥤ Sets`, `𝓕 ↦ 𝓕_s̄`, commutes with finite limits,
> with finite colimits, and with colimits of any size.

```lean
theorem pointSmallEtale_sheafFiber_type_exact :
    PreservesFiniteLimits ((pointSmallEtale s).sheafFiber (A := Type (max u v))) ∧
      PreservesFiniteColimits ((pointSmallEtale s).sheafFiber (A := Type (max u v))) ∧
      PreservesColimitsOfSize.{w₁, w₂}
        ((pointSmallEtale s).sheafFiber (A := Type (max u v)))
```

## Tag 03PU, a theorem

[Tag 03PU](https://stacks.math.columbia.edu/tag/03PU) in the Stacks Project.

**`AlgebraicGeometry.isZero_of_forall_isZero_etaleStalk_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFaithfulnessModules.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFaithfulnessModules.lean#L131). The attribute's comment: “module coefficients, the vanishing case of the isomorphism criterion: a sheaf of modules whose geometric stalks all vanish is zero”.

> **Stacks 03PU for sheaves of modules, the vanishing case.** A sheaf of `Λ`-modules on the
> small étale site of `S` whose stalk at every geometric point of `S` vanishes is zero.
>
> The zero map from the zero sheaf is surjective on every geometric stalk, the target of each of
> those maps being a zero module, so it is locally surjective by Tag 03PU and therefore an
> epimorphism; an epimorphism out of a zero object forces the identity of its target to
> vanish.

```lean
public theorem isZero_of_forall_isZero_etaleStalk_module (S : Scheme.{u}) (hS : B.Contains S)
    (F : Sheaf (SmallEtale.topology B S hS) (ModuleCat.{u + 1} Λ))
    (h : ∀ t : GeometricPoint S, IsZero (etaleStalk B S hS t F.obj)) :
    IsZero F
```

**`AlgebraicGeometry.isIso_of_bijective_etaleStalkMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardBaseChange.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/FinitePushforwardBaseChange.lean#L202). The attribute's comment: “sheaves of sets, the isomorphism case”.

> A morphism of sheaves of sets on the small étale site of `X` which is bijective on the stalk
> at every geometric point of `X` is an isomorphism.

```lean
public theorem isIso_of_bijective_etaleStalkMap (α : F ⟶ G)
    (h : ∀ s : GeometricPoint X, Function.Bijective
      ((etaleStalkFunctor.{u, u + 1} B X hX s).map α)) :
    IsIso α
```

**`AlgebraicGeometry.GeometricPoint.mono_iff_forall_injective_stalkFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/StalksTestMaps.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/StalksTestMaps.lean#L147). The attribute's comment: “injectivity on stalks at geometric points”. References: SGA 4 VIII (3.6), “mono ⟺ inj on stalks”.

> **Stacks Project, Tag 03PU.** A map of sheaves of sets on the small étale site of a scheme
> is injective if and only if it is injective on the stalk at every geometric point.

```lean
theorem mono_iff_forall_injective_stalkFunctor (φ : F ⟶ G) :
    Mono φ ↔ ∀ s : GeometricPoint S, Function.Injective (s.stalkFunctor.map φ)
```

**`AlgebraicGeometry.GeometricPoint.epi_iff_forall_surjective_stalkFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/StalksTestMaps.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/StalksTestMaps.lean#L160). The attribute's comment: “surjectivity on stalks at geometric points”. References: SGA 4 VIII (3.6), “epi ⟺ surj on stalks”.

> **Stacks Project, Tag 03PU.** A map of sheaves of sets on the small étale site of a scheme
> is surjective if and only if it is surjective on the stalk at every geometric point.

```lean
theorem epi_iff_forall_surjective_stalkFunctor (φ : F ⟶ G) :
    Epi φ ↔ ∀ s : GeometricPoint S, Function.Surjective (s.stalkFunctor.map φ)
```

**`AlgebraicGeometry.isLocallySurjective_of_surjective_etaleStalkMapOfCoefficients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean#L106). The attribute's comment: “local surjectivity from surjectivity on geometric stalks, arbitrary coefficients”.

> **Stacks 03PU** for an arbitrary concrete coefficient category. A map of sheaves on the small
> étale site of `S` which is surjective on the stalk at every geometric point of `S` is locally
> surjective.
>
> A section over `V` is, near every point of `V`, the image of a section: its germ at the geometric
> point attached to that point is the image of a germ, germs are computed on étale neighbourhoods,
> and two sections with the same germ agree on an étale neighbourhood of the point.

```lean
public theorem isLocallySurjective_of_surjective_etaleStalkMapOfCoefficients
    {F G : Sheaf (SmallEtale.topology B S hS) A} (α : F ⟶ G)
    (h : ∀ s : GeometricPoint S, Function.Surjective
      ((etaleStalkPresheafFunctor B S hS s A).map α.hom)) :
    Presheaf.IsLocallySurjective (SmallEtale.topology B S hS) α.hom
```

**`AlgebraicGeometry.surjective_etaleStalkMap_of_isLocallySurjective_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean#L225). The attribute's comment: “surjectivity on geometric stalks, module coefficients”.

> **Stacks 03PU for sheaves of modules.** A locally surjective map of sheaves of `Λ`-modules on
> a small étale site is surjective on the stalk at every geometric point: the stalk is the fiber of
> the point of the site attached to the geometric point, and a point of a site turns local
> surjectivity into surjectivity.

```lean
public theorem surjective_etaleStalkMap_of_isLocallySurjective_module
    (S : Scheme.{u}) (hS : B.Contains S)
    {F G : Sheaf (SmallEtale.topology B S hS) (ModuleCat.{u + 1} Λ)} (α : F ⟶ G)
    [Presheaf.IsLocallySurjective (SmallEtale.topology B S hS) α.hom]
    (s : GeometricPoint S) :
    Function.Surjective
      ((etaleStalkPresheafFunctor B S hS s (ModuleCat.{u + 1} Λ)).map α.hom)
```

**`AlgebraicGeometry.isLocallySurjective_of_surjective_etaleStalkMap_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PullbackStalk/ModuleCoefficients.lean#L238). The attribute's comment: “local surjectivity from surjectivity on geometric stalks, module coefficients”.

> **Stacks 03PU for sheaves of modules.** A map of sheaves of `Λ`-modules on the small étale
> site of `S` which is surjective on the stalk at every geometric point of `S` is locally
> surjective.

```lean
public theorem isLocallySurjective_of_surjective_etaleStalkMap_module
    (S : Scheme.{u}) (hS : B.Contains S)
    {F G : Sheaf (SmallEtale.topology B S hS) (ModuleCat.{u + 1} Λ)} (α : F ⟶ G)
    (h : ∀ s : GeometricPoint S, Function.Surjective
      ((etaleStalkPresheafFunctor B S hS s (ModuleCat.{u + 1} Λ)).map α.hom)) :
    Presheaf.IsLocallySurjective (SmallEtale.topology B S hS) α.hom
```

**`AlgebraicGeometry.jointlyFaithful_etaleStalkSheafFiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkExactnessCriterion.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkExactnessCriterion.lean#L100). The attribute's comment: “the geometric stalks are jointly faithful on abelian étale sheaves”. References: SGA 4 VIII (3.7), “special case”.

> **Stacks 03PU.** The stalk functors at the geometric points of `S` are jointly faithful on
> abelian sheaves on the small étale site of `S`: two morphisms of sheaves inducing the same map on
> every stalk are equal.
>
> Two morphisms with the same germ at every geometric point agree, over each object of the site, on
> the sieve of arrows along which the two sections become equal; that sieve is covering because
> every point of the object carries a geometric point lifting to it, and a sheaf is separated for a
> covering sieve.

```lean
public theorem jointlyFaithful_etaleStalkSheafFiber :
    JointlyFaithful (fun s : GeometricPoint S =>
      (geometricPointSitePoint B S hS s).sheafFiber (A := AddCommGrpCat.{max (u + 1) v}))
```

**`AlgebraicGeometry.exact_iff_etaleStalk_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkExactnessCriterion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StalkExactnessCriterion.lean#L138). The attribute's comment: “exactness of abelian étale sheaves is checked on geometric stalks”.

> **Stacks 03PU.** A short complex of abelian sheaves on the small étale site of `S` is exact
> exactly when its short complex of stalks at every geometric point of `S` is exact.
>
> A stalk is a filtered colimit, so the stalk functors are exact and the condition is necessary;
> it is sufficient because the stalk functors are jointly faithful, so a sheaf whose stalks all
> vanish vanishes, applied to the homology of the complex.

```lean
public theorem exact_iff_etaleStalk_exact
    (T : ShortComplex (Sheaf (SmallEtale.topology B S hS) AddCommGrpCat.{max (u + 1) v})) :
    T.Exact ↔ ∀ s : GeometricPoint S,
      let Φ := sheafToPresheaf (SmallEtale.topology B S hS) AddCommGrpCat.{max (u + 1) v} ⋙
        etaleStalkPresheafFunctor B S hS s AddCommGrpCat.{max (u + 1) v}
      ∀ b : Φ.obj T.X₂,
        ((Φ.map T.g).hom b = 0 ↔ ∃ a : Φ.obj T.X₁, (Φ.map T.f).hom a = b)
```

**`AlgebraicGeometry.surjective_etaleStalkMap_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean#L268). The attribute's comment: “surjectivity on stalks at geometric points, abelian sheaves”. References: SGA 4 VIII (3.6), “epi ⇒ surj on stalks”.

> **Stacks 03PU.** A locally surjective morphism of abelian sheaves on a small étale site is
> surjective on the stalk at every geometric point: the stalk is the fiber of the point of the
> site attached to the geometric point, and a point of a site turns local surjectivity into
> surjectivity.

```lean
public theorem surjective_etaleStalkMap_of_isLocallySurjective
    (Y : Scheme.{u}) (hY : B.Contains Y)
    {F G : Sheaf (SmallEtale.topology B Y hY) AddCommGrpCat.{u + 1}} (α : F ⟶ G)
    [Presheaf.IsLocallySurjective (SmallEtale.topology B Y hY) α.hom]
    (s : GeometricPoint Y) :
    Function.Surjective
      ((etaleStalkPresheafFunctor B Y hY s AddCommGrpCat.{u + 1}).map α.hom)
```

## Tag 04HU, a lemma

[Tag 04HU](https://stacks.math.columbia.edu/tag/04HU) in the Stacks Project.

**`AlgebraicGeometry.exists_geometricPoint_fiber_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/SitePoints.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/SitePoints.lean#L582). The attribute's comment: “part (1)”. References: SGA 4 VIII (7.9), “essential surjectivity”.

> **Stacks 04HU, part (1).** Every point of the small étale site of `S` is given by a geometric
> point of `S`: its fibre functor is naturally isomorphic to the functor of lifts of that geometric
> point, which is the fibre functor of
> `AlgebraicGeometry.geometricPointSitePoint`.

```lean
public theorem exists_geometricPoint_fiber_iso
    (p : (SmallEtale.topology B S hS).Point.{u}) :
    ∃ s : GeometricPoint S, Nonempty (p.fiber ≅ geometricPointFiber B S hS s)
```

**`AlgebraicGeometry.exists_geometricPoint_inverseImage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/SitePoints.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/NeighborhoodsStalksPoints/SitePoints.lean#L703). The attribute's comment: “part (2)”. References: SGA 4 VIII (7.9), “essential surjectivity”.

> **Stacks 04HU, part (2).** Every point of the small étale topos of `S` has the geometric
> stalk functor of a geometric point of `S` as its inverse image: the stalk of a sheaf `F` at the
> point is the colimit of `F` over the category of étale neighbourhoods of that geometric point.
>
> The point of the topos is first reconstructed as a point of the site
> (`PointOfTopos.exists_sitePoint_fiber_eq`, Stacks 00YA (2)); that point of the site is then a
> geometric point by `AlgebraicGeometry.exists_geometricPoint_fiber_iso`, part (1), and the
> canonical comparison identifies the two inverse images
> (`PointOfTopos.isIso_sheafFiberComparison`).

```lean
public theorem exists_geometricPoint_inverseImage_iso
    (p : PointOfTopos.{u + 1} (SmallEtale.topology B S hS)) :
    ∃ s : GeometricPoint S,
      Nonempty (p.inverseImage ≅
        sheafToPresheaf (SmallEtale.topology B S hS) (Type (u + 1)) ⋙
          (Functor.whiskeringLeft _ _ _).obj
            (Functor.Elements.π (geometricPointFiber B S hS s)).op ⋙
          colim)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.29, Tag 03PN](https://stacks.math.columbia.edu/tag/03PN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
