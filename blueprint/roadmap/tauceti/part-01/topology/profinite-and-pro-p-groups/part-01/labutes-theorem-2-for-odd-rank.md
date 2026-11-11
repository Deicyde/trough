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

- [Labute's normal form for `q = 2` and odd rank (Labute, Theorem 3, case (2))](labutes-normal-form-for-q-2-and-odd-rank-labute.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)](../part-02/the-necessity-half-of-the-existence-theorem-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_range_demushkinCharacter_eq_of_odd` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean#L106)
