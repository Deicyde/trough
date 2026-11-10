---
declaration: theorem
origin: cited
lean: TauCeti.exists_mem_orientedGS_of_not_isMeagre, TauCeti.exists_gSGraph_adj_of_not_isMeagre
statement: formalized
proof: formalized
---

# Miller's independence lemma

If every word extends to a word of `S`, then every
non-meagre subset of Cantor space with the Baire property contains both ends of an oriented
edge of `orientedGS S`.

```lean
TauCeti.exists_mem_orientedGS_of_not_isMeagre {S : Set (List Bool)} {A : Set (ℕ → Bool)}
  (hS : TauCeti.DenseWords S) (hA : BaireMeasurableSet A) (hn : ¬IsMeagre A) :
  ∃ a ∈ A, ∃ b ∈ A, (a, b) ∈ TauCeti.orientedGS S
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_mem_orientedGS_of_not_isMeagre`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GSGraph.html#TauCeti.exists_mem_orientedGS_of_not_isMeagre).

## Other forms

**Miller's independence lemma, for the simple graph.** Formalized in Tau Ceti as [`TauCeti.exists_gSGraph_adj_of_not_isMeagre`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GSGraph.html#TauCeti.exists_gSGraph_adj_of_not_isMeagre).

```lean
TauCeti.exists_gSGraph_adj_of_not_isMeagre {S : Set (List Bool)} {A : Set (ℕ → Bool)}
  (hS : TauCeti.DenseWords S) (hA : BaireMeasurableSet A) (hn : ¬IsMeagre A) :
  ∃ a ∈ A, ∃ b ∈ A, (TauCeti.gSGraph S).Adj a b
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_mem_orientedGS_of_not_isMeagre`](https://taucetiproject.org/docs/TauCeti/SetTheory/Descriptive/GSGraph.html#TauCeti.exists_mem_orientedGS_of_not_isMeagre)
- [Source of `TauCeti.exists_mem_orientedGS_of_not_isMeagre` in TauCeti/SetTheory/Descriptive/GSGraph.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/SetTheory/Descriptive/GSGraph.lean#L312)
