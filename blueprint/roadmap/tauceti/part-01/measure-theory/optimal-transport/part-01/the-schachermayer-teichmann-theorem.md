---
declaration: theorem
origin: cited
lean: TauCeti.IsCoupling.isOptimalCoupling_iff_exists_isCyclicallyMonotone
statement: formalized
proof: formalized
---

# The Schachermayer--Teichmann theorem

For a finite-valued lower semicontinuous cost on a
product of Polish spaces, a coupling of finite cost between two probability measures is optimal
if and only if it is concentrated on a measurable `c`-cyclically monotone set.

The finite-cost hypothesis is used only for the forward implication: when every coupling has
infinite cost, every coupling is optimal.

```lean
TauCeti.IsCoupling.isOptimalCoupling_iff_exists_isCyclicallyMonotone.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [MeasurableSpace X] [TopologicalSpace X] [PolishSpace X] [BorelSpace X]
  [MeasurableSpace Y] [TopologicalSpace Y] [PolishSpace Y] [BorelSpace Y]
  {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y} [MeasureTheory.IsProbabilityMeasure μ]
  [MeasureTheory.IsProbabilityMeasure ν] {c : X × Y → ENNReal} {π : MeasureTheory.Measure (X × Y)}
  (hπ : TauCeti.IsCoupling π μ ν) (hc : LowerSemicontinuous c) (hctop : ∀ (z : X × Y), c z ≠ ⊤)
  (hfin : ∫⁻ (z : X × Y), c z ∂π ≠ ⊤) :
  TauCeti.IsOptimalCoupling c π μ ν ↔
    ∃ S, MeasurableSet S ∧ TauCeti.IsCyclicallyMonotone c S ∧ π Sᶜ = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lusin's universal-measurability theorem](../../measurable-space/lusins-universal-measurability-theorem.md)
- [Strong Kantorovich duality for probability measures](../part-02/strong-kantorovich-duality-for-probability-measu.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsCoupling.isOptimalCoupling_iff_exists_isCyclicallyMonotone`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/SchachermayerTeichmann.html#TauCeti.IsCoupling.isOptimalCoupling_iff_exists_isCyclicallyMonotone).

## Sources

- [Tau Ceti documentation: `TauCeti.IsCoupling.isOptimalCoupling_iff_exists_isCyclicallyMonotone`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Duality/SchachermayerTeichmann.html#TauCeti.IsCoupling.isOptimalCoupling_iff_exists_isCyclicallyMonotone)
- [Source of `TauCeti.IsCoupling.isOptimalCoupling_iff_exists_isCyclicallyMonotone` in TauCeti/MeasureTheory/OptimalTransport/Duality/SchachermayerTeichmann.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/OptimalTransport/Duality/SchachermayerTeichmann.lean#L97)
