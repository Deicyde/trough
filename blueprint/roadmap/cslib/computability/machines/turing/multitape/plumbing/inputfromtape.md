---
catalog: module
lean: Turing.MultiTapeTM.clampMove, Turing.MultiTapeTM.inputFromTape, Turing.MultiTapeTM.inCfg, Turing.MultiTapeTM.inCfg_inputPos, Turing.MultiTapeTM.inCfg_workTapes_castAdd, Turing.MultiTapeTM.inCfg_workTapes_vip, Turing.MultiTapeTM.inCfg_workTapes_flag, Turing.MultiTapeTM.inCfg_workTapePos_castAdd, Turing.MultiTapeTM.inCfg_workTapePos_natAdd, Turing.MultiTapeTM.inCfg_workTapeSymbols_castAdd, Turing.MultiTapeTM.inCfg_workTapeSymbols_vip, Turing.MultiTapeTM.inCfg_workTapeSymbols_flag, Turing.MultiTapeTM.val_moveInputPos_sub_one_eq_clampMove, Turing.MultiTapeTM.inCfgHom, Turing.MultiTapeTM.space_map_inCfgHom_le
statement: formalized
proof: formalized
---

# Reading the input from a work tape

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.InputFromTape`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean), by Christian Reitwiessner, Samuel Schlesinger.

> `inputFromTape tm` behaves like `tm`, except that it reads its input from a work tape — the
> *virtual input tape* — instead of the real one, which it never touches. The virtual input head
> lives at cell `p - 1` when the simulated input head is at position `p`, so the word cells
> `0, …, len - 1` are the input positions `1, …, len` and the two boundary positions read the blanks
> at cells `-1` and `len`.
>
> The one thing a blank cell cannot tell the machine is *which* boundary it is at — and it must
> know, because the input head clamps there. This ambiguity is resolved by tracking a boundary
> classification. A second fresh work tape, the *flag tape*, moves in lockstep with the virtual input
> head and carries a single non-blank `mark` at cell `-1`, so the left boundary is recognised by
> reading the flag. Reading blank on both the virtual input tape and the flag tape means the right
> boundary.
>
> The configuration map `inCfg` places the simulated input on the virtual input tape, places the
> marker on the flag tape, and leaves the real input tape unused. It is a homomorphism of step
> relations (`inCfgHom`), so each run path of `tm` maps to a run path of the redirected machine.

`Turing.MultiTapeTM.clampMove` (definition, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L40))

> The clamped move of the virtual input head: at the left boundary (blank under the virtual
> head, flag marked) left moves are blocked, at the right boundary (blank on both) right moves
> are.

```lean
public def clampMove (wvip wflag : Option Symbol) (m : SignType) : SignType
```

`Turing.MultiTapeTM.inputFromTape` (definition, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L51))

> `tm`, reading its input from the virtual input tape `Fin.natAdd k 0`, with the flag tape
> `Fin.natAdd k 1` marking the cell left of the input. The real input tape is never read and never
> moved.

```lean
public noncomputable def inputFromTape (tm : MultiTapeTM k Symbol State) :
MultiTapeTM (k + 2) Symbol State
```

`Turing.MultiTapeTM.inCfg` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L67))

> A configuration of `tm` on `input`, as the redirecting machine sees it, over an arbitrary
> ambient input: `input` sits on the virtual input tape with the head at cell `inputPos - 1`, the flag
> tape carries its mark at `-1` with its head in lockstep, and the ambient input head rests at
> `1`.

```lean
public def inCfg (mark : Symbol) {input : List Symbol} (c : Cfg k Symbol State input)
(outerInput : List Symbol) : Cfg (k + 2) Symbol State outerInput
```

`Turing.MultiTapeTM.inCfg_inputPos` (lemma, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L81))

```lean
public lemma inCfg_inputPos (c : Cfg k Symbol State input) :
    (inCfg mark c outerInput).inputPos = 1
```

`Turing.MultiTapeTM.inCfg_workTapes_castAdd` (lemma, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L85))

```lean
public lemma inCfg_workTapes_castAdd (c : Cfg k Symbol State input) (j : Fin k) :
    (inCfg mark c outerInput).workTapes (j.castAdd 2) = c.workTapes j
```

`Turing.MultiTapeTM.inCfg_workTapes_vip` (lemma, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L90))

```lean
public lemma inCfg_workTapes_vip (c : Cfg k Symbol State input) :
    (inCfg mark c outerInput).workTapes (Fin.natAdd k 0) = tapeOfList input
```

`Turing.MultiTapeTM.inCfg_workTapes_flag` (lemma, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L95))

```lean
public lemma inCfg_workTapes_flag (c : Cfg k Symbol State input) :
    (inCfg mark c outerInput).workTapes (Fin.natAdd k 1) =
      Function.update (fun _ => none) (-1) (some mark)
```

`Turing.MultiTapeTM.inCfg_workTapePos_castAdd` (lemma, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L101))

```lean
public lemma inCfg_workTapePos_castAdd (c : Cfg k Symbol State input) (j : Fin k) :
    (inCfg mark c outerInput).workTapePos (j.castAdd 2) = c.workTapePos j
```

`Turing.MultiTapeTM.inCfg_workTapePos_natAdd` (lemma, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L107))

> The virtual input head and the flag head both stand at cell `inputPos - 1`.

```lean
public lemma inCfg_workTapePos_natAdd (c : Cfg k Symbol State input) (i : Fin 2) :
    (inCfg mark c outerInput).workTapePos (Fin.natAdd k i) = (c.inputPos.val : ℤ) - 1
```

`Turing.MultiTapeTM.inCfg_workTapeSymbols_castAdd` (lemma, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L112))

```lean
public lemma inCfg_workTapeSymbols_castAdd (c : Cfg k Symbol State input) (j : Fin k) :
    (inCfg mark c outerInput).workTapeSymbols (j.castAdd 2) = c.workTapeSymbols j
```

`Turing.MultiTapeTM.inCfg_workTapeSymbols_vip` (lemma, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L119))

> The virtual input head reads exactly what the simulated input head reads: the word cells are
> the input positions, the two boundary cells are blank.

```lean
public lemma inCfg_workTapeSymbols_vip (c : Cfg k Symbol State input) :
    (inCfg mark c outerInput).workTapeSymbols (Fin.natAdd k 0) = c.inputSymbol
```

`Turing.MultiTapeTM.inCfg_workTapeSymbols_flag` (lemma, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L134))

> The flag head reads the mark exactly at the left boundary.

```lean
public lemma inCfg_workTapeSymbols_flag (c : Cfg k Symbol State input) :
    (inCfg mark c outerInput).workTapeSymbols (Fin.natAdd k 1) =
      if c.inputPos.val = 0 then some mark else none
```

`Turing.MultiTapeTM.val_moveInputPos_sub_one_eq_clampMove` (lemma, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L140))

> The clamped move of the virtual input head tracks the simulated input head exactly.

```lean
public lemma val_moveInputPos_sub_one_eq_clampMove (mark : Symbol) (c : Cfg k Symbol State input)
    (m : SignType) :
    ((moveInputPos c.inputPos m).val : ℤ) - 1 =
      ((c.inputPos.val : ℤ) - 1) +
        (clampMove c.inputSymbol (if c.inputPos.val = 0 then some mark else none) m : ℤ)
```

`Turing.MultiTapeTM.inCfgHom` (definition, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L161))

> The redirection preserves steps, so it maps run paths of `tm` to run paths of the redirected
> machine.

```lean
public noncomputable def inCfgHom (tm : MultiTapeTM k Symbol State)
(mark : Symbol) (outerInput : List Symbol) :
(tm.stepRel input).Hom (tm.inputFromTape.stepRel outerInput)
```

`Turing.MultiTapeTM.space_map_inCfgHom_le` (lemma, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean#L176))

> **Space of the input-redirected path.** The `k` inner tapes visit exactly what the original
> path visits; the two extra tapes (virtual input, flag) each move only with the simulated input
> head, which stays within `[-1, input.length]`, so they add at most `2 * (input.length + 2)`.

```lean
public lemma space_map_inCfgHom_le (tm : MultiTapeTM k Symbol State) (mark : Symbol)
    (outerInput : List Symbol) (p : tm.RunPath input) :
    (p.map (inCfgHom tm mark outerInput)).space ≤ p.space + 2 * (input.length + 2)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)
- [Tapes holding words and configurations of such tapes](wordscfg.md)

## Proof depends on

- [Extending a machine with additional work tapes](extendtapes.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/InputFromTape.lean)
