---
declaration: section
origin: cited
lean: MathlibExt.Biology.Phylogenetics.JukesCantor.jcProb, MathlibExt.Biology.Phylogenetics.JukesCantor.jcRate, MathlibExt.Biology.Phylogenetics.JukesCantor.pDiff, MathlibExt.Biology.Phylogenetics.JukesCantor.jcDistance, MathlibExt.Biology.Phylogenetics.JukesCantor.jcRate_nonneg, MathlibExt.Biology.Phylogenetics.JukesCantor.sum_jcRate, MathlibExt.Biology.Phylogenetics.JukesCantor.sum_jcProb, MathlibExt.Biology.Phylogenetics.JukesCantor.jcProb_nonneg
statement: formalized
proof: formalized
---

# Jukes–Cantor model

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html).

## Jukes–Cantor transition probability

The Jukes–Cantor transition probability from base `i` to base `j` over a branch of length
`t`, with substitution rate `μ`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcProb`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-prob).

## Jukes–Cantor rate matrix

The Jukes–Cantor rate matrix: rate `μ / 3` to each other base, `-μ` on the diagonal.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcRate`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-rate).

## Probability that the ends of a branch differ

The probability that the two ends of a branch of length `t` carry different bases, given
base `i` at the start.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.pDiff`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#p-diff).

## Jukes–Cantor distance

The Jukes–Cantor distance: the expected number of substitutions per site corresponding to a
proportion `p` of differing sites. Meaningful only for `0 ≤ p < 3/4`; outside that range the
value is Lean's totalized logarithm, not a distance (at `p = 3/4` it is `0`).

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcDistance`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-distance).

## Nonnegativity of off-diagonal Jukes–Cantor rates

Off-diagonal Jukes–Cantor rates are nonnegative when `0 ≤ μ`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcRate_nonneg`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-rate-nonneg).

## Rows of the Jukes–Cantor rate matrix sum to zero

Each row of the Jukes–Cantor rate matrix sums to `0`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.sum_jcRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#sum-jc-rate).

## Rows of the Jukes–Cantor transition matrix sum to one

Each row of the Jukes–Cantor transition matrix sums to `1`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.sum_jcProb`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#sum-jc-prob).

## Nonnegativity of Jukes–Cantor transition probabilities

The Jukes–Cantor transition probabilities are nonnegative when `0 ≤ μ * t`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcProb_nonneg`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-prob-nonneg).

## Jukes–Cantor transition matrix at time zero is the identity

At time `0` the Jukes–Cantor transition matrix is the identity.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcProb_zero`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-prob-zero).

## Chapman–Kolmogorov equation

**Chapman–Kolmogorov equation** for the Jukes–Cantor model.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.sum_jcProb_mul_jcProb`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#sum-jc-prob-mul-jc-prob).

## Right-hand side of the Jukes–Cantor forward equation in closed form

The right-hand side of the forward equation, in closed form.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.sum_jcProb_mul_jcRate`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#sum-jc-prob-mul-jc-rate).

## Kolmogorov forward equation

**Kolmogorov forward equation** for the Jukes–Cantor model:
`d/dt P(t) = P(t) Q` with `Q = jcRate μ`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.hasDerivAt_jcProb`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#has-deriv-at-jc-prob).

## Closed form of the Jukes–Cantor difference probability

The probability that the two ends of a branch differ is `3/4 · (1 - exp (-4 μ t / 3))`,
whatever the starting base.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.pDiff_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#p-diff-eq).

## Jukes–Cantor transition matrix as a stochastic matrix

The Jukes–Cantor transition matrix over a branch with `0 ≤ μ * t`, packaged as a
`StochasticMatrix` on the four states `Fin (3 + 1)` so that the finite Markov-chain API
(matrix powers, stationarity, detailed balance) applies to it.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcStochasticMatrix`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-stochastic-matrix).

## Chapman–Kolmogorov equation for the Jukes–Cantor chain

The `n`-step matrix of the Jukes–Cantor chain observed every `t` time units is the
transition matrix over the branch length `n * t` (Chapman–Kolmogorov).

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.matPow_jcStochasticMatrix`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#mat-pow-jc-stochastic-matrix).

## Detailed balance of the Jukes–Cantor chain

The uniform distribution satisfies detailed balance with the Jukes–Cantor matrix (the
matrix is symmetric), hence is stationary.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.detailedBalance_jcStochasticMatrix`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#detailed-balance-jc-stochastic-matrix).

## Nonnegativity of the Jukes–Cantor difference probability

The probability that the ends of a branch differ is nonnegative when `0 ≤ μ * t`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.pDiff_nonneg`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#p-diff-nonneg).

## Jukes–Cantor difference probability is below 3/4

The probability that the ends of a branch differ is below the saturation value `3/4`, for
all real `μ` and `t` (it is negative when `μ * t < 0`, see `pDiff_mem_Ico`).

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.pDiff_lt_three_quarters`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#p-diff-lt-three-quarters).

## Jukes–Cantor difference probability lies in (0, 3/4)

For `0 ≤ μ * t` the probability that the ends of a branch differ lies in `[0, 3/4)`, the
domain of `jcDistance`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.pDiff_mem_Ico`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#p-diff-mem-ico).

## The Jukes–Cantor distance correction

`-(3/4) · log (1 - 4/3 · pDiff μ t i) = μ * t`,
the expected number of substitutions per site along the branch.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcDistance_pDiff`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-distance-p-diff).

## Jukes–Cantor rate matrix as a matrix

The Jukes–Cantor rate matrix as a `Matrix`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcRateMatrix`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-rate-matrix).

## Eigenbasis of the Jukes–Cantor rate matrix

An eigenbasis of the Jukes–Cantor rate matrix, as columns: the constant vector (eigenvalue
`0`) and three vectors with zero sum (eigenvalue `-4 μ / 3`).

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcEigenbasis`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-eigenbasis).

## Invertible Jukes–Cantor eigenbasis

The eigenbasis as a unit, with its explicit inverse.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcEigenbasisUnit`, a definition declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-eigenbasis-unit).

## Diagonalization of the Jukes–Cantor rate matrix

Diagonalization of `t • jcRateMatrix μ`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.smul_jcRateMatrix_eq`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#smul-jc-rate-matrix-eq).

## The Jukes–Cantor transition matrix is the matrix exponential of the rate matrix

`jcProb μ t = exp (t • jcRateMatrix μ)`.

Formalized by `MathlibExt.Biology.Phylogenetics.JukesCantor.jcProb_eq_exp`, a theorem declared in [MathlibExt/Biology/Phylogenetics/JukesCantor.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/JukesCantor.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html#jc-prob-eq-exp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jukes–Cantor model](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/jukes-cantor-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/jukes-cantor-model)
