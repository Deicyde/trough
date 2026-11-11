---
declaration: theorem
origin: cited
lean: TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity
statement: formalized
proof: formalized
---

# Kostant's multiplicity theorem for the spinor module

The spinor module of a polarization
of the Killing form is a direct sum of `2 ^ (l / 2)` copies of an irreducible Lie submodule of
dimension `2 ^ ((d - l) / 2)`, for `L` of dimension `d` and rank `l`.

```lean
TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity.{u, v} {K : Type u} [Field K] {L : Type v}
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [Invertible 2] [LieAlgebra.IsKilling K L]
  (P : TauCeti.SpinPolarizationData (TauCeti.LieAlgebra.killingQuadraticForm K L)) [CharZero K]
  [IsAlgClosed K] :
  ∃ S,
    LieModule.IsIrreducible K L ↥S ∧
      Module.finrank K ↥S = 2 ^ ((Module.finrank K L - LieAlgebra.rank K L) / 2) ∧
        Nonempty
          (ExteriorAlgebra K ↥P.W ≃ₗ⁅K,L⁆
            DirectSum (Fin (2 ^ (LieAlgebra.rank K L / 2))) fun x => ↥S)
```

## Depends on

- [The spinor module of Kostant's theorem](the-spinor-module-of-kostants-theorem.md)

## Proof depends on

- [Cauchy-Schwarz against a majorant](../../linear-algebra/bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The lattice form of Weyl's theorem](../../algebra/part-02/lie/part-01/the-lattice-form-of-weyls-theorem.md)
- [The multiplicity theorem](../../ring-theory/part-01/semisimple/the-multiplicity-theorem.md)
- [The Weyl dimension formula (`TauCeti.finrank_eq_prod_coweightPairing_div`)](../../algebra/part-02/lie/part-02/the-weyl-dimension-formula-tauceti-finrank-eq-pr.md)
- [Weyl's complete reducibility theorem](../../algebra/part-02/lie/part-02/weyls-complete-reducibility-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity)
- [Source of `TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity` in TauCeti/RepresentationTheory/Spin/Kostant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Spin/Kostant.lean#L207)
