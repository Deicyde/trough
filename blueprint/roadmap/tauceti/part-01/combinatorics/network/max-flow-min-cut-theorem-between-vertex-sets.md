---
declaration: theorem
origin: cited
lean: TauCeti.SetFlow.exists_val_eq_arrowSum
statement: formalized
proof: formalized
---

# Max-flow/min-cut theorem between vertex sets

For disjoint `A` and `B` and nonnegative
capacities, some `A`–`B` flow has value equal to the capacity of some `A`–`B` cut. By weak duality
(`TauCeti.SetFlow.val_le_arrowSum`) this flow is maximum and this cut is minimum.

```lean
TauCeti.SetFlow.exists_val_eq_arrowSum.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w}
  [Fintype V] [(v w : V) → Fintype (Q v w)] [AddCommGroup K] [DecidableEq V] [LinearOrder K]
  [IsOrderedAddMonoid K] {cap : TauCeti.Assignment Q K} {A B : Finset V} (hAB : Disjoint A B)
  (hcap : 0 ≤ cap) :
  ∃ f S, TauCeti.TerminalCut.IsAdmissible A B S ∧ f.val = TauCeti.arrowSum cap S Sᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.residualUpdate](../finite-graph-connectivity-and-network-flows/part-01/tauceti-residualupdate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SetFlow.exists_val_eq_arrowSum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/SetFlow.html#TauCeti.SetFlow.exists_val_eq_arrowSum).

## Sources

- [Tau Ceti documentation: `TauCeti.SetFlow.exists_val_eq_arrowSum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/SetFlow.html#TauCeti.SetFlow.exists_val_eq_arrowSum)
- [Source of `TauCeti.SetFlow.exists_val_eq_arrowSum` in TauCeti/Combinatorics/Network/SetFlow.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Network/SetFlow.lean#L512)
