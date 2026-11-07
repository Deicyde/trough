---
declaration: theorem
origin: cited
lean: TauCeti.Flow.exists_isMaximum_mem
statement: formalized
proof: formalized
---

# Integrality of maximum flows

For nonnegative capacities in an additive subgroup `H`, some
maximum ordinary flow takes values in `H`. For distinct terminals, its value is the capacity of
some cut by `TauCeti.Flow.IsMaximum.exists_val_eq_arrowSum`.

```lean
TauCeti.Flow.exists_isMaximum_mem.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w}
  [Fintype V] [(v w : V) → Fintype (Q v w)] [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]
  {cap : TauCeti.Assignment Q K} {s t : V} (hcap : 0 ≤ cap) (H : AddSubgroup K)
  (hcapH : ∀ ⦃v w : V⦄ (e : Q v w), cap e ∈ H) :
  ∃ f, f.IsMaximum ∧ ∀ ⦃v w : V⦄ (e : Q v w), f.toFun e ∈ H
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.residualUpdate](tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Flow.exists_isMaximum_mem`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/ShortestAugmentation.html#TauCeti.Flow.exists_isMaximum_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.Flow.exists_isMaximum_mem`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/ShortestAugmentation.html#TauCeti.Flow.exists_isMaximum_mem)
- [Source of `TauCeti.Flow.exists_isMaximum_mem` in TauCeti/Combinatorics/Network/ShortestAugmentation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/ShortestAugmentation.lean#L356)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
