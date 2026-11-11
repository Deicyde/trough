---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.isGroundState_iff_exists_inner_gnsHamiltonian_nonneg
statement: formalized
proof: formalized
---

# Ground states are the invariant states with nonnegative GNS Hamiltonian

A state `ω` is a
ground state of `α` exactly when it is `α`-invariant and its GNS Hamiltonian `H` satisfies
`0 ≤ ⟪ξ, H ξ⟫` on its domain.

```lean
TauCeti.CStarAction.isGroundState_iff_exists_inner_gnsHamiltonian_nonneg.{u_1} {A : Type u_1}
  [NonUnitalCStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
  {α : TauCeti.CStarAction (Multiplicative ℝ) A} {ω : A →P[ℂ] ℂ} :
  α.IsGroundState ω ↔
    ‖ω.toContinuousLinearMap‖ = 1 ∧
      ∃ (hf :
        ∀ (t : Multiplicative ℝ) (a : A),
          ω.toPositiveLinearMap ((α t) a) = ω.toPositiveLinearMap a),
        ∀ (ξ : ↥(α.gnsHamiltonian hf).domain), 0 ≤ inner ℂ (↑ξ) (↑(α.gnsHamiltonian hf) ξ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ground states are the states satisfying the generator inequality](ground-states-are-the-states-satisfying-the-gene.md)
- [Phragmén–Lindelöf principle on the upper half-plane](../../part-02/complex/part-03/phragmen-lindelof-principle-on-the-upper-half-pl.md)
- [Schwarz reflection principle (real axis)](../../part-02/complex/part-03/schwarz-reflection-principle-real-axis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.isGroundState_iff_exists_inner_gnsHamiltonian_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/GNS.html#TauCeti.CStarAction.isGroundState_iff_exists_inner_gnsHamiltonian_nonneg).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.isGroundState_iff_exists_inner_gnsHamiltonian_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/GNS.html#TauCeti.CStarAction.isGroundState_iff_exists_inner_gnsHamiltonian_nonneg)
- [Source of `TauCeti.CStarAction.isGroundState_iff_exists_inner_gnsHamiltonian_nonneg` in TauCeti/Analysis/CStarAlgebra/Action/GroundState/GNS.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/GroundState/GNS.lean#L68)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
