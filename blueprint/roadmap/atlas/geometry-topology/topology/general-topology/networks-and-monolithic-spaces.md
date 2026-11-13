---
declaration: section
origin: cited
lean: HasCountableNetwork, hasCountableNetwork_of_secondCountable, CountablyMonolithicSpace
statement: formalized
proof: formalized
---

# Networks and monolithic spaces

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/networks-and-monolithic-spaces/index.html).

## Countable network

A topological space $X$ has a countable network if there is a
countable family $\mathcal{N}$ of subsets of $X$ such that for every open set $U \subseteq X$
and every point $x \in U$ there is some $V \in \mathcal{N}$ with $x \in V \subseteq U$.

Network sets need not themselves be open.

Formalized by `HasCountableNetwork`, a definition declared in [MathlibExt/Topology/CountablyMonolithic.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/CountablyMonolithic.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/networks-and-monolithic-spaces/index.html#has-countable-network).

## Second-countable spaces have a countable network

Every second-countable topological
space has a countable network.

Formalized by `hasCountableNetwork_of_secondCountable`, a theorem declared in [MathlibExt/Topology/CountablyMonolithic.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/CountablyMonolithic.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/networks-and-monolithic-spaces/index.html#has-countable-network-of-second-countabl).

## Countably monolithic space

A topological space is countably monolithic (ω-monolithic) if the closure
of every countable subspace has a countable network.

Formalized by `CountablyMonolithicSpace`, a class declared in [MathlibExt/Topology/CountablyMonolithic.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/CountablyMonolithic.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/networks-and-monolithic-spaces/index.html#countably-monolithic-space).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Networks and monolithic spaces](https://deicyde.github.io/atlas-lean/roadmap/Topology/general-topology/networks-and-monolithic-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/general-topology/networks-and-monolithic-spaces)
