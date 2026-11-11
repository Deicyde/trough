---
declaration: section
origin: cited
lean: MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf, MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail, MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_nonneg, MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_pos, MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_eq_zero, MathlibExt.Biology.CancerGenomics.DetectionPower.sum_binomPmf, MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_nonneg, MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_zero
statement: formalized
proof: formalized
---

# Detection power for somatic mutations

30 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html).

## Binomial probability mass function

The binomial probability `C(n, i) p^i (1 - p)^(n - i)` of `i` successes in `n` trials, as a
function of `i : ℕ`. It vanishes for `i > n` (the binomial coefficient is zero there, so the
truncated subtraction `n - i` is harmless).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf`, a definition declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#binom-pmf).

## Binomial upper tail probability

The binomial upper tail `ℙ_p(X ≥ m) = ∑_{m ≤ i ≤ n} C(n, i) p^i (1 - p)^(n - i)`, Carter's
`P(m)` with `p = ε / 3`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail`, a definition declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail).

## Nonnegativity of binomial probabilities

Binomial probabilities are nonnegative for `0 ≤ p ≤ 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_nonneg`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#binom-pmf-nonneg).

## Positivity of binomial probabilities

Binomial probabilities are positive on `{0, …, n}` for `0 < p < 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_pos`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#binom-pmf-pos).

## Binomial probabilities vanish above n

Binomial probabilities vanish above `n`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_eq_zero`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#binom-pmf-eq-zero).

## Binomial probabilities sum to one

The binomial law sums to one (the binomial theorem), for every real `p`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.sum_binomPmf`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#sum-binom-pmf).

## Nonnegativity of binomial tail probabilities

Tail probabilities are nonnegative for `0 ≤ p ≤ 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_nonneg`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-nonneg).

## Binomial upper tail from zero is one

`P(0) = 1`, for every real `p`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_zero`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-zero).

## Binomial upper tail beyond n is zero

`P(m) = 0` for `m > n`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_eq_zero`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-eq-zero).

## Binomial upper tail as one minus a lower sum

Carter's form of the tail: `P(m) = 1 - ∑_{i < m} Binom(i | n, p)`, for every `m`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_eq_one_sub_sum`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-eq-one-sub-sum).

## Recursion for the binomial upper tail

One step of the tail recursion: `P(m) = Binom(m | n, p) + P(m + 1)`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_eq_add`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-eq-add).

## Binomial upper tail is decreasing

`m ↦ P(m)` is antitone for `0 ≤ p ≤ 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_antitone`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-antitone).

## Binomial tails increase with the success probability

For `0 ≤ p ≤ p' ≤ 1`,
`ℙ_p(X ≥ m) ≤ ℙ_{p'}(X ≥ m)`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_mono`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-mono).

## The binomial likelihood is unimodal in `p`, increasing part

For `a ≤ n` and
`0 ≤ p ≤ p' ≤ a / n`, `Binom(a | n, p) ≤ Binom(a | n, p')`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_le_binomPmf_of_le_div`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#binom-pmf-le-binom-pmf-of-le-div).

## The binomial likelihood is unimodal in `p`, decreasing part

For `a ≤ n` and
`a / n ≤ p ≤ p' ≤ 1`, `Binom(a | n, p') ≤ Binom(a | n, p)`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.binomPmf_le_binomPmf_of_div_le`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#binom-pmf-le-binom-pmf-of-div-le).

## Critical count of the mutation detection test

Carter's critical count `k = min {m | P(m) ≤ FPR}` for the null success probability
`p₀ = ε / 3` (Online Methods, before Eq. 9).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.criticalCount`, a definition declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#critical-count).

## Randomization probability of the detection test

The randomization probability `d = (FPR - P(k)) / (P(k - 1) - P(k))` of Eq. 9.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.randomization`, a definition declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#randomization).

## Power of the randomized mutation detection test

The power `Pow(n, f) = P_f(X ≥ k) + d Binom(k - 1 | n, f)` of the exact-size randomized
test (Carter et al. 2012, Eq. 9, with the randomization at `k - 1`; see the module doc).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.power`, a definition declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#power).

## Critical count meets the false-positive bound

The critical count meets the false-positive bound: `P(k) ≤ FPR` (for `FPR ≥ 0`).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_criticalCount_le`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-critical-count-le).

## Upper bound on the critical count

The critical count is at most `n + 1` (for `FPR ≥ 0`).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.criticalCount_le`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#critical-count-le).

## Positivity of the critical count

The critical count is positive when `FPR < 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.criticalCount_pos`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#critical-count-pos).

## Minimality of the critical count

Minimality of the critical count: `FPR < P(k - 1)` (for `0 ≤ FPR < 1`).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.lt_upperTail_criticalCount_sub_one`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#lt-upper-tail-critical-count-sub-one).

## Tail gap at the critical count

The gap `P(k - 1) - P(k)` is the null probability of the boundary point `k - 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.upperTail_sub_one_sub`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#upper-tail-sub-one-sub).

## The randomization is a probability

`0 ≤ d < 1` for `0 ≤ FPR < 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.randomization_mem`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#randomization-mem).

## Exact size

**Exact size** (Carter et al. 2012, Eq. 9 with the randomization at `k - 1`): under the
null `f = p₀` the rejection probability is exactly `FPR`, for `0 ≤ FPR < 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.power_self`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#power-self).

## Detection power as a mixture of tail probabilities

The power is the mixture `(1 - d) P_f(X ≥ k) + d P_f(X ≥ k - 1)` of two tail
probabilities.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.power_eq_mix`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#power-eq-mix).

## Power increases with the allelic fraction

`Pow(n, f) ≤ Pow(n, f')` for
`0 ≤ f ≤ f' ≤ 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.power_mono`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#power-mono).

## Power increases with purity

**Power increases with purity** at the ABSOLUTE allelic fraction `α s / (α q + 2 (1 - α))`
of a clonal mutation of multiplicity `0 ≤ s ≤ q` (Carter et al. 2012, Eqs. 2, 9, 10).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.power_somaticAF_mono_purity`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#power-somatic-af-mono-purity).

## Power decreases with local copy number

**Power decreases with local copy number** at the ABSOLUTE allelic fraction, for a clonal
mutation of multiplicity `0 ≤ s ≤ q ≤ q'` (Carter et al. 2012, Eqs. 2, 9, 10).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.power_somaticAF_anti_copy`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#power-somatic-af-anti-copy).

## Power increases with multiplicity

**Power increases with multiplicity** at the ABSOLUTE allelic fraction, for
`0 ≤ s ≤ s' ≤ q` (Carter et al. 2012, Eqs. 2, 9).

Formalized by `MathlibExt.Biology.CancerGenomics.DetectionPower.power_somaticAF_mono_mult`, a theorem declared in [MathlibExt/Biology/CancerGenomics/DetectionPower.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/DetectionPower.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html#power-somatic-af-mono-mult).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Detection power for somatic mutations](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/cancer-genomics/detection-power-for-somatic-mutations)
