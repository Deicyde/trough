---
declaration: theorem
origin: cited
lean: TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules
statement: formalized
proof: formalized
---

# TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules

The distinct simple coefficient spaces give an internal direct sum decomposition
of a linearly reductive coalgebra, over an arbitrary field.

```lean
TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules.{u, v} {k : Type u}
  [Field k] {C : Type v} [AddCommGroup C] [_root_.Module k C] [Coalgebra k C]
  (hC : TauCeti.Coalgebra.IsLinearlyReductive k C) : DirectSum.IsInternal fun P => ↑P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/LinearlyReductive/Decomposition.html#TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules).

## Sources

- [Tau Ceti documentation: `TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules`](https://taucetiproject.org/docs/TauCeti/Algebra/Coalgebra/Comodule/LinearlyReductive/Decomposition.html#TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules)
- [Source of `TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules` in TauCeti/Algebra/Coalgebra/Comodule/LinearlyReductive/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Coalgebra/Comodule/LinearlyReductive/Decomposition.lean#L54)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReductiveGroups/STATUS.md)
