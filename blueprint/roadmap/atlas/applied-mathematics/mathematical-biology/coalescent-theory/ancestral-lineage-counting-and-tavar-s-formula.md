---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.wfLineageProb, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.wfLineageMatrix, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingGenerator, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.tavareProb, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.tendsto_smul_wfLineageMatrix_sub_one, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.tendsto_wfLineageMatrix_pow_floor, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingRightEigen, MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingLeftEigen
statement: formalized
proof: formalized
---

# Ancestral lineage counting and Tavaré's formula

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html).

## Wright–Fisher transition probability of the lineage count

One-generation transition probability of the ancestral lineage count in a neutral
Wright–Fisher population of `M` gene copies: `k` lineages pick their parents uniformly and
independently among `M` copies, and `j` distinct parents occur with probability
`stirlingSecond k j * M.descFactorial j / M ^ k`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.wfLineageProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#wf-lineage-prob).

## Wright–Fisher transition matrix of the lineage count

The one-generation transition matrix of the ancestral lineage count of a sample of at most
`n` gene copies in a Wright–Fisher population of `M` copies; row `k`, column `j` is
`wfLineageProb M k j`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.wfLineageMatrix`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#wf-lineage-matrix).

## Generator of Kingman's block-counting process

The rate matrix of Kingman's block-counting (pure-death) process on `{0, …, n}`: `k`
lineages become `k - 1` at rate `k.choose 2`, time in units of `M = 2N` generations.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingGenerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#block-counting-generator).

## Tavaré's formula for the number of ancestral lineages

Tavaré's closed form for the probability that `i` lineages of Kingman's coalescent have
`j` ancestors `t` time units (`2N` generations each) earlier, for `1 ≤ j ≤ i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.tavareProb`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#tavare-prob).

## Scaled Wright–Fisher lineage matrix converges to Kingman's generator

The scaled one-generation increment `M • (wfLineageMatrix n M - 1)` converges entrywise to
the block-counting generator: `k` lineages coalesce to `k - 1` with probability
`(k.choose 2) / M + o(1/M)`, and to fewer with probability `O(1/M²)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.tendsto_smul_wfLineageMatrix_sub_one`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#tendsto-smul-wf-lineage-matrix-sub-one).

## Kingman's theorem for the lineage count

For `t ≥ 0`, the `⌊t M⌋`-generation transition
matrix of the Wright–Fisher ancestral lineage count converges, as the population size `M`
tends to infinity, to the transition matrix `exp (t • G)` of the pure-death process with rates
`k.choose 2`.

## Sources

- Kingman (1982); Durrett (2008), ch. 1. Proves the deferred entry `tendsto_wfLineageMatrix_pow_floor`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.tendsto_wfLineageMatrix_pow_floor`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#tendsto-wf-lineage-matrix-pow-floor).

## Right eigenvectors of Kingman's block-counting generator

Right eigenvectors of the block-counting generator, as columns: column `k` has entries
`i_{(k)} / i^{(k)}` (falling over rising factorial) and eigenvalue `-(k.choose 2)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingRightEigen`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#block-counting-right-eigen).

## Left eigenvectors of Kingman's block-counting generator

Left eigenvectors of the block-counting generator, as rows: row `0` is the indicator of
state `0`, and for `1 ≤ k` row `k` has entries `(2k-1) (-1)^{k-j} j^{(k-1)} / (j! (k-j)!)` for
`j ≤ k` and `0` for `j > k`; the eigenvalue is `-(k.choose 2)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingLeftEigen`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#block-counting-left-eigen).

## Eigenvalues of Kingman's block-counting generator

The eigenvalues of the block-counting generator, `-(k.choose 2)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingEigenvalue`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#block-counting-eigenvalue).

## Right eigenvector equation for the block-counting generator

The columns of `blockCountingRightEigen n` are right eigenvectors: `G V = V D`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingGenerator_mul_rightEigen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#block-counting-generator-mul-right-eigen).

## Left eigenvector equation for the block-counting generator

The rows of `blockCountingLeftEigen n` are left eigenvectors: `W G = D W`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingLeftEigen_mul_generator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#block-counting-left-eigen-mul-generator).

## Left and right eigenvector matrices are mutually inverse

The left and right eigenvector matrices are mutually inverse: `W V = 1`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.blockCountingLeftEigen_mul_rightEigen`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#block-counting-left-eigen-mul-right-eige).

## Spectral decomposition of the block-counting transition matrix

The spectral decomposition of the transition matrix of the block-counting process:
`exp (t • G) = V diag(exp (-(k.choose 2) t)) W`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.exp_smul_blockCountingGenerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 488](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L488). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#exp-smul-block-counting-generator).

## Tavaré's formula

The transition probabilities of Kingman's block-counting process
from `i` to `j` lineages in time `t`, for `1 ≤ j ≤ i ≤ n`, are given by `tavareProb`.

## Sources

- Tavaré (1984). Proves the deferred entry `exp_blockCountingGenerator_apply`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.exp_blockCountingGenerator_apply`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#exp-block-counting-generator-apply).

## Truncation consistency

For `n ≤ N`, the top-left `(n + 1) × (n + 1)` block of the
transition matrix `exp (t • G)` of the block-counting process on `{0, …, N}` is the transition
matrix of the process on `{0, …, n}` (the process only moves down). Holds for every real `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.exp_smul_blockCountingGenerator_castLE`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 548](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L548). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#exp-smul-block-counting-generator-cast-l).

## The block-counting process never gains lineages

The block-counting process never gains lineages: `exp (t • G) i j = 0` for `i < j`. Holds
for every real `t`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.KingmanBlockCounting.exp_smul_blockCountingGenerator_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/PopulationGenetics/Coalescent/BlockCounting.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html#exp-smul-block-counting-generator-of-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ancestral lineage counting and Tavaré's formula](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/coalescent-theory/ancestral-lineage-counting-and-tavar-s-formula)
