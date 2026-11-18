---
declaration: module
origin: cited
lean: ProbabilisticTheory.MeasurableProjectionResolution.probabilityLaw, ProbabilisticTheory.MeasurableProjectionResolution.probabilityLaw_apply, ProbabilisticTheory.MeasurableProjectionResolution.scalarBoundedBorel_eq_integral, ProbabilisticTheory.MeasurableProjectionResolution.eq_of_forall_normal_state_eq, ProbabilisticTheory.MeasurableProjectionResolution.eq_of_forall_normal_probabilityLaw_eq
statement: formalized
proof: formalized
---

# Projection resolutions in JBW-algebras

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JBW.ProjectionResolution`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean): 5 declarations, 5 with a docstring.

> Normal states turn projection resolutions into probability laws and separate them.

## i. Overview

> A projection resolution is defined at the Jordan order-unit level. In a JBW-algebra two further
> things hold. A normal state turns a projection resolution into an ordinary probability law, and
> its bounded Borel calculus into ordinary integration against that law. And normal states
> separate projection resolutions, so a projection resolution is determined by its probability laws.

## ii. Key results

> - `MeasurableProjectionResolution.probabilityLaw` : the probability law in a normal state.
> - `MeasurableProjectionResolution.scalarBoundedBorel_eq_integral` : a normal state applied to the
>   bounded Borel calculus is the integral against the scalarized measure.
> - `MeasurableProjectionResolution.eq_of_forall_normal_probabilityLaw_eq` : normal-state
>   probability laws determine the projection resolution.

## iv. References

> * None.

## A. Probability laws

**`ProbabilisticTheory.MeasurableProjectionResolution.probabilityLaw`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean#L56).

> The probability law of a projection resolution in a normal state.

```lean
noncomputable def probabilityLaw (P : MeasurableProjectionResolution Ω E)
    (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) : ProbabilityMeasure Ω
```

**`ProbabilisticTheory.MeasurableProjectionResolution.probabilityLaw_apply`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean#L61).

> The probability of an event is the state evaluated at its projection.

```lean
lemma probabilityLaw_apply (P : MeasurableProjectionResolution Ω E)
    (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) (s : Set Ω) (hs : MeasurableSet s) :
    (P.probabilityLaw ω hω : Measure Ω) s = ENNReal.ofReal (ω (P s hs : E))
```

**`ProbabilisticTheory.MeasurableProjectionResolution.scalarBoundedBorel_eq_integral`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean#L68).

> A normal state applied to the bounded Borel calculus is the bounded integral against the
> scalarized measure.

```lean
lemma scalarBoundedBorel_eq_integral (P : MeasurableProjectionResolution Ω E)
    (ω : 𝓢[ℝ, E]) (hω : ω.IsNormal) {f : Ω → ℝ} (hf : Measurable f) {M : ℝ}
    (hM : ∀ x, |f x| ≤ M) :
    ω (P.boundedBorel f hf hM) =
      EffectValuedMeasure.integral hf hM (P.toEffectValuedMeasure.scalarize ω hω)
```

## B. Separation by normal states

**`ProbabilisticTheory.MeasurableProjectionResolution.eq_of_forall_normal_state_eq`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean#L78).

> Normal states separate projection resolutions pointwise.

```lean
lemma eq_of_forall_normal_state_eq {P Q : MeasurableProjectionResolution Ω E} [JBWAlgebra E]
    (h : ∀ ω : 𝓢[ℝ, E], ω.IsNormal → ∀ s hs, ω (P s hs : E) = ω (Q s hs : E)) : P = Q
```

**`ProbabilisticTheory.MeasurableProjectionResolution.eq_of_forall_normal_probabilityLaw_eq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean#L84).

> A projection resolution in a JBW-algebra is determined by its probability laws in all normal
> states.

```lean
lemma eq_of_forall_normal_probabilityLaw_eq {P Q : MeasurableProjectionResolution Ω E}
    [JBWAlgebra E]
    (h : ∀ ω : 𝓢[ℝ, E], ∀ hω : ω.IsNormal, P.probabilityLaw ω hω = Q.probabilityLaw ω hω) :
    P = Q
```

## Depends on

- [JBW-algebras](jbw-basic.md)
- [Projection resolutions](../part-01/projectionresolution.md)
- [The Born rule for effect-valued measures](../../measurement/bornrule.md)

## Proof depends on

- [Channels and integrals](../../measurement/boundedscalarization.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JBW/ProjectionResolution.lean)
