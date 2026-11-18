---
declaration: theorem
origin: cited
lean: TauCeti.isCellularSet_closedBall_inter_preimage, TauCeti.isCellularSet_preimage_singleton_of_injOn
statement: formalized
proof: formalized
---

# Brown's theorem on inverse sets

Let `E` be a finite-dimensional real normed space of
dimension `n`, and let `f` map the closed unit ball `Q` of `E` continuously into the unit sphere
`Sⁿ` of a real normed space of dimension `n + 1`. Suppose that the fibre `Q ∩ f⁻¹(y)` of a point
`y` of `f(Q)` lies in the open ball and that `f` is injective off it, so that it is the only
inverse set of `f`. Then this fibre is cellular.

```lean
TauCeti.isCellularSet_closedBall_inter_preimage.{u_1, u_2} {F : Type u_1} [NormedAddCommGroup F]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [NormedSpace ℝ F]
  {f : E → ↑(Metric.sphere 0 1)} {y : ↑(Metric.sphere 0 1)}
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hf : ContinuousOn f (Metric.closedBall 0 1))
  (hinj : Set.InjOn f (Metric.closedBall 0 1 \ f ⁻¹' {y})) (hy : y ∉ f '' Metric.sphere 0 1)
  (hy' : y ∈ f '' Metric.closedBall 0 1) :
  TauCeti.IsCellularSet E (Metric.closedBall 0 1 ∩ f ⁻¹' {y})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brown's Theorem 3: the only inverse set of a map of a cell is cellular](browns-theorem-3-the-only-inverse-set-of-a-map-o.md)
- [The Jordan–Brouwer separation theorem](../../../part-01/algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCellularSet_closedBall_inter_preimage`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet/Sphere.html#TauCeti.isCellularSet_closedBall_inter_preimage).

## Other forms

**Brown's theorem on two inverse sets.** Formalized in Tau Ceti as [`TauCeti.isCellularSet_preimage_singleton_of_injOn`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet/Sphere.html#TauCeti.isCellularSet_preimage_singleton_of_injOn).

```lean
TauCeti.isCellularSet_preimage_singleton_of_injOn.{u_1, u_2} {F : Type u_1} [NormedAddCommGroup F]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [InnerProductSpace ℝ F] {g : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  {p q : ↑(Metric.sphere 0 1)} (hn : 1 ≤ Module.finrank ℝ E)
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hg : Continuous g)
  (hgs : Function.Surjective g) (hpq : p ≠ q) (hinj : Set.InjOn g (g ⁻¹' {p, q})ᶜ) :
  TauCeti.IsCellularSet E (g ⁻¹' {q})
```

## Sources

- [Tau Ceti documentation: `TauCeti.isCellularSet_closedBall_inter_preimage`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet/Sphere.html#TauCeti.isCellularSet_closedBall_inter_preimage)
- [Source of `TauCeti.isCellularSet_closedBall_inter_preimage` in TauCeti/Topology/CellularSet/InverseSet/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/CellularSet/InverseSet/Sphere.lean#L114)
