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
- [Source of `TauCeti.Coalgebra.IsLinearlyReductive.isInternal_simpleCoefficientSubmodules` in TauCeti/Algebra/Coalgebra/Comodule/LinearlyReductive/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Coalgebra/Comodule/LinearlyReductive/Decomposition.lean#L54)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroups/STATUS.md)
