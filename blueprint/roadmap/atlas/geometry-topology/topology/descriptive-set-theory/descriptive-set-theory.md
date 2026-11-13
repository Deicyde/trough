---
declaration: section
origin: cited
lean: MathlibExt.Topology.DescriptiveSetTheory.CantorSpaceCharacterizationWanted.brouwer_cantor_space_characterization, MathlibExt.Topology.DescriptiveSetTheory.BernsteinSet.bernstein_set_exists, MathlibExt.Topology.DescriptiveSetTheory.RationalsCharacterizationWanted.sierpinski_rationals_characterization
statement: formalized
proof: formalized
---

# Descriptive set theory: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/index.html).

The topology of Polish spaces and their definable subsets: classical characterizations of Cantor space, Baire space and the rationals, Borel complexity, Bernstein sets and topological games.

## Brouwer's characterization of the Cantor space

Every nonempty compact metrizable perfect totally disconnected space is homeomorphic to the Cantor
space.

## Sources

- L. E. J. Brouwer, Proc. Kon. Ned. Akad. Wet. 12 (1910), 785-794.

Formalized by `MathlibExt.Topology.DescriptiveSetTheory.CantorSpaceCharacterizationWanted.brouwer_cantor_space_characterization`, a theorem declared in [MathlibExt/Topology/DescriptiveSetTheory/CantorSpaceCharacterization.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/DescriptiveSetTheory/CantorSpaceCharacterization.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/index.html#brouwer-cantor-space-characterization).

## Existence of a Bernstein set

There is a set $B \subseteq \mathbb{R}$ such that every closed,
uncountable set $F \subseteq \mathbb{R}$ meets both $B$ and its complement $\mathbb{R} \setminus B$.

## Sources

- F. Bernstein (construction); J. C. Oxtoby, Measure and Category, 2nd ed. (1980); A. S. Kechris, Classical Descriptive Set Theory, Thm 8.24 (1995).

Formalized by `MathlibExt.Topology.DescriptiveSetTheory.BernsteinSet.bernstein_set_exists`, a theorem declared in [MathlibExt/Topology/DescriptiveSetTheory/BernsteinSet.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/DescriptiveSetTheory/BernsteinSet.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/index.html#bernstein-set-exists).

## Sierpinski's characterization of the rationals

Every nonempty countable metrizable space with no isolated points is homeomorphic to Q.

## Sources

- W. Sierpinski, Sur une propriete topologique, Fund. Math. 1 (1920), 11-16, DOI 10.4064/FM-1-1-11-16.

Formalized by `MathlibExt.Topology.DescriptiveSetTheory.RationalsCharacterizationWanted.sierpinski_rationals_characterization`, a theorem declared in [MathlibExt/Topology/DescriptiveSetTheory/RationalsCharacterization.lean, line 1752](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/DescriptiveSetTheory/RationalsCharacterization.lean#L1752). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/index.html#sierpinski-rationals-characterization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Descriptive set theory](https://deicyde.github.io/atlas-lean/roadmap/Topology/descriptive-set-theory/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/descriptive-set-theory)
