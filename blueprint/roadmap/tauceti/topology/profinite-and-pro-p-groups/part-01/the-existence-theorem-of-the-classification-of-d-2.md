---
declaration: theorem
origin: cited
lean: TauCeti.exists_isDemushkin_one_range_eq_zpowers_neg_one, TauCeti.exists_isDemushkin_range_eq_of_even_of_lt, TauCeti.exists_isDemushkin_range_eq_unitsPlusMinus_of_odd, TauCeti.exists_isDemushkin_range_eq_zpowers_neg_one_of_odd
statement: formalized
proof: formalized
---

# The existence theorem of the classification of Demushkin groups, rank one (Labute, Remark 2 (iii); NSW (3.9.10))

There is a Demushkin group of rank `1`, presented on one generator by
the single relator `x₁²`, namely `ℤ/2`, which has exactly one continuous character with the
prescription property, and that character has image `{±1}`. This is the instance `n = 1` of the
odd-rank statement at level `f = ∞`, whose relator word reads `x₁²` at rank one.

```lean
TauCeti.exists_isDemushkin_one_range_eq_zpowers_neg_one :
  ∃ r,
    ∃ (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin 1) {r})),
      TauCeti.demushkinRank hG = 1 ∧
        (∃! χ, TauCeti.HasPrescriptionProperty χ) ∧
          ∀ (χ : TauCeti.presentedProP 2 (Fin 1) {r} →ₜ* ℤ_[2]ˣ),
            TauCeti.HasPrescriptionProperty χ → χ.range = Subgroup.zpowers (-1)
```

## Depends on

- [The Demushkin predicate (Labute, p. 106), for a prime `p` and a topological group `G`](the-demushkin-predicate-labute-p-106-for-a-prime.md)

## Proof depends on

- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [Labute's classification of the closed subgroups of `ℤ_2ˣ`](../../../number-theory/part-02/padics/labutes-classification-of-the-closed-subgroups-o.md)
- [Labute's criterion](labutes-criterion.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isDemushkin_one_range_eq_zpowers_neg_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.exists_isDemushkin_one_range_eq_zpowers_neg_one).

## Other forms

**The existence theorem of the classification of Demushkin groups, even rank (Labute, Theorem 1 and Remark 2; Serre, Theorem 3.2).** Formalized in Tau Ceti as [`TauCeti.exists_isDemushkin_range_eq_of_even_of_lt`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.exists_isDemushkin_range_eq_of_even_of_lt).

```lean
TauCeti.exists_isDemushkin_range_eq_of_even_of_lt {p : ℕ} [hp : Fact (Nat.Prime p)] {n : ℕ}
  {A : Subgroup ℤ_[p]ˣ} (hA : IsClosed ↑A) (hAp : TauCeti.IsProP p ↥A) (hn : Even n)
  (hlt :
    ((Subgroup.map (powMonoidHom p) A).subgroupOf A).profiniteIndex <
      TauCeti.Supernatural.primePower ⟨p, ⋯⟩ ↑n) :
  ∃ r,
    ∃ (hG : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r})),
      TauCeti.demushkinRank hG = n ∧
        (∃! χ, TauCeti.HasPrescriptionProperty χ) ∧
          ∀ (χ : TauCeti.presentedProP p (Fin n) {r} →ₜ* ℤ_[p]ˣ),
            TauCeti.HasPrescriptionProperty χ → χ.range = A
```

**The existence theorem of the classification of Demushkin groups, odd rank `n ≥ 3` (Labute, Theorem 1; Serre, Theorem 3.2).** Formalized in Tau Ceti as [`TauCeti.exists_isDemushkin_range_eq_unitsPlusMinus_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.exists_isDemushkin_range_eq_unitsPlusMinus_of_odd).

```lean
TauCeti.exists_isDemushkin_range_eq_unitsPlusMinus_of_odd {n : ℕ} (hn : Odd n) (hn₃ : 3 ≤ n) {f : ℕ}
  (hf : 2 ≤ f) :
  ∃ r,
    ∃ (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r})),
      TauCeti.demushkinRank hG = n ∧
        (∃! χ, TauCeti.HasPrescriptionProperty χ) ∧
          ∀ (χ : TauCeti.presentedProP 2 (Fin n) {r} →ₜ* ℤ_[2]ˣ),
            TauCeti.HasPrescriptionProperty χ → χ.range = TauCeti.unitsPlusMinus f
```

**The existence theorem of the classification of Demushkin groups, odd rank at level `f = ∞` (Labute, Theorem 1 and Remark 2; Serre, Theorem 3.2).** Formalized in Tau Ceti as [`TauCeti.exists_isDemushkin_range_eq_zpowers_neg_one_of_odd`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.exists_isDemushkin_range_eq_zpowers_neg_one_of_odd).

```lean
TauCeti.exists_isDemushkin_range_eq_zpowers_neg_one_of_odd {n : ℕ} (hn : Odd n) :
  ∃ r,
    ∃ (hG : TauCeti.IsDemushkin 2 (TauCeti.presentedProP 2 (Fin n) {r})),
      TauCeti.demushkinRank hG = n ∧
        (∃! χ, TauCeti.HasPrescriptionProperty χ) ∧
          ∀ (χ : TauCeti.presentedProP 2 (Fin n) {r} →ₜ* ℤ_[2]ˣ),
            TauCeti.HasPrescriptionProperty χ → χ.range = Subgroup.zpowers (-1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isDemushkin_one_range_eq_zpowers_neg_one`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.html#TauCeti.exists_isDemushkin_one_range_eq_zpowers_neg_one)
- [Source of `TauCeti.exists_isDemushkin_one_range_eq_zpowers_neg_one` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Existence.lean#L521)
