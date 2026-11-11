---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow_le
statement: formalized
proof: formalized
---

# The Littlewood–Paley square function inequality

Let `V` be a real inner product space
of finite dimension `n ≥ 1`, let `φ` be a smooth bump function on `V`, and let `1 < p < ∞`. Let
`Δⱼ` be the `L²` Fourier multipliers with the pieces `ψ₀ = φ`, `ψⱼ = φ (2^{-j} ·) - φ (2^{1-j} ·)`
of the inhomogeneous Littlewood–Paley partition as symbols. For every complex Hilbert space `F`
there is a constant `C` such that for every `f ∈ L²(V, F)`,

`‖(∑ⱼ ‖Δⱼ f‖²)^{1/2}‖_p ≤ C ‖f‖_p`.

Each symbol enters as any element of `L^∞` almost everywhere equal to `ψⱼ`.

```lean
TauCeti.exists_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow_le.{u_1, u_2} {V : Type u_1}
  {F : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V]
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [Nontrivial V] [MeasurableSpace V] [BorelSpace V]
  [CompleteSpace F] (φ : ContDiffBump 0) {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (m : ℕ → ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)),
      (∀ (j : ℕ), ↑↑(m j) =ᵐ[MeasureTheory.volume] fun ξ => ↑(φ.inhomogeneousLittlewoodPaley j ξ)) →
        ∀ (f : ↥(MeasureTheory.Lp F 2 MeasureTheory.volume)),
          MeasureTheory.eLpNorm
              (fun x =>
                (∑' (j : ℕ), ‖↑↑((MeasureTheory.Lp.fourierMultiplierCLM F (m j)) f) x‖ₑ ^ 2) ^ 2⁻¹)
              p MeasureTheory.volume ≤
            ↑C * MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Calderón–Zygmund theorem](../../../measure-theory/integral/part-01/the-calderon-zygmund-theorem.md)
- [Hölder's inequality for the integral of a product](../../../measure-theory/function/part-01/holders-inequality-for-the-integral-of-a-product.md)
- [Plancherel's theorem for the inverse Fourier transform of Schwartz functions](../distribution/plancherels-theorem-for-the-inverse-fourier-tran.md)
- [The weighted Plancherel bound](../distribution/the-weighted-plancherel-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LittlewoodPaley.html#TauCeti.exists_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LittlewoodPaley.html#TauCeti.exists_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow_le)
- [Source of `TauCeti.exists_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow_le` in TauCeti/Analysis/Fourier/LittlewoodPaley.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/LittlewoodPaley.lean#L471)
