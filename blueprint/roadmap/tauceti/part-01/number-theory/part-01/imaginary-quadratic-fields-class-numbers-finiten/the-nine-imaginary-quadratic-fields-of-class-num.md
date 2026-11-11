---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.classNumber_eq_one_of_mem_heegnerDiscriminants
statement: formalized
proof: formalized
---

# The nine imaginary quadratic fields of class number one

A quadratic field of
discriminant `-n`, for `n` one of `3, 4, 7, 8, 11, 19, 43, 67, 163`, has class number one: the
principal form is the only primitive reduced form of discriminant `-n`.

```lean
TauCeti.NumberField.classNumber_eq_one_of_mem_heegnerDiscriminants.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (hK : Module.finrank ℚ K = 2) {n : ℕ} (hn : NumberField.discr K = -↑n)
  (hmem : n ∈ TauCeti.heegnerDiscriminants) : NumberField.classNumber K = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ideal representatives of the Picard group](ideal-representatives-of-the-picard-group.md)
- [The order `ℤ + f 𝓞 K`](the-order-z-f-o-k.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.classNumber_eq_one_of_mem_heegnerDiscriminants`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/HeegnerNumbers.html#TauCeti.NumberField.classNumber_eq_one_of_mem_heegnerDiscriminants).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.classNumber_eq_one_of_mem_heegnerDiscriminants`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/HeegnerNumbers.html#TauCeti.NumberField.classNumber_eq_one_of_mem_heegnerDiscriminants)
- [Source of `TauCeti.NumberField.classNumber_eq_one_of_mem_heegnerDiscriminants` in TauCeti/NumberTheory/ClassNumberOne/HeegnerNumbers.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassNumberOne/HeegnerNumbers.lean#L131)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
