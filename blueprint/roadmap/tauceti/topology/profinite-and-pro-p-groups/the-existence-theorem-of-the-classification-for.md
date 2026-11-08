---
declaration: theorem
origin: cited
lean: TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff
statement: formalized
proof: formalized
---

# The existence theorem of the classification for `q ≠ 2`, as an equivalence (Labute, Theorem 1 and Remark 2; Demushkin and Serre)

Let `A ≤ ℤ_pˣ` be a closed pro-`p` subgroup,
contained in `1 + 4ℤ_2` when `p = 2`; these are the possible images of the canonical characters of
the Demushkin groups with `q ≠ 2`
(`TauCeti.demushkinQ_ne_two_iff_range_demushkinCharacter_le`). Then `(n, A)` is the pair of
invariants of a Demushkin group, presented on `n` generators by one relator, exactly when `n` is
even and `(A : A^p) < p ^ n`. Together with
`TauCeti.IsDemushkin.nonempty_continuousMulEquiv_of_range_demushkinCharacter_eq`, this classifies
the Demushkin groups with `q ≠ 2` by their rank and the image of their canonical character.

```lean
TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff {p : ℕ} [hp : Fact (Nat.Prime p)] {n : ℕ}
  {A : Subgroup ℤ_[p]ˣ} (hA : IsClosed ↑A) (hAp : TauCeti.IsProP p ↥A)
  (hA₂ : p = 2 → A ≤ TauCeti.unitsPrincipal p 2) :
  (∃ r,
      ∃ (hG : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r})),
        TauCeti.demushkinRank hG = n ∧ (TauCeti.demushkinCharacter hG).range = A) ↔
    Even n ∧
      ((Subgroup.map (powMonoidHom p) A).subgroupOf A).profiniteIndex <
        TauCeti.Supernatural.primePower ⟨p, ⋯⟩ ↑n
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The existence theorem of the classification of Demushkin groups, rank one (Labute, Remark 2 (iii); NSW (3.9.10))](the-existence-theorem-of-the-classification-of-d.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [Labute's Theorem 2](labutes-theorem-2.md)
- [The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)](the-necessity-half-of-the-existence-theorem-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff)
- [Source of `TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.lean#L578)
