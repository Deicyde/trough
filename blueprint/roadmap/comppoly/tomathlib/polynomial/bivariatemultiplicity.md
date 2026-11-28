---
catalog: module
lean: Polynomial.Bivariate.rootMultiplicity₀, Polynomial.Bivariate.shift, Polynomial.Bivariate.rootMultiplicity, Polynomial.Bivariate.rootMultiplicity₀_ge_iff, Polynomial.Bivariate.discr_y
statement: formalized
proof: formalized
---

# Mathlib-Facing Bivariate Multiplicity Helpers

`CompPoly.ToMathlib.Polynomial.BivariateMultiplicity`, in [CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean), by Quang Dao.

> This file collects multiplicity- and discriminant-oriented helpers for Mathlib's
> bivariate polynomial surface `R[X][Y]`.

`Polynomial.Bivariate.rootMultiplicity₀` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean#L34))

> Root multiplicity of a bivariate polynomial at the origin.

```lean
def rootMultiplicity₀ [DecidableEq F] (f : F[X][Y]) : Option ℕ
```

`Polynomial.Bivariate.shift` (definition, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean#L51))

> Shift a bivariate polynomial by `(x, y)`.

```lean
def shift (f : F[X][Y]) (x y : F) : F[X][Y]
```

`Polynomial.Bivariate.rootMultiplicity` (definition, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean#L57))

> Root multiplicity (order of vanishing) of a bivariate polynomial at `(x, y)`.

```lean
def rootMultiplicity (f : F[X][Y]) (x y : F) : Option ℕ
```

`Polynomial.Bivariate.rootMultiplicity₀_ge_iff` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean#L62))

> `rootMultiplicity₀ g` is at least `r` (vacuously so when `g = 0`, where it is `none`)
> iff every coefficient of total degree `< r` vanishes.

```lean
theorem rootMultiplicity₀_ge_iff (g : F[X][Y]) (r : ℕ) :
    (∀ i j, i + j < r → coeff g i j = 0) ↔ ∀ m ∈ rootMultiplicity₀ g, r ≤ m
```

`Polynomial.Bivariate.discr_y` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean#L117))

> A discriminant-like helper in the outer `Y` variable.
>
> Unlike Mathlib's univariate `discr`, this returns `0` for constant bivariate polynomials.

```lean
def discr_y (f : F[X][Y]) : F[X]
```

## Depends on

- [Mathlib-Facing Bivariate Degree Helpers](bivariatedegree.md)

## Sources

- [CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/ToMathlib/Polynomial/BivariateMultiplicity.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.ToMathlib.Polynomial.BivariateMultiplicity.json)
