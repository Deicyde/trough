---
declaration: section
origin: cited
lean: StatMech.Ising.ifk_isingProb_positively_associated
statement: formalized
proof: formalized
---

# Correlation inequalities for spin systems: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/index.html).

Inequalities for the correlations of ferromagnetic Ising models: the Griffiths (GKS) and FKG inequalities, monotonicity in the couplings and the temperature, and the Griffiths–Hurst–Sherman inequality with its consequences for the magnetization.

## FKG inequality

**FKG inequality** for the Ising model. For `β ≥ 0` and any field, increasing functions are
positively correlated under the Ising Gibbs distribution on a finite graph.

C. M. Fortuin, P. W. Kasteleyn and J. Ginibre, *Correlation inequalities on some partially
ordered sets*, Comm. Math. Phys. 22 (1971). See also
`MathlibExt.Probability.CorrelationInequalities.FKG`.

Formalized by `StatMech.Ising.ifk_isingProb_positively_associated`, a theorem declared in [PhyslibExt/CondensedMatter/IsingModel/IsingFKGLayer.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/IsingFKGLayer.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/index.html#ifk-ising-prob-positively-associated).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Correlation inequalities for spin systems](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/correlation-inequalities/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/correlation-inequalities)
