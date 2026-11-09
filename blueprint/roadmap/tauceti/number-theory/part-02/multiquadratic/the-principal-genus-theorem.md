---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.isSquare_iff_forall_genusCharFunNarrowClassGroupHom_eq_one
statement: formalized
proof: formalized
---

# The principal genus theorem

Let `K = ℚ(√d)` with `d` squarefree and let
`∏ P ∈ s, P = fundamentalDiscriminant d` be the prime-discriminant factorization of its
discriminant. A narrow ideal class of `K` is a square exactly when every genus character is
trivial on it; that is, the principal genus is the group of squares.

This is the classical statement that the genus characters cut out `Cl⁺(K)²` inside `Cl⁺(K)`.

```lean
TauCeti.Multiquadratic.isSquare_iff_forall_genusCharFunNarrowClassGroupHom_eq_one.{u_1}
  {K : Type u_1} [Field K] [NumberField K] {θ : NumberField.RingOfIntegers K} {d : ℤ} {s : Finset ℤ}
  (hs : ∀ P ∈ s, TauCeti.Multiquadratic.IsPrimeDiscriminant P)
  (heven :
    ∀ P ∈ s,
      ∀ P' ∈ s,
        TauCeti.Multiquadratic.IsEvenPrimeDiscriminant P →
          TauCeti.Multiquadratic.IsEvenPrimeDiscriminant P' → P = P')
  (hprod : ∏ P ∈ s, P = TauCeti.Multiquadratic.fundamentalDiscriminant d)
  (hmin : minpoly ℤ θ = Polynomial.X ^ 2 - Polynomial.C d) (hgen : ℚ[↑θ] = ⊤) (hsf : Squarefree d)
  (A : NumberField.NarrowClassGroup K) :
  IsSquare A ↔
    ∀ (P : ℤ) (hP : P ∈ s),
      (TauCeti.Multiquadratic.genusCharFunNarrowClassGroupHom hs heven hprod hmin hgen hsf ⋯) A = 1
```

## Depends on

- [The genus character on the narrow class group](../../part-01/multiquadratic-fields-and-genus-theory/the-genus-character-on-the-narrow-class-group.md)
- [NumberField.NarrowClassGroup](../../part-01/multiquadratic-fields-and-genus-theory/numberfield-narrowclassgroup.md)

## Proof depends on

- [The `2`-rank formula for the narrow class group of a quadratic field](../../part-01/multiquadratic-fields-and-genus-theory/the-2-rank-formula-for-the-narrow-class-group-of.md)
- [Dirichlet's theorem for prime-discriminant characters](dirichlets-theorem-for-prime-discriminant-charac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.isSquare_iff_forall_genusCharFunNarrowClassGroupHom_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/PrincipalGenus.html#TauCeti.Multiquadratic.isSquare_iff_forall_genusCharFunNarrowClassGroupHom_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.isSquare_iff_forall_genusCharFunNarrowClassGroupHom_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/PrincipalGenus.html#TauCeti.Multiquadratic.isSquare_iff_forall_genusCharFunNarrowClassGroupHom_eq_one)
- [Source of `TauCeti.Multiquadratic.isSquare_iff_forall_genusCharFunNarrowClassGroupHom_eq_one` in TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/PrincipalGenus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/Quadratic/GenusCharacter/PrincipalGenus.lean#L144)
