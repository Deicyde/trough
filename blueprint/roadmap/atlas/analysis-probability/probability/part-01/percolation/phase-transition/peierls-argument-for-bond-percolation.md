---
declaration: section
origin: cited
lean: StatMech.Lattice.axisSite, StatMech.Lattice.exitPred, StatMech.Lattice.exitIndex, StatMech.Lattice.exitFaceUp, StatMech.Lattice.exitFaceDown, StatMech.Lattice.AnchoredCycleExists, StatMech.Lattice.pcAnchoredEnclosure_of_anchoredCycle, StatMech.Lattice.CycleHasLeftFace
statement: formalized
proof: formalized
---

# Peierls argument for bond percolation

46 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html).

## Site on the positive horizontal axis

The site `(j, 0)` on the positive horizontal axis.

Formalized by `StatMech.Lattice.axisSite`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#axis-site).

## Axis site lies outside the origin cluster

The site `(j + 1, 0)` is not in the open cluster of the origin.

Formalized by `StatMech.Lattice.exitPred`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-pred).

## Exit index of a finite origin cluster

For a finite origin cluster, the least `j` such that `(j + 1, 0)` is not in the cluster.

Formalized by `StatMech.Lattice.exitIndex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-index).

## Face above the exit edge

The unit face directly above the exit edge from `(j, 0)` to `(j + 1, 0)`.

Formalized by `StatMech.Lattice.exitFaceUp`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-face-up).

## Face below the exit edge

The unit face directly below the exit edge from `(j, 0)` to `(j + 1, 0)`.

Formalized by `StatMech.Lattice.exitFaceDown`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-face-down).

## Existence of an anchored dual cycle around the origin cluster

Some cycle of the face-boundary graph of the origin cluster is based at the upper exit face
and is longer than the exit index.

Formalized by `StatMech.Lattice.AnchoredCycleExists`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#anchored-cycle-exists).

## Anchored dual cycles give the anchored enclosure property

If every finite origin cluster has an anchored dual cycle (`AnchoredCycleExists`), then the
anchored enclosure property `StatMech.Percolation.PcAnchoredEnclosure` holds. This reduces
the Peierls bound to `AnchoredCycleExists`; it does not prove that hypothesis.

Formalized by `StatMech.Lattice.pcAnchoredEnclosure_of_anchoredCycle`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourAnchor.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#pc-anchored-enclosure-of-anchored-cycle).

## Dual cycle reaching the left half-plane

Some cycle of the face-boundary graph of the origin cluster, based at the upper exit face,
visits a face whose first coordinate is at most zero.

Formalized by `StatMech.Lattice.CycleHasLeftFace`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EnclosingLength.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EnclosingLength.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#cycle-has-left-face).

## Boundary edges of a set of sites in $\mathbb{Z}^2$, as unordered pairs

The edges of `ℤ²` with exactly one endpoint in `S`, as unordered pairs.

Formalized by `StatMech.Lattice.bdEdgeSet2`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceRegion.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceRegion.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#bd-edge-set2).

## Cut lattice of a set of sites

The square lattice with the boundary edges of `S` deleted.

Formalized by `StatMech.Lattice.cutLattice`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceRegion.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceRegion.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#cut-lattice).

## Inside region of an open cluster in the cut lattice

The sites reachable from `o` in the cut lattice of the open cluster of `o`.

Formalized by `StatMech.Lattice.insideRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceRegion.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/FaceRegion.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#inside-region).

## Open cluster maps into the lattice minus its boundary edges

The open subgraph on the cluster of `o` maps into the lattice with the boundary edges of the
cluster removed.

Formalized by `StatMech.Lattice.clusterOpenToBarrierHom`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanContour.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanContour.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#cluster-open-to-barrier-hom).

## Box exterior maps into the lattice minus boundary edges

The lattice on the exterior of a box disjoint from `K` maps into the lattice with the
boundary edges of `K` removed.

Formalized by `StatMech.Lattice.extToBarrierHom`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanContour.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanContour.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#ext-to-barrier-hom).

## Discrete Jordan separation for finite open clusters

A discrete **Jordan separation** for a finite open cluster: removing its boundary edges
leaves the cluster connected, the far exterior connected, and no path between the cluster and
its complement.

Formalized by `StatMech.Lattice.discrete_jordan_separation`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanContour.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanContour.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#discrete-jordan-separation).

## Site on the negative horizontal axis

The site `(-k, 0)` on the negative horizontal axis.

Formalized by `StatMech.Lattice.leftAxisSite`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#left-axis-site).

## Left exit condition at an axis site

The site `(-(k + 1), 0)` is not in the open cluster of the origin.

Formalized by `StatMech.Lattice.leftExitPred`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#left-exit-pred).

## Left exit index of a finite cluster

For a finite origin cluster, the least `k` such that `(-(k + 1), 0)` is not in the cluster.

Formalized by `StatMech.Lattice.leftExitIndex`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#left-exit-index).

## Face above the left exit edge

The unit face directly above the left exit edge.

Formalized by `StatMech.Lattice.leftExitFaceUp`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#left-exit-face-up).

## Face below the left exit edge

The unit face directly below the left exit edge.

Formalized by `StatMech.Lattice.leftExitFaceDown`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/LeftFace.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#left-exit-face-down).

## Origin cluster's enclosing contour links the two axis exits

Some cycle of the face-boundary graph of the origin cluster, based at the upper exit face on
the positive axis, passes through the upper exit face on the negative axis.

Formalized by `StatMech.Lattice.EnclosingContourLinksExits`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConnected.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConnected.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#enclosing-contour-links-exits).

## $p_c(\mathbb{Z}^2) < 1$ via boundary connectivity, assuming linked exits

`p_c(ℤ²) < 1`, under the hypothesis that `EnclosingContourLinksExits` holds for every
configuration with a finite origin cluster.

Formalized by `StatMech.Lattice.pc_lt_one_via_boundary`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConnected.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoundaryConnected.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#pc-lt-one-via-boundary).

## Exit dart on the positive horizontal axis

The boundary dart of the origin cluster across the exit edge on the positive horizontal axis.

Formalized by `StatMech.Lattice.exitDart`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-dart).

## Exit dart on the negative horizontal axis

The boundary dart of the origin cluster across the exit edge on the negative horizontal axis.

Formalized by `StatMech.Lattice.leftExitDart`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#left-exit-dart).

## Negative part of an integer

The negative part `min z 0` of an integer.

Formalized by `StatMech.Lattice.negPart`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#neg-part).

## Unit face to the left of a dart

The unit face to the left of the dart `e`, labelled by its lower left corner.

Formalized by `StatMech.Lattice.dartFace`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#dart-face).

## Left and right exit darts lie in the same boundary orbit

The left exit dart lies in the boundary orbit of the right exit dart.

Formalized by `StatMech.Lattice.ExitDartsSameOrbit`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-darts-same-orbit).

## $p_c(\mathbb{Z}^2) < 1$ via exit dart orbits, assuming linked exits

`p_c(ℤ²) < 1`, under the hypothesis that `EnclosingContourLinksExits` holds for every
configuration with a finite origin cluster.

Formalized by `StatMech.Lattice.pc_lt_one_via_dartOrbit`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/ContourLinksExits.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#pc-lt-one-via-dart-orbit).

## Undirected lattice edge of a dart

The undirected lattice edge underlying a dart.

Formalized by `StatMech.Lattice.dartPrimalEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#dart-primal-edge).

## Canonical contour of a finite origin cluster

The canonical contour of a finite origin cluster: the closed walk around the boundary orbit
of the exit dart on the positive axis.

Formalized by `StatMech.Lattice.canonicalContour`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#canonical-contour).

## Darts of the canonical contour

The darts of one period of the boundary orbit of the exit dart.

Formalized by `StatMech.Lattice.canonicalContourDarts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#canonical-contour-darts).

## Primal edges of the canonical contour

The primal edges of the canonical contour.

Formalized by `StatMech.Lattice.canonicalPrimalEdgeFinset`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#canonical-primal-edge-finset).

## Event that every edge of the canonical contour is closed

The set of configurations in which every primal edge of the canonical contour of `ω` is
closed.

Formalized by `StatMech.Lattice.closedDartContourEvent`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#closed-dart-contour-event).

## Canonical contour is longer than the exit index

The period of the canonical contour exceeds the exit index, the length condition of an
anchored enclosure.

Formalized by `StatMech.Lattice.CanonicalContourWinds`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#canonical-contour-winds).

## Face walk along the first successors of a boundary dart

The walk of faces to the left of the first `n` successors of a boundary dart.

Formalized by `StatMech.Lattice.canonicalFaceWalkAux`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#canonical-face-walk-aux).

## Closed face walk of the canonical contour

The closed walk of faces to the left of the darts of the canonical contour, based at the
upper exit face.

Formalized by `StatMech.Lattice.canonicalFaceWalk`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#canonical-face-walk).

## $p_c(\mathbb{Z}^2) < 1$ via the canonical contour, assuming anchored cycles

`p_c(ℤ²) < 1`, under the hypothesis that `AnchoredCycleExists` holds for every configuration
with a finite origin cluster.

Formalized by `StatMech.Lattice.pc_lt_one_via_canonicalContour`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CanonicalContour.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#pc-lt-one-via-canonical-contour).

## Face walk along a boundary orbit

The walk in the face-boundary graph of `K` through the faces of `e` and its first `n`
successors.

Formalized by `StatMech.Lattice.dartOrbitFaceWalk`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#dart-orbit-face-walk).

## Face loop of a boundary orbit in the face-boundary graph

The closed walk of faces along one period of the boundary orbit of `e`, for finite `K`.

Formalized by `StatMech.Lattice.dartOrbitFaceLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#dart-orbit-face-loop).

## Face loop of the exit orbit of a finite cluster

The closed face walk of the exit orbit of a finite origin cluster, based at the upper exit
face.

Formalized by `StatMech.Lattice.exitOrbitFaceLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-orbit-face-loop).

## Canonical orbit cycle condition

The face loop of the exit orbit is a cycle, and the left exit dart lies in the exit orbit.

Formalized by `StatMech.Lattice.CanonicalOrbitCycle`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#canonical-orbit-cycle).

## $p_c(\mathbb{Z}^2) < 1$ assuming a canonical orbit cycle

`p_c(ℤ²) < 1`, under the hypothesis that `CanonicalOrbitCycle` holds for every configuration
with a finite origin cluster.

Formalized by `StatMech.Lattice.pc_lt_one_orbit`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitEncloses.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#pc-lt-one-orbit).

## Exit dart of a finite origin cluster

The exit dart of a finite origin cluster, as an element of the subtype of boundary darts.

Formalized by `StatMech.Lattice.exitBaseSub`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-base-sub).

## Minimal-period face loop of the exit orbit

The closed walk of faces along one period of the exit orbit, based at the upper exit face.

Formalized by `StatMech.Lattice.exitMinFaceLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#exit-min-face-loop).

## Simplicity of the exit orbit's face walk

The exit orbit has period at least three and visits distinct faces during one period.

Formalized by `StatMech.Lattice.OrbitFaceSimple`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#orbit-face-simple).

## $p_c(\mathbb{Z}^2) < 1$ assuming simple exit orbits

`p_c(ℤ²) < 1`, under the hypothesis that for every configuration with a finite origin cluster
the exit orbit is simple (`OrbitFaceSimple`) and contains the left exit dart.

Formalized by `StatMech.Lattice.pc_lt_one_of_orbitFaceSimple`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanSingleCycle.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#pc-lt-one-of-orbit-face-simple).

## Set and walk interior share boundary edges

The set `K` and the inside `jec_leftRegion Vc` of the closed walk `Vc` have the same boundary
edges.

Formalized by `StatMech.Lattice.pww_BdEdgeMatch`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitWindingWitness.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/OrbitWindingWitness.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html#pww-bd-edge-match).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Peierls argument for bond percolation](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/phase-transition/peierls-argument-for-bond-percolation)
