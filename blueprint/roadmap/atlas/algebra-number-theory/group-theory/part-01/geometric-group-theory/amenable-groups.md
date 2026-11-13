---
declaration: section
origin: cited
lean: IsAmenable, isAmenable_of_finite, isAmenable_of_subsingleton
statement: formalized
proof: formalized
---

# Amenable groups

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/amenable-groups/index.html).

## Amenable group (Følner condition)

A discrete group $G$ is *amenable* if it satisfies the
Følner condition: for every finite subset $K \subseteq G$ and every real $\varepsilon > 0$ there is
a finite nonempty subset $F \subseteq G$ such that
$|sF \mathbin{\triangle} F| / |F| < \varepsilon$ for every $s \in K$. Here
$sF = \{sf : f \in F\}$ is the left translate of $F$ by $s$, $\triangle$ is symmetric difference
and $|\cdot|$ is cardinality.

Formalized by `IsAmenable`, a definition declared in [MathlibExt/GroupTheory/AmenableGroup.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/AmenableGroup.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/amenable-groups/index.html#is-amenable).

## Finite groups are amenable

Every finite group is amenable.

The whole group $F = G$ is invariant under left translation, so it is a Følner set whose
symmetric-difference ratio is $0$.

Formalized by `isAmenable_of_finite`, a theorem declared in [MathlibExt/GroupTheory/AmenableGroup.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/AmenableGroup.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/amenable-groups/index.html#is-amenable-of-finite).

## Trivial groups are amenable

Every group with at most one element is amenable; the set
$F = \{1\}$ witnesses the Følner condition.

Formalized by `isAmenable_of_subsingleton`, a theorem declared in [MathlibExt/GroupTheory/AmenableGroup.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/AmenableGroup.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/amenable-groups/index.html#is-amenable-of-subsingleton).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Amenable groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/geometric-group-theory/amenable-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/geometric-group-theory/amenable-groups)
