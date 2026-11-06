# Cauchy-Davenport theorem

The **Cauchy-Davenport Theorem**. If `s`, `t` are nonempty sets in `ℤ/pℤ`, then the size of
`s + t` is lower-bounded by `|s| + |t| - 1`, unless this quantity is greater than `p`.

```lean
ZMod.cauchy_davenport {p : ℕ} (hp : Nat.Prime p) {s t : Finset (ZMod p)} (hs : s.Nonempty)
  (ht : t.Nonempty) : min p (s.card + t.card - 1) ≤ (s + t).card
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Integer](../../general-algebra/numbers/integer.md)
- [Irreducible element](../../general-algebra/divisibility-in-integral-domains/irreducible-element.md)

## Proof depends on

- [Cardinal](../../logic-and-computation/set-theory/cardinals/cardinal.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Periodic points](../../dynamics/general-theory/periodic-points.md)
- [Ring morphism](../../general-algebra/rings/ring-morphism.md)

## Sources

- [Mathlib documentation: `ZMod.cauchy_davenport`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/CauchyDavenport.html#ZMod.cauchy_davenport)
- [Source of `ZMod.cauchy_davenport` in Mathlib/Combinatorics/Additive/CauchyDavenport.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/CauchyDavenport.lean#L196)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L550)
