---
declaration: structure
origin: cited
mathlib: true
mathlib_declaration: ModuleCat
mathlib_file: Mathlib/Algebra/Category/ModuleCat/Basic.lean
---

# The category of modules over a ring

The category of R-modules and their morphisms.

Note that in the case of `R = ℤ`, we cannot
impose here that the `ℤ`-multiplication field from the module structure is defeq to the one coming
from the `isAddCommGroup` structure \(contrary to what we do for all module structures in
mathlib\), which creates some difficulties down the road.

```lean
ModuleCat.{v, u} (R : Type u) [Ring R] : Type (max u (v + 1))
```

## Depends on

- [Integer](../../general-algebra/numbers/integer.md)
- [Module](module.md)
- [Ring](../../general-algebra/rings/ring.md)

## Sources

- [Mathlib documentation: `ModuleCat`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/ModuleCat/Basic.html#ModuleCat)
- [Source of `ModuleCat` in Mathlib/Algebra/Category/ModuleCat/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Category/ModuleCat/Basic.lean#L53)
- [Mathlib overview: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L171)
