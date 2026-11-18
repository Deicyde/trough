---
declaration: theorem
origin: cited
lean: TauCeti.Colored3Graph.abs_inducedCopyCount_sub_expectedInducedCount_le_of_topRegular
statement: formalized
proof: formalized
---

# Induced counting over a regular triadic complex

Let `C` be a polyad decomposition on
`V`, let `F` be a pattern on `k` vertices, and let `0 < ε`. Suppose that

* `H` approximates `H'` within `inducedCountingParameter3 k ε`,
* the lower skeleton of `C` is regular for the schedule `inducedCountingSchedule3 k ε`,
* `H'` is top-regular, at tolerance `inducedCountingSchedule3 k ε C.complexity` and a positive
  rank `r`, over all polyads of `C` except an `inducedCountingParameter3 k ε` proportion, and
* the vertex cells of `C` form an equipartition into at least `diagonalControl3 k ε` cells.

Then the induced count of `F` in `H` differs from the prediction `H'.expectedInducedCount C F` by
at most `ε |V| ^ k`.

```lean
TauCeti.Colored3Graph.abs_inducedCopyCount_sub_expectedInducedCount_le_of_topRegular.{u_1, u_2}
  {κ : Type u_1} {V : Type u_2} [DecidableEq κ] [Fintype V] [DecidableEq V]
  {C : TauCeti.TriadicComplex3 V} {F : TauCeti.FiniteColored3Pattern κ}
  {H H' : TauCeti.Colored3Graph κ V} (hC : C.IsPolyadDecomposition) {ε : ℝ} (hε : 0 < ε)
  (hedit : H.Approximates3 H' (TauCeti.inducedCountingParameter3 F.k ε))
  (hlower : C.skeleton.LowerSkeletonRegular (TauCeti.inducedCountingSchedule3 F.k ε)) {r : ℕ}
  (hr : 1 ≤ r)
  (htop :
    H'.TopRegularOverMostPolyads C (TauCeti.inducedCountingSchedule3 F.k ε C.complexity)
      (TauCeti.inducedCountingParameter3 F.k ε) r)
  (hcells : C.VertexCellsControlled (TauCeti.diagonalControl3 F.k ε)) :
  |↑(H.inducedCopyCount F) - TauCeti.Colored3Graph.expectedInducedCount C F H'| ≤
    ε * ↑(Fintype.card V) ^ F.k
```

## Depends on

- [TauCeti.Colored3Graph.expectedInducedCount](tauceti-colored3graph-expectedinducedcount.md)
- [TauCeti.TriadicComplex3](tauceti-triadiccomplex3.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.abs_inducedCopyCount_sub_expectedInducedCount_le_of_topRegular`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/InducedCounting.html#TauCeti.Colored3Graph.abs_inducedCopyCount_sub_expectedInducedCount_le_of_topRegular).

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.abs_inducedCopyCount_sub_expectedInducedCount_le_of_topRegular`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/InducedCounting.html#TauCeti.Colored3Graph.abs_inducedCopyCount_sub_expectedInducedCount_le_of_topRegular)
- [Source of `TauCeti.Colored3Graph.abs_inducedCopyCount_sub_expectedInducedCount_le_of_topRegular` in TauCeti/Combinatorics/Hypergraph/Triadic/InducedCounting.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Hypergraph/Triadic/InducedCounting.lean#L99)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Regularity/STATUS.md)
