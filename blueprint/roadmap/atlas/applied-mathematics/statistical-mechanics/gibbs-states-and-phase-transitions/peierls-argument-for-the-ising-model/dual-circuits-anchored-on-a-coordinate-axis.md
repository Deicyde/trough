---
declaration: section
origin: cited
lean: StatMech.Lattice.PerContourDualCircuit, StatMech.Lattice.axisVertex, StatMech.Lattice.axisAnchorPool, StatMech.Lattice.AxisContourDualCircuit
statement: formalized
proof: formalized
---

# Dual circuits anchored on a coordinate axis

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-anchored-on-a-coordinate-axis/index.html).

## A. Per-contour circuits

## Closed-walk decoding of each realised contour from an anchor pool

Every realised contour of length `ℓ` is decoded from a closed walk of length `ℓ` based at a site
of a common pool of at most `ℓ` anchors.

Formalized by `StatMech.Lattice.PerContourDualCircuit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-anchored-on-a-coordinate-axis/index.html#per-contour-dual-circuit).

## Site $(j, 0, \ldots, 0)$ on the first coordinate axis

The site `(j, 0, …, 0)` on the first coordinate axis.

Formalized by `StatMech.Lattice.axisVertex`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-anchored-on-a-coordinate-axis/index.html#axis-vertex).

## First $\ell$ sites of the first coordinate axis

The axis sites `(j, 0, …, 0)` with `j < ℓ`.

Formalized by `StatMech.Lattice.axisAnchorPool`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-anchored-on-a-coordinate-axis/index.html#axis-anchor-pool).

## Closed-walk decoding of each realised contour from an axis site

Every realised contour of length `ℓ` is decoded from a closed walk of length `ℓ` based at an
axis site `(j, 0, …, 0)` with `j < ℓ`.

Formalized by `StatMech.Lattice.AxisContourDualCircuit`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Peierls/PeierlsAnchorEncode.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-anchored-on-a-coordinate-axis/index.html#axis-contour-dual-circuit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dual circuits anchored on a coordinate axis](https://deicyde.github.io/atlas-lean/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-anchored-on-a-coordinate-axis/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/StatisticalMechanics/gibbs-states-and-phase-transitions/peierls-argument-for-the-ising-model/dual-circuits-anchored-on-a-coordinate-axis)
