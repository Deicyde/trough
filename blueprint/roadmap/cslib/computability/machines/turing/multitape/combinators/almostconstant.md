---
catalog: module
lean: Turing.MultiTapeTM.almostConstTime, Turing.MultiTapeTM.computableInTimeAndSpace_almostConstTime, Turing.MultiTapeTM.computableInTimeAndSpace_of_exists_finite_ne, Turing.MultiTapeTM.computableInTimeAndSpace_of_const, Turing.MultiTapeTM.finiteFunTime, Turing.MultiTapeTM.computableInTimeAndSpace_finiteFunTime, Turing.MultiTapeTM.computableInTimeAndSpace_of_finite
statement: formalized
proof: formalized
---

# Complexity of Almost Constant Functions

`Cslib.Computability.Machines.Turing.MultiTape.Combinators.AlmostConstant`, in [Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean), by Christian Reitwiessner.

> A function `f : α → β` that is constant except for a finite number of arguments is computable in
> constant time and zero space: the machine reads the encoded input while remembering the prefix it
> has seen so far. After a finite number of steps it either reaches the end of the input or a point
> where the prefix cannot be extended to the encoding of one of the finitely many exceptions. In both
> cases, it emits the corresponding output one symbol at a time.
>
> This result also holds for functions whose domain is already finite.
>
> ## Main Results
>
> * `encodedComputableInTimeAndSpace_of_finite`: Every function on a finite type is computable in
>     constant time and zero space, relative to any encoding.
> * `encodedComputableInTimeAndSpace_of_exists_finite_ne`: Every function that is constant except
>     for a finite number of arguments is computable in constant time and zero space, relative to any
>     encoding.
> * `encodedComputableInTimeAndSpace_of_const`: Every constant function is computable in constant
>     time and zero space, relative to any encoding.
> * `encodedComputableInTimeAndSpace_almostConstTime` and
>     `encodedComputableInTimeAndSpace_finiteFunTime`: The same with explicit time bounds.

> ## The machine computing a function that is constant outside a finite set
>
> The machine `almostConstTM encIn encOut f S out` computes `f`, provided that the encoded output
> of `f` is the fixed Boolean string `out` outside of the finite set `S`.

`Turing.MultiTapeTM.almostConstTime` (definition, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L252))

> A constant time bound for the machine `almostConstTM`.

```lean
public def almostConstTime (encIn : α ↪ List Bool) (encOut : β ↪ List Bool) (f : α → β)
    (S : Finset α) (out : List Bool) : ℕ
```

`Turing.MultiTapeTM.computableInTimeAndSpace_almostConstTime` (theorem, [line 346](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L346))

> Every function whose encoded output is constant outside of a finite set is computable in time
> `almostConstTime` and zero space.

```lean
public theorem computableInTimeAndSpace_almostConstTime
    (f : α → β) (S : Finset α) (out : List Bool) (h : ∀ a ∉ S, encOut (f a) = out) :
    ComputableInTimeAndSpace f encIn encOut
      (fun _ => almostConstTime encIn encOut f S out) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_exists_finite_ne` (theorem, [line 354](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L354))

> Every almost constant function is computable in constant time and zero space.

```lean
public theorem computableInTimeAndSpace_of_exists_finite_ne
    {f : α → β} (h : ∃ b : β, {a : α | f a ≠ b}.Finite) :
    ∃ c, ComputableInTimeAndSpace f encIn encOut (fun _ => c) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_const` (theorem, [line 364](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L364))

> Every constant function is computable in constant time and zero space.

```lean
public theorem computableInTimeAndSpace_of_const {α β : Type*}
    {encIn : α ↪ List Bool} {encOut : β ↪ List Bool} (b : β) :
    ∃ c, ComputableInTimeAndSpace (Function.const α b) encIn encOut
      (fun _ => c) (fun _ => 0)
```

`Turing.MultiTapeTM.finiteFunTime` (definition, [line 372](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L372))

> A constant time bound for functions on a finite type.

```lean
public noncomputable def finiteFunTime {α β : Type*} [Finite α] (encIn : α ↪ List Bool)
    (encOut : β ↪ List Bool) (f : α → β) : ℕ
```

`Turing.MultiTapeTM.computableInTimeAndSpace_finiteFunTime` (theorem, [line 378](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L378))

> Every function on a finite type is computable in time `finiteFunTime` and zero space.

```lean
public theorem computableInTimeAndSpace_finiteFunTime {α β : Type*} [Finite α]
    {encIn : α ↪ List Bool} {encOut : β ↪ List Bool} (f : α → β) :
    ComputableInTimeAndSpace f encIn encOut
      (fun _ => finiteFunTime encIn encOut f) (fun _ => 0)
```

`Turing.MultiTapeTM.computableInTimeAndSpace_of_finite` (theorem, [line 386](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean#L386))

> Every function on a finite type is computable in constant time and zero space.

```lean
public theorem computableInTimeAndSpace_of_finite {α β : Type*} [Finite α]
    {encIn : α ↪ List Bool} {encOut : β ↪ List Bool}
    (f : α → β) :
    ∃ c, ComputableInTimeAndSpace f encIn encOut (fun _ => c) (fun _ => 0)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](../deterministic.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Combinators/AlmostConstant.lean)
