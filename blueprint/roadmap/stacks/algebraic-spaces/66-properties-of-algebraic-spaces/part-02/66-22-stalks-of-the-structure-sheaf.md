---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isHenselization_chartLocalRingToEtaleLocalRing, AlgebraicGeometry.Space.exists_algebra_isHenselization_etaleLocalRing_chart, AlgebraicGeometry.Space.exists_algebra_isHenselization_etaleLocalRing_elementary, AlgebraicGeometry.Space.etaleLocalRingEquivChart, AlgebraicGeometry.Space.strictHenselizationEquivEtaleLocalRing, AlgebraicGeometry.Space.strictHenselizationEquivEtaleLocalRing_germ, AlgebraicGeometry.Space.etaleLocalRingChartIso, AlgebraicGeometry.Space.etaleLocalRing
statement: formalized
proof: formalized
---

# 66.22 Stalks of the structure sheaf

Section 66.22 of the Stacks Project, [Tag 04KE](https://stacks.math.columbia.edu/tag/04KE). 6 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04KF, a lemma

[Tag 04KF](https://stacks.math.columbia.edu/tag/04KF) in the Stacks Project.

**`AlgebraicGeometry.Space.isHenselization_chartLocalRingToEtaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingChartHenselization.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingChartHenselization.lean#L166). The attribute's comment: “the étale local ring is a strict henselization of a neighborhood stalk along the canonical map of Stacks 05VP”. References: SGA 4½ Arcata (2.3.1), “partial, special case”.

> **Stacks 04KF, with the structure map named.** The étale local ring of an algebraic space at
> a geometric point `x̄` is a strict henselization of the local ring `𝒪_{U, u}` of a scheme chart
> at the point under the chosen lift, *along the canonical map of Stacks 05VP*
> `AlgebraicGeometry.Space.chartLocalRingToEtaleLocalRing`, with the separable closure of the
> residue field of `𝒪_{U, u}` inside the residue field of the geometric point as the residue
> extension.
>
> This is the form `AlgebraicGeometry.Space.exists_algebra_isHenselization_etaleLocalRing_chart`
> is proved from: there the algebra structure is produced existentially and an arbitrary chosen
> separable closure is matched to this one by uniqueness of separable closures, which is all the
> residue extension is used for. Naming the structure map is what lets a statement about
> `𝒪_{U, u} → 𝒪_{X, x̄}` — flatness, locality, lengths, orders of vanishing — be read off the
> henselization.

```lean
theorem isHenselization_chartLocalRingToEtaleLocalRing {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) :
    @IsHenselization ↥(chartLocalRing B S hS X V) _ _
      (separableClosure (ResidueField ↥(chartLocalRing B S hS X V))
        (chartGeometricPoint V).residueField) _ _
      (etaleLocalRing B S hS X x : Type (u + 1)) _
      (isLocalRing_etaleLocalRing B S hS X hX x)
      (chartLocalRingToEtaleLocalRing B S hS X hX V).toAlgebra
```

**`AlgebraicGeometry.Space.exists_algebra_isHenselization_etaleLocalRing_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingChartHenselization.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingChartHenselization.lean#L187). The attribute's comment: “the étale local ring is a strict henselization of a neighborhood stalk”. References: SGA 4½ Arcata (2.3.1), “special case”.

> **Stacks 04KF.** The étale local ring of an algebraic space at a geometric point is a strict
> henselization of the local ring of a scheme chart at the point under the chosen lift, for every
> chosen separable algebraic closure of the residue field of that local ring. The algebra
> structure is the canonical map of Stacks 05VP.

```lean
theorem exists_algebra_isHenselization_etaleLocalRing_chart {x : GeometricPoint B S hS X}
    (V : SmallEtaleNeighborhood x) (p : chartScheme V.chart)
    (hp : chartPoint B S hS X V = p)
    (κsep : Type u) [Field κsep]
    [Algebra (ResidueField ((chartScheme V.chart).presheaf.stalk p : Type u)) κsep]
    [IsSepClosure (ResidueField ((chartScheme V.chart).presheaf.stalk p : Type u)) κsep] :
    letI : IsLocalRing (etaleLocalRing B S hS X x : Type (u + 1)) :=
      isLocalRing_etaleLocalRing B S hS X hX x
    ∃ alg : Algebra ((chartScheme V.chart).presheaf.stalk p : Type u)
        (etaleLocalRing B S hS X x : Type (u + 1)),
      @IsHenselization ((chartScheme V.chart).presheaf.stalk p : Type u) _ _ κsep _ _
        (etaleLocalRing B S hS X x : Type (u + 1)) _
        (isLocalRing_etaleLocalRing B S hS X hX x) alg
```

**`AlgebraicGeometry.Space.exists_algebra_isHenselization_etaleLocalRing_elementary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingChartHenselization.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleLocalRingChartHenselization.lean#L261). The attribute's comment: “the étale local ring is a strict henselization of an elementary neighborhood stalk”.

> **Stacks 04KF.** The étale local ring of an algebraic space at a geometric point `x̄` is a
> strict henselization of the local ring of an elementary étale neighborhood of the point below
> `x̄`, at its distinguished point, for every chosen separable algebraic closure of the residue
> field of that local ring.

```lean
theorem exists_algebra_isHenselization_etaleLocalRing_elementary (hxbar : xbar.LiesOver x)
    (κsep : Type u) [Field κsep]
    [instAlg : Algebra (ResidueField (U.scheme.left.1.presheaf.stalk U.point : Type u)) κsep]
    [instSep : IsSepClosure (ResidueField (U.scheme.left.1.presheaf.stalk U.point : Type u))
      κsep] :
    letI : IsLocalRing (etaleLocalRing B S hS X xbar : Type (u + 1)) :=
      isLocalRing_etaleLocalRing B S hS X hX xbar
    ∃ alg : Algebra (U.scheme.left.1.presheaf.stalk U.point : Type u)
        (etaleLocalRing B S hS X xbar : Type (u + 1)),
      @IsHenselization (U.scheme.left.1.presheaf.stalk U.point : Type u) _ _ κsep _ _
        (etaleLocalRing B S hS X xbar : Type (u + 1)) _
        (isLocalRing_etaleLocalRing B S hS X hX xbar) alg
```

**`AlgebraicGeometry.Space.etaleLocalRingEquivChart`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingChart.lean, line 603](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingChart.lean#L603). The attribute's comment: “identification of the two étale stalks”.

> The stalk of the structure sheaf of an algebraic space is canonically
> the étale local ring of a scheme étale neighborhood. The comparison sends
> ordinary chart germs and all common pointed étale-refinement germs to their
> scheme-side germs.

```lean
noncomputable def etaleLocalRingEquivChart
    (hF : IsAlgebraicSpace B S hS F)
    (V : SmallEtaleNeighborhood x)
    (E : BigEtaleSite.{u}) (hV : E.Contains (neighborhoodChartScheme V)) :
    { e : etaleLocalRing B S hS F x ≃+*
        _root_.AlgebraicGeometry.etaleLocalRing E (neighborhoodChartScheme V) hV
          (chartGeometricPoint V) //
      (∀ a : Γ(neighborhoodChartScheme V, ⊤),
        e (etaleLocalRingGerm B S hS F x (Opposite.op V) a) =
          structureSheafStalkFromLocalRing E (neighborhoodChartScheme V) hV
            (chartGeometricPoint V)
            ((neighborhoodChartScheme V).presheaf.germ ⊤
              ((chartGeometricPoint V).hom
                (closedPoint (chartGeometricPoint V).residueField)) trivial a)) ∧
      (∀ (W : SmallEtaleNeighborhood x) (f : W ⟶ V)
          (U : (geometricPointFiber E (neighborhoodChartScheme V) hV
            (chartGeometricPoint V)).Elementsᵒᵖ)
          (a : Γ(neighborhoodChartScheme W, ⊤))
          (hs : neighborhoodChartScheme W =
            (_root_.AlgebraicGeometry.SmallEtale.toScheme E
              (neighborhoodChartScheme V) hV).obj U.unop.1)
          (_hp : HEq (chartGeometricPoint W).hom U.unop.2.1)
          (_hf : HEq (neighborhoodChartMap f)
            (E.inclusion.map U.unop.1.obj.hom)),
        e (etaleLocalRingGerm B S hS F x (Opposite.op W) a) =
          (colimit.ι
            ((Functor.Elements.π
              (geometricPointFiber E (neighborhoodChartScheme V) hV
                (chartGeometricPoint V))).op ⋙
              (_root_.AlgebraicGeometry.SmallEtale.structureSheaf E
                (neighborhoodChartScheme V) hV).obj)
            U).hom (show Γ((_root_.AlgebraicGeometry.SmallEtale.toScheme E
              (neighborhoodChartScheme V) hV).obj U.unop.1, ⊤) from hs ▸ a)) }
```

**`AlgebraicGeometry.Space.strictHenselizationEquivEtaleLocalRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingChart.lean, line 641](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingChart.lean#L641). The attribute's comment: “strict-henselization identification”.

> The étale local ring of the algebraic space is the strict henselization
> of the local ring of a scheme étale neighborhood at the selected point.

```lean
noncomputable def strictHenselizationEquivEtaleLocalRing
    (hF : IsAlgebraicSpace B S hS F)
    (V : SmallEtaleNeighborhood x)
    (E : BigEtaleSite.{u}) (hV : E.Contains (neighborhoodChartScheme V))
    (T : IsLocalRing.HenselizationTower
      ((neighborhoodChartScheme V).presheaf.stalk
        ((chartGeometricPoint V).hom
          (closedPoint (chartGeometricPoint V).residueField)))
      (separableClosure (ResidueField
        ((neighborhoodChartScheme V).presheaf.stalk
          ((chartGeometricPoint V).hom
            (closedPoint (chartGeometricPoint V).residueField))))
        (chartGeometricPoint V).residueField)) :
    T.strictHenselization ≃+* etaleLocalRing B S hS F x
```

**`AlgebraicGeometry.Space.strictHenselizationEquivEtaleLocalRing_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingChart.lean, line 662](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingChart.lean#L662). The attribute's comment: “compatibility with chart germs”.

> The strict-henselization comparison sends the ordinary germ of a chart
> section to its germ in the algebraic-space structure sheaf.

```lean
theorem strictHenselizationEquivEtaleLocalRing_germ
    (hF : IsAlgebraicSpace B S hS F)
    (V : SmallEtaleNeighborhood x)
    (E : BigEtaleSite.{u}) (hV : E.Contains (neighborhoodChartScheme V))
    (T : IsLocalRing.HenselizationTower
      ((neighborhoodChartScheme V).presheaf.stalk
        ((chartGeometricPoint V).hom
          (closedPoint (chartGeometricPoint V).residueField)))
      (separableClosure (ResidueField
        ((neighborhoodChartScheme V).presheaf.stalk
          ((chartGeometricPoint V).hom
            (closedPoint (chartGeometricPoint V).residueField))))
        (chartGeometricPoint V).residueField))
    (a : Γ(neighborhoodChartScheme V, ⊤)) :
    (strictHenselizationEquivEtaleLocalRing hF V E hV T)
      (algebraMap _ T.strictHenselization
        ((neighborhoodChartScheme V).presheaf.germ ⊤
          ((chartGeometricPoint V).hom
            (closedPoint (chartGeometricPoint V).residueField)) trivial a)) =
      etaleLocalRingGerm B S hS F x (Opposite.op V) a
```

**`AlgebraicGeometry.Space.etaleLocalRingChartIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingEtaleInvariance.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EtaleLocalRingEtaleInvariance.lean#L305). The attribute's comment: “O\_\{X, xbar} = O\_\{U, ubar}”.

> **Stacks 04KF, first equality.** Let `X` be an algebraic space over `S`, let `x̄` be a
> geometric point of `X` and let `(U, ū)` be an étale neighbourhood of `x̄` with `U` a scheme.
> Then the étale local ring of `U` at `ū` is the étale local ring of `X` at `x̄`.
>
> Only the first of the two equalities of Stacks 04KF is proved here.  The second,
> `𝒪_{U, ū} = 𝒪_{U, u}^{sh}`, is Étale Cohomology, Lemma 04HX, which is not in the library.

```lean
noncomputable def etaleLocalRingChartIso {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (x : GeometricPoint B S hS F)
    (N : SmallEtaleNeighborhood x) :
    etaleLocalRing B S hS (yoneda.obj ((SmallEtale.toOver B S hS F).obj N.chart))
        (chartPresheafGeometricPoint B S hS x N) ≅ etaleLocalRing B S hS F x
```

## Tag 04KG, a definition

[Tag 04KG](https://stacks.math.columbia.edu/tag/04KG) in the Stacks Project.

**`AlgebraicGeometry.Space.etaleLocalRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean#L387). The attribute's comment: “étale local ring”.

> The *étale local ring* of an algebraic space at a geometric point: the
> stalk of the structure sheaf on the small étale site, i.e. the ring of germs at that point of
> regular functions on étale neighbourhoods.

```lean
noncomputable abbrev etaleLocalRing (x : GeometricPoint B S hS F) : CommRingCat.{u + 1}
```

**`AlgebraicGeometry.Space.strictHenselization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean, line 402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GeometricPoints.lean#L402). The attribute's comment: “strict henselization”. References: SGA 4½ Arcata (5.1.1).

> The *strict henselization* of an algebraic space at a geometric point is
> the spectrum of its étale local ring.

```lean
noncomputable abbrev strictHenselization (x : GeometricPoint B S hS F) : Scheme.{u + 1}
```

## Tag 04KH, a lemma

[Tag 04KH](https://stacks.math.columbia.edu/tag/04KH) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtaleRingedSite_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleLocallyRinged.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleLocallyRinged.lean#L135).

> **Stacks Project, Tag 04KH.** The small étale site of an algebraic space, endowed with its
> structure sheaf, is a locally ringed site.

```lean
theorem smallEtaleRingedSite_isLocallyRinged (hF : IsAlgebraicSpace B S hS F) :
    RingedSite.IsLocallyRinged (smallEtaleRingedSite B S hS F hF)
```

## Tag 04N9, a lemma

[Tag 04N9](https://stacks.math.columbia.edu/tag/04N9) in the Stacks Project.

**`AlgebraicGeometry.Space.localRingDimension_eq_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocalRingGeometricStalk.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocalRingGeometricStalk.lean#L167).

> **Stacks 04N9.** For a point `x` of an algebraic space and `d` in `ℕ∞`, the dimension of
> the local ring of the space at `x` is `d` exactly when the stalk at some geometric point
> above `x` has Krull dimension `d`, and exactly when the stalk at every geometric point above
> `x` does.

```lean
theorem localRingDimension_eq_tfae (hF : IsAlgebraicSpace B S hS F)
    (x : points B S hS F) (d : ℕ∞) :
    List.TFAE
      [localRingDimension B S hS x = d,
        ∃ xbar : GeometricPoint B S hS F, xbar.LiesOver x ∧
          ringKrullDim (etaleLocalRing B S hS F xbar) = (d : WithBot ℕ∞),
        ∀ xbar : GeometricPoint B S hS F, xbar.LiesOver x →
          ringKrullDim (etaleLocalRing B S hS F xbar) = (d : WithBot ℕ∞)]
```

## Tag 0A4H, a lemma

[Tag 0A4H](https://stacks.math.columbia.edu/tag/0A4H) in the Stacks Project.

**`AlgebraicGeometry.Space.dimensionAtPoint_eq_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionEtaleInvariance.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionEtaleInvariance.lean#L54). The attribute's comment: “dimension\_at\_point”.

> **Stacks 0A4H.** An étale morphism of algebraic spaces preserves the dimension at a
> point.

```lean
theorem dimensionAtPoint_eq_of_isEtale (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsEtale B S hS f)
    (x : points B S hS X) :
    dimensionAtPoint B S hS X hX x =
      dimensionAtPoint B S hS Y hY (pointsMap B S hS X f x)
```

**`AlgebraicGeometry.Space.localRingDimension_pointsMap_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionEtaleInvariance.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionEtaleInvariance.lean#L68). The attribute's comment: “dimension\_local\_ring”.

> **Stacks 0A4H.** An étale morphism of algebraic spaces preserves the dimension of the
> local ring at a point.

```lean
theorem localRingDimension_pointsMap_of_etale (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsEtale B S hS f)
    (x : points B S hS X) :
    localRingDimension B S hS (pointsMap B S hS X f x) = localRingDimension B S hS x
```

**`AlgebraicGeometry.Space.dimension_eq_of_isEtale_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionEtaleInvariance.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionEtaleInvariance.lean#L81). The attribute's comment: “dimension\_surjective”.

> **Stacks 0A4H.** A surjective étale morphism of algebraic spaces preserves the
> dimension.

```lean
theorem dimension_eq_of_isEtale_of_isSurjective (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsEtale B S hS f)
    (hfs : IsSurjective B S hS f) :
    dimension B S hS X hX = dimension B S hS Y hY
```

## Tag 0E01, a lemma

[Tag 0E01](https://stacks.math.columbia.edu/tag/0E01) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_localRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LocalRingGeometricStalk.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/LocalRingGeometricStalk.lean#L192).

> **Stacks 0E01.** For a point `x` of an algebraic space, the local ring of the space at
> `x` is reduced exactly when the stalk at some geometric point above `x` is reduced, and
> exactly when the stalk at every geometric point above `x` is reduced.

```lean
theorem isReduced_localRing_tfae (hF : IsAlgebraicSpace B S hS F) (x : points B S hS F) :
    List.TFAE
      [HasLocalRingPropertyAtPoint B S hS F hF x
          (fun (R : Type u) ↦ fun [CommRing R] ↦ _root_.IsReduced R)
          isReduced_localization_etale_invariant,
        ∃ xbar : GeometricPoint B S hS F, xbar.LiesOver x ∧
          _root_.IsReduced (etaleLocalRing B S hS F xbar),
        ∀ xbar : GeometricPoint B S hS F, xbar.LiesOver x →
          _root_.IsReduced (etaleLocalRing B S hS F xbar)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.22, Tag 04KE](https://stacks.math.columbia.edu/tag/04KE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
