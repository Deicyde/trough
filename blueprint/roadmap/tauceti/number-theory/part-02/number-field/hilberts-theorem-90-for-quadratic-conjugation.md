---
declaration: theorem
origin: cited
lean: NumberField.exists_ne_zero_mul_eq_mul_ringOfIntegersQuadraticConj
statement: formalized
proof: formalized
---

# Hilbert's Theorem 90 for quadratic conjugation

Let `σ` be the quadratic conjugation of a
quadratic number field and let `x y : 𝓞 K` with `x ≠ 0` have equal norms, `x σx = y σy`. Then there
is a nonzero `ε : 𝓞 K` with `x ε = y σε`; equivalently `y / x = ε / σε` is a "coboundary". The
construction is explicit: `ε = σx (x + y)` works unless `x + y = 0`, and then `ε = σx θ x` does.

```lean
NumberField.exists_ne_zero_mul_eq_mul_ringOfIntegersQuadraticConj.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {θ : NumberField.RingOfIntegers K} {d : ℤ}
  (hmin : minpoly ℤ θ = Polynomial.X ^ 2 - Polynomial.C d) (hgen : ℚ[↑θ] = ⊤)
  {x y : NumberField.RingOfIntegers K} (hx : x ≠ 0)
  (hnorm :
    x * (NumberField.ringOfIntegersQuadraticConj hmin hgen) x =
      y * (NumberField.ringOfIntegersQuadraticConj hmin hgen) y) :
  ∃ ε, ε ≠ 0 ∧ x * ε = y * (NumberField.ringOfIntegersQuadraticConj hmin hgen) ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.exists_ne_zero_mul_eq_mul_ringOfIntegersQuadraticConj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/Conjugation/Hilbert90.html#NumberField.exists_ne_zero_mul_eq_mul_ringOfIntegersQuadraticConj).

## Sources

- [Tau Ceti documentation: `NumberField.exists_ne_zero_mul_eq_mul_ringOfIntegersQuadraticConj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Quadratic/Conjugation/Hilbert90.html#NumberField.exists_ne_zero_mul_eq_mul_ringOfIntegersQuadraticConj)
- [Source of `NumberField.exists_ne_zero_mul_eq_mul_ringOfIntegersQuadraticConj` in TauCeti/NumberTheory/NumberField/Quadratic/Conjugation/Hilbert90.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Quadratic/Conjugation/Hilbert90.lean#L32)
