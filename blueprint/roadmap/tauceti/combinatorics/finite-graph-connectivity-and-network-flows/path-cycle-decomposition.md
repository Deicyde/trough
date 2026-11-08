---
declaration: theorem
origin: cited
lean: TauCeti.exists_pathCycleDecomposition
statement: formalized
proof: formalized
---

# Path–cycle decomposition

Every nonnegative arrow assignment `f` on a finite arrow family
is a sum of positively weighted directed paths, each from a vertex of negative excess to a vertex
of positive excess, and positively weighted directed cycles. The number of components is at most
the number of arrows on which `f` is positive, and if the values of `f` lie in an additive subgroup
`H`, then so do all weights.

```lean
TauCeti.exists_pathCycleDecomposition.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w}
  [Fintype V] [(x y : V) → Fintype (Q x y)] [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]
  {f : TauCeti.Assignment Q K} (H : AddSubgroup K) (hf : 0 ≤ f)
  (hH : ∀ ⦃x y : V⦄ (e : Q x y), f e ∈ H) :
  ∃ D,
    (∀ p ∈ D.paths, p.weight ∈ H) ∧
      (∀ c ∈ D.cycles, c.weight ∈ H) ∧ D.paths.length + D.cycles.length ≤ {a | 0 < f a.snd.snd}.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_pathCycleDecomposition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Decomposition.html#TauCeti.exists_pathCycleDecomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_pathCycleDecomposition`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Decomposition.html#TauCeti.exists_pathCycleDecomposition)
- [Source of `TauCeti.exists_pathCycleDecomposition` in TauCeti/Combinatorics/Network/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/Decomposition.lean#L549)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
