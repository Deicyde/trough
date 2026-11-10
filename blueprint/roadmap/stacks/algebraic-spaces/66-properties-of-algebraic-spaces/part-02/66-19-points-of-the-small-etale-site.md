---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.geometricPointOfSpecHom, AlgebraicGeometry.Space.GeometricPoint, AlgebraicGeometry.Space.GeometricPoint.image, AlgebraicGeometry.Space.GeometricPoint.LiesOver, AlgebraicGeometry.Space.EtaleNeighborhood, AlgebraicGeometry.Space.EtaleNeighborhood.Hom, AlgebraicGeometry.Space.EtaleNeighborhood.exists_common_refinement, AlgebraicGeometry.Space.EtaleNeighborhood.exists_equalizing_refinement
statement: formalized
proof: formalized
---

# 66.19 Points of the small étale site

Section 66.19 of the Stacks Project, [Tag 04JU](https://stacks.math.columbia.edu/tag/04JU). 14 tags here are carried by 46 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0486, a definition

[Tag 0486](https://stacks.math.columbia.edu/tag/0486) in the Stacks Project.

**`AlgebraicGeometry.Space.geometricPointOfSpecHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointOfSpecHom.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointOfSpecHom.lean#L57). The attribute's comment: “part (1): a geometric point of a representable algebraic space”.

> For an object `U` of the big fppf site over `S`, an algebraically closed field `Ω` whose
> spectrum the site contains, a morphism `tb : Spec Ω ⟶ S` and a morphism of schemes
> `σ : Spec Ω ⟶ U` over `tb`, the geometric point of `yoneda.obj U` whose field is `Ω`, whose
> structure morphism to `S` is `tb` and whose section is `σ`.

```lean
def geometricPointOfSpecHom (U : BigFppfOver B S hS) {Ω : Type u} [Field Ω] [IsAlgClosed Ω]
    (hΩ : B.Contains (Spec (.of Ω))) (tb : Spec (.of Ω) ⟶ S)
    (σ : Spec (.of Ω) ⟶ (BigFppfOver.toScheme B S hS).obj U)
    (hσ : σ ≫ B.inclusion.map U.hom = tb) :
    GeometricPoint B S hS (yoneda.obj U)
```

**`AlgebraicGeometry.Space.GeometricPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean#L75). The attribute's comment: “part (1): geometric point”.

> A morphism from the spectrum of an algebraically closed field to a presheaf over a scheme.
> For an algebraic space this is a geometric point.

```lean
abbrev GeometricPoint (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Type (u + 1)
```

**`AlgebraicGeometry.Space.GeometricPoint.image`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean#L81). The attribute's comment: “part (2): image point”.

> The point of the algebraic space represented by a geometric point.

```lean
abbrev GeometricPoint.image {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (p : GeometricPoint B S hS F) :
    points B S hS F
```

**`AlgebraicGeometry.Space.GeometricPoint.LiesOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean#L87). The attribute's comment: “part (2): lying over a point”.

> A geometric point lies over its image point in the underlying point set.

```lean
abbrev GeometricPoint.LiesOver {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (p : GeometricPoint B S hS F)
    (x : points B S hS F) : Prop
```

## Tag 04JV, a definition

[Tag 04JV](https://stacks.math.columbia.edu/tag/04JV) in the Stacks Project.

**`AlgebraicGeometry.Space.EtaleNeighborhood`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean#L94). The attribute's comment: “part (1): étale neighborhoods”. References: SGA 4½ Arcata (2.3.1), “étale neighbourhood”.

> An étale neighbourhood of a geometric point of an algebraic space, with a chosen lift from
> the same field spectrum as the given geometric point.

```lean
structure EtaleNeighborhood (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hF : IsAlgebraicSpace B S hS F)
    (x : GeometricPoint B S hS F)
```

**`AlgebraicGeometry.Space.EtaleNeighborhood.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean#L120). The attribute's comment: “part (2): morphisms of étale neighborhoods”.

> A map of étale neighbourhoods over the fixed algebraic space which carries the chosen lift
> to the chosen lift.

```lean
structure Hom (U V : EtaleNeighborhood B S hS F hF x)
```

## Tag 04JW, a lemma

[Tag 04JW](https://stacks.math.columbia.edu/tag/04JW) in the Stacks Project.

**`AlgebraicGeometry.Space.EtaleNeighborhood.exists_common_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean#L182). The attribute's comment: “common\_refinement”.

> Two étale neighbourhoods of a geometric point have a common refinement.

```lean
theorem exists_common_refinement (U V : EtaleNeighborhood B S hS F hF x) :
    ∃ W : EtaleNeighborhood B S hS F hF x, Nonempty ((W ⟶ U) × (W ⟶ V))
```

**`AlgebraicGeometry.Space.EtaleNeighborhood.exists_equalizing_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean#L227). The attribute's comment: “equalizing\_refinement”.

> Two parallel morphisms of étale neighbourhoods of a geometric point are equalized by a
> further étale neighbourhood.

```lean
theorem exists_equalizing_refinement {U V : EtaleNeighborhood B S hS F hF x} (h₁ h₂ : U ⟶ V) :
    ∃ (W : EtaleNeighborhood B S hS F hF x) (h : W ⟶ U), h ≫ h₁ = h ≫ h₂
```

**`AlgebraicGeometry.Space.EtaleNeighborhood.exists_smallEtaleNeighborhood_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean#L318). The attribute's comment: “scheme\_refinement, in the small étale site”.

> Every étale neighbourhood of a geometric point is refined by one coming from the small étale
> site, i.e. by one in the image of `AlgebraicGeometry.Space.EtaleNeighborhood.ofSmallEtale`.

```lean
theorem exists_smallEtaleNeighborhood_refinement (U : EtaleNeighborhood B S hS F hF x) :
    ∃ V : SmallEtaleNeighborhood x, Nonempty ((ofSmallEtale hF x).obj V ⟶ U)
```

**`AlgebraicGeometry.Space.exists_scheme_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/GeometricPoints.lean#L167). The attribute's comment: “scheme\_refinement”.

> Every étale neighbourhood of a geometric point admits a refinement by a scheme.

```lean
theorem exists_scheme_refinement (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F)
    (x : GeometricPoint B S hS F)
    (U : EtaleNeighborhood B S hS F hF x) :
    ∃ (U' : EtaleNeighborhood B S hS F hF x),
      ∃ (_f : U' ⟶ U), U'.space.IsRepresentable
```

## Tag 05VN, a lemma

[Tag 05VN](https://stacks.math.columbia.edu/tag/05VN) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_geometricPoint_lift_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointEtaleLift.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPointEtaleLift.lean#L171).

> A geometric point lifts along an étale morphism of algebraic spaces to any
> specified point of the source above its image, without extending its field.

```lean
theorem exists_geometricPoint_lift_of_isEtale
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {U X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hU : IsAlgebraicSpace B S hS U)
    (hX : IsAlgebraicSpace B S hS X)
    (φ : U ⟶ X) (hφ : IsEtale B S hS φ)
    (xbar : GeometricPoint B S hS X)
    (u : points B S hS U)
    (hu : pointsMap B S hS U φ u = xbar.image) :
    ∃ ubar : GeometricPoint B S hS U,
      ubar.LiesOver u ∧
        FieldValuedPoint.map B S hS U φ ubar.val = xbar.val
```

## Tag 04JX, a lemma

[Tag 04JX](https://stacks.math.columbia.edu/tag/04JX) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_lift_to_etaleCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleNeighborhood.lean#L429).

> A covering of an étale neighbourhood `U` of a geometric point `x` of an algebraic space `X`,
> taken in the spaces-étale site of `X`, has a member to which `x` lifts; that member, with the
> lift, is again an étale neighbourhood of `x`, and the covering arrow is a morphism of étale
> neighbourhoods.

```lean
theorem exists_lift_to_etaleCovering (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (X : AlgebraicSpaces B S hS) (x : GeometricPoint B S hS X.1)
    (U : EtaleNeighborhood B S hS X.1 X.2 x)
    (E : PreZeroHypercover.{u + 1} (etaleSiteObjectOfNeighborhood B S hS X x U))
    (hE : SpacesEtale.IsCovering B S hS X
      ⟨etaleSiteObjectOfNeighborhood B S hS X x U, E⟩) :
    ∃ i : E.I₀,
      ∃ uiBar : ((SpacesEtale.toSpaces B S hS X).obj (E.X i)).1.obj
        (Opposite.op x.val.siteObject),
      ∃ huiBar : (((SpacesEtale.inclusion B S hS X).obj (E.X i)).hom.hom).app
          (Opposite.op x.val.siteObject) uiBar = x.val.value,
      ∃ φ : etaleNeighborhoodOfSitePoint B S hS X x (E.X i) uiBar huiBar ⟶ U,
        EtaleNeighborhood.Hom.hom φ =
          ((SpacesEtale.toSpaces B S hS X).map (E.f i)).hom
```

## Tag 04JY, a definition

[Tag 04JY](https://stacks.math.columbia.edu/tag/04JY) in the Stacks Project.

**`AlgebraicGeometry.Space.yonedaIdentityNeighborhood`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingFieldSpace.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingFieldSpace.lean#L84). The attribute's comment: “the identity chart of a representable algebraic space”.

> **A representable algebraic space is its own pointed étale chart.** The identity of
> `yoneda.obj X` is an étale chart, and it is a small étale neighbourhood of *every* geometric
> point of `yoneda.obj X`: the section defining the point is itself the required lift.

```lean
abbrev yonedaIdentityNeighborhood (X : BigFppfOver B S hS)
    (w : GeometricPoint B S hS (yoneda.obj X)) : SmallEtaleNeighborhood w
```

**`AlgebraicGeometry.Space.stalk`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean#L164). The attribute's comment: “category-valued stalk”.

> The stalk of a presheaf on the small étale site at a geometric point,
> formed as the colimit of its sections over the small étale neighbourhoods of that point.

```lean
noncomputable abbrev stalk {C : Type w} [Category.{v} C] (x : GeometricPoint B S hS F)
    (P : (SmallEtale B S hS F)ᵒᵖ ⥤ C)
    [HasColimit (SmallEtaleNeighborhood.sections (x := x) P)] : C
```

**`AlgebraicGeometry.Space.stalkFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean#L171). The attribute's comment: “stalk functor”.

> The stalk at a geometric point, as a functor of the presheaf.

```lean
noncomputable def stalkFunctor (C : Type w) [Category.{v} C] (x : GeometricPoint B S hS F)
    [HasColimitsOfShape (SmallEtaleNeighborhood x)ᵒᵖ C] :
    ((SmallEtale B S hS F)ᵒᵖ ⥤ C) ⥤ C
```

**`AlgebraicGeometry.Space.stalkSet`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean#L201). The attribute's comment: “set-valued stalk”.

> The set-valued stalk at a geometric point, formed as the quotient colimit
> `CategoryTheory.Functor.ColimitType`, with no smallness assumption on the neighbourhood
> category.

```lean
abbrev stalkSet (x : GeometricPoint B S hS F) (P : (SmallEtale B S hS F)ᵒᵖ ⥤ Type w) :
    Type _
```

**`AlgebraicGeometry.Space.stalkSetFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean#L230). The attribute's comment: “set-valued stalk functor”.

> The set-valued stalk at a geometric point, as a functor of the presheaf.

```lean
def stalkSetFunctor (x : GeometricPoint B S hS F) :
    ((SmallEtale B S hS F)ᵒᵖ ⥤ Type w) ⥤ Type (max (u + 1) w)
```

## Tag 04JZ, an equation

[Tag 04JZ](https://stacks.math.columbia.edu/tag/04JZ) in the Stacks Project.

**`AlgebraicGeometry.Space.stalkSpacesEtaleIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleStalk.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleStalk.lean#L185).

> **Stacks 04JZ.** The small-site stalk at a geometric point is the colimit of sections
> over all étale algebraic-space neighbourhoods of that point, naturally in the presheaf on the
> spaces-étale site.

```lean
noncomputable def stalkSpacesEtaleIso :
    ((Functor.whiskeringLeft (SmallEtale B S hS X.1)ᵒᵖ (SpacesEtale B S hS X)ᵒᵖ
        (Type w)).obj (comparisonFunctor B S hS X).op ⋙ stalkSetFunctor x) ≅
      spacesStalkSetFunctor x
```

## Tag 04K0, a lemma

[Tag 04K0](https://stacks.math.columbia.edu/tag/04K0) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleSitePoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSitePoint.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSitePoint.lean#L286). The attribute's comment: “the point of the site”.

> The point of the small étale site of an algebraic space determined by
> a geometric point of it: its fibre functor is the functor of lifts of the geometric point
> into the étale scheme charts.

```lean
noncomputable def etaleSitePoint (x : GeometricPoint B S hS F)
    (hF : IsAlgebraicSpace B S hS F) : (SmallEtale.topology B S hS F).Point.{u}
```

**`AlgebraicGeometry.Space.etaleSitePoint_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSitePoint.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSitePoint.lean#L296). The attribute's comment: “the fibre functor”.

> The fibre functor of the point of the small étale site determined by a geometric point is
> the geometric fibre functor.

```lean
theorem etaleSitePoint_fiber (x : GeometricPoint B S hS F)
    (hF : IsAlgebraicSpace B S hS F) :
    (etaleSitePoint B S hS F x hF).fiber = geometricFiber B S hS F x
```

**`AlgebraicGeometry.Space.etaleSitePointStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSitePoint.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleSitePoint.lean#L330). The attribute's comment: “the stalk comparison”.

> The stalk at the point of the small étale site determined by a geometric point is
> isomorphic to the geometric stalk, naturally in the presheaf.

```lean
noncomputable def etaleSitePointStalkIso (x : GeometricPoint B S hS F)
    (hF : IsAlgebraicSpace B S hS F) :
    (etaleSitePoint B S hS F x hF).presheafFiber (A := Type (u + 1)) ≅
      stalkSetFunctor x
```

## Tag 04K1, a lemma

[Tag 04K1](https://stacks.math.columbia.edu/tag/04K1) in the Stacks Project.

**`AlgebraicGeometry.Space.presheafAbelianStalk_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 897](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L897). The attribute's comment: “part (1): finite limits”.

> **Stacks 04K1, part (1).** The geometric stalk of a presheaf of abelian groups on the
> small étale site is left exact.

```lean
theorem presheafAbelianStalk_preservesFiniteLimits (x : GeometricPoint B S hS X) :
    PreservesFiniteLimits (stalkFunctor AddCommGrpCat.{max (u + 1) w} x)
```

**`AlgebraicGeometry.Space.presheafAbelianStalk_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 910](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L910). The attribute's comment: “part (1): finite colimits”.

> **Stacks 04K1, part (1).** The geometric stalk of a presheaf of abelian groups on the
> small étale site is right exact.

```lean
theorem presheafAbelianStalk_preservesFiniteColimits (x : GeometricPoint B S hS X) :
    PreservesFiniteColimits (stalkFunctor AddCommGrpCat.{max (u + 1) w} x)
```

**`AlgebraicGeometry.Space.stalkSetMap_toSheafify_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 926](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L926). The attribute's comment: “part (2): sheafification comparison”.

> **Stacks 04K1, part (2).** Sheafification does not change the geometric stalk of a
> presheaf of sets: the comparison induced by the unit of sheafification is an isomorphism.

```lean
theorem stalkSetMap_toSheafify_isIso (x : GeometricPoint B S hS X)
    (P : (SmallEtale B S hS X)ᵒᵖ ⥤ Type (max (u + 1) w)) :
    IsIso ((stalkSetFunctor x).map
      ((SmallEtale.topology B S hS X).toSheafify P))
```

**`AlgebraicGeometry.Space.sheafAbelianStalk_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 959](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L959). The attribute's comment: “part (3): finite limits”.

> **Stacks 04K1, part (3).** The geometric stalk of a sheaf of abelian groups on the small
> étale site is left exact.

```lean
theorem sheafAbelianStalk_preservesFiniteLimits (x : GeometricPoint B S hS X) :
    PreservesFiniteLimits
      (sheafToPresheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{max (u + 1) w} ⋙
        stalkFunctor AddCommGrpCat.{max (u + 1) w} x)
```

**`AlgebraicGeometry.Space.sheafAbelianStalk_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 975](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L975). The attribute's comment: “part (3): finite colimits”.

> **Stacks 04K1, part (3).** The geometric stalk of a sheaf of abelian groups on the small
> étale site is right exact.

```lean
theorem sheafAbelianStalk_preservesFiniteColimits (x : GeometricPoint B S hS X) :
    PreservesFiniteColimits
      (sheafToPresheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{max (u + 1) w} ⋙
        stalkFunctor AddCommGrpCat.{max (u + 1) w} x)
```

**`AlgebraicGeometry.Space.presheafSetStalk_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 997](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L997). The attribute's comment: “part (4): presheaf sets, finite limits”.

> **Stacks 04K1, part (4).** The geometric stalk of a presheaf of sets on the small étale
> site preserves finite limits.

```lean
theorem presheafSetStalk_preservesFiniteLimits (x : GeometricPoint B S hS X) :
    PreservesFiniteLimits
      (stalkSetFunctor x : ((SmallEtale B S hS X)ᵒᵖ ⥤ Type w) ⥤ Type (max (u + 1) w))
```

**`AlgebraicGeometry.Space.presheafSetStalk_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 1010](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L1010). The attribute's comment: “part (4): presheaf sets, finite colimits”.

> **Stacks 04K1, part (4).** The geometric stalk of a presheaf of sets on the small étale
> site preserves finite colimits.

```lean
theorem presheafSetStalk_preservesFiniteColimits (x : GeometricPoint B S hS X) :
    PreservesFiniteColimits
      (stalkSetFunctor x : ((SmallEtale B S hS X)ᵒᵖ ⥤ Type w) ⥤ Type (max (u + 1) w))
```

**`AlgebraicGeometry.Space.presheafSetStalk_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 1023](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L1023). The attribute's comment: “part (4): presheaf sets, colimits”.

> **Stacks 04K1, part (4).** The geometric stalk of a presheaf of sets on the small étale
> site commutes with arbitrary colimits of presheaves.

```lean
theorem presheafSetStalk_preservesColimits (x : GeometricPoint B S hS X) :
    PreservesColimitsOfSize.{w, w}
      (stalkSetFunctor x : ((SmallEtale B S hS X)ᵒᵖ ⥤ Type w) ⥤ Type (max (u + 1) w))
```

**`AlgebraicGeometry.Space.sheafSetStalk_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 1042](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L1042). The attribute's comment: “part (4): sheaves of sets, finite limits”.

> **Stacks 04K1, part (4).** The geometric stalk of a sheaf of sets on the small étale site
> preserves finite limits.

```lean
theorem sheafSetStalk_preservesFiniteLimits (x : GeometricPoint B S hS X) :
    PreservesFiniteLimits
      (sheafToPresheaf (SmallEtale.topology B S hS X) (Type w) ⋙ stalkSetFunctor x)
```

**`AlgebraicGeometry.Space.sheafSetStalk_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 1051](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L1051). The attribute's comment: “part (4): sheaves of sets, finite colimits”.

> **Stacks 04K1, part (4).** The geometric stalk of a sheaf of sets on the small étale site
> preserves finite colimits.

```lean
theorem sheafSetStalk_preservesFiniteColimits (x : GeometricPoint B S hS X) :
    PreservesFiniteColimits
      (sheafToPresheaf (SmallEtale.topology B S hS X) (Type (max (u + 1) w)) ⋙
        stalkSetFunctor x)
```

**`AlgebraicGeometry.Space.sheafSetStalk_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 1068](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L1068). The attribute's comment: “part (4): sheaves of sets, colimits”. References: SGA 4 VIII (3.5), “3.5 a)”.

> **Stacks 04K1, part (4).** The geometric stalk of a sheaf of sets on the small étale site
> commutes with arbitrary colimits of sheaves.

```lean
theorem sheafSetStalk_preservesColimits (x : GeometricPoint B S hS X) :
    PreservesColimitsOfSize.{max (u + 1) w, max (u + 1) w}
      (sheafToPresheaf (SmallEtale.topology B S hS X) (Type (max (u + 1) w)) ⋙
        stalkSetFunctor x)
```

## Tag 04K2, a lemma

[Tag 04K2](https://stacks.math.columbia.edu/tag/04K2) in the Stacks Project.

**`AlgebraicGeometry.Space.abelianPullback_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImage.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImage.lean#L73). The attribute's comment: “abelian\_pullback\_exact”.

> **Stacks 04K2.** Pullback of sheaves of abelian groups along a morphism of algebraic
> spaces is exact on the small étale sites.

```lean
theorem abelianPullback_exact :
    exactFunctor
      (Sheaf (SmallEtale.topology B S hS Y.1) AddCommGrpCat.{u + 1})
      (Sheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1})
      (abelianPullback B S hS f)
```

**`AlgebraicGeometry.Space.smallEtalePullbackRepresentableNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImage.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImage.lean#L88). The attribute's comment: “representable\_pullback”.

> **Stacks 04K2.** The inverse image of the small étale sheaf represented by an algebraic
> space `V` étale over `Y` is the sheaf represented by the cartesian base change `X ×_Y V`,
> naturally in `V`.
>
> An algebraic space étale over `Y` need not be a scheme, so the sheaf it represents on the
> small étale site is its sheafified Yoneda presheaf on the spaces-étale site, restricted along
> the comparison functor of Stacks 03G1.

```lean
noncomputable def smallEtalePullbackRepresentableNatIso :
    (yoneda ⋙ presheafToSheaf (SpacesEtale.topology B S hS Y) (Type (u + 1)) ⋙
      (comparisonFunctor B S hS Y).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B S hS Y.1) (SpacesEtale.topology B S hS Y) ⋙
      (smallToposMorphism B S hS f).inverseImage) ≅
    ((spacesBaseChange B S hS f).functor ⋙ yoneda ⋙
      presheafToSheaf (SpacesEtale.topology B S hS X) (Type (u + 1)) ⋙
      (comparisonFunctor B S hS X).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B S hS X.1) (SpacesEtale.topology B S hS X))
```

**`AlgebraicGeometry.Space.smallEtaleInverseImage_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImage.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImage.lean#L168). The attribute's comment: “sheaf\_pullback\_exact”.

> **Stacks 04K2.** Pullback of sheaves of sets along a morphism of algebraic spaces is exact
> on the small étale sites.

```lean
theorem smallEtaleInverseImage_exact :
    exactFunctor _ _ (smallToposMorphism B S hS f).inverseImage
```

**`AlgebraicGeometry.Space.smallEtaleInverseImageFiberIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageFiberType.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageFiberType.lean#L120). The attribute's comment: “part (4), for sheaves of sets at the universe of the structure rings”.

> The fibre at a geometric point `x` of `X` of the inverse image along the canonical morphism
> of small étale topoi of Stacks 03G8 of a sheaf of sets on the small étale site of `Y` is the
> fibre of that sheaf at the image point `f ∘ x`, naturally in the sheaf.
>
> It is the right-adjoint transpose of `AlgebraicGeometry.Space.smallEtaleSkyscraperIso`.

```lean
def smallEtaleInverseImageFiberIso :
    (etaleSitePoint B S hS Y.1 (geometricPointMap f.hom x) Y.2).sheafFiber (A := Type u) ≅
      (smallEtaleRingedToposHom B S hS f).toToposHom.inverseImage ⋙
        (etaleSitePoint B S hS X.1 x X.2).sheafFiber (A := Type u)
```

**`AlgebraicGeometry.Space.smallEtaleInverseImageStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageStalk.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageStalk.lean#L193). The attribute's comment: “stalk\_pullback”.

> **Stacks 04K2, part (4).** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` and a
> geometric point `x` of `X`, the stalk at `x` of the small étale inverse image of a sheaf on `Y`
> is the stalk of that sheaf at the image geometric point `f ∘ x`, naturally in the sheaf.

```lean
def smallEtaleInverseImageStalkIso (f : X ⟶ Y) (x : GeometricPoint B S hS X.1) :
    (smallToposMorphism B S hS f).inverseImage ⋙
        sheafToPresheaf (SmallEtale.topology B S hS X.1) (Type (u + 1)) ⋙ stalkSetFunctor x ≅
      sheafToPresheaf (SmallEtale.topology B S hS Y.1) (Type (u + 1)) ⋙
        stalkSetFunctor (geometricPointMap f.hom x)
```

**`AlgebraicGeometry.Space.smallEtaleAbelianInverseImageStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageStalkAbelian.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageStalkAbelian.lean#L256). The attribute's comment: “stalk\_pullback, abelian sheaves”.

> **Stacks 04K2, part (4), for abelian sheaves.** For a morphism `f : X ⟶ Y` of algebraic
> spaces over `S` with representable underlying morphism and a geometric point `x` of `X`, the
> stalk at `x` of the inverse image of an abelian sheaf on the small étale site of `Y` is the
> stalk of that sheaf at the image geometric point `f ∘ x`, naturally in the sheaf.

```lean
def smallEtaleAbelianInverseImageStalkIso (x : GeometricPoint B S hS X.1) :
    letI := isContinuous_smallBaseChange B S hS f hf
    (smallBaseChange B S hS f hf).sheafPullback AddCommGrpCat.{u + 1}
          (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1) ⋙
        sheafToPresheaf (SmallEtale.topology B S hS X.1) AddCommGrpCat.{u + 1} ⋙
          stalkFunctor AddCommGrpCat.{u + 1} x ≅
      sheafToPresheaf (SmallEtale.topology B S hS Y.1) AddCommGrpCat.{u + 1} ⋙
        stalkFunctor AddCommGrpCat.{u + 1} (geometricPointMap f.hom x)
```

**`AlgebraicGeometry.Space.preservesFiniteLimits_smallEtaleAbelianInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageStalkAbelian.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleInverseImageStalkAbelian.lean#L359). The attribute's comment: “part (1): finite limits”.

> **Stacks 04K2, part (1).** The inverse image of abelian sheaves along a morphism of
> algebraic spaces with representable underlying morphism is left exact.
>
> Base change of scheme charts is not representably flat, for want of a terminal object on the
> small étale site; left exactness is instead inherited from base change of étale algebraic
> spaces through the equivalences of Stacks 03G1.

```lean
theorem preservesFiniteLimits_smallEtaleAbelianInverseImage :
    letI := isContinuous_smallBaseChange B S hS f hf
    PreservesFiniteLimits ((smallBaseChange B S hS f hf).sheafPullback AddCommGrpCat.{u + 1}
      (SmallEtale.topology B S hS Y.1) (SmallEtale.topology B S hS X.1))
```

## Tag 04K3, a remark

[Tag 04K3](https://stacks.math.columbia.edu/tag/04K3) in the Stacks Project.

**`AlgebraicGeometry.Space.globalSections_isEquivalence_of_geometricPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkAsPullback.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkAsPullback.lean#L199). The attribute's comment: “equivalence by global sections”. References: SGA 4½ Arcata (2.4.4), “sep. closed field, G=1”.

> Global sections is an equivalence from sheaves of sets on the small étale site of the
> algebraic space represented by the field spectrum of a geometric point onto sets.

```lean
theorem globalSections_isEquivalence_of_geometricPoint (x : GeometricPoint B S hS F) :
    (Sheaf.Γ (SmallEtale.topology B S hS (yoneda.obj x.val.siteObject))
      (Type (u + 1))).IsEquivalence
```

**`AlgebraicGeometry.Space.smallEtaleStalkIsoPullbackGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkAsPullback.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkAsPullback.lean#L241). The attribute's comment: “the stalk as global sections of the pullback”.

> The stalk functor at a geometric point `x` of an algebraic space `X` is the inverse image
> along `x` — viewed as a morphism of algebraic spaces from the space represented by its field
> spectrum, hence as a morphism of small étale topoi — followed by global sections on the source.

```lean
def smallEtaleStalkIsoPullbackGlobalSections (x : GeometricPoint B S hS X.obj) :
    sheafToPresheaf (SmallEtale.topology B S hS X.obj) (Type (u + 1)) ⋙ stalkSetFunctor x ≅
      (smallToposMorphism B S hS
            (ObjectProperty.homMk (fieldMorphism B S hS X.obj x.val) :
              (⟨yoneda.obj x.val.siteObject,
                  isAlgebraicSpace_yoneda B S hS x.val.siteObject⟩ :
                AlgebraicSpaces B S hS) ⟶ X)).inverseImage ⋙
        Sheaf.Γ (SmallEtale.topology B S hS (yoneda.obj x.val.siteObject))
          (Type (u + 1))
```

## Tag 04K4, a remark

[Tag 04K4](https://stacks.math.columbia.edu/tag/04K4) in the Stacks Project.

**`AlgebraicGeometry.Space.stalkFunctor_iso_of_liesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/StalkIndependenceOfGeometricPoint.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/StalkIndependenceOfGeometricPoint.lean#L483).

> **Stacks 04K4.** The stalk functors on the small étale site at two geometric points
> lying over the same point of the algebraic space are isomorphic, naturally in the presheaf.
> The isomorphism is not canonical: the two points are compared through a common dominating
> geometric point.

```lean
theorem stalkFunctor_iso_of_liesOver (hF : IsAlgebraicSpace B S hS F) (C : Type w)
    [Category.{v} C] {x : points B S hS F} (p q : GeometricPoint B S hS F)
    [HasColimitsOfShape (SmallEtaleNeighborhood p)ᵒᵖ C]
    [HasColimitsOfShape (SmallEtaleNeighborhood q)ᵒᵖ C]
    (hp : p.LiesOver x) (hq : q.LiesOver x) :
    Nonempty (stalkFunctor C p ≅ stalkFunctor C q)
```

## Tag 04K5, a theorem

[Tag 04K5](https://stacks.math.columbia.edu/tag/04K5) in the Stacks Project.

**`AlgebraicGeometry.Space.injective_iff_stalkSetMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L502). The attribute's comment: “injectivity”. References: SGA 4 VIII (3.6), “injectivity clause”.

> **Stacks 04K5.** A map of sheaves of sets on the small étale site of an algebraic space
> is injective on sections over every étale chart exactly when it is injective on every
> geometric stalk.

```lean
theorem injective_iff_stalkSetMap_injective
    {F G : Sheaf (SmallEtale.topology B S hS X) (Type w)} (a : F ⟶ G) :
    (∀ U : SmallEtale B S hS X, Function.Injective (a.hom.app (Opposite.op U))) ↔
      ∀ x : GeometricPoint B S hS X, Function.Injective (stalkSetMap x a.hom)
```

**`AlgebraicGeometry.Space.surjective_iff_stalkSetMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L541). The attribute's comment: “surjectivity”. References: SGA 4 VIII (3.6), “surjectivity clause”.

> **Stacks 04K5.** A map of sheaves of sets on the small étale site of an algebraic space
> is locally surjective exactly when it is surjective on every geometric stalk.

```lean
theorem surjective_iff_stalkSetMap_surjective
    {F G : Sheaf (SmallEtale.topology B S hS X) (Type w)} (a : F ⟶ G) :
    Sheaf.IsLocallySurjective a ↔
      ∀ x : GeometricPoint B S hS X, Function.Surjective (stalkSetMap x a.hom)
```

**`AlgebraicGeometry.Space.exact_iff_stalk_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleStalkExactness.lean#L689). The attribute's comment: “exactness”.

> **Stacks 04K5.** A short complex of sheaves of abelian groups on the small étale site of
> an algebraic space is exact exactly when its sequence of geometric stalks is exact at every
> geometric point.

```lean
theorem exact_iff_stalk_exact
    (T : ShortComplex (Sheaf (SmallEtale.topology B S hS X)
      AddCommGrpCat.{max (u + 1) w})) :
    T.Exact ↔ ∀ x : GeometricPoint B S hS X,
      let Φ := sheafToPresheaf (SmallEtale.topology B S hS X)
        AddCommGrpCat.{max (u + 1) w} ⋙ stalkFunctor AddCommGrpCat.{max (u + 1) w} x
      ∀ b : Φ.obj T.X₂,
        ((Φ.map T.g).hom b = 0 ↔ ∃ a : Φ.obj T.X₁, (Φ.map T.f).hom a = b)
```

## Tag 04K6, a lemma

[Tag 04K6](https://stacks.math.columbia.edu/tag/04K6) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_geometricPoint_stalkFunctor_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsOfSmallEtaleTopos.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsOfSmallEtaleTopos.lean#L559). References: SGA 4 VIII (7.9), “essential surjectivity”.

> **Stacks 04K6.** Every point of the small étale topos of an algebraic space is
> represented, at the level of stalk functors, by a geometric point of the space.

```lean
theorem exists_geometricPoint_stalkFunctor_iso (hF : IsAlgebraicSpace B S hS F)
    (p : PointOfTopos.{u + 1} (SmallEtale.topology B S hS F)) :
    ∃ x : GeometricPoint B S hS F,
      Nonempty (p.inverseImage ≅
        sheafToPresheaf (SmallEtale.topology B S hS F) (Type (u + 1)) ⋙
          stalkSetFunctor x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.19, Tag 04JU](https://stacks.math.columbia.edu/tag/04JU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
