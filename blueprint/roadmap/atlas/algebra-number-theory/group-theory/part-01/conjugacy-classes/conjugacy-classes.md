---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.CommProbClosedWanted.GroupTheory.commProb_closed
statement: formalized
---

# Conjugacy classes: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/index.html).

Conjugacy classes of groups as a structural invariant: class sizes and breadth, the class number, commuting probability, Thompson's conjecture on class sizes, products of conjugacy classes, and relations between class sizes and group structure; class sizes of p-groups go to Finite p-groups, and character-theoretic class arguments to Characters of finite groups.

## The set of commuting probabilities is closed

Let $\Pr(G)$ denote the commuting
probability of a group $G$: $\Pr(G) = |\{(x, y) \in G \times G : xy = yx\}| / |G|^2$ if $G$ is
finite, and $\Pr(G) = 0$ if $G$ is infinite. Then the set $\{\Pr(G) : G \text{ a group}\}$ is a
closed subset of $\mathbb{R}$.

## Sources

- https://arxiv.org/abs/2201.09402. Problem `commProb_closed` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.CommProbClosedWanted.GroupTheory.commProb_closed` is written with `theorem_wanted` in [WantedExt/GroupTheory/CommProbClosedWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/CommProbClosedWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/index.html#comm-prob-closed).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugacy classes](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/conjugacy-classes)
