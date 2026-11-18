---
catalog: module
lean: Cslib.MachineLearning.PACLearning.VersionSpace, Cslib.MachineLearning.PACLearning.mem_versionSpace_iff, Cslib.MachineLearning.PACLearning.versionSpace_subset, Cslib.MachineLearning.PACLearning.versionSpace_empty_sample, Cslib.MachineLearning.PACLearning.versionSpace_reindex, Cslib.MachineLearning.PACLearning.versionSpace_antitone, Cslib.MachineLearning.PACLearning.versionSpace_mono_C, Cslib.MachineLearning.PACLearning.empiricalMiscount, Cslib.MachineLearning.PACLearning.empiricalMeasure, Cslib.MachineLearning.PACLearning.empiricalError, Cslib.MachineLearning.PACLearning.mem_versionSpace_iff_empiricalMiscount_zero, Cslib.MachineLearning.PACLearning.mem_versionSpace_iff_empiricalError_zero, Cslib.MachineLearning.PACLearning.empiricalError_eq_div, Cslib.MachineLearning.PACLearning.Realizable, Cslib.MachineLearning.PACLearning.IsConsistent, Cslib.MachineLearning.PACLearning.IsConsistent.output_mem_conceptClass, Cslib.MachineLearning.PACLearning.IsConsistent.output_agrees, Cslib.MachineLearning.PACLearning.IsConsistent.empiricalMiscount_eq_zero, Cslib.MachineLearning.PACLearning.IsConsistent.empiricalError_eq_zero, Cslib.MachineLearning.PACLearning.mem_versionSpace_of_realizable, Cslib.MachineLearning.PACLearning.Realizable.versionSpace_nonempty, Cslib.MachineLearning.PACLearning.ae_mem_versionSpace_of_realizable
statement: formalized
proof: formalized
---

# Version Space

`Cslib.MachineLearning.PACLearning.VersionSpace`, in [Cslib/MachineLearning/PACLearning/VersionSpace.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean), by Dhruv Gupta.

> The *version space* of a concept class `C` given a labeled sample `S` is the
> subset of `C` whose concepts agree with `S` on every observed point — the
> classical "concepts still consistent with the data" of Mitchell (1977) and
> Angluin (1980).
>
> ## Main definitions
>
> - `VersionSpace C S`: the subset of `C` whose concepts agree with `S` on every
>   sample point.
> - `IsConsistent A C`: a learner is consistent with `C` if its output lies in
>   the version space at every realizable sample.
> - `empiricalMiscount h S`: number of sample points where `h` errs (`[DecidableEq β]`).
> - `empiricalMeasure S`: the uniform Dirac mixture over the sample.
> - `empiricalError h S`: the empirical distribution's mass on the disagreement set.
> - `Realizable C S`: some concept in `C` labels every sample point correctly.
>
> ## Main results
>
> - `versionSpace_subset`, `versionSpace_empty_sample`, `versionSpace_reindex`,
>   `versionSpace_antitone`, `versionSpace_mono_C`: structural properties.
> - `mem_versionSpace_iff_empiricalMiscount_zero`: combinatorial bridge.
> - `mem_versionSpace_iff_empiricalError_zero`: measure-theoretic bridge.
> - `IsConsistent.empiricalMiscount_eq_zero`, `IsConsistent.empiricalError_eq_zero`:
>   consistent learners achieve zero error / miscount on every realizable sample.
> - `mem_versionSpace_of_realizable`, `Realizable.versionSpace_nonempty`: realizable
>   samples give non-empty version spaces.
> - `ae_mem_versionSpace_of_realizable`: under iid sampling from a realizable
>   joint distribution, the target concept lies in the version space almost surely.
>
> ## References
>
> * [Mitchell1977]
> * [Mitchell1982]
> * [Angluin1980]
> * [Mitchell1997]

> ### Version Space

`Cslib.MachineLearning.PACLearning.VersionSpace` (definition, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L65))

> The *version space* of a concept class `C` given a labeled sample `S`:
> the set of concepts in `C` whose labels agree with `S` on every observed point.

```lean
def VersionSpace {m : ℕ} (C : ConceptClass α β) (S : LabeledSample α β m) :
    ConceptClass α β
```

`Cslib.MachineLearning.PACLearning.mem_versionSpace_iff` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L71))

> Membership in the version space unfolds to concept membership plus
> per-sample consistency.

```lean
theorem mem_versionSpace_iff {m : ℕ} {C : ConceptClass α β}
    {S : LabeledSample α β m} {h : α → β} :
    h ∈ VersionSpace C S ↔ h ∈ C ∧ ∀ i : Fin m, h (S i).1 = (S i).2
```

`Cslib.MachineLearning.PACLearning.versionSpace_subset` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L76))

> The version space is a subset of the original concept class.

```lean
theorem versionSpace_subset {m : ℕ} (C : ConceptClass α β)
    (S : LabeledSample α β m) :
    VersionSpace C S ⊆ C
```

`Cslib.MachineLearning.PACLearning.versionSpace_empty_sample` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L81))

> Version space on the empty sample equals the whole concept class.

```lean
theorem versionSpace_empty_sample (C : ConceptClass α β)
    (S : LabeledSample α β 0) :
    VersionSpace C S = C
```

`Cslib.MachineLearning.PACLearning.versionSpace_reindex` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L90))

> *Version space reindexing.* For any reindexing `f : Fin m → Fin n`, the
> version space on `S` is contained in the version space on the reindexed sample
> `S ∘ f`.

```lean
theorem versionSpace_reindex {m n : ℕ} (f : Fin m → Fin n) (C : ConceptClass α β)
    (S : LabeledSample α β n) :
    VersionSpace C S ⊆ VersionSpace C (S ∘ f)
```

`Cslib.MachineLearning.PACLearning.versionSpace_antitone` (theorem, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L99))

> *Version space antitonicity.* Given a sample of size `n` and `m ≤ n`, the
> version space on all `n` observations is a subset of the version space on the
> first `m` observations. Special case of `versionSpace_reindex` with
> `f := Fin.castLE hmn`.

```lean
theorem versionSpace_antitone {m n : ℕ} (hmn : m ≤ n) (C : ConceptClass α β)
    (S : LabeledSample α β n) :
    VersionSpace C S ⊆ VersionSpace C (S ∘ Fin.castLE hmn)
```

`Cslib.MachineLearning.PACLearning.versionSpace_mono_C` (theorem, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L105))

> *Version space is monotone in the concept class.*

```lean
theorem versionSpace_mono_C {m : ℕ} {C C' : ConceptClass α β} (hCC' : C ⊆ C')
    (S : LabeledSample α β m) :
    VersionSpace C S ⊆ VersionSpace C' S
```

> ### Empirical Error

`Cslib.MachineLearning.PACLearning.empiricalMiscount` (definition, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L114))

> The *empirical miscount* of a hypothesis `h` on a labeled sample `S`: the
> number of sample points where `h` predicts incorrectly.

```lean
def empiricalMiscount [DecidableEq β] {m : ℕ} (h : α → β)
    (S : LabeledSample α β m) : ℕ
```

`Cslib.MachineLearning.PACLearning.empiricalMeasure` (definition, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L123))

> The *empirical distribution* of a labeled sample: the uniform mixture of
> Dirac measures at each sample point. Equals the zero measure when `m = 0`.

```lean
noncomputable def empiricalMeasure {m : ℕ} (S : LabeledSample α β m) :
    Measure (α × β)
```

`Cslib.MachineLearning.PACLearning.empiricalError` (definition, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L130))

> The *empirical 0-1 error* of `h` on `S`: the empirical distribution's
> mass on the disagreement set.

```lean
noncomputable def empiricalError {m : ℕ} (h : α → β) (S : LabeledSample α β m) :
    ℝ≥0∞
```

`Cslib.MachineLearning.PACLearning.mem_versionSpace_iff_empiricalMiscount_zero` (theorem, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L138))

> Version-space membership equals concept-class membership plus zero empirical
> miscount (combinatorial bridge).

```lean
theorem mem_versionSpace_iff_empiricalMiscount_zero [DecidableEq β]
    {m : ℕ} {C : ConceptClass α β} {S : LabeledSample α β m} {h : α → β} :
    h ∈ VersionSpace C S ↔ h ∈ C ∧ empiricalMiscount h S = 0
```

`Cslib.MachineLearning.PACLearning.mem_versionSpace_iff_empiricalError_zero` (theorem, [line 147](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L147))

> Version-space membership equals concept-class membership plus zero empirical
> error (measure-theoretic bridge).

```lean
theorem mem_versionSpace_iff_empiricalError_zero
    [MeasurableSpace α] [MeasurableSpace β]
    [MeasurableSingletonClass α] [MeasurableSingletonClass β]
    {m : ℕ} {C : ConceptClass α β} {S : LabeledSample α β m} {h : α → β} :
    h ∈ VersionSpace C S ↔ h ∈ C ∧ empiricalError h S = 0
```

`Cslib.MachineLearning.PACLearning.empiricalError_eq_div` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L161))

> The empirical 0-1 error equals the empirical miscount divided by the
> sample size.

```lean
theorem empiricalError_eq_div [DecidableEq β]
    [MeasurableSpace α] [MeasurableSpace β]
    [MeasurableSingletonClass α] [MeasurableSingletonClass β]
    {m : ℕ} (hm : 0 < m) (h : α → β) (S : LabeledSample α β m) :
    empiricalError h S = (empiricalMiscount h S : ℝ≥0∞) / m
```

> ### Realizable Samples

`Cslib.MachineLearning.PACLearning.Realizable` (definition, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L176))

> A labeled sample `S` is *realizable* by concept class `C` if some concept
> in `C` labels every sample point correctly.

```lean
def Realizable {m : ℕ} (C : ConceptClass α β) (S : LabeledSample α β m) : Prop
```

> ### Consistent Learners

`Cslib.MachineLearning.PACLearning.IsConsistent` (definition, [line 185](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L185))

> A learner is *consistent* with the concept class `C` if, on every sample
> realizable by `C`, its output hypothesis lies in the version space of `C` at
> that sample — i.e. the output is in `C` and agrees with every observed labeled
> pair. No condition is imposed on samples that no concept in `C` can realize.

```lean
def IsConsistent {m : ℕ} (A : Learner α β m) (C : ConceptClass α β) : Prop
```

`Cslib.MachineLearning.PACLearning.IsConsistent.output_mem_conceptClass` (theorem, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L189))

> A consistent learner's output is in the concept class on every realizable sample.

```lean
theorem IsConsistent.output_mem_conceptClass {m : ℕ} {A : Learner α β m}
    {C : ConceptClass α β} (hA : IsConsistent A C) (S : LabeledSample α β m)
    (hS : Realizable C S) :
    A S ∈ C
```

`Cslib.MachineLearning.PACLearning.IsConsistent.output_agrees` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L196))

> On every realizable sample, a consistent learner's output agrees with
> every observed point.

```lean
theorem IsConsistent.output_agrees {m : ℕ} {A : Learner α β m}
    {C : ConceptClass α β} (hA : IsConsistent A C) (S : LabeledSample α β m)
    (hS : Realizable C S) (i : Fin m) :
    A S (S i).1 = (S i).2
```

`Cslib.MachineLearning.PACLearning.IsConsistent.empiricalMiscount_eq_zero` (theorem, [line 202](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L202))

> A consistent learner has zero empirical miscount on every realizable sample.

```lean
theorem IsConsistent.empiricalMiscount_eq_zero [DecidableEq β]
    {m : ℕ} {A : Learner α β m} {C : ConceptClass α β} (hA : IsConsistent A C)
    (S : LabeledSample α β m) (hS : Realizable C S) :
    empiricalMiscount (A S) S = 0
```

`Cslib.MachineLearning.PACLearning.IsConsistent.empiricalError_eq_zero` (theorem, [line 209](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L209))

> A consistent learner has zero empirical error on every realizable sample.

```lean
theorem IsConsistent.empiricalError_eq_zero
    [MeasurableSpace α] [MeasurableSpace β]
    [MeasurableSingletonClass α] [MeasurableSingletonClass β]
    {m : ℕ} {A : Learner α β m} {C : ConceptClass α β}
    (hA : IsConsistent A C) (S : LabeledSample α β m) (hS : Realizable C S) :
    empiricalError (A S) S = 0
```

> ### Realizable Version Spaces

`Cslib.MachineLearning.PACLearning.mem_versionSpace_of_realizable` (theorem, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L222))

> *Realizable version-space nonemptiness.* If a target concept `c` lies in
> `C` and the sample `S` is labeled by `c` (i.e. every `(S i).2 = c (S i).1`),
> then `c` itself lies in the version space `VersionSpace C S`.

```lean
theorem mem_versionSpace_of_realizable {m : ℕ} {C : ConceptClass α β}
    {c : α → β} (hc : c ∈ C) (S : LabeledSample α β m)
    (hS : ∀ i : Fin m, (S i).2 = c (S i).1) :
    c ∈ VersionSpace C S
```

`Cslib.MachineLearning.PACLearning.Realizable.versionSpace_nonempty` (theorem, [line 229](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L229))

> A realizable sample has nonempty version space.

```lean
theorem Realizable.versionSpace_nonempty {m : ℕ} {C : ConceptClass α β}
    {S : LabeledSample α β m} (h : Realizable C S) :
    (VersionSpace C S).Nonempty
```

> ### Probabilistic Realizable

`Cslib.MachineLearning.PACLearning.ae_mem_versionSpace_of_realizable` (theorem, [line 263](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean#L263))

> Under iid sampling from the realizable joint distribution induced by
> `c ∈ C` and a probability measure `P` on `α`, the target concept `c` lies in
> the version space almost surely.

```lean
theorem ae_mem_versionSpace_of_realizable
    [MeasurableSpace α] [MeasurableSpace β]
    {C : ConceptClass α β} {c : α → β} (hc : c ∈ C) (hcm : Measurable c)
    (hG : MeasurableSet {p : α × β | p.2 = c p.1})
    (P : Measure α) [IsProbabilityMeasure P] (m : ℕ) :
    ∀ᵐ S : LabeledSample α β m
      ∂(Measure.pi (fun _ : Fin m => P.map (fun x => (x, c x)))),
      c ∈ VersionSpace C S
```

## Depends on

- [PAC Learning](defs.md)

## Sources

- [Cslib/MachineLearning/PACLearning/VersionSpace.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VersionSpace.lean)
