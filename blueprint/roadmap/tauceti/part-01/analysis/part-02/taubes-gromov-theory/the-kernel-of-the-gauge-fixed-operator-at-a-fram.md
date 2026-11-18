---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.finrank_le_two_mul_of_tendsto_sectionValue_mul_inv_pow
statement: formalized
proof: formalized
---

# The kernel of the gauge-fixed operator at a framed vortex has dimension at most `2m`

At a
`C²` field with vanishing holomorphicity rows and the degree-`m` end framing
`α(z) (z / |z|)⁻ᵐ → 1`, every real vector space of `C²` square-integrable solutions of
`L_x y = 0` has dimension at most `2m`, the real dimension of the divisor space `Sym^m ℂ`.

```lean
TauCeti.Vortex.finrank_le_two_mul_of_tendsto_sectionValue_mul_inv_pow {μ : MeasureTheory.Measure ℂ}
  [μ.IsAddHaarMeasure] {x : ℂ → EuclideanSpace ℝ (Fin 4)}
  {V : Submodule ℝ (ℂ → EuclideanSpace ℝ (Fin 4))} {m : ℕ} (hx : ContDiff ℝ 2 x)
  (hhol :
    ∀ (w : ℂ), (TauCeti.Vortex.equation x w).ofLp 1 = 0 ∧ (TauCeti.Vortex.equation x w).ofLp 2 = 0)
  (hframe :
    Filter.Tendsto (fun z => TauCeti.Vortex.sectionValue x z * ((z / ↑‖z‖) ^ m)⁻¹)
      (Filter.cocompact ℂ) (nhds 1))
  (hV :
    ∀ y ∈ V,
      ContDiff ℝ 2 y ∧
        MeasureTheory.MemLp y 2 μ ∧ ∀ (w : ℂ), TauCeti.Vortex.gaugeFixedOperator x y w = 0) :
  Module.finrank ℝ ↥V ≤ 2 * m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula with a cutoff](../../part-03/complex/part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)
- [The Dolbeault lemma on a disc](../../part-03/complex/part-01/the-dolbeault-lemma-on-a-disc.md)
- [Green's second identity against a test function](../../part-04/sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [The monotone du Bois-Reymond lemma](../../part-03/distribution/the-monotone-du-bois-reymond-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.finrank_le_two_mul_of_tendsto_sectionValue_mul_inv_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/KernelDimension.html#TauCeti.Vortex.finrank_le_two_mul_of_tendsto_sectionValue_mul_inv_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.finrank_le_two_mul_of_tendsto_sectionValue_mul_inv_pow`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/KernelDimension.html#TauCeti.Vortex.finrank_le_two_mul_of_tendsto_sectionValue_mul_inv_pow)
- [Source of `TauCeti.Vortex.finrank_le_two_mul_of_tendsto_sectionValue_mul_inv_pow` in TauCeti/Analysis/PDE/Vortex/KernelDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Vortex/KernelDimension.lean#L200)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
