---
declaration: theorem
origin: cited
lean: Setoid.hasCantorAntichainOn_range_of_forall_gSGraph_adj
statement: formalized
proof: formalized
---

# The category route to Silver's theorem

Let `E` be a Borel equivalence relation and `φ` a
continuous map from Cantor space sending the edges of `gSGraph S` to `E`-inequivalent pairs. If `S`
is dense, the range of `φ` carries a Cantor antichain for `E`.

```lean
Setoid.hasCantorAntichainOn_range_of_forall_gSGraph_adj.{u_1} {X : Type u_1} {S : Set (List Bool)}
  {φ : (ℕ → Bool) → X} [TopologicalSpace X] [MeasurableSpace X] [BorelSpace X] (E : Setoid X)
  (hE : MeasurableSet {p | E p.1 p.2}) (hS : TauCeti.DenseWords S) (hφ : Continuous φ)
  (hφE : ∀ ⦃y z : ℕ → Bool⦄, (TauCeti.gSGraph S).Adj y z → ¬E (φ y) (φ z)) :
  E.HasCantorAntichainOn (Set.range φ)
```

## Depends on

- [Setoid.HasCantorAntichainOn](setoid-hascantorantichainon.md)

## Proof depends on

- [The Kuratowski–Ulam theorem](the-kuratowski-ulam-theorem.md)
- [Miller's independence lemma](../descriptive/millers-independence-lemma.md)
- [Mycielski's theorem](../../topology/other-results/mycielskis-theorem.md)

## Lean

Formalized in Tau Ceti as [`Setoid.hasCantorAntichainOn_range_of_forall_gSGraph_adj`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.hasCantorAntichainOn_range_of_forall_gSGraph_adj).

## Sources

- [Tau Ceti documentation: `Setoid.hasCantorAntichainOn_range_of_forall_gSGraph_adj`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/Silver.html#Setoid.hasCantorAntichainOn_range_of_forall_gSGraph_adj)
- [Source of `Setoid.hasCantorAntichainOn_range_of_forall_gSGraph_adj` in TauCeti/SetTheory/Descriptive/Silver.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/SetTheory/Descriptive/Silver.lean#L112)
- [Tau Ceti roadmap status: Borel equivalence relations, the G₀ dichotomy and Silver's theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BorelEquivalenceRelations/STATUS.md)
