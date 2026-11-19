---
declaration: theorem
origin: cited
lean: TauCeti.LiRankGenusTheorem.not_rankGenusConjecture
statement: formalized
proof: formalized
---

# Li's theorem refutes Waldhausen's conjecture

some closed orientable `3`-manifold has
Heegaard genus different from the rank of its fundamental group.

```lean
TauCeti.LiRankGenusTheorem.not_rankGenusConjecture.{u} (h : TauCeti.LiRankGenusTheorem) :
  ¬TauCeti.RankGenusConjecture
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Koszul formula](../../../part-01/geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LiRankGenusTheorem.not_rankGenusConjecture`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem.not_rankGenusConjecture), assuming [`TauCeti.LiRankGenusTheorem`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.LiRankGenusTheorem.not_rankGenusConjecture`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem.not_rankGenusConjecture)
- [Source of `TauCeti.LiRankGenusTheorem.not_rankGenusConjecture` in TauCeti/LowDimTopology/Heegaard/RankGenus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LowDimTopology/Heegaard/RankGenus.lean#L156)
