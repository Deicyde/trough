---
declaration: theorem
origin: cited
lean: Nat.card_filter_not_dvd_choose
statement: formalized
proof: formalized
---

# Fine's theorem

The number of `k ≤ n` for which `p ∤ n choose k` is `∏ⱼ (nⱼ + 1)`, the
product over the base-`p` digits `nⱼ` of `n`.

```lean
Nat.card_filter_not_dvd_choose {p : ℕ} [hp : Fact (Nat.Prime p)] (n : ℕ) :
  {k ∈ Finset.range (n + 1) | ¬p ∣ n.choose k}.card = (List.map (fun x => x + 1) (p.digits n)).prod
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lucas' theorem for divisibility, one digit at a time](lucas-theorem-for-divisibility-one-digit-at-a-ti.md)

## Lean

Formalized in Tau Ceti as [`Nat.card_filter_not_dvd_choose`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Choose/Digits.html#Nat.card_filter_not_dvd_choose).

## Sources

- [Tau Ceti documentation: `Nat.card_filter_not_dvd_choose`](https://taucetiproject.org/docs/TauCeti/Data/Nat/Choose/Digits.html#Nat.card_filter_not_dvd_choose)
- [Source of `Nat.card_filter_not_dvd_choose` in TauCeti/Data/Nat/Choose/Digits.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Data/Nat/Choose/Digits.lean#L99)
