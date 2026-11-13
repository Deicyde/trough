---
declaration: section
origin: cited
lean: SimpleGraph.exists_isIndepSet_caroWei, SimpleGraph.caroWei_le_indepNum
statement: formalized
proof: formalized
---

# Caro–Wei theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/caro-wei-theorem/index.html).

## Caro–Wei bound

Every finite graph has an independent set of size at
least the sum over its vertices of the reciprocal of one more than the
degree.

Formalized by `SimpleGraph.exists_isIndepSet_caroWei`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/CaroWei.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CaroWei.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/caro-wei-theorem/index.html#exists-is-indep-set-caro-wei).

## Caro–Wei bound for the independence number

For every finite simple graph $G$, the
independence number of $G$ is at least $\sum_{v} \frac{1}{\deg(v) + 1}$, the sum running over all
vertices $v$ of $G$.

Formalized by `SimpleGraph.caroWei_le_indepNum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/CaroWei.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/CaroWei.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/caro-wei-theorem/index.html#caro-wei-le-indep-num).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Caro–Wei theorem](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/caro-wei-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/independence-and-domination/caro-wei-theorem)
