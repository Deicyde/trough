---
declaration: section
origin: cited
lean: ProbabilityTheory.measurable_polyaUrnPredictive, ProbabilityTheory.blackwellMacQueen, ProbabilityTheory.isProbabilityMeasure_blackwellMacQueen, ProbabilityTheory.blackwellMacQueen_succ_pi, ProbabilityTheory.polyaUrnPredictive_comp_perm, ProbabilityTheory.map_perm_blackwellMacQueen, ProbabilityTheory.tiePartition, ProbabilityTheory.mem_part_tiePartition
statement: formalized
proof: formalized
---

# Blackwell–MacQueen urn

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html).

## Measurability of the Pólya urn predictive law

The predictive law depends measurably on the previous draws.

Formalized by `ProbabilityTheory.measurable_polyaUrnPredictive`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#measurable-polya-urn-predictive).

## Blackwell–MacQueen urn

The **Blackwell–MacQueen urn** with parameter `α` and base measure `H`: the joint law of the
first `n` draws, where draw `n` has law `polyaUrnPredictive α H xs` given the previous draws
`xs` (Blackwell–MacQueen 1973).

Formalized by `ProbabilityTheory.blackwellMacQueen`, a definition declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#blackwell-mac-queen).

## Blackwell–MacQueen urn law is a probability measure

The urn law is a probability measure.

Formalized by `ProbabilityTheory.isProbabilityMeasure_blackwellMacQueen`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#is-probability-measure-blackwell-mac-que).

## The predictive rule of the urn

`P(X₀ ∈ A₀, …, X_n ∈ A_n)` is the integral over
`A₀ × ⋯ × A_{n-1}` of the predictive probability `(α H(A_n) + #{i < n | xᵢ ∈ A_n}) / (α + n)`.

Formalized by `ProbabilityTheory.blackwellMacQueen_succ_pi`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#blackwell-mac-queen-succ-pi).

## Pólya urn predictive law is invariant under reordering

The predictive law does not depend on the order of the previous draws.

Formalized by `ProbabilityTheory.polyaUrnPredictive_comp_perm`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#polya-urn-predictive-comp-perm).

## Exchangeability of the Blackwell–MacQueen urn

**Exchangeability of the Blackwell–MacQueen urn** (Blackwell–MacQueen 1973): relabeling the
draws by a permutation does not change their joint law.

Formalized by `ProbabilityTheory.map_perm_blackwellMacQueen`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#map-perm-blackwell-mac-queen).

## Tie partition of a sequence of draws

The partition of the indices `{0, …, n-1}` into groups of equal entries of `xs`.

Formalized by `ProbabilityTheory.tiePartition`, a definition declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#tie-partition).

## Blocks of the tie partition are classes of equal entries

Two indices lie in the same block of `tiePartition xs` iff the entries agree.

Formalized by `ProbabilityTheory.mem_part_tiePartition`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#mem-part-tie-partition).

## Characterization of the tie partition

`tiePartition xs = π` iff equal entries are exactly the pairs in a common block of `π`.

Formalized by `ProbabilityTheory.tiePartition_eq_iff`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#tie-partition-eq-iff).

## Tie partition after forgetting the last draw

Forgetting the last draw restricts the tie partition to the earlier draws.

Formalized by `ProbabilityTheory.comap_castSucc_tiePartition_snoc`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#comap-cast-succ-tie-partition-snoc).

## Last draw opens a new block iff it is new

Where the last draw sits: a new table iff it differs from all earlier draws.

Formalized by `ProbabilityTheory.tiePartition_snoc_eq_seat_none_iff`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 481](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L481). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#tie-partition-snoc-eq-seat-none-iff).

## Last draw joins a block iff it matches that block

Where the last draw sits: at the table `B` iff it equals the earlier draws in `B`.

Formalized by `ProbabilityTheory.tiePartition_snoc_eq_seat_some_iff`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#tie-partition-snoc-eq-seat-some-iff).

## Measurability of the tie partition event

The event that the draws have a given tie partition is measurable.

Formalized by `ProbabilityTheory.measurableSet_tiePartition_eq`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#measurable-set-tie-partition-eq).

## The ties of the Blackwell–MacQueen urn follow the Chinese restaurant process

**The ties of the Blackwell–MacQueen urn follow the Chinese restaurant process** (Pitman
2006, §3.1): for an atomless base measure, the partition of the first `n` draws into groups of
equal values has the law `α^{|π|} ∏_{B ∈ π} (|B| - 1)! / α^{(n)}`.

Formalized by `ProbabilityTheory.blackwellMacQueen_tiePartition`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 591](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L591). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#blackwell-mac-queen-tie-partition).

## Moments of the Dirichlet process for at most two draws

For `n ≤ 2`,
`E[∏_{i<n} G(Aᵢ)] = P(X₀ ∈ A₀, …, X_{n-1} ∈ A_{n-1})` for the Blackwell–MacQueen urn. The case
`n ≥ 3` is the wanted `lintegral_dirichletProcess_prod`.

Formalized by `ProbabilityTheory.lintegral_dirichletProcess_prod_of_le_two`, a theorem declared in [MathlibExt/Probability/BlackwellMacQueen.lean, line 635](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/BlackwellMacQueen.lean#L635). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html#lintegral-dirichlet-process-prod-of-le-t).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Blackwell–MacQueen urn](https://deicyde.github.io/atlas-lean/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/bayesian-statistics/blackwell-macqueen-urn)
