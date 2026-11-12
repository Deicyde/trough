---
catalog: module
lean: Cslib.LTS, Cslib.LTS.UnlabelledTr, Cslib.LTS.IsTerminal, Cslib.LTS.MTr, Cslib.LTS.MTr.nil_eq, Cslib.LTS.MTr.nil_iff, Cslib.LTS.MTr.single, Cslib.LTS.MTr.cons_iff, Cslib.LTS.MTr.stepR, Cslib.LTS.MTr.comp, Cslib.LTS.MTr.single_invert, Cslib.LTS.MTr.singleton_iff, Cslib.LTS.MTr.split, Cslib.LTS.MTr.append_iff, Cslib.LTS.TrInv, Cslib.LTS.MTrInv, Cslib.LTS.mtrInv_of_trInv, Cslib.LTS.CanReach, Cslib.LTS.CanReach.refl, Cslib.LTS.generatedBy, Cslib.LTS.traces, Cslib.LTS.completeTraces, Cslib.LTS.mem_traces_iff, Cslib.LTS.mem_traces_singleton_iff, Cslib.LTS.mem_traces_cons_iff, Cslib.LTS.traces_in, Cslib.LTS.image, Cslib.LTS.DeterministicStateLabel, Cslib.LTS.deterministicStateLabel_iff_subsingleton_image, Cslib.LTS.DeterministicState, Cslib.LTS.deterministicState_iff_subsingleton_image, Cslib.LTS.Deterministic, Cslib.LTS.deterministic_iff_subsingleton_image, Cslib.LTS.Deterministic.eq_of_tr, Cslib.LTS.Deterministic.eq_of_mTr, Cslib.LTS.imageMultistep, Cslib.LTS.ImageFinite, Cslib.LTS.DeterministicStateLabel.not_tr_of_ne, Cslib.LTS.DeterministicStateLabel.image_singleton_iff_tr, Cslib.LTS.DeterministicStateLabel.image_char, Cslib.LTS.DeterministicStateLabel.finite_image, Cslib.LTS.deterministic_imageFinite, Cslib.LTS.finiteState_imageFinite, Cslib.LTS.HasOutLabel, Cslib.LTS.outgoingLabels, Cslib.LTS.FinitelyBranching, Cslib.LTS.FinitelyBranching.of_finite, Cslib.LTS.BoundedUpTo, Cslib.LTS.Bounded, Cslib.LTS.Terminating, Cslib.LTS.Acyclic, Cslib.LTS.Deterministic.traces_of_mTr, Cslib.LTS.Deterministic.traces_of_tr
statement: formalized
proof: formalized
---

# Labelled Transition System (LTS)

`Cslib.Foundations.Semantics.LTS.Basic`, in [Cslib/Foundations/Semantics/LTS/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean), by Fabrizio Montesi.

> A Labelled Transition System (`LTS`) models the observable behaviour of the possible states of a
> system. They are particularly popular in the fields of concurrency theory, logic, and programming
> languages.
>
> ## Main definitions
>
> - `LTS` is a structure for labelled transition systems, consisting of a labelled transition
> relation `Tr` between states. We follow the style and conventions in [Sangiorgi2011].
>
> - `LTS.MTr` extends the transition relation of any LTS to a multistep transition relation,
> formalising the inference system and admissible rules for such relations in [Montesi2023].
>
> - `LTS.BoundedUpTo` records an explicit global execution-length bound. `LTS.Bounded`,
> `LTS.Terminating`, and `LTS.Acyclic` distinguish globally bounded execution length, absence of
> infinite executions, and absence of nonempty cycles.
>
> - Definitions for all the common classes of LTSs: image-finite, finitely branching, finite-state,
> and deterministic.
>
> ## Main statements
>
> - A series of results on `LTS.MTr` that allow for obtaining and composing multistep transitions in
> different ways.
>
> - `LTS.deterministic_imageFinite`: every deterministic LTS is also image-finite.
>
> - `LTS.finiteState_imageFinite`: every finite-state LTS is also image-finite.
>
> - `LTS.finiteState_finitelyBranching`: every finite-state LTS is also finitely-branching, if the
> type of labels is finite.
>
> ## References
>
> * [F. Montesi, *Introduction to Choreographies*][Montesi2023]
> * [D. Sangiorgi, *Introduction to Bisimulation and Coinduction*][Sangiorgi2011]

`Cslib.LTS` (structure, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L64))

> A Labelled Transition System (LTS) for a type of states (`State`) and a type of transition
> labels (`Label`) consists of a labelled transition relation (`Tr`).

```lean
structure LTS (State : Type u) (Label : Type v) where
  /-- The transition relation. -/
  Tr : State → Label → State → Prop
```

`Cslib.LTS.UnlabelledTr` (definition, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L71))

> The unlabelled transition relation underlying an LTS.

```lean
def UnlabelledTr (lts : LTS State Label) : State → State → Prop
```

`Cslib.LTS.IsTerminal` (definition, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L75))

> A state is terminal if it has no outgoing transitions.

```lean
def IsTerminal (lts : LTS State Label) (s : State) : Prop
```

> ## Multistep transitions and executions with finite traces
>
> This section treats executions with a finite number of steps.

`Cslib.LTS.MTr` (inductive type, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L95))

> Definition of a multistep transition.
>
> (Implementation note: compared to [Montesi2023], we choose stepL instead of stepR as fundamental
> rule. This makes working with lists of labels more convenient, because we follow the same
> construction. It is also similar to what is done in the `SimpleGraph` library in mathlib.)

```lean
inductive MTr (lts : LTS State Label) : State → List Label → State → Prop where
  | refl {s : State} : lts.MTr s [] s
  | stepL {s1 : State} {μ : Label} {s2 : State} {μs : List Label} {s3 : State} :
    lts.Tr s1 μ s2 → lts.MTr s2 μs s3 →
    lts.MTr s1 (μ :: μs) s3
```

`Cslib.LTS.MTr.nil_eq` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L103))

> In any zero-steps multistep transition, the origin and the derivative are the same.

```lean
theorem MTr.nil_eq (h : lts.MTr s1 [] s2) : s1 = s2
```

`Cslib.LTS.MTr.nil_iff` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L107))

```lean
theorem MTr.nil_iff (s1 s2 : State) : lts.MTr s1 [] s2 ↔ s1 = s2
```

`Cslib.LTS.MTr.single` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L112))

> Any transition is also a multistep transition.

```lean
theorem MTr.single {s1 : State} {μ : Label} {s2 : State} :
  lts.Tr s1 μ s2 → lts.MTr s1 [μ] s2
```

`Cslib.LTS.MTr.cons_iff` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L121))

> A multistep transition along `μ :: μs` is a transition labelled by `μ` plus a multistep
> transition labelled by `μs`.

```lean
theorem MTr.cons_iff {lts : LTS State Label} :
    lts.MTr s1 (μ :: μs) s2 ↔ ∃ s, lts.Tr s1 μ s ∧ lts.MTr s μs s2
```

`Cslib.LTS.MTr.stepR` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L130))

> Any multistep transition can be extended by adding a transition.

```lean
theorem MTr.stepR {s1 : State} {μs : List Label} {s2 : State} {μ : Label} {s3 : State} :
  lts.MTr s1 μs s2 → lts.Tr s2 μ s3 → lts.MTr s1 (μs ++ [μ]) s3
```

`Cslib.LTS.MTr.comp` (theorem, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L142))

> Multistep transitions can be composed.

```lean
theorem MTr.comp {s1 : State} {μs1 : List Label} {s2 : State} {μs2 : List Label} {s3 : State} :
  lts.MTr s1 μs1 s2 → lts.MTr s2 μs2 s3 →
  lts.MTr s1 (μs1 ++ μs2) s3
```

`Cslib.LTS.MTr.single_invert` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L155))

> Any 1-sized multistep transition implies a transition with the same states and label.

```lean
theorem MTr.single_invert (s1 : State) (μ : Label) (s2 : State) :
  lts.MTr s1 [μ] s2 → lts.Tr s1 μ s2
```

`Cslib.LTS.MTr.singleton_iff` (theorem, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L164))

> A 1-sized multistep transition is exactly a single transition with the given label.

```lean
theorem MTr.singleton_iff (s1 : State) (μ : Label) (s2 : State) :
lts.MTr s1 [μ] s2 ↔ lts.Tr s1 μ s2
```

`Cslib.LTS.MTr.split` (theorem, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L168))

> A multistep transition over a concatenation can be split into two multistep transitions.

```lean
theorem MTr.split {lts : LTS State Label} (h : lts.MTr s1 (μs ++ μs') s2) :
    ∃ s, lts.MTr s1 μs s ∧ lts.MTr s μs' s2
```

`Cslib.LTS.MTr.append_iff` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L181))

> Multistep-transitions over `μs ++ μs'` are exactly multistep transitions over `μs` and `μs'`
> with a common end & start state (respectively).

```lean
theorem MTr.append_iff : lts.MTr s1 (μs ++ μs') s2 ↔ ∃ s, lts.MTr s1 μs s ∧ lts.MTr s μs' s2
```

`Cslib.LTS.TrInv` (definition, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L188))

> Single-step invariant.

```lean
def TrInv (p : State → Prop) : Prop
```

`Cslib.LTS.MTrInv` (definition, [line 193](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L193))

> Multistep invariant.

```lean
def MTrInv (p : State → Prop) : Prop
```

`Cslib.LTS.mtrInv_of_trInv` (theorem, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L197))

> Any single-step invariant is also a multistep invariant.

```lean
theorem mtrInv_of_trInv {lts : LTS State Label} {p : State → Prop}
    (htr : lts.TrInv p) : lts.MTrInv p
```

`Cslib.LTS.CanReach` (definition, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L205))

> A state `s1` can reach a state `s2` if there exists a multistep transition from
> `s1` to `s2`.

```lean
def CanReach (s1 s2 : State) : Prop
```

`Cslib.LTS.CanReach.refl` (theorem, [line 210](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L210))

> Any state can reach itself.

```lean
theorem CanReach.refl (s : State) : lts.CanReach s s
```

`Cslib.LTS.generatedBy` (definition, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L216))

> The LTS generated by a state `s` is the LTS given by all the states reachable from `s`.

```lean
def generatedBy (s : State) : LTS {s' : State // lts.CanReach s s'} Label
```

`Cslib.LTS.traces` (definition, [line 227](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L227))

> The traces of a state `s` is the set of all lists of labels `μs` such that there is a multi-step
> transition labelled by `μs` originating from `s`.

```lean
def traces (s : State)
```

`Cslib.LTS.completeTraces` (definition, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L231))

> The complete traces of a state `s` is the set of all lists of labels `μs` such that there is a
> multi-step transition labelled by `μs` from `s` to a state with no outgoing transitions.

```lean
def completeTraces (s : State)
```

`Cslib.LTS.mem_traces_iff` (theorem, [line 234](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L234))

> Definition of `LTS.traces` for general label sequences, ...

```lean
theorem mem_traces_iff {lts : LTS State Label} (μs : List Label) :
  μs ∈ lts.traces s ↔ ∃ s', lts.MTr s μs s'
```

`Cslib.LTS.mem_traces_singleton_iff` (theorem, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L238))

> ... singleton sequences, ...

```lean
theorem mem_traces_singleton_iff {lts : LTS State Label} (μ : Label) :
    [μ] ∈ lts.traces s ↔ ∃ s', lts.Tr s μ s'
```

`Cslib.LTS.mem_traces_cons_iff` (theorem, [line 243](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L243))

> ... and sequences extended with a single transition.

```lean
theorem mem_traces_cons_iff {lts : LTS State Label} (μ : Label) (μs : List Label) :
    (μ :: μs) ∈ lts.traces s ↔ ∃ s', lts.Tr s μ s' ∧ μs ∈ lts.traces s'
```

`Cslib.LTS.traces_in` (theorem, [line 250](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L250))

> If there is a multi-step transition from `s` labelled by `μs`, then `μs` is in the traces of
> `s`.

```lean
theorem traces_in {lts : LTS State Label} (h : lts.MTr s μs s') : μs ∈ lts.traces s
```

> ### Classes of LTSs

`Cslib.LTS.image` (definition, [line 263](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L263))

> The `μ`-image of a state `s` is the set of all `μ`-derivatives of `s`.

```lean
def image (s : State) (μ : Label) : Set State
```

`Cslib.LTS.DeterministicStateLabel` (definition, [line 267](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L267))

> A state `s` is deterministic for a label `μ` if `s` has at most one `μ`-derivative.

```lean
def DeterministicStateLabel (s : State) (μ : Label) : Prop
```

`Cslib.LTS.deterministicStateLabel_iff_subsingleton_image` (theorem, [line 271](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L271))

> Determinism at a state and label means that its image is a subsingleton.

```lean
theorem deterministicStateLabel_iff_subsingleton_image {lts : LTS State Label} :
    lts.DeterministicStateLabel s μ ↔ (lts.image s μ).Subsingleton
```

`Cslib.LTS.DeterministicState` (definition, [line 280](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L280))

> A state `s` is deterministic if it is deterministic for all labels.

```lean
def DeterministicState (s : State) : Prop
```

`Cslib.LTS.deterministicState_iff_subsingleton_image` (theorem, [line 283](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L283))

> A state is deterministic exactly when each of its labelled images is a subsingleton.

```lean
theorem deterministicState_iff_subsingleton_image {lts : LTS State Label} :
    lts.DeterministicState s ↔ ∀ μ, (lts.image s μ).Subsingleton
```

`Cslib.LTS.Deterministic` (class, [line 292](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L292))

> An lts is deterministic if it is deterministic at every state.

```lean
class Deterministic (lts : LTS State Label) where
  /-- For all states and labels, there is at most one state reachable from a given state
  with a given label. -/
  deterministic : ∀ s, lts.DeterministicState s
```

`Cslib.LTS.deterministic_iff_subsingleton_image` (theorem, [line 298](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L298))

> An LTS is deterministic exactly when every labelled image is a subsingleton.

```lean
theorem deterministic_iff_subsingleton_image {lts : LTS State Label} :
    lts.Deterministic ↔ ∀ s μ, (lts.image s μ).Subsingleton
```

`Cslib.LTS.Deterministic.eq_of_tr` (theorem, [line 305](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L305))

```lean
theorem Deterministic.eq_of_tr {lts : LTS State Label} [h : lts.Deterministic]
    (htr : lts.Tr s1 μ s2) (htr' : lts.Tr s1 μ s2') : s2 = s2'
```

`Cslib.LTS.Deterministic.eq_of_mTr` (theorem, [line 311](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L311))

> In a deterministic lts, multistep transitions with a given start state and trace reach a unique
> end state.

```lean
theorem Deterministic.eq_of_mTr {lts : LTS State Label} [lts.Deterministic]
    (hmtr : lts.MTr s1 μs s2) (hmtr' : lts.MTr s1 μs s2') : s2 = s2'
```

`Cslib.LTS.imageMultistep` (definition, [line 323](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L323))

> The `μs`-image of a state `s`, where `μs` is a list of labels, is the set of all
> `μs`-derivatives of `s`.

```lean
def imageMultistep (s : State) (μs : List Label) : Set State
```

`Cslib.LTS.ImageFinite` (abbreviation, [line 327](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L327))

> An lts is image-finite if all images of its states are finite.

```lean
abbrev ImageFinite
```

`Cslib.LTS.DeterministicStateLabel.not_tr_of_ne` (theorem, [line 332](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L332))

> In a deterministic LTS, if a state has a `μ`-derivative, then it can have no other
> `μ`-derivative.

```lean
theorem DeterministicStateLabel.not_tr_of_ne (hdet : lts.DeterministicStateLabel s μ)
    (hne : s₁ ≠ s₂) (htr₁ : lts.Tr s μ s₁) : ¬lts.Tr s μ s₂
```

`Cslib.LTS.DeterministicStateLabel.image_singleton_iff_tr` (theorem, [line 337](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L337))

```lean
theorem DeterministicStateLabel.image_singleton_iff_tr (h : lts.DeterministicStateLabel s μ) :
    lts.image s μ = {s'} ↔ lts.Tr s μ s'
```

`Cslib.LTS.DeterministicStateLabel.image_char` (theorem, [line 345](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L345))

> If `s` is deterministic for `μ`, then the `μ`-image of `s` is either a singleton or the empty
> set.

```lean
theorem DeterministicStateLabel.image_char (h : lts.DeterministicStateLabel s μ) :
    (∃ s', lts.image s μ = { s' }) ∨ (lts.image s μ = ∅)
```

`Cslib.LTS.DeterministicStateLabel.finite_image` (theorem, [line 351](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L351))

> If `s` is deterministic at `μ`, then the `μ`-image of `s` is finite.

```lean
theorem DeterministicStateLabel.finite_image (h : lts.DeterministicStateLabel s μ) :
    Finite (lts.image s μ)
```

`Cslib.LTS.deterministic_imageFinite` (instance, [line 359](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L359))

> Every deterministic LTS is also image-finite.

```lean
instance deterministic_imageFinite [lts.Deterministic] : lts.ImageFinite
```

`Cslib.LTS.finiteState_imageFinite` (instance, [line 363](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L363))

> Every finite-state LTS is also image-finite.

```lean
instance finiteState_imageFinite [Finite State] : lts.ImageFinite
```

`Cslib.LTS.HasOutLabel` (definition, [line 366](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L366))

> A state has an outgoing label `μ` if it has a `μ`-derivative.

```lean
def HasOutLabel (s : State) (μ : Label) : Prop
```

`Cslib.LTS.outgoingLabels` (definition, [line 370](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L370))

> The set of outgoing labels of a state.

```lean
def outgoingLabels (s : State)
```

`Cslib.LTS.FinitelyBranching` (class, [line 374](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L374))

> An LTS is finitely branching if it is image-finite and all states have finite sets of
> outgoing labels.

```lean
class FinitelyBranching where
  [image_finite : lts.ImageFinite]
  [finite_state : ∀ s, Finite (lts.outgoingLabels s)]
```

`Cslib.LTS.FinitelyBranching.of_finite` (instance, [line 381](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L381))

> Every LTS with finite types for states and labels is also finitely branching.

```lean
instance FinitelyBranching.of_finite [Finite State] [Finite Label] : lts.FinitelyBranching
```

`Cslib.LTS.BoundedUpTo` (definition, [line 384](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L384))

> An LTS is bounded up to `n` if every finite execution has length strictly less than `n`.

```lean
def BoundedUpTo (lts : LTS State Label) (n : ℕ) : Prop
```

`Cslib.LTS.Bounded` (class, [line 388](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L388))

> An LTS is bounded if there is a global bound on the length of all of its finite executions.

```lean
class Bounded (lts : LTS State Label) where
  bounded : ∃ n, lts.BoundedUpTo n
```

`Cslib.LTS.Terminating` (class, [line 393](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L393))

> An LTS is terminating if its underlying unlabelled transition relation is terminating,
> equivalently if it admits no infinite execution.

```lean
class Terminating (lts : LTS State Label) where
  terminating : Relation.Terminating lts.UnlabelledTr
```

`Cslib.LTS.Acyclic` (class, [line 398](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L398))

> An LTS is acyclic if its underlying unlabelled transition relation contains no nonempty
> cycle.

```lean
class Acyclic (lts : LTS State Label) where
  [acyclic : Relation.Acyclic lts.UnlabelledTr]
```

`Cslib.LTS.Deterministic.traces_of_mTr` (theorem, [line 405](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L405))

> In a deterministic lts, a state's traces are determined by any of its multi-step predecessors.

```lean
theorem Deterministic.traces_of_mTr {lts : LTS State Label} [lts.Deterministic]
    (h : lts.MTr s μs s') : lts.traces s' = {μs' | μs ++ μs' ∈ lts.traces s}
```

`Cslib.LTS.Deterministic.traces_of_tr` (theorem, [line 417](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean#L417))

> In a deterministic lts, a state's traces are determined by any of its predecessors.

```lean
theorem Deterministic.traces_of_tr {lts : LTS State Label} [lts.Deterministic]
    (h : lts.Tr s μ s') : lts.traces s' = {μs | μ :: μs ∈ lts.traces s}
```

## Depends on

- [Relations: Definitions](../../relation/defs.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Basic.lean)
