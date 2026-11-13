---
declaration: section
origin: cited
lean: StatMech.Percolation.withinConnEvent, StatMech.Percolation.edgesWithinFinset, StatMech.Percolation.boxEdgeFinset, StatMech.Percolation.boxCrossingEvent, StatMech.Percolation.boxCrossProb, StatMech.Percolation.pivotalEvent, StatMech.Percolation.connBdry, StatMech.Percolation.surfaceSet
statement: formalized
proof: formalized
---

# Duminil-Copin–Tassion differential inequality

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html).

## Event of a connection inside a finite set

The event `{o ↔ x inside S}`: `o` and `x` lie in `S` and are joined by an open path in `S`.

Formalized by `StatMech.Percolation.withinConnEvent`, a definition declared in [MathlibExt/Probability/Percolation/ConnectionsInsideSet.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/ConnectionsInsideSet.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#within-conn-event).

## Pairs of sites of a finite set

All unordered pairs of sites of the finite set `S`.

Formalized by `StatMech.Percolation.edgesWithinFinset`, a definition declared in [MathlibExt/Probability/Percolation/ConnectionsInsideSet.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/ConnectionsInsideSet.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#edges-within-finset).

## Pairs of sites of a lattice box

All unordered pairs of sites of `Λ_n` (containing the lattice edges of `Λ_n`).

Formalized by `StatMech.Percolation.boxEdgeFinset`, a definition declared in [MathlibExt/Probability/Percolation/DctDifferential.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctDifferential.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#box-edge-finset).

## Box-crossing event

The event that the origin is joined by an open path inside `Λ_n` to the vertex boundary of
`Λ_n`.

Formalized by `StatMech.Percolation.boxCrossingEvent`, a definition declared in [MathlibExt/Probability/Percolation/DctDifferential.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctDifferential.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#box-crossing-event).

## Box-crossing probability

The probability of `boxCrossingEvent d n`.

Formalized by `StatMech.Percolation.boxCrossProb`, a definition declared in [MathlibExt/Probability/Percolation/DctDifferential.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctDifferential.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#box-cross-prob).

## Pivotal edge event

The event that the edge `e` is pivotal for `A` (flipping `e` changes whether `A` occurs).

Formalized by `StatMech.Percolation.pivotalEvent`, a definition declared in [MathlibExt/Probability/Percolation/DctSurfacePartition.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctSurfacePartition.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#pivotal-event).

## Connection of a site to the box boundary

`x ∈ Λ_n` is joined by an open path inside `Λ_n` to a site of the vertex boundary of `Λ_n`.

Formalized by `StatMech.Percolation.connBdry`, a definition declared in [MathlibExt/Probability/Percolation/DctSurfacePartition.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctSurfacePartition.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#conn-bdry).

## Set of sites not connected to the box boundary

The random set `𝒮(ω)` of sites of `Λ_n` not joined inside `Λ_n` to the vertex boundary.

Formalized by `StatMech.Percolation.surfaceSet`, a definition declared in [MathlibExt/Probability/Percolation/DctSurfacePartition.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctSurfacePartition.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#surface-set).

## Event that the unconnected set equals a given set

The event `{𝒮 = S}`.

Formalized by `StatMech.Percolation.surfaceEvent`, a definition declared in [MathlibExt/Probability/Percolation/DctSurfacePartition.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctSurfacePartition.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#surface-event).

## Pairs of box sites outside a given set

The pairs of sites of `Λ_n` that are not pairs of sites of `S`.

Formalized by `StatMech.Percolation.boxEdgesOutside`, a definition declared in [MathlibExt/Probability/Percolation/DctSurfacePartition.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DctSurfacePartition.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#box-edges-outside).

## Duminil-Copin–Tassion differential inequality

The **Duminil-Copin–Tassion differential inequality**: if `φ_p(S) ≥ m` for every finite
`S ∋ 0`, then `d/dp ℙ_p(A_n) ≥ (p(1 - p))⁻¹ m (1 - ℙ_p(A_n))` for `0 < p < 1` and `n ≥ 1`
(Duminil-Copin–Tassion 2016).

Formalized by `StatMech.Percolation.dct_differential_inequality`, a theorem declared in [MathlibExt/Probability/Percolation/DifferentialInequality.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DifferentialInequality.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#dct-differential-inequality).

## Box-crossing probability as a polynomial in the density

The polynomial `t ↦ ℙ_t(A_{n+1})` (the box-crossing probability as a polynomial in the
density), defined for all real `t`.

Formalized by `StatMech.Percolation.crossPoly`, a definition declared in [MathlibExt/Probability/Percolation/DifferentialInequality.lean, line 567](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DifferentialInequality.lean#L567). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#cross-poly).

## Mean-field lower bound

**Mean-field lower bound** (Duminil-Copin–Tassion 2016): for
`p̃_c < q < 1` (with `p̃_c > 0`), `θ(q) ≥ (q - p̃_c) / (q(1 - p̃_c))`.

Formalized by `StatMech.Percolation.theta_ge_meanField_of_tildePc_lt`, a theorem declared in [MathlibExt/Probability/Percolation/DifferentialInequality.lean, line 629](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/Percolation/DifferentialInequality.lean#L629). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#theta-ge-mean-field-of-tilde-pc-lt).

## Edges of $\mathbb{Z}^d$ inside a set

The edges of `ℤ^d` with both endpoints in `S`.

Formalized by `StatMech.Sharpness.internalEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/ConnWithinFactorization.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/ConnWithinFactorization.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#internal-edges).

## Event that a vertex is connected to a target set

The event that `o` is connected to `B`.

Formalized by `StatMech.Sharpness.mpiCrossingEvent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-crossing-event).

## Vertices not connected to a target set

The set of vertices not connected to `B` in `ω`.

Formalized by `StatMech.Sharpness.mpiBlockedSet`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-blocked-set).

## Event that the set of vertices not connected to $B$ is $S$

The event that the set of vertices not connected to `B` is exactly `S`.

Formalized by `StatMech.Sharpness.mpiSurfaceEvent`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-surface-event).

## Edges with both endpoints in a vertex set

The edges with both endpoints in `S`.

Formalized by `StatMech.Sharpness.mpiInternalEdges`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-internal-edges).

## Inhomogeneous Duminil-Copin–Tassion quantity $\varphi(S)$

The inhomogeneous Duminil-Copin–Tassion quantity `φ(S) = ∑_{(x,y) ∈ ∂S} (1 - e^{-βJ_{xy}}) P(o ↔
x in S)`.

Formalized by `StatMech.Sharpness.mpiPhi`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-phi).

## Event that an edge is closed and pivotal

The event that `e` is closed and pivotal for `A`.

Formalized by `StatMech.Sharpness.mpiPivotalClosed`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 480](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L480). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-pivotal-closed).

## Product of the edge laws over all other edges

The product of the edge laws over all edges other than `e`.

Formalized by `StatMech.Sharpness.mpiWeightOff`, a definition declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 724](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L724). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-weight-off).

## Mean-field differential inequality for inhomogeneous percolation

The mean-field differential inequality for inhomogeneous percolation: Russo's formula `∂_β P(o ↔
B) = ∑_e J_e P(e closed pivotal)` and, if `φ(S) ≥ m` for all `S ∋ o`, `(m/β)(1 - P(o ↔ B)) ≤ ∂_β P(o
↔ B)`. Reference: H. Duminil-Copin, V. Tassion, "A new proof of the sharpness of the phase
transition for Bernoulli percolation and the Ising model", Comm. Math. Phys. 343 (2016) 725–745.

Formalized by `StatMech.Sharpness.mpi_meanfield_perco`, a lemma declared in [PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean, line 890](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/PhyslibExt/CondensedMatter/IsingModel/Sharpness/MeanfieldPercoInhom.lean#L890). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html#mpi-meanfield-perco).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Duminil-Copin–Tassion differential inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/sharpness/duminil-copin-tassion-differential-inequality)
