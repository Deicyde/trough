---
declaration: section
origin: cited
lean: AlgebraicGeometry.blowUp, AlgebraicGeometry.blowUpToBase, AlgebraicGeometry.exceptionalIdeal, AlgebraicGeometry.exceptionalDivisor, Stacks.Blowup.exists_reesAlgebraData, Stacks.Blowup.blowUp, Stacks.Blowup.blowUpToBase, Stacks.Blowup.isPullback_blowUpChart
statement: formalized
proof: formalized
---

# 31.33 Blowing up

Section 31.33 of the Stacks Project, [Tag 01OF](https://stacks.math.columbia.edu/tag/01OF). 14 tags here are carried by 43 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01OG, a definition

[Tag 01OG](https://stacks.math.columbia.edu/tag/01OG) in the Stacks Project.

**`AlgebraicGeometry.blowUp`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean#L63). The attribute's comment: “blowup morphism”. References: EGA II (8.1.3), “qcoh ideal case”; EGA IV (19.4.1), “X'=Proj(⊕J^n)”.

> **Stacks Project, Tag 01OG.** The blowup of `X` in the quasi-coherent ideal `I`: the
> relative `Proj` of the Rees algebra `⨁ₙ Iⁿ`.

```lean
public noncomputable abbrev blowUp {X : Scheme.{u}} (I : X.IdealSheafData) : Scheme.{u}
```

**`AlgebraicGeometry.blowUpToBase`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean#L71). The attribute's comment: “blowup morphism”. References: EGA II (8.1.3), “qcoh ideal case”; EGA IV (19.4.1), “structural morphism f”.

> **Stacks Project, Tag 01OG.** The blowup morphism: the structure morphism of the blowup of
> `X` in `I` to `X`.

```lean
public noncomputable abbrev blowUpToBase {X : Scheme.{u}} (I : X.IdealSheafData) :
    blowUp I ⟶ X
```

**`AlgebraicGeometry.exceptionalIdeal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean#L77). The attribute's comment: “exceptional ideal sheaf”.

> The inverse-image ideal defining the exceptional divisor.

```lean
public noncomputable abbrev exceptionalIdeal {X : Scheme.{u}} (I : X.IdealSheafData) :
    (blowUp I).IdealSheafData
```

**`AlgebraicGeometry.exceptionalDivisor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowUp.lean#L84). The attribute's comment: “exceptional divisor scheme”. References: EGA IV (19.4.1), “Y'=f^\{-1}(Y)”; SGA 7 XVIII (2.1).

> **Stacks Project, Tag 01OG.** The exceptional divisor is the inverse image of the
> closed subscheme cut out by `I`.

```lean
public noncomputable abbrev exceptionalDivisor {X : Scheme.{u}} (I : X.IdealSheafData) :
    Scheme.{u}
```

**`Stacks.Blowup.exists_reesAlgebraData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebraSheaf.lean, line 805](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebraSheaf.lean#L805). The attribute's comment: “Rees algebra sheaf”.

> **Stacks Project, Tag 01OG.** A graded sheaf with the canonical affine-local description
> of `⨁ₙ Iⁿ` exists.

```lean
public theorem exists_reesAlgebraData {X : Scheme.{u}} (I : X.IdealSheafData) :
    Nonempty (ReesAlgebraData I)
```

**`Stacks.Blowup.blowUp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L233). The attribute's comment: “the blowup as a scheme”. References: EGA II (8.1.3); EGA IV (19.4.1); SGA 6 VII (1.8).

> The blowup of a scheme `S` in a quasi-coherent sheaf of ideals
> `ℐ`: the relative `Proj` of the Rees algebra `⨁_{n ≥ 0} ℐⁿ`.

```lean
def blowUp : Scheme.{u}
```

**`Stacks.Blowup.blowUpToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 237](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L237). The attribute's comment: “the blowup morphism”.

> The structure morphism of the blowup to its base.

```lean
def blowUpToBase : blowUp ℐ ⟶ S
```

**`Stacks.Blowup.isPullback_blowUpChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L256). The attribute's comment: “the affine charts of the blowup”.

> The blowup restricted to an affine open `U` of the base is `Proj` of the Rees algebra of
> `ℐ(U)`: the chart over `U` is the preimage of `U` under the blowup morphism.

```lean
theorem isPullback_blowUpChart (U : S.affineOpens) :
    IsPullback (Stacks.RelativeProj.chartToOpen (fun W : S.affineOpens ↦ reesGrading (ℐ.ideal W))
      U (reesBase ℐ U)) (blowUpChart ℐ U) U.1.ι (blowUpToBase ℐ)
```

**`Stacks.Blowup.exceptionalIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L269). The attribute's comment: “the exceptional ideal sheaf”.

> The ideal sheaf of the exceptional divisor: the inverse image of `ℐ` under the blowup
> morphism.

```lean
def exceptionalIdeal : (blowUp ℐ).IdealSheafData
```

**`Stacks.Blowup.exceptionalDivisor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L274). The attribute's comment: “the exceptional divisor”. References: SGA 7 XVIII (2.1).

> The exceptional divisor of the blowup: the closed subscheme of the blowup cut out by the
> inverse image of `ℐ`.

```lean
def exceptionalDivisor : Scheme.{u}
```

## Tag 0804, a lemma

[Tag 0804](https://stacks.math.columbia.edu/tag/0804) in the Stacks Project.

**`Stacks.Blowup.reesAwayEquivAffineBlowup`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AffineChart.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AffineChart.lean#L229). The attribute's comment: “the chart D₊(a⁽¹⁾) is Spec of the affine blowup algebra”.

> **Stacks Project, Tag 0804.** For `a ∈ I` the standard affine chart of `Proj` of the Rees
> algebra at the degree-one element `a⁽¹⁾` is the affine blowup algebra `R[I/a]`: the degree-zero
> part of the localization of `R[It]` at `a⁽¹⁾` is `R[I/a]`.
>
> This is the chart computation behind the second assertion of tag 0804; the covering statement
> itself is `Stacks.Blowup.iSup_opensRange_blowUpAffineChart`.

```lean
def reesAwayEquivAffineBlowup (ha : a ∈ I) :
    Away (reesGrading I) (reesDegOne I ha) ≃+* affineBlowup I a
```

**`Stacks.Blowup.iSup_opensRange_blowUpAffineChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/AffineChart.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/AffineChart.lean#L409). The attribute's comment: “b⁻¹(U) is covered by the spectra of the affine blowup algebras”.

> **Stacks Project, Tag 0804, second assertion.** Let `b : X' ⟶ S` be the blowup of a scheme
> `S` in a quasi-coherent sheaf of ideals `ℐ`, and let `U` be an affine open of `S`. Then `b⁻¹(U)`
> is covered by the spectra of the affine blowup algebras `Γ(S, U)[ℐ(U)/a]` for `a ∈ ℐ(U)`: the
> morphisms `Stacks.Blowup.blowUpAffineChart` are open immersions whose images have supremum
> `b⁻¹(U)`.
>
> Together with the first assertion, `Stacks.Blowup.isPullback_blowUpChart`, this completes tag
> 0804.

```lean
theorem iSup_opensRange_blowUpAffineChart (U : S.affineOpens) :
    ⨆ r : ℐ.ideal U, (blowUpAffineChart ℐ U r.2).opensRange
      = blowUpToBase ℐ ⁻¹ᵁ (U : S.Opens)
```

**`AlgebraicGeometry.affineBlowupStandardOpenIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean, line 539](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean#L539). The attribute's comment: “affine blowup algebra chart”.

> The standard affine chart of the Rees projective spectrum is canonically the
> spectrum of the affine blowup algebra.

```lean
public noncomputable def affineBlowupStandardOpenIso {X : Scheme.{u}}
    (I : X.IdealSheafData) (U : X.affineOpens) (a : I.ideal U) :
    letI := (reesSituation I).sectionRingGradedRing U.1
    letI := (reesSituation I).sectionRingGradingGradedRing U.1
    Spec (.of <| affineBlowupAlgebra (I.ideal U) (a : X.presheaf.obj (.op U.1))
      (Localization.Away (a : X.presheaf.obj (.op U.1)))) ≅
      (Proj.basicOpen ((reesSituation I).sectionRingGrading U.1)
        (reesDegreeOne I U a).1).toScheme
```

**`AlgebraicGeometry.affineBlowupStandardOpenIso_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean#L558). The attribute's comment: “affine blowup chart over the base”.

> The affine blowup chart is an isomorphism over the affine base: its structure
> map is induced by the canonical inclusion of the ring into its blowup algebra.

```lean
public theorem affineBlowupStandardOpenIso_over {X : Scheme.{u}}
    (I : X.IdealSheafData) (U : X.affineOpens) (a : I.ideal U) :
    letI := (reesSituation I).sectionRingGradedRing U.1
    letI := (reesSituation I).sectionRingGradingGradedRing U.1
    (affineBlowupStandardOpenIso I U a).hom ≫
        (Proj.basicOpen ((reesSituation I).sectionRingGrading U.1)
          (reesDegreeOne I U a).1).ι ≫
        Stacks.RelativeProj.Situation.projInclusionToOpen (reesSituation I) U.1 U.2 =
    Spec.map (CommRingCat.ofHom
        (algebraMap (X.presheaf.obj (.op U.1))
          (affineBlowupAlgebra (I.ideal U) (a : X.presheaf.obj (.op U.1))
            (Localization.Away (a : X.presheaf.obj (.op U.1)))))) ≫
        U.2.isoSpec.inv
```

**`AlgebraicGeometry.affineBlowupStandardOpenIso_fraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean#L585). The attribute's comment: “canonical affine blowup fractions”.

> On the standard chart at `a`, a degree-one section `b` divided by `a`
> corresponds to the generating fraction `b/a` in the affine blowup algebra.

```lean
public theorem affineBlowupStandardOpenIso_fraction {X : Scheme.{u}}
    (I : X.IdealSheafData) (U : X.affineOpens) (a b : I.ideal U) :
    letI := (reesSituation I).sectionRingGradedRing U.1
    letI := (reesSituation I).sectionRingGradingGradedRing U.1
    (((Spec.preimage
      ((affineBlowupStandardOpenIso I U a).hom ≫
        (Proj.basicOpenIsoSpec
          ((reesSituation I).sectionRingGrading U.1)
          (reesDegreeOne I U a).1 (reesDegreeOne I U a).2 (by omega)).hom)).hom
      (HomogeneousLocalization.Away.mk
        ((reesSituation I).sectionRingGrading U.1)
        (reesDegreeOne I U a).2 1 (reesDegreeOne I U b).1
        (by simp)) :
      affineBlowupAlgebra (I.ideal U) (a : X.presheaf.obj (.op U.1))
        (Localization.Away (a : X.presheaf.obj (.op U.1)))) :
      Localization.Away (a : X.presheaf.obj (.op U.1))) =
      IsLocalization.mk' (Localization.Away (a : X.presheaf.obj (.op U.1)))
        (b : X.presheaf.obj (.op U.1))
        ⟨(a : X.presheaf.obj (.op U.1)), Submonoid.mem_powers _⟩
```

**`AlgebraicGeometry.blownUpAffine_chart_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean#L699). The attribute's comment: “affine chart covering”.

> Degree-one Rees elements give an affine open cover of the inverse image of
> an affine open under the blowup morphism.

```lean
public theorem blownUpAffine_chart_cover {X : Scheme.{u}} (I : X.IdealSheafData)
    (U : X.affineOpens) :
    letI := (reesSituation I).sectionRingGradedRing U.1
    letI := (reesSituation I).sectionRingGradingGradedRing U.1
    (⋃ a : I.ideal U,
      Set.range ((Proj.basicOpen ((reesSituation I).sectionRingGrading U.1)
        (reesDegreeOne I U a).1).ι ≫
        Stacks.RelativeProj.Situation.relativeProjChart (reesSituation I) U)) =
      (blowUpToBase I ⁻¹ᵁ U.1).1
```

**`Stacks.Blowup.isPullback_blowUpChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesSheafData.lean#L256). The attribute's comment: “the canonical identification of b⁻¹(U) with Proj of the Rees algebra”.

> The blowup restricted to an affine open `U` of the base is `Proj` of the Rees algebra of
> `ℐ(U)`: the chart over `U` is the preimage of `U` under the blowup morphism.

```lean
theorem isPullback_blowUpChart (U : S.affineOpens) :
    IsPullback (Stacks.RelativeProj.chartToOpen (fun W : S.affineOpens ↦ reesGrading (ℐ.ideal W))
      U (reesBase ℐ U)) (blowUpChart ℐ U) U.1.ι (blowUpToBase ℐ)
```

Declarations registered for the tag:

- [`Stacks.RelativeProj.Situation.relativeProjChart_isPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProj/Charts/Descent.lean#L334), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/AffineCharts.lean#L56) (StacksFrontier): “canonical local projective-spectrum identification”.

## Tag 0805, a lemma

[Tag 0805](https://stacks.math.columbia.edu/tag/0805) in the Stacks Project.

**`AlgebraicGeometry.exists_isPullback_blowUpToBase_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/FlatBaseChange.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/FlatBaseChange.lean#L55).

> **Stacks Project, Tag 0805.** Blowing up commutes with flat base change: for a flat
> `g : X₁ ⟶ X₂` and a quasi-coherent ideal `I` on `X₂`, the blowup of `X₁` in the inverse image
> of `I` sits in a cartesian square over the blowup of `X₂` in `I`.

```lean
theorem exists_isPullback_blowUpToBase_comap {X₁ X₂ : Scheme.{u}} (g : X₁ ⟶ X₂) [Flat g]
    (I : X₂.IdealSheafData) :
    ∃ h : blowUp (I.comap g) ⟶ blowUp I,
      IsPullback (blowUpToBase (I.comap g)) h g (blowUpToBase I)
```

## Tag 02OS, a lemma

[Tag 02OS](https://stacks.math.columbia.edu/tag/02OS) in the Stacks Project.

**`Stacks.Blowup.isEffectiveCartierDivisor_exceptionalIdeal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalCartier.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalCartier.lean#L572). The attribute's comment: “exceptional\_effective\_cartier”. References: EGA IV (19.4.1).

> **Stacks Project, Tag 02OS part (2).** For a scheme `X` and a quasi-coherent ideal sheaf
> `I`, the exceptional divisor of the blowup of `X` in `I` — the inverse image of the closed
> subscheme cut out by `I` — is an effective Cartier divisor on the blowup.
>
> Declared as an `instance`, as the tagged statement has it: the head is the ideal sheaf of the
> exceptional divisor, so instance search is not widened.

```lean
instance isEffectiveCartierDivisor_exceptionalIdeal {X : Scheme.{u}} (I : X.IdealSheafData) :
    Stacks.Divisors.IsEffectiveCartierDivisor (exceptionalIdeal I)
```

**`Stacks.Blowup.ideal_exceptionalIdeal_blowUpAffineChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean#L259). The attribute's comment: “the exceptional ideal is generated by one section on an affine chart”.

> **Stacks Project, Tag 02OS, second assertion, affine-local form.** On the affine open of the
> blowup underlying the chart `Spec Γ(S, U)[ℐ(U)/a]`, the exceptional ideal is generated by
> `Stacks.Blowup.exceptionalChartSection`.
>
> This is the equation `IA' = aA'` of the proof of Stacks tag 02OS, for the chart supplied by the
> second assertion of Stacks tag 0804, transported from
> `Stacks.Blowup.ideal_comap_exceptionalIdeal_blowUpAffineChart` across the chart's identification
> of sections.

```lean
theorem ideal_exceptionalIdeal_blowUpAffineChart (U : S.affineOpens)
    {a : Γ(S, U.1)} (ha : a ∈ ℐ.ideal U) :
    (exceptionalIdeal ℐ).ideal ⟨blowUpAffineChart ℐ U ha ''ᵁ ⊤,
        (isAffineOpen_top _).image_of_isOpenImmersion _⟩ =
      Ideal.span {exceptionalChartSection ℐ U ha}
```

**`Stacks.Blowup.exceptionalChartSection_mem_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean#L280). The attribute's comment: “the generator on an affine chart is a nonzerodivisor”.

> **Stacks Project, Tag 02OS, second assertion, affine-local form.** The generator of the
> exceptional ideal on an affine chart of the blowup is a nonzerodivisor.
>
> This is the sentence "`a` maps to a nonzerodivisor in `A'`" of the proof of Stacks tag 02OS.

```lean
theorem exceptionalChartSection_mem_nonZeroDivisors (U : S.affineOpens)
    {a : Γ(S, U.1)} (ha : a ∈ ℐ.ideal U) :
    exceptionalChartSection ℐ U ha ∈
      nonZeroDivisors Γ(blowUp ℐ, blowUpAffineChart ℐ U ha ''ᵁ ⊤)
```

**`Stacks.Blowup.exists_span_eq_ideal_exceptionalIdeal_blowUpAffineChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean#L299). The attribute's comment: “the exceptional ideal is generated by a nonzerodivisor on an affine chart”.

> **Stacks Project, Tag 02OS, second assertion, affine-local form.** On the affine open of the
> blowup underlying the chart `Spec Γ(S, U)[ℐ(U)/a]`, the exceptional ideal is generated by a
> single section, and that section is a nonzerodivisor.
>
> This is the sentence "Then `IA' = aA'` and `a` maps to a nonzerodivisor in `A'`" of the proof of
> Stacks tag 02OS, for the chart supplied by the second assertion of Stacks tag 0804. The generator
> is `Stacks.Blowup.exceptionalChartSection`.

```lean
theorem exists_span_eq_ideal_exceptionalIdeal_blowUpAffineChart (U : S.affineOpens)
    {a : Γ(S, U.1)} (ha : a ∈ ℐ.ideal U) :
    ∃ t ∈ nonZeroDivisors Γ(blowUp ℐ, blowUpAffineChart ℐ U ha ''ᵁ ⊤),
      (exceptionalIdeal ℐ).ideal ⟨blowUpAffineChart ℐ U ha ''ᵁ ⊤,
          (isAffineOpen_top _).image_of_isOpenImmersion _⟩ = Ideal.span {t}
```

**`Stacks.Blowup.isLocallyPrincipal_exceptionalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ExceptionalChart.lean#L317). The attribute's comment: “the exceptional divisor is a locally principal closed subscheme”.

> **Stacks Project, Tag 02OS, second assertion, local principality.** The exceptional divisor
> of the blowup of a scheme in a quasi-coherent sheaf of ideals is a locally principal closed
> subscheme: around every point of the blowup there is an affine open on which the exceptional
> ideal is generated by one element.
>
> Every point of the blowup lies over an affine open `U` of the base, hence in one of the charts
> `Spec Γ(S, U)[ℐ(U)/a]` by the second assertion of Stacks tag 0804
> (`Stacks.Blowup.iSup_opensRange_blowUpAffineChart`), and on that chart the exceptional ideal is
> principal by `Stacks.Blowup.exists_span_eq_ideal_exceptionalIdeal_blowUpAffineChart`.

```lean
theorem isLocallyPrincipal_exceptionalIdeal :
    Stacks.Divisors.IsLocallyPrincipal (exceptionalIdeal ℐ)
```

**`AlgebraicGeometry.isIso_blowUp_restrict_compl_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/IsomorphismOffCenter/Basic.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/IsomorphismOffCenter/Basic.lean#L234). The attribute's comment: “isomorphism\_off\_center”. References: SGA 7 XVIII (2.1), “more general”.

> **Stacks Project, Tag 02OS.** The blowup of a scheme in a quasi-coherent ideal sheaf is an
> isomorphism over the open complement of the closed subscheme the ideal cuts out.

```lean
public theorem isIso_blowUp_restrict_compl_support (I : X.IdealSheafData) :
    IsIso (blowUpToBase I ∣_ (⟨I.supportᶜ, I.support.isClosed.isOpen_compl⟩ : X.Opens))
```

**`AlgebraicGeometry.twistOneIsoExceptionalIdealModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/TwistOneExceptionalIdeal.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/TwistOneExceptionalIdeal.lean#L155). The attribute's comment: “part (3)”. References: EGA IV (19.4.1), “(1)”.

> **[Stacks, Tag 02OS] part (3).** For a scheme `X` and a quasi-coherent sheaf of ideals `ℐ` on
> it, the twisting sheaf `𝒪_{X'}(1)` of the blowup `b : X' ⟶ X` of `X` in `ℐ` is the ideal sheaf
> of the exceptional divisor, the inverse image `ℐ·𝒪_{X'}` of the centre.
>
> No hypothesis is carried: `X` is an arbitrary scheme and `ℐ` an arbitrary quasi-coherent sheaf of
> ideals. Parts (1) and (2) of the tag are
> `AlgebraicGeometry.isIso_blowUp_restrict_compl_support` and
> `Stacks.Blowup.isEffectiveCartierDivisor_exceptionalIdeal`.

```lean
def twistOneIsoExceptionalIdealModule : blowUpTwist I 1 ≅ exceptionalIdealModule I
```

## Tag 0806, a lemma

[Tag 0806](https://stacks.math.columbia.edu/tag/0806) in the Stacks Project.

**`Stacks.Blowup.isTerminal_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ClassifyingMorphism.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ClassifyingMorphism.lean#L478). References: EGA IV (19.4.1); SGA 6 XIII (7.1.4), “more general”.

> **Stacks Project, Tag 0806. The universal property of blowing up.** The blowup of a scheme
> `X` in a quasi-coherent ideal sheaf `ℐ` is a final object of the category `C` of schemes over
> `X` on which the inverse image of the centre is an effective Cartier divisor.
>
> Unconditional. The five geometric inputs of
> `Stacks.Blowup.exists_nonempty_isTerminal`, which is the uniqueness half of the tag reduced to
> them, are now all theorems:
>
> * separatedness of the blowup morphism is tag 01O2,
>   `Stacks.RelativeProj.Situation.isSeparated_relativeProjToBase`;
> * membership of the blowup in `C` is tag 02OS part (2),
>   `Stacks.Blowup.isEffectiveCartierDivisor_exceptionalIdeal`;
> * the blowup is an isomorphism over the complement of the centre by tag 02OS part (1),
>   `AlgebraicGeometry.isIso_blowUpToBase_restrict_compl_support`;
> * scheme-theoretic density of the complement of an effective Cartier divisor is tag 07ZU,
>   `Stacks.Divisors.isSchemeTheoreticallyDense_compl_of_isEffectiveCartierDivisor`, transported
>   along the open immersions of the gluing cover by
>   `AlgebraicGeometry.Scheme.Opens.isSchemeTheoreticallyDense_preimage_of_isOpenImmersion`;
> * the existence of the classifying morphism, which the source deduces from the universal
>   property of relative `Proj` (Constructions, Section 01NS), is
>   `Stacks.Blowup.exists_hom_blowUp_of_isEffectiveCartierDivisor`.
>
> This supersedes `Stacks.Blowup.exists_nonempty_isTerminal_blowUp`, which is the same statement
> with the last two of those as hypotheses.

```lean
theorem isTerminal_blowUp {X : Scheme.{u}} (I : X.IdealSheafData) :
    ∃ h : IsCartierOver I (Over.mk (AlgebraicGeometry.blowUpToBase I)),
      Nonempty (IsTerminal
        (⟨Over.mk (AlgebraicGeometry.blowUpToBase I), h⟩ : CartierOver I))
```

**`AlgebraicGeometry.existsUnique_lift_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupUniversal.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/BlowUpSquare/ChartBlowupUniversal.lean#L87). The attribute's comment: “the terminality of the blowup read as a unique factorization: a morphism along which the inverse image of the centre is an effective Cartier divisor factors through the blowup in exactly one way”.

> **The universal property of blowing up, Stacks tag 0806, as a unique factorization.**  A
> morphism `f : Y ⟶ X` along which the inverse image of the centre is an effective Cartier divisor
> factors through the blowup in exactly one way.  This is the terminality statement
> `Stacks.Blowup.isTerminal_blowUp` read as a `∃!`.

```lean
theorem existsUnique_lift_blowUpToBase {X : Scheme.{u}} (I : X.IdealSheafData) {Y : Scheme.{u}}
    (f : Y ⟶ X) (hf : Stacks.Divisors.IsEffectiveCartierDivisor (I.comap f)) :
    ∃! k : Y ⟶ blowUp I, k ≫ blowUpToBase I = f
```

## Tag 0BFL, a lemma

[Tag 0BFL](https://stacks.math.columbia.edu/tag/0BFL) in the Stacks Project.

**`AlgebraicGeometry.mem_affineBlowupStandardOpen_iff_exceptionalIdeal_stalk_eq_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/ChartMembership.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/ChartMembership.lean#L360).

> A point of a blowup lies in the standard affine chart at `a` if and only if
> the image of `a` generates the exceptional ideal in its local ring.

```lean
public theorem mem_affineBlowupStandardOpen_iff_exceptionalIdeal_stalk_eq_span
    {X : Scheme.{u}} (I : X.IdealSheafData) (U : X.affineOpens)
    (a : I.ideal U) (x : (blowUp I))
    (hx : (blowUpToBase I) x ∈ U.1) :
    letI := (reesSituation I).sectionRingGradedRing U.1
    letI := (reesSituation I).sectionRingGradingGradedRing U.1
    x ∈ Set.range
      ((Proj.basicOpen ((reesSituation I).sectionRingGrading U.1)
        (reesDegreeOne I U a).1).ι ≫
        (Stacks.RelativeProj.Situation.relativeProjChart (reesSituation I) U)) ↔
      AlgebraicGeometry.IdealSheafData.stalk (exceptionalIdeal I) x =
        Ideal.span
          {((blowUpToBase I).stalkMap x)
            (X.presheaf.germ U.1 ((blowUpToBase I) x) hx
              (a : X.presheaf.obj (.op U.1)))}
```

## Tag 0807, a lemma

[Tag 0807](https://stacks.math.columbia.edu/tag/0807) in the Stacks Project.

**`Stacks.Blowup.isIso_blowUpToBase_of_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/CartierCentre.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/CartierCentre.lean#L56).

> **[Stacks, Tag 0807].** Blowing up a scheme in an effective Cartier divisor does not change
> it: the blowup morphism is an isomorphism.
>
> The identity of `X` lies in the category `C` of [Stacks, Tag 0806] precisely because `I` is an
> effective Cartier divisor, and the blowup is a final object of `C`
> (`Stacks.Blowup.isTerminal_blowUp`), so the classifying morphism of the identity is a two-sided
> inverse of the blowup morphism.

```lean
public theorem isIso_blowUpToBase_of_isEffectiveCartierDivisor {X : Scheme.{u}}
    (I : X.IdealSheafData) (hI : Stacks.Divisors.IsEffectiveCartierDivisor I) :
    IsIso (AlgebraicGeometry.blowUpToBase I)
```

## Tag 0808, a lemma

[Tag 0808](https://stacks.math.columbia.edu/tag/0808) in the Stacks Project.

**`AlgebraicGeometry.isReduced_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/Reduced.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/Reduced.lean#L53).

> **Stacks Project, Tag 0808.** The blowup of a reduced scheme in a quasi-coherent ideal is
> reduced.

```lean
theorem isReduced_blowUp [IsReduced X] : IsReduced (blowUp I)
```

## Tag 02ND, a lemma

[Tag 02ND](https://stacks.math.columbia.edu/tag/02ND) in the Stacks Project.

**`AlgebraicGeometry.isIntegral_blowUp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/Integral.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/Integral.lean#L134). References: EGA II (8.1.4), “(i) integrality, blowup”.

> **Stacks Project, Tag 02ND.** The blowup of an integral scheme in a nonzero quasi-coherent
> ideal is integral.

```lean
theorem isIntegral_blowUp (hI : I ≠ ⊥) : IsIntegral (blowUp I)
```

## Tag 0BFM, a lemma

[Tag 0BFM](https://stacks.math.columbia.edu/tag/0BFM) in the Stacks Project.

**`AlgebraicGeometry.bijOn_genericPoints_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/GenericPoints.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/GenericPoints.lean#L82).

> The blowup morphism restricts to a bijection from the generic
> points of the irreducible components of the blowup onto the generic points of those irreducible
> components of the base that are not contained in the centre.

```lean
theorem bijOn_genericPoints_blowUpToBase {X : Scheme.{u}} (I : X.IdealSheafData) :
    Set.BijOn (blowUpToBase I) (genericPoints (blowUp I)) (genericPoints X \ I.supportSet)
```

## Tag 0809, a lemma

[Tag 0809](https://stacks.math.columbia.edu/tag/0809) in the Stacks Project.

**`AlgebraicGeometry.isPullbackDefined_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/RegularPullback.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/RegularPullback.lean#L293). The attribute's comment: “effective Cartier divisors”. References: SGA 7 X (2.6), “partial”.

> **Stacks Project, Tag 0809.** Every effective Cartier divisor on a scheme has a defined
> pullback along the blowup of the scheme in any quasi-coherent ideal.

```lean
theorem isPullbackDefined_blowUpToBase (D : X.IdealSheafData)
    (hD : Stacks.Divisors.IsEffectiveCartierDivisor D) :
    Stacks.Divisors.IsPullbackDefined (blowUpToBase I) D
```

**`AlgebraicGeometry.pullbacksMeromorphicSections_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/RegularPullback.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/RegularPullback.lean#L334). The attribute's comment: “meromorphic functions”.

> **Stacks Project, Tag 0809.** Pullbacks of meromorphic functions are defined along the
> blowup of a scheme in any quasi-coherent ideal.

```lean
theorem pullbacksMeromorphicSections_blowUpToBase :
    PullbacksMeromorphicSections (blowUpToBase I).toLRSHom
```

## Tag 080A, a lemma

[Tag 080A](https://stacks.math.columbia.edu/tag/080A) in the Stacks Project.

**`AlgebraicGeometry.blowUpMulIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/Product.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/Product.lean#L139). The attribute's comment: “canonical isomorphism”.

> **Stacks Project, Tag 080A.** Blowing up `X` in `I` and then in the inverse image of `J` is
> canonically, over `X`, the blowup of `X` in `I * J`.

```lean
def blowUpMulIso :
    Over.mk (blowUpToBase (J.comap (blowUpToBase I)) ≫ blowUpToBase I) ≅
      Over.mk (blowUpToBase (I * J))
```

**`AlgebraicGeometry.blowUpMulIso_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/Transform/Product.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/Transform/Product.lean#L149). The attribute's comment: “uniqueness”.

> The isomorphism of Stacks tag 080A is the unique isomorphism of these two blowups over
> `X`: both are terminal in the same category.

```lean
theorem blowUpMulIso_unique
    (e : Over.mk (blowUpToBase (J.comap (blowUpToBase I)) ≫ blowUpToBase I) ≅
      Over.mk (blowUpToBase (I * J))) : e = blowUpMulIso I J
```

## Tag 02NS, a lemma

[Tag 02NS](https://stacks.math.columbia.edu/tag/02NS) in the Stacks Project.

**`AlgebraicGeometry.exists_isInvertibleModule_isRelativelyAmple_blowUpTwist`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowupTwist.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/BlowupTwist.lean#L88). The attribute's comment: “part (2): `𝒪_{X'}(1)` is a `b`-relatively ample invertible sheaf”. References: EGA II (4.6.18), “special case”; EGA III (2.3.4), “(i), special case”.

> **Stacks Project, Tag 02NS, part (2).** Let `ℐ ⊆ 𝒪_X` be a quasi-coherent sheaf of ideals of
> finite type and `b : X' ⟶ X` the blowup of `X` in `ℐ`. Then `𝒪_{X'}(1)` is a `b`-relatively
> ample invertible sheaf: it is invertible, and with that invertibility it is ample relative to `b`
> in the sense of Tag 01VH.
>
> Invertibility is stated, not presupposed: it is the witness of the existential, and the relative
> ampleness that follows is read with it. The twist `𝒪_{X'}(1)` is `AlgebraicGeometry.blowUpTwist`,
> the twisting sheaf of the relative `Proj` of the Rees algebra glued along the transition datum
> `Stacks.RelativeProj.Situation.twistTransition`.

```lean
public theorem exists_isInvertibleModule_isRelativelyAmple_blowUpTwist (hI : I.IsFiniteType) :
    ∃ _ : Stacks.Ample.IsInvertibleModule (blowUp I) (blowUpTwist I 1),
      Stacks.RelativeAmple.IsRelativelyAmple (blowUpToBase I) (blowUpTwist I 1)
```

**`AlgebraicGeometry.isProjective_blowUpToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/Projective.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/Projective.lean#L76). The attribute's comment: “part (1): `b : X' ⟶ X` is a projective morphism”. References: EGA IV (19.4.1).

> The blowup of a scheme in a quasi-coherent sheaf of ideals of finite type is a projective
> morphism.

```lean
public theorem isProjective_blowUpToBase (hI : I.IsFiniteType) :
    IsProjective (blowUpToBase I)
```

**`AlgebraicGeometry.isRelativelyAmple_twist_reesSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/TwistAmple.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/ReesAlgebra/TwistAmple.lean#L152). The attribute's comment: “part (2): `𝒪_{X'}(1)` is a `b`-relatively ample invertible sheaf, for the twist glued from the chart twists along a transition datum for Tag 01NO (3) and (4), which is carried as the hypothesis `Stacks.RelativeProj.Situation.TwistTransition`”.

> **Stacks Project, Tag 02NS, part (2).** The twisting sheaf `𝒪_{X'}(1)` of the blowup of a
> scheme in a quasi-coherent sheaf of ideals of finite type is a relatively ample invertible sheaf
> for the blowup morphism: over an affine open `V` of the base the blowup is the `Proj` of the Rees
> algebra of `ℐ(V)`, the twist restricts there to the absolute `𝒪(1)`, and that is ample.

```lean
public theorem isRelativelyAmple_twist_reesSituation (hI : I.IsFiniteType)
    (t : (reesSituation I).TwistTransition 1) :
    Stacks.RelativeAmple.IsRelativelyAmple (blowUpToBase I) (Situation.twist t)
```

## Tag 080B, a lemma

[Tag 080B](https://stacks.math.columbia.edu/tag/080B) in the Stacks Project.

**`AlgebraicGeometry.finitePresentation_mul_subschemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentre.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentre.lean#L137). The attribute's comment: “the centre Y is of finite presentation. Y is the explicit product I * J of the first centre with the second-centre ideal that Stacks Lemma 31.32.5, Tag 0803, supplies, and a product of a finitely presented centre with a centre of finite type is finitely presented”.

> The product of a finitely presented centre with a centre of finite type is again a finitely
> presented centre: by [Stacks, Tag 01TV] both statements say that the ideal is finitely generated
> over every affine open, and the ideal of `I * J` there is the product of the two ideals.
>
> This is the finite-presentation clause of [Stacks, Tag 080B].

```lean
theorem finitePresentation_mul_subschemeι (I J : X.IdealSheafData)
    (hI : FinitePresentation I.subschemeι) (hJ : ∀ U : X.affineOpens, (J.ideal U).FG) :
    FinitePresentation (I * J).subschemeι
```

**`AlgebraicGeometry.exists_centre_supportSet_eq_and_nonempty_blowUpCompositionIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentreExistence.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentreExistence.lean#L74).

> **Stacks Project, Tag 080B.** Let `X` be a quasi-compact and quasi-separated scheme, let `I`
> be a finitely presented centre on `X` with blowup `b : X' ⟶ X`, and let `Z'` be a finitely
> presented centre on `X'`. Then there is a finitely presented centre `Y` on `X` whose support is
> `Supp I ∪ b(Supp Z')` and for which the two-step blowup `Bl_{Z'}(X') ⟶ X' ⟶ X` is the blowup of
> `X` in `Y`, over `X`.
>
> The centre is the product `I · J` of `I` with the second-centre ideal that
> `Stacks.Blowup.exists_secondCentre` produces from `Z'`.

```lean
theorem exists_centre_supportSet_eq_and_nonempty_blowUpCompositionIso
    [CompactSpace X] [QuasiSeparatedSpace X] (I : X.IdealSheafData)
    (hI : FinitePresentation I.subschemeι) (Z' : (blowUp I).IdealSheafData)
    (hfp : FinitePresentation Z'.subschemeι) :
    ∃ Y : X.IdealSheafData, FinitePresentation Y.subschemeι ∧
      Y.supportSet = I.supportSet ∪ (blowUpToBase I).base '' Z'.supportSet ∧
        Nonempty (Over.mk (blowUpToBase Z' ≫ blowUpToBase I) ≅ Over.mk (blowUpToBase Y))
```

**`AlgebraicGeometry.exists_centre_supportSet_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentreExistence.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentreExistence.lean#L90). The attribute's comment: “part (1), the support of the centre”.

> **The support of the centre of [Stacks, Tag 080B].** There is a finitely presented centre
> `Y` on `X` with `Supp Y = Supp I ∪ b(Supp Z')`.

```lean
theorem exists_centre_supportSet_eq [CompactSpace X] [QuasiSeparatedSpace X]
    (I : X.IdealSheafData) (hI : FinitePresentation I.subschemeι)
    (Z' : (blowUp I).IdealSheafData) (hfp : FinitePresentation Z'.subschemeι) :
    ∃ Y : X.IdealSheafData, FinitePresentation Y.subschemeι ∧
      Y.supportSet = I.supportSet ∪ (blowUpToBase I).base '' Z'.supportSet
```

**`AlgebraicGeometry.exists_centre_nonempty_blowUpCompositionIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentreExistence.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Blowup/CompositeCentreExistence.lean#L103). The attribute's comment: “part (2), the composite of the two blowups is the blowup in the centre”.

> **The composite of two blowups is a blowup, [Stacks, Tag 080B].** There is a finitely
> presented centre `Y` on `X` for which blowing `X` up in `Y` is the two-step blowup
> `Bl_{Z'}(X') ⟶ X' ⟶ X`, over `X`.

```lean
theorem exists_centre_nonempty_blowUpCompositionIso [CompactSpace X] [QuasiSeparatedSpace X]
    (I : X.IdealSheafData) (hI : FinitePresentation I.subschemeι)
    (Z' : (blowUp I).IdealSheafData) (hfp : FinitePresentation Z'.subschemeι) :
    ∃ Y : X.IdealSheafData, FinitePresentation Y.subschemeι ∧
      Nonempty (Over.mk (blowUpToBase Z' ≫ blowUpToBase I) ≅ Over.mk (blowUpToBase Y))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.33, Tag 01OF](https://stacks.math.columbia.edu/tag/01OF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
