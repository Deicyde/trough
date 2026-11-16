# Sequence

`Seq α` is the type of possibly infinite lists (referred here as sequences).
It is encoded as an infinite stream of options such that if `f n = none`, then
`f m = none` for all `m ≥ n`.

```lean
Stream'.Seq.{u} (α : Type u) : Type u
```

## Depends on

- [Stream](stream.md)

## Sources

- [Mathlib documentation: `Stream'.Seq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Seq/Defs.html#Stream'.Seq)
- [Source of `Stream'.Seq` in Mathlib/Data/Seq/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Data/Seq/Defs.lean#L61)
- [Mathlib overview: Data structures › List-like structures](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L575)
