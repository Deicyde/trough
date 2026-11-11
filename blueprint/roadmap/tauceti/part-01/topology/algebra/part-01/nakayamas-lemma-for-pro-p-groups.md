---
declaration: theorem
origin: cited
lean: TauCeti.IsProP.eq_bot_of_le_pLowerCentralStep, TauCeti.IsProP.le_of_le_topologicalClosure_sup_pLowerCentralStep
statement: formalized
proof: formalized
---

# Nakayama's lemma for pro-`p` groups

In a profinite pro-`p` group a subgroup `K` with
`K ≤ closure (Kᵖ ⬝ [K, G])` is trivial: it lies in every term of the lower `p`-series.

```lean
TauCeti.IsProP.eq_bot_of_le_pLowerCentralStep.{u_1} {p : ℕ} {G : Type u_1} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (hG : TauCeti.IsProP p G) (hp : Nat.Prime p) {K : Subgroup G}
  (h : K ≤ TauCeti.pLowerCentralStep p K) : K = ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsProP.eq_bot_of_le_pLowerCentralStep`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.html#TauCeti.IsProP.eq_bot_of_le_pLowerCentralStep).

## Other forms

**Nakayama's lemma for pro-`p` groups, relative form.** Formalized in Tau Ceti as [`TauCeti.IsProP.le_of_le_topologicalClosure_sup_pLowerCentralStep`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.html#TauCeti.IsProP.le_of_le_topologicalClosure_sup_pLowerCentralStep).

```lean
TauCeti.IsProP.le_of_le_topologicalClosure_sup_pLowerCentralStep.{u_1} {p : ℕ} {G : Type u_1}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (hG : TauCeti.IsProP p G) (hp : Nat.Prime p) {R N : Subgroup G}
  [N.Normal] (hN : IsClosed ↑N) (h : R ≤ (N ⊔ TauCeti.pLowerCentralStep p R).topologicalClosure) :
  R ≤ N
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsProP.eq_bot_of_le_pLowerCentralStep`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.html#TauCeti.IsProP.eq_bot_of_le_pLowerCentralStep)
- [Source of `TauCeti.IsProP.eq_bot_of_le_pLowerCentralStep` in TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ProP/LowerCentralSeries.lean#L253)
