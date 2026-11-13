---
declaration: section
origin: cited
lean: MetaMathlibExt.IsCCC, MetaMathlibExt.IsSigmaCentered, MetaMathlibExt.MartinAxiomSigmaCentered, MetaMathlibExt.MartinAxiom
statement: formalized
proof: formalized
---

# Martin's axiom

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/martin-s-axiom/index.html).

## Countable chain condition

A partial order $(P, \le)$ has the countable chain condition
(c.c.c.) if every antichain of $P$ is countable, where an antichain is a set of pairwise
incompatible elements: no two distinct members of it have a common lower bound in $P$.

Formalized by `MetaMathlibExt.IsCCC`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/martin-s-axiom/index.html#is-ccc).

## σ-centered partial orders

A partial order $P$ is $\sigma$-centered if there is a map
$c : P \to \mathbb{N}$ such that for every $n \in \mathbb{N}$, every finite set of elements $p$
with $c(p) = n$ has a common lower bound in $P$. Thus $P$ splits into countably many centered
pieces $c^{-1}(n)$; the empty set is among the finite sets, so $P$ must be nonempty.

Formalized by `MetaMathlibExt.IsSigmaCentered`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/martin-s-axiom/index.html#is-sigma-centered).

## Martin's axiom for σ-centered partial orders

For a cardinal $\kappa$, this is the
statement that for every $\sigma$-centered partial order $P$, every family $\mathcal{D}$ of at
most $\kappa$ dense subsets of $P$ and every $p \in P$, there is a filter $G$ on $P$ with
$p \in G$ that meets every member of $\mathcal{D}$. Here $D \subseteq P$ is dense if every
element of $P$ has an element of $D$ below it, and a filter is a nonempty upward closed subset
of $P$ any two of whose elements have a common lower bound in it.

Formalized by `MetaMathlibExt.MartinAxiomSigmaCentered`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/martin-s-axiom/index.html#martin-axiom-sigma-centered).

## Martin's axiom

For a cardinal $\kappa$, $\mathrm{MA}(\kappa)$ is the statement that for
every partial order $P$ with the countable chain condition, every family $\mathcal{D}$ of at most
$\kappa$ dense subsets of $P$ and every $p \in P$, there is a filter $G$ on $P$ with $p \in G$
that meets every member of $\mathcal{D}$. Here $D \subseteq P$ is dense if every element of $P$
has an element of $D$ below it, and a filter is a nonempty upward closed subset of $P$ any two
of whose elements have a common lower bound in it.

Formalized by `MetaMathlibExt.MartinAxiom`, a definition declared in [MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Forcing/ForcingAxioms/MartinAxiom.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/martin-s-axiom/index.html#martin-axiom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Martin's axiom](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/martin-s-axiom/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/SetTheory/forcing/martin-s-axiom)
