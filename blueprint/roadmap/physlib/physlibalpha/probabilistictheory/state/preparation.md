---
declaration: module
origin: cited
lean: ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.of_smul_le, ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.of_mix_left, ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.of_mix_right, ProbabilisticTheory.Preparation, ProbabilisticTheory.Preparation.integrable_prepare, ProbabilisticTheory.Preparation.state, ProbabilisticTheory.Preparation.state_apply, ProbabilisticTheory.Preparation.state_isNormal
statement: formalized
proof: formalized
---

# Preparation procedures

The module `PhyslibAlpha.ProbabilisticTheory.State.Preparation`, [PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean): 21 declarations (2 instances with no name), 16 with a docstring.

> Preparation procedures: random preparations of states, their prepared states and outcome laws.

## i. Overview

> A preparation procedure rolls a die and, depending on the outcome `x`, prepares the state
> `prepare x`. The die is any classical random variable, with law `law`. Whoever does not see the roll
> is left with the average of the prepared states: the state the procedure prepares.
>
> A measurement `M` performed after the procedure has an outcome whose law depends on the roll. Roll
> and outcome together are a pair of random variables. Their joint law is the law of the roll combined
> with the outcome law given the roll. Forgetting the roll, the outcome has the Born law of the
> prepared state.

## ii. Key results

> - `Preparation E X` : a preparation procedure with a die taking values in `X`.
> - `Preparation.state` : the state a procedure prepares.
> - `Preparation.state_isNormal` : a prepared state is normal.
> - `Preparation.ofMix` : preparing one of two states at random.
> - `Preparation.conditionalState` : the state prepared given that the roll lies in an event.
> - `Preparation.outcome` : the outcome law of a measurement given the roll.
> - `Preparation.outcome_comp_law` : forgetting the roll, the outcome has the Born law of the
>   prepared state.
> - `UnitalPositiveLinearMap.IsNormal.of_mix_left` : the components of a normal mixture are normal.

## iv. References

> * None.

## A. Normal components of mixtures

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.of_smul_le`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L68).

> A state dominated by a positive multiple of a normal state is normal.

```lean
lemma IsNormal.of_smul_le {ω φ : 𝓢[ℝ, E]} (hω : ω.IsNormal) {c : ℝ} (hc : 0 < c)
    (h : ∀ A, 0 ≤ A → c * φ A ≤ ω A) : φ.IsNormal
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.of_mix_left`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L86).

> If a proper mixture is normal, so is its first component.

```lean
lemma IsNormal.of_mix_left {φ ψ : 𝓢[ℝ, E]} {t : unitInterval} (h : (mix φ ψ t).IsNormal)
    (ht : t ≠ 0) : φ.IsNormal
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsNormal.of_mix_right`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L92).

> If a proper mixture is normal, so is its second component.

```lean
lemma IsNormal.of_mix_right {φ ψ : 𝓢[ℝ, E]} {t : unitInterval} (h : (mix φ ψ t).IsNormal)
    (ht : t ≠ 1) : ψ.IsNormal
```

## B. Preparation procedures

**`ProbabilisticTheory.Preparation`**, a structure, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L103).

> A preparation procedure: roll a die with values in `X` and law `law`, and on the roll `x`
> prepare the normal state `prepare x`.

```lean
structure Preparation (E : Type u) [OrderUnitSpace E] (X : Type v) [MeasurableSpace X] where
  /-- The law of the die. -/
  law : ProbabilityMeasure X
  /-- The state prepared on each roll. -/
  prepare : X → 𝓢[ℝ, E]
  /-- The state prepared on each roll is normal. -/
  normal : ∀ x, (prepare x).IsNormal
  /-- Every expectation value depends measurably on the roll. -/
  measurable_prepare : ∀ A : E, Measurable fun x => prepare x A
```

**`ProbabilisticTheory.Preparation.integrable_prepare`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L118).

> Every expectation value is integrable in the roll.

```lean
lemma integrable_prepare (p : Preparation E X) (A : E) :
    Integrable (fun x => p.prepare x A) (p.law : Measure X)
```

**`ProbabilisticTheory.Preparation.state`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L129).

> The state a procedure prepares, once the roll is forgotten: the average of the prepared
> states.

```lean
noncomputable def state (p : Preparation E X) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.Preparation.state_apply`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L141).

```lean
lemma state_apply (p : Preparation E X) (A : E) :
    p.state A = ∫ x, p.prepare x A ∂(p.law : Measure X)
```

**`ProbabilisticTheory.Preparation.state_isNormal`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L146).

> A prepared state is normal.

```lean
lemma state_isNormal (p : Preparation E X) : p.state.IsNormal
```

## C. Preparing one of two states

**`ProbabilisticTheory.Preparation.ofMix`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L159).

> Prepare `φ` with probability `t` and `ψ` otherwise.

```lean
noncomputable def ofMix (φ ψ : 𝓢[ℝ, E]) (t : unitInterval) (hφ : φ.IsNormal)
    (hψ : ψ.IsNormal) : Preparation E Bool
```

**`ProbabilisticTheory.Preparation.state_ofMix`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L168).

> Preparing one of two states at random prepares their mixture.

```lean
lemma state_ofMix (φ ψ : 𝓢[ℝ, E]) (t : unitInterval) (hφ : φ.IsNormal) (hψ : ψ.IsNormal) :
    (ofMix φ ψ t hφ hψ).state = mix φ ψ t
```

**`ProbabilisticTheory.Preparation.ae_ofMix_iff`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L181).

> When both states have positive probability, a property holds almost surely exactly when it
> holds for both rolls.

```lean
lemma ae_ofMix_iff {φ ψ : 𝓢[ℝ, E]} {t : unitInterval} {hφ : φ.IsNormal} {hψ : ψ.IsNormal}
    (ht0 : t ≠ 0) (ht1 : t ≠ 1) {P : Bool → Prop} :
    (∀ᵐ b ∂((ofMix φ ψ t hφ hψ).law : Measure Bool), P b) ↔ P true ∧ P false
```

## D. Conditional states

**`ProbabilisticTheory.Preparation.conditionalState`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L197).

> The state prepared given that the roll lies in an event of positive probability.

```lean
noncomputable def conditionalState (p : Preparation E X) (s : Set X)
    (hpos : 0 < (p.law : Measure X).real s) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.Preparation.conditionalState_apply`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L217).

```lean
lemma conditionalState_apply (p : Preparation E X) (s : Set X)
    (hpos : 0 < (p.law : Measure X).real s) (A : E) :
    p.conditionalState s hpos A =
      ((p.law : Measure X).real s)⁻¹ * ∫ x in s, p.prepare x A ∂(p.law : Measure X)
```

**`ProbabilisticTheory.Preparation.mix_conditionalState_compl`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L225).

> The prepared state is the mixture of the states conditioned on an event and on its complement,
> weighted by their probabilities.

```lean
lemma mix_conditionalState_compl (p : Preparation E X) {s : Set X} (hs : MeasurableSet s)
    (hpos : 0 < (p.law : Measure X).real s) (hposc : 0 < (p.law : Measure X).real sᶜ) :
    mix (p.conditionalState s hpos) (p.conditionalState sᶜ hposc)
      ⟨(p.law : Measure X).real s, measureReal_nonneg, measureReal_le_one⟩ = p.state
```

## E. Measurement outcomes

**`ProbabilisticTheory.Preparation.outcome`**, a def, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L238).

> The outcome law of the measurement `M` given the roll.

```lean
noncomputable def outcome (p : Preparation E X) (M : Measurement Ω E) : Kernel X Ω
```

**`ProbabilisticTheory.Preparation.outcome_apply`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L244).

```lean
lemma outcome_apply (p : Preparation E X) (M : Measurement Ω E) (x : X) :
    p.outcome M x = M.probabilityLaw (p.prepare x) (p.normal x)
```

**An instance with no name**, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L248).

```lean
instance (p : Preparation E X) (M : Measurement Ω E) : IsMarkovKernel (p.outcome M)
```

**`ProbabilisticTheory.Preparation.outcome_comp_law`**, a lemma, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L252).

> Forgetting the roll, the outcome of `M` has the Born law of the prepared state.

```lean
lemma outcome_comp_law (p : Preparation E X) (M : Measurement Ω E) :
    p.outcome M ∘ₘ (p.law : Measure X) = M.probabilityLaw p.state p.state_isNormal
```

**`ProbabilisticTheory.Preparation.forgetfulOutcome`**, a def, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L263).

> The outcome law of `M` when the roll is forgotten: the Born law of the prepared state, whatever
> the roll.

```lean
noncomputable def forgetfulOutcome (p : Preparation E X) (M : Measurement Ω E) :
    Kernel X Ω
```

**An instance with no name**, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L267).

```lean
instance (p : Preparation E X) (M : Measurement Ω E) :
    IsMarkovKernel (p.forgetfulOutcome M)
```

**`ProbabilisticTheory.Preparation.forgetfulOutcome_isPostprocessing`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean#L272).

> Forgetting the roll is a post-processing of the outcome law given the roll.

```lean
lemma forgetfulOutcome_isPostprocessing (p : Preparation E X) (M : Measurement Ω E) :
    Kernel.FactorsThrough (p.forgetfulOutcome M) (p.outcome M)
```

## Depends on

- [Factorization of Markov kernels](../../mathematics/part-02/probability/kernel-factorization.md)
- [Measurements](../measurement/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/State/Preparation.lean)
