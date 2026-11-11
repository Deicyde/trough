---
declaration: theorem
origin: cited
lean: IsCyclic.card_filter_dvd_orderOf_eq_mul_prod_primeFactors, IsAddCyclic.card_filter_dvd_addOrderOf_eq_add_sum_primeFactors
statement: formalized
proof: formalized
---

# Euler's product formula for the elements of order divisible by `f`

For `f` dividing the
order `h` of a cyclic group, the elements of order divisible by `f` are a proportion
`∏ p ∣ f, (1 - p ^ -(v_p h - v_p f + 1))` of the group, the product running over the primes of
`f`.

```lean
IsCyclic.card_filter_dvd_orderOf_eq_mul_prod_primeFactors.{u_1} {α : Type u_1} [Group α] [Fintype α]
  [IsCyclic α] {f : ℕ} (hf : f ∣ Fintype.card α) :
  ↑{τ | f ∣ orderOf τ}.card =
    ↑(Fintype.card α) *
      ∏ p ∈ f.primeFactors,
        (1 - (↑p ^ ((Fintype.card α).factorization p - f.factorization p + 1))⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsCyclic.card_filter_dvd_orderOf_eq_mul_prod_primeFactors`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Cyclic/OrderCount.html#IsCyclic.card_filter_dvd_orderOf_eq_mul_prod_primeFactors).

## Other forms

**Euler's product formula for the elements of additive order divisible by `f`.** Formalized in Tau Ceti as [`IsAddCyclic.card_filter_dvd_addOrderOf_eq_add_sum_primeFactors`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Cyclic/OrderCount.html#IsAddCyclic.card_filter_dvd_addOrderOf_eq_add_sum_primeFactors).

```lean
IsAddCyclic.card_filter_dvd_addOrderOf_eq_add_sum_primeFactors.{u_1} {α : Type u_1} [AddGroup α]
  [Fintype α] [IsAddCyclic α] {f : ℕ} (hf : f ∣ Fintype.card α) :
  ↑{τ | f ∣ addOrderOf τ}.card =
    ↑(Fintype.card α) *
      ∏ p ∈ f.primeFactors,
        (1 - (↑p ^ ((Fintype.card α).factorization p - f.factorization p + 1))⁻¹)
```

## Sources

- [Tau Ceti documentation: `IsCyclic.card_filter_dvd_orderOf_eq_mul_prod_primeFactors`](https://taucetiproject.org/docs/TauCeti/GroupTheory/SpecificGroups/Cyclic/OrderCount.html#IsCyclic.card_filter_dvd_orderOf_eq_mul_prod_primeFactors)
- [Source of `IsCyclic.card_filter_dvd_orderOf_eq_mul_prod_primeFactors` in TauCeti/GroupTheory/SpecificGroups/Cyclic/OrderCount.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/SpecificGroups/Cyclic/OrderCount.lean#L227)
