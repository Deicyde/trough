---
declaration: theorem
origin: cited
lean: Polynomial.Separable.isSquare_discr_iff_sign_eq_one
statement: formalized
proof: formalized
---

# The discriminant test, intrinsically

For a separable polynomial over a field of
characteristic other than `2`, the discriminant is a square exactly when the parity character of
the Galois group is trivial. Unlike
`Polynomial.Separable.isSquare_discr_iff_range_le_alternatingGroup`, this mentions no splitting
extension; through `Polynomial.Gal.sign_eq_one_iff_range_le_alternatingGroup` it reads the parity
of the Galois image in any extension in which `f` splits.

```lean
Polynomial.Separable.isSquare_discr_iff_sign_eq_one.{u} {F : Type u} [Field F] {f : Polynomial F}
  (hsep : f.Separable) (hchar : ringChar F ≠ 2) : IsSquare f.discr ↔ Polynomial.Gal.sign f = 1
```

## Depends on

- [Polynomial.Gal.sign](polynomial-gal-sign.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.Separable.isSquare_discr_iff_sign_eq_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Discriminant/Basic.html#Polynomial.Separable.isSquare_discr_iff_sign_eq_one).

## Sources

- [Tau Ceti documentation: `Polynomial.Separable.isSquare_discr_iff_sign_eq_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Discriminant/Basic.html#Polynomial.Separable.isSquare_discr_iff_sign_eq_one)
- [Source of `Polynomial.Separable.isSquare_discr_iff_sign_eq_one` in TauCeti/FieldTheory/GaloisGroups/Discriminant/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/GaloisGroups/Discriminant/Basic.lean#L209)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PolynomialGaloisGroups/STATUS.md)
