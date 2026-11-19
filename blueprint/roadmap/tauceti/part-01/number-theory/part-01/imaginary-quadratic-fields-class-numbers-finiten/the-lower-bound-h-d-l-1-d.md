---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.sqrt_mul_LFunction_one_re_div_le_classNumber
statement: formalized
proof: formalized
---

# The lower bound `h ≥ √|D| L(1, χ_D) / π`

If `K` is imaginary quadratic of discriminant
`D`, then its class number `h` is at least `√|D| L(1, χ_D) / π`, read for the real part of
`L(1, χ_D)`. This is the class number formula with the number of units bounded below by `2`.

```lean
TauCeti.NumberField.sqrt_mul_LFunction_one_re_div_le_classNumber.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (hK : Module.finrank ℚ K = 2) [NumberField.IsTotallyComplex K] :
  √|↑(NumberField.discr K)| *
        (DirichletCharacter.LFunction
            (MulChar.ringHomComp
              (TauCeti.Multiquadratic.fundamentalDiscriminantChar (NumberField.discr K) ⋯)
              (Int.castRingHom ℂ))
            1).re /
      Real.pi ≤
    ↑(NumberField.classNumber K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic class number formula of an imaginary quadratic field](the-analytic-class-number-formula-of-an-imaginar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.sqrt_mul_LFunction_one_re_div_le_classNumber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.html#TauCeti.NumberField.sqrt_mul_LFunction_one_re_div_le_classNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.sqrt_mul_LFunction_one_re_div_le_classNumber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.html#TauCeti.NumberField.sqrt_mul_LFunction_one_re_div_le_classNumber)
- [Source of `TauCeti.NumberField.sqrt_mul_LFunction_one_re_div_le_classNumber` in TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/Quadratic/DedekindZeta.lean#L316)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
