---
declaration: abbrev
origin: cited
mathlib: true
mathlib_declaration: IsNoetherianRing
mathlib_file: Mathlib/RingTheory/Noetherian/Defs.lean
---

# Noetherian ring

A (semi)ring is Noetherian if it is Noetherian as a module over itself,
i.e. all its ideals are finitely generated.

```lean
IsNoetherianRing.{u_1} (R : Type u_1) [Semiring R] : Prop
```

## Depends on

- [Noetherian module](../../linear-algebra/fundamentals/noetherian-module.md)

## Sources

- [Mathlib documentation: `IsNoetherianRing`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Noetherian/Defs.html#IsNoetherianRing)
- [Source of `IsNoetherianRing` in Mathlib/RingTheory/Noetherian/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Noetherian/Defs.lean#L188)
- [Mathlib overview: General algebra › Rings](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L71)
