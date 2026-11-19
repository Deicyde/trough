---
catalog: module
lean: NonBinaryField, two_mul_inv_two, inv_two_mul_two, coeffs_of_comp_minus_x, comp_x_square_coeff, eq_poly_deg_one
statement: formalized
proof: formalized
---

# Non-binary fields and polynomial utilities

`CompPoly.Fields.Basic`, in [CompPoly/Fields/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean), by František Silváši, Julian Sutherland, Ilia Vlasov.

> This module defines `NonBinaryField` (fields with char ≠ 2) and provides lemmas about
> polynomial composition with `-X` and `X²`.

`NonBinaryField` (class, [line 22](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean#L22))

> A type class for fields of characteristic ≠ 2, extending `Field`.

```lean
class NonBinaryField (F : Type*) extends Field F where
  char_neq_2 : (2 : F) ≠ 0
```

`two_mul_inv_two` (lemma, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean#L34))

```lean
lemma two_mul_inv_two : (2 : F) * 2⁻¹ = 1
```

`inv_two_mul_two` (lemma, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean#L37))

```lean
lemma inv_two_mul_two : 2⁻¹ * (2 : F) = 1
```

`coeffs_of_comp_minus_x` (theorem, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean#L55))

```lean
theorem coeffs_of_comp_minus_x {f : Polynomial F} {n : ℕ} :
    (f.comp (-X)).coeff n = if Even n then f.coeff n else -f.coeff n
```

`comp_x_square_coeff` (theorem, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean#L79))

```lean
theorem comp_x_square_coeff {f : Polynomial F} {n : ℕ} :
    (f.comp (X * X)).coeff n = if Even n then f.coeff (n / 2) else 0
```

`eq_poly_deg_one` (lemma, [line 90](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean#L90))

```lean
lemma eq_poly_deg_one {a b c d : F} {x₁ x₂ : F}
    (h1 : a + b * x₁ = c + d * x₁)
    (h2 : a + b * x₂ = c + d * x₂)
    (h1_2 : x₁ ≠ x₂) :
    Polynomial.C a + Polynomial.C b * Polynomial.X =
      Polynomial.C c + Polynomial.C d * Polynomial.X
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Fields/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Fields/Basic.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Fields.Basic.json)
