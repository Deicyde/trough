---
declaration: section
origin: cited
lean: ProbabilityTheory.map_div_sqrt_chiSquare_eq_studentT, ProbabilityTheory.map_div_chiSquare_eq_snedecorF, ProbabilityTheory.map_tStatistic_pi_gaussianReal, ProbabilityTheory.NormalTheoryWanted.tendstoInDistribution_uStatistic
statement: formalized
---

# Student's t and Snedecor's F distributions

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/student-s-t-and-snedecor-s-f-distributions/index.html).

## Student's `t` law

**Student's `t` law** (Casella–Berger, Definition 5.3.4): for independent `Z ~ N(0, 1)` and
`V ~ χ²_k` with `k ≥ 1`, `Z / √(V / k)` has density
`Γ((k + 1)/2) / (√(k π) Γ(k/2)) · (1 + t²/k)^{-(k+1)/2}`.

Formalized by `ProbabilityTheory.map_div_sqrt_chiSquare_eq_studentT`, a theorem declared in [MathlibExt/Probability/Distributions/StudentT.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/StudentT.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/student-s-t-and-snedecor-s-f-distributions/index.html#map-div-sqrt-chi-square-eq-student-t).

## Snedecor's `F` law

**Snedecor's `F` law** (Casella–Berger, Definition 5.3.6): for independent `V₁ ~ χ²_{d₁}` and
`V₂ ~ χ²_{d₂}` with `d₁, d₂ ≥ 1`, `(V₁ / d₁) / (V₂ / d₂)` has density
`Γ((d₁ + d₂)/2) / (Γ(d₁/2) Γ(d₂/2)) · (d₁/d₂)^{d₁/2} x^{d₁/2 - 1} (1 + d₁ x / d₂)^{-(d₁+d₂)/2}`
on `x > 0`.

Formalized by `ProbabilityTheory.map_div_chiSquare_eq_snedecorF`, a theorem declared in [MathlibExt/Probability/Distributions/SnedecorF.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/SnedecorF.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/student-s-t-and-snedecor-s-f-distributions/index.html#map-div-chi-square-eq-snedecor-f).

## One-sample `t` statistic

For an i.i.d. sample `X₁, …, Xₙ ~ N(μ, v)` with `n ≥ 2` and
`v > 0`, `√n (X̄ - μ) / S` with `S² = ∑ (Xᵢ - X̄)² / (n - 1)` has the Student `t` law with
`n - 1` degrees of freedom.

Formalized by `ProbabilityTheory.map_tStatistic_pi_gaussianReal`, a theorem declared in [MathlibExt/Probability/Statistics/LinearModel/Inference.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Statistics/LinearModel/Inference.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/student-s-t-and-snedecor-s-f-distributions/index.html#map-t-statistic-pi-gaussian-real).

## Hoeffding's central limit theorem

**Hoeffding's central limit theorem** (1948, §7): for an i.i.d. sample from `μ` and a
symmetric square-integrable kernel `h` of degree `m`, `√n (U_n - θ)` converges in distribution
to `N(0, m² σ₁²)`, where `θ = E h` and `σ₁² = Var h₁`.

Stated but not proved: `ProbabilityTheory.NormalTheoryWanted.tendstoInDistribution_uStatistic` is written with `theorem_wanted` in [WantedExt/Probability/Statistics/NormalTheoryWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/Statistics/NormalTheoryWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/student-s-t-and-snedecor-s-f-distributions/index.html#tendsto-in-distribution-u-statistic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Student's t and Snedecor's F distributions](https://deicyde.github.io/atlas-lean/roadmap/Probability/linear-models-multivariate/student-s-t-and-snedecor-s-f-distributions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/linear-models-multivariate/student-s-t-and-snedecor-s-f-distributions)
