---
declaration: def
origin: cited
lean: TauCeti.freeCumulant
statement: formalized
---

# TauCeti.freeCumulant

The *free cumulant* `κ_s(a)` of the word `(a_i)_{i ∈ s}`: the cumulant of the partition of
`s` into one part. For `s = Finset.univ : Finset (Fin n)` with `n ≥ 1` this is the `n`-th free
cumulant `κ_n(a₁, …, aₙ)`; for `s = ∅` it is the meaningless value `1`.

```lean
TauCeti.freeCumulant.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2} {α : Type u_3} [LinearOrder α]
  [CommRing R] [Monoid A] (φ : A → R) (a : α → A) (s : Finset α) : R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.freeCumulant).

## Sources

- [Tau Ceti documentation: `TauCeti.freeCumulant`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Cumulant/Basic.html#TauCeti.freeCumulant)
- [Source of `TauCeti.freeCumulant` in TauCeti/Probability/FreeProbability/Cumulant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/FreeProbability/Cumulant/Basic.lean#L168)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FreeProbability/STATUS.md)
