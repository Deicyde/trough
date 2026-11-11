---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_le_mul_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow
statement: formalized
proof: formalized
---

# The reverse Littlewood–Paley square function inequality

Let `V` be a real inner product
space of finite dimension `n ≥ 1`, let `φ` be a smooth bump function on `V`, and let `1 < p < ∞`.
Let `Δⱼ` be the `L²` Fourier multipliers with the pieces `ψ₀ = φ`,
`ψⱼ = φ (2^{-j} ·) - φ (2^{1-j} ·)` of the inhomogeneous Littlewood–Paley partition as symbols.
For every complex Hilbert space `F` there is a constant `C` such that for every `f ∈ L²(V, F)`,

`‖f‖_p ≤ C ‖(∑ⱼ ‖Δⱼ f‖²)^{1/2}‖_p`.

Neither side is assumed finite: in particular `f ∈ Lᵖ` as soon as its square function is. Each
symbol enters as any element of `L^∞` almost everywhere equal to `ψⱼ`.

```lean
TauCeti.exists_eLpNorm_le_mul_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow.{u_1, u_2}
  {V : Type u_1} {F : Type u_2} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [NormedAddCommGroup F] [InnerProductSpace ℂ F] [Nontrivial V]
  [MeasurableSpace V] [BorelSpace V] [CompleteSpace F] (φ : ContDiffBump 0) {p : ENNReal}
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (m : ℕ → ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)),
      (∀ (j : ℕ), ↑↑(m j) =ᵐ[MeasureTheory.volume] fun ξ => ↑(φ.inhomogeneousLittlewoodPaley j ξ)) →
        ∀ (f : ↥(MeasureTheory.Lp F 2 MeasureTheory.volume)),
          MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume ≤
            ↑C *
              MeasureTheory.eLpNorm
                (fun x =>
                  (∑' (j : ℕ), ‖↑↑((MeasureTheory.Lp.fourierMultiplierCLM F (m j)) f) x‖ₑ ^ 2) ^
                    2⁻¹)
                p MeasureTheory.volume
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy–Schwarz for a banded double sum](../../part-03/mean-inequalities/cauchy-schwarz-for-a-banded-double-sum.md)
- [The Littlewood–Paley square function inequality](the-littlewood-paley-square-function-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_le_mul_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LittlewoodPaley.html#TauCeti.exists_eLpNorm_le_mul_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_le_mul_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/LittlewoodPaley.html#TauCeti.exists_eLpNorm_le_mul_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow)
- [Source of `TauCeti.exists_eLpNorm_le_mul_eLpNorm_tsum_enorm_fourierMultiplierCLM_sq_rpow` in TauCeti/Analysis/Fourier/LittlewoodPaley.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/LittlewoodPaley.lean#L650)
