---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate, MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate, MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.blockCountingGenerator, MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_of_le, MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_nonneg, MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_two_two, MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate_nonneg, MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.isRateMatrix_blockCountingGenerator
statement: formalized
---

# Λ-coalescents

20 results, 19 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html).

## Pitman's merger rate

**Pitman's merger rate** `λ_{b,k} = ∫ x ^ (k - 2) (1 - x) ^ (b - k) Λ(dx)`: while there are
`b` blocks, the rate at which a given set of `k` of them merges into one block, for
`2 ≤ k ≤ b` (Pitman 1999, Theorem 1; Sagitov 1999). Powers are natural-number powers, so
`0 ^ 0 = 1`. Outside `2 ≤ k ≤ b` no such merger exists, and the rate is defined to be `0`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate).

## Total merger rate of a Λ-coalescent

The **total merger rate** `λ_b = ∑_{k=2}^b (b.choose k) λ_{b,k}` while there are `b`
blocks (Pitman 1999; Berestycki 2009, §3.1).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#total-merger-rate).

## Generator of the Λ-coalescent block-counting process

The generator of the **block-counting process** of the Λ-coalescent on the states
`0, …, n` (state `b` means `b` blocks): from `b` blocks the process jumps to `j < b` blocks at
rate `(b.choose (b + 1 - j)) λ_{b, b + 1 - j}` (a `(b + 1 - j)`-merger), and the diagonal is
`-λ_b`. States `0` and `1` are absorbing (state `0` is never reached from `b ≥ 1`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.blockCountingGenerator`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#block-counting-generator).

## Pitman's integral formula for merger rates when $2 \le k \le b$

The merger rate inside its domain.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_of_le`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate-of-le).

## Nonnegativity of Λ-coalescent merger rates

Merger rates are nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate-nonneg).

## Pair merger rate of a Λ-coalescent

Two blocks merge at rate `Λ [0, 1]`; `Λ` is often normalized to a probability measure,
so that this pair rate is `1` as in Kingman's coalescent.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_two_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate-two-two).

## Nonnegativity of the total merger rate

The total merger rate is nonnegative.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate_nonneg`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#total-merger-rate-nonneg).

## Λ-coalescent block-counting generator is a rate matrix

The block-counting generator is a rate matrix: its jump rates are nonnegative and each
row sums to `0`, since the jump rates out of `b` blocks add up to `λ_b`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.isRateMatrix_blockCountingGenerator`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#is-rate-matrix-block-counting-generator).

## Merger rates are bounded by the total mass of Λ

A merger rate is at most the total mass of `Λ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_le_measure_univ`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate-le-measure-univ).

## Pitman's consistency relation

**Pitman's consistency relation** `λ_{b,k} = λ_{b+1,k} + λ_{b+1,k+1}` for `2 ≤ k ≤ b`
(Pitman 1999; Berestycki 2009, §3.1): a given `k`-set of `b` blocks merges, with an extra
block present, either without it or together with it.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_consistent`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate-consistent).

## Binomial identity behind the total merger rate

The polynomial identity behind the closed form of the total merger rate:
`x ^ 2 ∑_{k=2}^b (b.choose k) x ^ (k - 2) (1 - x) ^ (b - k) = 1 - (1 - x) ^ b -
b x (1 - x) ^ (b - 1)` for every real `x` and every `b` (binomial theorem).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.sq_mul_sum_choose_mul_pow`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#sq-mul-sum-choose-mul-pow).

## The total merger rate in closed form

**The total merger rate in closed form** (Berestycki 2009, §3.1):
`λ_b = (b.choose 2) Λ {0} + ∫_{(0,1]} (1 - (1 - x) ^ b - b x (1 - x) ^ (b - 1)) / x ^ 2 Λ(dx)`.
The atom at `0` (the Kingman part) is split off, so no division by `0` occurs.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#total-merger-rate-eq).

## Recursion for the total merger rate

Adding a block raises the total merger rate by `b λ_{b+1,2}`:
`λ_{b+1} = λ_b + b λ_{b+1,2}`. The new events are exactly the binary mergers of the new block
with one of the `b` old ones (a consequence of the consistency relation).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate_succ`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#total-merger-rate-succ).

## Monotonicity of the total merger rate

The total merger rate `λ_b` is nondecreasing in the number of blocks `b`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate_mono`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#total-merger-rate-mono).

## Uniqueness in Pitman's representation

A finite measure on `[0, 1]` is determined by
its merger rates; indeed by the rates `λ_{k,k} = ∫ x ^ (k - 2) Λ(dx)` of complete mergers,
which are its moments (Pitman 1999, Theorem 1).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.eq_of_mergerRate_eq`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#eq-of-merger-rate-eq).

## Kingman's coalescent

**Kingman's coalescent** is the Λ-coalescent with `Λ = δ₀`: only binary mergers occur,
each pair merging at rate `1` (Pitman 1999; Berestycki 2009, §3.1).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_dirac_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 372](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L372). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate-dirac-zero).

## Total merger rate of Kingman's coalescent

For Kingman's coalescent the total merger rate is the number of pairs, `λ_b = b.choose 2`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate_dirac_zero`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 386](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L386). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#total-merger-rate-dirac-zero).

## Merger rates of the Bolthausen–Sznitman coalescent

The **Bolthausen–Sznitman coalescent** (`Λ` = Lebesgue measure on `[0, 1]`) has merger
rates given by the Beta integral `λ_{b,k} = (k - 2)! (b - k)! / (b - 1)!` for `2 ≤ k ≤ b`
(Bolthausen–Sznitman 1998; Pitman 1999; Berestycki 2009, §3.1).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.mergerRate_volume`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#merger-rate-volume).

## Total merger rate of the Bolthausen–Sznitman coalescent

For the Bolthausen–Sznitman coalescent the total merger rate is `λ_b = b - 1` (`b ≥ 1`).

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescent.totalMergerRate_volume`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescent.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#total-merger-rate-volume).

## Pitman's representation theorem, existence half

**Pitman's representation theorem, existence half** (Pitman 1999, Theorem 1): every
consistent family of nonnegative merger rates `r b k`, `2 ≤ k ≤ b`, is the family of merger
rates `λ_{b,k}` of some finite measure `Λ` on `[0, 1]`. (Uniqueness of `Λ` is
`LambdaCoalescent.eq_of_mergerRate_eq`.)

## Sources

- Pitman (1999), Theorem 1; Hausdorff (1921).

Stated but not proved: `MathlibExt.Biology.PopulationGenetics.Coalescent.LambdaCoalescentWanted.exists_measure_of_consistent` is written with `theorem_wanted` in [WantedExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescentWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Biology/PopulationGenetics/Coalescent/LambdaCoalescentWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html#exists-measure-of-consistent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Λ-coalescents](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/coalescents/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/coalescents)
