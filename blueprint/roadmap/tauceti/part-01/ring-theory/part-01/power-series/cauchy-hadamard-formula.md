---
declaration: theorem
origin: cited
lean: PowerSeries.radius_inv_eq_limsup, PowerSeries.radius_eq_liminf
statement: formalized
proof: formalized
---

# Cauchy–Hadamard formula

the inverse of the radius of `∑ aₙ Xⁿ` is
`limsup ‖aₙ‖ ^ (1 / n)`.

```lean
PowerSeries.radius_inv_eq_limsup.{u_1} {R : Type u_1} [NormedRing R] {f : PowerSeries R} :
  f.radius⁻¹ = Filter.limsup (fun n => ↑(‖(PowerSeries.coeff n) f‖₊ ^ (1 / ↑n))) Filter.atTop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.radius_inv_eq_limsup`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Radius.html#PowerSeries.radius_inv_eq_limsup).

## Other forms

**Cauchy–Hadamard formula, `liminf` form.** Formalized in Tau Ceti as [`PowerSeries.radius_eq_liminf`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Radius.html#PowerSeries.radius_eq_liminf).

```lean
PowerSeries.radius_eq_liminf.{u_1} {R : Type u_1} [NormedRing R] {f : PowerSeries R} :
  f.radius = Filter.liminf (fun n => 1 / ↑(‖(PowerSeries.coeff n) f‖₊ ^ (1 / ↑n))) Filter.atTop
```

## Sources

- [Tau Ceti documentation: `PowerSeries.radius_inv_eq_limsup`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Radius.html#PowerSeries.radius_inv_eq_limsup)
- [Source of `PowerSeries.radius_inv_eq_limsup` in TauCeti/RingTheory/PowerSeries/Radius.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/PowerSeries/Radius.lean#L187)
