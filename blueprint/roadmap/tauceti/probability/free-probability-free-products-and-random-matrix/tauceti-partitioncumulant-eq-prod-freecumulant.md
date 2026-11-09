---
declaration: theorem
origin: cited
lean: TauCeti.partitionCumulant_eq_prod_freeCumulant
statement: formalized
proof: formalized
---

# TauCeti.partitionCumulant_eq_prod_freeCumulant

The free cumulants are *multiplicative*: the free cumulant of a noncrossing partition is the
product of the free cumulants of the words read along its parts, `κ_π(a) = ∏_{B ∈ π} κ_B(a)`.

```lean
TauCeti.partitionCumulant_eq_prod_freeCumulant.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2}
  {α : Type u_3} [LinearOrder α] {s : Finset α} [CommRing R] [Monoid A] (φ : A → R) (a : α → A)
  (π : TauCeti.NoncrossingPartition s) :
  TauCeti.partitionCumulant φ a π = ∏ B ∈ (↑π).parts, TauCeti.freeCumulant φ a B
```

## Depends on

- [TauCeti.freeCumulant](tauceti-freecumulant.md)

## Proof depends on

- [TauCeti.NoncrossingPartition.iicOrderIso](tauceti-noncrossingpartition-iicorderiso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.partitionCumulant_eq_prod_freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.partitionCumulant_eq_prod_freeCumulant).

## Sources

- [Tau Ceti documentation: `TauCeti.partitionCumulant_eq_prod_freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.partitionCumulant_eq_prod_freeCumulant)
- [Source of `TauCeti.partitionCumulant_eq_prod_freeCumulant` in TauCeti/Probability/FreeProbability/Cumulant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/FreeProbability/Cumulant/Basic.lean#L281)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FreeProbability/STATUS.md)
