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
- [Source of `TauCeti.IntegralLattice.discriminantQuadraticModule` in TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.lean#L182)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/IntegralLattices/STATUS.md)
