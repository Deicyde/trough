# Smn theorem

The $S_n^m$ theorem: There is a computable function, namely `Nat.Partrec.Code.curry`, that takes a
program and a ℕ `n`, and returns a new program using `n` as the first argument.

```lean
Nat.Partrec.Code.smn :
  ∃ f, Computable₂ f ∧ ∀ (c : Nat.Partrec.Code) (n x : ℕ), (f c n).eval x = c.eval (Nat.pair n x)
```

## Depends on

- [In terms of general recursive functions](../../overview/logic-and-computation/computability/computable-function/in-terms-of-general-recursive-functions.md)

## Proof depends on

- [Primitive recursive function](../../overview/logic-and-computation/computability/primitive-recursive-function.md)

## Sources

- [Mathlib documentation: `Nat.Partrec.Code.smn`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Computability/PartrecCode.html#Nat.Partrec.Code.smn)
- [Source of `Nat.Partrec.Code.smn` in Mathlib/Computability/PartrecCode.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Computability/PartrecCode.lean#L520)
- [1000+ theorems list: Q1766814](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1885)
- [1000+ theorems project: Q1766814](https://1000-plus.github.io/all.html?length=-1#Q1766814)
- [Wikipedia: Smn theorem](https://en.wikipedia.org/wiki/Smn_theorem)
- [Wikidata: Q1766814](https://www.wikidata.org/wiki/Q1766814)
