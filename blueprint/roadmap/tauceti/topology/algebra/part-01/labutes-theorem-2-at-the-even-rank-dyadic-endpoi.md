---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one
statement: formalized
proof: formalized
---

# Labute's Theorem 2 at the even-rank dyadic endpoint

Let `r, r' ∈ Φ(F)` be relators of the
free pro-`2` group on an even number `n` of generators presenting Demushkin groups whose canonical
characters both have image `{±1}`. Then a continuous automorphism of `F` carries `r` to `r'`; in
particular the closed normal closures of `r` and `r'` are carried to each other.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one {n : ℕ}
  (hn : Even n) {r r' : TauCeti.freeProP 2 (Fin n)}
  (hr : r ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hr' : r' ∈ TauCeti.proPFrattini 2 (TauCeti.freeProP 2 (Fin n)))
  (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r}))
  (hG' : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r'}))
  (hA : (TauCeti.demushkinCharacter hG).range = Subgroup.zpowers (-1))
  (hA' : (TauCeti.demushkinCharacter hG').range = Subgroup.zpowers (-1)) : ∃ e, e r = r'
```

## Depends on

- [The Demushkin predicate](../../profinite-and-pro-p-groups/part-01/the-demushkin-predicate.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's criterion](../../profinite-and-pro-p-groups/part-01/labutes-criterion.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [The relative successive-approximation theorem](../../profinite-and-pro-p-groups/part-02/the-relative-successive-approximation-theorem.md)
- [The successive-approximation theorem with tails](../part-02/the-successive-approximation-theorem-with-tails.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Endpoint.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Endpoint.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_eq_zpowers_neg_one` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Endpoint.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Endpoint.lean#L107)
