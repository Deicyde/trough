---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: FractionalIdeal
mathlib_file: Mathlib/RingTheory/FractionalIdeal/Basic.lean
---

# Fractional ideal

The fractional ideals of a domain `R` are ideals of `R` divided by some `a ∈ R`.

More precisely, let `P` be a localization of `R` at some submonoid `S`,
then a fractional ideal `I ⊆ P` is an `R`-submodule of `P`,
such that there is an `a ∈ S` with `a I ⊆ R`.

```lean
FractionalIdeal.{u_1, u_2} {R : Type u_1} [CommRing R] (S : Submonoid R) (P : Type u_2) [CommRing P]
  [Algebra R P] : Type u_2
```

## Depends on

- [Associative algebra over a commutative ring](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Ring](../rings/ring.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `FractionalIdeal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/FractionalIdeal/Basic.html#FractionalIdeal)
- [Source of `FractionalIdeal` in Mathlib/RingTheory/FractionalIdeal/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/FractionalIdeal/Basic.lean#L76)
- [Mathlib overview: General algebra › Ideals and quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L80)
