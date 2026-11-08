---
declaration: theorem
origin: cited
lean: TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd
statement: formalized
proof: formalized
---

# The existence theorem of the classification for odd rank, as an equivalence (Labute, Theorem 1 and Remark 2; Serre, Theorem 3.2)

Let `n` be odd and let `A ≤ ℤ₂ˣ` be a subgroup. Then
`(n, A)` is the pair of invariants of a Demushkin group, presented on `n` generators by one relator,
exactly when `A = {±1}`, or `n ≥ 3` and `A = {±1} × U^(f)` for some `f ≥ 2`. At `n = 1` the only
admissible image is `{±1}`, the image of the canonical character of `ℤ/2`. Every such `A` is
closed and pro-`2`, so no hypothesis on `A` is needed.

```lean
TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd {n : ℕ} (hn : Odd n)
  {A : Subgroup ℤ_[2]ˣ} :
  (∃ r,
      ∃ (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r})),
        TauCeti.demushkinRank hG = n ∧ (TauCeti.demushkinCharacter hG).range = A) ↔
    A = Subgroup.zpowers (-1) ∨ 3 ≤ n ∧ ∃ f, 2 ≤ f ∧ A = TauCeti.unitsPlusMinus f
```

## Depends on

- [The Demushkin predicate](../../profinite-and-pro-p-groups/the-demushkin-predicate.md)

## Proof depends on

- [Burnside's basis theorem, cardinal form](burnsides-basis-theorem-cardinal-form.md)
- [The existence theorem of the classification of Demushkin groups, rank one (Labute, Remark 2 (iii); NSW (3.9.10))](../../profinite-and-pro-p-groups/the-existence-theorem-of-the-classification-of-d.md)
- [Labute's Theorem 2](../../profinite-and-pro-p-groups/labutes-theorem-2.md)
- [The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)](../../profinite-and-pro-p-groups/the-necessity-half-of-the-existence-theorem-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Image.html#TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Image.html#TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd)
- [Source of `TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Image.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Odd/Image.lean#L228)
