---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.classNumber_eq_card_units_mul_LFunction_one
statement: formalized
proof: formalized
---

# The analytic class number formula of an imaginary quadratic field

If `K` is imaginary
quadratic of discriminant `D`, then `h = w √|D| L(1, χ_D) / (2π)`, where `h` is the class number
of `K`, `w` is the number of units of `𝓞 K` and `χ_D` is the complex quadratic character of
`D`.

```lean
TauCeti.NumberField.classNumber_eq_card_units_mul_LFunction_one.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (hK : Module.finrank ℚ K = 2) [NumberField.IsTotallyComplex K] :
  ↑(NumberField.classNumber K) =
    ↑(Nat.card (NumberField.RingOfIntegers K)ˣ) * ↑√|↑(NumberField.discr K)| *
        DirichletCharacter.LFunction
          (MulChar.ringHomComp
            (TauCeti.Multiquadratic.fundamentalDiscriminantChar (NumberField.discr K) ⋯)
            (Int.castRingHom ℂ))
          1 /
      (2 * ↑Real.pi)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.classNumber_eq_card_units_mul_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.html#TauCeti.NumberField.classNumber_eq_card_units_mul_LFunction_one).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.classNumber_eq_card_units_mul_LFunction_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.html#TauCeti.NumberField.classNumber_eq_card_units_mul_LFunction_one)
- [Source of `TauCeti.NumberField.classNumber_eq_card_units_mul_LFunction_one` in TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.lean#L276)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
