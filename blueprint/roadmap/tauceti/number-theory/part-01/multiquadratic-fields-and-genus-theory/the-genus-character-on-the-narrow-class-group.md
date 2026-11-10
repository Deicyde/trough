---
declaration: def
origin: cited
lean: TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom
statement: formalized
---

# The genus character on the narrow class group

For a factor `t` of a prime-discriminant factorization, this is the homomorphism
`Cl⁺(K) → ℤˣ` obtained by evaluating a coprime integral representative. Its definition is
independent of the representative by `genusCharFunCoprimeIdealHom_eq_of_mk0_eq`.

```lean
TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {θ : NumberField.RingOfIntegers K} {d : ℤ} {s t : Finset ℤ}
  (hs : ∀ P ∈ s, TauCeti.Multiquadratic.IsPrimeDiscriminant P)
  (heven :
    ∀ P ∈ s,
      ∀ P' ∈ s,
        TauCeti.Multiquadratic.IsEvenPrimeDiscriminant P →
          TauCeti.Multiquadratic.IsEvenPrimeDiscriminant P' → P = P')
  (hprod : ∏ P ∈ s, P = TauCeti.Multiquadratic.fundamentalDiscriminant d)
  (hmin : minpoly ℤ θ = Polynomial.X ^ 2 - Polynomial.C d) (hgen : ℚ[↑θ] = ⊤) (hsf : Squarefree d)
  (hts : t ⊆ s) : NumberField.NarrowClassGroup K →* ℤˣ
```

## Depends on

- [NumberField.NarrowClassGroup](numberfield-narrowclassgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/NarrowClassGroup.html#TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/NarrowClassGroup.html#TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom)
- [Source of `TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom` in TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/NarrowClassGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/NarrowClassGroup.lean#L128)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Multiquadratic/STATUS.md)
