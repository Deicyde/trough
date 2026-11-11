---
declaration: theorem
origin: cited
lean: TauCeti.quinticF20Spec_specialize_X_pow_five_add_C_mul_X_add_C, TauCeti.resolventSextic_X_pow_five_add_C_mul_X_add_C
statement: formalized
proof: formalized
---

# Dummit's formula for the resolvent of a quintic trinomial

Over every commutative ring,
the specialization of the quintic `F₂₀` specification at `X⁵ + aX + b` is
`X⁶ + 8aX⁵ + 40a²X⁴ + 160a³X³ + 400a⁴X² + (512a⁵ - 3125b⁴)X + (256a⁶ - 9375ab⁴)`.

```lean
TauCeti.quinticF20Spec_specialize_X_pow_five_add_C_mul_X_add_C.{u_1} {R : Type u_1} [CommRing R]
  (a b : R) :
  TauCeti.quinticF20Spec.specialize R
      (Polynomial.X ^ 5 + Polynomial.C a * Polynomial.X + Polynomial.C b) =
    Polynomial.X ^ 6 + Polynomial.C (8 * a) * Polynomial.X ^ 5 +
              Polynomial.C (40 * a ^ 2) * Polynomial.X ^ 4 +
            Polynomial.C (160 * a ^ 3) * Polynomial.X ^ 3 +
          Polynomial.C (400 * a ^ 4) * Polynomial.X ^ 2 +
        Polynomial.C (512 * a ^ 5 - 3125 * b ^ 4) * Polynomial.X +
      Polynomial.C (256 * a ^ 6 - 9375 * a * b ^ 4)
```

## Depends on

- [TauCeti.ResolventSpec](../galois-groups-of-polynomials/tauceti-resolventspec.md)

## Proof depends on

- [Vieta's formulas, in the form the symmetric descent uses](../galois-groups-of-polynomials/vietas-formulas-in-the-form-the-symmetric-descen.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.quinticF20Spec_specialize_X_pow_five_add_C_mul_X_add_C`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Trinomial.html#TauCeti.quinticF20Spec_specialize_X_pow_five_add_C_mul_X_add_C).

## Other forms

**Dummit's formula (2′) for the resolvent sextic of the integral quintic `X⁵ + aX + b`.** Formalized in Tau Ceti as [`TauCeti.resolventSextic_X_pow_five_add_C_mul_X_add_C`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Trinomial.html#TauCeti.resolventSextic_X_pow_five_add_C_mul_X_add_C).

```lean
TauCeti.resolventSextic_X_pow_five_add_C_mul_X_add_C (a b : ℤ) :
  TauCeti.resolventSextic (Polynomial.X ^ 5 + Polynomial.C a * Polynomial.X + Polynomial.C b) =
    Polynomial.X ^ 6 + Polynomial.C (8 * a) * Polynomial.X ^ 5 +
              Polynomial.C (40 * a ^ 2) * Polynomial.X ^ 4 +
            Polynomial.C (160 * a ^ 3) * Polynomial.X ^ 3 +
          Polynomial.C (400 * a ^ 4) * Polynomial.X ^ 2 +
        Polynomial.C (512 * a ^ 5 - 3125 * b ^ 4) * Polynomial.X +
      Polynomial.C (256 * a ^ 6 - 9375 * a * b ^ 4)
```

## Sources

- [Tau Ceti documentation: `TauCeti.quinticF20Spec_specialize_X_pow_five_add_C_mul_X_add_C`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Trinomial.html#TauCeti.quinticF20Spec_specialize_X_pow_five_add_C_mul_X_add_C)
- [Source of `TauCeti.quinticF20Spec_specialize_X_pow_five_add_C_mul_X_add_C` in TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Trinomial.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/GaloisGroups/Resolvent/Quintic/Trinomial.lean#L347)
