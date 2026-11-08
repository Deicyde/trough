---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_typeE₈RootLattice_of_isEven
statement: formalized
proof: formalized
---

# `E₈` is the unique even unimodular positive definite lattice of rank eight

```lean
TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_typeE₈RootLattice_of_isEven.{u} {V : Type u}
  [AddCommGroup V] [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} (hL : L.IsPosDef)
  (hU : L.IsUnimodular) (he : L.IsEven) (hn : Module.finrank ℤ ↥L.carrier = 8) :
  Nonempty (TauCeti.IntegralLattice.typeE₈RootLattice.Isometry L)
```

## Depends on

- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Proof depends on

- [The `E₈` root lattice is isometric to the spinor glue lattice `D₈⁺`](the-e8-root-lattice-is-isometric-to-the-spinor-g.md)
- [A positive definite lattice is `I_k` plus a lattice without vectors of norm one](a-positive-definite-lattice-is-i-k-plus-a-lattic.md)
- [Hermite's inequality for the minimum](../../number-theory/part-01/integral-quadratic-forms-and-lattices/hermites-inequality-for-the-minimum.md)
- [TauCeti.FiniteQuadraticModule](../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_typeE₈RootLattice_of_isEven`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.html#TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_typeE%E2%82%88RootLattice_of_isEven).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_typeE₈RootLattice_of_isEven`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.html#TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_typeE%E2%82%88RootLattice_of_isEven)
- [Source of `TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_typeE₈RootLattice_of_isEven` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.lean#L402)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/IntegralLattices/STATUS.md)
