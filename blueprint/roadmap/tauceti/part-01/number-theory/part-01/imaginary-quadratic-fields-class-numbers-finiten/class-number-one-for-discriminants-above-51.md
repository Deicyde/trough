---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.classNumber_eq_one_iff_of_neg_fifty_one_lt_discr
statement: formalized
proof: formalized
---

# Class number one for discriminants above `-51`

A quadratic field of discriminant `-n`
with `-51 < -n` has class number one exactly when `n ∈ heegnerDiscriminants`, that is when its
discriminant is one of `-3, -4, -7, -8, -11, -19, -43`.

```lean
TauCeti.NumberField.classNumber_eq_one_iff_of_neg_fifty_one_lt_discr.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (hK : Module.finrank ℚ K = 2) {n : ℕ} (hn : NumberField.discr K = -↑n)
  (h51 : -51 < NumberField.discr K) :
  NumberField.classNumber K = 1 ↔ n ∈ TauCeti.heegnerDiscriminants
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ideal representatives of the Picard group](ideal-representatives-of-the-picard-group.md)
- [The order `ℤ + f 𝓞 K`](the-order-z-f-o-k.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.classNumber_eq_one_iff_of_neg_fifty_one_lt_discr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/SmallDiscriminant.html#TauCeti.NumberField.classNumber_eq_one_iff_of_neg_fifty_one_lt_discr).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.classNumber_eq_one_iff_of_neg_fifty_one_lt_discr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/SmallDiscriminant.html#TauCeti.NumberField.classNumber_eq_one_iff_of_neg_fifty_one_lt_discr)
- [Source of `TauCeti.NumberField.classNumber_eq_one_iff_of_neg_fifty_one_lt_discr` in TauCeti/NumberTheory/ClassNumberOne/SmallDiscriminant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassNumberOne/SmallDiscriminant.lean#L53)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
