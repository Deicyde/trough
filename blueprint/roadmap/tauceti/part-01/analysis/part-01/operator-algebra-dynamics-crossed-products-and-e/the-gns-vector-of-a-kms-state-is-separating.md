---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.IsKMSState.eq_zero_of_apply_toPreGNS_one_eq_zero
statement: formalized
proof: formalized
---

# The GNS vector of a KMS state is separating

Let `ω` be a β-KMS state on a unital
C⋆-algebra, with GNS representation `π_ω` and GNS vector `Ω = [1]`. An operator `x` in the von
Neumann algebra `π_ω(A)''` with `x Ω = 0` is zero.

```lean
TauCeti.CStarAction.IsKMSState.eq_zero_of_apply_toPreGNS_one_eq_zero.{u_1} {A : Type u_1}
  [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
  {α : TauCeti.CStarAction (Multiplicative ℝ) A} {β : ℝ} {ω : A →P[ℂ] ℂ} (hω : α.IsKMSState β ω)
  {x : ω.GNS →L[ℂ] ω.GNS} (hx : x ∈ VonNeumannAlgebra.adjoin (Set.range ⇑ω.gnsStarAlgHom))
  (hx₀ : x ↑(ω.toPreGNS 1) = 0) : x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schwarz reflection principle (real axis)](../../part-02/complex/part-03/schwarz-reflection-principle-real-axis.md)
- [The von Neumann density theorem](../../part-03/other-results/the-von-neumann-density-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.IsKMSState.eq_zero_of_apply_toPreGNS_one_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/Separating.html#TauCeti.CStarAction.IsKMSState.eq_zero_of_apply_toPreGNS_one_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.IsKMSState.eq_zero_of_apply_toPreGNS_one_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/KMS/Separating.html#TauCeti.CStarAction.IsKMSState.eq_zero_of_apply_toPreGNS_one_eq_zero)
- [Source of `TauCeti.CStarAction.IsKMSState.eq_zero_of_apply_toPreGNS_one_eq_zero` in TauCeti/Analysis/CStarAlgebra/Action/KMS/Separating.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/Action/KMS/Separating.lean#L111)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
