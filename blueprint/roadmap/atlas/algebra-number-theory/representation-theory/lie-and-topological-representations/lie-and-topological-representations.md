---
declaration: section
origin: cited
lean: IsContinuousSemilinearRepresentation
statement: formalized
proof: formalized
---

# Representations of topological and Lie groups: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/index.html).

Representations of infinite groups and Lie algebras: continuous and unitary representations of compact and topological groups (Peter–Weyl theorem, complete reducibility), continuous representations over topological rings, representations of Lie algebras and of general linear groups (Schur–Weyl duality), and groups characterized by their irreducible representations.

## Continuous semilinear representation

Let $G$ be a topological group, $R$ a topological
ring and $M$ a topological abelian group that is a finite free $R$-module. Suppose that $G$ acts
on $R$ by ring automorphisms and on $M$ by additive automorphisms, and that the actions of $G$ on
$R$, of $G$ on $M$ and of $R$ on $M$ are jointly continuous. This is a continuous semilinear
representation of $G$ on $M$ when $g \cdot (r x) = (g \cdot r)(g \cdot x)$ for all $g \in G$,
$r \in R$ and $x \in M$, and the coordinate map $M \to R^n$ of a fixed basis of $M$ over $R$,
where $n$ is the size of the basis, is a homeomorphism onto $R^n$ with the product topology.

## Sources

- arXiv:2608.00845, Definition `defsemilinrep` (lines 1947–1950); this class records its object-level content.

Formalized by `IsContinuousSemilinearRepresentation`, a class declared in [MathlibExt/Topology/Algebra/ContinuousSemilinearRepresentation.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/ContinuousSemilinearRepresentation.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/index.html#is-continuous-semilinear-representation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representations of topological and Lie groups](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RepresentationTheory/lie-and-topological-representations)
