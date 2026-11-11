---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher, MathlibExt.Biology.PopulationGenetics.WrightFisherChain.coe_z, MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher_prob, MathlibExt.Biology.PopulationGenetics.WrightFisherChain.heterozygosity, MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher_prob_eq_binomial, MathlibExt.Biology.PopulationGenetics.WrightFisherChain.sum_prob_mul_wrightFisher, MathlibExt.Biology.PopulationGenetics.WrightFisherChain.sum_matPow_mul_wrightFisher, MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher_prob_zero_zero
statement: formalized
proof: formalized
---

# Wright–Fisher Markov chain

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html).

## Neutral Wright–Fisher transition matrix

The neutral Wright–Fisher transition matrix on `M` gene copies (Ewens 2004, ch. 3):
`P(i, j) = (M choose j) (i/M)^j (1 - i/M)^(M - j)`, the binomial law `Bin(M, i/M)` of the
number of `A` copies among `M` draws with replacement. The model needs `M ≥ 1`; for `M = 0`
(where `i / M` is Lean's junk value `0`) the matrix is the one-state chain, which is
`Bin(0, p) = δ₀` for every `p`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher`, a definition declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#wright-fisher).

## Allele frequency of a Wright–Fisher state

The frequency of allele `A` in state `i` is `bernstein.z i = i / M` (for `M = 0` it is
Lean's junk value `i / 0 = 0`).

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.coe_z`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#coe-z).

## Entries of the Wright–Fisher matrix

Entries of the Wright–Fisher matrix.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher_prob`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#wright-fisher-prob).

## Heterozygosity of a Wright–Fisher state

The heterozygosity `H(j) = 2 (j/M) (1 - j/M)` of state `j`: the probability that two
gene copies drawn with replacement carry different alleles.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.heterozygosity`, a definition declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#heterozygosity).

## Wright–Fisher rows are binomial laws

The rows of the Wright–Fisher matrix are Mathlib's binomial laws `Bin(M, i/M)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher_prob_eq_binomial`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#wright-fisher-prob-eq-binomial).

## One-step martingale property of the Wright–Fisher allele count

Martingale property of the allele count (one step): `∑ j, P(i, j) j = i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.sum_prob_mul_wrightFisher`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#sum-prob-mul-wright-fisher).

## Multi-step martingale property of the Wright–Fisher allele count

Martingale property of the allele count (`t` steps): `∑ j, P^t(i, j) j = i`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.sum_matPow_mul_wrightFisher`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#sum-mat-pow-mul-wright-fisher).

## Loss of an allele is absorbing in the Wright–Fisher chain

The state `0` (allele `A` lost) is absorbing.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher_prob_zero_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#wright-fisher-prob-zero-zero).

## Fixation of an allele is absorbing in the Wright–Fisher chain

The state `M` (allele `A` fixed) is absorbing.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.wrightFisher_prob_last_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#wright-fisher-prob-last-last).

## One-step decay of heterozygosity under Wright–Fisher drift

Heterozygosity decays by the factor `1 - 1/M` per generation (one step). For `M = 0` both
sides are `0` because `H ≡ 0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.sum_prob_mul_heterozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#sum-prob-mul-heterozygosity).

## Geometric decay of heterozygosity under Wright–Fisher drift

Heterozygosity decays geometrically (Ewens 2004, ch. 3):
`∑ j, P^t(i, j) H(j) = (1 - 1/M)^t H(i)`. For `M = 0` both sides are `0` because `H ≡ 0`
(the factor `1 - 1/0 = 1` is then irrelevant).

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.sum_matPow_mul_heterozygosity`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#sum-mat-pow-mul-heterozygosity).

## Interior Wright–Fisher states vanish in the limit

The probability of sitting in an interior state `0 < j < M` at time `t` tends to `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.tendsto_matPow_interior`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#tendsto-mat-pow-interior).

## Fixation probability in the Wright–Fisher chain

Fixation probability (Ewens 2004, ch. 3): started from `i` copies, allele `A` is fixed with
limiting probability `i / M`, i.e. `P^t(i, M) → i / M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.tendsto_matPow_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#tendsto-mat-pow-last).

## Limiting loss probability of the Wright–Fisher transition matrix

Loss probability: started from `i` copies, allele `A` is lost with limiting probability
`1 - i / M`, i.e. `P^t(i, 0) → 1 - i / M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.tendsto_matPow_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#tendsto-mat-pow-zero).

## Limiting fixation probability of a Wright–Fisher chain

Path-level fixation probability: if `X` is a Wright–Fisher chain (in the sense of
`IsFiniteMarkovChain`) started from `i` copies, then `P(X_t = M) → i / M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.tendsto_measureReal_eq_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#tendsto-measure-real-eq-last).

## Almost-sure absorption of the Wright–Fisher chain

Almost-sure absorption: a Wright–Fisher chain is almost surely eventually absorbed in `0`
or `M` (Ewens 2004, ch. 3).

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.measure_exists_absorbed`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#measure-exists-absorbed).

## Fixation probability of a Wright–Fisher chain

Path-level fixation probability (Ewens 2004, ch. 3): a Wright–Fisher chain started from `i`
copies ever reaches `M` (fixation of `A`) with probability `i / M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.measureReal_exists_eq_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#measure-real-exists-eq-last).

## Loss probability of a Wright–Fisher chain

Path-level loss probability: a Wright–Fisher chain started from `i` copies ever reaches `0`
(loss of `A`) with probability `1 - i / M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.measureReal_exists_eq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean, line 493](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChain.lean#L493). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#measure-real-exists-eq-zero).

## Finite Wright–Fisher chain is absorbed almost surely

The finite Wright–Fisher chain under the canonical Markov law almost surely
reaches an endpoint. The law and chain are not premises supplied by a caller.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.measure_markovChainMeasure_exists_absorbed`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChainConstruction.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChainConstruction.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#measure-markov-chain-measure-exists-abso).

## Fixation probability of the finite Wright–Fisher chain

Under the canonical finite Wright–Fisher law, the probability of ever fixing
at `M` equals the initial allele frequency `i / M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.measureReal_markovChainMeasure_exists_eq_last`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChainConstruction.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChainConstruction.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#measure-real-markov-chain-measure-exists).

## Loss probability of an allele in the finite Wright–Fisher chain

Under the canonical finite Wright–Fisher law, the probability of ever losing
the allele at `0` equals `1 - i / M`.

Formalized by `MathlibExt.Biology.PopulationGenetics.WrightFisherChain.measureReal_markovChainMeasure_exists_eq_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/WrightFisherChainConstruction.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/WrightFisherChainConstruction.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html#measure-real-markov-chain-measure-exists-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wright–Fisher Markov chain](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/wright-fisher-markov-chain/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/wright-fisher-markov-chain)
