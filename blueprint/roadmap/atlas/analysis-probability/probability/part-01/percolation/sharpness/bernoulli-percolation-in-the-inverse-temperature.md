---
declaration: section
origin: cited
lean: StatMech.Sharpness.pBeta, StatMech.Sharpness.betaTildeC
statement: formalized
proof: formalized
---

# Bernoulli percolation in the inverse-temperature parametrization

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/bernoulli-percolation-in-the-inverse-temperature/index.html).

## A. The parametrization

## Bond probability $p(\beta) = 1 - e^{-\beta J}$

The bond-percolation edge probability `p(β) = 1 - exp(-βJ)` attached to coupling `J` at inverse
temperature `β`.

Formalized by `StatMech.Sharpness.pBeta`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SharpnessBeta.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SharpnessBeta.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/bernoulli-percolation-in-the-inverse-temperature/index.html#p-beta).

## Auxiliary critical inverse temperature from $\tilde p_c$

The auxiliary critical inverse temperature `β̃_c = -log(1 - p̃_c)/J`, so that `p(β̃_c) = p̃_c`.

Formalized by `StatMech.Sharpness.betaTildeC`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/SharpnessBeta.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/SharpnessBeta.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/bernoulli-percolation-in-the-inverse-temperature/index.html#beta-tilde-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernoulli percolation in the inverse-temperature parametrization](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/bernoulli-percolation-in-the-inverse-temperature/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/sharpness/bernoulli-percolation-in-the-inverse-temperature)
