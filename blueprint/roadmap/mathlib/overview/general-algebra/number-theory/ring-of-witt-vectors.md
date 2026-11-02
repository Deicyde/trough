---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: WittVector
mathlib_file: Mathlib/RingTheory/WittVector/Defs.lean
---

# Ring of Witt vectors

`WittVector p R` is the ring of `p`-typical Witt vectors over the commutative ring `R`,
where `p` is a prime number.

If `p` is invertible in `R`, this ring is isomorphic to `ℕ → R` (the product of `ℕ` copies of `R`).
If `R` is a ring of characteristic `p`, then `WittVector p R` is a ring of characteristic `0`.
The canonical example is `WittVector p (ZMod p)`,
which is isomorphic to the `p`-adic integers `ℤ_[p]`.

```lean
WittVector.{u_1} (p : ℕ) (R : Type u_1) : Type u_1
```

## Depends on

- [Natural number](../numbers/natural-number.md)

## Sources

- [Mathlib documentation: `WittVector`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/WittVector/Defs.html#WittVector)
- [Source of `WittVector` in Mathlib/RingTheory/WittVector/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/WittVector/Defs.lean#L45)
- [Mathlib overview: General algebra › Number theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L151)
