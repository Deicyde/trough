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

- [The Koszul formula](../../geometry/part-01/manifold/part-02/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LiRankGenusTheorem.not_rankGenusConjecture`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem.not_rankGenusConjecture), assuming [`TauCeti.LiRankGenusTheorem`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.LiRankGenusTheorem.not_rankGenusConjecture`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/Heegaard/RankGenus.html#TauCeti.LiRankGenusTheorem.not_rankGenusConjecture)
- [Source of `TauCeti.LiRankGenusTheorem.not_rankGenusConjecture` in TauCeti/LowDimTopology/Heegaard/RankGenus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LowDimTopology/Heegaard/RankGenus.lean#L156)
