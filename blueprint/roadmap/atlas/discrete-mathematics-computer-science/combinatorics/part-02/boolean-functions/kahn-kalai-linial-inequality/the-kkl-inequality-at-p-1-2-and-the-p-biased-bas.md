---
declaration: section
origin: cited
lean: StatMech.Probability.fsr_ptn_psi_half, StatMech.Probability.fsr_ptn_pchar_half, StatMech.Probability.fsr_ptn_coeff_half_sq, StatMech.Probability.fsr_totalInfl_half_eq, StatMech.Probability.fsr_pbiased_endpoint
statement: formalized
proof: formalized
---

# The KKL inequality at p = 1/2, and the p-biased basis at p = 1/2

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas/index.html).

## Normalized bit at $p = 1/2$ is $-(-1)^b$

At `p = 1/2` the normalized bit is `-(-1)^b`.

Formalized by `StatMech.Probability.fsr_ptn_psi_half`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas/index.html#fsr-ptn-psi-half).

## $p$-biased character at $p = 1/2$ is the Walsh character up to sign

At `p = 1/2` the `p`-biased character is `(-1)^{|S|}` times the Walsh character.

Formalized by `StatMech.Probability.fsr_ptn_pchar_half`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas/index.html#fsr-ptn-pchar-half).

## Squared $p$-biased and Walsh coefficients agree at $p = 1/2$

At `p = 1/2` the squared `p`-biased and Walsh Fourier coefficients agree.

Formalized by `StatMech.Probability.fsr_ptn_coeff_half_sq`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas/index.html#fsr-ptn-coeff-half-sq).

## Total influence at $p = 1/2$ via $p$-biased Fourier coefficients

Total influence at `p = 1/2` in terms of the `p`-biased Fourier coefficients.

Formalized by `StatMech.Probability.fsr_totalInfl_half_eq`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas/index.html#fsr-total-infl-half-eq).

## Kahn–Kalai–Linial inequality

**Kahn–Kalai–Linial inequality** for the uniform measure with constant `2` (J. Kahn, G. Kalai,
 N. Linial, *The influence of variables on Boolean functions*, FOCS 1988; proof after D. Falik,
 A. Samorodnitsky, 2007): for every finite nonempty `E` and every Boolean function `φ` on `{0,
 1}^E`, `2 · Var(φ) · log (1 / maxₑ Infₑ(φ)) ≤ ∑ₑ Infₑ(φ)`, where `Infₑ(φ)` is the probability
 that `e` is pivotal. This is the `p = 1/2` case of the `p`-biased KKL inequality.

Formalized by `StatMech.Probability.fsr_pbiased_endpoint`, a theorem declared in [CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Complexity/BooleanFunctions/KKL/FSRhoOptimise.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas/index.html#fsr-pbiased-endpoint).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The KKL inequality at p = 1/2, and the p-biased basis at p = 1/2](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/kahn-kalai-linial-inequality/the-kkl-inequality-at-p-1-2-and-the-p-biased-bas)
