---
declaration: section
origin: cited
lean: MulAction.poles, MulAction.mem_poles, MulAction.smul_mem_poles, MulAction.image_smul_poles, MulAction.poles_eq_iUnion_fixedBy
statement: formalized
proof: formalized
---

# Poles of group actions

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions/index.html).

## Poles of a group action

A pole of a group action is a point fixed by some nonidentity element.

Formalized by `MulAction.poles`, a definition declared in [MathlibExt/GroupTheory/GroupAction/Poles.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/GroupAction/Poles.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions/index.html#poles).

## Characterization of poles

Let a group $G$ act on a set $X$. A point $p \in X$ is
a pole of the action if and only if there is some $g \in G$ with $g \neq 1$ and
$g \cdot p = p$.

Formalized by `MulAction.mem_poles`, a theorem declared in [MathlibExt/GroupTheory/GroupAction/Poles.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/GroupAction/Poles.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions/index.html#mem-poles).

## The action sends poles to poles

Let a group $G$ act on a set $X$. If $p \in X$ is a
pole of the action, then $g \cdot p$ is a pole for every $g \in G$.

If $p$ is fixed by $h \neq 1$, then $g \cdot p$ is fixed by the conjugate $g h g^{-1} \neq 1$.

Formalized by `MulAction.smul_mem_poles`, a theorem declared in [MathlibExt/GroupTheory/GroupAction/Poles.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/GroupAction/Poles.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions/index.html#smul-mem-poles).

## The poles are invariant under the action

Let a group $G$ act on a set $X$ and let
$P \subseteq X$ be the set of poles of the action. For every $g \in G$, the image of $P$
under the map $x \mapsto g \cdot x$ is $P$.

Formalized by `MulAction.image_smul_poles`, a theorem declared in [MathlibExt/GroupTheory/GroupAction/Poles.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/GroupAction/Poles.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions/index.html#image-smul-poles).

## The poles as a union of fixed-point sets

Let a group $G$ act on a set $X$. The set
of poles equals $\bigcup_{g \in G,\, g \neq 1} \{x \in X : g \cdot x = x\}$, the union of
the fixed-point sets of the nonidentity elements of $G$.

Formalized by `MulAction.poles_eq_iUnion_fixedBy`, a theorem declared in [MathlibExt/GroupTheory/GroupAction/Poles.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/GroupAction/Poles.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions/index.html#poles-eq-i-union-fixed-by).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Poles of group actions](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/permutation-groups/finite-permutation-groups/poles-of-group-actions)
