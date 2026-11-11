---
declaration: theorem
origin: cited
lean: TauCeti.isNashAt_iff_exists_isSemialgebraicOn, TauCeti.forall_isNashAt_apply_iff_exists_isSemialgebraicOn
statement: formalized
proof: formalized
---

# The local Nash graph criterion

A scalar function is a Nash germ at `x` exactly when
it is analytic there and its graph is semialgebraic on some open semialgebraic neighbourhood.

```lean
TauCeti.isNashAt_iff_exists_isSemialgebraicOn.{u_1} {σ : Type u_1} [Fintype σ] {f : (σ → ℝ) → ℝ}
  {x : σ → ℝ} :
  TauCeti.IsNashAt f x ↔
    AnalyticAt ℝ f x ∧
      ∃ U,
        IsOpen U ∧ x ∈ U ∧ TauCeti.IsSemialgebraic U ∧ TauCeti.IsSemialgebraicOn (fun y x => f y) U
```

## Depends on

- [TauCeti.IsNashAt](tauceti-isnashat.md)

## Proof depends on

- [Cauchy's bound on the symmetric power](../../../analysis/part-03/polynomial/cauchys-bound-on-the-symmetric-power.md)
- [Existence of adapted cylindrical algebraic decompositions](../real-algebraic-geometry-sign-determination-and-c/existence-of-adapted-cylindrical-algebraic-decom.md)
- [The Tarski–Seidenberg theorem](../complex-morse-theory-affine-topology-and-weak-le/the-tarski-seidenberg-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isNashAt_iff_exists_isSemialgebraicOn`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Graph.html#TauCeti.isNashAt_iff_exists_isSemialgebraicOn).

## Other forms

**The local Nash graph criterion for maps.** Formalized in Tau Ceti as [`TauCeti.forall_isNashAt_apply_iff_exists_isSemialgebraicOn`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Graph.html#TauCeti.forall_isNashAt_apply_iff_exists_isSemialgebraicOn).

```lean
TauCeti.forall_isNashAt_apply_iff_exists_isSemialgebraicOn.{u_1, u_2} {σ : Type u_1} {τ : Type u_2}
  [Fintype σ] [Fintype τ] {g : (σ → ℝ) → τ → ℝ} {x : σ → ℝ} :
  (∀ (i : τ), TauCeti.IsNashAt (fun y => g y i) x) ↔
    AnalyticAt ℝ g x ∧ ∃ U, IsOpen U ∧ x ∈ U ∧ TauCeti.IsSemialgebraicOn g U
```

## Sources

- [Tau Ceti documentation: `TauCeti.isNashAt_iff_exists_isSemialgebraicOn`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Graph.html#TauCeti.isNashAt_iff_exists_isSemialgebraicOn)
- [Source of `TauCeti.isNashAt_iff_exists_isSemialgebraicOn` in TauCeti/Geometry/RealAlgebraic/Nash/Graph.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Nash/Graph.lean#L161)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
