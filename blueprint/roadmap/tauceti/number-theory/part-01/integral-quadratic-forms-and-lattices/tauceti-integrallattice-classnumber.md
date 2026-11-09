---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.classNumber
statement: formalized
---

# TauCeti.IntegralLattice.classNumber

The class number `h(L)`: the number of isometry classes in the genus of `L`. It is `0` when
the genus contains infinitely many classes.

```lean
TauCeti.IntegralLattice.classNumber.{u} {V : Type u} [AddCommGroup V] [_root_.Module ℚ V]
  (L : TauCeti.IntegralLattice V) : ℕ
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.classNumber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/ClassNumber.html#TauCeti.IntegralLattice.classNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.classNumber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/ClassNumber.html#TauCeti.IntegralLattice.classNumber)
- [Source of `TauCeti.IntegralLattice.classNumber` in TauCeti/NumberTheory/IntegralLattice/ClassNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/IntegralLattice/ClassNumber.lean#L142)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
