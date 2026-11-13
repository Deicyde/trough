---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.cloneProb, MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.convPow, MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.ldPmf, MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.clonePgf, MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.integral_cloneSize, MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.hasSum_cloneProb, MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.hasSum_cloneProb_mul_pow, MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.ldPmf_zero
statement: formalized
proof: formalized
---

# Luria–Delbrück distribution

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html).

## Lea–Coulson clone-size law

The **Lea–Coulson clone-size law** `P(size = j) = 1 / (j (j + 1))` for `j ≥ 1`
(`P(size = 0) = 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.cloneProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#clone-prob).

## Convolution power of a sequence on the naturals

The `k`-fold convolution power of a sequence on `ℕ`: `p^{*0} = δ₀` and
`p^{*(k+1)}(n) = ∑_{i ≤ n} p(i) p^{*k}(n - i)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.convPow`, a definition declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#conv-pow).

## Luria–Delbrück distribution

The **Luria–Delbrück probability** of `n` mutants with expected mutation number `m`: the
compound-Poisson law `∑_k e^{-m} m^k / k! · cloneProb^{*k}(n)`. Since clones have size at
least `1`, only `k ≤ n` contribute.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.ldPmf`, a definition declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#ld-pmf).

## Closed form of the clone-size generating function

The clone-size generating function `h(z) = 1 + (1 / z - 1) log (1 - z)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.clonePgf`, a definition declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#clone-pgf).

## Clone-size law from the founding-time density

A clone founded `τ` before the end has
geometric size `e^{-τ} (1 - e^{-τ})^{j-1}`; mixing over the founding-time density `e^{-τ}` on
`(0, ∞)` gives `1 / (j (j + 1))` for `j ≥ 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.integral_cloneSize`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#integral-clone-size).

## The clone-size law sums to one

The clone-size law sums to `1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.hasSum_cloneProb`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#has-sum-clone-prob).

## Clone-size generating function

For `0 < z < 1`,
`∑ⱼ zʲ / (j (j + 1)) = 1 + (1 / z - 1) log (1 - z)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.hasSum_cloneProb_mul_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#has-sum-clone-prob-mul-pow).

## `p₀`

The probability of no mutants is `e^{-m}`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.ldPmf_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#ld-pmf-zero).

## The `p₀` method

**The `p₀` method** (Luria–Delbrück 1943): the expected number of mutations is recovered
from the proportion of cultures with no mutants, `m = -log p₀`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.p0_method`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#p0-method).

## Nonnegativity of Luria–Delbrück probabilities

The Luria–Delbrück probabilities are nonnegative for `m ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.ldPmf_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#ld-pmf-nonneg).

## The Luria–Delbrück probabilities sum to one

The Luria–Delbrück probabilities sum to `1` (for `m ≥ 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.hasSum_ldPmf`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#has-sum-ld-pmf).

## Lea–Coulson generating function

For `m ≥ 0` and `0 < z < 1`,
`∑ₙ pₙ zⁿ = exp (m (h(z) - 1)) = exp (m (1 / z - 1) log (1 - z))`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.hasSum_ldPmf_mul_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#has-sum-ld-pmf-mul-pow).

## Power form of the Lea–Coulson generating function

The Lea–Coulson generating function in power form:
`exp (m (1 / z - 1) log (1 - z)) = (1 - z)^{m (1 - z) / z}` for `z < 1`, `z ≠ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.exp_leaCoulson_eq_rpow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#exp-lea-coulson-eq-rpow).

## Ma–Sandri–Sarkar recursion

For `n ≥ 1`,
`pₙ = (m / n) ∑_{i < n} pᵢ / (n - i + 1)` (all real `m`).

Formalized by `MathlibExt.Biology.PopulationGenetics.LuriaDelbruck.ldPmf_recursion`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/LuriaDelbruck.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html#ld-pmf-recursion).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Luria–Delbrück distribution](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/luria-delbr-ck-distribution/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/population-genetics/luria-delbr-ck-distribution)
