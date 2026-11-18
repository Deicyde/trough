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

- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.discriminantQuadraticModule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.html#TauCeti.IntegralLattice.discriminantQuadraticModule).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.discriminantQuadraticModule`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.html#TauCeti.IntegralLattice.discriminantQuadraticModule)
- [Source of `TauCeti.IntegralLattice.discriminantQuadraticModule` in TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Discriminant/Quadratic.lean#L181)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/IntegralLattices/STATUS.md)
