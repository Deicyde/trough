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

- [Cauchy-Schwarz against a majorant](../../../linear-algebra/part-01/bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [The group `Int L` of inner automorphisms of a Lie algebra `L`](the-group-int-l-of-inner-automorphisms-of-a-lie.md)
- [The lattice form of Weyl's theorem](../../part-02/lie/part-01/the-lattice-form-of-weyls-theorem.md)
- [The multiplicity theorem](../../../ring-theory/part-02/semisimple/the-multiplicity-theorem.md)
- [The Weyl dimension formula (`TauCeti.finrank_eq_prod_coweightPairing_div`)](../../part-02/lie/part-02/the-weyl-dimension-formula-tauceti-finrank-eq-pr.md)
- [Weyl's complete reducibility theorem](../../part-02/lie/part-02/weyls-complete-reducibility-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity).

## Sources

- [Tau Ceti documentation: `TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Kostant.html#TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity)
- [Source of `TauCeti.SpinPolarizationData.kostantSpinRep_multiplicity` in TauCeti/RepresentationTheory/Spin/Kostant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Spin/Kostant.lean#L207)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RepresentationTheory/STATUS.md)
