---
declaration: section
origin: cited
lean: InverseLimit.carrier, InverseLimit.mem_carrier_iff, InverseLimit.proj_compat, InverseLimit.isClosed_carrier, InverseLimit.isCompact_carrier
statement: formalized
proof: formalized
---

# Inverse limits of topological spaces

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces/index.html).

## Inverse limit as compatible tuples

Let $I$ be a preordered set, let $(X_i)_{i \in I}$
be a family of sets, and for every $i \le j$ let $f_{ij} \colon X_j \to X_i$ be a map. The inverse
limit is the set of tuples $x = (x_i)_{i \in I}$ in the product $\prod_{i \in I} X_i$ such that
$f_{ij}(x_j) = x_i$ whenever $i \le j$.

## Sources

- ATLAS NumberTheoryI, Definition 8.9.

Formalized by `InverseLimit.carrier`, a definition declared in [MathlibExt/Topology/InverseLimit.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/InverseLimit.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces/index.html#carrier).

## Membership in the inverse limit

Let $I$ be a preordered set, let $(X_i)_{i \in I}$ be a
family of sets, and for every $i \le j$ let $f_{ij} \colon X_j \to X_i$ be a map. A tuple
$x \in \prod_{i \in I} X_i$ lies in the inverse limit if and only if $f_{ij}(x_j) = x_i$ for all
$i \le j$.

Formalized by `InverseLimit.mem_carrier_iff`, a theorem declared in [MathlibExt/Topology/InverseLimit.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/InverseLimit.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces/index.html#mem-carrier-iff).

## Elements of the inverse limit are compatible

Let $I$ be a preordered set, let
$(X_i)_{i \in I}$ be a family of sets, and for every $i \le j$ let $f_{ij} \colon X_j \to X_i$ be
a map. If $x = (x_i)_{i \in I}$ lies in the inverse limit, then $f_{ij}(x_j) = x_i$ for all
$i \le j$.

Formalized by `InverseLimit.proj_compat`, a theorem declared in [MathlibExt/Topology/InverseLimit.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/InverseLimit.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces/index.html#proj-compat).

## The inverse limit is closed

Let $I$ be a preordered set, let $(X_i)_{i \in I}$ be a
family of Hausdorff topological spaces, and for every $i \le j$ let $f_{ij} \colon X_j \to X_i$
be a continuous map. Then the inverse limit
$\{x \in \prod_{i \in I} X_i : f_{ij}(x_j) = x_i \text{ for all } i \le j\}$ is closed in the
product $\prod_{i \in I} X_i$.

Each equation $f_{ij}(x_j) = x_i$ cuts out a closed set because $X_i$ is Hausdorff, and the
limit is the intersection of all of them.

Formalized by `InverseLimit.isClosed_carrier`, a theorem declared in [MathlibExt/Topology/InverseLimit.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/InverseLimit.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces/index.html#is-closed-carrier).

## The inverse limit of compact Hausdorff spaces is compact

Let $I$ be a preordered set, let
$(X_i)_{i \in I}$ be a family of compact Hausdorff topological spaces, and for every $i \le j$
let $f_{ij} \colon X_j \to X_i$ be a continuous map. Then the inverse limit
$\{x \in \prod_{i \in I} X_i : f_{ij}(x_j) = x_i \text{ for all } i \le j\}$ is compact in the
product $\prod_{i \in I} X_i$.

It is a closed subset of a compact product.

Formalized by `InverseLimit.isCompact_carrier`, a theorem declared in [MathlibExt/Topology/InverseLimit.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/InverseLimit.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces/index.html#is-compact-carrier).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inverse limits of topological spaces](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/general-topology/inverse-limits-of-topological-spaces)
