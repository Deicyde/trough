---
declaration: theorem
origin: cited
lean: TauCeti.mem_image_intCast_of_tschirnhausPolynomial_X_pow_four_eq
statement: formalized
proof: formalized
---

# The six values of `γ`

If the Tschirnhaus transform by `X⁴` of an integer cubic
`X³ + a X² + b X + c` is `X³ - γ X - 16`, then `γ` is one of `0, -32, -96, -960, -5280, -640320`.
These are the values of `γ₂` at the CM points of discriminants `-3, -11, -19, -43, -67, -163`.

```lean
TauCeti.mem_image_intCast_of_tschirnhausPolynomial_X_pow_four_eq.{u_1} {R : Type u_1} [CommRing R]
  [CharZero R] {a b c : ℤ} {γ : R}
  (h :
    (Polynomial.X ^ 3 + Polynomial.C ↑a * Polynomial.X ^ 2 + Polynomial.C ↑b * Polynomial.X +
            Polynomial.C ↑c).tschirnhausPolynomial
        (Polynomial.X ^ 4) =
      Polynomial.X ^ 3 - Polynomial.C γ * Polynomial.X - 16) :
  γ ∈ Int.cast '' {0, -32, -96, -960, -5280, -640320}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The integer points of the Heegner quartic](the-integer-points-of-the-heegner-quartic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_image_intCast_of_tschirnhausPolynomial_X_pow_four_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.html#TauCeti.mem_image_intCast_of_tschirnhausPolynomial_X_pow_four_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_image_intCast_of_tschirnhausPolynomial_X_pow_four_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.html#TauCeti.mem_image_intCast_of_tschirnhausPolynomial_X_pow_four_eq)
- [Source of `TauCeti.mem_image_intCast_of_tschirnhausPolynomial_X_pow_four_eq` in TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.lean#L313)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
