---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.finite_genusClasses
statement: formalized
proof: formalized
---

# A positive definite genus contains finitely many classes

The lattices of the genus all
have the rank and determinant of `L`, so this is the finiteness of positive definite classes of
given rank and bounded determinant.

```lean
TauCeti.IntegralLattice.IsPosDef.finite_genusClasses.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef) : L.genusClasses.Finite
```

## Depends on

- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Proof depends on

- [Hermite's inequality for the minimum](hermites-inequality-for-the-minimum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.finite_genusClasses`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/ClassNumber.html#TauCeti.IntegralLattice.IsPosDef.finite_genusClasses).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.finite_genusClasses`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/ClassNumber.html#TauCeti.IntegralLattice.IsPosDef.finite_genusClasses)
- [Source of `TauCeti.IntegralLattice.IsPosDef.finite_genusClasses` in TauCeti/NumberTheory/IntegralLattice/ClassNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/IntegralLattice/ClassNumber.lean#L170)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
