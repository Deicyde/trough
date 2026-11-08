---
declaration: theorem
origin: cited
lean: TauCeti.robinsonSchensted_injective
statement: formalized
proof: formalized
---

# The Robinson--Schensted correspondence is injective

a word is determined by its
insertion tableau and its recording word.

```lean
TauCeti.robinsonSchensted_injective.{u_1} {α : Type u_1} [LinearOrder α] :
  Function.Injective TauCeti.robinsonSchensted
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.robinsonSchensted_injective`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/RobinsonSchensted.html#TauCeti.robinsonSchensted_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.robinsonSchensted_injective`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/RobinsonSchensted.html#TauCeti.robinsonSchensted_injective)
- [Source of `TauCeti.robinsonSchensted_injective` in TauCeti/Combinatorics/Young/RobinsonSchensted.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Young/RobinsonSchensted.lean#L218)
