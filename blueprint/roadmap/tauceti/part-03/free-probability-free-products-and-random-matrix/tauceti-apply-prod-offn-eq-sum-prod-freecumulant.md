---
declaration: theorem
origin: cited
lean: TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant
statement: formalized
proof: formalized
---

# TauCeti.apply\_prod\_ofFn\_eq\_sum\_prod\_freeCumulant

The *moment–cumulant formula* for a word `a₁, …, aₙ` with `n ≥ 1` in multiplicative form:
`φ (a₁ * ⋯ * aₙ) = ∑_{π ∈ NC(n)} ∏_{B ∈ π} κ_B(a₁, …, aₙ)`.

```lean
TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant.{u_1, u_2} {R : Type u_1} {A : Type u_2}
  [CommRing R] [Monoid A] (φ : A → R) {n : ℕ} (hn : n ≠ 0) (a : Fin n → A) :
  φ (List.ofFn a).prod = ∑ π, ∏ B ∈ (↑π).parts, TauCeti.freeCumulant φ a B
```

## Depends on

- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Proof depends on

- [TauCeti.partitionCumulant\_eq\_prod\_freeCumulant](tauceti-partitioncumulant-eq-prod-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant).

## Sources

- [Tau Ceti documentation: `TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant)
- [Source of `TauCeti.apply_prod_ofFn_eq_sum_prod_freeCumulant` in TauCeti/Probability/FreeProbability/Cumulant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/FreeProbability/Cumulant/Basic.lean#L326)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeProbability/STATUS.md)
