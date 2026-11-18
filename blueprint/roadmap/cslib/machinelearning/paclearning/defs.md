---
catalog: module
lean: Cslib.MachineLearning.PACLearning.ConceptClass, Cslib.MachineLearning.PACLearning.LabeledSample, Cslib.MachineLearning.PACLearning.Learner, Cslib.MachineLearning.PACLearning.error, Cslib.MachineLearning.PACLearning.optimalError, Cslib.MachineLearning.PACLearning.IsPACLearnerFor, Cslib.MachineLearning.PACLearning.IsRPACLearnerFor, Cslib.MachineLearning.PACLearning.IsPACLearnerFor.toIsRPACLearnerFor, Cslib.MachineLearning.PACLearning.IsPACLearnerFor.antitone_family, Cslib.MachineLearning.PACLearning.IsPACLearnerFor.mono_δ, Cslib.MachineLearning.PACLearning.IsPACLearnerFor.mono_ε, Cslib.MachineLearning.PACLearning.IsPACLearnerFor.antitone_C, Cslib.MachineLearning.PACLearning.IsRPACLearnerFor.antitone_family, Cslib.MachineLearning.PACLearning.IsRPACLearnerFor.mono_δ, Cslib.MachineLearning.PACLearning.IsPACLearnable, Cslib.MachineLearning.PACLearning.IsRPACLearnable, Cslib.MachineLearning.PACLearning.IsPACLearnable.toIsRPACLearnable, Cslib.MachineLearning.PACLearning.IsPACLearnable.antitone_family, Cslib.MachineLearning.PACLearning.IsPACLearnable.antitone_C, Cslib.MachineLearning.PACLearning.IsRPACLearnable.antitone_family, Cslib.MachineLearning.PACLearning.LearnerModel, Cslib.MachineLearning.PACLearning.sampleComplexity, Cslib.MachineLearning.PACLearning.rsampleComplexity, Cslib.MachineLearning.PACLearning.sampleComplexity_le_of_forall, Cslib.MachineLearning.PACLearning.sampleComplexity_antitone_δ, Cslib.MachineLearning.PACLearning.sampleComplexity_antitone_ε, Cslib.MachineLearning.PACLearning.sampleComplexity_mono_family, Cslib.MachineLearning.PACLearning.sampleComplexity_mono_C, Cslib.MachineLearning.PACLearning.rsampleComplexity_antitone_δ, Cslib.MachineLearning.PACLearning.rsampleComplexity_mono_family, Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_antitone_δ, Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_antitone_ε, Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_mono_family, Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_mono_C, Cslib.MachineLearning.PACLearning.IsRPACLearnable.rsampleComplexity_antitone_δ, Cslib.MachineLearning.PACLearning.IsRPACLearnable.rsampleComplexity_mono_family, Cslib.MachineLearning.PACLearning.hypothesisError, Cslib.MachineLearning.PACLearning.falsePositiveError, Cslib.MachineLearning.PACLearning.falseNegativeError, Cslib.MachineLearning.PACLearning.hypothesisError_eq_add, Cslib.MachineLearning.PACLearning.error_map_eq_hypothesisError
statement: formalized
proof: formalized
---

# PAC Learning

`Cslib.MachineLearning.PACLearning.Defs`, in [Cslib/MachineLearning/PACLearning/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean), by Samuel Schlesinger.

> This file defines the Probably Approximately Correct (PAC) learning model
> introduced by Valiant [Valiant1984], generalized to an arbitrary label type `β`
> and parameterized by a family of distributions `𝒟` on `α × β`.
>
> A concept class `C` over domain `α` with labels in `β` is a collection of
> functions `α → β`. A learning algorithm receives a labeled sample drawn i.i.d.
> from an unknown joint distribution `D` on `α × β` and must produce a hypothesis
> whose 0-1 error is within `ε` of the best concept in `C`, with probability at
> least `1 - δ`.
>
> The single definition `IsPACLearnerFor` captures the realizable, agnostic, and
> noise-tolerant settings by varying the distribution family `𝒟`:
>
> - **Agnostic** [Haussler1992]: `𝒟 = Set.univ` — the learner must work for all distributions.
> - **Realizable**: `𝒟` consists of pushforwards of arbitrary probability measures
>   `P` on `α` along the graph `x ↦ (x, c x)` of some concept `c ∈ C`, so that
>   `optimalError D C = 0`.
> - **Noise-tolerant** [AngluinLaird1988]: `𝒟` consists of noisy versions of realizable
>   distributions, where each label is corrupted independently with some probability `η`.
>
> The accuracy and confidence parameters `ε` and `δ` are elements of the subtype
> `Set.Ioo (0 : ℝ≥0) 1`, which bundles the value together with the proof that it
> lies in the open interval `(0, 1)`, ensuring the learning condition is non-vacuous.
>
> All declarations live under the `Cslib.MachineLearning.PACLearning` namespace so that
> generic names like `error` and `optimalError` do not pollute the parent namespace.
>
> ## Main definitions
>
> - `ConceptClass`: a set of functions `α → β` (classifiers).
> - `LabeledSample`: a finite sequence of `(point, label)` pairs.
> - `Learner`: a function from labeled samples to hypotheses.
> - `error`: the 0-1 error of a hypothesis under a joint distribution.
> - `optimalError`: the infimum of `error` over a concept class.
> - `IsPACLearnerFor`: deterministic `(ε, δ)`-PAC learner over a distribution family.
> - `IsRPACLearnerFor`: randomized variant of `IsPACLearnerFor`. Universe-polymorphic in the
>   randomness space `Ω : Type*`.
> - `IsPACLearnable`: a concept class is PAC learnable if `IsPACLearnerFor` holds for
>   all `ε, δ : Set.Ioo (0 : ℝ≥0) 1` with some sample size `m`.
> - `IsRPACLearnable`: randomized variant of `IsPACLearnable`. Pins the randomness space to
>   `Type 0`; `IsRPACLearnerFor` itself remains universe-polymorphic for users who need it.
> - `LearnerModel`: the common predicate shape `ℕ → ε → δ → C → 𝒟 → Prop` abstracting both
>   the deterministic and randomized learners so sample-complexity lemmas can be shared.
> - `sampleComplexity`: sample complexity of a generic learner model.
> - `rsampleComplexity`: randomized sample complexity, i.e. `sampleComplexity IsRPACLearnerFor`.
>
> ## Binary classification
>
> When `β = Bool`, concepts correspond to subsets of `α`. The section
> *Binary Classification* provides:
>
> - `hypothesisError`: the symmetric-difference error `P(h ∆ c)`.
> - `falsePositiveError`, `falseNegativeError`: its decomposition.
> - `hypothesisError_eq_add`: the decomposition theorem.
> - `error_map_eq_hypothesisError`: bridge between the general `error` and
>   the binary `hypothesisError` under a realizable distribution.
>
> ## Main statements
>
> - `IsPACLearnerFor.toIsRPACLearnerFor`: every deterministic PAC learner is a
>   randomized one (via the trivial randomness space `PUnit`).
> - `IsPACLearnerFor.antitone_family`, `.antitone_C`: the deterministic PAC learner
>   predicate is antitone in the distribution family and concept class.
> - `IsPACLearnerFor.mono_δ`, `.mono_ε`: the predicate is monotone in the confidence and
>   accuracy parameters (a weaker bound still holds).
> - `IsRPACLearnerFor.antitone_family`, `.mono_δ`: analogues for the randomized predicate.
>   (`mono_ε` and `antitone_C` are not provided because they change the integrand and
>   would require an extra measurability assumption.)
> - `IsPACLearnable.toIsRPACLearnable`: deterministic learnability implies randomized.
> - `IsPACLearnable.antitone_family`, `.antitone_C`, `IsRPACLearnable.antitone_family`:
>   PAC learnability is antitone in the distribution family and concept class.
> - `sampleComplexity_antitone_δ`, `_antitone_ε`, `_mono_family`, `_mono_C`: variation of
>   deterministic sample complexity in confidence, accuracy, distribution family, and concept
>   class (antitone in the numeric parameters, monotone under `⊆` in the set parameters). The
>   randomized analogues `rsampleComplexity_antitone_δ` and `_mono_family` are provided.
> - `IsPACLearnable.sampleComplexity_*`, `IsRPACLearnable.rsampleComplexity_*`: the same
>   monotonicity facts phrased with a learnability hypothesis in place of the ad-hoc
>   `∃ m, IsPACLearnerFor m …` existence witness, so callers who already know the class is
>   learnable need not thread it through.
> - `hypothesisError_eq_add`: total error = false positive + false negative.
>
> ## References
>
> * [L. G. Valiant, *A Theory of the Learnable*][Valiant1984]
> * [A. Ehrenfeucht, D. Haussler, M. Kearns, L. Valiant,
>   *A General Lower Bound on the Number of Examples Needed for Learning*][EHKV1989]
> * [M. J. Kearns, U. V. Vazirani,
>   *An Introduction to Computational Learning Theory*][KearnsVazirani1994]
> * [D. Haussler, *Decision Theoretic Generalizations of the PAC Model for Neural Net
>   and Other Learning Applications*][Haussler1992]
> * [D. Angluin, P. Laird, *Learning from Noisy Examples*][AngluinLaird1988]

> ### Core Definitions

`Cslib.MachineLearning.PACLearning.ConceptClass` (abbreviation, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L121))

> A *concept class* over domain `α` with label type `β` is a set of functions `α → β`.
> For binary classification (`β = Bool`), this is equivalent to a collection of subsets of `α`
> via the characteristic function.

```lean
abbrev ConceptClass (α β : Type*)
```

`Cslib.MachineLearning.PACLearning.LabeledSample` (abbreviation, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L125))

> A *labeled sample* of size `m` over domain `α` with label type `β` is a finite sequence
> of `(point, label)` pairs.

```lean
abbrev LabeledSample (α β : Type*) (m : ℕ)
```

`Cslib.MachineLearning.PACLearning.Learner` (abbreviation, [line 129](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L129))

> A *learner* using `m` samples is a function that takes a labeled sample and produces
> a hypothesis (a function from the domain to the label type).

```lean
abbrev Learner (α β : Type*) (m : ℕ)
```

`Cslib.MachineLearning.PACLearning.error` (definition, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L137))

> The *prediction error* (0-1 loss) of a hypothesis `h` under a joint distribution `D`
> on `α × β`, defined as the probability that the prediction disagrees with the label:
> `D({(x, y) | h(x) ≠ y})`.

```lean
noncomputable def error (D : Measure (α × β)) (h : α → β) : ℝ≥0∞
```

`Cslib.MachineLearning.PACLearning.optimalError` (definition, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L143))

> The *optimal error* of a concept class `C` under a joint distribution `D`, defined as the
> infimum of `error D c` over all concepts `c ∈ C`. When `C` is empty this is `⊤`, making the
> PAC learning condition vacuously true.

```lean
noncomputable def optimalError (D : Measure (α × β)) (C : ConceptClass α β) : ℝ≥0∞
```

> ### PAC Learners

`Cslib.MachineLearning.PACLearning.IsPACLearnerFor` (definition, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L158))

> `IsPACLearnerFor m ε δ C 𝒟` asserts that there exists a learner using `m` samples
> that is `(ε, δ)`-correct for the concept class `C` over the distribution family `𝒟`: for every
> probability measure `D ∈ 𝒟` on `α × β`, the probability (over i.i.d. samples from `D`) that
> the learner's hypothesis has error exceeding `opt_C(D) + ε` is at most `δ`.
>
> The parameters `ε` and `δ` are elements of `Set.Ioo (0 : ℝ≥0) 1`, bundling the value with
> the proof that it lies in `(0, 1)`. This ensures the condition is non-vacuous:
> `ε < 1` prevents the error threshold from exceeding the maximum possible error under a
> probability measure, and `δ < 1` prevents the confidence bound from being trivially
> satisfied.

```lean
def IsPACLearnerFor (m : ℕ) (ε δ : Set.Ioo (0 : ℝ≥0) 1)
    (C : ConceptClass α β) (𝒟 : Set (Measure (α × β))) : Prop
```

`Cslib.MachineLearning.PACLearning.IsRPACLearnerFor` (definition, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L181))

> `IsRPACLearnerFor m ε δ C 𝒟` asserts that there exists a *randomized* learner using
> `m` samples that is `(ε, δ)`-correct for the concept class `C` over the distribution family
> `𝒟`. A randomized learner draws internal randomness `ω` from a probability space `(Ω, Q)` and
> acts as the deterministic learner `A(ω)`.
>
> For every probability measure `D ∈ 𝒟`, the failure probability function
> `ω ↦ D^m{S | error(A(ω)(S)) > opt_C(D) + ε}` must be `Q`-a.e. measurable, and its
> expectation over `ω` must be at most `δ`.
>
> The randomness space `Ω : Type*` is universe-polymorphic; the universe is an implicit
> parameter of `IsRPACLearnerFor`, and downstream statements reference it via the pattern
> `IsRPACLearnerFor.{_, _, u}`. Fix `u := 0` for the usual case of a standard randomness space.
>
> A deterministic learner (`IsPACLearnerFor`) is the special case `Ω = PUnit`;
> see `IsPACLearnerFor.toIsRPACLearnerFor`.

```lean
def IsRPACLearnerFor (m : ℕ) (ε δ : Set.Ioo (0 : ℝ≥0) 1)
    (C : ConceptClass α β) (𝒟 : Set (Measure (α × β))) : Prop
```

`Cslib.MachineLearning.PACLearning.IsPACLearnerFor.toIsRPACLearnerFor` (theorem, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L195))

> Every deterministic PAC learner is in particular a randomized PAC learner
> (with the trivial one-point randomness space `PUnit`).

```lean
theorem IsPACLearnerFor.toIsRPACLearnerFor {m : ℕ} {ε δ : Set.Ioo (0 : ℝ≥0) 1}
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (h : IsPACLearnerFor m ε δ C 𝒟) :
    IsRPACLearnerFor m ε δ C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnerFor.antitone_family` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L208))

> The deterministic PAC learner predicate is antitone in the distribution family: a
> learner for a larger family `𝒟'` is also a learner for any subfamily `𝒟 ⊆ 𝒟'`.

```lean
theorem IsPACLearnerFor.antitone_family {m : ℕ} {ε δ : Set.Ioo (0 : ℝ≥0) 1}
    {C : ConceptClass α β} {𝒟 𝒟' : Set (Measure (α × β))}
    (h𝒟 : 𝒟 ⊆ 𝒟') (h : IsPACLearnerFor m ε δ C 𝒟') :
    IsPACLearnerFor m ε δ C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnerFor.mono_δ` (theorem, [line 217](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L217))

> A PAC learner with confidence `δ₁` is also a PAC learner with any weaker confidence
> `δ₂ ≥ δ₁`: the failure-probability bound only gets looser.

```lean
theorem IsPACLearnerFor.mono_δ {m : ℕ} {ε : Set.Ioo (0 : ℝ≥0) 1}
    {δ₁ δ₂ : Set.Ioo (0 : ℝ≥0) 1} (hδ : δ₁.val ≤ δ₂.val)
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (h : IsPACLearnerFor m ε δ₁ C 𝒟) :
    IsPACLearnerFor m ε δ₂ C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnerFor.mono_ε` (theorem, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L228))

> A PAC learner with accuracy `ε₁` is also a PAC learner with any weaker accuracy
> `ε₂ ≥ ε₁`: the bad event `{error > opt + ε}` only shrinks.

```lean
theorem IsPACLearnerFor.mono_ε {m : ℕ} {δ : Set.Ioo (0 : ℝ≥0) 1}
    {ε₁ ε₂ : Set.Ioo (0 : ℝ≥0) 1} (hε : ε₁.val ≤ ε₂.val)
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (h : IsPACLearnerFor m ε₁ δ C 𝒟) :
    IsPACLearnerFor m ε₂ δ C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnerFor.antitone_C` (theorem, [line 244](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L244))

> The deterministic PAC learner predicate is antitone in the concept class: a learner
> for a larger class `C'` is also a learner for any subclass `C ⊆ C'`, since the agnostic
> benchmark `optimalError _ C ≥ optimalError _ C'` makes the error requirement easier.

```lean
theorem IsPACLearnerFor.antitone_C {m : ℕ} {ε δ : Set.Ioo (0 : ℝ≥0) 1}
    {C C' : ConceptClass α β} (hC : C ⊆ C')
    {𝒟 : Set (Measure (α × β))} (h : IsPACLearnerFor m ε δ C' 𝒟) :
    IsPACLearnerFor m ε δ C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsRPACLearnerFor.antitone_family` (theorem, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L258))

> The randomized PAC learner predicate is antitone in the distribution family. The
> universe of the randomness space `Ω` is pinned so the hypothesis and conclusion share it.

```lean
theorem IsRPACLearnerFor.antitone_family.{u} {m : ℕ} {ε δ : Set.Ioo (0 : ℝ≥0) 1}
    {C : ConceptClass α β} {𝒟 𝒟' : Set (Measure (α × β))}
    (h𝒟 : 𝒟 ⊆ 𝒟') (h : IsRPACLearnerFor.{_, _, u} m ε δ C 𝒟') :
    IsRPACLearnerFor.{_, _, u} m ε δ C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsRPACLearnerFor.mono_δ` (theorem, [line 268](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L268))

> A randomized PAC learner with confidence `δ₁` is also a randomized PAC learner with
> any weaker confidence `δ₂ ≥ δ₁`. Unlike `mono_ε` or `antitone_C`, this does not touch the
> integrand, so it carries the `AEMeasurable` part through unchanged.

```lean
theorem IsRPACLearnerFor.mono_δ.{u} {m : ℕ} {ε : Set.Ioo (0 : ℝ≥0) 1}
    {δ₁ δ₂ : Set.Ioo (0 : ℝ≥0) 1} (hδ : δ₁.val ≤ δ₂.val)
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (h : IsRPACLearnerFor.{_, _, u} m ε δ₁ C 𝒟) :
    IsRPACLearnerFor.{_, _, u} m ε δ₂ C 𝒟
```

> ### PAC Learnability

`Cslib.MachineLearning.PACLearning.IsPACLearnable` (definition, [line 285](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L285))

> A concept class `C` is *PAC learnable* over the distribution family `𝒟` if for every
> accuracy `ε ∈ (0, 1)` and confidence `δ ∈ (0, 1)`, there exists a sample size `m` admitting
> a deterministic `(ε, δ)`-PAC learner for `C`. Here `ε` and `δ` are elements of the subtype
> `Set.Ioo (0 : ℝ≥0) 1`.

```lean
def IsPACLearnable (C : ConceptClass α β) (𝒟 : Set (Measure (α × β))) : Prop
```

`Cslib.MachineLearning.PACLearning.IsRPACLearnable` (definition, [line 293](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L293))

> A concept class `C` is *randomized PAC learnable* over the distribution family `𝒟` if for
> every accuracy `ε ∈ (0, 1)` and confidence `δ ∈ (0, 1)`, there exists a sample size `m`
> admitting a randomized `(ε, δ)`-PAC learner for `C`. The randomness space is pinned to
> `Type 0` at the learnability level; `IsRPACLearnerFor` itself remains universe-polymorphic.

```lean
def IsRPACLearnable (C : ConceptClass α β) (𝒟 : Set (Measure (α × β))) : Prop
```

`Cslib.MachineLearning.PACLearning.IsPACLearnable.toIsRPACLearnable` (theorem, [line 298](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L298))

> Deterministic PAC learnability implies randomized PAC learnability.

```lean
theorem IsPACLearnable.toIsRPACLearnable {C : ConceptClass α β}
    {𝒟 : Set (Measure (α × β))} (h : IsPACLearnable C 𝒟) :
    IsRPACLearnable C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnable.antitone_family` (theorem, [line 307](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L307))

> PAC learnability is antitone in the distribution family: a subfamily of a learnable
> family is learnable.

```lean
theorem IsPACLearnable.antitone_family {C : ConceptClass α β} {𝒟 𝒟' : Set (Measure (α × β))}
    (h𝒟 : 𝒟 ⊆ 𝒟') (h : IsPACLearnable C 𝒟') : IsPACLearnable C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnable.antitone_C` (theorem, [line 313](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L313))

> PAC learnability is antitone in the concept class: a subclass of a learnable class is
> learnable.

```lean
theorem IsPACLearnable.antitone_C {C C' : ConceptClass α β} (hC : C ⊆ C')
    {𝒟 : Set (Measure (α × β))} (h : IsPACLearnable C' 𝒟) : IsPACLearnable C 𝒟
```

`Cslib.MachineLearning.PACLearning.IsRPACLearnable.antitone_family` (theorem, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L318))

> Randomized PAC learnability is antitone in the distribution family.

```lean
theorem IsRPACLearnable.antitone_family {C : ConceptClass α β}
    {𝒟 𝒟' : Set (Measure (α × β))} (h𝒟 : 𝒟 ⊆ 𝒟')
    (h : IsRPACLearnable C 𝒟') : IsRPACLearnable C 𝒟
```

> ### Sample Complexity

`Cslib.MachineLearning.PACLearning.LearnerModel` (abbreviation, [line 329](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L329))

> A *learner model* is a predicate on (sample size, accuracy, confidence, concept class,
> distribution family) that classifies which sample sizes admit a learner of the given kind.
> Instantiating with `IsPACLearnerFor` gives the deterministic model; with `IsRPACLearnerFor`
> gives the randomized one.

```lean
abbrev LearnerModel (α β : Type*) [MeasurableSpace α] [MeasurableSpace β]
```

`Cslib.MachineLearning.PACLearning.sampleComplexity` (definition, [line 342](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L342))

> The *sample complexity* of a concept class `C` under a learner model `L`, at accuracy
> `ε ∈ (0, 1)` and confidence `δ ∈ (0, 1)` over distribution family `𝒟`, is the smallest sample
> size `m` with `L m ε δ C 𝒟`. Specialize with `L := IsPACLearnerFor` for the deterministic model
> and `L := IsRPACLearnerFor` for the randomized one.
>
> **Caveat**: because `sInf` on `ℕ` returns `0` for the empty set, this definition returns `0`
> when no learner exists (e.g., a concept class of infinite VC dimension). It is only meaningful
> when the defining set `{m | L m ε δ C 𝒟}` is nonempty. The `IsPACLearnable.sampleComplexity_*`
> variants below discharge this nonemptiness from a learnability hypothesis.

```lean
noncomputable def sampleComplexity (L : LearnerModel α β) (C : ConceptClass α β)
    (ε δ : Set.Ioo (0 : ℝ≥0) 1) (𝒟 : Set (Measure (α × β))) : ℕ
```

`Cslib.MachineLearning.PACLearning.rsampleComplexity` (definition, [line 348](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L348))

> The *randomized sample complexity* of `C`, i.e. `sampleComplexity` instantiated at the
> randomized learner model `IsRPACLearnerFor`. The randomness space is pinned to `Type 0`.

```lean
noncomputable def rsampleComplexity (C : ConceptClass α β) (ε δ : Set.Ioo (0 : ℝ≥0) 1)
    (𝒟 : Set (Measure (α × β))) : ℕ
```

> ### Monotonicity of Sample Complexity
>
> These lemmas are all special cases of the following observation: if `{m | L₁ m ε₁ δ₁ C₁ 𝒟₁} ⊆
> {m | L₂ m ε₂ δ₂ C₂ 𝒟₂}` and the first set is nonempty, then the sample complexity under
> `(L₂, ε₂, δ₂, C₂, 𝒟₂)` is at most the sample complexity under `(L₁, ε₁, δ₁, C₁, 𝒟₁)`. The
> nonemptiness hypothesis is essential: `sInf` on `ℕ` returns `0` for an empty set, so without
> it the inequality can fail at the degenerate boundary. The `IsPACLearnable`-flavoured variants
> at the end of this section discharge that witness from a learnability hypothesis.

`Cslib.MachineLearning.PACLearning.sampleComplexity_le_of_forall` (theorem, [line 364](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L364))

> General pointwise monotonicity of `sampleComplexity`: if every witness sample size for
> `(L₁, ε₁, δ₁, C₁, 𝒟₁)` is also a witness for `(L₂, ε₂, δ₂, C₂, 𝒟₂)`, then the latter's
> sample complexity is at most the former's (provided the former is attained).

```lean
theorem sampleComplexity_le_of_forall {L₁ L₂ : LearnerModel α β}
    {ε₁ δ₁ ε₂ δ₂ : Set.Ioo (0 : ℝ≥0) 1} {C₁ C₂ : ConceptClass α β}
    {𝒟₁ 𝒟₂ : Set (Measure (α × β))}
    (hL : ∀ {m : ℕ}, L₁ m ε₁ δ₁ C₁ 𝒟₁ → L₂ m ε₂ δ₂ C₂ 𝒟₂)
    (h : ∃ m, L₁ m ε₁ δ₁ C₁ 𝒟₁) :
    sampleComplexity L₂ C₂ ε₂ δ₂ 𝒟₂ ≤ sampleComplexity L₁ C₁ ε₁ δ₁ 𝒟₁
```

`Cslib.MachineLearning.PACLearning.sampleComplexity_antitone_δ` (theorem, [line 374](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L374))

> Deterministic sample complexity is antitone in the confidence parameter `δ`: weaker
> confidence requires no more samples.

```lean
theorem sampleComplexity_antitone_δ {ε δ₁ δ₂ : Set.Ioo (0 : ℝ≥0) 1} (hδ : δ₁.val ≤ δ₂.val)
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (h : ∃ m, IsPACLearnerFor m ε δ₁ C 𝒟) :
    sampleComplexity IsPACLearnerFor C ε δ₂ 𝒟 ≤ sampleComplexity IsPACLearnerFor C ε δ₁ 𝒟
```

`Cslib.MachineLearning.PACLearning.sampleComplexity_antitone_ε` (theorem, [line 382](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L382))

> Deterministic sample complexity is antitone in the accuracy parameter `ε`: weaker
> accuracy requires no more samples.

```lean
theorem sampleComplexity_antitone_ε {ε₁ ε₂ δ : Set.Ioo (0 : ℝ≥0) 1} (hε : ε₁.val ≤ ε₂.val)
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (h : ∃ m, IsPACLearnerFor m ε₁ δ C 𝒟) :
    sampleComplexity IsPACLearnerFor C ε₂ δ 𝒟 ≤ sampleComplexity IsPACLearnerFor C ε₁ δ 𝒟
```

`Cslib.MachineLearning.PACLearning.sampleComplexity_mono_family` (theorem, [line 390](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L390))

> Deterministic sample complexity is monotone in the distribution family under `⊆`: a
> smaller family (fewer distributions to cover) requires no more samples.

```lean
theorem sampleComplexity_mono_family {ε δ : Set.Ioo (0 : ℝ≥0) 1}
    {C : ConceptClass α β} {𝒟 𝒟' : Set (Measure (α × β))} (h𝒟 : 𝒟 ⊆ 𝒟')
    (h : ∃ m, IsPACLearnerFor m ε δ C 𝒟') :
    sampleComplexity IsPACLearnerFor C ε δ 𝒟 ≤ sampleComplexity IsPACLearnerFor C ε δ 𝒟'
```

`Cslib.MachineLearning.PACLearning.sampleComplexity_mono_C` (theorem, [line 398](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L398))

> Deterministic sample complexity is monotone in the concept class under `⊆`: a smaller
> class (weaker agnostic benchmark) requires no more samples.

```lean
theorem sampleComplexity_mono_C {ε δ : Set.Ioo (0 : ℝ≥0) 1}
    {C C' : ConceptClass α β} (hC : C ⊆ C') {𝒟 : Set (Measure (α × β))}
    (h : ∃ m, IsPACLearnerFor m ε δ C' 𝒟) :
    sampleComplexity IsPACLearnerFor C ε δ 𝒟 ≤ sampleComplexity IsPACLearnerFor C' ε δ 𝒟
```

`Cslib.MachineLearning.PACLearning.rsampleComplexity_antitone_δ` (theorem, [line 405](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L405))

> Randomized sample complexity is antitone in the confidence parameter `δ`.

```lean
theorem rsampleComplexity_antitone_δ {ε δ₁ δ₂ : Set.Ioo (0 : ℝ≥0) 1}
    (hδ : δ₁.val ≤ δ₂.val) {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (h : ∃ m, IsRPACLearnerFor.{_, _, 0} m ε δ₁ C 𝒟) :
    rsampleComplexity C ε δ₂ 𝒟 ≤ rsampleComplexity C ε δ₁ 𝒟
```

`Cslib.MachineLearning.PACLearning.rsampleComplexity_mono_family` (theorem, [line 412](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L412))

> Randomized sample complexity is monotone in the distribution family under `⊆`.

```lean
theorem rsampleComplexity_mono_family {ε δ : Set.Ioo (0 : ℝ≥0) 1}
    {C : ConceptClass α β} {𝒟 𝒟' : Set (Measure (α × β))} (h𝒟 : 𝒟 ⊆ 𝒟')
    (h : ∃ m, IsRPACLearnerFor.{_, _, 0} m ε δ C 𝒟') :
    rsampleComplexity C ε δ 𝒟 ≤ rsampleComplexity C ε δ 𝒟'
```

> Convenience variants conditional on learnability, which discharge the nonemptiness
> hypothesis `(∃ m, IsPACLearnerFor m …)` from an `IsPACLearnable` / `IsRPACLearnable` witness.
> Bodies go through `sampleComplexity_le_of_forall` directly rather than the top-level
> `sampleComplexity_*` lemmas, whose unqualified names would resolve as self-recursion inside
> these theorems' `IsPACLearnable.*` / `IsRPACLearnable.*` namespaces.

`Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_antitone_δ` (theorem, [line 426](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L426))

> `sampleComplexity_antitone_δ` for a learnable class: the nonemptiness hypothesis comes
> for free from `IsPACLearnable`.

```lean
theorem IsPACLearnable.sampleComplexity_antitone_δ
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))} (hL : IsPACLearnable C 𝒟)
    {ε δ₁ δ₂ : Set.Ioo (0 : ℝ≥0) 1} (hδ : δ₁.val ≤ δ₂.val) :
    sampleComplexity IsPACLearnerFor C ε δ₂ 𝒟 ≤ sampleComplexity IsPACLearnerFor C ε δ₁ 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_antitone_ε` (theorem, [line 433](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L433))

> `sampleComplexity_antitone_ε` for a learnable class.

```lean
theorem IsPACLearnable.sampleComplexity_antitone_ε
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))} (hL : IsPACLearnable C 𝒟)
    {ε₁ ε₂ δ : Set.Ioo (0 : ℝ≥0) 1} (hε : ε₁.val ≤ ε₂.val) :
    sampleComplexity IsPACLearnerFor C ε₂ δ 𝒟 ≤ sampleComplexity IsPACLearnerFor C ε₁ δ 𝒟
```

`Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_mono_family` (theorem, [line 441](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L441))

> `sampleComplexity_mono_family` for a learnable class (learnability at the *larger*
> family `𝒟'` is the hypothesis).

```lean
theorem IsPACLearnable.sampleComplexity_mono_family
    {C : ConceptClass α β} {𝒟 𝒟' : Set (Measure (α × β))}
    (hL : IsPACLearnable C 𝒟') (h𝒟 : 𝒟 ⊆ 𝒟') {ε δ : Set.Ioo (0 : ℝ≥0) 1} :
    sampleComplexity IsPACLearnerFor C ε δ 𝒟 ≤ sampleComplexity IsPACLearnerFor C ε δ 𝒟'
```

`Cslib.MachineLearning.PACLearning.IsPACLearnable.sampleComplexity_mono_C` (theorem, [line 449](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L449))

> `sampleComplexity_mono_C` for a learnable class (learnability at the *larger* class
> `C'` is the hypothesis).

```lean
theorem IsPACLearnable.sampleComplexity_mono_C
    {C C' : ConceptClass α β} {𝒟 : Set (Measure (α × β))}
    (hL : IsPACLearnable C' 𝒟) (hC : C ⊆ C') {ε δ : Set.Ioo (0 : ℝ≥0) 1} :
    sampleComplexity IsPACLearnerFor C ε δ 𝒟 ≤ sampleComplexity IsPACLearnerFor C' ε δ 𝒟
```

`Cslib.MachineLearning.PACLearning.IsRPACLearnable.rsampleComplexity_antitone_δ` (theorem, [line 456](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L456))

> `rsampleComplexity_antitone_δ` for a randomized-learnable class.

```lean
theorem IsRPACLearnable.rsampleComplexity_antitone_δ
    {C : ConceptClass α β} {𝒟 : Set (Measure (α × β))} (hL : IsRPACLearnable C 𝒟)
    {ε δ₁ δ₂ : Set.Ioo (0 : ℝ≥0) 1} (hδ : δ₁.val ≤ δ₂.val) :
    rsampleComplexity C ε δ₂ 𝒟 ≤ rsampleComplexity C ε δ₁ 𝒟
```

`Cslib.MachineLearning.PACLearning.IsRPACLearnable.rsampleComplexity_mono_family` (theorem, [line 463](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L463))

> `rsampleComplexity_mono_family` for a randomized-learnable class.

```lean
theorem IsRPACLearnable.rsampleComplexity_mono_family
    {C : ConceptClass α β} {𝒟 𝒟' : Set (Measure (α × β))}
    (hL : IsRPACLearnable C 𝒟') (h𝒟 : 𝒟 ⊆ 𝒟') {ε δ : Set.Ioo (0 : ℝ≥0) 1} :
    rsampleComplexity C ε δ 𝒟 ≤ rsampleComplexity C ε δ 𝒟'
```

> ### Binary Classification
>
> When `β = Bool`, concepts correspond to subsets of `α` via the characteristic function.
> The symmetric-difference error `P(h ∆ c)` is the natural error metric, and it decomposes
> into false positive and false negative components.
>
> The bridge lemma `error_map_eq_hypothesisError` connects the general `error` on `α × Bool`
> to the binary `hypothesisError` on `α`, showing they coincide for realizable distributions.

`Cslib.MachineLearning.PACLearning.hypothesisError` (definition, [line 485](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L485))

> The *symmetric-difference error* of a hypothesis `h` with respect to a target concept `c`
> (both viewed as subsets of `α`) under distribution `P`, defined as `P(h ∆ c)`.

```lean
noncomputable def hypothesisError (P : Measure α) (h c : Set α) : ℝ≥0∞
```

`Cslib.MachineLearning.PACLearning.falsePositiveError` (definition, [line 490](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L490))

> The *false positive error* `P(h \ c)` — points classified positive but not in the
> concept.

```lean
noncomputable def falsePositiveError (P : Measure α) (h c : Set α) : ℝ≥0∞
```

`Cslib.MachineLearning.PACLearning.falseNegativeError` (definition, [line 494](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L494))

> The *false negative error* `P(c \ h)` — points in the concept but classified negative.

```lean
noncomputable def falseNegativeError (P : Measure α) (h c : Set α) : ℝ≥0∞
```

`Cslib.MachineLearning.PACLearning.hypothesisError_eq_add` (theorem, [line 499](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L499))

> The total hypothesis error decomposes as the sum of false positive and false negative
> errors, since `h ∆ c = (h \ c) ∪ (c \ h)` is a disjoint union.

```lean
theorem hypothesisError_eq_add {P : Measure α} {h c : Set α}
    (hh : MeasurableSet h) (hc : MeasurableSet c) :
    hypothesisError P h c = falsePositiveError P h c + falseNegativeError P h c
```

`Cslib.MachineLearning.PACLearning.error_map_eq_hypothesisError` (theorem, [line 508](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean#L508))

> Under a realizable distribution `P.map (x ↦ (x, c(x)))`, the general 0-1 `error`
> coincides with the binary `hypothesisError P h c`, where `h` and `c` are viewed as subsets
> of `α` via the characteristic function `decide (· ∈ ·)`.

```lean
theorem error_map_eq_hypothesisError (P : Measure α) (h c : Set α)
    (hh : MeasurableSet h) (hc : MeasurableSet c) :
    error (P.map (fun x => (x, decide (x ∈ c)))) (fun x => decide (x ∈ h)) =
    hypothesisError P h c
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/MachineLearning/PACLearning/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/Defs.lean)
