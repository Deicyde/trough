---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.isCompactOperator_inclusion
statement: formalized
proof: formalized
---

# Rellich's theorem on the circle

the inclusion `H^s → H^t` is a compact operator for
`t < s` when `E` is finite-dimensional.

```lean
TauCeti.CircleSobolev.isCompactOperator_inclusion.{u_1} {s t : ℝ} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] (h : t < s) :
  IsCompactOperator ⇑(TauCeti.CircleSobolev.inclusion ⋯)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.isCompactOperator_inclusion`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.isCompactOperator_inclusion).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.isCompactOperator_inclusion`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Basic.html#TauCeti.CircleSobolev.isCompactOperator_inclusion)
- [Source of `TauCeti.CircleSobolev.isCompactOperator_inclusion` in TauCeti/Analysis/Sobolev/Circle/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Circle/Basic.lean#L709)
