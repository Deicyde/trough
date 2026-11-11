---
declaration: theorem
origin: cited
lean: LinearMap.continuous_of_seq_closed_graph_of_isTate
statement: formalized
proof: formalized
---

# Sequential Closed Graph Theorem for normed modules over a Tate ring

a linear map from a
complete ultrametric normed module to a complete ultrametric seminormed module whose graph is
sequentially closed is continuous.

```lean
LinearMap.continuous_of_seq_closed_graph_of_isTate.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {N : Type u_3} [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [NormedAddCommGroup M]
  [IsUltrametricDist M] [CompleteSpace M] [_root_.Module R M] [IsBoundedSMul R M]
  [SeminormedAddCommGroup N] [IsUltrametricDist N] [CompleteSpace N] [_root_.Module R N]
  [IsBoundedSMul R N] (f : M →ₗ[R] N)
  (hg :
    ∀ (u : ℕ → M) (x : M) (y : N),
      Filter.Tendsto u Filter.atTop (nhds x) →
        Filter.Tendsto (⇑f ∘ u) Filter.atTop (nhds y) → y = f x) :
  Continuous ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Closed Graph Theorem for normed modules over a Tate ring](../part-01/closed-graph-theorem-for-normed-modules-over-a-t.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.continuous_of_seq_closed_graph_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#LinearMap.continuous_of_seq_closed_graph_of_isTate).

## Sources

- [Tau Ceti documentation: `LinearMap.continuous_of_seq_closed_graph_of_isTate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.html#LinearMap.continuous_of_seq_closed_graph_of_isTate)
- [Source of `LinearMap.continuous_of_seq_closed_graph_of_isTate` in TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/RingOpNorm/OpenMapping.lean#L437)
