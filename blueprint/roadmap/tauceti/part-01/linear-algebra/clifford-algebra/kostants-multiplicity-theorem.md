---
declaration: theorem
origin: cited
lean: CliffordAlgebra.kostant_multiplicity
statement: formalized
proof: formalized
---

# Kostant's multiplicity theorem

The Clifford algebra of the Killing form, under left
multiplication by the quadratic lift of the adjoint representation, is a direct sum of
`2 ^ ((d + l) / 2)` copies of an irreducible Lie submodule of dimension `2 ^ ((d - l) / 2)`, for `L`
of dimension `d` and rank `l`.

```lean
CliffordAlgebra.kostant_multiplicity.{u, v} {K : Type u} [Field K] [CharZero K] {L : Type v}
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [Invertible 2] [LieAlgebra.IsKilling K L]
  [IsAlgClosed K] :
  ∃ S,
    LieModule.IsIrreducible K L ↥S ∧
      Module.finrank K ↥S = 2 ^ ((Module.finrank K L - LieAlgebra.rank K L) / 2) ∧
        Nonempty
          (CliffordAlgebra (TauCeti.LieAlgebra.killingQuadraticForm K L) ≃ₗ⁅K,L⁆
            DirectSum (Fin (2 ^ ((Module.finrank K L + LieAlgebra.rank K L) / 2))) fun x => ↥S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy-Schwarz against a majorant](../bilinear-form/cauchy-schwarz-against-a-majorant.md)
- [Kostant's decomposition](kostants-decomposition.md)
- [The Weyl dimension formula (`TauCeti.finrank_eq_prod_coweightPairing_div`)](../../algebra/part-02/lie/part-02/the-weyl-dimension-formula-tauceti-finrank-eq-pr.md)
- [Weyl's complete reducibility theorem](../../algebra/part-02/lie/part-02/weyls-complete-reducibility-theorem.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.kostant_multiplicity`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.html#CliffordAlgebra.kostant_multiplicity).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.kostant_multiplicity`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.html#CliffordAlgebra.kostant_multiplicity)
- [Source of `CliffordAlgebra.kostant_multiplicity` in TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Quadratic/Lie/Isotypic.lean#L149)
