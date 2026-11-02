---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Combinatorics.exists_mono_homothetic_copy
mathlib_file: Mathlib/Combinatorics/HalesJewett.lean
---

# Van der Waerden theorem

A generalization of Van der Waerden's theorem: if `M` is a finitely colored commutative
monoid, and `S` is a finite subset, then there exists a monochromatic homothetic copy of `S`.

```lean
Combinatorics.exists_mono_homothetic_copy.{u_5, u_6} {M : Type u_5} {κ : Type u_6} [AddCommMonoid M]
  (S : Finset M) [Finite κ] (C : M → κ) : ∃ a > 0, ∃ b c, ∀ s ∈ S, C (a • s + b) = c
```

## Depends on

- [Array](../../data-structures/list-like-structures/array.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Proof depends on

- [Hales-Jewett theorem](hales-jewett-theorem.md)

## Sources

- [Mathlib documentation: `Combinatorics.exists_mono_homothetic_copy`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/HalesJewett.html#Combinatorics.exists_mono_homothetic_copy)
- [Source of `Combinatorics.exists_mono_homothetic_copy` in Mathlib/Combinatorics/HalesJewett.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/HalesJewett.lean#L458)
- [Mathlib overview: Combinatorics › Ramsey theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L534)
- [1000+ theorems list: Q764287](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L857)
- [1000+ theorems project: Q764287](https://1000-plus.github.io/?length=-1#Q764287)
- [Wikipedia: Van der Waerden's theorem](https://en.wikipedia.org/wiki/Van_der_Waerden's_theorem)
- [Wikidata: Q764287](https://www.wikidata.org/wiki/Q764287)
