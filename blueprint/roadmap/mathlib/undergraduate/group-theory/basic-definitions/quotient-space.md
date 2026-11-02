---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MulAction.orbitEquivQuotientStabilizer
mathlib_file: Mathlib/GroupTheory/GroupAction/Quotient.lean
---

# Quotient space

**Orbit-stabilizer theorem**.

```lean
MulAction.orbitEquivQuotientStabilizer.{u, v} (G : Type u) {X : Type v} [Group G] [MulAction G X]
  (b : X) : ↑(MulAction.orbit G b) ≃ G ⧸ MulAction.stabilizer G b
```

## Depends on

- [Orbit](orbit.md)
- [Stabilizer of a point](stabilizer-of-a-point.md)

## Sources

- [Mathlib documentation: `MulAction.orbitEquivQuotientStabilizer`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.orbitEquivQuotientStabilizer)
- [Source of `MulAction.orbitEquivQuotientStabilizer` in Mathlib/GroupTheory/GroupAction/Quotient.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/GroupAction/Quotient.lean#L167)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L90)
- [1000+ theorems list: Q288465](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L352)
- [1000+ theorems project: Q288465](https://1000-plus.github.io/?length=-1#Q288465)
- [Wikipedia: Orbit-stabilizer theorem](https://en.wikipedia.org/wiki/Orbit-stabilizer_theorem)
- [Wikidata: Q288465](https://www.wikidata.org/wiki/Q288465)
