# Noetherian module

`IsNoetherian R M` is the proposition that `M` is a Noetherian `R`-module,
implemented as the predicate that all `R`-submodules of `M` are finitely generated.

```lean
IsNoetherian.{u_1, u_2} (R : Type u_1) (M : Type u_2) [Semiring R] [AddCommMonoid M]
  [_root_.Module R M] : Prop
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Generating sets](../../../undergraduate/linear-algebra/fundamentals/generating-sets.md)

## Sources

- [Mathlib documentation: `IsNoetherian`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Noetherian/Defs.html#IsNoetherian)
- [Source of `IsNoetherian` in Mathlib/RingTheory/Noetherian/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/RingTheory/Noetherian/Defs.lean#L57)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L175)
