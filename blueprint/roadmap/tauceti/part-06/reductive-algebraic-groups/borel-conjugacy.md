---
declaration: theorem
origin: cited
lean: TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq
statement: formalized
proof: formalized
---

# Borel conjugacy

Any two Borel subgroups of a finite-type affine group over an
algebraically closed field are conjugate by a rational point. The ambient group need not
be smooth, reduced, or connected.

```lean
TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq.{u} {k : Type u} [Field k]
  [IsAlgClosed k] {H : TauCeti.FiniteTypeCommHopfAlgCat k} {I J : TauCeti.HopfIdeal k ↑H.obj}
  (hI : TauCeti.HopfIdeal.IsBorelOverAlgClosed k H I)
  (hJ : TauCeti.HopfIdeal.IsBorelOverAlgClosed k H J) : ∃ g, I.conjugate g = J
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.html#TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.html#TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq)
- [Source of `TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq` in TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.lean#L130)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
