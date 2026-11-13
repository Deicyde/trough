---
declaration: section
origin: cited
lean: ProbabilityTheory.binomTail, ProbabilityTheory.binomTail_zero, ProbabilityTheory.binomTail_of_lt, ProbabilityTheory.binomTail_succ_le, ProbabilityTheory.hasDerivAt_binomTail, ProbabilityTheory.monotoneOn_binomTail, ProbabilityTheory.strictMonoOn_binomTail, MathlibExt.Biology.Phylogenetics.MotifConservation.mcsApprox
statement: formalized
proof: formalized
---

# Evolutionary conservation scores

44 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html).

## Upper tail of the binomial distribution

The upper tail `P(X ≥ k) = ∑_{i = k}^{n} C(n, i) p^i (1 - p)^(n - i)` of the binomial law
`Bin(n, p)`.

Formalized by `ProbabilityTheory.binomTail`, a definition declared in [MathlibExt/Probability/Distributions/BinomialTail.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BinomialTail.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#binom-tail).

## Binomial upper tail at zero equals one

`P(X ≥ 0) = 1`, for every real `p` (the binomial theorem).

Formalized by `ProbabilityTheory.binomTail_zero`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialTail.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BinomialTail.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#binom-tail-zero).

## Binomial upper tail vanishes beyond $n$

`P(X ≥ k) = 0` for `k > n`.

Formalized by `ProbabilityTheory.binomTail_of_lt`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialTail.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BinomialTail.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#binom-tail-of-lt).

## The tail is nonincreasing in `k`

**The tail is nonincreasing in `k`** for `p ∈ [0, 1]`.

Formalized by `ProbabilityTheory.binomTail_succ_le`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialTail.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BinomialTail.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#binom-tail-succ-le).

## Derivative of the binomial upper tail

**Derivative of the binomial upper tail** in the success probability: for `1 ≤ k ≤ n`,
`d/dp P(Bin(n, p) ≥ k) = n C(n - 1, k - 1) p^(k-1) (1-p)^(n-k)` at every real `p` (the sum
telescopes).

Formalized by `ProbabilityTheory.hasDerivAt_binomTail`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialTail.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BinomialTail.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#has-deriv-at-binom-tail).

## The binomial upper tail is nondecreasing in `p` on `[0, 1]`

**The binomial upper tail is nondecreasing in `p` on `[0, 1]`**, for every `n` and `k`.

Formalized by `ProbabilityTheory.monotoneOn_binomTail`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialTail.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BinomialTail.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#monotone-on-binom-tail).

## The binomial upper tail is strictly increasing in `p` on `[0, 1]`

**The binomial upper tail is strictly increasing in `p` on `[0, 1]`** when `1 ≤ k ≤ n`.

Formalized by `ProbabilityTheory.strictMonoOn_binomTail`, a theorem declared in [MathlibExt/Probability/Distributions/BinomialTail.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Distributions/BinomialTail.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#strict-mono-on-binom-tail).

## Binomial z-score approximation to the motif conservation score

The conserved count
`k` of a motif with `N` occurrences, standardized under `Bin(N, p)`:
`(k - N p) / √(N p (1 - p))`. This is an approximation to Xie et al.'s MCS, not their
exact score.

Formalized by `MathlibExt.Biology.Phylogenetics.MotifConservation.mcsApprox`, a definition declared in [MathlibExt/Biology/Phylogenetics/MotifConservation.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/MotifConservation.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#mcs-approx).

## Motif conservation score approximation is strictly increasing

The MCS approximation is strictly increasing in the conserved count, for `N ≥ 1` and `p ∈ (0, 1)`.

Formalized by `MathlibExt.Biology.Phylogenetics.MotifConservation.mcsApprox_strictMono`, a theorem declared in [MathlibExt/Biology/Phylogenetics/MotifConservation.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/MotifConservation.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#mcs-approx-strict-mono).

## Motif conservation score approximation as a de Moivre–Laplace sum

The MCS approximation of the number of conserved occurrences among the first `n` is the
de Moivre–Laplace standardized sum.

Formalized by `MathlibExt.Biology.Phylogenetics.MotifConservation.mcsApprox_sum_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/MotifConservation.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/MotifConservation.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#mcs-approx-sum-eq).

## De Moivre–Laplace for the MCS approximation

If the conservation indicators of
the occurrences are i.i.d. Bernoulli(`p`) with `0 < p < 1`, then for every `z`,
`P(z ≤ MCS approximation of the first n occurrences)` tends to the standard normal mass of
`[z, ∞)`.

Formalized by `MathlibExt.Biology.Phylogenetics.MotifConservation.tendsto_prob_le_mcsApprox`, a theorem declared in [MathlibExt/Biology/Phylogenetics/MotifConservation.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/MotifConservation.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#tendsto-prob-le-mcs-approx).

## The SiPhy rate matrix

**The SiPhy rate matrix** `Q a b = ω R a b π b` for `a ≠ b` (Garber et al. 2009, Eq. 10),
with rows summing to zero: `ω` times the GTR matrix with exchangeabilities `R` and base
frequencies `π`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.siphyRate`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#siphy-rate).

## SiPhy matrix is a rate matrix

With `ω ≥ 0`, nonnegative `R` and nonnegative `π`, the SiPhy matrix is a rate matrix.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.isRateMatrix_siphyRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#is-rate-matrix-siphy-rate).

## `π` is the equilibrium of the SiPhy matrix

For symmetric `R` it is in detailed balance
with `π`, for every `ω`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.isDetailedBalance_siphyRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#is-detailed-balance-siphy-rate).

## The expected complete-data log-likelihood

**The expected complete-data log-likelihood** of a rate matrix `Q` and root distribution `π`
(Garber et al. 2009, Eq. 6): `∑_{a ≠ b} n a b log Q a b + ∑ a, τ a Q a a + ∑ b, r b log π b`,
for expected substitution counts `n`, expected state durations `τ` and the root posterior `r`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.expectedLogLik`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#expected-log-lik).

## Expected total number of substitutions

The expected total number of substitutions `N = ∑_{a ≠ b} n a b`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.totalCount`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#total-count).

## Weight of a state: substitutions into it plus root posterior

The weight `c b = ∑_{a ≠ b} n a b + r b` of state `b`: substitutions into `b` plus the root
posterior of `b`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.inCount`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#in-count).

## Time-weighted exchange rate into a state

The time-weighted exchange rate into `b`, `e b = ∑_{a ≠ b} τ a R a b`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.exitWeight`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#exit-weight).

## Part of the SiPhy objective depending on the constraint vector

The part of Eq. 6 that depends on `π` (for fixed `ω`):
`∑ b, (c b * log (π b) - d b * π b)`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.piObjective`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#pi-objective).

## Constant $n \log R$ term of the SiPhy objective

The `n log R` constant of Eq. 6.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.exchangeTerm`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#exchange-term).

## Eq. 6 for the SiPhy matrix

For `ω > 0`, positive off-diagonal `R` and positive `π`,
`expectedLogLik = N log ω + ∑_{a ≠ b} n a b log R a b + piObjective c (ω e) π`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.expectedLogLik_siphyRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#expected-log-lik-siphy-rate).

## The SiPhy rate update

**The SiPhy rate update** (Eq. 7, for fixed `π`): `ω = N / ∑ b, e b π b`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.omegaUpdate`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#omega-update).

## The rate update maximizes Eq. 6 over `ω > 0`

**The rate update maximizes Eq. 6 over `ω > 0`** for a fixed positive `π`, when the expected
number of substitutions `N` and the time-weighted rate `∑ b, e b π b` are positive.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.expectedLogLik_le_omegaUpdate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#expected-log-lik-le-omega-update).

## The rate update is the unique maximizer

Any other `ω > 0` gives a strictly smaller
value of Eq. 6.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.expectedLogLik_lt_omegaUpdate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#expected-log-lik-lt-omega-update).

## The Lagrange multiplier of the `π` update exists and is unique

For positive `c` and
nonnegative `d` on a nonempty finite alphabet there is exactly one `γ` with `d b + γ > 0` for
all `b` and `∑ b, c b / (d b + γ) = 1`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.existsUnique_lagrange`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#exists-unique-lagrange).

## The `π` update is the unique maximizer

**The `π` update is the unique maximizer** of `piObjective c d` over the positive
probability vectors: with `γ` as in `existsUnique_lagrange`, every other positive `π` summing to
one has a strictly smaller objective than `b ↦ c b / (d b + γ)`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.piObjective_lt`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#pi-objective-lt).

## The SiPhy constraint-vector update

**The SiPhy constraint-vector update** (Eq. 8, for fixed `ω`):
`π b = c b / (ω e b + γ)`, with `γ` the Lagrange multiplier of `existsUnique_lagrange`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.piUpdate`, a definition declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 340](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L340). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#pi-update).

## The constraint-vector update is the unique maximizer of Eq. 6

**The constraint-vector update is the unique maximizer of Eq. 6** over the positive
probability vectors `π` (the rate matrix `ω R π` and the root distribution both use `π`), for
fixed `ω > 0`, positive off-diagonal `R` and positive weights `c`.

Formalized by `MathlibExt.Biology.Phylogenetics.SiPhy.expectedLogLik_lt_piUpdate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/SiPhy.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/SiPhy.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#expected-log-lik-lt-pi-update).

## Leaf set meeting both sides of a tree edge

Whether the leaf set `S` meets both sides of an edge with leaf set `B` below it, inside a
tree with leaf set `U`: `S ∩ B` and `S ∩ (U \ B)` are nonempty.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.Separates`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#separates).

## Nonnegative edge lengths of a tree

Edge lengths are nonnegative: every dart's undirected edge has nonnegative length.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.NonnegWeights`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#nonneg-weights).

## Total branch length of a tree

The total branch length: half the sum of the edge lengths over the darts, since each
undirected edge is traversed once in each direction.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.totalLength`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#total-length).

## The Branch Length Score

**The Branch Length Score** (unnormalized): the total branch length of the smallest
subtree of `T` connecting the leaves `S`, as half the sum over the darts of the edge length
times the indicator that `S` meets both sides (`edgeSide`) of the dart's edge.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls).

## Normalized branch length score

The normalized Branch Length Score, `bls S T w / totalLength T w`, as reported by
Kheradpour et al. (a fraction of the total branch length).

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.blsFrac`, a definition declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-frac).

## Branch length score is nonnegative for nonnegative edge lengths

The BLS is nonnegative for nonnegative edge lengths.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-nonneg).

## Branch length score is at most the tree length for nonnegative lengths

The BLS is at most the total branch length.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls_le_totalLength`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-le-total-length).

## Monotonicity

With nonnegative edge lengths, more conserving species never lower the
BLS.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls_mono`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-mono).

## Branch length score of the empty set is zero

The BLS of the empty set is `0`.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls_empty`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-empty).

## A single species has BLS `0`

**A single species has BLS `0`** (a motif present in one genome is not conserved).

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls_singleton`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-singleton).

## All species give the whole tree

The BLS of the set of all leaves is the total branch
length.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls_leaves`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-leaves).

## Subadditivity

For sets of species `S`, `S'` that share a species, the subtree
connecting `S ∪ S'` is at most as long as the two subtrees together.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.bls_union_le`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-union-le).

## Normalized branch length score is nonnegative for nonnegative lengths

The normalized BLS is nonnegative.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.blsFrac_nonneg`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-frac-nonneg).

## Normalized branch length score is at most one for nonnegative lengths

The normalized BLS is at most `1` when the tree has positive total length.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.blsFrac_le_one`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#bls-frac-le-one).

## The side of a pendant edge is the singleton of its leaf

The taxa whose leaf is
closer to the leaf vertex than to its neighbor are exactly that leaf's taxon.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.edgeSide_of_leaf`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#edge-side-of-leaf).

## Sum over darts is twice the sum over edges

A sum over darts of a function of the undirected edge is twice the sum over the edges:
the two darts of each edge contribute equally.

Formalized by `Cslib.Bioinformatics.Phylogenetics.BranchLengthScore.dart_sum_edge`, a theorem declared in [CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Phylogenetics/BranchLengthScore.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html#dart-sum-edge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Evolutionary conservation scores](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/evolutionary-conservation-scores/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/evolutionary-conservation-scores)
