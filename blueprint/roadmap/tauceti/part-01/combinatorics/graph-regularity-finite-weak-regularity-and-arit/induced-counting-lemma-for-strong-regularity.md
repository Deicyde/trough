---
declaration: theorem
origin: cited
lean: SimpleGraph.StrongRegular.inducedGraphCount3_estimate
statement: formalized
proof: formalized
---

# Induced counting lemma for strong regularity

Let `(P, Q)` be a strong regularity witness
for `G` with `τ = F #P.parts > 0`, and suppose every part of `P` has at most `m` vertices. Then for
every graph `J` on `Fin 3`, the number of labelled induced copies of `J` in `G` differs from the
coarse prediction `J.coarseInducedGraphEstimate G P` by at most
`(15 τ + 3 √ε) (card α) ^ 3 + 6 m (card α) ^ 2`. Only the refinement, the equitability and
uniformity of `Q`, and the energy gap are used.

```lean
SimpleGraph.StrongRegular.inducedGraphCount3_estimate.{u_1} {α : Type u_1} [Fintype α]
  [DecidableEq α] {G : SimpleGraph α} [DecidableRel G.Adj] (J : SimpleGraph (Fin 3))
  [DecidableRel J.Adj] {P Q : Finpartition Finset.univ} {ε : ℝ} {F : ℕ → ℝ} {l₀ : ℕ}
  (h : G.StrongRegular P Q ε F l₀) (hF : 0 < F P.parts.card) {m : ℕ}
  (hm : ∀ A ∈ P.parts, A.card ≤ m) :
  |↑(J.inducedGraphCount3 G) - J.coarseInducedGraphEstimate G P| ≤
    (15 * F P.parts.card + 3 * √ε) * ↑(Fintype.card α) ^ 3 + 6 * ↑m * ↑(Fintype.card α) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`SimpleGraph.StrongRegular.inducedGraphCount3_estimate`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.html#SimpleGraph.StrongRegular.inducedGraphCount3_estimate).

## Sources

- [Tau Ceti documentation: `SimpleGraph.StrongRegular.inducedGraphCount3_estimate`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.html#SimpleGraph.StrongRegular.inducedGraphCount3_estimate)
- [Source of `SimpleGraph.StrongRegular.inducedGraphCount3_estimate` in TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Regularity/Graph/StrongRegularity.lean#L216)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Regularity/STATUS.md)
