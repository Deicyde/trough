---
catalog: module
lean: Turing.Action, Turing.Cfg, Turing.Cfg.ext_zero_tapes, Turing.moveInputPos, Turing.moveInputPos_zero, Turing.moveInputPos_leftBoundary, Turing.moveInputPos_rightBoundary, Turing.moveInputPos_neg_of_ne_left, Turing.moveInputPos_pos_of_ne_right, Turing.val_moveInputPos_eq, Turing.val_moveInputPos_le, Turing.Cfg.inputSymbol, Turing.inputSymbol_eq_none_of_boundary, Turing.inputSymbolInner, Turing.Cfg.workTapeSymbols, Turing.HeadSymbols, Turing.Cfg.headSymbols, Turing.Cfg.Halted, Turing.Cfg.prependOutput, Turing.Cfg.withState, Turing.Cfg.mapState, Turing.Cfg.init, Turing.Action.apply, Turing.workTapePos_apply_le
statement: formalized
proof: formalized
---

# Configurations of Multi-Tape Turing Machines

`Cslib.Computability.Machines.Turing.MultiTape.Configuration`, in [Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean), by Christian Reitwiessner, Samuel Schlesinger, Aviv Bar Natan.

> Configurations of a multi-tape Turing machine with a read-only input tape, `k` work tapes and one
> write-only output tape, together with what a single transition does to a configuration.
>
> The configurations are used by both deterministic and nondeterministic multi-tape Turing machines
> and give instantaneous descriptions of their state. An `Action` describes how one configuration
> transitions to the next. It records which way the input head moves, what is written and where the
> work heads move, which symbol is emitted and which state follows. `Action.apply` carries out the
> action on a configuration.
>
> ## Design
>
> Configurations and actions are defined independently of a machine.
>
> The output tape is part of the configuration, so the string emitted along a run can be read off
> the configuration the run ends in. An action can optionally output one symbol, which models the
> write-only output tape.
>
> The input head can move freely on the input, but any move attempt beyond one cell outside the input
> results in no movement. Restricting the movement of the input head is not essential, but useful
> because it allows us to easily bound the number of possible configurations of a space-bounded
> machine. Most textbooks have this restriction.
>
> This definition is adapted from the one in [Papadimitriou94], chapter 2.3 including
> the sub-linear space modifications from chapter 2.5 with the following changes:
>
> - We allow Turing machines to choose to not write on a tape. This is equivalent to
>   writing the read symbol again but makes it easier to reason about the semantics.
> - Our tapes are infinite in both directions instead of just to the right. This definition is
>   equivalent (see [AroraBarak09], Claim 1.4). It saves us from having to add a "start marker" to
>   the alphabet.
> - We only have a single halting state. The different ways to halt (accepting, rejecting, etc) can
>   be distinguished based on the output.
> - The input-head restriction is enforced by `Action.apply`, rather than by restricting the
>   transition relation. The two definitions are equivalent, but allowing all actions makes it
>   easier to define a universal machine.
>
> ## Important Declarations
>
> * `Cfg`: the configuration: the internal state, the tape contents and head positions, and the
>     output tape
> * `Action`: what a machine does in one step
> * `Action.apply`: the effect of one action on a configuration
> * `HeadSymbols`, `Cfg.headSymbols`: the symbols under the heads, which a transition reads
> * `Cfg.Halted`, `Cfg.init`: halting, and the configuration a machine starts in
>
> ## References
>
> * [C. Papadimitriou, *Computational Complexity*][Papadimitriou94]
> * [S. Arora, B. Barak, *Computational Complexity: A Modern Approach*][AroraBarak09]

`Turing.Action` (structure, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L79))

> What a machine does in one step.

```lean
structure Action (k : ℕ) (Symbol State : Type*) where
  /-- The movement (attempt) of the input head. -/
  inputTape : SignType
  /-- Actions on the work tapes: optionally a symbol to write and the head movement. -/
  workTapes : Fin k → (Option (Option Symbol)) × SignType
  /-- An optional symbol to output. -/
  output : Option Symbol
  /-- The successor state or none to halt. -/
  state : Option State
```

`Turing.Cfg` (structure, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L98))

> The configurations of a Turing machine is relative to the input of the machine and consist of:
> - an `Option`al state (or none for the halting state),
> - the position of the input head (shifted by one),
> - the contents of the work tape,
> - the positions of the work tape heads,
> - the contents of the write-only output tape

```lean
structure Cfg (k : ℕ) (Symbol State : Type*) (input : List Symbol) where
  /-- the state of the TM (or none for the halting state) -/
  state : Option State
  /-- the position of the input head, shifted by one -/
  inputPos : Fin (input.length + 2)
  /-- the work tapes -/
  workTapes : Fin k → ℤ → Option Symbol
  /-- the positions of the heads on the work tapes -/
  workTapePos : Fin k → ℤ
  /-- the contents of the write-only output tape -/
  output : List Symbol
deriving Inhabited
```

`Turing.Cfg.ext_zero_tapes` (lemma, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L113))

> Two configurations with no work tapes are equal when their state, input head and output
> agree.

```lean
lemma Cfg.ext_zero_tapes {Symbol State : Type*} {input : List Symbol}
    {cfg₁ cfg₂ : Cfg 0 Symbol State input} (state : cfg₁.state = cfg₂.state)
    (inputPos : cfg₁.inputPos = cfg₂.inputPos) (output : cfg₁.output = cfg₂.output) :
    cfg₁ = cfg₂
```

`Turing.moveInputPos` (definition, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L126))

> Attempt to move the input tape head.
> The machine can only read one empty cell outside of the input,
> any attempted movement beyond that results in no movement.
>
> The addition is performed in `ℤ` before clamping. Performing it in `Fin (n + 2)` would wrap an
> outward boundary move to the opposite end of the input.

```lean
def moveInputPos {n : ℕ} (pos : Fin (n + 2)) (m : SignType) : Fin (n + 2)
```

`Turing.moveInputPos_zero` (lemma, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L131))

```lean
lemma moveInputPos_zero {n : ℕ} (pos : Fin (n + 2)) :
    moveInputPos pos 0 = pos
```

`Turing.moveInputPos_leftBoundary` (lemma, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L137))

```lean
lemma moveInputPos_leftBoundary {n : ℕ} :
    moveInputPos (0 : Fin (n + 2)) (-1) = 0
```

`Turing.moveInputPos_rightBoundary` (lemma, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L143))

```lean
lemma moveInputPos_rightBoundary {n : ℕ} :
    moveInputPos (⟨n + 1, by omega⟩ : Fin (n + 2)) 1 = ⟨n + 1, by omega⟩
```

`Turing.moveInputPos_neg_of_ne_left` (lemma, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L149))

> A left move away from the left input boundary decrements the native input position.

```lean
lemma moveInputPos_neg_of_ne_left {n : ℕ} (p : Fin (n + 2)) (h : p ≠ 0) :
    moveInputPos p .neg = ⟨p.val - 1, by have := p.isLt; omega⟩
```

`Turing.moveInputPos_pos_of_ne_right` (lemma, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L157))

> A right move away from the right input boundary increments the native input position.

```lean
lemma moveInputPos_pos_of_ne_right {n : ℕ} (p : Fin (n + 2)) (h : p.val ≠ n + 1) :
    moveInputPos p .pos = ⟨p.val + 1, by have := p.isLt; omega⟩
```

`Turing.val_moveInputPos_eq` (lemma, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L167))

> The value of the input head after a move, as a clamped integer. `omega`-friendly.

```lean
lemma val_moveInputPos_eq {n : ℕ} (pos : Fin (n + 2)) (m : SignType) :
    ((moveInputPos pos m).val : ℤ) = min ((n : ℤ) + 1) (max 0 ((pos.val : ℤ) + (m.cast : ℤ)))
```

`Turing.val_moveInputPos_le` (lemma, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L172))

> The input head moves by at most one position.

```lean
lemma val_moveInputPos_le {n : ℕ} (pos : Fin (n + 2)) (m : SignType) :
    (moveInputPos pos m).val ≤ pos.val + 1
```

`Turing.Cfg.inputSymbol` (definition, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L180))

> The symbol currently under the input tape head.

```lean
def Cfg.inputSymbol (cfg : Cfg k Symbol State input) : Option Symbol
```

`Turing.inputSymbol_eq_none_of_boundary` (lemma, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L186))

> At either boundary of the input, the head reads a blank.

```lean
lemma inputSymbol_eq_none_of_boundary {cfg : Cfg k Symbol State input}
    (h : cfg.inputPos.val = 0 ∨ cfg.inputPos.val = input.length + 1) :
    cfg.inputSymbol = none
```

`Turing.inputSymbolInner` (lemma, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L192))

```lean
lemma inputSymbolInner {cfg : Cfg k Symbol State input} (p : ℕ)
    (h₁ : cfg.inputPos.val = 1 + p)
    (h₂ : p < input.length) :
    cfg.inputSymbol = some input[p]
```

`Turing.Cfg.workTapeSymbols` (definition, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L199))

> The symbol read by work tape `i`.

```lean
def Cfg.workTapeSymbols (cfg : Cfg k Symbol State input) (i : Fin k) : Option Symbol
```

`Turing.HeadSymbols` (structure, [line 204](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L204))

> The symbols under the heads of a machine with `k` work tapes, which its transitions read.

```lean
structure HeadSymbols (k : ℕ) (Symbol : Type*) where
  /-- the symbol under the input head -/
  inputSymbol : Option Symbol
  /-- the symbols under the work-tape heads -/
  workTapeSymbols : Fin k → Option Symbol
```

`Turing.Cfg.headSymbols` (definition, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L212))

> The symbols under the heads of a configuration.

```lean
def Cfg.headSymbols (cfg : Cfg k Symbol State input) : HeadSymbols k Symbol
```

`Turing.Cfg.Halted` (abbreviation, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L216))

> A configuration is halted when it has no state to continue from.

```lean
abbrev Cfg.Halted (cfg : Cfg k Symbol State input) : Prop
```

`Turing.Cfg.prependOutput` (definition, [line 220](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L220))

> The same configuration with a word prepended to the output tape. A machine never reads its
> output, so prepending to it preserves steps: cf. `Turing.MultiTapeNTM.prependOutputHom`.

```lean
def Cfg.prependOutput (c : Cfg k Symbol State input) (pre : List Symbol) :
    Cfg k Symbol State input
```

`Turing.Cfg.withState` (definition, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L225))

> The same configuration in a different control state, possibly of a different state type.

```lean
def Cfg.withState (cfg : Cfg k Symbol State input)
    {State' : Type*} (q : Option State') : Cfg k Symbol State' input
```

`Turing.Cfg.mapState` (definition, [line 232](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L232))

> Remap the (optional) state of a configuration through `φ`, leaving the input head, the work
> tapes, the work-tape heads and the output alone. Control-flow combinators such as `seq` embed a
> sub-machine's configurations into the combined machine by exactly such a state remap.

```lean
def Cfg.mapState {State' : Type*} (φ : Option State → Option State')
    (c : Cfg k Symbol State input) : Cfg k Symbol State' input
```

`Turing.Cfg.init` (definition, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L238))

> The initial configuration for a starting state and an input string.

```lean
def Cfg.init (q₀ : State) (input : List Symbol) : Cfg k Symbol State input
```

`Turing.Action.apply` (definition, [line 247](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L247))

> The effect of an action on a configuration: move the input head, write and move on the work tapes,
> append the emitted symbol to the output tape, and go to the successor state. This is the part of a
> step that does not depend on how the action was chosen.

```lean
def Action.apply (action : Action k Symbol State) (cfg : Cfg k Symbol State input) :
    Cfg k Symbol State input
```

`Turing.workTapePos_apply_le` (lemma, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean#L258))

> A work tape head moves by at most one cell when an action is applied.

```lean
lemma workTapePos_apply_le (action : Action k Symbol State)
    (cfg : Cfg k Symbol State input) (i : Fin k) :
    |(action.apply cfg).workTapePos i - cfg.workTapePos i| ≤ 1
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Configuration.lean)
