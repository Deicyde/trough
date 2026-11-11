---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.sfsKernel, MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.variableSFS, MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.integral_sfs_of_indep, MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.variableSFS_inv_choose_two, MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.sfsKernel_eq_zero_of_lt, MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.sfsKernel_diag_pos, MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.eq_of_variableSFS_eq, MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.thetaWeighted
statement: formalized
---

# Site frequency spectrum under variable population size

43 results, 42 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html).

## Griffiths–Tavaré kernel

The **Griffiths–Tavaré kernel** `k C(n-i-1, k-2) / C(n-1, k-1)`: the expected number of
branches subtending exactly `i` of the `n` sample copies while `k` lineages remain
(`SiteFrequencySpectrum.joinStep_iterate_count`). Meaningful for `1 ≤ i < n`, `2 ≤ k ≤ n`;
outside that range the natural-number subtractions give junk values.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.sfsKernel`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#sfs-kernel).

## Expected site frequency spectrum under variable population size

The expected SFS entry `(θ / 2) ∑_{k=2}^{n} sfsKernel n i k · t k` of a sample of size
`n` whose mean holding times are `t k = E T_k` (Griffiths & Tavaré 1998, Polanski & Kimmel
2003).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.variableSFS`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#variable-sfs).

## Expected SFS under a variable population size

**Expected SFS under a variable population size** (Griffiths & Tavaré 1998; Polanski &
Kimmel 2003). Let the genealogy of a sample of `n` copies consist of holding times `T k`
(integrable for `2 ≤ k ≤ n`, otherwise arbitrary) and an independent block-size history `τ`
with the random-joining law. If, given the genealogy, the count `ξ i` is integrable with
conditional mean `(θ / 2) L_i`, then `E ξ_i = (θ / 2) ∑_k k C(n-i-1,k-2)/C(n-1,k-1) E T_k`
for `1 ≤ i ≤ n - 1`. Independence of the holding times and the topology holds for the
time-changed Kingman coalescent of any deterministic population-size history (a standard property of that model; here it is a hypothesis).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.integral_sfs_of_indep`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#integral-sfs-of-indep).

## Variable-size spectrum reduces to Fu's $\theta/i$ at constant size

With the constant-size means `E T_k = 1 / C(k,2)`, the variable-size SFS is Fu's
`θ / i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.variableSFS_inv_choose_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#variable-sfs-inv-choose-two).

## Griffiths–Tavaré kernel vanishes beyond the diagonal

The kernel row `i` vanishes beyond `k = n - i + 1`: a branch subtending `i` copies cannot
exist while more than `n - i + 1` lineages remain.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.sfsKernel_eq_zero_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#sfs-kernel-eq-zero-of-lt).

## Positivity of the Griffiths–Tavaré kernel on the diagonal

The kernel entry at `k = n - i + 1` is `(n - i + 1) / C(n-1, i-1) > 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.sfsKernel_diag_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#sfs-kernel-diag-pos).

## The expected SFS determines the mean holding times

If two vectors of mean holding
times give the same expected SFS for some `θ ≠ 0`, they agree at every `k = 2, …, n`. This is
a direct consequence of `sfsKernel_eq_zero_of_lt` and `sfsKernel_diag_pos` (the kernel is
triangular with nonzero diagonal); it is recorded here as an observation, not as a cited
theorem.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.eq_of_variableSFS_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#eq-of-variable-sfs-eq).

## Achaz's weighted estimator of $\theta$

Achaz's weighted estimator `θ_ω = ∑_{i=1}^{n-1} ω_i i ξ_i` (Achaz 2009, with the
weights already normalized).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.thetaWeighted`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#theta-weighted).

## Tajima's $\theta_\pi$ in site frequency spectrum form

Tajima's `θ_π` in its SFS form `∑_i i (n - i) ξ_i / C(n,2)` (weights `(n - i) / C(n,2)`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.thetaPi`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#theta-pi).

## Fay and Wu's $\theta_H$

Fay & Wu's `θ_H = ∑_i i² ξ_i / C(n,2)` (weights `i / C(n,2)`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.thetaH`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#theta-h).

## Fay and Wu's H statistic

Fay & Wu's `H = θ_π - θ_H` (Fay & Wu 2000).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.fayWuH`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#fay-wu-h).

## Numerator of Fu and Li's D

The numerator `S - a₁ ξ₁` of Fu & Li's `D` with an outgroup, where `S = ∑_i ξ_i` and the
external-branch mutations are the derived singletons `ξ₁` (Fu & Li 1993).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.fuLiDNumerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#fu-li-dnumerator).

## Numerator of Fu and Li's F

The numerator `θ_π - ξ₁` of Fu & Li's `F` with an outgroup (Fu & Li 1993), with `θ_π` in
its SFS form.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.fuLiFNumerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#fu-li-fnumerator).

## Achaz's unbiasedness

**Achaz's unbiasedness** (Achaz 2009): if `E ξ_i = θ / i` for `1 ≤ i ≤ n - 1` (the
constant-size spectrum, `SiteFrequencySpectrum.integral_sfs`), every weighted estimator with
`∑_i ω_i = 1` has mean `θ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.integral_thetaWeighted`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#integral-theta-weighted).

## Fay and Wu's H has mean zero at constant size

Fay & Wu's `H` has mean zero under the constant-size spectrum (`n ≥ 2`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.integral_fayWuH`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#integral-fay-wu-h).

## Numerator of Fu and Li's D has mean zero at constant size

The numerator of Fu & Li's `D` has mean zero under the constant-size spectrum
(`n ≥ 2`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.integral_fuLiDNumerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#integral-fu-li-dnumerator).

## Numerator of Fu and Li's F has mean zero at constant size

The numerator of Fu & Li's `F` has mean zero under the constant-size spectrum
(`n ≥ 2`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.integral_fuLiFNumerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#integral-fu-li-fnumerator).

## Achaz's estimator is unbiased under Kingman's coalescent

Achaz's unbiasedness under Kingman's coalescent, with the hypotheses of
`SiteFrequencySpectrum.integral_sfs`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.integral_thetaWeighted_kingman`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#integral-theta-weighted-kingman).

## Cumulative coalescence intensity

The cumulative coalescence intensity `R(s) = ∫_0^s 1/η` of a relative population-size
function `η` (pairs coalesce at rate `1/η(s)` at time `s` before the present). Meaningful for
positive `η` with `1/η` locally integrable.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.cumRate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#cum-rate).

## Expected time to the first coalescence

The expected time to the first coalescence among `m` lineages,
`c_m = ∫_0^∞ exp(-C(m,2) R(s)) ds`, in a population of relative size `η`
(Bhaskar & Song's `E[T_{m,m}]`). When the integrand is not integrable (for example `η ≡ 0`),
this is Lean's junk value `0`; for piecewise-constant histories it is integrable
(`choose_two_mul_firstCoalMean`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.firstCoalMean`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#first-coal-mean).

## Piecewise-constant population-size history

A **piecewise-constant population-size history with `K` pieces**: piece `j < K` starts at
time `start j` (backward from the present, `start 0 = 0`, strictly increasing) and has
relative size `size j > 0`; the last piece extends to infinity. Adjacent pieces may have equal
sizes, so this also covers histories with fewer than `K` distinct pieces. Values at indices
`j ≥ K` are unused. The case `K = 0` is degenerate (its size function is `0`); the theorems
about `c_m` assume `0 < K` where it matters.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory`, a structure declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 425](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L425). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#piecewise-history).

## Size function of a piecewise-constant history

The population-size function of a piecewise-constant history: at time `s ≥ 0` it is the
size of the piece `j` with `start j ≤ s < start (j + 1)` (the last piece has no end). Equal to
`0` for `s < 0` (junk; only `s ≥ 0` is meaningful).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.sizeFn`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#size-fn).

## Monotonicity of piece start times

The start times are monotone on the pieces.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.start_mono`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#start-mono).

## Nonnegativity of piece start times

Every piece starts at a nonnegative time.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.start_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#start-nonneg).

## Size function on a piece equals the piece size

On piece `j` the size function equals `size j`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.sizeFn_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#size-fn-eq).

## Cumulative rate is affine on each piece

On piece `j` (including its right end), `1 / sizeFn` is integrable on `[0, s]` and the
cumulative rate is affine: `R(s) = R(start j) + (s - start j) / size j`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.cumRate_piece`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#cum-rate-piece).

## Closed form of the first-coalescence times

For a history with `K ≥ 1` pieces and
`m ≥ 2`, writing `a = C(m,2)` and `R = cumRate h.sizeFn`,
`a c_m = size 0 + ∑_{j=1}^{K-1} (size j - size (j-1)) exp(-a R(start j))`. In particular the
integral defining `c_m` converges.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.choose_two_mul_firstCoalMean`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#choose-two-mul-first-coal-mean).

## Every nonnegative time lies in some piece

Every time `s ≥ 0` lies in some piece.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.exists_piece`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 639](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L639). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#exists-piece).

## Positivity of the piecewise size function

The size function is positive on `[0, ∞)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.sizeFn_pos`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 651](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L651). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#size-fn-pos).

## Coalescent-time breakpoints are strictly increasing

The coalescent-time breakpoints `R(start j)` are strictly increasing.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.cumRate_start_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 658](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L658). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#cum-rate-start-lt).

## Dual history in coalescent time

The dual history in coalescent time: piece `j` starts at `R(start j)` and has size
`1 / size j`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.dual`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#dual).

## Size function is the inverse of the dual size in coalescent time

The size at time `s` is the inverse of the dual history's size at coalescent time
`R(s)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.sizeFn_eq_inv_dual`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 691](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L691). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#size-fn-eq-inv-dual).

## Dual cumulative rate inverts the cumulative rate

The dual cumulative rate inverts the cumulative rate.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.cumRate_dual_cumRate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 699](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L699). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#cum-rate-dual-cum-rate).

## Cumulative rate is strictly increasing

The cumulative rate is strictly increasing on `[0, ∞)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.cumRate_strictMonoOn`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#cum-rate-strict-mono-on).

## Bhaskar–Song identifiability

**Bhaskar–Song identifiability** (Bhaskar & Song 2014, Corollary 7, "determined" half,
stated for the first-coalescence times): two piecewise-constant histories with `K` pieces whose
expected first-coalescence times `c_m` agree for `2 ≤ m ≤ n`, with `n ≥ 2K`, have the same
population size at every time `s ≥ 0`. The proof writes `C(m,2) c_m` as an exponential sum in
`C(m,2)` over at most `2K - 1` rates (`choose_two_mul_firstCoalMean`), identifies the
coefficients with `Real.eq_zero_of_sum_mul_exp_eq_zero`, recovers the size as a function of
coalescent time (the `dual` history) and inverts `R` (`cumRate_dual_cumRate`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.sizeFn_eq_of_firstCoalMean_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 832](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L832). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#size-fn-eq-of-first-coal-mean-eq).

## Tightness of `n ≥ 2K`

**Tightness of `n ≥ 2K`** (Bhaskar & Song 2014, Corollary 7): for every `K ≥ 2` there are
two piecewise-constant histories with `K` pieces whose sizes differ at some time `s ≥ 0` but
whose first-coalescence times `c_m` agree for `2 ≤ m ≤ 2K - 1`; so
`sizeFn_eq_of_firstCoalMean_eq` fails for `n = 2K - 1`. The construction is explicit: with
`z = 2^{-C(m,2)}`, the two histories have coalescent-time breakpoints `(2j - 1) log 2` and
`2j log 2`, so `C(m,2) (c_m - c'_m)` is a polynomial of degree `2K - 2` in `z`; its
coefficients are those of `∏_{m=2}^{2K-1} (X - 2^{-C(m,2)})`, which vanishes at the `2K - 2`
points and has a nonzero constant term (the sizes at time `0` differ).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.exists_ne_firstCoalMean_eq_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 932](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L932). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#exists-ne-first-coal-mean-eq-of-lt).

## Measurability of the piecewise size function

The size function is measurable.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.measurable_sizeFn`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 1030](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L1030). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#measurable-size-fn).

## Size function lies between the extreme piece sizes

On `[0, ∞)` the size function lies between the smallest and the largest piece size.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.exists_le_sizeFn_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 1041](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L1041). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#exists-le-size-fn-le).

## Size function is locally constant to the right

The size function is constant on an interval to the right of every `s ≥ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.exists_sizeFn_eq_Ico`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 1052](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L1052). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#exists-size-fn-eq-ico).

## Distinct two-piece histories with equal first-coalescence times

The two-piece case of `exists_ne_firstCoalMean_eq_of_lt`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.PiecewiseHistory.exists_ne_firstCoalMean_eq_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 1063](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L1063). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#exists-ne-first-coal-mean-eq-two).

## First-coalescence times depend only on sizes at nonnegative times

Only the values on `[0, ∞)` enter the first-coalescence times.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.firstCoalMean_comp_max`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 1071](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L1071). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#first-coal-mean-comp-max).

## Non-identifiability from a bounded sample size

For every `n` there are two measurable
population-size functions, bounded between positive constants and different on a set of
positive measure in `[0, ∞)`, with the same `c_m` for `2 ≤ m ≤ n` (two `(n + 2)`-piece
histories from `PiecewiseHistory.exists_ne_firstCoalMean_eq_of_lt`, extended to `s < 0` by
their size at `0`). This is the finite-sample shape of the statement of Myers, Fefferman &
Patterson (2008); their theorem gives one pair of functions with equal `c_m` for **every** `m`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFS.exists_ne_ae_firstCoalMean_eq_Icc`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean, line 1087](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/VariableSFS.lean#L1087). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#exists-ne-ae-first-coal-mean-eq-icc).

## Non-identifiability of general histories

**Non-identifiability of general histories** (Myers, Fefferman & Patterson 2008): there
are two measurable population-size functions, bounded between positive constants, that differ
on a set of positive Lebesgue measure in `[0, ∞)` and have the same expected first-coalescence
time `c_m` for every `m ≥ 2` (hence the same expected SFS for every sample size).

## Sources

- Myers, Fefferman & Patterson (2008).

Stated but not proved: `MathlibExt.Biology.PopulationGenetics.Coalescent.VariableSFSWanted.exists_ne_ae_firstCoalMean_eq` is written with `theorem_wanted` in [WantedExt/Biology/PopulationGenetics/Coalescent/VariableSFSWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Biology/PopulationGenetics/Coalescent/VariableSFSWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html#exists-ne-ae-first-coal-mean-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Site frequency spectrum under variable population size](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/site-frequency-spectrum-under-variable-populatio)
