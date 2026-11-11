---
declaration: theorem
origin: cited
lean: TauCeti.SU2.weyl_integration_formula
statement: formalized
proof: formalized
---

# The Weyl integration formula for `SU(2)`

For a continuous class function `f` on `SU(2)`,
the integral of `f` against the Haar probability measure is the integral over the Weyl chamber
`[0, π]` of the maximal torus against the Weyl density `(2π)⁻¹ · 4 sin²θ dθ`:

`∫ f dμ = (2π)⁻¹ ∫₀^π f (diag (e^{iθ}, e^{-iθ})) · 4 sin²θ dθ`.

The Weyl factor `4 sin²θ = |e^{iθ} - e^{-iθ}|²` is the squared modulus of the Weyl denominator,
and the density has total mass one (`TauCeti.SU2.weyl_integration_formula_normalized`).

```lean
TauCeti.SU2.weyl_integration_formula {f : TauCeti.SU2 → ℂ} (hf : Continuous f)
  (hconj : ∀ (u g : TauCeti.SU2), f (u * g * u⁻¹) = f g) :
  ∫ (g : TauCeti.SU2), f g ∂TauCeti.haarProb TauCeti.SU2 =
    1 / (2 * ↑Real.pi) * ∫ (θ : ℝ) in 0..Real.pi, f (TauCeti.SU2.torusExp θ) * ↑(4 * Real.sin θ ^ 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The spectral theorem for normal matrices](../../analysis/part-03/matrix/the-spectral-theorem-for-normal-matrices.md)
- [The Weyl character formula for `SU(2)`](the-weyl-character-formula-for-su-2.md)
- [The Weyl numerator identity](the-weyl-numerator-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SU2.weyl_integration_formula`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Integration.html#TauCeti.SU2.weyl_integration_formula).

## Sources

- [Tau Ceti documentation: `TauCeti.SU2.weyl_integration_formula`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/SU2/Weyl/Integration.html#TauCeti.SU2.weyl_integration_formula)
- [Source of `TauCeti.SU2.weyl_integration_formula` in TauCeti/RepresentationTheory/SU2/Weyl/Integration.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/SU2/Weyl/Integration.lean#L138)
