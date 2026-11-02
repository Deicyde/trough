---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Combinatorics.Line.exists_mono_in_high_dimension
mathlib_file: Mathlib/Combinatorics/HalesJewett.lean
---

# Hales-Jewett theorem

The **Hales-Jewett theorem**: For any finite types `α` and `κ`, there exists a finite type `ι`
such that whenever the hypercube `ι → α` is `κ`-colored, there is a monochromatic combinatorial
line.

```lean
Combinatorics.Line.exists_mono_in_high_dimension.{u, v} (α : Type u) [Finite α] (κ : Type v)
  [Finite κ] : ∃ ι x, ∀ (C : (ι → α) → κ), ∃ l, Combinatorics.Line.IsMono C l
```

## Depends on

- [Finite set](../../data-structures/sets/finite-set.md)
- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Set](../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Combinatorics.Line.exists_mono_in_high_dimension`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/HalesJewett.html#Combinatorics.Line.exists_mono_in_high_dimension)
- [Source of `Combinatorics.Line.exists_mono_in_high_dimension` in Mathlib/Combinatorics/HalesJewett.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/HalesJewett.lean#L446)
- [Mathlib overview: Combinatorics › Ramsey theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L535)
- [1000+ theorems list: Q1032886](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L1204)
- [1000+ theorems project: Q1032886](https://1000-plus.github.io/all.html?length=-1#Q1032886)
- [Wikipedia: Hales–Jewett theorem](https://en.wikipedia.org/wiki/Hales%E2%80%93Jewett_theorem)
- [Wikidata: Q1032886](https://www.wikidata.org/wiki/Q1032886)
