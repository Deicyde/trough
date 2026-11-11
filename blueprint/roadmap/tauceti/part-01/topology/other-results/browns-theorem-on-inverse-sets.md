---
declaration: theorem
origin: cited
lean: TauCeti.isCellularSet_closedBall_inter_preimage, TauCeti.isCellularSet_preimage_singleton_of_injOn
statement: formalized
proof: formalized
---

# Brown's theorem on inverse sets

Let `E` be a real normed space of dimension `n ≥ 2`, and
let `f` map the closed unit ball `Q` of `E` continuously into the unit sphere `Sⁿ` of a real inner
product space of dimension `n + 1`. Suppose that the fibre `Q ∩ f⁻¹(y)` of a point `y` of `f(Q)`
lies in the open ball and that `f` is injective off it, so that it is the only inverse set of `f`.
Then this fibre is cellular.

```lean
TauCeti.isCellularSet_closedBall_inter_preimage.{u_1, u_2} {F : Type u_1} [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] {f : E → ↑(Metric.sphere 0 1)} {y : ↑(Metric.sphere 0 1)}
  (hn : 2 ≤ Module.finrank ℝ E) (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1)
  (hf : ContinuousOn f (Metric.closedBall 0 1))
  (hinj : Set.InjOn f (Metric.closedBall 0 1 \ f ⁻¹' {y})) (hy : y ∉ f '' Metric.sphere 0 1)
  (hy' : y ∈ f '' Metric.closedBall 0 1) :
  TauCeti.IsCellularSet E (Metric.closedBall 0 1 ∩ f ⁻¹' {y})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jordan–Brouwer separation theorem](../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCellularSet_closedBall_inter_preimage`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet.html#TauCeti.isCellularSet_closedBall_inter_preimage).

## Other forms

**Brown's theorem on two inverse sets.** Formalized in Tau Ceti as [`TauCeti.isCellularSet_preimage_singleton_of_injOn`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet.html#TauCeti.isCellularSet_preimage_singleton_of_injOn).

```lean
TauCeti.isCellularSet_preimage_singleton_of_injOn.{u_1, u_2} {F : Type u_1} [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] {g : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  {p q : ↑(Metric.sphere 0 1)} (hn : 2 ≤ Module.finrank ℝ E)
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hg : Continuous g)
  (hgs : Function.Surjective g) (hpq : p ≠ q) (hinj : Set.InjOn g (g ⁻¹' {p, q})ᶜ) :
  TauCeti.IsCellularSet E (g ⁻¹' {q})
```

## Sources

- [Tau Ceti documentation: `TauCeti.isCellularSet_closedBall_inter_preimage`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet.html#TauCeti.isCellularSet_closedBall_inter_preimage)
- [Source of `TauCeti.isCellularSet_closedBall_inter_preimage` in TauCeti/Topology/CellularSet/InverseSet.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/CellularSet/InverseSet.lean#L305)
