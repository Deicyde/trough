---
declaration: section
origin: cited
lean: MathlibExt.Topology.DescriptiveSetTheory.BaireSpaceCharacterizationWanted.IsZeroDimensionalSpace, MathlibExt.Topology.DescriptiveSetTheory.BaireSpaceCharacterizationWanted.baire_space_characterization
statement: formalized
proof: formalized
---

# Alexandrov–Urysohn characterization of Baire space

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/alexandrov-urysohn-characterization-of-baire-spa/index.html).

## Zero-dimensional space

A topological space $X$ is zero-dimensional if for every point
$x \in X$ and every open set $U \subseteq X$ containing $x$ there is a clopen set $V$ with
$x \in V \subseteq U$.

Formalized by `MathlibExt.Topology.DescriptiveSetTheory.BaireSpaceCharacterizationWanted.IsZeroDimensionalSpace`, a definition declared in [MathlibExt/Topology/DescriptiveSetTheory/BaireSpaceCharacterization.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/DescriptiveSetTheory/BaireSpaceCharacterization.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/alexandrov-urysohn-characterization-of-baire-spa/index.html#is-zero-dimensional-space).

## Alexandrov–Urysohn theorem on Baire space

Let $X$ be a nonempty Polish space that
is zero-dimensional (for every point $x$ and every open set $U$ containing $x$ there is a clopen
set $V$ with $x \in V \subseteq U$) and in which every compact subset has empty interior. Then $X$
is homeomorphic to the Baire space $\mathbb{N}^{\mathbb{N}}$ of all sequences of natural numbers,
with the product of the discrete topologies.

## Sources

- Alexandrov–Urysohn characterization; A. S. Kechris, Classical Descriptive Set Theory (1995), Theorem 7.7.

Formalized by `MathlibExt.Topology.DescriptiveSetTheory.BaireSpaceCharacterizationWanted.baire_space_characterization`, a theorem declared in [MathlibExt/Topology/DescriptiveSetTheory/BaireSpaceCharacterization.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/DescriptiveSetTheory/BaireSpaceCharacterization.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/alexandrov-urysohn-characterization-of-baire-spa/index.html#baire-space-characterization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alexandrov–Urysohn characterization of Baire space](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/alexandrov-urysohn-characterization-of-baire-spa/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/descriptive-set-theory/alexandrov-urysohn-characterization-of-baire-spa)
