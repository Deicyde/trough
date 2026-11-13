---
catalog: module
lean: Cslib.Turing.SingleTapeTM.Stmt, Cslib.Turing.SingleTapeTM, Cslib.Turing.SingleTapeTM.inhabitedStmt, Cslib.Turing.SingleTapeTM.Cfg, Cslib.Turing.SingleTapeTM.step, Cslib.Turing.SingleTapeTM.initCfg, Cslib.Turing.SingleTapeTM.haltCfg, Cslib.Turing.SingleTapeTM.Cfg.spaceUsed, Cslib.Turing.SingleTapeTM.Cfg.spaceUsed_initCfg, Cslib.Turing.SingleTapeTM.Cfg.spaceUsed_haltCfg, Cslib.Turing.SingleTapeTM.Cfg.spaceUsed_step, Cslib.Turing.SingleTapeTM.TransitionRelation, Cslib.Turing.SingleTapeTM.Outputs, Cslib.Turing.SingleTapeTM.OutputsWithinTime, Cslib.Turing.SingleTapeTM.output_length_le_input_length_add_time, Cslib.Turing.SingleTapeTM.idComputer, Cslib.Turing.SingleTapeTM.compComputer, Cslib.Turing.SingleTapeTM.compComputer_q₀_eq, Cslib.Turing.SingleTapeTM.TimeComputable, Cslib.Turing.SingleTapeTM.TimeComputable.id, Cslib.Turing.SingleTapeTM.TimeComputable.comp, Cslib.Turing.SingleTapeTM.TimeComputable.withMonotoneBound, Cslib.Turing.SingleTapeTM.TimeComputable.withMonotoneBound_timeBound_monotone, Cslib.Turing.SingleTapeTM.PolyTimeComputable, Cslib.Turing.SingleTapeTM.PolyTimeComputable.id, Cslib.Turing.SingleTapeTM.PolyTimeComputable.withMonotoneBound, Cslib.Turing.SingleTapeTM.PolyTimeComputable.comp
statement: formalized
proof: formalized
---

# Single-Tape Turing Machines

`Cslib.Computability.Machines.Turing.SingleTape.Deterministic`, in [Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean), by Bolton Bailey, Pim Spelier, Daan van Gent.

> Defines a single-tape Turing machine for computing functions on `List Symbol`
> for finite alphabet `Symbol`.
>
> ## Design
>
> Here are some design choices made in this file:
>
> These machines have access to a single bidirectionally-infinite tape (`BiTape`)
> which uses symbols from `Option Symbol`.
>
> The transition function of the machine takes a state
> and a tape alphabet character under the read-head (i.e. an `Option Symbol`)
> and returns a `Stmt` describing the tape action to take,
> as well as an optional new state to transition to (where `none` means halt).
>
> We do not make the "halting state" a member of the state type for a few reasons:
>
> * To avoid the need for passing a subtype of "non-halting states" to the transition function.
> * To make clear that TMs are not expected to continue on after entering this special state
>   (in contrast to, say, a DFA entering/leaving an accepting state).
> * To make it simpler to match on halting when modifying a machine.
>
> We also include the possibility for non-movement actions,
> for convenience in composition of machines.
>
> ## Important Declarations
>
> We define a number of structures related to Turing machine computation:
>
> * `Stmt`: the write and movement operations a TM can do in a single step.
> * `SingleTapeTM`: the TM itself.
> * `Cfg`: the configuration of a TM, including internal and tape state.
> * `TimeComputable f`: a TM for computing `f`, packaged with a bound on runtime.
> * `PolyTimeComputable f`: `TimeComputable f` packaged with a polynomial bound on runtime.
>
> We also provide ways of constructing polynomial-runtime TMs
>
> * `PolyTimeComputable.id`: computes the identity function
> * `PolyTimeComputable.comp`: computes the composition of polynomial time machines
> * `TimeComputable.withMonotoneBound`, `PolyTimeComputable.withMonotoneBound`: replace the time
>   bound with a monotone one (its `partialSups`) without changing the machine
>
> …

`Cslib.Turing.SingleTapeTM.Stmt` (structure, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L83))

> A Turing machine "statement" is just a `Option`al command to move left or right,
> and write a symbol (i.e. an `Option Symbol`, where `none` is the blank symbol) on the `BiTape`

```lean
structure Stmt (Symbol : Type) where
  /-- The symbol to write at the current head position -/
  symbol : Option Symbol
  /-- The direction to move the tape head -/
  movement : Option Dir
deriving Inhabited
```

`Cslib.Turing.SingleTapeTM` (structure, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L96))

> A single-tape Turing machine
> over the alphabet of `Option Symbol` (where `none` is the blank `BiTape` symbol).

```lean
structure SingleTapeTM Symbol [Inhabited Symbol] [Fintype Symbol] where
  /-- type of state labels -/
  (State : Type)
  /-- finiteness of the state type -/
  [stateFintype : Fintype State]
  /-- Initial state -/
  (q₀ : State)
  /-- Transition function, mapping a state and a head symbol to a `Stmt` to invoke,
  and optionally the new state to transition to afterwards (`none` for halt) -/
  (tr : State → Option Symbol → SingleTapeTM.Stmt Symbol × Option State)
```

> ## Configurations of a Turing Machine
>
> This section defines the configurations of a Turing machine,
> the step function that lets the machine transition from one configuration to the next,
> and the intended initial and final configurations.

`Cslib.Turing.SingleTapeTM.inhabitedStmt` (instance, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L125))

```lean
instance inhabitedStmt : Inhabited (Stmt Symbol)
```

`Cslib.Turing.SingleTapeTM.Cfg` (structure, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L132))

> The configurations of a Turing machine consist of:
> an `Option`al state (or none for the halting state),
> and a `BiTape` representing the tape contents.

```lean
structure Cfg : Type where
  /-- the state of the TM (or none for the halting state) -/
  state : Option tm.State
  /-- the BiTape contents -/
  BiTape : BiTape Symbol
deriving Inhabited
```

`Cslib.Turing.SingleTapeTM.step` (definition, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L141))

> The step function corresponding to a `SingleTapeTM`.

```lean
def step : tm.Cfg → Option tm.Cfg
```

`Cslib.Turing.SingleTapeTM.initCfg` (definition, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L157))

> The initial configuration corresponding to a list in the input alphabet.
> Note that the entries of the tape constructed by `BiTape.mk₁` are all `some` values.
> This is to ensure that distinct lists map to distinct initial configurations.

```lean
def initCfg (tm : SingleTapeTM Symbol) (s : List Symbol) : tm.Cfg
```

`Cslib.Turing.SingleTapeTM.haltCfg` (definition, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L162))

> The final configuration corresponding to a list in the output alphabet.
> (We demand that the head halts at the leftmost position of the output.)

```lean
def haltCfg (tm : SingleTapeTM Symbol) (s : List Symbol) : tm.Cfg
```

`Cslib.Turing.SingleTapeTM.Cfg.spaceUsed` (definition, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L167))

> The space used by a configuration is the space used by its tape.

```lean
def Cfg.spaceUsed (tm : SingleTapeTM Symbol) (cfg : tm.Cfg) : ℕ
```

`Cslib.Turing.SingleTapeTM.Cfg.spaceUsed_initCfg` (lemma, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L170))

```lean
lemma Cfg.spaceUsed_initCfg (tm : SingleTapeTM Symbol) (s : List Symbol) :
    (tm.initCfg s).spaceUsed = max 1 s.length
```

`Cslib.Turing.SingleTapeTM.Cfg.spaceUsed_haltCfg` (lemma, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L174))

```lean
lemma Cfg.spaceUsed_haltCfg (tm : SingleTapeTM Symbol) (s : List Symbol) :
    (tm.haltCfg s).spaceUsed = max 1 s.length
```

`Cslib.Turing.SingleTapeTM.Cfg.spaceUsed_step` (lemma, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L177))

```lean
lemma Cfg.spaceUsed_step {tm : SingleTapeTM Symbol} (cfg cfg' : tm.Cfg)
    (hstep : tm.step cfg = some cfg') : cfg'.spaceUsed ≤ cfg.spaceUsed + 1
```

`Cslib.Turing.SingleTapeTM.TransitionRelation` (definition, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L201))

> The `TransitionRelation` corresponding to a `SingleTapeTM Symbol`
> is defined by the `step` function,
> which maps a configuration to its next configuration, if it exists.

```lean
def TransitionRelation (tm : SingleTapeTM Symbol) (c₁ c₂ : tm.Cfg) : Prop
```

`Cslib.Turing.SingleTapeTM.Outputs` (definition, [line 204](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L204))

> A proof of `tm` outputting `l'` on input `l`.

```lean
def Outputs (tm : SingleTapeTM Symbol) (l l' : List Symbol) : Prop
```

`Cslib.Turing.SingleTapeTM.OutputsWithinTime` (definition, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L208))

> A proof of `tm` outputting `l'` on input `l` in at most `m` steps.

```lean
def OutputsWithinTime (tm : SingleTapeTM Symbol) (l l' : List Symbol) (m : ℕ)
```

`Cslib.Turing.SingleTapeTM.output_length_le_input_length_add_time` (lemma, [line 218](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L218))

> This lemma bounds the size blow-up of the output of a Turing machine.
> It states that the increase in length of the output over the input is bounded by the runtime.
> This is important for guaranteeing that composition of polynomial time Turing machines
> remains polynomial time, as the input to the second machine
> is bounded by the output length of the first machine.

```lean
lemma output_length_le_input_length_add_time (tm : SingleTapeTM Symbol) (l l' : List Symbol) (t : ℕ)
    (h : tm.OutputsWithinTime l l' t) :
    l'.length ≤ max 1 l.length + t
```

`Cslib.Turing.SingleTapeTM.idComputer` (definition, [line 228](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L228))

> A Turing machine computing the identity.

```lean
def idComputer : SingleTapeTM Symbol
```

`Cslib.Turing.SingleTapeTM.compComputer` (definition, [line 240](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L240))

> A Turing machine computing the composition of two other Turing machines.
>
> If f and g are computed by Turing machines `tm1` and `tm2`
> then we can construct a Turing machine which computes g ∘ f by first running `tm1`
> and then, when `tm1` halts, transitioning to the start state of `tm2` and running `tm2`.

```lean
def compComputer (tm1 tm2 : SingleTapeTM Symbol) : SingleTapeTM Symbol
```

> ### Composition Computer Lemmas

`Cslib.Turing.SingleTapeTM.compComputer_q₀_eq` (lemma, [line 275](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L275))

```lean
lemma compComputer_q₀_eq : (compComputer tm1 tm2).q₀ = Sum.inl tm1.q₀
```

> ## Time Computability
>
> This section defines the notion of time-bounded Turing Machines

`Cslib.Turing.SingleTapeTM.TimeComputable` (structure, [line 392](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L392))

> A Turing machine + a time function +
> a proof it outputs `f` in at most `time(input.length)` steps.

```lean
structure TimeComputable (f : List Symbol → List Symbol) where
  /-- the underlying bundled SingleTapeTM -/
  tm : SingleTapeTM Symbol
  /-- a bound on runtime -/
  timeBound : ℕ → ℕ
  /-- proof this machine outputs `f` in at most `timeBound(input.length)` steps -/
  outputsFunInTime (a) : tm.OutputsWithinTime a (f a) (timeBound a.length)
```

`Cslib.Turing.SingleTapeTM.TimeComputable.id` (definition, [line 402](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L402))

> The identity map on Symbol is computable in constant time.

```lean
def TimeComputable.id : TimeComputable (Symbol := Symbol) id
```

`Cslib.Turing.SingleTapeTM.TimeComputable.comp` (definition, [line 421](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L421))

> Time bounds for `compComputer`.
>
> The `compComputer` of two machines which have time bounds is bounded by
>
> * The time taken by the first machine on the input size
> * added to the time taken by the second machine on the output size of the first machine
>   (which is itself bounded by the time taken by the first machine)
>
> Note that we require the time function of the second machine to be monotone;
> this is to ensure that if the first machine returns an output
> which is shorter than the maximum possible length of output for that input size,
> then the time bound for the second machine still holds for that shorter input to the second machine.

```lean
def TimeComputable.comp {f g : List Symbol → List Symbol}
    (hf : TimeComputable f) (hg : TimeComputable g)
    (h_mono : Monotone hg.timeBound) :
    (TimeComputable (g ∘ f))
```

`Cslib.Turing.SingleTapeTM.TimeComputable.withMonotoneBound` (definition, [line 461](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L461))

> Convert a `TimeComputable` to one with a monotone time bound, by replacing the time bound `t`
> with `partialSups t`, i.e. `n ↦ max (t 0) ⋯ (t n)`. The underlying machine is unchanged.

```lean
def TimeComputable.withMonotoneBound {f : List Symbol → List Symbol}
    (hf : TimeComputable f) : TimeComputable f
```

`Cslib.Turing.SingleTapeTM.TimeComputable.withMonotoneBound_timeBound_monotone` (lemma, [line 468](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L468))

```lean
lemma TimeComputable.withMonotoneBound_timeBound_monotone {f : List Symbol → List Symbol}
    (hf : TimeComputable f) : Monotone hf.withMonotoneBound.timeBound
```

> ## Polynomial Time Computability
>
> This section defines polynomial time computable functions on Turing machines,
> and proves that:
>
> * The identity function is polynomial time computable
> * The composition of two polynomial time computable functions is polynomial time computable

`Cslib.Turing.SingleTapeTM.PolyTimeComputable` (structure, [line 491](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L491))

> A Turing machine + a polynomial time function +
> a proof it outputs `f` in at most `time(input.length)` steps.

```lean
structure PolyTimeComputable (f : List Symbol → List Symbol) extends TimeComputable f where
  /-- a polynomial time bound -/
  poly : Polynomial ℕ
  /-- proof that this machine outputs `f` in at most `time(input.length)` steps -/
  bounds : ∀ n, timeBound n ≤ poly.eval n
```

`Cslib.Turing.SingleTapeTM.PolyTimeComputable.id` (definition, [line 498](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L498))

> A proof that the identity map on Symbol is computable in polytime.

```lean
noncomputable def PolyTimeComputable.id : PolyTimeComputable (Symbol := Symbol) id
```

`Cslib.Turing.SingleTapeTM.PolyTimeComputable.withMonotoneBound` (definition, [line 507](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L507))

> Convert a `PolyTimeComputable` to one with a monotone time bound.
> The polynomial bound is unchanged, since polynomial evaluation over `ℕ` is monotone.

```lean
noncomputable def PolyTimeComputable.withMonotoneBound {f : List Symbol → List Symbol}
    (hf : PolyTimeComputable f) : PolyTimeComputable f
```

`Cslib.Turing.SingleTapeTM.PolyTimeComputable.comp` (definition, [line 519](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean#L519))

> A proof that the composition of two polytime computable functions is polytime computable.
>
> The time bound of `hg` is first replaced by a monotone one via `withMonotoneBound`,
> so that no monotonicity assumption is required of the caller.

```lean
noncomputable def PolyTimeComputable.comp {f g : List Symbol → List Symbol}
    (hf : PolyTimeComputable f) (hg : PolyTimeComputable g) :
    PolyTimeComputable (g ∘ f)
```

## Depends on

- [BiTape: Bidirectionally infinite TM tape representation using StackTape](../../../../foundations/data/bitape.md)
- [Relations Across Steps](../../../../foundations/relation/relatesinsteps.md)

## Proof depends on

- [Monotonicity of polynomial evaluation](../../../../foundations/data/polynomial/monotone.md)

## Sources

- [Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Deterministic.lean)
