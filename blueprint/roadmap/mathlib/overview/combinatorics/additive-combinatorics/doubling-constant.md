# Doubling constant

The doubling constant `σ[A, B]` of two finsets `A` and `B` in a group is `|A + B| / |A|`.

The notation `σ[A, B]` is available in scope `Combinatorics.Additive`.

```lean
Finset.addConst.{u_1} {G : Type u_1} [AddGroup G] [DecidableEq G] (A B : Finset G) : ℚ≥0
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Rational number](../../general-algebra/numbers/rational-number.md)

## Sources

- [Mathlib documentation: `Finset.addConst`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/DoublingConst.html#Finset.addConst)
- [Source of `Finset.addConst` in Mathlib/Combinatorics/Additive/DoublingConst.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/DoublingConst.lean#L33)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L544)
