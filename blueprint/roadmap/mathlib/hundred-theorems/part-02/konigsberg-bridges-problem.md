---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Konigsberg.not_isEulerian
mathlib_file: Archive/Wiedijk100Theorems/Konigsberg.lean
---

# Königsberg Bridges Problem

The Königsberg graph is not Eulerian.

```lean
Konigsberg.not_isEulerian {u v : Konigsberg.Verts} (p : Konigsberg.graph.Walk u v)
  (h : p.IsEulerian) : False
```

## Depends on

- [List](../../overview/data-structures/list-like-structures/list.md)
- [Natural number](../../overview/general-algebra/numbers/natural-number.md)
- [Simple graph](../../overview/combinatorics/graph-theory/simple-graph.md)

## Proof depends on

- [Characteristic zero](../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Finite set](../../overview/data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `Konigsberg.not_isEulerian`](https://leanprover-community.github.io/mathlib4_docs/Archive/Wiedijk100Theorems/Konigsberg.html#Konigsberg.not_isEulerian)
- [Source of `Konigsberg.not_isEulerian` in Archive/Wiedijk100Theorems/Konigsberg.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Archive/Wiedijk100Theorems/Konigsberg.lean#L80)
- [Freek Wiedijk's 100 theorems, no. 54](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L279)
