---
declaration: theorem
origin: cited
lean: TauCeti.kepler_kappa_eq, TauCeti.isotropicOscillator_sq_eq_sq_mul, TauCeti.isotropicOscillator_energy_eq, TauCeti.kepler_sq_eq_neg_two_mul_mul_mul
statement: formalized
proof: formalized
---

# Vieta's formula for the Kepler sum of turning points

If `r₁ ≠ r₂` are nonzero turning
points of a Kepler orbit with `m ≠ 0`, then `κ = -E (r₁ + r₂)`; equivalently, for `E ≠ 0` the
semi-major axis `(r₁ + r₂) / 2` is `κ / (-2 E)`.

```lean
TauCeti.kepler_kappa_eq {m κ ℓ E r₁ r₂ : ℝ} (hm : m ≠ 0) (h₁ : r₁ ≠ 0) (h₂ : r₂ ≠ 0) (hne : r₁ ≠ r₂)
  (hr₁ : 2 * m * (E + κ / r₁) = ℓ ^ 2 / r₁ ^ 2) (hr₂ : 2 * m * (E + κ / r₂) = ℓ ^ 2 / r₂ ^ 2) :
  κ = -E * (r₁ + r₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.kepler_kappa_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.html#TauCeti.kepler_kappa_eq).

## Other forms

**Vieta's formula for the isotropic oscillator, product of squared turning points.** Formalized in Tau Ceti as [`TauCeti.isotropicOscillator_sq_eq_sq_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.html#TauCeti.isotropicOscillator_sq_eq_sq_mul).

```lean
TauCeti.isotropicOscillator_sq_eq_sq_mul {m ν ℓ E r₁ r₂ : ℝ} (hm : m ≠ 0) (h₁ : r₁ ≠ 0)
  (h₂ : r₂ ≠ 0) (hne : r₁ ^ 2 ≠ r₂ ^ 2)
  (hr₁ : 2 * m * (E - m * ν ^ 2 * r₁ ^ 2 / 2) = ℓ ^ 2 / r₁ ^ 2)
  (hr₂ : 2 * m * (E - m * ν ^ 2 * r₂ ^ 2 / 2) = ℓ ^ 2 / r₂ ^ 2) : ℓ ^ 2 = (m * ν * (r₁ * r₂)) ^ 2
```

**Vieta's formula for the isotropic oscillator, sum of squared turning points.** Formalized in Tau Ceti as [`TauCeti.isotropicOscillator_energy_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.html#TauCeti.isotropicOscillator_energy_eq).

```lean
TauCeti.isotropicOscillator_energy_eq {m ν ℓ E r₁ r₂ : ℝ} (hm : m ≠ 0) (h₁ : r₁ ≠ 0) (h₂ : r₂ ≠ 0)
  (hne : r₁ ^ 2 ≠ r₂ ^ 2) (hr₁ : 2 * m * (E - m * ν ^ 2 * r₁ ^ 2 / 2) = ℓ ^ 2 / r₁ ^ 2)
  (hr₂ : 2 * m * (E - m * ν ^ 2 * r₂ ^ 2 / 2) = ℓ ^ 2 / r₂ ^ 2) :
  2 * E = m * ν ^ 2 * (r₁ ^ 2 + r₂ ^ 2)
```

**Vieta's formula for the Kepler product of turning points.** Formalized in Tau Ceti as [`TauCeti.kepler_sq_eq_neg_two_mul_mul_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.html#TauCeti.kepler_sq_eq_neg_two_mul_mul_mul).

```lean
TauCeti.kepler_sq_eq_neg_two_mul_mul_mul {m κ ℓ E r₁ r₂ : ℝ} (hm : m ≠ 0) (h₁ : r₁ ≠ 0)
  (h₂ : r₂ ≠ 0) (hne : r₁ ≠ r₂) (hr₁ : 2 * m * (E + κ / r₁) = ℓ ^ 2 / r₁ ^ 2)
  (hr₂ : 2 * m * (E + κ / r₂) = ℓ ^ 2 / r₂ ^ 2) : ℓ ^ 2 = -2 * m * E * (r₁ * r₂)
```

## Sources

- [Tau Ceti documentation: `TauCeti.kepler_kappa_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.html#TauCeti.kepler_kappa_eq)
- [Source of `TauCeti.kepler_kappa_eq` in TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.lean#L142)
