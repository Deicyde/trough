---
declaration: theorem
origin: cited
lean: Matrix.IsHermitian.isKMSState_iff_eq_gibbsState
statement: formalized
proof: formalized
---

# Uniqueness of the KMS state

A state is a β-KMS state for the time evolution generated
by a Hermitian matrix `K` exactly when it is the Gibbs state, for every real `β`.

```lean
Matrix.IsHermitian.isKMSState_iff_eq_gibbsState.{u_1} {m : Type u_1} [Fintype m] [DecidableEq m]
  [Nonempty m] {K : Matrix m m ℂ} (hK : K.IsHermitian) (β : ℝ) {ω : Matrix m m ℂ →P[ℂ] ℂ} :
  (selfAdjoint.cstarAction ⟨K, hK⟩).IsKMSState β ω ↔ ω = K.gibbsState hK β
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schwarz reflection principle (real axis)](../../part-03/complex/part-04/schwarz-reflection-principle-real-axis.md)

## Lean

Formalized in Tau Ceti as [`Matrix.IsHermitian.isKMSState_iff_eq_gibbsState`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Gibbs.html#Matrix.IsHermitian.isKMSState_iff_eq_gibbsState).

## Sources

- [Tau Ceti documentation: `Matrix.IsHermitian.isKMSState_iff_eq_gibbsState`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Gibbs.html#Matrix.IsHermitian.isKMSState_iff_eq_gibbsState)
- [Source of `Matrix.IsHermitian.isKMSState_iff_eq_gibbsState` in TauCeti/Analysis/CStarAlgebra/Action/Gibbs.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/Action/Gibbs.lean#L115)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
