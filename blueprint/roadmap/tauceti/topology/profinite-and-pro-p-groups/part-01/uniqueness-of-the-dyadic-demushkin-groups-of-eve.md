---
declaration: theorem
origin: cited
lean: TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_even_demushkinRank_of_range_eq_unitsPlusMinus
statement: formalized
proof: formalized
---

# Uniqueness of the dyadic Demushkin groups of even rank with image `{±1} × U^(f)` (Labute, Theorem 6)

Two Demushkin groups at `p = 2` of the same even rank `n ≥ 4` whose canonical
characters have the same image `V^(f) = {±1} × U^(f)`, `f ≥ 2` finite, are topologically
isomorphic.

```lean
TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_even_demushkinRank_of_range_eq_unitsPlusMinus.{u,
    v}
  {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] {H : Type v} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  [CompactSpace H] [TotallyDisconnectedSpace H] (hG : TauCeti.IsDemushkin 2 G)
  (hH : TauCeti.IsDemushkin 2 H) (hn : TauCeti.demushkinRank hG = TauCeti.demushkinRank hH)
  (heven : Even (TauCeti.demushkinRank hG)) (hn3 : 3 < TauCeti.demushkinRank hG) {f : ℕ}
  (hf : 2 ≤ f) (hA : (TauCeti.demushkinCharacter hG).range = TauCeti.unitsPlusMinus f)
  (hB : (TauCeti.demushkinCharacter hH).range = TauCeti.unitsPlusMinus f) : Nonempty (G ≃ₜ* H)
```

## Depends on

- [The Demushkin predicate (Labute, p. 106), for a prime `p` and a topological group `G`](the-demushkin-predicate-labute-p-106-for-a-prime.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The constrained successive-approximation theorem](the-constrained-successive-approximation-theorem.md)
- [Dedekind's modular law](../../../algebra/other-results/dedekinds-modular-law.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's criterion](labutes-criterion.md)
- [Labute's Theorem 2](labutes-theorem-2.md)
- [The relative successive-approximation theorem](the-relative-successive-approximation-theorem.md)
- [The successive-approximation theorem with tails](../part-02/the-successive-approximation-theorem-with-tails.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_even_demushkinRank_of_range_eq_unitsPlusMinus`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/UnitsPlusMinus.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_even_demushkinRank_of_range_eq_unitsPlusMinus).

## Sources

- [Tau Ceti documentation: `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_even_demushkinRank_of_range_eq_unitsPlusMinus`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/UnitsPlusMinus.html#TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_even_demushkinRank_of_range_eq_unitsPlusMinus)
- [Source of `TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_even_demushkinRank_of_range_eq_unitsPlusMinus` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/UnitsPlusMinus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/UnitsPlusMinus.lean#L645)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ProfiniteProPGroups/STATUS.md)
