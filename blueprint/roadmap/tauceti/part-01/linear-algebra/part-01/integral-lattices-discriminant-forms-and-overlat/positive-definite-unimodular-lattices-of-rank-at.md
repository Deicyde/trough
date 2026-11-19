---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_of_isUnimodular_of_finrank_le_nine
statement: formalized
proof: formalized
---

# Positive definite unimodular lattices of rank at most nine

Such a lattice is the
standard lattice `Iₙ`, the root lattice `E₈`, or `I₁ ⊕ E₈`.

```lean
TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_of_isUnimodular_of_finrank_le_nine.{u}
  {V : Type u} [AddCommGroup V] [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V}
  (hL : L.IsPosDef) (hU : L.IsUnimodular) (hn : Module.finrank ℤ ↥L.carrier ≤ 9) :
  Nonempty ((TauCeti.IntegralLattice.unitLattice (Fin (Module.finrank ℤ ↥L.carrier))).Isometry L) ∨
    Nonempty (TauCeti.IntegralLattice.typeE₈RootLattice.Isometry L) ∨
      Nonempty
        (((TauCeti.IntegralLattice.unitLattice (Fin 1)).orthogonalSum
              TauCeti.IntegralLattice.typeE₈RootLattice).Isometry
          L)
```

## Depends on

- [TauCeti.IntegralLattice](tauceti-integrallattice.md)

## Proof depends on

- [The `E₈` root lattice is isometric to the spinor glue lattice `D₈⁺`](the-e8-root-lattice-is-isometric-to-the-spinor-g.md)
- [Hermite's inequality for the minimum](../integral-lattice/hermites-inequality-for-the-minimum.md)
- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_of_isUnimodular_of_finrank_le_nine`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.html#TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_of_isUnimodular_of_finrank_le_nine).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_of_isUnimodular_of_finrank_le_nine`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.html#TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_of_isUnimodular_of_finrank_le_nine)
- [Source of `TauCeti.IntegralLattice.IsPosDef.nonempty_isometry_of_isUnimodular_of_finrank_le_nine` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/PosDef/SmallRankUnimodular.lean#L374)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/IntegralLattices/STATUS.md)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/IntegralLattices/STATUS.md)
