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

- [The Koszul formula](../../../part-01/geometry/part-02/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LiRankGenusTheorem.not_rankGenusConjecture`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem.not_rankGenusConjecture), assuming [`TauCeti.LiRankGenusTheorem`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.LiRankGenusTheorem.not_rankGenusConjecture`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem.not_rankGenusConjecture)
- [Source of `TauCeti.LiRankGenusTheorem.not_rankGenusConjecture` in TauCeti/LowDimTopology/Heegaard/RankGenus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LowDimTopology/Heegaard/RankGenus.lean#L156)
