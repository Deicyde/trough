---
declaration: theorem
origin: cited
lean: TauCeti.freeCumulant_fiberProd_eq_sum_prod
statement: formalized
proof: formalized
---

# TauCeti.freeCumulant_fiberProd_eq_sum_prod

*Free cumulants with products as arguments*, in multiplicative form:
`κ(fiberProd a s f) = ∑_{π ⊔ σ_f = 1_s} ∏_{B ∈ π} κ_B(a)`, where `σ_f` is the partition of `s`
into the fibres of `f`.

```lean
TauCeti.freeCumulant_fiberProd_eq_sum_prod.{u_1, u_2, u_3, u_4} {R : Type u_1} {A : Type u_2}
  {α : Type u_3} {β : Type u_4} [LinearOrder α] {s : Finset α} {f : α → β} [LinearOrder β]
  [CommRing R] [Monoid A] (φ : A → R) (a : α → A) (hf : MonotoneOn f ↑s) :
  TauCeti.freeCumulant φ (TauCeti.fiberProd a s f) (Finset.image f s) =
    ∑ π with π ⊔ (TauCeti.NoncrossingPartition.comap hf) ⊥ = ⊤,
      ∏ B ∈ (↑π).parts, TauCeti.freeCumulant φ a B
```

## Depends on

- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Proof depends on

- [TauCeti.partitionCumulant_eq_prod_freeCumulant](tauceti-partitioncumulant-eq-prod-freecumulant.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeCumulant_fiberProd_eq_sum_prod`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Product.html#TauCeti.freeCumulant_fiberProd_eq_sum_prod).

## Sources

- [Tau Ceti documentation: `TauCeti.freeCumulant_fiberProd_eq_sum_prod`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Product.html#TauCeti.freeCumulant_fiberProd_eq_sum_prod)
- [Source of `TauCeti.freeCumulant_fiberProd_eq_sum_prod` in TauCeti/Probability/FreeProbability/Cumulant/Product.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/FreeProbability/Cumulant/Product.lean#L162)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeProbability/STATUS.md)
