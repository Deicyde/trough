---
declaration: theorem
origin: cited
lean: TauCeti.const_mul_schwarzChristoffelPrimitive_two_neg_one_add_eq_log
statement: formalized
proof: formalized
---

# The explicit Schwarz--Christoffel formula for a strip

Two distinct prevertices
of exponent `-1` give the principal logarithm of their fractional-linear ratio, after
scaling by their separation and translating by the value at the base point.

```lean
TauCeti.const_mul_schwarzChristoffelPrimitive_two_neg_one_add_eq_log (a : Fin 2 → ℝ)
  (ha : a 0 ≠ a 1) (z₀ : UpperHalfPlane) {z : ℂ} (hz : z ∈ UpperHalfPlane.upperHalfPlaneSet) :
  (↑(a 1) - ↑(a 0)) * TauCeti.schwarzChristoffelPrimitive a (fun x => -1) z₀ z +
      Complex.log ((↑z₀ - ↑(a 1)) / (↑z₀ - ↑(a 0))) =
    Complex.log ((z - ↑(a 1)) / (z - ↑(a 0)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.const_mul_schwarzChristoffelPrimitive_two_neg_one_add_eq_log`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/Strip.html#TauCeti.const_mul_schwarzChristoffelPrimitive_two_neg_one_add_eq_log).

## Sources

- [Tau Ceti documentation: `TauCeti.const_mul_schwarzChristoffelPrimitive_two_neg_one_add_eq_log`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/Strip.html#TauCeti.const_mul_schwarzChristoffelPrimitive_two_neg_one_add_eq_log)
- [Source of `TauCeti.const_mul_schwarzChristoffelPrimitive_two_neg_one_add_eq_log` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/Strip.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/MultipleEnds/Strip.lean#L40)
