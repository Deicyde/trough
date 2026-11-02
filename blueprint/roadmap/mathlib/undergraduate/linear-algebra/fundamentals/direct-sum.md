---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: DirectSum.IsInternal
mathlib_file: Mathlib/Algebra/DirectSum/Basic.lean
---

# Direct sum

The `DirectSum` formed by a collection of additive submonoids (or subgroups, or submodules) of
`M` is said to be internal if the canonical map `(⨁ i, A i) →+ M` is bijective.

For the alternate statement in terms of independence and spanning, see
`DirectSum.subgroup_isInternal_iff_iSupIndep_and_supr_eq_top` and
`DirectSum.isInternal_submodule_iff_iSupIndep_and_iSup_eq_top`.

```lean
DirectSum.IsInternal.{v, u_1, u_2} {ι : Type v} {M : Type u_1} {S : Type u_2} [DecidableEq ι]
  [AddCommMonoid M] [SetLike S M] [AddSubmonoidClass S M] (A : ι → S) : Prop
```

## Depends on

- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Module](../../../overview/linear-algebra/fundamentals/module.md)
- [Set](../../../overview/data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `DirectSum.IsInternal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/DirectSum/Basic.html#DirectSum.IsInternal)
- [Source of `DirectSum.IsInternal` in Mathlib/Algebra/DirectSum/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/DirectSum/Basic.lean#L434)
- [Mathlib undergraduate list: Linear algebra › Fundamentals](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L12)
