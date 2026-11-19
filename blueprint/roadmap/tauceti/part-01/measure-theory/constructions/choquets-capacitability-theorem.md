---
declaration: theorem
origin: cited
lean: TauCeti.IsChoquetCapacity.analyticSet_eq_biSup_isCompact
statement: formalized
proof: formalized
---

# Choquet's capacitability theorem

On a Hausdorff space, the capacity of every analytic set
equals the supremum of the capacities of its compact subsets.

```lean
TauCeti.IsChoquetCapacity.analyticSet_eq_biSup_isCompact.{u_1} {X : Type u_1} [TopologicalSpace X]
  [T2Space X] {I : Set X → ENNReal} (hI : TauCeti.IsChoquetCapacity I) {S : Set X}
  (hS : MeasureTheory.AnalyticSet S) : I S = ⨆ K, ⨆ (_ : IsCompact K), ⨆ (_ : K ⊆ S), I K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsChoquetCapacity.analyticSet_eq_biSup_isCompact`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Capacitability.html#TauCeti.IsChoquetCapacity.analyticSet_eq_biSup_isCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.IsChoquetCapacity.analyticSet_eq_biSup_isCompact`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Constructions/Polish/Capacitability.html#TauCeti.IsChoquetCapacity.analyticSet_eq_biSup_isCompact)
- [Source of `TauCeti.IsChoquetCapacity.analyticSet_eq_biSup_isCompact` in TauCeti/MeasureTheory/Constructions/Polish/Capacitability.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/MeasureTheory/Constructions/Polish/Capacitability.lean#L228)
