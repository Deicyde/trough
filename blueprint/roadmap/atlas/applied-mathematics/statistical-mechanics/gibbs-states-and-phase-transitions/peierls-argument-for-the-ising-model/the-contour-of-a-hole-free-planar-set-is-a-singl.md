---
declaration: section
origin: cited
lean: StatMech.Lattice.phb_doubleDualShift, StatMech.Lattice.phb_doubleDualEquiv, StatMech.Lattice.phb_doubleDualIso, StatMech.Lattice.phb_boundarySupport, StatMech.Lattice.phb_planarBoundary
statement: formalized
proof: formalized
---

# The contour of a hole-free planar set is a single cycle

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl/index.html).

## A. The double dual of the square lattice

## Shift by $(-1, -1)$ identifying the double dual with $\mathbb{Z}^2$

The shift `x ↦ x - (1, 1)` identifying the dual of the dual lattice with `ℤ²`.

Formalized by `StatMech.Lattice.phb_doubleDualShift`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl/index.html#phb-double-dual-shift).

## Shift by $(-1, -1)$ as an equivalence of $\mathbb{Z}^2$

The shift by `(-1, -1)` as an equivalence of `ℤ²`.

Formalized by `StatMech.Lattice.phb_doubleDualEquiv`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl/index.html#phb-double-dual-equiv).

## Shift isomorphism: lattice minus barrier edges to face region graph

The lattice minus the barrier edges of `K` is isomorphic, by the shift by `(-1, -1)`, to the
face region graph of the face-boundary graph of `K`.

Formalized by `StatMech.Lattice.phb_doubleDualIso`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl/index.html#phb-double-dual-iso).

## Support of the face-boundary graph of a finite set

The support of the face-boundary graph of a finite set `K`, as a finset.

Formalized by `StatMech.Lattice.phb_boundarySupport`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl/index.html#phb-boundary-support).

## Face-boundary graph of a finite set as a planar subgraph

The face-boundary graph of a finite set `K`, as a finite planar subgraph of `ℤ²`.

Formalized by `StatMech.Lattice.phb_planarBoundary`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsHoleFreeBoundary.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl/index.html#phb-planar-boundary).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The contour of a hole-free planar set is a single cycle](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/the-contour-of-a-hole-free-planar-set-is-a-singl)
