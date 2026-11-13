---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.blowUpAlong', AlgebraicGeometry.Space.blowUpAlongHom', AlgebraicGeometry.Space.exceptionalDivisor', AlgebraicGeometry.Space.blowUpAlong, AlgebraicGeometry.Space.blowUpAlongHom, AlgebraicGeometry.Space.exceptionalDivisor, AlgebraicGeometry.Space.exists_iso_proj_reesGrading_affineChart, AlgebraicGeometry.Space.exists_iSup_opensRange_specAffineBlowupι_affineChart
statement: formalized
proof: formalized
---

# 71.17 Blowing up

Section 71.17 of the Stacks Project, [Tag 085P](https://stacks.math.columbia.edu/tag/085P). 12 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 085Q, a definition

[Tag 085Q](https://stacks.math.columbia.edu/tag/085Q) in the Stacks Project.

**`AlgebraicGeometry.Space.blowUpAlong'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupEquivalenceRelationClosed.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupEquivalenceRelationClosed.lean#L78). The attribute's comment: “the blowup of X along Z as the relative Proj of the Rees algebra, the same object as blowUpAlong with the descent datum's equivalence-relation field discharged rather than assumed; the three B.Contains side conditions on the relative Projs remain”.

> **Stacks 085Q.** The blowing up of an algebraic space `X` along a closed subspace `Z ⊆ X`:
> the relative Proj `Proj_X(⨁_{n ≥ 0} 𝓘_Zⁿ)` of the Rees algebra of the defining ideal sheaf of
> `Z`, as an algebraic space over `S`.
>
> This is `AlgebraicGeometry.Space.blowUpAlong` with its equivalence-relation parameter supplied by
> `AlgebraicGeometry.Space.isEquivalenceRelation_post_reesProj` rather than assumed.

```lean
def blowUpAlong' : AlgebraicSpaces B S hS
```

**`AlgebraicGeometry.Space.blowUpAlongHom'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupEquivalenceRelationClosed.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupEquivalenceRelationClosed.lean#L89). The attribute's comment: “the morphism b of the blowup, with the descent datum's equivalence-relation field discharged rather than assumed; the three B.Contains side conditions on the relative Projs remain”.

> **Stacks 085Q.** The blowing up `b : Proj_X(⨁_{n ≥ 0} 𝓘_Zⁿ) ⟶ X` of an algebraic space `X`
> along a closed subspace `Z ⊆ X`, as a morphism of algebraic spaces over `S`, with the
> equivalence-relation field of the descent datum discharged.

```lean
def blowUpAlongHom' : blowUpAlong' Z P hcU hcR hcRR ⟶ X
```

**`AlgebraicGeometry.Space.exceptionalDivisor'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupEquivalenceRelationClosed.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupEquivalenceRelationClosed.lean#L100). The attribute's comment: “the exceptional divisor b⁻¹(Z) of the blowup and the centre Z, with the descent datum's equivalence-relation field discharged rather than assumed; the three B.Contains side conditions on the relative Projs remain”.

> **Stacks 085Q.** The exceptional divisor `b⁻¹(Z)` of the blowing up of `X` along `Z`: the
> inverse image of the centre along the structure morphism of the blowup, as a closed subspace of
> the blowup, with the equivalence-relation field of the descent datum discharged.

```lean
def exceptionalDivisor' : ClosedSubspaces B S hS (blowUpAlong' Z P hcU hcR hcRR).obj
```

**`AlgebraicGeometry.Space.blowUpAlong`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupRelativeProj.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupRelativeProj.lean#L439). The attribute's comment: “the blowup as the relative Proj of the Rees algebra, with the descent datum's equivalence-relation field carried as a parameter; Φ and its invertibility and both pullback squares are supplied from the Rees comparison”.

> The blowing up of an algebraic space `X` along a closed subspace `Z ⊆ X`: the relative Proj
> `Proj_X(⨁_{n ≥ 0} 𝓘_Zⁿ)` of the Rees algebra of the defining ideal sheaf of `Z`, as an algebraic
> space over `S`. The subspace `Z` is the centre.

```lean
def blowUpAlong : AlgebraicSpaces B S hS
```

**`AlgebraicGeometry.Space.blowUpAlongHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupRelativeProj.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupRelativeProj.lean#L446). The attribute's comment: “the morphism b of the blowup, with the descent datum's equivalence-relation field carried as a parameter”.

> The blowing up `b : Proj_X(⨁_{n ≥ 0} 𝓘_Zⁿ) ⟶ X` of an algebraic space `X` along a closed
> subspace `Z ⊆ X`, as a morphism of algebraic spaces over `S`.

```lean
def blowUpAlongHom : blowUpAlong Z P hcU hcR heq ⟶ X
```

**`AlgebraicGeometry.Space.exceptionalDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupRelativeProj.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupRelativeProj.lean#L452). The attribute's comment: “the exceptional divisor b⁻¹(Z) of the blowup, and the centre Z”.

> The exceptional divisor `b⁻¹(Z)` of the blowing up of `X` along `Z`: the inverse image of the
> centre along the structure morphism of the blowup, as a closed subspace of the blowup.

```lean
def exceptionalDivisor : ClosedSubspaces B S hS (blowUpAlong Z P hcU hcR heq).obj
```

## Tag 085R, a lemma

[Tag 085R](https://stacks.math.columbia.edu/tag/085R) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_iso_proj_reesGrading_affineChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartRees.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartRees.lean#L448). The attribute's comment: “the canonical isomorphism clause: for an affine scheme U = Spec A of the site étale over X, the fibre product U ×\_X X' is the scheme Proj of the Rees algebra of the ideal I of A corresponding to the restriction of the centre's defining sheaf of ideals, by an isomorphism over U; the blowup b is named by the universal property of Stacks 085U, and the only side conditions are the three B.Contains conditions on the relative Projs of the chart's own presentation that the construction of Stacks 085Q already takes; the tag's affine open covering clause is a separate registration”.

> **Stacks 085R, the canonical isomorphism.**  Let `S` be a scheme, let `X` be an algebraic
> space over `S`, let `Z ⊆ X` be a closed subspace with quasi-coherent defining sheaf of ideals
> `ℐ ⊆ 𝒪_X` and let `b : X' ⟶ X` be the blowup of `X` in `Z`.  Let `U = Spec A` be an affine
> scheme of the site étale over `X` and let `I ⊆ A` be the ideal corresponding to `ℐ|_U`.  Then
> `U ×_X X'` is a scheme, and it is canonically isomorphic over `U` to the homogeneous spectrum
> `Proj(⨁_{d ≥ 0} Iᵈ)` of the Rees algebra of `I` in `A`.
>
> The first isomorphism exhibits the fibre product as the algebraic space of a scheme of the
> site, namely the relative `Proj` `P_U` of the Rees algebra of `ℐ|_U`, compatibly with the
> projections to `U`; the second identifies that scheme over `U` with `Proj` of the Rees algebra
> of `I`, where `I` is the ideal of sections of `ℐ|_U` over `A`, which is the defining ideal of
> the centre on the chart by
> `AlgebraicGeometry.Space.reesChartIdeal_selfPresentation_eq_ofIdealTop`.

```lean
theorem exists_iso_proj_reesGrading_affineChart
    {X X' W : AlgebraicSpaces B S hS} {Z : ClosedSubspaces B S hS X.obj}
    {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    {a : schemeSpace V ⟶ X} (ha : IsEtale B S hS a.hom)
    (hcU : B.Contains (reesChartSituation (centreIdeal (preimageClosedSubspace a Z))
      (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).relativeProj)
    (hcR : B.Contains (reesRelationSituation (centreIdeal (preimageClosedSubspace a Z))
      (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).relativeProj)
    (hcRR : B.Contains (reesDoubleSituation (centreIdeal (preimageClosedSubspace a Z))
      (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).relativeProj)
    {q : W ⟶ schemeSpace V} {r : W ⟶ X'} (sq : IsPullback q r a b)
    (I : Ideal ↥Γ((BigFppfOver.toScheme B S hS).obj V,
      (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1))
    (hI : (reesChartIdeal (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).ideal
        (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)) = I) :
    ∃ e : W ≅ schemeSpace (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU),
      e.hom ≫ schemeSpaceMap (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
          (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU) = q ∧
      ∃ f : AlgebraicGeometry.Proj (Stacks.Blowup.reesGrading I) ≅
          (BigFppfOver.toScheme B S hS).obj
            (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU),
        f.hom ≫ (BigFppfOver.toScheme B S hS).map
            (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU) =
          Stacks.Blowup.toSpec I ≫
            (Stacks.RelativeProj.isAffineOpen (Stacks.Blowup.topAffineOpen
              ((BigFppfOver.toScheme B S hS).obj V))).isoSpec.inv ≫
              (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1.ι
```

**`AlgebraicGeometry.Space.exists_iSup_opensRange_specAffineBlowupι_affineChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartRees.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartRees.lean#L499). The attribute's comment: “the affine open covering clause: the scheme U ×\_X X' is covered by the images of the open immersions Spec A[I/a] ⟶ U ×\_X X', a ∈ I, out of the spectra of the affine blowup algebras; same hypotheses and same side conditions as the canonical-isomorphism clause”.

> **Stacks 085R, the affine open covering.**  In the situation of
> `AlgebraicGeometry.Space.exists_iso_proj_reesGrading_affineChart`, the scheme representing
> `U ×_X X'` has an affine open covering by the spectra of the affine blowup algebras
> `A[I/a]`, `a ∈ I`: the morphisms `Spec A[I/a] ⟶ U ×_X X'` obtained by composing the standard
> chart `Stacks.Blowup.specAffineBlowupι` with the identification of the previous theorem -- the
> same isomorphism over `U`, whose compatibility with the projections to `U` is restated here --
> are open immersions whose images have supremum the whole space.
>
> The sources of the covering morphisms are the spectra of the affine blowup algebras
> `Stacks.Blowup.affineBlowup I a` by construction, so this is the tag's "Moreover" clause.

```lean
theorem exists_iSup_opensRange_specAffineBlowupι_affineChart
    {X X' W : AlgebraicSpaces B S hS} {Z : ClosedSubspaces B S hS X.obj}
    {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    {a : schemeSpace V ⟶ X} (ha : IsEtale B S hS a.hom)
    (hcU : B.Contains (reesChartSituation (centreIdeal (preimageClosedSubspace a Z))
      (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).relativeProj)
    (hcR : B.Contains (reesRelationSituation (centreIdeal (preimageClosedSubspace a Z))
      (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).relativeProj)
    (hcRR : B.Contains (reesDoubleSituation (centreIdeal (preimageClosedSubspace a Z))
      (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).relativeProj)
    {q : W ⟶ schemeSpace V} {r : W ⟶ X'} (sq : IsPullback q r a b)
    (I : Ideal ↥Γ((BigFppfOver.toScheme B S hS).obj V,
      (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1))
    (hI : (reesChartIdeal (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).ideal
        (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)) = I) :
    ∃ e : W ≅ schemeSpace (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU),
      e.hom ≫ schemeSpaceMap (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
          (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU) = q ∧
      ∃ f : AlgebraicGeometry.Proj (Stacks.Blowup.reesGrading I) ≅
          (BigFppfOver.toScheme B S hS).obj
            (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU),
        (f.hom ≫ (BigFppfOver.toScheme B S hS).map
            (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V) hcU) =
          Stacks.Blowup.toSpec I ≫
            (Stacks.RelativeProj.isAffineOpen (Stacks.Blowup.topAffineOpen
              ((BigFppfOver.toScheme B S hS).obj V))).isoSpec.inv ≫
              (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1.ι) ∧
        (∀ c : I, _root_.AlgebraicGeometry.IsOpenImmersion
            (Stacks.Blowup.specAffineBlowupι I (c : _) c.2 ≫ f.hom)) ∧
          ⨆ c : I, (Stacks.Blowup.specAffineBlowupι I (c : _) c.2 ≫ f.hom).opensRange = ⊤
```

**`AlgebraicGeometry.Space.exists_iso_proj_reesGrading_affineChart_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartReesUnconditional.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartReesUnconditional.lean#L126). The attribute's comment: “the canonical isomorphism clause: for an affine scheme U = Spec A of the site étale over X, the fibre product U ×\_X X' is the scheme Proj of the Rees algebra of the ideal I of A corresponding to the restriction of the centre's defining sheaf of ideals, by an isomorphism over U; the blowup b is named by the universal property of Stacks 085U; there are no side conditions, the three B.Contains conditions on the relative Projs of the chart's own presentation being proved here from the Rees size bound; the tag's affine open covering clause is a separate registration”.

> **Stacks 085R, the canonical isomorphism.**  Let `S` be a scheme, let `X` be an algebraic
> space over `S`, let `Z ⊆ X` be a closed subspace with quasi-coherent defining sheaf of ideals
> `ℐ ⊆ 𝒪_X` and let `b : X' ⟶ X` be the blowup of `X` in `Z`.  Let `U = Spec A` be an affine
> scheme of the site étale over `X` and let `I ⊆ A` be the ideal corresponding to `ℐ|_U`.  Then
> `U ×_X X'` is a scheme, and it is canonically isomorphic over `U` to the homogeneous spectrum
> `Proj(⨁_{d ≥ 0} Iᵈ)` of the Rees algebra of `I` in `A`.
>
> The first isomorphism exhibits the fibre product as the algebraic space of a scheme of the
> site, namely the relative `Proj` `P_U` of the Rees algebra of `ℐ|_U`, compatibly with the
> projections to `U`; the second identifies that scheme over `U` with `Proj` of the Rees algebra
> of `I`, where `I` is the ideal of sections of `ℐ|_U` over `A`, which is the defining ideal of
> the centre on the chart by
> `AlgebraicGeometry.Space.reesChartIdeal_selfPresentation_eq_ofIdealTop`.

```lean
theorem exists_iso_proj_reesGrading_affineChart_unconditional
    {X X' W : AlgebraicSpaces B S hS} {Z : ClosedSubspaces B S hS X.obj}
    {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    {a : schemeSpace V ⟶ X} (ha : IsEtale B S hS a.hom)
    {q : W ⟶ schemeSpace V} {r : W ⟶ X'} (sq : IsPullback q r a b)
    (I : Ideal ↥Γ((BigFppfOver.toScheme B S hS).obj V,
      (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1))
    (hI : (reesChartIdeal (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).ideal
        (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)) = I) :
    ∃ e : W ≅ schemeSpace (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
        (contains_relativeProj_reesChartSituation_selfPresentation Z V a)),
      e.hom ≫ schemeSpaceMap (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
          (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
          (contains_relativeProj_reesChartSituation_selfPresentation Z V a)) = q ∧
      ∃ f : AlgebraicGeometry.Proj (Stacks.Blowup.reesGrading I) ≅
          (BigFppfOver.toScheme B S hS).obj
            (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
              (contains_relativeProj_reesChartSituation_selfPresentation Z V a)),
        f.hom ≫ (BigFppfOver.toScheme B S hS).map
            (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
              (contains_relativeProj_reesChartSituation_selfPresentation Z V a)) =
          Stacks.Blowup.toSpec I ≫
            (Stacks.RelativeProj.isAffineOpen (Stacks.Blowup.topAffineOpen
              ((BigFppfOver.toScheme B S hS).obj V))).isoSpec.inv ≫
              (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1.ι
```

**`AlgebraicGeometry.Space.exists_iSup_opensRange_specAffineBlowupι_affineChart_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartReesUnconditional.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupAffineChartReesUnconditional.lean#L175). The attribute's comment: “the affine open covering clause: the scheme U ×\_X X' is covered by the images of the open immersions Spec A[I/a] ⟶ U ×\_X X', a ∈ I, out of the spectra of the affine blowup algebras; same hypotheses as the canonical-isomorphism clause and, like it, no side conditions”.

> **Stacks 085R, the affine open covering.**  In the situation of
> `AlgebraicGeometry.Space.exists_iso_proj_reesGrading_affineChart_unconditional`, the scheme
> representing `U ×_X X'` has an affine open covering by the spectra of the affine blowup
> algebras `A[I/a]`, `a ∈ I`: the morphisms `Spec A[I/a] ⟶ U ×_X X'` obtained by composing the
> standard chart `Stacks.Blowup.specAffineBlowupι` with the identification of the previous
> theorem -- the same isomorphism over `U`, whose compatibility with the projections to `U` is
> restated here -- are open immersions whose images have supremum the whole space.
>
> The sources of the covering morphisms are the spectra of the affine blowup algebras
> `Stacks.Blowup.affineBlowup I a` by construction, so this is the tag's "Moreover" clause.

```lean
theorem exists_iSup_opensRange_specAffineBlowupι_affineChart_unconditional
    {X X' W : AlgebraicSpaces B S hS} {Z : ClosedSubspaces B S hS X.obj}
    {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
    {a : schemeSpace V ⟶ X} (ha : IsEtale B S hS a.hom)
    {q : W ⟶ schemeSpace V} {r : W ⟶ X'} (sq : IsPullback q r a b)
    (I : Ideal ↥Γ((BigFppfOver.toScheme B S hS).obj V,
      (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1))
    (hI : (reesChartIdeal (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).ideal
        (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)) = I) :
    ∃ e : W ≅ schemeSpace (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
        (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
        (contains_relativeProj_reesChartSituation_selfPresentation Z V a)),
      e.hom ≫ schemeSpaceMap (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
          (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
          (contains_relativeProj_reesChartSituation_selfPresentation Z V a)) = q ∧
      ∃ f : AlgebraicGeometry.Proj (Stacks.Blowup.reesGrading I) ≅
          (BigFppfOver.toScheme B S hS).obj
            (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
              (contains_relativeProj_reesChartSituation_selfPresentation Z V a)),
        (f.hom ≫ (BigFppfOver.toScheme B S hS).map
            (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
              (contains_relativeProj_reesChartSituation_selfPresentation Z V a)) =
          Stacks.Blowup.toSpec I ≫
            (Stacks.RelativeProj.isAffineOpen (Stacks.Blowup.topAffineOpen
              ((BigFppfOver.toScheme B S hS).obj V))).isoSpec.inv ≫
              (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1.ι) ∧
        (∀ c : I, _root_.AlgebraicGeometry.IsOpenImmersion
            (Stacks.Blowup.specAffineBlowupι I (c : _) c.2 ≫ f.hom)) ∧
          ⨆ c : I, (Stacks.Blowup.specAffineBlowupι I (c : _) c.2 ≫ f.hom).opensRange = ⊤
```

## Tag 085S, a lemma

[Tag 085S](https://stacks.math.columbia.edu/tag/085S) in the Stacks Project.

**`AlgebraicGeometry.Space.isBlowupAlong_preimage_of_isPullback_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupFlatBaseChange.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupFlatBaseChange.lean#L130).

> **Stacks 085S.** Let `g : X₁ ⟶ X₂` be a flat morphism of algebraic spaces over `S`, let
> `Z₂ ⊆ X₂` be a closed subspace and let `b₂ : X₂' ⟶ X₂` be the blowup of `X₂` in `Z₂`.  Then for
> any cartesian square with legs `q : W ⟶ X₁` and `r : W ⟶ X₂'` over `g` and `b₂`, the projection
> `q` is the blowup of `X₁` in the inverse image of `Z₂`.
>
> So the square expressing `W = X₁ ×_{X₂} X₂'` is the cartesian square of the source, with
> `W = X₁'`.
>
> Flatness enters only to see that the inverse image of the centre in `W` — which is the inverse
> image along `r` of the exceptional divisor of `b₂` — is an effective Cartier divisor; the
> universal property of `q` holds for an arbitrary `g`.

```lean
theorem isBlowupAlong_preimage_of_isPullback_of_isFlat
    {X₁ X₂ X₂' W : AlgebraicSpaces B S hS} {g : X₁ ⟶ X₂} (hg : IsFlat B S hS g.hom)
    {Z₂ : ClosedSubspaces B S hS X₂.1} {b₂ : X₂' ⟶ X₂}
    (hb₂ : IsBlowupAlong B S hS Z₂ b₂) {q : W ⟶ X₁} {r : W ⟶ X₂'}
    (sq : IsPullback q r g b₂) :
    IsBlowupAlong B S hS (preimageClosedSubspace g Z₂) q
```

**`AlgebraicGeometry.Space.isBlowupAlong_pullbackFst_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupFlatBaseChange.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupFlatBaseChange.lean#L159).

> **Stacks 085S for the chosen fibre product.** The first projection of the fibre product
> `X₁ ×_{X₂} X₂'` of a flat morphism `g : X₁ ⟶ X₂` with the blowup `b₂ : X₂' ⟶ X₂` of `X₂` in a
> closed subspace `Z₂` is the blowup of `X₁` in the inverse image of `Z₂`.

```lean
theorem isBlowupAlong_pullbackFst_of_isFlat
    {X₁ X₂ X₂' : AlgebraicSpaces B S hS} {g : X₁ ⟶ X₂} (hg : IsFlat B S hS g.hom)
    {Z₂ : ClosedSubspaces B S hS X₂.1} {b₂ : X₂' ⟶ X₂}
    (hb₂ : IsBlowupAlong B S hS Z₂ b₂) :
    IsBlowupAlong B S hS (preimageClosedSubspace g Z₂) (pullback.fst g b₂)
```

**`AlgebraicGeometry.Space.exists_isPullback_blowup_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupFlatBaseChange.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupFlatBaseChange.lean#L183).

> **Stacks 085S in the source's phrasing.** For a flat morphism `g : X₁ ⟶ X₂` of algebraic
> spaces over `S`, a closed subspace `Z₂ ⊆ X₂` with inverse image `Z₁ ⊆ X₁`, the blowup
> `b₁ : X₁' ⟶ X₁` of `X₁` in `Z₁` and the blowup `b₂ : X₂' ⟶ X₂` of `X₂` in `Z₂`, there is a
> morphism `X₁' ⟶ X₂'` making the square
>
> ```
> X₁' ⟶ X₂'
>  ↓      ↓
> X₁ ⟶  X₂
> ```
>
> cartesian.
>
> The fibre product `X₁ ×_{X₂} X₂'` is a blowup of `X₁` in `Z₁` by
> `AlgebraicGeometry.Space.isBlowupAlong_pullbackFst_of_isFlat`, and any two blowups of `X₁` in
> `Z₁` are isomorphic over `X₁`, so `X₁'` is itself a fibre product.

```lean
theorem exists_isPullback_blowup_of_isFlat
    {X₁ X₂ X₁' X₂' : AlgebraicSpaces B S hS} {g : X₁ ⟶ X₂} (hg : IsFlat B S hS g.hom)
    {Z₂ : ClosedSubspaces B S hS X₂.1} {b₂ : X₂' ⟶ X₂}
    (hb₂ : IsBlowupAlong B S hS Z₂ b₂) {b₁ : X₁' ⟶ X₁}
    (hb₁ : IsBlowupAlong B S hS (preimageClosedSubspace g Z₂) b₁) :
    ∃ m : X₁' ⟶ X₂', IsPullback b₁ m g b₂
```

## Tag 085T, a lemma

[Tag 085T](https://stacks.math.columbia.edu/tag/085T) in the Stacks Project.

**`AlgebraicGeometry.Space.isEffectiveCartierDivisor_exceptionalDivisor_blowUpAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupExceptionalCartier.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupExceptionalCartier.lean#L124). The attribute's comment: “part (2), the exceptional divisor b⁻¹(Z) of the blowup of an algebraic space along a closed subspace is an effective Cartier divisor on the blowup”.

> **Stacks 085T part (2).** Let `X` be an algebraic space over a scheme `S`, let `Z ⊆ X` be a
> closed subspace and let `b : X' ⟶ X` be the blowing up of `X` along `Z` of Stacks 085Q, the
> relative `Proj` of the Rees algebra `⨁_{n ≥ 0} 𝓘_Zⁿ`.  Then the exceptional divisor `b⁻¹(Z)` is
> an effective Cartier divisor on `X'`.
>
> By Stacks 083C (2) ⟹ (1) it is enough to see this on one surjective étale scheme chart of `X'`,
> and the construction supplies one: the relative `Proj` `P_U` of the Rees algebra on the
> presenting scheme `U` of the étale presentation, whose composite with `b` is `P_U ⟶ U ⟶ X`.  The
> inverse image of `b⁻¹(Z)` there is therefore the inverse image along `P_U ⟶ U` of the closed
> subscheme `Z ×_X U` of `U`, whose ideal sheaf is the sheaf of ideals `𝓘_Z|_U` the Rees algebra is
> formed from, and for a scheme that inverse image is an effective Cartier divisor by Stacks 02OS
> (2).
>
> The parameters `hcU`, `hcR` and `heq` are the ones the blowup of Stacks 085Q is built from: two
> containment conditions on the big fppf site and the normalisation and cocycle conditions making
> the two projections of the relative `Proj`s an internal equivalence relation.

```lean
theorem isEffectiveCartierDivisor_exceptionalDivisor_blowUpAlong :
    IsEffectiveCartierDivisor B S hS (blowUpAlong Z P hcU hcR heq)
      (exceptionalDivisor Z P hcU hcR heq)
```

**`AlgebraicGeometry.Space.IsBlowupAlong.isIso_and_isEffectiveCartierDivisor_and_twist_neg_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupExceptionalTwist.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupExceptionalTwist.lean#L209). The attribute's comment: “all three parts, for any blowup b of X in a closed subspace Z in the sense of the Stacks 085U universal property: (1) b is an isomorphism over the complement of Z, (2) the exceptional divisor is an effective Cartier divisor, (3) O(E) = O(-1), read as in Stacks 084D on every affine scheme V etale over X, where V x\_X X' = Proj of the Rees algebra (Stacks 085R) and the base change of O(E) is the twist O(-1); no other hypothesis”.

> **Stacks 085T.**  Let `S` be a scheme, let `X` be an algebraic space over `S`, let `Z ⊆ X` be
> a closed subspace and let `b : X' ⟶ X` be the blowing up of `X` in `Z`, in the sense of the
> universal property of Stacks 085U.  Then
>
> 1. the restriction `b⁻¹(X ∖ Z) ⟶ X ∖ Z` of `b` is an isomorphism;
> 2. the exceptional divisor `E = b⁻¹(Z)` is an effective Cartier divisor on `X'`;
> 3. `𝒪_{X'}(E) = 𝒪_{X'}(-1)`: for every affine scheme `V = Spec A` étale over `X`, with `I ⊆ A` the
>    ideal of `Z` on `V`, the fibre product `V ×_X X'` is identified over `V` with the scheme
>    `Proj(⨁_{d ≥ 0} Iᵈ)` (by `e` and `f`, as in Stacks 085R), and under that identification the
>    base change of the invertible sheaf `𝒪_{X'}(E)` of Stacks 0841 is the twist `𝒪(-1)`.
>
> Part (3) is the characterization of the twists of the relative `Proj` in Stacks 084D (their base
> change to schemes over `X` are the twists of Stacks 01NR), applied to the affine schemes étale
> over `X`, which cover it.

```lean
theorem isIso_and_isEffectiveCartierDivisor_and_twist_neg_one
    {X X' : AlgebraicSpaces B S hS} {Z : ClosedSubspaces B S hS X.1} {b : X' ⟶ X}
    (hb : IsBlowupAlong B S hS Z b) :
    IsIso ((openComplementOfClosedSubspace B S hS X Z).1.fromPreimage b.hom) ∧
      IsEffectiveCartierDivisor B S hS X' (preimageClosedSubspace b Z) ∧
      ∀ (V : BigFppfOver B S hS) [IsAffine ((BigFppfOver.toScheme B S hS).obj V)]
        (a : schemeSpace V ⟶ X), IsEtale B S hS a.hom →
        ∀ (I : Ideal ↥Γ((BigFppfOver.toScheme B S hS).obj V,
            (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1)),
          (reesChartIdeal (centreIdeal (preimageClosedSubspace a Z))
            (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)).ideal
            (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)) = I →
        ∀ {W : AlgebraicSpaces B S hS} {q : W ⟶ schemeSpace V} {r : W ⟶ X'},
          IsPullback q r a b →
        ∃ e : W ≅ schemeSpace (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
            (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
            (contains_relativeProj_reesChartSituation_selfPresentation Z V a)),
          e.hom ≫ schemeSpaceMap (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
              (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
              (contains_relativeProj_reesChartSituation_selfPresentation Z V a)) = q ∧
          ∃ f : AlgebraicGeometry.Proj (Stacks.Blowup.reesGrading I) ≅
              (BigFppfOver.toScheme B S hS).obj
                (reesProjChart (centreIdeal (preimageClosedSubspace a Z))
                  (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
                  (contains_relativeProj_reesChartSituation_selfPresentation Z V a)),
            f.hom ≫ (BigFppfOver.toScheme B S hS).map
                (reesProjChartHom (centreIdeal (preimageClosedSubspace a Z))
                  (isCartesianOnAffineCharts_centreIdeal _) (selfPresentation B S hS V)
                  (contains_relativeProj_reesChartSituation_selfPresentation Z V a)) =
              Stacks.Blowup.toSpec I ≫
                (Stacks.RelativeProj.isAffineOpen (Stacks.Blowup.topAffineOpen
                  ((BigFppfOver.toScheme B S hS).obj V))).isoSpec.inv ≫
                  (Stacks.Blowup.topAffineOpen ((BigFppfOver.toScheme B S hS).obj V)).1.ι ∧
            Nonempty ((Scheme.Modules.pullback f.hom).obj
                (baseChangeModule B S hS (associatedInvertibleSheaf B S hS X'
                  (preimageClosedSubspace b Z) hb.isPullbackDefined) _ (e.inv ≫ r).hom) ≅
              twistingSheaf (Stacks.Blowup.reesGrading I) (-1))
```

**`AlgebraicGeometry.Space.isIso_fromPreimage_openComplement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupIsomorphismOffCentre.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupIsomorphismOffCentre.lean#L200). The attribute's comment: “part (1): the blowup is an isomorphism away from the centre”.

> **Stacks 085T, part (1).** The blowup `b : X' ⟶ X` of an algebraic space `X` in a closed
> subspace `Z` is an isomorphism over the open complement of `Z`: the restriction
> `b⁻¹(X ∖ Z) ⟶ X ∖ Z` of `b` is an isomorphism.
>
> Both `X ∖ Z` and `b⁻¹(X ∖ Z)` are algebraic spaces over `X` on which the inverse image of `Z`
> has no points, hence is an effective Cartier divisor, so each admits a unique morphism to `X'`
> over `X` by the universal property of Stacks 085U.  The morphism out of `X ∖ Z` lands in
> `b⁻¹(X ∖ Z)` and is inverse to the restriction of `b`, the two composites being identified with
> the identities by the uniqueness of those lifts.

```lean
theorem isIso_fromPreimage_openComplement {X X' : AlgebraicSpaces B S hS}
    {Z : ClosedSubspaces B S hS X.1} {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b) :
    IsIso ((openComplementOfClosedSubspace B S hS X Z).1.fromPreimage b.hom)
```

**`AlgebraicGeometry.Space.blowUpTwistSpaceNegOneIsoAssociatedInvertibleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupTwistDescentCanonical.lean, line 869](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupTwistDescentCanonical.lean#L869). The attribute's comment: “part (3): the canonical isomorphism O\_\{X'}(-1) = O\_\{X'}(E) on the blowup of an algebraic space, O\_\{X'}(1) being descended along the unique transition compatible with the canonical map O(1) → O”. References: EGA II (8.1.8), “partial”.

> **Stacks 085T, part (3): the canonical isomorphism `𝒪_{X'}(-1) ≅ 𝒪_{X'}(E)`.**  Let
> `b : X' ⟶ X` be the blowing up of an algebraic space `X` along a closed subspace `Z` (Stacks
> 085Q, `AlgebraicGeometry.Space.blowUpAlong'`, with the equivalence-relation field of its descent
> datum discharged by `AlgebraicGeometry.Space.isEquivalenceRelation_post_reesProj`), with
> exceptional divisor `E = b⁻¹(Z)`, an effective Cartier divisor by part (2).  Then the twisting
> sheaf `𝒪_{X'}(-1)` is isomorphic to the invertible sheaf `𝒪_{X'}(E)` of Stacks 0841 (1).
>
> Here `𝒪_{X'}(n)` is the `n`th tensor power (Stacks 01CU) of the invertible sheaf `𝒪_{X'}(1)`
> obtained by descending, along the étale presentation `P_R ⇉ P_U` of `X'` and the equivalence of
> Stacks 03M3, the twisting sheaf `𝒪_{P_U}(1)` of the blowup `P_U` of the presenting scheme `U` in
> `𝓘_Z|_U`, with transition morphism `α'` (`AlgebraicGeometry.Space.blowUpTwistDescentDatum`).
>
> **Why the isomorphism is canonical.**  The descent datum of `𝒪_{X'}(1)` is characterised
> without reference to `E` (`AlgebraicGeometry.Space.eq_blowUpTwistDescentDatum_alpha_iff`): a
> morphism `β : t^*𝒪_{P_U}(1)^a ⟶ s^*𝒪_{P_U}(1)^a` is the transition `α'` if and only if
> `β ≫ s^*c = t^*c ≫ α_𝒪`, where `α_𝒪` is the canonical descent datum of `𝒪_{X'}` and
> `c = (blowUpChartTwistOneToUnit)^a ≫ u⁻¹`, built from the canonical map `𝒪(1) ⟶ 𝒪` of the
> scheme blowup `P_U` (`AlgebraicGeometry.Space.blowUpChartTwistOneToUnit`: Stacks 02OS (3)
> followed by the inclusion into `𝒪`, which on the standard chart at `a ∈ 𝓘(U)` is
> `t ↦ (t / a⁽¹⁾) · b^♯(a)`, the map induced by the shift `A(1) ⟶ A` of the Rees algebra,
> `AlgebraicGeometry.incl_app_twistOneIsoExceptionalIdealModule_hom`) and the identification
> `u : φ^*𝒪_{X'} ≅ 𝒪_{P_U}^a` of `AlgebraicGeometry.Space.modulePullbackPresentationAtlasUnitIso`,
> built from `𝒪` alone.  That lemma combines the uniqueness of the transition
> (`AlgebraicGeometry.Space.eq_blowUpTwistDescentDatum_alpha`), its computation at the atlas
> (`AlgebraicGeometry.Space.blowUpAtlasMapComputes_idealSheaf`) and on the chart
> (`AlgebraicGeometry.Space.blowUpChartTwistOneIsoIdealSheaf_hom_comp_ι`).  So `𝒪_{X'}(1)` is the
> descent of `𝒪_{P_U}(1)` along the unique datum compatible with `𝒪(1) ⟶ 𝒪`, and the isomorphism
> below is `AlgebraicGeometry.Space.blowUpTwistSpaceNegOneIso`, the inverse of the descended
> `𝒪_{X'}(1) ≅ 𝓘_E` of Stacks 02OS (3).
>
> The parameters `hcU`, `hcR` and `hcRR` are the containment conditions on the big fppf site under
> which the relative `Proj`s of the blowup are objects of the site.

```lean
def blowUpTwistSpaceNegOneIsoAssociatedInvertibleSheaf (Z : ClosedSubspaces B S hS X.obj)
    (P : Presentation B S hS X.obj X.property)
    (hcU : B.Contains (reesChartSituation (centreIdeal Z)
      (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcR : B.Contains (reesRelationSituation (centreIdeal Z)
      (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcRR : B.Contains (reesDoubleSituation (centreIdeal Z)
      (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj) :
    blowUpTwistSpace Z P hcU hcR (isEquivalenceRelation_post_reesProj (centreIdeal Z)
        (isCartesianOnAffineCharts_centreIdeal Z) P hcU hcR hcRR) (-1) ≅
      associatedInvertibleSheaf B S hS (blowUpAlong Z P hcU hcR
          (isEquivalenceRelation_post_reesProj (centreIdeal Z)
            (isCartesianOnAffineCharts_centreIdeal Z) P hcU hcR hcRR))
        (exceptionalDivisor Z P hcU hcR (isEquivalenceRelation_post_reesProj (centreIdeal Z)
          (isCartesianOnAffineCharts_centreIdeal Z) P hcU hcR hcRR))
        (isEffectiveCartierDivisor_exceptionalDivisor_blowUpAlong Z P hcU hcR
          (isEquivalenceRelation_post_reesProj (centreIdeal Z)
            (isCartesianOnAffineCharts_centreIdeal Z) P hcU hcR hcRR))
```

## Tag 085U, a lemma

[Tag 085U](https://stacks.math.columbia.edu/tag/085U) in the Stacks Project.

**`AlgebraicGeometry.Space.isBlowupAlong_blowUpAlongHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupFinality.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupFinality.lean#L441). The attribute's comment: “the blowup of an algebraic space along a closed subspace is a final object of the category of those Y over X whose inverse image of the centre is an effective Cartier divisor; both halves, membership and finality”.

> **Stacks 085U.**  The blowing up `b : X' ⟶ X` of an algebraic space `X` along a closed
> subspace `Z ⊆ X` is a final object of the category `𝒞` of algebraic spaces over `X` on which the
> inverse image of `Z` is an effective Cartier divisor.
>
> Membership in `𝒞` is
> `AlgebraicGeometry.Space.isEffectiveCartierDivisor_exceptionalDivisor'` and finality is
> `AlgebraicGeometry.Space.existsUnique_hom_blowUpAlong'`; the two are assembled by
> `AlgebraicGeometry.Space.isBlowupAlong_of_existsUnique_lift`.  The hypotheses are exactly the
> data the construction of Tag 085Q itself takes — an étale presentation `P` of `X`, the universe
> choice `HasSheafify` for the quotient presheaf, and the three `B.Contains` side conditions on
> the relative `Proj`s which `AlgebraicGeometry.Space.relativeProjChartOfSituation` already asks
> for; nothing is assumed about `Z` beyond being a closed subspace, and in particular no
> separatedness or density input is used.
>
> This declaration alone carries Tag 085U.  Both halves are recovered from it by projection —
> membership as `AlgebraicGeometry.Space.IsBlowupAlong.isPullbackDefined`, which is
> `AlgebraicGeometry.Space.isEffectiveCartierDivisor_exceptionalDivisor'` up to unfolding
> `AlgebraicGeometry.Space.exceptionalDivisor'`, and finality as
> `AlgebraicGeometry.Space.IsBlowupAlong.existsUnique_lift`, which is
> `AlgebraicGeometry.Space.existsUnique_lift_blowUpAlongHom'` — so neither of those two is
> registered.

```lean
theorem isBlowupAlong_blowUpAlongHom' :
    IsBlowupAlong B S hS Z (blowUpAlongHom' Z P hcU hcR hcRR)
```

## Tag 085V, a lemma

[Tag 085V](https://stacks.math.columbia.edu/tag/085V) in the Stacks Project.

**`AlgebraicGeometry.Space.isBlowupAlong_id_of_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupOfEffectiveCartierDivisor.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupOfEffectiveCartierDivisor.lean#L92).

> **Stacks 085V.** Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `Z ⊆ X` be an effective Cartier divisor.  **The blowup of `X` in `Z` is the identity morphism
> of `X`.**
>
> Being the blowup of `X` in `Z` is the universal property of Tag 085U, which
> `AlgebraicGeometry.Space.IsBlowupAlong` records: terminality in the category `𝒞` of algebraic
> spaces over `X` on which the inverse image of `Z` is an effective Cartier divisor.  The
> identity of `X` is an object of `𝒞` precisely because `Z` is an effective Cartier divisor, and
> it is terminal in `𝒞` because it is already terminal in all of `Spaces/X` and `𝒞` is a full
> subcategory.  Since terminal objects are unique up to unique isomorphism over `X`, this says
> that the blowup of `X` in `Z` exists and is the identity of `X`; see
> `AlgebraicGeometry.Space.IsBlowupAlong.isIso_of_isEffectiveCartierDivisor`.

```lean
theorem isBlowupAlong_id_of_isEffectiveCartierDivisor (X : AlgebraicSpaces B S hS)
    (Z : ClosedSubspaces B S hS X.1) (hZ : IsEffectiveCartierDivisor B S hS X Z) :
    IsBlowupAlong B S hS Z (𝟙 X)
```

## Tag 085W, a lemma

[Tag 085W](https://stacks.math.columbia.edu/tag/085W) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_of_isBlowupAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupReduced.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupReduced.lean#L120). The attribute's comment: “given the étale-chart representability of the blowup supplied by Stacks 085Q”.

> **Stacks 085W**, with the étale-chart representability of Stacks 085Q carried as a
> hypothesis.
>
> Let `X` be a reduced algebraic space over `S`, let `Z ⊆ X` be the closed subspace cut out by a
> quasi-coherent sheaf of ideals and let `b : X' ⟶ X` be the blowup of `X` in `Z`.  Then `X'` is
> reduced.
>
> The chart datum is the source's: a surjective étale morphism `a : U ⟶ X` from a scheme `U` of
> the site, and the fibre product `W = U ×_X X'` as a cartesian square.  The hypothesis `hrep`
> supplies what Stacks 085Q would: some blowup of `U` in the inverse image of `Z` is
> representable by a scheme isomorphic to a scheme blowup of `U`.  See the module documentation
> for why that hypothesis is upstream of this conclusion.

```lean
theorem isReduced_of_isBlowupAlong
    {X X' W : AlgebraicSpaces B S hS} {Z : ClosedSubspaces B S hS X.1} {b : X' ⟶ X}
    (hb : IsBlowupAlong B S hS Z b)
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsReduced T))
    (V : BigFppfOver B S hS) (a : schemeSpace V ⟶ X)
    (haE : IsEtale B S hS a.hom) (haS : IsSurjective B S hS a.hom)
    {q : W ⟶ schemeSpace V} {r : W ⟶ X'} (sq : IsPullback q r a b)
    (hrep : ∃ (Y : AlgebraicSpaces B S hS) (p : Y ⟶ schemeSpace V),
      IsBlowupAlong B S hS (preimageClosedSubspace a Z) p ∧
      ∃ (V' : BigFppfOver B S hS) (_ : Y.1 ≅ yoneda.obj V')
        (I : ((BigFppfOver.toScheme B S hS).obj V).IdealSheafData),
        Nonempty ((BigFppfOver.toScheme B S hS).obj V' ≅ blowUp I)) :
    HasEtaleLocalProperty B S hS X'.1 (fun T : Scheme.{u} => IsReduced T)
```

**`AlgebraicGeometry.Space.isReduced_of_isBlowupAlong_of_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupReducedPresentation.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupReducedPresentation.lean#L90). The attribute's comment: “the blowup of a reduced algebraic space in a closed subspace is reduced, with no assumed inputs beyond the Stacks 085Q construction data — the étale presentation P of the space, the HasSheafify universe choice for the quotient presheaf, and the three B.Contains size conditions on the relative Projs of the chart, relation and double situations — none of which occurs in the conclusion”.

> **Stacks 085W.**  Let `X` be an algebraic space over `S` and let `Z ⊆ X` be the closed
> subspace cut out by a quasi-coherent sheaf of ideals.  If `X` is reduced then so is the blowup
> `b : X' ⟶ X` of `X` in `Z`.
>
> Nothing about the blowup is assumed beyond its universal property, Stacks 085U: the étale chart
> of `X'` the proof runs on is the one the construction of Stacks 085Q supplies, namely the
> relative `Proj` `P_U` of the Rees algebra of the chart ideal on the presenting scheme `U` of the
> presentation `P`.  That scheme is the blowup of the *scheme* `U`, by
> `Stacks.Blowup.reesSituationBlowUpIso`, so it is reduced by Stacks 0808; `P_U ⟶ X'` is
> surjective étale, so Stacks 06MI carries reducedness to the constructed blowup, and from there
> to `b` along the isomorphism of any two blowups in the same centre.
>
> Besides `Z`, the blowup `b` and reducedness of `X` the statement takes only the data the
> construction of Stacks 085Q itself takes: the presentation `P`, the universe choice
> `HasSheafify` for the quotient presheaf, and the three `B.Contains` side conditions on the
> relative `Proj`s which `AlgebraicGeometry.Space.relativeProjChartOfSituation` already asks for.
> None of that appears in the conclusion.

```lean
theorem isReduced_of_isBlowupAlong_of_presentation
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    {X X' : AlgebraicSpaces B S hS} (Z : ClosedSubspaces B S hS X.obj)
    (P : Presentation B S hS X.obj X.property)
    (hcU : B.Contains (reesChartSituation (centreIdeal Z)
        (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcR : B.Contains (reesRelationSituation (centreIdeal Z)
        (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcRR : B.Contains (reesDoubleSituation (centreIdeal Z)
        (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsReduced T)) :
    HasEtaleLocalProperty B S hS X'.1 (fun T : Scheme.{u} => IsReduced T)
```

## Tag 0BH1, a lemma

[Tag 0BH1](https://stacks.math.columbia.edu/tag/0BH1) in the Stacks Project.

**`AlgebraicGeometry.Space.hasLocallyFiniteIrreducibleComponents_of_isBlowupAlong_of_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupLocallyFiniteIrreducibleComponents.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupLocallyFiniteIrreducibleComponents.lean#L127). The attribute's comment: “the blowup of an algebraic space satisfying the equivalent conditions of Stacks 0BB1 in a closed subspace satisfies them too, with no assumed inputs beyond the Stacks 085Q construction data for the centre -- a presentation P, the HasSheafify universe choice, and the three B.Contains side conditions hcU, hcR and hcRR on the relative Projs -- none of which occurs in the conclusion”.

> **Stacks 0BH1.**  Let `X` be an algebraic space over `S` and let `Z ⊆ X` be the closed
> subspace cut out by a quasi-coherent sheaf of ideals.  If `X` satisfies the equivalent
> conditions of Stacks 0BB1 — here its condition (2),
> `AlgebraicGeometry.Space.HasLocallyFiniteIrreducibleComponents` — then so does the blowup
> `b : X' ⟶ X` of `X` in `Z`.
>
> Nothing about the blowup is assumed beyond its universal property, Stacks 085U: the étale
> chart of `X'` the proof runs on is the one the construction of Stacks 085Q supplies, namely the
> relative `Proj` `P_U` of the Rees algebra of the chart ideal on the presenting scheme `U` of
> the presentation `P`.  That scheme is the blowup of the *scheme* `U`, by
> `Stacks.Blowup.reesSituationBlowUpIso`, so every quasi-compact open of it has finitely many
> irreducible components by
> `AlgebraicGeometry.finite_irreducibleComponents_of_isCompact_blowUp`; `P_U ⟶ X'` is surjective
> étale, so conditions (1) and (2) of Stacks 0BB1 carry the condition to the constructed blowup,
> and from there to `b` along the isomorphism of any two blowups in the same centre.
>
> Besides `Z`, the blowup `b` and the hypothesis on `X` the statement takes only the data the
> construction of Stacks 085Q itself takes: the presentation `P`, the universe choice
> `HasSheafify` for the quotient presheaf, and the three `B.Contains` side conditions on the
> relative `Proj`s which `AlgebraicGeometry.Space.relativeProjChartOfSituation` already asks for.
> None of that appears in the conclusion.

```lean
theorem hasLocallyFiniteIrreducibleComponents_of_isBlowupAlong_of_presentation
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    {X X' : AlgebraicSpaces B S hS} (Z : ClosedSubspaces B S hS X.obj)
    (P : Presentation B S hS X.obj X.property)
    (hcU : B.Contains (reesChartSituation (centreIdeal Z)
        (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcR : B.Contains (reesRelationSituation (centreIdeal Z)
        (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    (hcRR : B.Contains (reesDoubleSituation (centreIdeal Z)
        (isCartesianOnAffineCharts_centreIdeal Z) P).relativeProj)
    {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    (hX : HasLocallyFiniteIrreducibleComponents B S hS X.1) :
    HasLocallyFiniteIrreducibleComponents B S hS X'.1
```

## Tag 085X, a lemma

[Tag 085X](https://stacks.math.columbia.edu/tag/085X) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullbackDefined_blowUpAlongHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupDivisorPullback.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupDivisorPullback.lean#L204). The attribute's comment: “for the blowup of Stacks 085Q: with no assumed inputs beyond the construction data P, hcU, hcR and heq naming the blowup, every effective Cartier divisor on an algebraic space has a defined pullback along it”.

> **Stacks 085X.** Let `X` be an algebraic space over a scheme `S`, let `Z ⊆ X` be a closed
> subspace and let `b : X' ⟶ X` be the blowing up of `X` along `Z` of Stacks 085Q.  Then for every
> effective Cartier divisor `D` on `X` the pullback `b⁻¹(D)` is defined in the sense of Stacks
> 083Y: the inverse image of `D` along `b` is again an effective Cartier divisor, on `X'`.
>
> By Stacks 083C (2) ⟹ (1) it is enough to see this on one surjective étale scheme chart of `X'`,
> and the construction supplies one: the relative `Proj` `P_U` of the Rees algebra of `𝓘_Z|_U` on
> the presenting scheme `U` of the étale presentation, whose composite with `b` is `P_U ⟶ U ⟶ X`.
> The inverse image of `b⁻¹(D)` there is therefore the inverse image along `P_U ⟶ U` of the closed
> subscheme `D ×_X U` of `U`, which is an effective Cartier divisor on `U` by Stacks 083C
> (1) ⟹ (3); and for a scheme the inverse image of an effective Cartier divisor along a blowup is
> an effective Cartier divisor by Stacks 0809.
>
> The parameters `P`, `hcU`, `hcR` and `heq` are the ones the blowup of Stacks 085Q is built from
> and only name the blowup; the hypothesis on `D` is the source's own.

```lean
theorem isPullbackDefined_blowUpAlongHom (D : ClosedSubspaces B S hS X.obj)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    IsPullbackDefined B S hS (blowUpAlongHom Z P hcU hcR heq) D
```

**`AlgebraicGeometry.Space.isPullbackDefined_of_isBlowupAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupDivisorPullback.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupDivisorPullback.lean#L267). The attribute's comment: “the source statement, for any b which is a blowup of X in a closed subspace in the sense of the Stacks 085U universal property; with no assumed inputs apart from the Stacks 085Q construction data P, hcU, hcR and hcRR, which does not occur in the conclusion”.

> **Stacks 085X, for an arbitrary blowup.**  Let `X` be an algebraic space over a scheme `S`,
> let `Z ⊆ X` be a closed subspace and let `b : X' ⟶ X` be *a* blowup of `X` in `Z`, in the sense
> of the universal property of Stacks 085U.  Then for every effective Cartier divisor `D` on `X`
> the pullback `b⁻¹(D)` is defined in the sense of Stacks 083Y.
>
> This is the source's statement: nothing distinguishes `b` beyond being a blowup of `X` in a
> closed subspace, and `D` is an arbitrary effective Cartier divisor.  A blowup in a fixed centre
> is unique up to isomorphism over the base,
> `AlgebraicGeometry.Space.IsBlowupAlong.exists_iso`, and the blowup of Stacks 085Q is one,
> `AlgebraicGeometry.Space.isBlowupAlong_blowUpAlongHom'` (Stacks 085U); so `b` is isomorphic over
> `X` to the constructed blowup, for which
> `AlgebraicGeometry.Space.isPullbackDefined_blowUpAlongHom` gives the conclusion; and that
> conclusion crosses the isomorphism by
> `AlgebraicGeometry.Space.isPullbackDefined_of_iso_over`.
>
> The parameters `P`, `hcU`, `hcR` and `hcRR` are those of the construction of Stacks 085Q, used
> only to produce the blowup `b` is compared against; none of them occurs in the conclusion.

```lean
theorem isPullbackDefined_of_isBlowupAlong {X' : AlgebraicSpaces B S hS} {b : X' ⟶ X}
    (hb : IsBlowupAlong B S hS Z b) (D : ClosedSubspaces B S hS X.obj)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    IsPullbackDefined B S hS b D
```

**`AlgebraicGeometry.Space.isPullbackDefined_of_exists_isBlowupAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupDivisorPullbackAnyBlowup.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupDivisorPullbackAnyBlowup.lean#L49). The attribute's comment: “the full statement, for every morphism b which is a blowup of X in some closed subspace (Stacks 085U universal property) and every effective Cartier divisor D on X; no construction data and no size condition on the site among the hypotheses”.

> **Stacks 085X.**  Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `b : X' ⟶ X` be a blowup of `X` in a closed subspace.  Then for every effective Cartier divisor
> `D` on `X` the pullback `b⁻¹(D)` is defined in the sense of Stacks 083Y: the inverse image of
> `D` along `b` is an effective Cartier divisor on `X'`.
>
> "A blowup of `X` in a closed subspace" is `∃ Z, IsBlowupAlong B S hS Z b`: `b` is a final object
> of the category of algebraic spaces over `X` on which the inverse image of the closed subspace
> `Z` is an effective Cartier divisor (Stacks 085U), so `b` is isomorphic over `X` to the blowing
> up of `X` along `Z` of Stacks 085Q.

```lean
theorem isPullbackDefined_of_exists_isBlowupAlong {X X' : AlgebraicSpaces B S hS}
    (b : X' ⟶ X) (hb : ∃ Z : ClosedSubspaces B S hS X.1, IsBlowupAlong B S hS Z b) :
    ∀ D : ClosedSubspaces B S hS X.1, IsEffectiveCartierDivisor B S hS X D →
      IsPullbackDefined B S hS b D
```

## Tag 085Y, a lemma

[Tag 085Y](https://stacks.math.columbia.edu/tag/085Y) in the Stacks Project.

**`AlgebraicGeometry.Space.isBlowupAlong_comp_of_isBlowupAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupComposite.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupComposite.lean#L218). The attribute's comment: “with no assumed inputs beyond the Stacks 085Q construction data P, hcU, hcR and hcRR for the second centre, which does not occur in the conclusion: for b a blowup of X in Z and b' a blowup of X' in the inverse image of Y, both in the sense of the Stacks 085U universal property, the composite b' followed by b is the blowup of X in the sum Z + Y”.

> **Stacks 085Y.**  Let `S` be a scheme, let `X` be an algebraic space over `S` and let
> `Z, Y ⊆ X` be closed subspaces.  Let `b : X' ⟶ X` be a blowup of `X` in `Z` and let
> `b' : X'' ⟶ X'` be a blowup of `X'` in the inverse image `b⁻¹(Y)`, both in the sense of the
> universal property of Stacks 085U.  Then the composite `b' ≫ b` is the blowup of `X` in the sum
> `Z + Y`, the closed subspace cut out by the product of the two defining ideals (Stacks 083U).
>
> Read through that universal property, which is how `AlgebraicGeometry.Space.IsBlowupAlong` says
> "is the blowup", the conclusion asserts both that the blowup of `X` in `Z + Y` exists and that
> it is `b' ≫ b`; that is the source's "`X'' ⟶ X` is canonically isomorphic to the blowing up of
> `X` in `𝓘𝓙`", and the isomorphism itself is
> `AlgebraicGeometry.Space.exists_iso_blowup_comp_of_isBlowupAlong'`.
>
> The hypotheses on the two blowups are the source's own: each is named only by being a blowup of
> its centre.  What is carried beyond them is the construction data of Stacks 085Q for the second
> centre `b⁻¹(Y)` — an étale presentation `P` of `X'`, the `HasSheafify` universe choice, and the
> three `B.Contains` side conditions on the relative `Proj`s which
> `AlgebraicGeometry.Space.relativeProjChartOfSituation` already asks for.  That data produces the
> *constructed* blowup of `X'` in `b⁻¹(Y)`, which is what Stacks 085X is proved for; none of it
> occurs in the conclusion, and no input of Stacks 085Y is assumed.
>
> The proof is `AlgebraicGeometry.Space.isBlowupAlong_comp_of_isBlowupAlong` with its Tag 085X
> hypothesis discharged by `AlgebraicGeometry.Space.isPullbackDefined_of_isBlowupAlong`, applied
> to the effective Cartier divisor `b⁻¹(Z)` on `X'` — effective Cartier because `b` is the blowup
> of `Z`, so this is `AlgebraicGeometry.Space.IsBlowupAlong.isPullbackDefined` of `hb`.

```lean
theorem isBlowupAlong_comp_of_isBlowupAlong'
    {Z Y : ClosedSubspaces B S hS X.1} {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    {b' : X'' ⟶ X'} (hb' : IsBlowupAlong B S hS (preimageClosedSubspace b Y) b')
    (P : Presentation B S hS X'.obj X'.property)
    (hcU : B.Contains (reesChartSituation (centreIdeal (preimageClosedSubspace b Y))
      (isCartesianOnAffineCharts_centreIdeal (preimageClosedSubspace b Y)) P).relativeProj)
    (hcR : B.Contains (reesRelationSituation (centreIdeal (preimageClosedSubspace b Y))
      (isCartesianOnAffineCharts_centreIdeal (preimageClosedSubspace b Y)) P).relativeProj)
    (hcRR : B.Contains (reesDoubleSituation (centreIdeal (preimageClosedSubspace b Y))
      (isCartesianOnAffineCharts_centreIdeal (preimageClosedSubspace b Y)) P).relativeProj) :
    IsBlowupAlong B S hS (sumClosedSubspaces B S hS X Z Y) (b' ≫ b)
```

## Tag 085Z, a lemma

[Tag 085Z](https://stacks.math.columbia.edu/tag/085Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_of_isBlowupAlong_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupPropernessReesChart.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupPropernessReesChart.lean#L244). The attribute's comment: “the blowup b : X' -> X of an algebraic space X in a closed subspace Z whose closed immersion is of finite presentation (equivalently, whose quasi-coherent ideal sheaf is of finite type) is a proper morphism, at the source's hypotheses: the relative Proj charts the proof reads are shown to lie in the site by hasReesProjChartInSite\_of\_isFinitePresentation”.

> **Stacks 085Z.**  Let `X` be an algebraic space over a scheme `S` and let `Z ⊆ X` be a
> closed subspace whose closed immersion is of finite presentation — equivalently, whose
> quasi-coherent sheaf of ideals `𝓘` is of finite type.  Then every blowup `b : X' ⟶ X` of `X` in
> `Z` (in `𝓘`) is a proper morphism.
>
> The source's proof: properness is étale local on the target (Stacks 083R), blowing up commutes
> with flat base change (Stacks 085S), and over a scheme chart the blowup is proper because `𝓘`
> is of finite type there (Stacks 02NS, 01WC).  That is
> `AlgebraicGeometry.Space.isProper_of_isBlowupAlong_of_hasReesProjChartInSite`, applied on the
> chart of an étale presentation of `X`, on which the relative `Proj`s the argument reads lie in
> the site by `AlgebraicGeometry.Space.hasReesProjChartInSite_of_isFinitePresentation`.
>
> The only argument beyond the source's is the instance `HasSheafify` for the big fppf topology:
> the existence of sheafification of `Type u`-valued presheaves on the site, which this library's
> construction of blowups of algebraic spaces (Stacks 085Q) and its chart description
> (Stacks 085R) are stated with.

```lean
theorem isProper_of_isBlowupAlong_of_isFinitePresentation (Z : ClosedSubspaces B S hS X.1)
    (b : X' ⟶ X) (hfp : IsFinitePresentation B S hS Z.1.ι) (hb : IsBlowupAlong B S hS Z b) :
    IsProper B S hS b.hom
```

## Tag 0860, a lemma

[Tag 0860](https://stacks.math.columbia.edu/tag/0860) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isCompositeCentre_isBlowupAlong_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BlowupCompositeCentre.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BlowupCompositeCentre.lean#L466).

> **Stacks 0860.**  Let `S` be a scheme and let `X` be a quasi-compact and quasi-separated
> algebraic space over `S`.  Let `Z ⊆ X` be a closed subspace of finite presentation and let
> `b : X' ⟶ X` be the blowing up of `X` in `Z`.  Let `Z' ⊆ X'` be a closed subspace of finite
> presentation and let `c : X'' ⟶ X'` be the blowing up of `X'` in `Z'`.  Then there exists a
> closed subspace `Y ⊆ X` of finite presentation such that `|Y| = |Z| ∪ |b|(|Z'|)` and
> `c ≫ b : X'' ⟶ X` is isomorphic to the blowing up of `X` in `Y`.
>
> The blowups are named by their universal property, Stacks 085U
> (`AlgebraicGeometry.Space.IsBlowupAlong`), so "isomorphic to the blowing up of `X` in `Y`" is
> `IsBlowupAlong B S hS Y (c ≫ b)`, and `|Y| = |Z| ∪ |b|(|Z'|)` is
> `AlgebraicGeometry.Space.IsCompositeCentre`.  Quasi-separatedness of `X` is absolute
> quasi-separatedness, which needs the terminal scheme in the site (`hZ`).
>
> This is `AlgebraicGeometry.Space.exists_isCompositeCentre_isBlowupAlong` with its second centre
> supplied by `AlgebraicGeometry.Space.hasSecondCentre`; see the module documentation for how that
> replaces the source's appeal to Stacks 085N.

```lean
theorem exists_isCompositeCentre_isBlowupAlong_of_isQuasiCompactSpace
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (hZ : B.Contains (⊤_ Scheme.{u})) (hXqc : IsQuasiCompactSpace B S hS X.1)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X.1)
    {Z : ClosedSubspaces B S hS X.1} {b : X' ⟶ X} (hb : IsBlowupAlong B S hS Z b)
    (hZfp : IsFinitePresentation B S hS Z.1.ι)
    {Z' : ClosedSubspaces B S hS X'.1} {c : X'' ⟶ X'} (hc : IsBlowupAlong B S hS Z' c)
    (hZ'fp : IsFinitePresentation B S hS Z'.1.ι) :
    ∃ Y : ClosedSubspaces B S hS X.1, IsFinitePresentation B S hS Y.1.ι ∧
      IsCompositeCentre B S hS b Z Z' Y ∧ IsBlowupAlong B S hS Y (c ≫ b)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.17, Tag 085P](https://stacks.math.columbia.edu/tag/085P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
