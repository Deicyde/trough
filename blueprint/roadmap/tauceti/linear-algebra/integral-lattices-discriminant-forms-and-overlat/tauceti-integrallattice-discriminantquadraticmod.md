---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.discriminantQuadraticModule
statement: formalized
---

# TauCeti.IntegralLattice.discriminantQuadraticModule

The discriminant group of an even nondegenerate integral lattice, equipped with its canonical
half-norm quadratic map and discriminant polar pairing.

```lean
TauCeti.IntegralLattice.discriminantQuadraticModule.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℚ V] (L : TauCeti.IntegralLattice V) [L.IsNondegenerate] (hL : L.IsEven) :
  TauCeti.FiniteQuadraticModule
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.discriminantQuadraticModule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.html#TauCeti.IntegralLattice.discriminantQuadraticModule).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.discriminantQuadraticModule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.html#TauCeti.IntegralLattice.discriminantQuadraticModule)
- [Source of `TauCeti.IntegralLattice.discriminantQuadraticModule` in TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.lean#L182)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/IntegralLattices/STATUS.md)
