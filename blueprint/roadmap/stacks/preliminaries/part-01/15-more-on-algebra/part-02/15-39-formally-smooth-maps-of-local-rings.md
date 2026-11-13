---
declaration: section
origin: cited
lean: formallySmooth_adic_iff_lifts_local_squareZero, isRegularLocalRing_of_isFormallySmooth_maximalIdeal, RingHom.FormallySmoothTop.isRegularLocalRing_of_maximalIdeal, exists_residueField_algHom_section, exists_algEquiv_mvPowerSeries_residueField, isFormallySmooth_maximalIdeal_of_isRegularLocalRing, smoothAt_iff_formallySmoothNAdic_localization
statement: formalized
proof: formalized
---

# 15.39 Formally smooth maps of local rings

Section 15.39 of the Stacks Project, [Tag 0DYF](https://stacks.math.columbia.edu/tag/0DYF). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DYG, a lemma

[Tag 0DYG](https://stacks.math.columbia.edu/tag/0DYG) in the Stacks Project.

**`formallySmooth_adic_iff_lifts_local_squareZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/LocalRings/LiftingCriterion.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/LocalRings/LiftingCriterion.lean#L480). References: EGA 0 (22.1.4); SGA 1 III (2.2), “(iv ter)”; SGA 1 III (2.1), “(i) ⇔ (iv bis)”.

> A local homomorphism of local rings is formally smooth for the adic
> topologies if and only if it lifts through all residually trivial square-zero quotients whose
> source has nilpotent maximal ideal. If the target is Noetherian, testing residually trivial
> small extensions suffices.

```lean
public theorem formallySmooth_adic_iff_lifts_local_squareZero
    {R : Type v} {S : Type w} [CommRing R] [IsLocalRing R]
    [CommRing S] [IsLocalRing S] (φ : R →+* S) [IsLocalHom φ] :
    (FormallySmoothAdic.{u, v, w} φ ↔ LiftsLocalSquareZero.{u, v, w} φ) ∧
      (IsNoetherianRing S →
        (FormallySmoothAdic.{u, v, w} φ ↔ LiftsLocalSmallExtension.{u, v, w} φ))
```

## Tag 07EI, a lemma

[Tag 07EI](https://stacks.math.columbia.edu/tag/07EI) in the Stacks Project.

**`isRegularLocalRing_of_isFormallySmooth_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean#L199). References: EGA 0 (19.6.5), “A regular (k'=k)”; EGA 0 (22.5.8), “a) ⇒ A regular”.

> A Noetherian local algebra over a field that is formally smooth for its
> maximal-ideal adic topology is a regular local ring.

```lean
public theorem isRegularLocalRing_of_isFormallySmooth_maximalIdeal.{v, w}
    {k : Type v} {A : Type w} [Field k] [CommRing A] [Algebra k A]
    [IsLocalRing A] [IsNoetherianRing A]
    (h : FormallySmoothDiscreteMaximalIdeal.{max v w, v, w} (algebraMap k A)) :
    IsRegularLocalRing A
```

**`RingHom.FormallySmoothTop.isRegularLocalRing_of_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/RegularLocal.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/RegularLocal.lean#L368). References: EGA 0 (19.6.5), “A regular (k'=k)”; EGA 0 (22.5.8), “a) ⇒ A regular”.

> A Noetherian local algebra over a field is regular if its structure map
> is formally smooth for the maximal-ideal adic topology.

```lean
theorem isRegularLocalRing_of_maximalIdeal.{v, w}
    {k : Type v} {A : Type w} [Field k] [CommRing A] [Algebra k A]
    [IsLocalRing A] [IsNoetherianRing A]
    (h :
      let m := IsLocalRing.maximalIdeal A
      let : TopologicalSpace k := ⊥
      let : DiscreteTopology k := ⟨rfl⟩
      let : TopologicalSpace A := m.adicTopology
      let : IsTopologicalRing A := m.ringFilterBasis.isTopologicalRing
      let : IsLinearTopology A A := m.isLinearTopology
      RingHom.FormallySmoothTop.{max v w} (algebraMap k A)) :
    IsRegularLocalRing A
```

## Tag 0C34, a lemma

[Tag 0C34](https://stacks.math.columbia.edu/tag/0C34) in the Stacks Project.

**`exists_residueField_algHom_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean#L106). References: EGA 0 (19.5.4.4), “special case”.

> A complete local algebra over a field whose residue field is separable over the
> base field has a coefficient field: the residue homomorphism has a section by an
> algebra homomorphism.

```lean
public theorem exists_residueField_algHom_section
    {k : Type*} {A : Type*} [Field k] [CommRing A] [IsLocalRing A] [Algebra k A]
    [IsAdicComplete (IsLocalRing.maximalIdeal A) A]
    (hsep : Algebra.IsSeparableExtension k (IsLocalRing.ResidueField A)) :
    ∃ σ : IsLocalRing.ResidueField A →ₐ[k] A,
      (Ideal.Quotient.mkₐ k (IsLocalRing.maximalIdeal A)).comp σ =
        AlgHom.id k (IsLocalRing.ResidueField A)
```

## Tag 0C35, a lemma

[Tag 0C35](https://stacks.math.columbia.edu/tag/0C35) in the Stacks Project.

**`exists_algEquiv_mvPowerSeries_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean#L144). References: EGA 0 (19.6.4), “special case”; EGA 0 (19.8.8), “(i), special case”; EGA 0 (21.9.2), “special case”; SGA 1 II (5.6), “(iii)”.

> A complete regular local algebra over a field whose residue field is separable over
> the base field is isomorphic, as an algebra over that field, to a multivariable formal
> power series ring over its residue field.

```lean
public theorem exists_algEquiv_mvPowerSeries_residueField
    {k : Type u} {A : Type v} [Field k] [CommRing A] [Algebra k A]
    [IsRegularLocalRing A] [IsAdicComplete (IsLocalRing.maximalIdeal A) A]
    (hsep : Algebra.IsSeparableExtension k (IsLocalRing.ResidueField A)) :
    Nonempty
      (A ≃ₐ[k] MvPowerSeries
        (Fin (Module.finrank (IsLocalRing.ResidueField A) (IsLocalRing.CotangentSpace A)))
        (IsLocalRing.ResidueField A))
```

## Tag 07EJ, a lemma

[Tag 07EJ](https://stacks.math.columbia.edu/tag/07EJ) in the Stacks Project.

**`isFormallySmooth_maximalIdeal_of_isRegularLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean#L565).

> A regular local algebra over a field whose residue field is separable over
> the base field is formally smooth for its maximal-ideal adic topology.

```lean
public theorem isFormallySmooth_maximalIdeal_of_isRegularLocalRing.{u, v, w}
    {k : Type v} {A : Type w} [Field k] [CommRing A] [Algebra k A]
    [IsRegularLocalRing A]
    (hsep : Algebra.IsSeparableExtension k (IsLocalRing.ResidueField A)) :
    FormallySmoothDiscreteMaximalIdeal.{u, v, w} (algebraMap k A)
```

## Tag 07VH, a lemma

[Tag 07VH](https://stacks.math.columbia.edu/tag/07VH) in the Stacks Project.

**`smoothAt_iff_formallySmoothNAdic_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean, line 671](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FormallySmooth/LocalRings/CoefficientFieldsAndRegularity.lean#L671). References: EGA 0 (22.6.4), “c) <=> d)”; EGA IV (6.8.6), “a) ⇔ c)”; EGA IV (17.5.3), “a) ⇔ d)”; SGA 1 III (1.9), “Noetherian A”.

> Let `A → B` be a finite type map with `A` Noetherian, and let the prime
> `q ⊆ B` lie over the prime `p ⊆ A`. Then the map is smooth at `q` if and
> only if the canonical local map `A_p → B_q` is formally smooth for the
> maximal-ideal-adic topology on `B_q`.

```lean
public theorem smoothAt_iff_formallySmoothNAdic_localization.{u, v}
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing A] [Algebra.FiniteType A B]
    (p : Ideal A) (q : Ideal B) [p.IsPrime] [q.IsPrime] [q.LiesOver p] :
    Algebra.SmoothAt A B q ↔
      RingHom.FormallySmoothNAdic.{max u v, u, v}
        (@algebraMap (Localization.AtPrime p) (Localization.AtPrime q) _ _
          (Localization.AtPrime.algebraOfLiesOver p q))
        (maximalIdeal (Localization.AtPrime q))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.39, Tag 0DYF](https://stacks.math.columbia.edu/tag/0DYF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
