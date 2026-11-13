---
declaration: section
origin: cited
lean: StatMech.Onsager.ons_criticalLogBound, StatMech.Onsager.ons_criticalInnerBound
statement: formalized
proof: formalized
---

# Continuity of Onsager's pressure at the critical point

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/continuity-of-onsager-s-pressure-at-the-critical/index.html).

## A. The integrand near the critical point

## Integrable dominating function for log g near the critical point

The dominating function `log 9 + log 2 + |log (1 - cos y)|` for `log g` near `β_c`.

Formalized by `StatMech.Onsager.ons_criticalLogBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalIntegrability.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalIntegrability.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/continuity-of-onsager-s-pressure-at-the-critical/index.html#ons-critical-log-bound).

## Uniform bound constant for the inner integrals near β_c

A uniform bound for the inner integrals `∫ log g dk₂` near `β_c`.

Formalized by `StatMech.Onsager.ons_criticalInnerBound`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalIntegrability.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Onsager/CriticalIntegrability.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/continuity-of-onsager-s-pressure-at-the-critical/index.html#ons-critical-inner-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Continuity of Onsager's pressure at the critical point](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/continuity-of-onsager-s-pressure-at-the-critical/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/exact-solutions/onsager-s-solution-of-the-two-dimensional-ising/continuity-of-onsager-s-pressure-at-the-critical)
