---
declaration: theorem
origin: cited
lean: TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_even
statement: formalized
proof: formalized
---

# The existence theorem of the classification of Demushkin groups for even rank, as an equivalence (Labute, Theorem 1 and Remark 2; Serre, Theorem 3.2)

Let `n` be even and let
`A ≤ ℤ_pˣ` be a closed pro-`p` subgroup. Then `(n, A)` is the pair of invariants `(rank, Im χ)` of
a Demushkin group, presented on `n` generators by one relator, exactly when `(A : A^p) < p ^ n` as
supernatural numbers. At `p = 2` the condition excludes exactly `n = 0` and the non-procyclic images
`{±1} × U^(f)` in rank two; at an odd prime it excludes exactly `n = 0`. Together with
`TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_odd`, this is the full list of the
pairs of invariants of Demushkin groups.

```lean
TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_even {p : ℕ} [hp : Fact (Nat.Prime p)]
  {n : ℕ} (hn : Even n) {A : Subgroup ℤ_[p]ˣ} (hA : IsClosed ↑A) (hAp : TauCeti.IsProP p ↥A) :
  (∃ r,
      ∃ (hG : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r})),
        TauCeti.demushkinRank hG = n ∧ (TauCeti.demushkinCharacter hG).range = A) ↔
    ((Subgroup.map (powMonoidHom p) A).subgroupOf A).profiniteIndex <
      TauCeti.Supernatural.primePower ⟨p, ⋯⟩ ↑n
```

## Depends on

- [The Demushkin predicate](../../profinite-and-pro-p-groups/part-01/the-demushkin-predicate.md)

## Proof depends on

- [Burnside's basis theorem, cardinal form](burnsides-basis-theorem-cardinal-form.md)
- [The existence theorem of the classification of Demushkin groups, rank one (Labute, Remark 2 (iii); NSW (3.9.10))](../../profinite-and-pro-p-groups/part-01/the-existence-theorem-of-the-classification-of-d.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)](../../profinite-and-pro-p-groups/part-02/the-necessity-half-of-the-existence-theorem-for.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_even`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Image.html#TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_even).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_even`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Image.html#TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_even)
- [Source of `TauCeti.exists_isDemushkin_range_demushkinCharacter_eq_iff_of_even` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Image.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Two/Even/Image.lean#L173)
