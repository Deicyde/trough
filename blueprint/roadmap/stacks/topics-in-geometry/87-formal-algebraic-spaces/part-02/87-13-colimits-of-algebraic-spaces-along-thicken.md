---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_isRepresentableThickeningULift, PadicComplexInt.isWeakIdealOfDefinition_maximalIdeal_and_not_isIdealOfDefinition, PadicComplexInt.isIdealOfDefinition_span_p, AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isWeakIdealOfDefinition_maximalIdeal, AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isWeaklyAdmissible, AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isAffineFormalAlgebraicSpace_formalSpectrum, AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isRelativelyRepresentable_residueField, AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isThickening_residueField
statement: formalized
proof: formalized
---

# 87.13 Colimits of algebraic spaces along thickenings

Section 87.13 of the Stacks Project, [Tag 0AIT](https://stacks.math.columbia.edu/tag/0AIT). 4 tags here are carried by 72 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AIU, a lemma

[Tag 0AIU](https://stacks.math.columbia.edu/tag/0AIU) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_isRepresentableThickeningULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ColimitOfAlgebraicSpaceThickenings.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ColimitOfAlgebraicSpaceThickenings.lean#L78). The attribute's comment: “corrected form (errata.md, 2026-10-27, entry 0GVM, 0AIU): the printed statement is false, since for an index set large compared with the site the colimit admits no surjection from an object of the site, so it fails the set-theoretic condition of Stacks 0AIS that Definition 0AIM includes in being a formal algebraic space (AlgebraicGeometry.FormalSpace.not\_forall\_isFormalAlgebraicSpace\_colimit\_thickenings). The correction adds exactly that clause of the conclusion to the hypotheses, for a sheaf isomorphic to the colimit; the source's other hypotheses are unchanged and its charts are constructed in the proof”.

> **Stacks 0AIU, corrected.** Let `E` be a directed system of algebraic spaces over `S` whose
> transition morphisms are representable thickenings. A sheaf `Z` isomorphic to `colim E` which
> satisfies the set-theoretic condition of Stacks 0AIS is a formal algebraic space over `S`.
>
> The set-theoretic condition cannot be dropped: without it the statement is false
> (`AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_colimit_thickenings`).

```lean
theorem isFormalAlgebraicSpace_of_colimit_isRepresentableThickeningULift
    (Λ : Type (u + 1)) [Preorder Λ] [Nonempty Λ] [IsDirected Λ (· ≤ ·)]
    (E : Λ ⥤ FppfSheaf B S hS)
    (halg : ∀ i : Λ, Space.IsAlgebraicSpaceULift.{u + 1} B S hS (E.obj i).obj)
    (hthick : ∀ ⦃i j : Λ⦄ (g : i ⟶ j),
      Space.IsRepresentableThickeningULift.{u + 1} B S hS (E.map g).hom)
    (Z : FppfSheaf B S hS) (hZset : SatisfiesSetTheoreticCondition B S hS Z)
    (hZ : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Nonempty (Z ≅ colimit E)) :
    IsFormalAlgebraicSpace B S hS Z
```

## Tag 0CB8, an example

[Tag 0CB8](https://stacks.math.columbia.edu/tag/0CB8) in the Stacks Project.

**`PadicComplexInt.isWeakIdealOfDefinition_maximalIdeal_and_not_isIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean#L127). The attribute's comment: “a weak ideal of definition that is not an ideal of definition, on the ring of integers of ℂ\_[p]”.

> **Stacks 0AIW**, the negative clause on the example of Stacks 0CB8. The maximal ideal of the
> ring of integers of the field `ℂ_[p]` of `p`-adic complex numbers is a weak ideal of definition
> of that admissible topological ring, and it is not an ideal of definition. So the two notions
> differ, and the correspondence of Stacks 0AIV between weak ideals of definition and thickenings
> cannot restrict to one between ideals of definition and thickenings.

```lean
theorem isWeakIdealOfDefinition_maximalIdeal_and_not_isIdealOfDefinition :
    TopologicalRing.IsWeakIdealOfDefinition (maximalIdeal (PadicComplexInt p)) ∧
      ¬ TopologicalRing.IsIdealOfDefinition (maximalIdeal (PadicComplexInt p))
```

**`PadicComplexInt.isIdealOfDefinition_span_p`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean#L162). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The ideal `(p)` is an ideal of definition of the ring of integers of
> `ℂ_[p]`: its topology is the `(p)`-adic one.

```lean
theorem isIdealOfDefinition_span_p :
    TopologicalRing.IsIdealOfDefinition
      (Ideal.span ({(p : PadicComplexInt p)} : Set (PadicComplexInt p)))
```

**`AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isWeakIdealOfDefinition_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean#L233). The attribute's comment: “a weak ideal of definition that is not an ideal of definition”.

> **Stacks 0CB8.** In a local ring whose topology is `(π)`-adic, with the radical of `(π)` the
> maximal ideal, the maximal ideal is a weak ideal of definition: it is open, and each of its
> elements lies in the radical of `(π)`, hence is topologically nilpotent.

```lean
theorem isWeakIdealOfDefinition_maximalIdeal
    (hadic : IsAdic (Ideal.span ({π} : Set A)))
    (hrad : (Ideal.span ({π} : Set A)).radical = maximalIdeal A) :
    TopologicalRing.IsWeakIdealOfDefinition (maximalIdeal A)
```

**`AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isWeaklyAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean#L245). The attribute's comment: “a weak ideal of definition that is not an ideal of definition”.

> **Stacks 0CB8.** A complete local ring whose topology is `(π)`-adic, with the radical of
> `(π)` the maximal ideal, is weakly admissible: the maximal ideal is a weak ideal of
> definition.

```lean
theorem isWeaklyAdmissible
    (hadic : IsAdic (Ideal.span ({π} : Set A)))
    (hcomplete : TopologicalRing.IsComplete A)
    (hrad : (Ideal.span ({π} : Set A)).radical = maximalIdeal A) :
    TopologicalRing.IsWeaklyAdmissible A
```

**`AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isAffineFormalAlgebraicSpace_formalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean#L307). The attribute's comment: “a weak ideal of definition that is not an ideal of definition”.

> **Stacks 0CB8.** A complete local ring whose topology is `(π)`-adic, with the radical of
> `(π)` the maximal ideal, has an affine formal algebraic space as formal spectrum, with no
> hypothesis on the chosen big fppf site beyond its containing the quotient spectra.
>
> Completeness and the radical identity are part of the situation of the example but are not
> needed for this particular conclusion, which holds for any adic topology; their names are
> therefore prefixed by an underscore.

```lean
theorem isAffineFormalAlgebraicSpace_formalSpectrum
    (hadic : IsAdic (Ideal.span ({π} : Set A)))
    (_hcomplete : TopologicalRing.IsComplete A)
    (_hrad : (Ideal.span ({π} : Set A)).radical = maximalIdeal A)
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    (D : QuotientSystem B S hS A) :
    IsAffineFormalAlgebraicSpace B S hS (formalSpectrum D)
```

**`AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isRelativelyRepresentable_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean#L378). The attribute's comment: “a weak ideal of definition that is not an ideal of definition”.

> **Stacks 0CB8.** The residue-field stage `Spec κ ⟶ Spf A` of the formal spectrum, that is
> the colimit cocone map at the weak ideal of definition `𝔪`, is representable by objects of the
> big fppf site.

```lean
theorem isRelativelyRepresentable_residueField
    (hadic : IsAdic (Ideal.span ({π} : Set A)))
    (hrad : (Ideal.span ({π} : Set A)).radical = maximalIdeal A)
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    (D : QuotientSystem B S hS A) :
    let J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I } :=
      ⟨maximalIdeal A, isWeakIdealOfDefinition_maximalIdeal π hadic hrad⟩
    (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).relativelyRepresentable
      (formalSpectrumInclusion D (OrderDual.toDual J))
```

**`AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isThickening_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean#L394). The attribute's comment: “a weak ideal of definition that is not an ideal of definition”.

> **Stacks 0CB8.** The residue-field stage `Spec κ ⟶ Spf A` of the formal spectrum is a
> thickening: each of its base changes along a morphism from a represented sheaf is a thickening
> of schemes.

```lean
theorem isThickening_residueField
    (hadic : IsAdic (Ideal.span ({π} : Set A)))
    (hrad : (Ideal.span ({π} : Set A)).radical = maximalIdeal A)
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    (D : QuotientSystem B S hS A) :
    let J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I } :=
      ⟨maximalIdeal A, isWeakIdealOfDefinition_maximalIdeal π hadic hrad⟩
    (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)))
      (formalSpectrumInclusion D (OrderDual.toDual J))
```

**`AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.not_isIdealOfDefinition_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/WeakIdealOfDefinitionExample.lean#L416). The attribute's comment: “a weak ideal of definition that is not an ideal of definition”.

> **Stacks 0CB8.** In a valuation ring whose topology is `(π)`-adic for some `π` in the
> maximal ideal, the maximal ideal is not an ideal of definition if it is not finitely generated:
> it is then idempotent, so all its powers coincide and cofinality of those powers would force
> `𝔪 = (π)` to be principal.

```lean
theorem not_isIdealOfDefinition_maximalIdeal
    [IsDomain A] (hval : IsValuationRing A) (hπm : π ∈ maximalIdeal A)
    (hadic : IsAdic (Ideal.span ({π} : Set A)))
    (hnotfg : ¬ (maximalIdeal A).FG) :
    ¬ TopologicalRing.IsIdealOfDefinition (maximalIdeal A)
```

**`rationalPolynomial`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L62). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** Finite sums `∑ a_α t^α` with `α` ranging over nonnegative rationals,
> realised as the monoid algebra of `ℚ≥0` over `k`.

```lean
abbrev rationalPolynomial (k : Type*) [CommRing k]
```

**`polynomialT`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L66). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The monomial `t = t^1` in `rationalPolynomial k`.

```lean
def polynomialT (k : Type*) [CommRing k] : rationalPolynomial k
```

**`polynomialTIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L71). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The principal ideal `(t)` of `rationalPolynomial k`.

```lean
def polynomialTIdeal (k : Type*) [CommRing k] : Ideal (rationalPolynomial k)
```

**`rationalPowerSeries`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L77). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The ring of power series with nonnegative rational exponents over `k`,
> constructed as the `(t)`-adic completion of `rationalPolynomial k`.

```lean
abbrev rationalPowerSeries (k : Type*) [CommRing k]
```

**`CoefficientFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L83). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** Coefficient families `(a_α)_{α ∈ ℚ≥0}` in `k` having, for every natural
> number `n`, only finitely many nonzero entries with `α ≤ n`.

```lean
def CoefficientFamily (k : Type*) [Zero k]
```

**`coefficientRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L90). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The subring of `HahnSeries ℚ≥0 k` generated by the series whose support
> is finite below every integer bound. `RationalPowerSeries.mem_coefficientRing_iff` shows that
> the generating set is already a subring, so this is exactly the displayed ring of series.

```lean
def coefficientRing (k : Type*) [CommRing k] : Subring (HahnSeries ℚ≥0 k)
```

**`RationalPowerSeries.t`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L98). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The element `π = t` of `rationalPowerSeries k`, the image of the
> exponent-one monomial under the completion map.

```lean
def t (k : Type*) [CommRing k] : rationalPowerSeries k
```

**`RationalPowerSeries.tIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L104). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The principal ideal `(t)` of `rationalPowerSeries k`, whose powers
> define the topology.

```lean
def tIdeal (k : Type*) [CommRing k] : Ideal (rationalPowerSeries k)
```

**`RationalPowerSeries.mem_coefficientRing_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CoefficientRing.lean#L248). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** Membership in `coefficientRing k` is precisely local finiteness of the
> support below every integer bound; in particular the generating set of `coefficientRing k` is
> already a subring.

```lean
theorem mem_coefficientRing_iff (k : Type*) [Field k] (f : HahnSeries ℚ≥0 k) :
    f ∈ coefficientRing k ↔
      ∀ n : ℕ, {q : ℚ≥0 | q ≤ n ∧ f.coeff q ≠ 0}.Finite
```

**`RationalPowerSeries.exists_equiv_coefficientFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CompletionEquiv.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CompletionEquiv.lean#L552). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** Every coefficient family `(a_α)` is represented by a unique element of
> the coefficient ring, with unchanged coefficients.

```lean
theorem exists_equiv_coefficientFamily (k : Type*) [Field k] :
    ∃ e : CoefficientFamily k ≃ coefficientRing k,
      ∀ f : CoefficientFamily k, ∀ q : ℚ≥0, ((e f).1).coeff q = f.1 q
```

**`RationalPowerSeries.exists_ringEquiv_coefficientRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CompletionEquiv.lean, line 607](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/CompletionEquiv.lean#L607). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The completed monoid algebra is the ring of locally finite coefficient
> series, with the usual addition and convolution multiplication; the isomorphism preserves the
> coefficients of polynomials.

```lean
theorem exists_ringEquiv_coefficientRing (k : Type*) [Field k] :
    ∃ e : rationalPowerSeries k ≃+* coefficientRing k,
      ∀ (p : rationalPolynomial k) (q : ℚ≥0),
        ((e (AdicCompletion.of (polynomialTIdeal k) (rationalPolynomial k) p)).1).coeff q =
          p.coeff q
```

**`RationalPowerSeries.isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L39). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The ring of power series with nonnegative rational exponents is a
> domain.

```lean
theorem isDomain (k : Type*) [Field k] : IsDomain (rationalPowerSeries k)
```

**`RationalPowerSeries.instIsDomain`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L52). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The ring of power series with nonnegative rational exponents is a
> domain.

```lean
instance instIsDomain (k : Type*) [Field k] : IsDomain (rationalPowerSeries k)
```

**`RationalPowerSeries.isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L58). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The ring of power series with nonnegative rational exponents is
> local.

```lean
theorem isLocalRing (k : Type*) [Field k] : IsLocalRing (rationalPowerSeries k)
```

**`RationalPowerSeries.instIsLocalRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L66). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The ring of power series with nonnegative rational exponents is
> local.

```lean
instance instIsLocalRing (k : Type*) [Field k] : IsLocalRing (rationalPowerSeries k)
```

**`RationalPowerSeries.isValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L72). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** This local domain is a valuation ring: inside its fraction field it is
> maximal for the domination order among local subrings.

```lean
theorem isValuationRing (k : Type*) [Field k] :
    IsValuationRing (rationalPowerSeries k)
```

**`RationalPowerSeries.t_mem_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L83). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The monomial `t` lies in the maximal ideal; in particular it is not a
> unit.

```lean
theorem t_mem_maximalIdeal (k : Type*) [Field k] :
    t k ∈ IsLocalRing.maximalIdeal (rationalPowerSeries k)
```

**`RationalPowerSeries.isAdic_span_t`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L94). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The topology of `rationalPowerSeries k` is the `(t)`-adic topology.

```lean
theorem isAdic_span_t (k : Type*) [Field k] :
    IsAdic (Ideal.span ({t k} : Set (rationalPowerSeries k)))
```

**`RationalPowerSeries.isComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L100). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The ring of power series with nonnegative rational exponents is
> separated and complete for its `(t)`-adic topology.

```lean
theorem isComplete (k : Type*) [Field k] :
    TopologicalRing.IsComplete (rationalPowerSeries k)
```

**`RationalPowerSeries.radical_span_t`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L133). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The radical of `(t)` is the maximal ideal: every non-unit has positive
> order, so some power of it is divisible by `t`.

```lean
theorem radical_span_t (k : Type*) [Field k] :
    (Ideal.span ({t k} : Set (rationalPowerSeries k))).radical =
      IsLocalRing.maximalIdeal (rationalPowerSeries k)
```

**`RationalPowerSeries.not_fg_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/RationalPowerSeries/ValuationRing.lean#L205). The attribute's comment: “the rational power series valuation ring”.

> **Stacks 0CB8.** The maximal ideal is not finitely generated: finitely many elements of
> the maximal ideal have a least positive order `a`, and the monomial of exponent `a / 2` is in
> the maximal ideal but not in the ideal they generate.

```lean
theorem not_fg_maximalIdeal (k : Type*) [Field k] :
    ¬ (IsLocalRing.maximalIdeal (rationalPowerSeries k)).FG
```

**`PadicComplexInt.isAdic_span_p`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean#L93). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The topology of the ring of integers of `ℂ_[p]`, inherited from `ℂ_[p]`, is
> the `(p)`-adic topology.

```lean
theorem isAdic_span_p :
    IsAdic (Ideal.span ({(p : PadicComplexInt p)} : Set (PadicComplexInt p)))
```

**`PadicComplexInt.instIsLinearTopology`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean#L131). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The topology of the ring of integers of `ℂ_[p]` is linear: the open ideals
> form a basis of neighbourhoods of zero.

```lean
instance instIsLinearTopology : IsLinearTopology (PadicComplexInt p) (PadicComplexInt p)
```

**`PadicComplexInt.isComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean#L138). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The ring of integers of `ℂ_[p]` is separated and complete for its
> topology.

```lean
theorem isComplete : TopologicalRing.IsComplete (PadicComplexInt p)
```

**`PadicComplexInt.natCast_mem_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean#L150). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The element `p` of the ring of integers of `ℂ_[p]` lies in its maximal
> ideal; in particular it is nonzero and not a unit.

```lean
theorem natCast_mem_maximalIdeal :
    (p : PadicComplexInt p) ∈ maximalIdeal (PadicComplexInt p)
```

**`PadicComplexInt.radical_span_p`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean#L162). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The radical of the ideal `(p)` of the ring of integers of `ℂ_[p]` is its
> maximal ideal.

```lean
theorem radical_span_p :
    (Ideal.span ({(p : PadicComplexInt p)} : Set (PadicComplexInt p))).radical =
      maximalIdeal (PadicComplexInt p)
```

**`PadicComplexInt.isValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean#L193). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The ring of integers of `ℂ_[p]` is a valuation ring: inside its fraction
> field it is maximal for the domination order among local subrings.

```lean
theorem isValuationRing : IsValuationRing (PadicComplexInt p)
```

**`PadicComplexInt.not_fg_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/PadicComplexInt.lean#L200). The attribute's comment: “the p-adic complex integers”.

> **Stacks 0CB8.** The maximal ideal of the ring of integers of `ℂ_[p]` is not finitely
> generated: the valuation of `ℂ_[p]` takes arbitrarily small positive values, since `ℂ_[p]` is
> algebraically closed, so no element of the maximal ideal generates it.

```lean
theorem not_fg_maximalIdeal : ¬ (maximalIdeal (PadicComplexInt p)).FG
```

## Tag 0AIV, a remark

[Tag 0AIV](https://stacks.math.columbia.edu/tag/0AIV) in the Stacks Project.

**`AlgebraicGeometry.McQuillanFormalScheme.not_forall_isFppfColimitOfThickenings_of_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/TwistedDoubleColimit.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/TwistedDoubleColimit.lean#L90). The attribute's comment: “the statement as printed is false: the if direction, for sectionwise weak ideals of definition, fails for the twisted double, a formal scheme with a fundamental system of (weak) ideals of definition whose functor of points h\_𝔛 is not a colimit of schemes as in Lemma 0AIU (colimit in fppf sheaves); the corrected form is McQuillanFormalScheme.isFppfColimitOfThickenings\_iff\_exists\_isFundamentalSystem”.

> **Stacks 0AIV, the "if" direction as printed, is false.** There is a formal scheme `𝔛` in the
> sense of McQuillan (the twisted double `AlgebraicGeometry.TwistedDouble.𝔛`, a formal scheme à la
> EGA) which has a fundamental system of weak ideals of definition, in the source's sectionwise
> sense, but whose functor of points `h_𝔛` is not a colimit of schemes along thickenings in fppf
> sheaves, as in Stacks 0AIU. On a formal scheme à la EGA the weak affine formal opens are the
> affine formal opens, and a fundamental system of ideals of definition is one of weak ideals of
> definition, so the fundamental system of
> `AlgebraicGeometry.TwistedDouble.exists_isFundamentalSystemOfIdealsOfDefinitionOn` serves.
>
> The corrected form is
> `McQuillanFormalScheme.isFppfColimitOfThickenings_iff_exists_isFundamentalSystem`,
> where the weak ideals of definition are cut out by their sections over the affine formal opens.

```lean
theorem McQuillanFormalScheme.not_forall_isFppfColimitOfThickenings_of_exists :
    ¬ ∀ 𝔛 : McQuillanFormalScheme.{0},
      (∃ 𝒮 : Set (IdealSheaf 𝔛.obj),
        IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsWeakAffineFormalOpen 𝔛.obj)) →
        𝔛.IsFppfColimitOfThickenings
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IdealSheaf.IsWeakIdealOfDefinitionOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinition.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinition.lean#L108). The attribute's comment: “the definition, over a class `𝒜` of affine formal opens”.

> An ideal sheaf on `X` is a *weak ideal of definition* over a class `𝒜` of opens — the
> affine formal open subschemes — when its ideal of sections over every open of `𝒜` is a weak
> ideal of definition of the topological ring of sections there.

```lean
def IsWeakIdealOfDefinitionOn (I : IdealSheaf X) (𝒜 : Opens X → Prop) : Prop
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IsFundamentalSystemOfWeakIdealsOfDefinitionOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinition.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinition.lean#L118). The attribute's comment: “the definition, over a class `𝒜` of affine formal opens”.

> A family of ideal sheaves on `X` is a *fundamental system of weak ideals of definition* over
> a class `𝒜` of opens — the affine formal open subschemes — when each member is a weak ideal of
> definition and, over every open of `𝒜`, their ideals of sections form a neighbourhood basis of
> zero in the topological ring of sections.

```lean
def IsFundamentalSystemOfWeakIdealsOfDefinitionOn {X : LTRS.{u}} (𝒮 : Set (IdealSheaf X))
    (𝒜 : Opens X → Prop) : Prop
```

**`AlgebraicGeometry.McQuillanFormalScheme.isFppfColimitOfThickenings_iff_exists_isFundamentalSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionColimitIff.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionColimitIff.lean#L130). The attribute's comment: “h\_𝔛 is a colimit of schemes along thickenings as in Lemma 0AIU (colimit in fppf sheaves) exactly when there exists a fundamental system of weak ideals of definition, CORRECTED: the weak ideals of definition are those cut out by their sections over the affine formal opens, the ones to which the correspondence ℐ ↦ (𝔛, 𝒪\_𝔛/ℐ) applies (it fails for an arbitrary ideal sheaf)”.

> The functor of points `h_𝔛` of a McQuillan formal scheme is a colimit of schemes along
> thickenings, as in Stacks 0AIU, in fppf sheaves if and only if `𝔛` has a fundamental system of
> weak ideals of definition cut out by their sections over the weakly affine formal opens.

```lean
theorem isFppfColimitOfThickenings_iff_exists_isFundamentalSystem (𝔛 : McQuillanFormalScheme.{u}) :
    𝔛.IsFppfColimitOfThickenings ↔ ∃ 𝒮 : Set (IdealSheaf 𝔛.obj),
      (∀ I ∈ 𝒮, I.IsCutOutOn (IsWeakAffineFormalOpen 𝔛.obj)) ∧
        IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsWeakAffineFormalOpen 𝔛.obj)
```

**`AlgebraicGeometry.McQuillanFormalScheme.exists_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_isFppfColimitOfThickenings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionColimitOnlyIf.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionColimitOnlyIf.lean#L60). The attribute's comment: “the forward direction of the last sentence, as printed, with no extra hypothesis: if h\_𝔛 is a colimit of schemes along thickenings as in Lemma 0AIU (colimit in fppf sheaves), then there exists a fundamental system of weak ideals of definition for 𝔛, in the sectionwise sense the source defines, with no condition on its members. The converse fails as printed (not\_forall\_isFppfColimitOfThickenings\_of\_exists) and needs the members to be cut out by their sections (isFppfColimitOfThickenings\_iff\_exists\_isFundamentalSystem)”.

> If the functor of points `h_𝔛` of a formal scheme `𝔛` in the sense of McQuillan is a colimit
> of schemes along thickenings, then there exists a fundamental system of weak ideals of definition
> for `𝔛`: a family of ideal sheaves each of which is a weak ideal of definition over every affine
> formal open, whose ideals of sections form a neighbourhood basis of zero over every affine formal
> open.

```lean
theorem exists_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_isFppfColimitOfThickenings
    (𝔛 : McQuillanFormalScheme.{u}) (h : 𝔛.IsFppfColimitOfThickenings) :
    ∃ 𝒮 : Set (IdealSheaf 𝔛.obj),
      IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsWeakAffineFormalOpen 𝔛.obj)
```

**`AlgebraicGeometry.McQuillanFormalScheme.weakIdealOfDefinitionEquivThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCorrespondence.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCorrespondence.lean#L219). The attribute's comment: “the one-to-one correspondence between weak ideals of definition and thickenings Z → h\_𝔛, CORRECTED: the weak ideals of definition are those cut out by their sections over the affine formal opens (`IdealSheaf.IsCutOutOn`, the formal analogue of quasi-coherence), the printed statement for an arbitrary ideal sheaf being false (`exists_isWeakIdealOfDefinitionOn_forall_thickening_ideal_ne`); a thickening is a scheme Z with a relatively representable morphism h\_Z → h\_𝔛 whose base changes are thickenings of schemes, the functors of points being presheaves on all schemes, and thickenings are taken up to isomorphism over h\_𝔛”.

> **Stacks 0AIV, the one-to-one correspondence between weak ideals of definition and thickenings
> `Z → h_𝔛`.** A weak ideal of definition `ℐ` (cut out by its sections over the weak affine formal
> opens) goes to the thickening `(𝔛, 𝒪_𝔛/ℐ) → h_𝔛`, and a thickening goes to its kernel ideal sheaf;
> the thickenings are taken up to isomorphism over `h_𝔛`.

```lean
noncomputable def weakIdealOfDefinitionEquivThickening :
    𝔛.WeakIdealOfDefinition ≃ Quotient (Thickening.setoid (𝔛 := 𝔛))
```

**`AlgebraicGeometry.McQuillanFormalScheme.ker_quotientPoint_and_existsUnique_factor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCorrespondence.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCorrespondence.lean#L245). The attribute's comment: “the correspondence associates to ℐ the scheme Z = (𝔛, 𝒪\_𝔛/ℐ) with the obvious morphism to 𝔛: its kernel is ℐ and the points of 𝔛 killing ℐ are those factoring through it”.

> **Stacks 0AIV: the thickening attached to `ℐ` is `(𝔛, 𝒪_𝔛/ℐ)` with its obvious morphism to
> `𝔛`.** The morphism `Z → 𝔛` of locally topologically ringed spaces underlying the thickening has
> kernel ideal sheaf `ℐ`, and a point `T → 𝔛` of a scheme factors through it, uniquely, exactly when
> it kills `ℐ`: `Z` is the closed subspace of `𝔛` cut out by `ℐ`.

```lean
theorem ker_quotientPoint_and_existsUnique_factor (I : 𝔛.WeakIdealOfDefinition) :
    IdealSheaf.ker I.thickening.point = I.1 ∧
      ∀ {T : Scheme.{u}} (f : schemeToLTRSObj T ⟶ 𝔛.obj),
        I.1.Kills f ↔ ∃! k : T ⟶ I.thickening.scheme, schemeToLTRS.map k ≫ I.thickening.point = f
```

**`AlgebraicGeometry.McQuillanFormalScheme.exists_isWeakIdealOfDefinitionOn_forall_thickening_ideal_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCorrespondence.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCorrespondence.lean#L259). The attribute's comment: “the printed correspondence, for an arbitrary ideal sheaf, is false: a weak ideal of definition which is the kernel of no thickening”.

> **Without the cut-out condition the correspondence of Stacks 0AIV fails.** There is a McQuillan
> formal scheme — the pseudo-discretisation of the spectrum of the dual numbers over the `2`-adic
> integers — with a weak ideal of definition which is the kernel ideal sheaf of no thickening
> `Z → h_𝔛`: kernels of thickenings are cut out by their sections over the affine formal opens, and
> this ideal sheaf is not.

```lean
theorem exists_isWeakIdealOfDefinitionOn_forall_thickening_ideal_ne :
    ∃ (𝔛 : McQuillanFormalScheme.{0}) (I : IdealSheaf 𝔛.obj),
      I.IsWeakIdealOfDefinitionOn (IsWeakAffineFormalOpen 𝔛.obj) ∧
        ∀ Z : 𝔛.Thickening, Z.ideal ≠ I
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IdealSheaf.exists_not_isWeakIdealOfDefinitionOn_of_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCoverCounterexample.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCoverCounterexample.lean#L200). The attribute's comment: “the statement as printed is false: checking the weak ideal-of-definition condition on the members of an affine open covering does not suffice, already for Spec of the dual numbers over the 2-adic integers covered by itself, with the ideal sheaf of sections vanishing at the closed point; the corrected form is IdealSheaf.isWeakIdealOfDefinitionOn\_of\_cover\_of\_isMcQuillanFormalScheme”.

> **Stacks 0AIV is false as printed: the weak ideal of definition condition cannot be checked on
> the members of an affine open covering.** There is a McQuillan formal scheme `X` whose whole space
> is a weak affine formal open, with an ideal sheaf `ℐ` such that `ℐ(X)` is a weak ideal of
> definition, while `ℐ` is not a weak ideal of definition over every weak affine formal open. The
> witness is the spectrum of the dual numbers `ℤ₂[ε]` over the `2`-adic integers, pseudo-discretised,
> with the ideal sheaf of sections vanishing at the closed point; here `t = 2` lies in the maximal
> ideal and `2ⁿ ε ≠ 0` for every `n`.

```lean
theorem exists_not_isWeakIdealOfDefinitionOn_of_cover :
    ∃ (X : LTRS.{0}) (_ : IsMcQuillanFormalScheme X) (I : IdealSheaf X),
      IsWeakAffineFormalOpen X ⊤ ∧ TopologicalRing.IsWeakIdealOfDefinition (I.ideal ⊤) ∧
        ¬ I.IsWeakIdealOfDefinitionOn (IsWeakAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.not_forall_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCoverCounterexample.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCoverCounterexample.lean#L248). The attribute's comment: “the statement as printed is false: checking the fundamental-system condition on the members of an affine open covering does not suffice, already for a one-member family on Spec of the dual numbers over the 2-adic integers covered by itself, with the ideal sheaf of sections vanishing at the closed point; the corrected form is isFundamentalSystemOfWeakIdealsOfDefinitionOn\_of\_cover\_of\_isMcQuillanFormalScheme”.

> **Stacks 0AIV, the locality of the fundamental-system condition, is false as printed.** It is
> not true that a family of ideal sheaves on a formal scheme in the sense of McQuillan is a
> fundamental system of weak ideals of definition as soon as, over the members of an affine open
> covering, its members are weak ideals of definition whose ideals of sections form a
> neighbourhood basis of zero, even for a nonempty family directed by inclusion. The witness is
> the one-member family `{ℐ}` of `IdealSheaf.exists_not_isWeakIdealOfDefinitionOn_of_cover`, on
> the pseudo-discretised spectrum of the dual numbers `ℤ₂[ε]` covered by itself: `ℐ(X) = 0` is a
> weak ideal of definition and a neighbourhood of zero of the discrete ring `𝒪_X(X)`, but `ℐ` is
> not a weak ideal of definition over the affine open `D(2)`.
>
> The corrected statement checks the condition on the affine formal opens contained in the members
> of the covering:
> `isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover_of_isMcQuillanFormalScheme`.

```lean
theorem not_forall_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover :
    ¬ ∀ (X : LTRS.{0}), IsMcQuillanFormalScheme X → ∀ (𝒮 : Set (IdealSheaf X))
      (𝒰 : Set (Opens X)), 𝒮.Nonempty →
      (∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
        K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W) →
      (∀ V ∈ 𝒰, IsWeakAffineFormalOpen X V) → sSup 𝒰 = ⊤ →
      (∀ I ∈ 𝒮, ∀ V ∈ 𝒰, TopologicalRing.IsWeakIdealOfDefinition (I.ideal V)) →
      (∀ V ∈ 𝒰, (nhds (0 : (X.presheaf.obj (op V)).α)).HasBasis (· ∈ 𝒮)
        fun I : IdealSheaf X => (I.ideal V : Set (X.presheaf.obj (op V)).α)) →
      IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsWeakAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.not_forall_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_hasBasis_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCoverCounterexample.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCoverCounterexample.lean#L315). The attribute's comment: “the statement as printed is false, also on the reading where the members are weak ideals of definition everywhere and the neighbourhood-basis property alone is checked on the members of an affine open covering: already for one weak ideal of definition on the pseudo-discretised Spec(Z[X\_0, X\_1, ...]/(X\_k^(k+1))) covered by itself; the corrected form is isFundamentalSystemOfWeakIdealsOfDefinitionOn\_of\_cover\_of\_isMcQuillanFormalScheme”.

> **Stacks 0AIV, the locality of the fundamental-system condition, is false as printed, also when
> only the neighbourhood-basis half is checked on the covering.** It is not true that a family of
> weak ideals of definition (over every affine formal open) on a formal scheme in the sense of
> McQuillan is a fundamental system as soon as its ideals of sections form a neighbourhood basis of
> zero over the members of an affine open covering, even for a nonempty family directed by
> inclusion. The witness is that of
> `not_forall_isFundamentalSystemOfIdealsOfDefinitionOn_of_hasBasis_cover` for Stacks 0AIW: on the
> pseudo-discretisation of `Spec (ℤ[X₀, X₁, …] / (X_k ^ (k + 1)))`, a McQuillan formal scheme, the
> sections whose germs are multiples of the germ of `X₁`, vanishing outside `D(n!)`, form an ideal
> of definition, hence a weak one, over every quasi-compact open; it is zero over the whole space,
> which is affine and has discrete sections, but its sections over `D(n!)`, which are discrete,
> contain `X₁ ≠ 0`.
>
> The corrected statement checks the condition on the affine formal opens contained in the members
> of the covering:
> `isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover_of_isMcQuillanFormalScheme`.

```lean
theorem not_forall_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_hasBasis_cover :
    ¬ ∀ (X : LTRS.{0}), IsMcQuillanFormalScheme X → ∀ (𝒮 : Set (IdealSheaf X))
      (𝒰 : Set (Opens X)), 𝒮.Nonempty →
      (∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
        K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W) →
      (∀ V ∈ 𝒰, IsWeakAffineFormalOpen X V) → sSup 𝒰 = ⊤ →
      (∀ I ∈ 𝒮, I.IsWeakIdealOfDefinitionOn (IsWeakAffineFormalOpen X)) →
      (∀ V ∈ 𝒰, (nhds (0 : (X.presheaf.obj (op V)).α)).HasBasis (· ∈ 𝒮)
        fun I : IdealSheaf X => (I.ideal V : Set (X.presheaf.obj (op V)).α)) →
      IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsWeakAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IdealSheaf.isWeakIdealOfDefinitionOn_of_cover_of_isCutOutOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCutOutLocality.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCutOutLocality.lean#L250). The attribute's comment: “it suffices to check the weak ideal-of-definition condition on the members of an affine open covering: for ideal sheaves cut out by their sections over the affine formal opens (IdealSheaf.IsCutOutOn), the class of the correspondence with thickenings and of the colimit criterion; for an arbitrary ideal sheaf it is false (IdealSheaf.exists\_not\_isWeakIdealOfDefinitionOn\_of\_cover)”.

> **Stacks 0AIV, the weak ideal-of-definition condition may be checked on the members of an
> affine open covering, for ideal sheaves cut out by their sections.** Let `𝔛` be a formal scheme
> in the sense of McQuillan and `ℐ` an ideal sheaf cut out by its sections over the affine formal
> opens (`IdealSheaf.IsCutOutOn`). If `ℐ(𝔙)` is a weak ideal of definition for the members `𝔙` of a
> covering of `𝔛` by affine formal opens, then `ℐ` is a weak ideal of definition.
>
> These are the ideal sheaves of the correspondence of Stacks 0AIV with thickenings
> (`McQuillanFormalScheme.weakIdealOfDefinitionEquivThickening`) and of its colimit criterion
> (`McQuillanFormalScheme.isFppfColimitOfThickenings_iff_exists_isFundamentalSystem`). For an
> arbitrary ideal sheaf checking the covering members is not enough
> (`IdealSheaf.exists_not_isWeakIdealOfDefinitionOn_of_cover`), and the condition must then be
> checked on the affine formal opens inside the covering members
> (`IdealSheaf.isWeakIdealOfDefinitionOn_of_cover_of_isMcQuillanFormalScheme`). Over an affine formal
> open `𝔚` inside a covering member `𝔙 ≅ Spfw A`, the ideal `ℐ(𝔚)` is the kernel of the quotient
> point `Spec (A/ℐ(𝔙)) → 𝔛` (`IdealSheaf.isWeakIdealOfDefinition_of_le_of_isCutOutOn`).

```lean
theorem IdealSheaf.isWeakIdealOfDefinitionOn_of_cover_of_isCutOutOn
    (hX : IsMcQuillanFormalScheme X) (I : IdealSheaf X)
    (hC : I.IsCutOutOn (IsWeakAffineFormalOpen X)) (𝒰 : Set (Opens X))
    (h𝒰 : ∀ V ∈ 𝒰, IsWeakAffineFormalOpen X V) (hcover : sSup 𝒰 = ⊤)
    (hI : ∀ V ∈ 𝒰, IsWeakIdealOfDefinition (I.ideal V)) :
    I.IsWeakIdealOfDefinitionOn (IsWeakAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover_of_isCutOutOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCutOutLocality.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionCutOutLocality.lean#L280). The attribute's comment: “it suffices to check the fundamental-system condition on the members of an affine open covering: for a family indexed by a directed set, as in the source, of ideal sheaves cut out by their sections over the affine formal opens (IdealSheaf.IsCutOutOn), the class of the colimit criterion; for arbitrary ideal sheaves it is false (not\_forall\_isFundamentalSystemOfWeakIdealsOfDefinitionOn\_of\_hasBasis\_cover)”.

> **Stacks 0AIV, the fundamental-system condition may be checked on the members of an affine
> open covering, for ideal sheaves cut out by their sections.** Let `𝔛` be a formal scheme in the
> sense of McQuillan and `{ℐ_λ}` a nonempty family of ideal sheaves, directed by inclusion, each cut
> out by its sections over the affine formal opens. If over the members `𝔙` of a covering of `𝔛` by
> affine formal opens the `ℐ_λ(𝔙)` are weak ideals of definition forming a neighbourhood basis of
> zero, then `{ℐ_λ}` is a fundamental system of weak ideals of definition.
>
> The family is indexed, as in the source, by a directed set (nonempty, by Stacks' definition of a
> directed set), with `ℐ_μ ⊆ ℐ_λ` for `μ ≥ λ`; this is the directedness asked here. Over an affine
> formal open inside a single covering member no directedness is used
> (`hasBasis_of_le_of_isCutOutOn`); it serves to pass to affine formal opens meeting several members.
> These are the families of the colimit criterion
> `McQuillanFormalScheme.isFppfColimitOfThickenings_iff_exists_isFundamentalSystem`. For arbitrary
> ideal sheaves checking the covering members is not enough
> (`not_forall_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover`,
> `not_forall_isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_hasBasis_cover`).

```lean
theorem isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover_of_isCutOutOn
    (hX : IsMcQuillanFormalScheme X) (𝒮 : Set (IdealSheaf X))
    (hC : ∀ I ∈ 𝒮, I.IsCutOutOn (IsWeakAffineFormalOpen X)) (hne : 𝒮.Nonempty)
    (hdir : ∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
      K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W)
    (𝒰 : Set (Opens X)) (h𝒰 : ∀ V ∈ 𝒰, IsWeakAffineFormalOpen X V) (hcover : sSup 𝒰 = ⊤)
    (h𝒮 : ∀ I ∈ 𝒮, ∀ V ∈ 𝒰, IsWeakIdealOfDefinition (I.ideal V))
    (hbasis : ∀ V ∈ 𝒰, (nhds (0 : (X.presheaf.obj (op V)).α)).HasBasis (· ∈ 𝒮)
      fun I : IdealSheaf X => (I.ideal V : Set (X.presheaf.obj (op V)).α)) :
    IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsWeakAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IdealSheaf.isWeakIdealOfDefinitionOn_of_cover_of_isMcQuillanFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionLocalityMcQuillan.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionLocalityMcQuillan.lean#L65). The attribute's comment: “it suffices to check the weak ideal-of-definition condition on an affine open covering, CORRECTED: on the affine formal opens contained in a covering member, checking the covering members alone being insufficient (`exists_not_isWeakIdealOfDefinitionOn_of_cover`)”.

> An ideal sheaf on a formal scheme `𝔛` in the sense of McQuillan is a weak ideal of definition
> as soon as its ideals of sections over the affine formal opens contained in the members of an open
> covering are weak ideals of definition.

```lean
theorem IdealSheaf.isWeakIdealOfDefinitionOn_of_cover_of_isMcQuillanFormalScheme
    (hX : IsMcQuillanFormalScheme X) (I : IdealSheaf X) (𝒰 : Set (Opens X)) (hcover : sSup 𝒰 = ⊤)
    (hI : ∀ V ∈ 𝒰, ∀ U : Opens X, U ≤ V → IsWeakAffineFormalOpen X U →
      TopologicalRing.IsWeakIdealOfDefinition (I.ideal U)) :
    I.IsWeakIdealOfDefinitionOn (IsWeakAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover_of_isMcQuillanFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionLocalityMcQuillan.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/WeakIdealOfDefinitionLocalityMcQuillan.lean#L81). The attribute's comment: “it suffices to check the fundamental-system condition on an affine open covering, CORRECTED: on the affine formal opens contained in a covering member, checking the covering members alone being insufficient (`exists_not_isWeakIdealOfDefinitionOn_of_cover`), for a nonempty system directed by inclusion”.

> A nonempty family of ideal sheaves on a formal scheme `𝔛` in the sense of McQuillan, directed
> by inclusion, is a fundamental system of weak ideals of definition as soon as, over every affine
> formal open contained in a member of an open covering, its members are weak ideals of definition
> whose ideals of sections form a neighbourhood basis of zero.

```lean
theorem isFundamentalSystemOfWeakIdealsOfDefinitionOn_of_cover_of_isMcQuillanFormalScheme
    (hX : IsMcQuillanFormalScheme X) (𝒮 : Set (IdealSheaf X)) (hne : 𝒮.Nonempty)
    (hdir : ∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
      K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W)
    (𝒰 : Set (Opens X)) (hcover : sSup 𝒰 = ⊤)
    (h𝒮 : ∀ I ∈ 𝒮, ∀ V ∈ 𝒰, ∀ U : Opens X, U ≤ V → IsWeakAffineFormalOpen X U →
      TopologicalRing.IsWeakIdealOfDefinition (I.ideal U))
    (hbasis : ∀ V ∈ 𝒰, ∀ U : Opens X, U ≤ V → IsWeakAffineFormalOpen X U →
      (nhds (0 : (X.presheaf.obj (op U)).α)).HasBasis (· ∈ 𝒮)
        fun I : IdealSheaf X => (I.ideal U : Set (X.presheaf.obj (op U)).α)) :
    IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsWeakAffineFormalOpen X)
```

## Tag 0AIW, a remark

[Tag 0AIW](https://stacks.math.columbia.edu/tag/0AIW) in the Stacks Project.

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IdealSheaf.IsIdealOfDefinitionOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean#L180). The attribute's comment: “the definition, over a class `𝒜` of affine formal opens”.

> An ideal sheaf on `X` is an *ideal of definition* over a class `𝒜` of opens — the affine
> formal open subschemes — when its ideal of sections over every open of `𝒜` is an ideal of
> definition of the topological ring of sections there.

```lean
def IsIdealOfDefinitionOn (I : IdealSheaf X) (𝒜 : Opens X → Prop) : Prop
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IsFundamentalSystemOfIdealsOfDefinitionOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean#L211). The attribute's comment: “the definition, over a class `𝒜` of affine formal opens”.

> A family of ideal sheaves on `X` is a *fundamental system of ideals of definition* over a
> class `𝒜` of opens — the affine formal open subschemes — when each member is an ideal of
> definition and, over every open of `𝒜`, their ideals of sections form a neighbourhood basis of
> zero in the topological ring of sections.

```lean
def IsFundamentalSystemOfIdealsOfDefinitionOn {X : LTRS.{u}} (𝒮 : Set (IdealSheaf X))
    (𝒜 : Opens X → Prop) : Prop
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.exists_isIdealOfDefinition_of_isFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean#L448). The attribute's comment: “`ℐ_λ` is an ideal of definition for `λ` large, on a quasi-compact formal scheme à la EGA, over the members of a finite affine open covering, which is what the source's argument proves; `hdir` and `hne` are the source's directed index set `Λ`. Over every affine formal open the step is false for arbitrary ideal sheaves (erratum in errata.md, `not_forall_exists_isIdealOfDefinitionOn_of_isFundamentalSystemOfWeakIdealsOfDefinitionOn`) and holds for systems cut out by their sections, `exists_forall_isIdealOfDefinitionOn_of_isCutOutOn`”.

> **Stacks 0AIW**, the eventual ideals of definition on a quasi-compact formal scheme à la EGA.
> Here the class of opens is the class of affine formal open subschemes, so the two geometric
> inputs of
> `exists_isIdealOfDefinition_of_isFundamentalSystemOfWeakIdealsOfDefinitionOn` are discharged: the
> affine formal opens cover `X` because `X` is a formal scheme, and the ring of sections over one of
> them is pre-admissible by Stacks 0AHY.

```lean
theorem exists_isIdealOfDefinition_of_isFormalScheme {X : LTRS.{u}} [CompactSpace ↥X]
    (hX : IsFormalScheme X) (𝒮 : Set (IdealSheaf X)) (hne : 𝒮.Nonempty)
    (hdir : ∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
      K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W)
    (hfund : IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X)) :
    ∃ 𝒰 : Set (Opens X), 𝒰.Finite ∧ (∀ V ∈ 𝒰, IsAffineFormalOpen X V) ∧ sSup 𝒰 = ⊤ ∧
      ∃ I₀ ∈ 𝒮, ∀ I ∈ 𝒮, (∀ W : Opens X, I.ideal W ≤ I₀.ideal W) →
        ∀ V ∈ 𝒰, TopologicalRing.IsIdealOfDefinition (I.ideal V)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.exists_isWeakIdealOfDefinitionOn_not_isIdealOfDefinitionOn_of_nilradical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean, line 565](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinition.lean#L565). The attribute's comment: “we do NOT get the same correspondence as in Stacks 0AIV: already on a formal scheme à la EGA the ideal-of-definition condition is strictly stronger than the weak one, witnessed by the nilradical of the pseudo-discretisation of a one-prime scheme whose nilradical is not nilpotent”.

> **Stacks 0AIW**, the separation of the ideal-of-definition condition from the weak one of
> Stacks 0AIV, at the level of ideal sheaves on a formal scheme à la EGA. Let `R` be a nontrivial
> commutative ring with exactly one prime ideal whose nilradical is not nilpotent. Then the
> pseudo-discretisation of `Spec R` is a formal scheme à la EGA carrying an ideal sheaf — the
> nilradical — which is a weak ideal of definition over its affine formal open subschemes and is
> *not* an ideal of definition over them. This is why the correspondence of Stacks 0AIV between
> weak ideals of definition and thickenings cannot restrict to a correspondence between ideals of
> definition and thickenings.

```lean
theorem exists_isWeakIdealOfDefinitionOn_not_isIdealOfDefinitionOn_of_nilradical
    (R : Type u) [CommRing R] [Nontrivial R] [Subsingleton (PrimeSpectrum R)]
    (hnil : ∀ n : ℕ, (nilradical R) ^ n ≠ ⊥) :
    ∃ (X : LTRS.{u}) (_ : IsFormalScheme X) (I : IdealSheaf X),
      I.IsWeakIdealOfDefinitionOn (IsAffineFormalOpen X) ∧
        ¬ I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.FormalScheme.exists_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFppfColimitOfThickenings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionColimit.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionColimit.lean#L192). The attribute's comment: “the direction from colimit to fundamental system: for 𝔛 quasi-compact, if h\_𝔛 is a colimit of schemes as in Lemma 0AIU (colimit in fppf sheaves) then there exists a fundamental system of ideals of definition for 𝔛, for ideal sheaves in the source's generality”.

> **Stacks 0AIW, the "only if" direction, for arbitrary ideal sheaves.** If the functor of points
> `h_𝔛` of a quasi-compact formal scheme `𝔛` à la EGA is a colimit of schemes along thickenings in
> fppf sheaves, as in Stacks 0AIU, then `𝔛` has a fundamental system of ideals of definition, with
> the definitions of the source: ideal sheaves whose ideals of sections over every affine formal open
> are ideals of definition, and a neighbourhood basis of zero there.

```lean
theorem FormalScheme.exists_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFppfColimitOfThickenings
    (X : FormalScheme.{u}) [CompactSpace ↥X.obj]
    (h : X.toMcQuillanFormalScheme.IsFppfColimitOfThickenings) :
    ∃ 𝒮 : Set (IdealSheaf X.obj),
      IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X.obj)
```

**`AlgebraicGeometry.FormalScheme.isFppfColimitOfThickenings_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionColimit.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionColimit.lean#L218). The attribute's comment: “corrected form: for 𝔛 quasi-compact, h\_𝔛 is a colimit of schemes as in Lemma 0AIU (colimit in fppf sheaves) iff there exists a fundamental system of ideals of definition for 𝔛 cut out by their sections over the affine formal opens (erratum in errata.md); the direction from fundamental system to colimit as printed is false: see FormalScheme.not\_forall\_isFppfColimitOfThickenings\_of\_exists; the direction from colimit to fundamental system holds for arbitrary ideal sheaves, exists\_isFundamentalSystemOfIdealsOfDefinitionOn\_of\_isFppfColimitOfThickenings”.

> **Stacks 0AIW.** The functor of points `h_𝔛` of a quasi-compact formal scheme `𝔛` à la EGA is a
> colimit of schemes along thickenings in fppf sheaves, as in Stacks 0AIU, if and only if `𝔛` has a
> fundamental system of ideals of definition cut out by their sections over the affine formal opens.
>
> This is the corrected form of the remark. The "only if" direction holds without the cut-out
> condition
> (`FormalScheme.exists_isFundamentalSystemOfIdealsOfDefinitionOn_of_isFppfColimitOfThickenings`).
> The source's definition of an ideal of definition is sectionwise and does not ask for the cut-out
> condition (the analogue of `ℐ|_𝔘 = ℐ(𝔘)^Δ` in EGA), and with it the "if" direction is false
> (`FormalScheme.not_forall_isFppfColimitOfThickenings_of_exists`).

```lean
theorem FormalScheme.isFppfColimitOfThickenings_iff (X : FormalScheme.{u}) [CompactSpace ↥X.obj] :
    X.toMcQuillanFormalScheme.IsFppfColimitOfThickenings ↔ ∃ 𝒮 : Set (IdealSheaf X.obj),
      (∀ I ∈ 𝒮, I.IsCutOutOn (IsAffineFormalOpen X.obj)) ∧
        IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X.obj)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.not_forall_exists_isIdealOfDefinitionOn_of_isFundamentalSystemOfWeakIdealsOfDefinitionOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCounterexample.lean, line 730](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCounterexample.lean#L730). The attribute's comment: “`ℐ_λ` is an ideal of definition for `λ` large: FALSE as printed, for ideal sheaves in the source's generality, on a quasi-compact (even affine) formal scheme à la EGA and for a nonempty directed system; the true statement is over the members of a finite affine open covering, `exists_isIdealOfDefinition_of_isFormalScheme`”.

> **Stacks 0AIW, the eventual ideals of definition, is false as printed.** It is not true that on
> every quasi-compact formal scheme à la EGA a fundamental system `{ℐ_λ}` of weak ideals of
> definition consists of ideals of definition for `λ` sufficiently large, even for a nonempty
> system directed by inclusion: in the system of
> `exists_isFundamentalSystemOfWeakIdealsOfDefinitionOn_forall_not_isIdealOfDefinitionOn` no member
> at all is an ideal of definition over the affine formal opens.
>
> The source's argument shows that `ℐ_λ(𝔘)` is an ideal of definition for `λ` large on the finitely
> many members `𝔘` of an affine open covering, which is true
> (`exists_isIdealOfDefinition_of_isFormalScheme`), and concludes by the locality claim refuted in
> `not_forall_isIdealOfDefinitionOn_of_cover`.

```lean
theorem not_forall_exists_isIdealOfDefinitionOn_of_isFundamentalSystemOfWeakIdealsOfDefinitionOn :
    ¬ ∀ (X : LTRS.{0}), IsFormalScheme X → CompactSpace X → ∀ 𝒮 : Set (IdealSheaf X),
      𝒮.Nonempty →
      (∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
        K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W) →
      IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X) →
      ∃ I₀ ∈ 𝒮, ∀ I ∈ 𝒮, (∀ W : Opens X, I.ideal W ≤ I₀.ideal W) →
        I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.not_forall_isIdealOfDefinitionOn_of_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCounterexample.lean, line 763](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCounterexample.lean#L763). The attribute's comment: “it suffices to check the ideal-of-definition condition on an affine open covering: FALSE as printed, for ideal sheaves in the source's generality, already for the covering of an affine formal scheme by itself”.

> **Stacks 0AIW, the locality of the ideal-of-definition condition, is false as printed.** It is
> not true that an ideal sheaf on a formal scheme à la EGA is an ideal of definition as soon as its
> ideals of sections over the members of an affine open covering are ideals of definition: on the
> pseudo-discretisation of `Spec (ℤ[X₀, X₁, …] / (X_k ^ (k + 1)))` the sections with nilpotent germs
> vanishing outside `D(n!)` are zero over the whole space, which is affine, and are not an ideal of
> definition over `D(n!)`.
>
> The corrected statement checks the condition on the affine formal opens contained in the members
> of the covering: `IdealSheaf.isIdealOfDefinitionOn_of_cover`.

```lean
theorem not_forall_isIdealOfDefinitionOn_of_cover :
    ¬ ∀ (X : LTRS.{0}), IsFormalScheme X → ∀ (I : IdealSheaf X) (𝒰 : Set (Opens X)),
      (∀ V ∈ 𝒰, IsAffineFormalOpen X V) → sSup 𝒰 = ⊤ →
      (∀ V ∈ 𝒰, TopologicalRing.IsIdealOfDefinition (I.ideal V)) →
      I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.not_forall_isFundamentalSystemOfIdealsOfDefinitionOn_of_hasBasis_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCounterexample.lean, line 796](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCounterexample.lean#L796). The attribute's comment: “it suffices to check the fundamental-system condition on an affine open covering: FALSE as printed, for ideal sheaves in the source's generality, already for a single ideal of definition and the covering of an affine formal scheme by itself”.

> **Stacks 0AIW, the locality of the fundamental-system condition, is false as printed.** It is
> not true that a family of ideals of definition on a formal scheme à la EGA is a fundamental system
> as soon as its ideals of sections form a neighbourhood basis of zero over the members of an affine
> open covering, even for a nonempty directed family whose members are ideals of definition over
> every affine formal open: on the pseudo-discretisation of `Spec (ℤ[X₀, X₁, …] / (X_k ^ (k + 1)))`
> the sections whose germs are multiples of the germ of `X₁`, vanishing outside `D(n!)`, form an
> ideal of definition which is zero over the whole space, which is affine, but whose sections over
> `D(n!)`, which are discrete, contain `X₁ ≠ 0`.
>
> The corrected statement checks the condition on the affine formal opens contained in the members
> of the covering: `isFundamentalSystemOfIdealsOfDefinitionOn_of_cover_of_directed`.

```lean
theorem not_forall_isFundamentalSystemOfIdealsOfDefinitionOn_of_hasBasis_cover :
    ¬ ∀ (X : LTRS.{0}), IsFormalScheme X → ∀ (𝒮 : Set (IdealSheaf X)) (𝒰 : Set (Opens X)),
      𝒮.Nonempty →
      (∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
        K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W) →
      (∀ V ∈ 𝒰, IsAffineFormalOpen X V) → sSup 𝒰 = ⊤ →
      (∀ I ∈ 𝒮, I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)) →
      (∀ V ∈ 𝒰, (nhds (0 : (X.presheaf.obj (op V)).α)).HasBasis (· ∈ 𝒮)
        fun I : IdealSheaf X => (I.ideal V : Set (X.presheaf.obj (op V)).α)) →
      IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.exists_forall_isIdealOfDefinitionOn_of_isCutOutOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCutOut.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCutOut.lean#L278). The attribute's comment: “`ℐ_λ` is an ideal of definition for `λ` large, over EVERY affine formal open, for a directed system whose members are cut out by their sections over the affine formal opens (the condition of Stacks 0AIV singling out the ideal sheaves of thickenings); for arbitrary ideal sheaves the statement is false, `not_forall_exists_isIdealOfDefinitionOn_of_isFundamentalSystemOfWeakIdealsOfDefinitionOn`”.

> **Stacks 0AIW, the eventual ideals of definition, for a system cut out by its sections.** On a
> quasi-compact formal scheme à la EGA, let `𝒮` be a nonempty, directed fundamental system of weak
> ideals of definition over the affine formal opens, each member cut out by its sections over the
> affine formal opens. Then there is a member `I₀` such that every member below it is an ideal of
> definition over every affine formal open.
>
> The finite affine covering produced by quasi-compactness gives `I₀` with ideals of definition over
> the members of the covering (`exists_isIdealOfDefinition_of_isFormalScheme`), and
> `IdealSheaf.pow_ideal_le_of_isCutOutOn` carries the comparison of powers from the covering to an
> arbitrary affine formal open.

```lean
theorem exists_forall_isIdealOfDefinitionOn_of_isCutOutOn {X : LTRS.{u}} [CompactSpace ↥X]
    (hX : IsFormalScheme X) (𝒮 : Set (IdealSheaf X)) (hne : 𝒮.Nonempty)
    (hdir : ∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
      K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W)
    (hfund : IsFundamentalSystemOfWeakIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X))
    (hcut : ∀ I ∈ 𝒮, I.IsCutOutOn (IsAffineFormalOpen X)) :
    ∃ I₀ ∈ 𝒮, ∀ I ∈ 𝒮, (∀ W : Opens X, I.ideal W ≤ I₀.ideal W) →
      I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IdealSheaf.isIdealOfDefinitionOn_of_cover_of_isCutOutOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCutOutLocality.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCutOutLocality.lean#L162). The attribute's comment: “it suffices to check the ideal-of-definition condition on the members of an affine open covering: for ideal sheaves cut out by their sections over the affine formal opens (IdealSheaf.IsCutOutOn), the class of the colimit criterion FormalScheme.isFppfColimitOfThickenings\_iff; for an arbitrary ideal sheaf it is false (not\_forall\_isIdealOfDefinitionOn\_of\_cover)”.

> **Stacks 0AIW, the ideal-of-definition condition may be checked on the members of an affine
> open covering, for ideal sheaves cut out by their sections.** Let `𝔛` be a formal scheme à la EGA
> and `ℐ` an ideal sheaf cut out by its sections over the affine formal opens
> (`IdealSheaf.IsCutOutOn`). If `ℐ(𝔙)` is an ideal of definition for the members `𝔙` of a covering
> of `𝔛` by affine formal opens, then `ℐ` is an ideal of definition.
>
> These are the ideal sheaves of the colimit criterion of Stacks 0AIW,
> `FormalScheme.isFppfColimitOfThickenings_iff`. For an arbitrary ideal sheaf checking the covering
> members is not enough (`not_forall_isIdealOfDefinitionOn_of_cover`), and the condition must then be
> checked on the affine formal opens inside the covering members
> (`IdealSheaf.isIdealOfDefinitionOn_of_cover_of_isFormalScheme`). Over an affine formal open inside
> a covering member the condition is `IdealSheaf.isIdealOfDefinition_of_le_of_isCutOutOn`.

```lean
theorem IdealSheaf.isIdealOfDefinitionOn_of_cover_of_isCutOutOn
    (hX : IsFormalScheme X) (I : IdealSheaf X)
    (hC : I.IsCutOutOn (IsAffineFormalOpen X)) (𝒰 : Set (Opens X))
    (h𝒰 : ∀ V ∈ 𝒰, IsAffineFormalOpen X V) (hcover : sSup 𝒰 = ⊤)
    (hI : ∀ V ∈ 𝒰, IsIdealOfDefinition (I.ideal V)) :
    I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.isFundamentalSystemOfIdealsOfDefinitionOn_of_cover_of_isCutOutOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCutOutLocality.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionCutOutLocality.lean#L191). The attribute's comment: “it suffices to check the fundamental-system condition on the members of an affine open covering: for a family indexed by a directed set, as in the source, of ideal sheaves cut out by their sections over the affine formal opens (IdealSheaf.IsCutOutOn), the class of the colimit criterion FormalScheme.isFppfColimitOfThickenings\_iff; for arbitrary ideal sheaves it is false (not\_forall\_isFundamentalSystemOfIdealsOfDefinitionOn\_of\_hasBasis\_cover)”. References: EGA I (10.3.7), “more general”.

> **Stacks 0AIW, the fundamental-system condition may be checked on the members of an affine
> open covering, for ideal sheaves cut out by their sections.** Let `𝔛` be a formal scheme à la EGA
> and `{ℐ_λ}` a nonempty family of ideal sheaves, directed by inclusion, each cut out by its sections
> over the affine formal opens. If over the members `𝔙` of a covering of `𝔛` by affine formal opens
> the `ℐ_λ(𝔙)` are ideals of definition forming a neighbourhood basis of zero, then `{ℐ_λ}` is a
> fundamental system of ideals of definition.
>
> The family is indexed, as in the source, by a directed set (nonempty, by Stacks' definition of a
> directed set), with `ℐ_μ ⊆ ℐ_λ` for `μ ≥ λ`; over an affine formal open inside a single covering
> member no directedness is used (`hasBasis_of_le_of_isCutOutOn`). These are the families of the
> colimit criterion `FormalScheme.isFppfColimitOfThickenings_iff`. For arbitrary ideal sheaves
> checking the covering members is not enough
> (`not_forall_isFundamentalSystemOfIdealsOfDefinitionOn_of_hasBasis_cover`).

```lean
theorem isFundamentalSystemOfIdealsOfDefinitionOn_of_cover_of_isCutOutOn
    (hX : IsFormalScheme X) (𝒮 : Set (IdealSheaf X))
    (hC : ∀ I ∈ 𝒮, I.IsCutOutOn (IsAffineFormalOpen X)) (hne : 𝒮.Nonempty)
    (hdir : ∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
      K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W)
    (𝒰 : Set (Opens X)) (h𝒰 : ∀ V ∈ 𝒰, IsAffineFormalOpen X V) (hcover : sSup 𝒰 = ⊤)
    (h𝒮 : ∀ I ∈ 𝒮, ∀ V ∈ 𝒰, IsIdealOfDefinition (I.ideal V))
    (hbasis : ∀ V ∈ 𝒰, (nhds (0 : (X.presheaf.obj (op V)).α)).HasBasis (· ∈ 𝒮)
      fun I : IdealSheaf X => (I.ideal V : Set (X.presheaf.obj (op V)).α)) :
    IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.IdealSheaf.isIdealOfDefinitionOn_of_cover_of_isFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionLocality.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionLocality.lean#L112). The attribute's comment: “it suffices to check the ideal-of-definition condition on an affine open covering, CORRECTED, on a formal scheme à la EGA with no further hypothesis: the condition is checked on the affine formal opens contained in a covering member, not on the covering members themselves, which is false as the source states it (`not_forall_isIdealOfDefinitionOn_of_cover`)”.

> **Stacks 0AIW**, the locality of the ideal-of-definition condition on a formal scheme à la EGA.
> An ideal sheaf is an ideal of definition as soon as its ideals of sections over the affine formal
> open subschemes contained in the members of some covering are ideals of definition. The
> affine formal open subschemes are quasi-compact and form a basis, which are the two hypotheses
> `IdealSheaf.isIdealOfDefinitionOn_of_cover` asks of the class of opens.

```lean
theorem IdealSheaf.isIdealOfDefinitionOn_of_cover_of_isFormalScheme {X : LTRS.{u}}
    (hX : IsFormalScheme X) (I : IdealSheaf X) (𝒰 : Set (Opens X)) (hcover : sSup 𝒰 = ⊤)
    (hI : ∀ V ∈ 𝒰, ∀ U : Opens X, U ≤ V → IsAffineFormalOpen X U →
      TopologicalRing.IsIdealOfDefinition (I.ideal U)) :
    I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.LocallyTopologicallyRingedSpace.isFundamentalSystemOfIdealsOfDefinitionOn_of_cover_of_isFormalScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionLocality.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/IdealOfDefinitionLocality.lean#L131). The attribute's comment: “it suffices to check the fundamental-system condition on an affine open covering, CORRECTED, on a formal scheme à la EGA with no further hypothesis: both halves are checked on the affine formal opens contained in a covering member, not on the covering members themselves, which is false as the source states it (`not_forall_isFundamentalSystemOfIdealsOfDefinitionOn_of_hasBasis_cover`), for a nonempty system directed by inclusion (`hne`, `hdir`), the source's directed index set `Λ`”.

> **Stacks 0AIW**, the locality of the fundamental-system condition on a formal scheme à la EGA,
> with no hypothesis on the class of opens: for a nonempty family directed by inclusion, both halves
> of the condition may be checked on the affine formal open subschemes contained in the members of a
> covering.

```lean
theorem isFundamentalSystemOfIdealsOfDefinitionOn_of_cover_of_isFormalScheme {X : LTRS.{u}}
    (hX : IsFormalScheme X) (𝒮 : Set (IdealSheaf X)) (hne : 𝒮.Nonempty)
    (hdir : ∀ I ∈ 𝒮, ∀ J ∈ 𝒮, ∃ K ∈ 𝒮, ∀ W : Opens X,
      K.ideal W ≤ I.ideal W ∧ K.ideal W ≤ J.ideal W)
    (𝒰 : Set (Opens X)) (hcover : sSup 𝒰 = ⊤)
    (h𝒮 : ∀ I ∈ 𝒮, ∀ V ∈ 𝒰, ∀ U : Opens X, U ≤ V → IsAffineFormalOpen X U →
      TopologicalRing.IsIdealOfDefinition (I.ideal U))
    (hbasis : ∀ V ∈ 𝒰, ∀ U : Opens X, U ≤ V → IsAffineFormalOpen X U →
      (nhds (0 : (X.presheaf.obj (op U)).α)).HasBasis (· ∈ 𝒮)
        fun I : IdealSheaf X => (I.ideal U : Set (X.presheaf.obj (op U)).α)) :
    IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X)
```

**`AlgebraicGeometry.FormalScheme.not_forall_isFppfColimitOfThickenings_of_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalScheme/TwistedDoubleColimit.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalScheme/TwistedDoubleColimit.lean#L65). The attribute's comment: “the if direction as printed (sectionwise ideals of definition) is false: a quasi-compact formal scheme with a fundamental system of ideals of definition whose functor of points h\_𝔛 is not a colimit of schemes as in Lemma 0AIU (colimit in fppf sheaves); corrected form: FormalScheme.isFppfColimitOfThickenings\_iff”.

> **Stacks 0AIW, the "if" direction as printed, is false.** There is a quasi-compact formal
> scheme `𝔛` à la EGA (the twisted double `AlgebraicGeometry.TwistedDouble.𝔛`) which has a
> fundamental system of ideals of definition, in the source's sectionwise sense, but whose functor
> of points `h_𝔛` is not a colimit of schemes along thickenings in fppf sheaves, as in Stacks 0AIU.
>
> The corrected form is `AlgebraicGeometry.FormalScheme.isFppfColimitOfThickenings_iff`, where the
> ideals of definition are cut out by their sections over the affine formal opens.

```lean
theorem FormalScheme.not_forall_isFppfColimitOfThickenings_of_exists :
    ¬ ∀ (X : FormalScheme.{0}) [CompactSpace X.obj],
      (∃ 𝒮 : Set (IdealSheaf X.obj),
        IsFundamentalSystemOfIdealsOfDefinitionOn 𝒮 (IsAffineFormalOpen X.obj)) →
        X.toMcQuillanFormalScheme.IsFppfColimitOfThickenings
```

**`AlgebraicGeometry.FormalSpace.WeakIdealOfDefinitionExample.isThickening_residueField_and_not_isIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean#L91). The attribute's comment: “we do NOT get the same correspondence between ideals of definition and thickenings as in Stacks 0AIV: the residue-field stage of Spf A is a thickening while the weak ideal of definition it corresponds to is not an ideal of definition (Stacks 0CB8); the formal spectrum is taken over a big fppf site through its presentation `D` (site membership and structure morphisms to `S`), as in the statements of Stacks 0CB8 combined here”.

> **Stacks 0AIW**, the failure of the correspondence of Stacks 0AIV for ideals of definition.
> For a valuation ring `(A, 𝔪, κ)` which is `(π)`-adically complete for a nonzero `π ∈ 𝔪` whose
> radical is `𝔪`, and whose maximal ideal is not finitely generated, the residue-field stage
> `Spec κ ⟶ Spf A` of the formal spectrum is a thickening, while the weak ideal of definition `𝔪`
> to which the correspondence of Stacks 0AIV attaches it is *not* an ideal of definition. So the
> correspondence between weak ideals of definition and thickenings does not restrict to a
> correspondence between ideals of definition and thickenings.

```lean
theorem isThickening_residueField_and_not_isIdealOfDefinition [IsDomain A]
    (hval : IsValuationRing A) (hπm : π ∈ maximalIdeal A)
    (hadic : IsAdic (Ideal.span ({π} : Set A)))
    (hrad : (Ideal.span ({π} : Set A)).radical = maximalIdeal A)
    (hnotfg : ¬ (maximalIdeal A).FG)
    {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    (D : QuotientSystem B S hS A) :
    let J : { I : Ideal A // TopologicalRing.IsWeakIdealOfDefinition I } :=
      ⟨maximalIdeal A, isWeakIdealOfDefinition_maximalIdeal π hadic hrad⟩
    (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)))
      (formalSpectrumInclusion D (OrderDual.toDual J)) ∧
      ¬ TopologicalRing.IsIdealOfDefinition J.1
```

**`PadicComplexInt.isWeakIdealOfDefinition_maximalIdeal_and_not_isIdealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean#L127). The attribute's comment: “the negative clause is not vacuous: in the ring of integers of ℂ\_[p] the maximal ideal is a weak ideal of definition and is not an ideal of definition”.

> **Stacks 0AIW**, the negative clause on the example of Stacks 0CB8. The maximal ideal of the
> ring of integers of the field `ℂ_[p]` of `p`-adic complex numbers is a weak ideal of definition
> of that admissible topological ring, and it is not an ideal of definition. So the two notions
> differ, and the correspondence of Stacks 0AIV between weak ideals of definition and thickenings
> cannot restrict to one between ideals of definition and thickenings.

```lean
theorem isWeakIdealOfDefinition_maximalIdeal_and_not_isIdealOfDefinition :
    TopologicalRing.IsWeakIdealOfDefinition (maximalIdeal (PadicComplexInt p)) ∧
      ¬ TopologicalRing.IsIdealOfDefinition (maximalIdeal (PadicComplexInt p))
```

**`PadicComplexInt.isThickening_residueField_not_from_idealOfDefinition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean#L142). The attribute's comment: “the negative clause on the example of Stacks 0CB8: a thickening of the formal spectrum of the ring of integers of ℂ\_[p] whose weak ideal of definition is not an ideal of definition; the formal spectrum is taken over a big fppf site through its presentation `D`”.

> **Stacks 0AIW**, the negative clause on the example of Stacks 0CB8, geometrically: the
> residue-field stage `Spec ℂ_[p]^- ⟶ Spf 𝒪_{ℂ_p}` of the formal spectrum of the ring of integers
> of `ℂ_[p]` is a thickening whose weak ideal of definition, the maximal ideal, is not an ideal of
> definition.

```lean
theorem isThickening_residueField_not_from_idealOfDefinition
    {B : BigFppfSite.{0}} {S : Scheme.{0}} {hS : B.Contains S}
    (D : QuotientSystem B S hS (PadicComplexInt p)) :
    let J : { I : Ideal (PadicComplexInt p) // TopologicalRing.IsWeakIdealOfDefinition I } :=
      ⟨maximalIdeal (PadicComplexInt p),
        (isWeakIdealOfDefinition_maximalIdeal_and_not_isIdealOfDefinition p).1⟩
    (MorphismProperty.relative
      (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
      (MorphismProperty.inverseImage
        (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{0})
        (BigFppfOver.toScheme B S hS)))
      (formalSpectrumInclusion D (OrderDual.toDual J)) ∧
      ¬ TopologicalRing.IsIdealOfDefinition J.1
```

**`PadicComplexInt.exists_isWeakIdealOfDefinitionOn_not_isIdealOfDefinitionOn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/IdealOfDefinitionNotAllThickenings.lean#L241). The attribute's comment: “the negative clause is not vacuous at the level of ideal sheaves: an explicit formal scheme à la EGA with a weak ideal of definition that is not an ideal of definition”.

> **Stacks 0AIW**, the negative clause at the level of ideal sheaves, unconditionally. The
> pseudo-discretisation of `Spec (𝒪_{ℂ_p}/(p))` is a formal scheme à la EGA whose nilradical is a
> weak ideal of definition over its affine formal open subschemes and is not an ideal of definition
> over them: the ring has the single prime `𝔪/(p)`, and no power of its nilradical vanishes because
> no power of `𝔪` lies inside `(p)`.

```lean
theorem exists_isWeakIdealOfDefinitionOn_not_isIdealOfDefinitionOn
    (q : ℕ) [Fact (Nat.Prime q)] :
    ∃ (X : LTRS.{0}) (_ : IsFormalScheme X) (I : LocallyTopologicallyRingedSpace.IdealSheaf X),
      I.IsWeakIdealOfDefinitionOn (IsAffineFormalOpen X) ∧
        ¬ I.IsIdealOfDefinitionOn (IsAffineFormalOpen X)
```

**`TopologicalRing.isIdealOfDefinition_of_le_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/IdealOfDefinition.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Algebra/AdicTopology/IdealOfDefinition.lean#L106). The attribute's comment: “in an admissible topological ring all sufficiently small open ideals are ideals of definition: any open ideal contained in an ideal of definition is one”.

> **Stacks 0AIW.** An open ideal contained in an ideal of definition is an ideal of definition:
> its powers lie inside the corresponding powers of the larger ideal, and those are cofinal among
> the neighbourhoods of zero. Since in an admissible topological ring the open ideals form a basis
> of neighbourhoods of zero, this is the source's observation that all sufficiently small open
> ideals of such a ring are ideals of definition.

```lean
public theorem isIdealOfDefinition_of_le_of_isOpen {I J : Ideal R}
    (hJ : IsIdealOfDefinition J) (hI : IsOpen (I : Set R)) (hIJ : I ≤ J) :
    IsIdealOfDefinition I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.13, Tag 0AIT](https://stacks.math.columbia.edu/tag/0AIT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
