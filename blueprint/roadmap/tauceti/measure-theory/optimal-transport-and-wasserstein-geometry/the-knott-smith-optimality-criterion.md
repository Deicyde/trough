---
declaration: theorem
origin: cited
lean: TauCeti.IsCoupling.isOptimalCoupling_iff_exists_ae_mem_subdifferential
statement: formalized
proof: formalized
---

# The Knott–Smith optimality criterion

On a separable real inner product space, a coupling
`π` of finite measures `μ` and `ν` with finite second moments is an optimal plan for the cost
`‖x - y‖ ^ 2 / 2` exactly when there is a proper (never `⊥`, and finite somewhere) convex, lower
semicontinuous `u : E → EReal` such that `y ∈ ∂u(x)` for `π`-almost every `(x, y)`.

```lean
TauCeti.IsCoupling.isOptimalCoupling_iff_exists_ae_mem_subdifferential.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [MeasurableSpace E] [OpensMeasurableSpace (E × E)]
  {μ ν : MeasureTheory.Measure E} {π : MeasureTheory.Measure (E × E)} [OpensMeasurableSpace E]
  [SecondCountableTopology E] [MeasureTheory.IsFiniteMeasure μ] (hπ : TauCeti.IsCoupling π μ ν)
  (hμ : MeasureTheory.MemLp id 2 μ) (hν : MeasureTheory.MemLp id 2 ν) :
  TauCeti.IsOptimalCoupling (fun z => ENNReal.ofReal (‖z.1 - z.2‖ ^ 2 / 2)) π μ ν ↔
    ∃ u,
      Convex ℝ {p | u p.1 ≤ ↑p.2} ∧
        LowerSemicontinuous u ∧
          (∀ (x : E), u x ≠ ⊥) ∧
            (∃ x, u x ≠ ⊤) ∧ ∀ᵐ (z : E × E) ∂π, z.2 ∈ TauCeti.subdifferential (innerₗ E) u z.1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fenchel–Young inequality](../../analysis/part-02/convex/the-fenchel-young-inequality.md)
- [Rockafellar's theorem](../optimal-transport/rockafellars-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCoupling.isOptimalCoupling_iff_exists_ae_mem_subdifferential`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.IsCoupling.isOptimalCoupling_iff_exists_ae_mem_subdifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.IsCoupling.isOptimalCoupling_iff_exists_ae_mem_subdifferential`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Brenier.html#TauCeti.IsCoupling.isOptimalCoupling_iff_exists_ae_mem_subdifferential)
- [Source of `TauCeti.IsCoupling.isOptimalCoupling_iff_exists_ae_mem_subdifferential` in TauCeti/MeasureTheory/OptimalTransport/Brenier.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Brenier.lean#L362)
