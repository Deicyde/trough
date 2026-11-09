---
declaration: theorem
origin: cited
lean: TauCeti.AddCircle.denseRange_coe_add_mul_iff
statement: formalized
proof: formalized
---

# Kronecker's theorem for linear flows on tori

A line `t ↦ θ + t ν` in the torus
`(ℝ / pℤ)^ι` is dense exactly when its velocity `ν` is nonresonant: `∑ i, k i * ν i ≠ 0` for every
nonzero integer vector `k`.

```lean
TauCeti.AddCircle.denseRange_coe_add_mul_iff.{u_1} {ι : Type u_1} [Fintype ι] {p : ℝ} (hp : p ≠ 0)
  (θ ν : ι → ℝ) :
  (DenseRange fun t i => ↑(θ i + ν i * t)) ↔ ∀ (k : ι → ℤ), ∑ i, ↑(k i) * ν i = 0 → k = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weyl's equidistribution theorem for linear flows](weyls-equidistribution-theorem-for-linear-flows.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AddCircle.denseRange_coe_add_mul_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Kronecker.html#TauCeti.AddCircle.denseRange_coe_add_mul_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.AddCircle.denseRange_coe_add_mul_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Kronecker.html#TauCeti.AddCircle.denseRange_coe_add_mul_iff)
- [Source of `TauCeti.AddCircle.denseRange_coe_add_mul_iff` in TauCeti/Analysis/Fourier/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/Kronecker.lean#L245)
