---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.IsGroundState.of_tendsto_isKMSState
statement: formalized
proof: formalized
---

# Zero-temperature limits of KMS states are ground states

If `β i → +∞`, the states
`ω' i` are eventually `β i`-KMS states, and they converge pointwise to a positive functional `ω`
of norm one, then `ω` is a ground state. The norm condition cannot be dropped for nonunital
`A`, where states may converge weak-* to `0`.

```lean
TauCeti.CStarAction.IsGroundState.of_tendsto_isKMSState.{u_1, u_2} {A : Type u_1}
  [NonUnitalCStarAlgebra A] {α : TauCeti.CStarAction (Multiplicative ℝ) A} [PartialOrder A]
  [StarOrderedRing A] {ω : A →P[ℂ] ℂ} {ι : Type u_2} {l : Filter ι} [l.NeBot] {β : ι → ℝ}
  (hβ : Filter.Tendsto β l Filter.atTop) {ω' : ι → A →P[ℂ] ℂ}
  (hω' : ∀ᶠ (i : ι) in l, α.IsKMSState (β i) (ω' i))
  (hlim : ∀ (a : A), Filter.Tendsto (fun i => (ω' i) a) l (nhds (ω a)))
  (hnorm : ‖ω.toContinuousLinearMap‖ = 1) : α.IsGroundState ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Analytic characterization of ground states](analytic-characterization-of-ground-states.md)
- [Schwarz reflection principle (real axis)](../../part-02/complex/part-03/schwarz-reflection-principle-real-axis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.IsGroundState.of_tendsto_isKMSState`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.html#TauCeti.CStarAction.IsGroundState.of_tendsto_isKMSState).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.IsGroundState.of_tendsto_isKMSState`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.html#TauCeti.CStarAction.IsGroundState.of_tendsto_isKMSState)
- [Source of `TauCeti.CStarAction.IsGroundState.of_tendsto_isKMSState` in TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/GroundState/Basic.lean#L461)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
