---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.nonempty_isometry_orthogonalSum_hyperbolicPlane_e8PowLattice
statement: formalized
proof: formalized
---

# `E₈ ⊕ E₈ ⊕ U ≅ D₁₆⁺ ⊕ U`

Adding the hyperbolic plane `U` makes the two non-isometric even
unimodular lattices of rank sixteen isometric.

```lean
TauCeti.IntegralLattice.nonempty_isometry_orthogonalSum_hyperbolicPlane_e8PowLattice :
  Nonempty
    (((TauCeti.IntegralLattice.e8PowLattice 2).orthogonalSum
          TauCeti.IntegralLattice.hyperbolicPlane).Isometry
      ((TauCeti.IntegralLattice.checkerboardPlusLattice (8 * 2) ⋯).orthogonalSum
        TauCeti.IntegralLattice.hyperbolicPlane))
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Proof depends on

- [TauCeti.FiniteQuadraticModule](tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.nonempty_isometry_orthogonalSum_hyperbolicPlane_e8PowLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/Cancellation.html#TauCeti.IntegralLattice.nonempty_isometry_orthogonalSum_hyperbolicPlane_e8PowLattice).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.nonempty_isometry_orthogonalSum_hyperbolicPlane_e8PowLattice`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/Cancellation.html#TauCeti.IntegralLattice.nonempty_isometry_orthogonalSum_hyperbolicPlane_e8PowLattice)
- [Source of `TauCeti.IntegralLattice.nonempty_isometry_orthogonalSum_hyperbolicPlane_e8PowLattice` in TauCeti/NumberTheory/IntegralLattice/Cancellation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/IntegralLattice/Cancellation.lean#L309)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
