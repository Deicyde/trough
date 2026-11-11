---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_demushkinWordTwoOdd_of_odd
statement: formalized
proof: formalized
---

# Labute's normal form for `q = 2` and odd rank (Labute, Theorem 3, case (2))

Let
`r ∈ Φ(F)` be a relator of the free pro-`2` group on an odd number `n` of generators presenting a
Demushkin group `G = ⟨x₁, …, x_n ∣ r⟩`. Then a continuous automorphism of `F` carries `r` either to
`x₁² (x₂, x₃) ⋯ (x_{n-1}, x_n)`, Labute's level `f = ∞`, or to
`x₁² x₂^{2^f} (x₂, x₃) ⋯ (x_{n-1}, x_n)` for some `f ≥ 2`.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_demushkinWordTwoOdd_of_odd {n : ℕ} (hn : Odd n)
  {r : TauCeti.freeProP 2 (Fin n)} (hr : r ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r})) :
  ∃ e,
    e r = TauCeti.demushkinWordTwoOddTop n (TauCeti.freeProPGen 2 n) ∨
      ∃ f, 2 ≤ f ∧ e r = TauCeti.demushkinWordTwoOdd f n (TauCeti.freeProPGen 2 n)
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's criterion](labutes-criterion.md)
- [The relative successive-approximation theorem](../part-02/the-relative-successive-approximation-theorem.md)
- [The successive-approximation theorem with tails](../../algebra/part-02/the-successive-approximation-theorem-with-tails.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_demushkinWordTwoOdd_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Exact.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_demushkinWordTwoOdd_of_odd).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_demushkinWordTwoOdd_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Exact.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_demushkinWordTwoOdd_of_odd)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_demushkinWordTwoOdd_of_odd` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Exact.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Exact.lean#L137)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ProfiniteProPGroups/STATUS.md)
