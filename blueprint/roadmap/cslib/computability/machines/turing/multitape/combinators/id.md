---
catalog: module
lean: Turing.MultiTapeTM.copy, Turing.MultiTapeTM.Copy.cfg, Turing.MultiTapeTM.Copy.step_scan, Turing.MultiTapeTM.Copy.step_halt, Turing.MultiTapeTM.Copy.runFrom_scan, Turing.MultiTapeTM.Copy.runFrom_full, Turing.MultiTapeTM.Copy.computesInTimeAndSpace, Turing.MultiTapeTM.computableInTimeAndSpace_id
statement: formalized
proof: formalized
---

# Complexity of the identity function

`Cslib.Computability.Machines.Turing.MultiTape.Combinators.Id`, in [Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean), by Christian Reitwiessner.

> A machine with a single state and no work tapes scans the input from left to right, copying each
> symbol to the output tape, and halts on the blank at the right end of the input. On input `w` it
> outputs `w` after `w.length + 1` steps, and having no work tapes it uses zero space.
>
> ## Main results
>
> * `Turing.MultiTapeTM.computableInTimeAndSpace_id`: the identity is computable in one step per
>   input symbol and zero space.

`Turing.MultiTapeTM.copy` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L30))

> The copy machine: a single state and no work tapes. It copies every input symbol to the output
> tape while moving right, and halts on reading the blank at the right end of the input.

```lean
def copy : MultiTapeTM 0 Symbol Unit
```

`Turing.MultiTapeTM.Copy.cfg` (definition, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L41))

> The configuration of the copy machine in state `q` after copying the first `n` input symbols
> to the output: the input head is over cell `n + 1` (capped at the right end marker) and there are
> no work tapes. `input` is explicit because it only occurs in the type.

```lean
def cfg (input : List Symbol) (q : Option Unit) (n : ℕ) : Cfg 0 Symbol Unit input
```

`Turing.MultiTapeTM.Copy.step_scan` (lemma, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L45))

> Over an input symbol, the copy machine emits it and moves right.

```lean
lemma step_scan {n : ℕ} (hn : n < input.length) :
    copy.step (cfg input (some ()) n) = cfg input (some ()) (n + 1)
```

`Turing.MultiTapeTM.Copy.step_halt` (lemma, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L57))

> On the blank at the right end of the input, the copy machine halts in place.

```lean
lemma step_halt :
    copy.step (cfg input (some ()) input.length) = cfg input none input.length
```

`Turing.MultiTapeTM.Copy.runFrom_scan` (lemma, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L65))

> After `n ≤ input.length` steps, the copy machine has copied the first `n` input symbols.

```lean
lemma runFrom_scan (n : ℕ) (hn : n ≤ input.length) :
    copy.runFrom (copy.initCfg input) n = cfg input (some ()) n
```

`Turing.MultiTapeTM.Copy.runFrom_full` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L74))

> The complete run: after `input.length + 1` steps the copy machine has halted with the input
> copied to the output.

```lean
lemma runFrom_full (input : List Symbol) :
    copy.runFrom (copy.initCfg input) (input.length + 1) = cfg input none input.length
```

`Turing.MultiTapeTM.Copy.computesInTimeAndSpace` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L79))

> The copy machine outputs its input unchanged, in `input.length + 1` steps and zero space.

```lean
theorem computesInTimeAndSpace (input : List Symbol) :
    ComputesInTimeAndSpace copy input input (input.length + 1) 0
```

`Turing.MultiTapeTM.computableInTimeAndSpace_id` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L90))

> The identity function is computable in one step per input symbol and zero space.

```lean
public theorem computableInTimeAndSpace_id {enc : α ↪ List Bool} :
    ComputableInTimeAndSpace (id : α → α) enc enc
      (fun a => (enc a).length + 1) (fun _ => 0)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean)
