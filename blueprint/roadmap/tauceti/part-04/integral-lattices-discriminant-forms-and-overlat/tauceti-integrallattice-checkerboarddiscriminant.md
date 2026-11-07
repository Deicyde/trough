---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry
statement: formalized
---

# TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry

**The standard model is isometric to the discriminant quadratic module of an even-rank
checkerboard lattice**, by the identification carrying `(1, 0)` to the vector class and `(0, 1)`
to the spinor class.

This is the `Dₙ` row of the ADE table for even `n`: not only is the discriminant group `(ℤ/2)²`,
its quadratic form is the displayed one.

```lean
TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry (n : ℕ) [NeZero n] (hn : Even n) :
  (TauCeti.IntegralLattice.checkerboardStandardQuadraticModule n hn).Isometry
    ((TauCeti.IntegralLattice.checkerboardLattice n).discriminantQuadraticModule ⋯)
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeD/Basic.html#TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeD/Basic.html#TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry)
- [Source of `TauCeti.IntegralLattice.checkerboardDiscriminantQuadraticIsometry` in TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeD/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeD/Basic.lean#L1129)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/IntegralLattices/STATUS.md)
