# Weak sequence

Weak sequences.

While the `Seq` structure allows for lists which may not be finite,
a weak sequence also allows the computation of each element to
involve an indeterminate amount of computation, including possibly
an infinite loop. This is represented as a regular `Seq` interspersed
with `none` elements to indicate that computation is ongoing.

This model is appropriate for Haskell style lazy lists, and is closed
under most interesting computation patterns on infinite lists,
but conversely it is difficult to extract elements from it.

```lean
Stream'.WSeq.{u_1} (α : Type u_1) : Type u_1
```

## Depends on

- [Sequence](sequence.md)

## Sources

- [Mathlib documentation: `Stream'.WSeq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/WSeq/Basic.html#Stream'.WSeq)
- [Source of `Stream'.WSeq` in Mathlib/Data/WSeq/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/WSeq/Basic.lean#L25)
- [Mathlib overview: Data structures › List-like structures](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L576)
