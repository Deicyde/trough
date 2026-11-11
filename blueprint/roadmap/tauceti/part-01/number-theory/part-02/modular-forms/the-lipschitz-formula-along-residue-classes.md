---
declaration: theorem
origin: cited
lean: TauCeti.EisensteinSeries.qExpansion_identity_zmod
statement: formalized
proof: formalized
---

# The Lipschitz formula along residue classes

For a function `f` of residues modulo `v`,
a weight `k ≥ 2` and `z` in the upper half-plane,
`∑_{n ∈ ℤ} f(n) (z + n)^(-k) = (-2πi)^k / ((k-1)! v^k) ∑_{m ≥ 1} 𝓕f(-m) m^(k-1) e^(2πi m z / v)`,
where `𝓕f(-m) = ∑_{r mod v} f(r) e^(2πi r m / v)` is the discrete Fourier transform of `f`.
For `v = 1` this is `f 0` times Mathlib's `EisensteinSeries.qExpansion_identity_pnat`.

```lean
TauCeti.EisensteinSeries.qExpansion_identity_zmod {v : ℕ} [NeZero v] (f : ZMod v → ℂ) {k : ℕ}
  (hk : 2 ≤ k) (z : UpperHalfPlane) :
  ∑' (n : ℤ), f ↑n * (↑z + ↑n) ^ (-↑k) =
    (-2 * ↑Real.pi * Complex.I) ^ k / (↑(k - 1).factorial * ↑v ^ k) *
      ∑' (m : ℕ+),
        ZMod.dft f (-↑↑m) * ↑↑m ^ (k - 1) * Complex.exp (2 * ↑Real.pi * Complex.I * ↑z / ↑v) ^ ↑m
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.EisensteinSeries.qExpansion_identity_zmod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/QExpansion.html#TauCeti.EisensteinSeries.qExpansion_identity_zmod).

## Sources

- [Tau Ceti documentation: `TauCeti.EisensteinSeries.qExpansion_identity_zmod`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/EisensteinSeries/QExpansion.html#TauCeti.EisensteinSeries.qExpansion_identity_zmod)
- [Source of `TauCeti.EisensteinSeries.qExpansion_identity_zmod` in TauCeti/NumberTheory/ModularForms/EisensteinSeries/QExpansion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/EisensteinSeries/QExpansion.lean#L125)
