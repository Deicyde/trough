---
declaration: theorem
origin: cited
lean: HomologicalComplex.finrank_homology_le_finrank_X
statement: formalized
proof: formalized
---

# The weak Morse inequality

In a homological complex of vector spaces, a homology group
has dimension at most that of the finite-dimensional term it is computed from.

```lean
HomologicalComplex.finrank_homology_le_finrank_X.{u_1, u_2, u_3} {k : Type u_1} [DivisionRing k]
  {ι : Type u_2} {c : ComplexShape ι} (K : HomologicalComplex (ModuleCat k) c) (i : ι)
  [Module.Finite k ↑(K.X i)] : Module.finrank k ↑(K.homology i) ≤ Module.finrank k ↑(K.X i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomologicalComplex.finrank_homology_le_finrank_X`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ModuleCat/Finrank.html#HomologicalComplex.finrank_homology_le_finrank_X).

## Sources

- [Tau Ceti documentation: `HomologicalComplex.finrank_homology_le_finrank_X`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/ModuleCat/Finrank.html#HomologicalComplex.finrank_homology_le_finrank_X)
- [Source of `HomologicalComplex.finrank_homology_le_finrank_X` in TauCeti/Algebra/Homology/ModuleCat/Finrank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/ModuleCat/Finrank.lean#L58)
