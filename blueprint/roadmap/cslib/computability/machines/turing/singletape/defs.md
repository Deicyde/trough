---
catalog: module
lean: Cslib.Computability.Turing.SingleTape.TrLabel, Cslib.Computability.Turing.SingleTape.TrLabel.applyToTape, Cslib.Computability.Turing.SingleTape.TrLabel.applyToTape_isSome, Cslib.Computability.Turing.SingleTape.TrLabel.applyToTape_foldl_isSome, Cslib.Computability.Turing.SingleTape.Cfg, Cslib.Computability.Turing.SingleTape.Cfg.mk₁, Cslib.Computability.Turing.SingleTape.Cfg.spaceUsed
statement: formalized
proof: formalized
---

# Basic definitions for Turing Machines (TMs)

`Cslib.Computability.Machines.Turing.SingleTape.Defs`, in [Cslib/Computability/Machines/Turing/SingleTape/Defs.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean), by Fabrizio Montesi, Bolton Bailey.

`Cslib.Computability.Turing.SingleTape.TrLabel` (inductive type, [line 18](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean#L18))

> The transition labels used by a single-tape Turing Machine.

```lean
inductive TrLabel (Symbol : Type*)
  /-- Read `x` from the tape. -/
  | read (x : Symbol)
  /-- Write `x` on the tape. -/
  | write (x : Symbol)
  /-- Move the head of the tape. -/
  | move (d : Turing.Dir)
  /-- Do nothing. -/
  | skip
```

`Cslib.Computability.Turing.SingleTape.TrLabel.applyToTape` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean#L30))

> Applies a transition label to a tape, returning `none` if it is not possible.
> The input is taken as an `Option` to make the function composable.

```lean
def TrLabel.applyToTape [DecidableEq Symbol]
    (otape : Option (Turing.BiTape Symbol)) (μ : TrLabel Symbol) :
    Option (Turing.BiTape Symbol)
```

`Cslib.Computability.Turing.SingleTape.TrLabel.applyToTape_isSome` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean#L41))

```lean
theorem TrLabel.applyToTape_isSome [DecidableEq Symbol] {μ : TrLabel Symbol}
    {ot : Option (Turing.BiTape Symbol)} (h : (μ.applyToTape ot).isSome) : ot.isSome
```

`Cslib.Computability.Turing.SingleTape.TrLabel.applyToTape_foldl_isSome` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean#L48))

```lean
theorem TrLabel.applyToTape_foldl_isSome [DecidableEq Symbol] {μs : List (TrLabel Symbol)}
    {ot : Option (Turing.BiTape Symbol)} (h : (μs.foldl applyToTape ot).isSome) : ot.isSome
```

`Cslib.Computability.Turing.SingleTape.Cfg` (structure, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean#L54))

> Configuration of a single-tape Turing machine.

```lean
structure Cfg (State Symbol : Type*) where
  /-- The state that the machine is in. -/
  state : State
  /-- Tape of the machine (memory). -/
  tape : Turing.BiTape Symbol
```

`Cslib.Computability.Turing.SingleTape.Cfg.mk₁` (definition, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean#L61))

> Helper builder for a configuration with a given tape content.

```lean
def Cfg.mk₁ (s : State) (xs : List Symbol) : Cfg State Symbol
```

`Cslib.Computability.Turing.SingleTape.Cfg.spaceUsed` (definition, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean#L66))

> The space used by a configuration is the space used by its tape.

```lean
def Cfg.spaceUsed (cfg : Cfg State Symbol) : ℕ
```

## Depends on

- [BiTape: Bidirectionally infinite TM tape representation using StackTape](../../../../foundations/data/bitape.md)

## Sources

- [Cslib/Computability/Machines/Turing/SingleTape/Defs.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/SingleTape/Defs.lean)
