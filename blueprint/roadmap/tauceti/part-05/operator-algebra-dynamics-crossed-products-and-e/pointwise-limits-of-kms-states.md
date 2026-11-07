---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.IsKMSState.of_tendsto
statement: formalized
proof: formalized
---

# Pointwise limits of KMS states

If β-KMS states converge pointwise to a positive
functional of norm one, then the limit is a β-KMS state.

```lean
TauCeti.CStarAction.IsKMSState.of_tendsto.{u_1, u_2} {A : Type u_1} [NonUnitalCStarAlgebra A]
  [PartialOrder A] [StarOrderedRing A] {α : TauCeti.CStarAction (Multiplicative ℝ) A} {β : ℝ}
  {ω : A →P[ℂ] ℂ} {ι : Type u_2} {l : Filter ι} [l.NeBot] {ω' : ι → A →P[ℂ] ℂ}
  (hω' : ∀ᶠ (i : ι) in l, α.IsKMSState β (ω' i))
  (hlim : ∀ (a : A), Filter.Tendsto (fun i => (ω' i) a) l (nhds (ω a)))
  (hnorm : ‖ω.toContinuousLinearMap‖ = 1) : α.IsKMSState β ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dense analytic KMS criterion](dense-analytic-kms-criterion.md)
- [Density of entire analytic elements](density-of-entire-analytic-elements.md)
- [Schwarz reflection principle (real axis)](../../part-02/conformal-mapping-and-the-geometric-theory-of-ho/schwarz-reflection-principle-real-axis.md)
- [TauCeti.CStarAction.entireAnalytic](tauceti-cstaraction-entireanalytic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.IsKMSState.of_tendsto`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.html#TauCeti.CStarAction.IsKMSState.of_tendsto).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.IsKMSState.of_tendsto`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.html#TauCeti.CStarAction.IsKMSState.of_tendsto)
- [Source of `TauCeti.CStarAction.IsKMSState.of_tendsto` in TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/KMS/StateSpace.lean#L49)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
