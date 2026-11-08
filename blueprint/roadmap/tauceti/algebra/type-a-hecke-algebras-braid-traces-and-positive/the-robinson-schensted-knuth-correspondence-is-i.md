---
declaration: theorem
origin: cited
lean: TauCeti.robinsonSchenstedKnuth_injOn
statement: formalized
proof: formalized
---

# The Robinson--Schensted--Knuth correspondence is injective on two-line arrays

a
two-line array is determined by its insertion and recording tableaux.

```lean
TauCeti.robinsonSchenstedKnuth_injOn.{u_1, u_2} {α : Type u_1} {β : Type u_2} [LinearOrder β]
  [LinearOrder α] : Set.InjOn TauCeti.robinsonSchenstedKnuth {ws | (List.map (⇑toLex) ws).SortedLE}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.robinsonSchenstedKnuth_injOn`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/KnuthCorrespondence.html#TauCeti.robinsonSchenstedKnuth_injOn).

## Sources

- [Tau Ceti documentation: `TauCeti.robinsonSchenstedKnuth_injOn`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/KnuthCorrespondence.html#TauCeti.robinsonSchenstedKnuth_injOn)
- [Source of `TauCeti.robinsonSchenstedKnuth_injOn` in TauCeti/Combinatorics/Young/KnuthCorrespondence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Young/KnuthCorrespondence.lean#L262)
