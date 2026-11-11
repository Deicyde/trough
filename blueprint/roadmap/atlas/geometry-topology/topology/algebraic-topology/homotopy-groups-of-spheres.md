---
declaration: section
origin: cited
lean: MathlibExt.Topology.HomotopyGroupsWanted.Topology.pi1_circle_mulEquiv_int, MathlibExt.Topology.PiSixSphereThreeWanted.Topology.PiSixSphereThree.pi6_sphere_three_mulEquiv_zmod_twelve
statement: formalized
---

# Homotopy groups of spheres

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/homotopy-groups-of-spheres/index.html).

## The fundamental group of the circle is infinite cyclic

The fundamental group of the unit
circle in $\mathbb{C}$ based at $1$ is isomorphic, as a group, to the additive group $\mathbb{Z}$.

## Sources

- Classical theorem in algebraic topology. Problem `pi1_circle_mulEquiv_int` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.HomotopyGroupsWanted.Topology.pi1_circle_mulEquiv_int` is written with `theorem_wanted` in [WantedExt/Topology/HomotopyGroupsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/HomotopyGroupsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/homotopy-groups-of-spheres/index.html#pi1-circle-mul-equiv-int).

## The sixth homotopy group of the 3-sphere

Let $S^3$ be the unit sphere in Euclidean space
$\mathbb{R}^4$. For every point $x \in S^3$, the homotopy group $\pi_6(S^3, x)$ is isomorphic as a
group to the cyclic group $\mathbb{Z}/12$.

## Sources

- H. Toda, 'Composition Methods in Homotopy Groups of Spheres', Annals of Mathematics Studies 49, Princeton University Press, 1962. The value pi_6(S^3) = Z/12 also appears in the tables of A. Hatcher, 'Algebraic Topology', Section 4.1. Problem `pi6_sphere_three_mulEquiv_zmod_twelve` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.PiSixSphereThreeWanted.Topology.PiSixSphereThree.pi6_sphere_three_mulEquiv_zmod_twelve` is written with `theorem_wanted` in [WantedExt/Topology/PiSixSphereThreeWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/PiSixSphereThreeWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/homotopy-groups-of-spheres/index.html#pi6-sphere-three-mul-equiv-zmod-twelve).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Homotopy groups of spheres](https://deicyde.github.io/atlas-lean/roadmap/Topology/algebraic-topology/homotopy-groups-of-spheres/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/algebraic-topology/homotopy-groups-of-spheres)
