---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.PopulationStructure.LiStephens.Obs, Cslib.Bioinformatics.PopulationStructure.LiStephens.obs, Cslib.Bioinformatics.PopulationStructure.LiStephens.trans, Cslib.Bioinformatics.PopulationStructure.LiStephens.emit, Cslib.Bioinformatics.PopulationStructure.LiStephens.hmm, Cslib.Bioinformatics.PopulationStructure.LiStephens.trans_row_sum, Cslib.Bioinformatics.PopulationStructure.LiStephens.init_sum, Cslib.Bioinformatics.PopulationStructure.LiStephens.emit_sum_bool
statement: formalized
proof: formalized
---

# Li–Stephens haplotype copying model

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html).

## Site observation in the Li–Stephens model

The observation at a site: the column of reference alleles and the target allele.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.Obs`, an abbreviation declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#obs).

## Observation sequence of a reference panel and target haplotype

The observation sequence for the reference panel `H` (haplotype `k` carries allele
`H k t` at site `t`) and the target haplotype `x`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.obs`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#obs-2).

## Li–Stephens copying transition probability

The copying transition probability: switch with probability `ρ` to a uniformly random
reference haplotype (possibly the same one), otherwise keep copying `k`:
`(1 - ρ) [k = k'] + ρ / K`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.trans`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#trans).

## Li–Stephens emission probability

The emission probability: `1 - ε` if the target allele equals the allele of the copied
haplotype `k`, and the mismatch probability `ε` otherwise.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.emit`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#emit).

## The Li–Stephens copying model

**The Li–Stephens copying model** with `K` reference haplotypes, switch probability `ρ` and
mismatch probability `ε`, as a hidden Markov model with a uniform initial copied haplotype.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.hmm`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#hmm).

## Li–Stephens transition rows sum to one

Each transition row sums to `1` (when `K` is invertible in `R`, e.g. `K ≠ 0` over `ℝ`).

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.trans_row_sum`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#trans-row-sum).

## Uniform initial law over haplotypes sums to one

The initial law (uniform over the `K` haplotypes) sums to `1`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.init_sum`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#init-sum).

## Biallelic emission probabilities sum to one

With biallelic sites, the two emission probabilities at a site sum to `1` over the target
allele, for each fixed panel column `col` (the emissions are conditional on the panel).

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.emit_sum_bool`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#emit-sum-bool).

## One step of the collapsed forward recursion

One step of the collapsed forward recursion on the previous site's forward variables `v`,
at output state `k`: `e_k ((1 - ρ) v k + ρ (∑ j, v j) / K)`. This is the pointwise
specification; each call evaluates the length-`K` sum, so use `fastStepTab` for the `O(K)`
per-site step.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.fastStep`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#fast-step).

## Forward variables of the collapsed recursion

The forward variables of the collapsed recursion, as a function of site and state. This is
the untabulated specification (it re-evaluates earlier sites inside each sum); `fastForwardTab`
is the `O(t K)` implementation.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.fastForward`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#fast-forward).

## Collapse of the sum over predecessor haplotypes

The sum over predecessors collapses: `∑ j, v j * trans ρ j k = (1 - ρ) v k + ρ (∑ v) / K`.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.sum_mul_trans`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#sum-mul-trans).

## The collapsed forward recursion computes the forward variables

**The collapsed forward recursion computes the forward variables** of the Li–Stephens HMM.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.fastForward_eq_forward`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#fast-forward-eq-forward).

## The likelihood of the target haplotype

**The likelihood of the target haplotype** (given the panel) is the sum of the collapsed
forward variables.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.likelihood_eq_sum_fastForward`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#likelihood-eq-sum-fast-forward).

## Tabulated O(K) forward step

One tabulated `O(K)` step: the total of the previous table is computed once.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.fastStepTab`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#fast-step-tab).

## Tabulated O(K) forward variables

The `O(K)` forward variables, tabulated site by site: `O(t K)` operations in total.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.fastForwardTab`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#fast-forward-tab).

## Tabulated recursion computes the Li–Stephens forward variables

The tabulated `O(K)` recursion computes the forward variables of the Li–Stephens HMM.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.fastForwardTab_get`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#fast-forward-tab-get).

## The tabulated Li–Stephens likelihood

**The tabulated Li–Stephens likelihood** in `O(t K)` operations.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.likelihoodTab`, a definition declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#likelihood-tab).

## Tabulated recursion computes the haplotype likelihood

The tabulated `O(K)` recursion computes the likelihood of the target haplotype.

Formalized by `Cslib.Bioinformatics.PopulationStructure.LiStephens.likelihoodTab_eq`, a theorem declared in [CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationStructure/LiStephens.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html#likelihood-tab-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Li–Stephens haplotype copying model](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-structure/li-stephens-haplotype-copying-model)
