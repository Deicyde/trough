---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd
statement: formalized
proof: formalized
---

# Labute's Theorem 2 for odd rank

Let `r, r' ∈ Φ(F)` be relators of the free pro-`2` group
on an odd number `n` of generators whose presented groups are Demushkin groups whose canonical
characters have the same image. Then a continuous automorphism of `F` carries `r` to `r'`; in
particular the closed normal closures of `r` and `r'` are carried to each other.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd {n : ℕ}
  (hn : Odd n) {r r' : TauCeti.freeProP 2 (Fin n)}
  (hr : r ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hr' : r' ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r}))
  (hG' : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r'}))
  (h : (TauCeti.demushkinCharacter hG).range = (TauCeti.demushkinCharacter hG').range) :
  ∃ e, e r = r'
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's criterion](labutes-criterion.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)](the-necessity-half-of-the-existence-theorem-for.md)
- [The relative successive-approximation theorem](../part-02/the-relative-successive-approximation-theorem.md)
- [The successive-approximation theorem with tails](../../algebra/part-02/the-successive-approximation-theorem-with-tails.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean#L106)
