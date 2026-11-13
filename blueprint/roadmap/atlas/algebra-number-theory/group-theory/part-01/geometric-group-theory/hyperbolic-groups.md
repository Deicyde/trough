---
declaration: section
origin: cited
lean: Group.IsHyperbolic, Group.IsHyperbolic.fg, Group.IsHyperbolic.of_subsingleton
statement: formalized
proof: formalized
---

# Hyperbolic groups

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/hyperbolic-groups/index.html).

## Word-hyperbolic groups

A group $G$ is word-hyperbolic if there are a finite index set
$\iota$ and a family $(s_i)_{i \in \iota}$ of elements generating $G$ such that $G$, equipped with
the word metric of this generating family, is $\delta$-hyperbolic for some real number $\delta$.

Formalized by `Group.IsHyperbolic`, a definition declared in [MathlibExt/GroupTheory/HyperbolicGroup.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/HyperbolicGroup.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/hyperbolic-groups/index.html#is-hyperbolic).

## Word-hyperbolic groups are finitely generated

Every word-hyperbolic group is finitely
generated.

Formalized by `Group.IsHyperbolic.fg`, a theorem declared in [MathlibExt/GroupTheory/HyperbolicGroup.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/HyperbolicGroup.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/hyperbolic-groups/index.html#fg).

## The trivial group is word-hyperbolic

Every trivial group is word-hyperbolic: the empty
family generates it, and its word metric is $0$-hyperbolic.

Formalized by `Group.IsHyperbolic.of_subsingleton`, a theorem declared in [MathlibExt/GroupTheory/HyperbolicGroup.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/HyperbolicGroup.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/hyperbolic-groups/index.html#of-subsingleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperbolic groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/hyperbolic-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/geometric-group-theory/hyperbolic-groups)
