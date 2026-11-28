---
catalog: module
lean: Turing.MultiTapeTM.computableInTimeAndSpace_id
statement: formalized
proof: formalized
---

# Complexity of the identity function

`Cslib.Computability.Machines.Turing.MultiTape.Combinators.Id`, in [Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean), by Christian Reitwiessner.

> A machine with a single state and no work tapes scans the input from left to right, copying each
> symbol to the output tape, and halts on the blank at the right end of the input. On input `w` it
> outputs `w` after `w.length + 1` steps, and having no work tapes it uses zero space.
>
> ## Main results
>
> * `Turing.MultiTapeTM.computableInTimeAndSpace_id`: the identity is computable in one step per
>   input symbol and zero space.

`Turing.MultiTapeTM.computableInTimeAndSpace_id` (theorem, [line 90](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean#L90))

> The identity function is computable in one step per input symbol and zero space.

```lean
public theorem computableInTimeAndSpace_id {enc : α ↪ List Bool} :
    ComputableInTimeAndSpace (id : α → α) enc enc
      (fun a => (enc a).length + 1) (fun _ => 0)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Id.lean)
- [Declaration ledger](../../../../../../../sources/cslib/Cslib.Computability.Machines.Turing.MultiTape.Combinators.Id.json)
