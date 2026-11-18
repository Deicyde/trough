---
catalog: module
lean: Cslib.LTS.reverse, Cslib.LTS.reverse_tr, Cslib.LTS.reverse_reverse, Cslib.LTS.reverse_involutive, Cslib.LTS.Execution.reverse, Cslib.LTS.reverse_execution, Cslib.LTS.reverse_mTr, Cslib.LTS.reverse_canReach, Cslib.LTS.reverse_unlabelledTr, Cslib.LTS.reverse_image, Cslib.LTS.mem_reverse_image, Cslib.LTS.reverse_imageMultistep, Cslib.LTS.mem_reverse_imageMultistep, Cslib.LTS.reverse_hasOutLabel, Cslib.LTS.reverse_boundedUpTo
statement: formalized
proof: formalized
---

# Reverse operation for LTS

`Cslib.Foundations.Semantics.LTS.Reverse`, in [Cslib/Foundations/Semantics/LTS/Reverse.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean), by Vignesh Karri.

> This file defines `Cslib.LTS.reverse`, which reverses every transition of an LTS.
> `reverse_canReach`, `reverse_unlabelledTr`, `reverse_image`, `reverse_imageMultistep`,
> `reverse_hasOutLabel` and `reverse_boundedUpTo` each state a property about `lts.reverse` in
> terms of `lts`.
>
> `reverse_mTr` states that the multistep transitions of `lts.reverse` are the reversed
> multistep transitions of `lts`. `reverse_execution` is the same statement for
> executions, and is derived from `Execution.reverse`.

`Cslib.LTS.reverse` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L35))

> Constructs an LTS by reversing the transitions of an existing LTS.

```lean
def reverse (lts : LTS State Label) : LTS State Label
```

`Cslib.LTS.reverse_tr` (theorem, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L40))

> The transitions of `lts.reverse` are exactly the reversed transitions of `lts`.

```lean
theorem reverse_tr {lts : LTS State Label} :
    (lts.reverse).Tr s μ s' ↔ lts.Tr s' μ s
```

`Cslib.LTS.reverse_reverse` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L45))

> Reversing an LTS twice gives back the original LTS.

```lean
theorem reverse_reverse (lts : LTS State Label) : lts.reverse.reverse = lts
```

`Cslib.LTS.reverse_involutive` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L48))

> Reversal of an LTS is an involution.

```lean
theorem reverse_involutive : Function.Involutive (reverse (Label := Label) (State := State))
```

`Cslib.LTS.Execution.reverse` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L51))

```lean
theorem Execution.reverse {lts : LTS State Label} (h : lts.Execution s μs s' ss) :
    lts.reverse.Execution s' μs.reverse s ss.reverse
```

`Cslib.LTS.reverse_execution` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L61))

> An execution of `lts.reverse` is an execution of `lts` with the labels, states
> and endpoints reversed.

```lean
theorem reverse_execution {lts : LTS State Label} :
    lts.reverse.Execution s μs s' ss ↔ lts.Execution s' μs.reverse s ss.reverse
```

`Cslib.LTS.reverse_mTr` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L68))

> The multistep transitions of `lts.reverse` are exactly the reversed multistep transitions of
> `lts`.

```lean
theorem reverse_mTr {lts : LTS State Label} :
    lts.reverse.MTr s' μs s ↔ lts.MTr s μs.reverse s'
```

`Cslib.LTS.reverse_canReach` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L75))

> `lts.reverse` can reach `s'` from `s` iff `lts` can reach `s` from `s'`.

```lean
theorem reverse_canReach {lts : LTS State Label} :
    lts.reverse.CanReach s s' ↔ lts.CanReach s' s
```

`Cslib.LTS.reverse_unlabelledTr` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L82))

> The unlabelled transitions of `lts.reverse` are those of `lts` with the endpoints swapped.

```lean
theorem reverse_unlabelledTr {lts : LTS State Label} :
    lts.reverse.UnlabelledTr s s' ↔ lts.UnlabelledTr s' s
```

`Cslib.LTS.reverse_image` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L87))

> The `μ`-image of a state in `lts.reverse` is its `μ`-preimage in `lts`.

```lean
theorem reverse_image {lts : LTS State Label} :
    lts.reverse.image s μ = {s' | lts.Tr s' μ s}
```

`Cslib.LTS.mem_reverse_image` (theorem, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L91))

> Membership form of `reverse_image`.

```lean
theorem mem_reverse_image {lts : LTS State Label} :
    s' ∈ lts.reverse.image s μ ↔ s ∈ lts.image s' μ
```

`Cslib.LTS.reverse_imageMultistep` (theorem, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L96))

> The `μs`-image of a state in `lts.reverse` is its `μs.reverse`-preimage in `lts`.

```lean
theorem reverse_imageMultistep {lts : LTS State Label} :
    lts.reverse.imageMultistep s μs = {s' | lts.MTr s' μs.reverse s}
```

`Cslib.LTS.mem_reverse_imageMultistep` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L101))

> Membership version of `reverse_imageMultistep`.

```lean
theorem mem_reverse_imageMultistep {lts : LTS State Label} :
    s' ∈ lts.reverse.imageMultistep s μs ↔ s ∈ lts.imageMultistep s' μs.reverse
```

`Cslib.LTS.reverse_hasOutLabel` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L107))

> A state has `μ` as an outgoing label in `lts.reverse` iff it has `μ` as an incoming
> label in `lts`.

```lean
theorem reverse_hasOutLabel {lts : LTS State Label} :
    lts.reverse.HasOutLabel s μ ↔ ∃ s', lts.Tr s' μ s
```

`Cslib.LTS.reverse_boundedUpTo` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean#L112))

> `lts.reverse` is bounded up to `n` iff `lts` is.

```lean
theorem reverse_boundedUpTo {lts : LTS State Label} {n : ℕ} :
    lts.reverse.BoundedUpTo n ↔ lts.BoundedUpTo n
```

## Depends on

- [Finite executions of LTS](execution.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Reverse.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Reverse.lean)
