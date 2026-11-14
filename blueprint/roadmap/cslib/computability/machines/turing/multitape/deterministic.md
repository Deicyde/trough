---
catalog: module
lean: Turing.MultiTapeNTM.IsDeterministic, Turing.MultiTapeTM, Turing.MultiTapeTM.tr, Turing.MultiTapeTM.tr_iff, Turing.MultiTapeTM.ofTr, Turing.MultiTapeTM.q₀_ofTr, Turing.MultiTapeTM.tr_ofTr, Turing.MultiTapeTM.adaptedTr, Turing.MultiTapeTM.adapt, Turing.MultiTapeTM.follows_adapt, Turing.MultiTapeTM.combine, Turing.MultiTapeTM.handOver, Turing.MultiTapeTM.handOver_some, Turing.MultiTapeTM.handOver_none, Turing.MultiTapeTM.follows_combine_left, Turing.MultiTapeTM.follows_combine_right, Turing.MultiTapeTM.combineLeftHom, Turing.MultiTapeTM.combineRightHom, Turing.MultiTapeTM.step, Turing.MultiTapeTM.step_iff, Turing.MultiTapeTM.step_of_state, Turing.MultiTapeTM.step_inputPos_of_state, Turing.MultiTapeTM.step_workTapes_of_state, Turing.MultiTapeTM.step_workTapePos_of_state, Turing.MultiTapeTM.step_of_halt, Turing.MultiTapeNTM.RunPath.ofDeterministic, Turing.MultiTapeNTM.RunPath.eq_ofDeterministic, Turing.MultiTapeNTM.ComputationPath.ofDeterministic, Turing.MultiTapeNTM.ComputationPath.eq_ofDeterministic, Turing.MultiTapeNTM.RunPath.eq_take, Turing.MultiTapeNTM.ComputationPath.spaceUsedByTape_le_of_space_le, Turing.MultiTapeNTM.RunPath.map_ofDeterministic, Turing.MultiTapeTM.runFrom, Turing.MultiTapeTM.runPath_apply_eq_runFrom, Turing.MultiTapeTM.computationPath_last_eq_runFrom, Turing.MultiTapeTM.runFrom_map, Turing.MultiTapeTM.runFrom_eq_of_halt, Turing.MultiTapeTM.runsInTime_of_halted, Turing.MultiTapeTM.inputPos_runFrom_le, Turing.MultiTapeTM.Computes, Turing.MultiTapeTM.ComputesInTimeAndSpace, Turing.MultiTapeTM.ComputesFunInTimeAndSpace, Turing.MultiTapeTM.ComputesFunInTimeAndSpace.mono, Turing.MultiTapeTM.ComputableInTimeAndSpace, Turing.MultiTapeTM.ComputableInTimeAndSpaceOfLength, Turing.MultiTapeTM.ComputableInTimeAndSpace.mono, Turing.MultiTapeTM.indicator, Turing.MultiTapeTM.DecidableInTimeAndSpace, Turing.MultiTapeTM.not_halts_of_repeat_nonhalt
statement: formalized
proof: formalized
---

# Deterministic Multi-Tape Turing Machines

`Cslib.Computability.Machines.Turing.MultiTape.Deterministic`, in [Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean), by Christian Reitwiessner, Samuel Schlesinger, Aviv Bar Natan.

> A deterministic Turing machine is a nondeterministic machine whose transition relation has exactly
> one action for every combination of state and symbols read. From the transition relation it derives
> a transition function `tr` and a function `step` which maps each configuration to its unique
> successor configuration (a halted configuration maps to itself).
>
> The design choices for configurations and actions are documented in
> `Cslib.Computability.Machines.Turing.MultiTape.Configuration`.
>
> ## Important Declarations
>
> We define a number of structures and concepts related to multi-tape Turing machine computation:
>
> * `MultiTapeNTM.IsDeterministic`: the transition relation relates every state and tuple of read
>     symbols to exactly one action
> * `MultiTapeTM`: the TM itself
> * `tr`, `ofTr`: the derived transition function and construction from a function
> * `adapt`: the machine run through an adapter
> * `combine`: two machines on the same tapes combined into one
> * `step`, `runFrom`: the successor configuration and iteration of this function
> * `MultiTapeNTM.RunPath.ofDeterministic`, `MultiTapeNTM.ComputationPath.ofDeterministic`:
>     paths of a given length from an arbitrary or initial configuration
> * `Computes`: the machine halts with the given output on an input
> * `ComputesInTimeAndSpace`: the machine produces an output within the shared resource bounds
> * `ComputesFunInTimeAndSpace`: function computation with the shared time and space bounds
> * `ComputableInTimeAndSpace`: such a machine exists with binary alphabet and finitely many states.
> * `ComputableInTimeAndSpaceOfLength`: the specialization to bounds on encoded input length.
> * `DecidableInTimeAndSpace`: a proof that a TM decides a language within a certain time
>     and space bound.

`Turing.MultiTapeNTM.IsDeterministic` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L57))

> Every state and tuple of read symbols is related to exactly one action by `ntm`'s transition
> relation.

```lean
def MultiTapeNTM.IsDeterministic (ntm : MultiTapeNTM k Symbol State) : Prop
```

`Turing.MultiTapeTM` (structure, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L67))

> A multi-tape Turing machine with `k` work tapes over the alphabet of `Option Symbol` (where `none`
> is the blank tape symbol). Note that it is not required that `Symbol` or `State` are finite
> to keep the definition more general. The restriction will be introduced once we start talking about
> computability by Turing machines in general.

```lean
structure MultiTapeTM (k : ℕ) (Symbol State : Type*)
    extends MultiTapeNTM k Symbol State where
  /-- Every state and tuple of read symbols is related to exactly one action by the transition
  relation. -/
  deterministic : toMultiTapeNTM.IsDeterministic
```

`Turing.MultiTapeTM.tr` (definition, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L81))

> The unique action related to the given state and read symbols by `Tr`.

```lean
noncomputable def tr (tm : MultiTapeTM k Symbol State) (q : State) (input : Option Symbol)
    (work : Fin k → Option Symbol) : Action k Symbol State
```

`Turing.MultiTapeTM.tr_iff` (lemma, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L87))

> `Tr` relates a state and read symbols to an action exactly when `tr` returns that action.

```lean
lemma tr_iff {q : State} {input : Option Symbol} {work : Fin k → Option Symbol}
    {action : Action k Symbol State} : tm.Tr q input work action ↔ tm.tr q input work = action
```

`Turing.MultiTapeTM.ofTr` (definition, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L93))

> Construct a deterministic machine from an initial state and transition function.

```lean
def ofTr (q₀ : State)
    (tr : State → Option Symbol → (Fin k → Option Symbol) → Action k Symbol State) :
    MultiTapeTM k Symbol State
```

`Turing.MultiTapeTM.q₀_ofTr` (lemma, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L102))

> The initial state of `ofTr` is the supplied one.

```lean
lemma q₀_ofTr (q₀ : State)
    (tr : State → Option Symbol → (Fin k → Option Symbol) → Action k Symbol State) :
    (ofTr q₀ tr).q₀ = q₀
```

`Turing.MultiTapeTM.tr_ofTr` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L109))

> Extracting the transition of `ofTr` recovers the supplied function.

```lean
lemma tr_ofTr (q₀ : State)
    (tr : State → Option Symbol → (Fin k → Option Symbol) → Action k Symbol State)
    (q : State) (input : Option Symbol) (work : Fin k → Option Symbol) :
    (ofTr q₀ tr).tr q input work = tr q input work
```

`Turing.MultiTapeTM.adaptedTr` (definition, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L117))

> The transitions of `tm` performed through `adapter`: it reads what `tm` reads through `adapter`
> and performs the adaptation of the action of `tm`.

```lean
noncomputable def adaptedTr {k' : ℕ} {State' : Type*} (tm : MultiTapeTM k Symbol State)
    (adapter : MultiTapeNTM.Adapter k k' Symbol State State') (q : State) (inp : Option Symbol)
    (work : Fin k' → Option Symbol) : Action k' Symbol State'
```

`Turing.MultiTapeTM.adapt` (definition, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L127))

> `tm` run through `adapter`, a `MultiTapeNTM.Adapter`: the adapter computes what `tm` reads
> from the symbols under the heads of the new machine, and gives the action of the new machine
> performing each action of `tm`. In state `q`, `tm.adapt adapter` performs the adaptation of the
> action of `tm` in `q` on what the adapter reads.

```lean
noncomputable def adapt {k' : ℕ} (tm : MultiTapeTM k Symbol State)
    (adapter : MultiTapeNTM.Adapter k k' Symbol State State) : MultiTapeTM k' Symbol State
```

`Turing.MultiTapeTM.follows_adapt` (lemma, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L132))

> `tm.adapt adapter` follows `tm`.

```lean
lemma follows_adapt {k' : ℕ} {adapter : MultiTapeNTM.Adapter k k' Symbol State State} :
    (tm.adapt adapter).Follows tm id adapter
```

`Turing.MultiTapeTM.combine` (definition, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L140))

> `tm₀` and `tm₁` combined into one machine on their shared tapes, which starts in `q₀`: in a
> state `inl q` it performs the transition of `tm₀` in `q`, and in `inr q` that of `tm₁`. The maps
> `next₀` and `next₁` say where the steps of each machine lead: within the same machine, to the other
> machine, or to halting.

```lean
noncomputable def combine {State₀ State₁ : Type*} (tm₀ : MultiTapeTM k Symbol State₀)
    (tm₁ : MultiTapeTM k Symbol State₁) (next₀ : Option State₀ → Option (State₀ ⊕ State₁))
    (next₁ : Option State₁ → Option (State₀ ⊕ State₁)) (q₀ : State₀ ⊕ State₁) :
    MultiTapeTM k Symbol (State₀ ⊕ State₁)
```

`Turing.MultiTapeTM.handOver` (definition, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L148))

> Where the steps of a first machine lead when it runs in its own states: halting hands over to
> the second machine in its state `q₁`.

```lean
def handOver {State₀ State₁ : Type*} (q₁ : State₁) (state : Option State₀) :
    Option (State₀ ⊕ State₁)
```

`Turing.MultiTapeTM.handOver_some` (lemma, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L152))

```lean
lemma handOver_some {State₀ State₁ : Type*} (q₁ : State₁) (q : State₀) :
    handOver q₁ (some q) = some (.inl q)
```

`Turing.MultiTapeTM.handOver_none` (lemma, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L155))

```lean
lemma handOver_none {State₀ State₁ : Type*} (q₁ : State₁) :
    handOver (State₀ := State₀) q₁ none = some (.inr q₁)
```

`Turing.MultiTapeTM.follows_combine_left` (lemma, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L165))

> In its states `inl q`, the combined machine follows `tm₀`, its steps leading along `next₀`.

```lean
lemma follows_combine_left : (combine tm₀ tm₁ next₀ next₁ q₀).Follows tm₀ .inl (.mapState next₀)
```

`Turing.MultiTapeTM.follows_combine_right` (lemma, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L169))

> In its states `inr q`, the combined machine follows `tm₁`, its steps leading along `next₁`.

```lean
lemma follows_combine_right : (combine tm₀ tm₁ next₀ next₁ q₀).Follows tm₁ .inr (.mapState next₁)
```

`Turing.MultiTapeTM.combineLeftHom` (definition, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L175))

> If `next₀` keeps the live states of `tm₀` in `tm₀`, the combined machine mirrors the running
> steps of `tm₀`, its states relabeled along `next₀`.

```lean
noncomputable def combineLeftHom {input : List Symbol} (h : ∀ q, next₀ (some q) = some (.inl q)) :
    (tm₀.runningStepRel input).Hom ((combine tm₀ tm₁ next₀ next₁ q₀).stepRel input)
```

`Turing.MultiTapeTM.combineRightHom` (definition, [line 182](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L182))

> If the steps of `tm₁` stay in `tm₁`, the combined machine mirrors them.

```lean
noncomputable def combineRightHom {input : List Symbol} :
    (tm₁.stepRel input).Hom ((combine tm₀ tm₁ next₀ (Option.map .inr) q₀).stepRel input)
```

> ## Stepping a Turing Machine
>
> The step function lets the machine transition from one configuration to the next, and `runFrom`
> gives the configuration reached after a number of steps. Configurations themselves are defined in
> `Cslib.Computability.Machines.Turing.MultiTape.Configuration`.

`Turing.MultiTapeTM.step` (definition, [line 203](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L203))

> The unique successor configuration related to `cfg` by the inherited step relation.

```lean
noncomputable def step (cfg : Cfg k Symbol State input) : Cfg k Symbol State input
```

`Turing.MultiTapeTM.step_iff` (lemma, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L208))

> `Step` relates `c` to `c'` exactly when `step c = c'`.

```lean
lemma step_iff {c c' : Cfg k Symbol State input} : tm.Step c c' ↔ tm.step c = c'
```

`Turing.MultiTapeTM.step_of_state` (lemma, [line 213](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L213))

> A running configuration takes the action selected by the transition function.

```lean
lemma step_of_state {cfg : Cfg k Symbol State input} {q : State} (h : cfg.state = some q) :
    tm.step cfg = (tm.tr q cfg.inputSymbol cfg.workTapeSymbols).apply cfg
```

`Turing.MultiTapeTM.step_inputPos_of_state` (lemma, [line 219](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L219))

> The input head after a live step.

```lean
public lemma step_inputPos_of_state {cfg : Cfg k Symbol State input} {q : State}
    (h : cfg.state = some q) :
    (tm.step cfg).inputPos =
      moveInputPos cfg.inputPos (tm.tr q cfg.inputSymbol cfg.workTapeSymbols).inputTape
```

`Turing.MultiTapeTM.step_workTapes_of_state` (lemma, [line 226](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L226))

> A work tape after a live step.

```lean
public lemma step_workTapes_of_state {cfg : Cfg k Symbol State input} {q : State}
    (h : cfg.state = some q) (i : Fin k) :
    (tm.step cfg).workTapes i =
      match (tm.tr q cfg.inputSymbol cfg.workTapeSymbols).workTapes i |>.1 with
      | none => cfg.workTapes i
      | some s => Function.update (cfg.workTapes i) (cfg.workTapePos i) s
```

`Turing.MultiTapeTM.step_workTapePos_of_state` (lemma, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L236))

> A work tape head after a live step.

```lean
public lemma step_workTapePos_of_state {cfg : Cfg k Symbol State input} {q : State}
    (h : cfg.state = some q) (i : Fin k) :
    (tm.step cfg).workTapePos i =
      cfg.workTapePos i + ((tm.tr q cfg.inputSymbol cfg.workTapeSymbols).workTapes i).2
```

`Turing.MultiTapeTM.step_of_halt` (lemma, [line 244](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L244))

```lean
lemma step_of_halt {cfg : Cfg k Symbol State input} (h : cfg.state = none) :
    tm.step cfg = cfg
```

`Turing.MultiTapeNTM.RunPath.ofDeterministic` (definition, [line 255](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L255))

> The path of the first `t` steps from `cfg`.

```lean
noncomputable def RunPath.ofDeterministic (tm : MultiTapeTM k Symbol State)
    (cfg : Cfg k Symbol State input) (t : ℕ) : tm.RunPath input
```

`Turing.MultiTapeNTM.RunPath.eq_ofDeterministic` (lemma, [line 262](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L262))

> Every deterministic run path is the canonical path from its head for its duration.

```lean
lemma RunPath.eq_ofDeterministic (p : tm.RunPath input) :
    p = .ofDeterministic tm p.head p.time
```

`Turing.MultiTapeNTM.ComputationPath.ofDeterministic` (definition, [line 271](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L271))

> The path of the first `t` steps on `input`, starting at the initial configuration.

```lean
noncomputable def ComputationPath.ofDeterministic (tm : MultiTapeTM k Symbol State)
    (input : List Symbol) (t : ℕ) : tm.ComputationPath input
```

`Turing.MultiTapeNTM.ComputationPath.eq_ofDeterministic` (lemma, [line 276](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L276))

> Every deterministic computation path is the canonical path for its duration.

```lean
lemma ComputationPath.eq_ofDeterministic (p : tm.ComputationPath input) :
    p = .ofDeterministic tm input p.time
```

`Turing.MultiTapeNTM.RunPath.eq_take` (lemma, [line 284](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L284))

> Deterministic run paths from the same configuration are prefixes of one another: the shorter one
> is the longer one, cut at its length.

```lean
lemma RunPath.eq_take {p q : tm.RunPath input} (hhead : p.head = q.head) (h : p.length ≤ q.length) :
    p = q.take ⟨p.length, Nat.lt_succ_of_le h⟩
```

`Turing.MultiTapeNTM.ComputationPath.spaceUsedByTape_le_of_space_le` (lemma, [line 292](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L292))

> The computation paths of a deterministic machine are prefixes of one another, so a path visiting
> at most as many cells as another visits at most as many on each tape.

```lean
lemma ComputationPath.spaceUsedByTape_le_of_space_le (p : tm.ComputationPath input)
    {q : tm.ComputationPath input} (h : p.space ≤ q.space) :
    p.spaceUsedByTape ≤ q.spaceUsedByTape
```

`Turing.MultiTapeNTM.RunPath.map_ofDeterministic` (lemma, [line 310](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L310))

> A step-preserving map sends the path of `t` steps from `cfg` to the path of `t` steps from the
> image of `cfg`.

```lean
lemma RunPath.map_ofDeterministic {k' : ℕ} {State' : Type*} {input' : List Symbol}
    {tm' : MultiTapeTM k' Symbol State'} (f : (tm.stepRel input).Hom (tm'.stepRel input'))
    (cfg : Cfg k Symbol State input) (t : ℕ) :
    (RunPath.ofDeterministic tm cfg t).map f = .ofDeterministic tm' (f cfg) t
```

`Turing.MultiTapeTM.runFrom` (definition, [line 324](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L324))

> The configuration reached by running the Turing machine for `t` steps from `cfg`.
> If the Turing machine halts, it will stay at the halting configuration.

```lean
noncomputable def runFrom (cfg : Cfg k Symbol State input) (t : ℕ) : Cfg k Symbol State input
```

`Turing.MultiTapeTM.runPath_apply_eq_runFrom` (lemma, [line 328](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L328))

> Every path of a deterministic machine follows its iterated step function.

```lean
lemma runPath_apply_eq_runFrom (p : tm.RunPath input) (i : Fin (p.length + 1)) :
    p i = tm.runFrom p.head i
```

`Turing.MultiTapeTM.computationPath_last_eq_runFrom` (lemma, [line 335](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L335))

> A deterministic computation ends at the corresponding iterate.

```lean
lemma computationPath_last_eq_runFrom (p : tm.ComputationPath input) :
    p.last = tm.runFrom (tm.initCfg input) p.time
```

`Turing.MultiTapeTM.runFrom_map` (lemma, [line 342](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L342))

> Running from the image of a configuration under a step-preserving map reaches the image of the
> original run.

```lean
lemma runFrom_map {k' : ℕ} {State' : Type*} {input' : List Symbol}
    {tm' : MultiTapeTM k' Symbol State'} (f : (tm.stepRel input).Hom (tm'.stepRel input'))
    (cfg : Cfg k Symbol State input) (t : ℕ) :
    tm'.runFrom (f cfg) t = f (tm.runFrom cfg t)
```

`Turing.MultiTapeTM.runFrom_eq_of_halt` (lemma, [line 349](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L349))

> Nothing changes after the machine has halted.

```lean
lemma runFrom_eq_of_halt
    (tm : MultiTapeTM k Symbol State)
    (cfg : Cfg k Symbol State input) {τ t : ℕ} (hle : τ ≤ t)
    (hhalt : (tm.runFrom cfg τ).state = none) :
    tm.runFrom cfg t = tm.runFrom cfg τ
```

`Turing.MultiTapeTM.runsInTime_of_halted` (lemma, [line 358](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L358))

> A deterministic machine halted after `t` steps satisfies the shared time bound.

```lean
lemma runsInTime_of_halted {input : List Symbol} {t : ℕ}
    (h : (tm.runFrom (tm.initCfg input) t).Halted) : tm.RunsInTime input t
```

`Turing.MultiTapeTM.inputPos_runFrom_le` (lemma, [line 365](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L365))

> In `t` steps the input head moves at most `t` positions to the right.

```lean
lemma inputPos_runFrom_le (tm : MultiTapeTM k Symbol State)
    (cfg : Cfg k Symbol State input) (t : ℕ) :
    ((tm.runFrom cfg t).inputPos : ℕ) ≤ (cfg.inputPos : ℕ) + t
```

`Turing.MultiTapeTM.Computes` (definition, [line 383](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L383))

> The machine eventually halts on `input` with the given `output`.

```lean
def Computes (tm : MultiTapeTM k Symbol State) (input output : List Symbol) : Prop
```

`Turing.MultiTapeTM.ComputesInTimeAndSpace` (definition, [line 388](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L388))

> The machine computes `output` from `input` within the shared time and space bounds.

```lean
def ComputesInTimeAndSpace (tm : MultiTapeTM k Symbol State)
    (input output : List Symbol) (t s : ℕ) : Prop
```

`Turing.MultiTapeTM.ComputesFunInTimeAndSpace` (definition, [line 393](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L393))

> The machine computes `f` relative to given encodings within the given time and space bounds.

```lean
def ComputesFunInTimeAndSpace {α β : Type*} (tm : MultiTapeTM k Symbol State)
    (encIn : α ↪ List Symbol) (encOut : β ↪ List Symbol) (f : α → β) (t s : α → ℕ) : Prop
```

`Turing.MultiTapeTM.ComputesFunInTimeAndSpace.mono` (theorem, [line 398](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L398))

> Resource bounds can be weakened independently on every input.

```lean
theorem ComputesFunInTimeAndSpace.mono {α β : Type*}
    {encIn : α ↪ List Symbol} {encOut : β ↪ List Symbol} {f : α → β} {t s t' s' : α → ℕ}
    (h : tm.ComputesFunInTimeAndSpace encIn encOut f t s)
    (ht : ∀ a, t a ≤ t' a) (hs : ∀ a, s a ≤ s' a) :
    tm.ComputesFunInTimeAndSpace encIn encOut f t' s'
```

`Turing.MultiTapeTM.ComputableInTimeAndSpace` (definition, [line 407](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L407))

> Computability by a deterministic machine with a binary tape alphabet and finitely many states,
> within the supplied input-indexed bounds.

```lean
def ComputableInTimeAndSpace {α β : Type*}
    (f : α → β) (encIn : α ↪ List Bool) (encOut : β ↪ List Bool)
    (t s : α → ℕ) : Prop
```

`Turing.MultiTapeTM.ComputableInTimeAndSpaceOfLength` (abbreviation, [line 416](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L416))

> There exists a binary Turing machine with finitely many states that, for every input `a`,
> computes `encOut (f a)` from `encIn a` in at most `t (encIn a).length` steps,
> using at most `s (encIn a).length` work-tape cells.

```lean
abbrev ComputableInTimeAndSpaceOfLength {α β : Type*}
    (f : α → β) (encIn : α ↪ List Bool) (encOut : β ↪ List Bool)
    (t s : ℕ → ℕ) : Prop
```

`Turing.MultiTapeTM.ComputableInTimeAndSpace.mono` (theorem, [line 423](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L423))

> Computability is monotone in the resource bounds.

```lean
theorem ComputableInTimeAndSpace.mono {α β : Type*}
    {f : α → β} {encIn : α ↪ List Bool} {encOut : β ↪ List Bool} {t s t' s' : α → ℕ}
    (h : ComputableInTimeAndSpace f encIn encOut t s)
    (ht : ∀ a, t a ≤ t' a) (hs : ∀ a, s a ≤ s' a) :
    ComputableInTimeAndSpace f encIn encOut t' s'
```

`Turing.MultiTapeTM.indicator` (definition, [line 433](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L433))

> The Boolean indicator function of a set.

```lean
noncomputable def indicator {α : Type*} (L : Set α) : α → Bool
```

`Turing.MultiTapeTM.DecidableInTimeAndSpace` (definition, [line 438](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L438))

> A set is decidable within the given input-indexed bounds when its Boolean indicator is
> computable in those bounds.

```lean
def DecidableInTimeAndSpace {α : Type*} (L : Set α) (enc : α ↪ List Bool)
    (t s : α → ℕ) : Prop
```

`Turing.MultiTapeTM.not_halts_of_repeat_nonhalt` (lemma, [line 446](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean#L446))

> If a deterministic machine repeats a non-halting configuration, it never halts,
> because the sequence between the two configurations will loop forever.
> Note that this can be applied to two arbitrary and different time steps `t` and `t + Δ`
> using `Function.iterate_add_apply`.

```lean
lemma not_halts_of_repeat_nonhalt
    (cfg : Cfg k Symbol State input)
    (h_not_halt : cfg.state ≠ none)
    (t : ℕ)
    (heq : tm.runFrom cfg (t + 1) = cfg) :
    ∀ t', (tm.runFrom cfg t').state ≠ none
```

## Depends on

- [Space usage of multi-tape Turing machines](space.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Deterministic.lean)
