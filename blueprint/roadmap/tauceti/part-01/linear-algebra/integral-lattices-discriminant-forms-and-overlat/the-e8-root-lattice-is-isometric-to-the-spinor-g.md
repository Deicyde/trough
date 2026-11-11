---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.typeE₈IsometryD8Plus
statement: formalized
---

# The `E₈` root lattice is isometric to the spinor glue lattice `D₈⁺`

The underlying rational equivalence sends the `i`-th simple root of `E₈` to the `i`-th vector of
Bourbaki's plate VII in Conway--Sloane coordinates.

```lean
TauCeti.IntegralLattice.typeE₈IsometryD8Plus :
  TauCeti.IntegralLattice.typeE₈RootLattice.Isometry
    (TauCeti.IntegralLattice.checkerboardPlusLattice 8
      TauCeti.IntegralLattice.typeE₈IsometryD8Plus._proof_1)
```

## Depends on

- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Proof depends on

- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.typeE₈IsometryD8Plus`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/D8Plus/Isometry.html#TauCeti.IntegralLattice.typeE%E2%82%88IsometryD8Plus).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.typeE₈IsometryD8Plus`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/D8Plus/Isometry.html#TauCeti.IntegralLattice.typeE%E2%82%88IsometryD8Plus)
- [Source of `TauCeti.IntegralLattice.typeE₈IsometryD8Plus` in TauCeti/LinearAlgebra/IntegralLattice/RootLattice/D8Plus/Isometry.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/D8Plus/Isometry.lean#L288)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/IntegralLattices/STATUS.md)
