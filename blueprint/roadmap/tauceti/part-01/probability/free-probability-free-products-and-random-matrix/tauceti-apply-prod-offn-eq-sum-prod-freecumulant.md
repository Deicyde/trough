---
declaration: theorem
origin: cited
lean: TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant
statement: formalized
proof: formalized
---

# TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant

The *moment–cumulant formula* for a word `a₁, …, aₙ` with `n ≥ 1` in multiplicative form:
`φ (a₁ * ⋯ * aₙ) = ∑_{π ∈ NC(n)} ∏_{B ∈ π} κ_B(a₁, …, aₙ)`.

```lean
TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant.{u_1, u_2} {R : Type u_1} {A : Type u_2}
  [CommRing R] [Monoid A] (φ : A → R) {n : ℕ} (hn : n ≠ 0) (a : Fin n → A) :
  φ (List.ofFn a).prod = ∑ π, ∏ B ∈ (↑π).parts, TauCeti.freeCumulant φ a B
```

## Depends on

- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant).

## Sources

- [Tau Ceti documentation: `TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant)
- [Source of `TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant` in TauCeti/Probability/FreeProbability/Cumulant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Cumulant/Basic.lean#L326)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
