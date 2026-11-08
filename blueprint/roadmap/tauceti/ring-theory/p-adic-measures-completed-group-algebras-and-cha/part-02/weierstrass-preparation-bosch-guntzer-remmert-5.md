---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq, TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq
statement: formalized
proof: formalized
---

# Weierstrass preparation (Bosch–Güntzer–Remmert §5.2.2, Theorem 1)

Over a complete
ultrametric normed commutative ring with multiplicative norm, a restricted series `f`
distinguished of degree `s` at a positive radius `c`, whose coefficient in degree `s` is a unit,
is a unit of the ring of restricted series times a monic polynomial of degree `s`:

```text
f = e * ω,    e a unit,    ω monic of degree s.
```

Over a field the unit condition is automatic, by
`TauCeti.PowerSeries.IsDistinguished.coeff_ne_zero`. The polynomial `ω` is then itself
distinguished of degree `s`, by `TauCeti.PowerSeries.IsDistinguished.of_isUnit_mul`, so no bound
on its lower coefficients needs stating separately. With a multiplicative norm, `f` is
multiplicatively distinguished, so this is
`TauCeti.PowerSeries.IsMulDistinguished.exists_isNormMulUnit_isMonicOfDegree_mul_eq`. The
factorization is unique by `TauCeti.PowerSeries.IsDistinguished.eq_and_eq_of_mul_eq_mul`.

```lean
TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] [NormMulClass R] {c : ℝ} {s : ℕ} {f : PowerSeries R}
  [CompleteSpace R] (hf : TauCeti.PowerSeries.IsDistinguished c s f)
  (hu : IsUnit ((PowerSeries.coeff s) f)) (hc : 0 < c) (hfr : PowerSeries.IsRestricted c f) :
  ∃ e ω, IsUnit e ∧ ω.IsMonicOfDegree s ∧ ↑e * ↑ω = f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate in several variables](../../mv-power-series/the-weierstrass-division-estimate-in-several-var.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.html#TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq).

## Other forms

**Weierstrass preparation (Bosch–Güntzer–Remmert §5.2.2, Theorem 1), in its unique-existence form.** Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.html#TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq).

```lean
TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] [NormMulClass R] {c : ℝ} {s : ℕ} {f : PowerSeries R}
  [CompleteSpace R] (hf : TauCeti.PowerSeries.IsDistinguished c s f)
  (hu : IsUnit ((PowerSeries.coeff s) f)) (hc : 0 < c) (hfr : PowerSeries.IsRestricted c f) :
  ∃! p, IsUnit p.1 ∧ p.2.IsMonicOfDegree s ∧ ↑p.1 * ↑p.2 = f
```

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.html#TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq)
- [Source of `TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq` in TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.lean#L428)
