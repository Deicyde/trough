---
declaration: theorem
origin: cited
lean: TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq, TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq
statement: formalized
proof: formalized
---

# Weierstrass preparation

**Weierstrass preparation** (Bosch–Güntzer–Remmert §5.2.2, Theorem 1), in its unique-existence
form: over a complete ultrametric normed commutative ring with multiplicative norm, a restricted
series distinguished of degree `s` at a positive radius, whose coefficient in degree `s` is a unit,
is in exactly one way a unit of the ring of restricted series times a monic polynomial of degree
`s`.

```lean
TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] [NormMulClass R] {c : ℝ} {s : ℕ} {f : PowerSeries R}
  [CompleteSpace R] (hf : TauCeti.PowerSeries.IsDistinguished c s f)
  (hu : IsUnit ((PowerSeries.coeff s) f)) (hc : 0 < c) (hfr : PowerSeries.IsRestricted c f) :
  ∃! p, IsUnit p.1 ∧ p.2.IsMonicOfDegree s ∧ ↑p.1 * ↑p.2 = f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](the-weierstrass-division-estimate-bosch-guntzer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.html#TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq).

## Other forms

**Weierstrass preparation (Bosch–Güntzer–Remmert §5.2.2, Theorem 1).** Formalized in Tau Ceti as [`TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.html#TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq).

```lean
TauCeti.PowerSeries.IsDistinguished.exists_isUnit_isMonicOfDegree_mul_eq.{u_1} {R : Type u_1}
  [NormedCommRing R] [IsUltrametricDist R] [NormMulClass R] {c : ℝ} {s : ℕ} {f : PowerSeries R}
  [CompleteSpace R] (hf : TauCeti.PowerSeries.IsDistinguished c s f)
  (hu : IsUnit ((PowerSeries.coeff s) f)) (hc : 0 < c) (hfr : PowerSeries.IsRestricted c f) :
  ∃ e ω, IsUnit e ∧ ω.IsMonicOfDegree s ∧ ↑e * ↑ω = f
```

## Sources

- [Tau Ceti documentation: `TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.html#TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq)
- [Source of `TauCeti.PowerSeries.IsDistinguished.existsUnique_isUnit_isMonicOfDegree_mul_eq` in TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/PowerSeries/Weierstrass/Preparation.lean#L472)
