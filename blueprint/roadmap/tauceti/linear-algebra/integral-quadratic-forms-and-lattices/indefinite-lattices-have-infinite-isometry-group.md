---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.infinite_isometry_of_isIndefinite
statement: formalized
proof: formalized
---

# Indefinite lattices have infinite isometry groups

A nondegenerate indefinite integral
lattice of rank at least three has infinitely many isometries.

```lean
TauCeti.IntegralLattice.infinite_isometry_of_isIndefinite.{u_1} {V : Type u_1} [AddCommGroup V]
  [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} [L.IsNondegenerate]
  (hrank : 3 ≤ Module.finrank ℤ ↥L.carrier) (hL : L.IsIndefinite) : Infinite (L.Isometry L)
```

## Depends on

- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.infinite_isometry_of_isIndefinite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/IndefiniteIsometry.html#TauCeti.IntegralLattice.infinite_isometry_of_isIndefinite).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.infinite_isometry_of_isIndefinite`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/IndefiniteIsometry.html#TauCeti.IntegralLattice.infinite_isometry_of_isIndefinite)
- [Source of `TauCeti.IntegralLattice.infinite_isometry_of_isIndefinite` in TauCeti/NumberTheory/IntegralLattice/IndefiniteIsometry.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/IntegralLattice/IndefiniteIsometry.lean#L169)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
