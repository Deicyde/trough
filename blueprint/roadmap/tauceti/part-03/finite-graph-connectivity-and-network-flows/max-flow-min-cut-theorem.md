---
declaration: theorem
origin: cited
lean: TauCeti.Flow.exists_val_eq_arrowSum
statement: formalized
proof: formalized
---

# Max-flow/min-cut theorem

For nonnegative capacities and distinct terminals, some ordinary
flow has value equal to the capacity of the arrows leaving some vertex set containing `s` but not
`t`. By weak duality (`TauCeti.Flow.val_le_arrowSum`) this flow is maximum and this cut is
minimum.

```lean
TauCeti.Flow.exists_val_eq_arrowSum.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w}
  [Fintype V] [(v w : V) → Fintype (Q v w)] [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]
  {cap : TauCeti.Assignment Q K} {s t : V} [DecidableEq V] (hst : s ≠ t) (hcap : 0 ≤ cap) :
  ∃ f S, s ∈ S ∧ t ∉ S ∧ f.val = TauCeti.arrowSum cap S Sᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Integrality of maximum flows](integrality-of-maximum-flows.md)
- [TauCeti.residualUpdate](tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Flow.exists_val_eq_arrowSum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/ShortestAugmentation.html#TauCeti.Flow.exists_val_eq_arrowSum).

## Sources

- [Tau Ceti documentation: `TauCeti.Flow.exists_val_eq_arrowSum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/ShortestAugmentation.html#TauCeti.Flow.exists_val_eq_arrowSum)
- [Source of `TauCeti.Flow.exists_val_eq_arrowSum` in TauCeti/Combinatorics/Network/ShortestAugmentation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/ShortestAugmentation.lean#L374)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
