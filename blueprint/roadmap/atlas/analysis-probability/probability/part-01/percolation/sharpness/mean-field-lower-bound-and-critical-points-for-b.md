---
declaration: section
origin: cited
lean: StatMech.Sharpness.item1_meanfield_lower_bound, StatMech.Sharpness.pc_le_tildePc, StatMech.Sharpness.tildePc_le_pc
statement: formalized
proof: formalized
---

# Mean-field lower bound and critical points for Bernoulli percolation

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/mean-field-lower-bound-and-critical-points-for-b/index.html).

## B. The mean-field lower bound

## Mean-field lower bound for $\theta(p)$ from a differential inequality

The mean-field lower bound `θ(p) ≥ (p - p₀)/(p(1 - p₀))` from the differential inequality for
crossing probabilities. Reference: H. Duminil-Copin, V. Tassion, "A new proof of the sharpness of
the phase transition for Bernoulli percolation and the Ising model", Comm. Math. Phys. 343 (2016)
725–745.

Formalized by `StatMech.Sharpness.item1_meanfield_lower_bound`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/PercolationMeanfield.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/PercolationMeanfield.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/mean-field-lower-bound-and-critical-points-for-b/index.html#item1-meanfield-lower-bound).

## $p_c \le \tilde p_c$ if $\theta > 0$ above $\tilde p_c$

`p_c ≤ p̃_c` when `θ` is positive above `p̃_c`. See also `Percolation.pc_le_tildePc`
(MathlibExt), stated with hypotheses on `θ(1)` and on `(p̃_c, 1)`.

Formalized by `StatMech.Sharpness.pc_le_tildePc`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/PercolationMeanfield.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/PercolationMeanfield.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/mean-field-lower-bound-and-critical-points-for-b/index.html#pc-le-tilde-pc).

## $\tilde p_c \le p_c$ if $\theta = 0$ on the set defining $\tilde p_c$

`p̃_c ≤ p_c` when `θ` vanishes on the set defining `p̃_c`. See also `Percolation.tildePc_le_pc`
(MathlibExt), stated with exponential decay of crossing probabilities.

Formalized by `StatMech.Sharpness.tildePc_le_pc`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/PercolationMeanfield.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/PhyslibExt/CondensedMatter/IsingModel/Sharpness/PercolationMeanfield.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/mean-field-lower-bound-and-critical-points-for-b/index.html#tilde-pc-le-pc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mean-field lower bound and critical points for Bernoulli percolation](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/mean-field-lower-bound-and-critical-points-for-b/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/percolation/sharpness/mean-field-lower-bound-and-critical-points-for-b)
