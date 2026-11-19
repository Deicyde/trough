---
declaration: theorem
origin: cited
lean: TauCeti.kepler_radialPeriod
statement: formalized
proof: formalized
---

# Kepler's third law

For distinct turning points `0 < r₁ < r₂` of a Kepler orbit, the
quadrature `radialPeriod` equals `2π √(m / κ) a^(3/2)` for `a = (r₁ + r₂) / 2`. For `ℓ ≠ 0` this is
the time of a radial oscillation between `r₁` and `r₂`. For `ℓ = 0` the turning points force
`E = κ = 0`, so there is no motion between them; both sides are then `0`, by the convention
`x / 0 = 0` (the integrand `m / 0` and `√(m / 0)`).

```lean
TauCeti.kepler_radialPeriod {m κ ℓ E r₁ r₂ : ℝ} (hm : 0 < m) (h₁ : 0 < r₁) (hlt : r₁ < r₂)
  (hr₁ : 2 * m * (E + κ / r₁) = ℓ ^ 2 / r₁ ^ 2) (hr₂ : 2 * m * (E + κ / r₂) = ℓ ^ 2 / r₂ ^ 2) :
  TauCeti.radialPeriod m (fun r => -κ / r) ℓ E r₁ r₂ =
    2 * Real.pi * √(m / κ) * ((r₁ + r₂) / 2) ^ (3 / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vieta's formula for the Kepler sum of turning points](../part-02/vietas-formula-for-the-kepler-sum-of-turning-poi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.kepler_radialPeriod`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.html#TauCeti.kepler_radialPeriod).

## Sources

- [Tau Ceti documentation: `TauCeti.kepler_radialPeriod`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.html#TauCeti.kepler_radialPeriod)
- [Source of `TauCeti.kepler_radialPeriod` in TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/RadialAction.lean#L279)
