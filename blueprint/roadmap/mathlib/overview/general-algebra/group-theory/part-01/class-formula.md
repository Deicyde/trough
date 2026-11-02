---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MulAction.selfEquivSigmaOrbitsQuotientStabilizer
mathlib_file: Mathlib/GroupTheory/GroupAction/Quotient.lean
---

# Class formula

**Class formula**. This is a special case of
`MulAction.self_equiv_sigma_orbits_quotient_stabilizer'` with `φ = Quotient.out`.

```lean
MulAction.selfEquivSigmaOrbitsQuotientStabilizer.{u, v} (G : Type u) (X : Type v) [Group G]
  [MulAction G X] : X ≃ (ω : Quotient (MulAction.orbitRel G X)) × G ⧸ MulAction.stabilizer G ω.out
```

## Depends on

- [Quotient space](../../../../undergraduate/group-theory/basic-definitions/quotient-space.md)

## Sources

- [Mathlib documentation: `MulAction.selfEquivSigmaOrbitsQuotientStabilizer`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Quotient.html#MulAction.selfEquivSigmaOrbitsQuotientStabilizer)
- [Source of `MulAction.selfEquivSigmaOrbitsQuotientStabilizer` in Mathlib/GroupTheory/GroupAction/Quotient.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/GroupAction/Quotient.lean#L226)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L36)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L91)
