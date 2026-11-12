---
catalog: module
lean: RelSeries.exists_of_mem_map, RelSeries.mem_or_mem_of_mem_smash, Turing.MultiTapeNTM, Turing.MultiTapeNTM.Step, Turing.MultiTapeNTM.step_of_halt, Turing.MultiTapeNTM.initCfg, Turing.MultiTapeNTM.stepRel, Turing.MultiTapeNTM.runningStepRel, Turing.MultiTapeNTM.RunPath, Turing.MultiTapeNTM.RunPath.map, Turing.MultiTapeNTM.RunPath.length_output_mono, Turing.MultiTapeNTM.RunPath.last_eq_of_head_halted, Turing.MultiTapeNTM.RunPath.last_eq_of_halted, Turing.MultiTapeNTM.RunPath.time, Turing.MultiTapeNTM.RunPath.exists_running, Turing.MultiTapeNTM.ComputationPath, Turing.MultiTapeNTM.ComputationPath.time, Turing.MultiTapeNTM.RunsInTime, Turing.MultiTapeNTM.RunsInTime.mono, Turing.MultiTapeNTM.Adapter, Turing.MultiTapeNTM.Adapter.mapState, Turing.MultiTapeNTM.Follows, Turing.MultiTapeNTM.Follows.step, Turing.MultiTapeNTM.Follows.runningStepHom, Turing.MultiTapeNTM.Follows.stepHom, Turing.MultiTapeNTM.prependOutputHom
statement: formalized
proof: formalized
---

# Nondeterministic Multi-Tape Turing Machines

`Cslib.Computability.Machines.Turing.MultiTape.Nondeterministic`, in [Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean), by Aviv Bar Natan.

> Defines nondeterministic Turing machines with a read-only input tape, `k` work tapes and one
> write-only output tape, their computation paths, and time bounds.
>
> ## Design
>
> The design choices for configurations and actions are documented in
> `Cslib.Computability.Machines.Turing.MultiTape.Configuration`.
>
> Following [Papadimitriou94], chapter 2.7, a nondeterministic machine is a Turing machine whose
> transition function is replaced by a transition relation: `Tr q input work action` holds when `Tr`
> relates the state `q` and the read symbols `input` and `work` to `action`.
>
> A halted configuration steps to itself, so once a machine has halted it has a run of every length.
> A time bound is therefore an upper bound, with no separate account of the step at which it halted.
>
> The transition relation may be empty at a running configuration. Such a configuration has no
> successor configuration and is called stuck.
>
> Time bounds apply to every computation path, regardless of its outcome. `RunsInTime input t`
> requires every path of at least `t` steps to end in a halted configuration.
>
> ## Important Declarations
>
> * `MultiTapeNTM`: the machine, an initial state and a transition relation
> * `Step`: the one-step relation on configurations
> * `RunPath`: finite relation series of steps
> * `ComputationPath`: a run path starting at the initial configuration
> * `Adapter`, `Follows`: a machine follows another when it performs each of its transitions,
>   reading and acting through an adapter
> * `Follows.step`, `Follows.runningStepHom`, `Follows.stepHom`: a configuration map that agrees with
>   the adapter maps steps to steps, so it is a homomorphism of step relations and maps run paths
> * `RunsInTime`: every computation path of at least the given length ends in a halted
>   configuration
>
> ## References
>
> * [C. Papadimitriou, *Computational Complexity*][Papadimitriou94]
> * [M. Sipser, *Introduction to the Theory of Computation*][Sipser2013]

`RelSeries.exists_of_mem_map` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L62))

> A member of a mapped series is the image of a member.

```lean
lemma exists_of_mem_map {p : RelSeries r} {f : r.Hom s} {b : β} (hb : b ∈ p.map f) :
    ∃ a ∈ p, f a = b
```

`RelSeries.mem_or_mem_of_mem_smash` (lemma, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L68))

> A member of two joined series lies on one of them.

```lean
lemma mem_or_mem_of_mem_smash {p q : RelSeries r} {h : p.last = q.head} {a : α}
    (ha : a ∈ p.smash q h) : a ∈ p ∨ a ∈ q
```

`Turing.MultiTapeNTM` (structure, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L85))

> A nondeterministic multi-tape Turing machine with `k` work tapes over the alphabet of
> `Option Symbol` (where `none` is the blank symbol). Neither `Symbol` nor `State` is required to be
> finite.

```lean
structure MultiTapeNTM (k : ℕ) (Symbol State : Type*) where
  /-- initial state -/
  q₀ : State
  /-- transition relation: which combinations of state, current input symbol, tuple of work head
  symbols and resulting actions are valid transitions -/
  Tr (q : State) (input : Option Symbol) (work : Fin k → Option Symbol)
    (action : Action k Symbol State) : Prop
```

`Turing.MultiTapeNTM.Step` (definition, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L100))

> The one-step relation on configurations. A halted configuration steps only to itself. A running
> configuration steps by applying any action related to its state and read symbols by `Tr`.

```lean
def Step (ntm : MultiTapeNTM k Symbol State) (c₁ c₂ : Cfg k Symbol State input) : Prop
```

`Turing.MultiTapeNTM.step_of_halt` (lemma, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L107))

> A halted configuration steps only to itself.

```lean
lemma step_of_halt {c c' : Cfg k Symbol State input} (h : c.Halted) :
    ntm.Step c c' ↔ c' = c
```

`Turing.MultiTapeNTM.initCfg` (definition, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L113))

> The initial configuration corresponding to an input string.

```lean
def initCfg (ntm : MultiTapeNTM k Symbol State) (input : List Symbol) :
    Cfg k Symbol State input
```

`Turing.MultiTapeNTM.stepRel` (abbreviation, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L118))

> The one-step relation on configurations for `input`, as a set of pairs.

```lean
abbrev stepRel (ntm : MultiTapeNTM k Symbol State) (input : List Symbol) :
    SetRel (Cfg k Symbol State input) (Cfg k Symbol State input)
```

`Turing.MultiTapeNTM.runningStepRel` (abbreviation, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L123))

> The steps of `ntm` from running configurations: the steps within a run until it halts.

```lean
abbrev runningStepRel (ntm : MultiTapeNTM k Symbol State) (input : List Symbol) :
    SetRel (Cfg k Symbol State input) (Cfg k Symbol State input)
```

`Turing.MultiTapeNTM.RunPath` (abbreviation, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L128))

> A nonempty list of configurations joined by steps of `ntm`.

```lean
abbrev RunPath (ntm : MultiTapeNTM k Symbol State) (input : List Symbol)
```

`Turing.MultiTapeNTM.RunPath.map` (abbreviation, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L135))

> A run path mapped along a step-preserving map of configurations: `RelSeries.map`, typed as a
> run path of the target machine.

```lean
abbrev map {k' : ℕ} {State' : Type*} {input' : List Symbol} {ntm' : MultiTapeNTM k' Symbol State'}
    (p : ntm.RunPath input) (f : (ntm.stepRel input).Hom (ntm'.stepRel input')) :
    ntm'.RunPath input'
```

`Turing.MultiTapeNTM.RunPath.length_output_mono` (lemma, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L141))

> The output only grows along a run path.

```lean
lemma length_output_mono (p : ntm.RunPath input) :
    Monotone fun i ↦ (p i).output.length
```

`Turing.MultiTapeNTM.RunPath.last_eq_of_head_halted` (lemma, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L149))

> Once a run path is halted, its configuration stays unchanged.

```lean
lemma last_eq_of_head_halted (p : ntm.RunPath input) (h : p.head.Halted) : p.last = p.head
```

`Turing.MultiTapeNTM.RunPath.last_eq_of_halted` (lemma, [line 158](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L158))

> The last configuration equals any earlier halted configuration.

```lean
lemma last_eq_of_halted (p : ntm.RunPath input) (i : Fin (p.length + 1))
    (h : (p i).Halted) : p.last = p i
```

`Turing.MultiTapeNTM.RunPath.time` (definition, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L163))

> The number of steps taken by a run path.

```lean
def time (p : ntm.RunPath input) : ℕ
```

`Turing.MultiTapeNTM.RunPath.exists_running` (lemma, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L167))

> A path that ends halted runs from its head to its last configuration in running steps, up to
> its first halted configuration.

```lean
lemma exists_running (p : ntm.RunPath input) (h : p.last.Halted) :
    ∃ q : RelSeries (ntm.runningStepRel input), q.head = p.head ∧ q.last = p.last ∧
      q.length ≤ p.length ∧ ∀ c ∈ q, c ∈ p
```

`Turing.MultiTapeNTM.ComputationPath` (structure, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L181))

> A run path starting at the initial configuration for `input`.

```lean
structure ComputationPath (ntm : MultiTapeNTM k Symbol State) (input : List Symbol)
    extends toRunPath : ntm.RunPath input where
  /-- the path starts at the initial configuration -/
  head_eq : toRunPath.head = ntm.initCfg input
```

`Turing.MultiTapeNTM.ComputationPath.time` (definition, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L189))

> The number of steps taken by a computation path.

```lean
def time (p : ntm.ComputationPath input) : ℕ
```

`Turing.MultiTapeNTM.RunsInTime` (definition, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L195))

> Every computation path on `input` of at least `t` steps ends in a halted configuration.
> A path ending in a stuck configuration must have fewer than `t` steps.

```lean
def RunsInTime (ntm : MultiTapeNTM k Symbol State) (input : List Symbol) (t : ℕ) : Prop
```

`Turing.MultiTapeNTM.RunsInTime.mono` (lemma, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L199))

> A time bound can be increased.

```lean
lemma RunsInTime.mono {input : List Symbol} {t t' : ℕ}
    (h : ntm.RunsInTime input t) (ht : t ≤ t') : ntm.RunsInTime input t'
```

> ### Following a machine

`Turing.MultiTapeNTM.Adapter` (structure, [line 210](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L210))

> How a machine with `k'` work tapes and states `State'` performs the transitions of a machine
> with `k` work tapes and states `State`. A transition turns the symbols under the heads into an
> action, so the outer machine translates both ends: `read` computes the symbols the inner machine
> reads from those under the outer heads, and `action` turns the inner action into an outer one,
> which may also depend on the outer symbols.

```lean
structure Adapter (k k' : ℕ) (Symbol State State' : Type*) where
  /-- the symbols the inner machine reads -/
  read : HeadSymbols k' Symbol → HeadSymbols k Symbol
  /-- the outer action performing an inner action -/
  action : HeadSymbols k' Symbol → Action k Symbol State → Action k' Symbol State'
```

`Turing.MultiTapeNTM.Adapter.mapState` (definition, [line 218](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L218))

> The adapter that relabels the states through `φ` and reads and acts on the same tapes.

```lean
def Adapter.mapState {State' : Type*} (φ : Option State → Option State') :
    Adapter k k Symbol State State'
```

`Turing.MultiTapeNTM.Follows` (definition, [line 224](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L224))

> `ntm'` follows `ntm` through `adapter`, in state `state q` while `ntm` is in state `q`: whatever
> `ntm` may do in `q` on what `adapter` reads, `ntm'` may do the adapted action in `state q`.

```lean
def Follows {k' : ℕ} {State' : Type*} (ntm' : MultiTapeNTM k' Symbol State')
    (ntm : MultiTapeNTM k Symbol State) (state : State → State')
    (adapter : Adapter k k' Symbol State State') : Prop
```

`Turing.MultiTapeNTM.Follows.step` (lemma, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L239))

> **A follower mirrors a step.** If `ntm'` follows `ntm`, and the map `f` relabels the state of
> `c` through `state`, reads through `adapter` what `c` reads, and carries the action of a step from
> `c` to its adaptation, then `f` maps the step to a step of `ntm'`.

```lean
lemma step (h : ntm'.Follows ntm state adapter)
    (f : Cfg k Symbol State input → Cfg k' Symbol State' input') {c c' : Cfg k Symbol State input}
    (hstep : ntm.Step c c') (hstate : c.state.map state = (f c).state)
    (hread : adapter.read (f c).headSymbols = c.headSymbols)
    (haction : ∀ action, action.apply c = c' →
      (adapter.action (f c).headSymbols action).apply (f c) = f c') :
    ntm'.Step (f c) (f c')
```

`Turing.MultiTapeNTM.Follows.runningStepHom` (definition, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L258))

> **A follower mirrors the running steps.** If `ntm'` follows `ntm`, and `f` sends a configuration
> in state `q` to one in state `state q`, from which `adapter` reads what the configuration reads and
> on which each adapted action acts as the action acts on the configuration, then `f` maps each
> running step of `ntm` to a step of `ntm'`.

```lean
def runningStepHom (h : ntm'.Follows ntm state adapter)
    (f : Cfg k Symbol State input → Cfg k' Symbol State' input')
    (hstate : ∀ c q, c.state = some q → (f c).state = some (state q))
    (hread : ∀ c, adapter.read (f c).headSymbols = c.headSymbols)
    (haction : ∀ c action,
      (adapter.action (f c).headSymbols action).apply (f c) = f (action.apply c)) :
    (ntm.runningStepRel input).Hom (ntm'.stepRel input')
```

`Turing.MultiTapeNTM.Follows.stepHom` (definition, [line 270](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L270))

> **A follower mirrors the steps.** As `runningStepHom`, for an `f` that relabels every state
> through `state`, so that it also keeps halted configurations halted.

```lean
def stepHom (h : ntm'.Follows ntm state adapter)
    (f : Cfg k Symbol State input → Cfg k' Symbol State' input')
    (hstate : ∀ c, c.state.map state = (f c).state)
    (hread : ∀ c, adapter.read (f c).headSymbols = c.headSymbols)
    (haction : ∀ c action,
      (adapter.action (f c).headSymbols action).apply (f c) = f (action.apply c)) :
    (ntm.stepRel input).Hom (ntm'.stepRel input')
```

`Turing.MultiTapeNTM.prependOutputHom` (definition, [line 283](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean#L283))

> A machine never reads its output tape, so prepending a word to the output preserves steps.

```lean
def prependOutputHom (ntm : MultiTapeNTM k Symbol State) (pre : List Symbol) :
    (ntm.stepRel input).Hom (ntm.stepRel input)
```

## Depends on

- [Configurations of Multi-Tape Turing Machines](configuration.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Nondeterministic.lean)
