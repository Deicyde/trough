---
declaration: section
origin: cited
lean: StatMech.Lattice.jce_nbr, StatMech.Lattice.jce_degree, StatMech.Lattice.jce_ClosedContour, StatMech.Lattice.jce_horizBelow, StatMech.Lattice.jce_phi, StatMech.Lattice.jce_HorizStepResidue, StatMech.Lattice.jce_Hc, StatMech.Lattice.jce_edgeFlip
statement: formalized
proof: formalized
---

# Whitney's cut–cycle duality on the square lattice

34 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html).

## Four nearest neighbours of a site

The four nearest neighbours of `v`: right, left, up, down.

Formalized by `StatMech.Lattice.jce_nbr`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-nbr).

## Degree of a site in an edge set

The number of edges of `E` at the site `v`.

Formalized by `StatMech.Lattice.jce_degree`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-degree).

## Closed contour as an even-degree edge set

Every site has even degree in the edge set `E`.

Formalized by `StatMech.Lattice.jce_ClosedContour`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-closed-contour).

## Horizontal edges below a face in its column

The horizontal edges in the column `[a, a + 1]` at heights at most `b`.

Formalized by `StatMech.Lattice.jce_horizBelow`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-horiz-below).

## Parity coloring of faces by an edge set

The parity coloring of faces: `f` is colored when an odd number of horizontal edges of `E`
lie directly below it in its column.

Formalized by `StatMech.Lattice.jce_phi`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-phi).

## Parity coloring changes across vertical contour edges

For every closed contour `E`, the parity coloring changes between horizontally adjacent faces
exactly when the vertical edge between them is in `E`.

Formalized by `StatMech.Lattice.jce_HorizStepResidue`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-horiz-step-residue).

## Number of horizontal contour edges below a height

The number of horizontal edges of `E` below height `b` in the column `[c, c + 1]`.

Formalized by `StatMech.Lattice.jce_Hc`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-hc).

## Edge flip relation of an edge set

The flip relation of `E`: the primal edge between the faces `a` and `b` is in `E`.

Formalized by `StatMech.Lattice.jce_edgeFlip`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EvenContourColoring.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jce-edge-flip).

## Face-region graph of a square-lattice subgraph

The face-region graph of `G`: two adjacent faces of `ℤ²` are joined unless the primal edge
between them (`sharedPrimalEdge`) is an edge of `G`. This is the faithful planar dual
complement of `G`.

Formalized by `StatMech.Lattice.whb_faceRegion`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WhitneyBridge.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WhitneyBridge.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whb-face-region).

## Whitney's cut–cycle duality

**Whitney's cut–cycle duality** for subgraphs of `ℤ²` (H. Whitney, *Planar graphs*, 1933):
for every `H` and lattice edge `pq` not in `H`, with `fg` the dual edge across `pq`, the
endpoints `p` and `q` are connected in `H` iff `f` and `g` are disconnected in the
face-region graph of `H` with `fg` deleted.

Formalized by `StatMech.Lattice.whb_CorrectWhitney`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WhitneyBridge.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WhitneyBridge.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whb-correct-whitney).

## Number of edge crossings of a face walk

The number of steps of the face walk `w` across an edge of `H`.

Formalized by `StatMech.Lattice.whc_dualCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-dual-cross).

## Primal edge between two faces lies in a subgraph

The primal edge between the faces `a` and `b` is an edge of `H`.

Formalized by `StatMech.Lattice.whc_isCross`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-is-cross).

## Face coloring compatible with a subgraph

`φ` changes value exactly across the dual edges of `H`.

Formalized by `StatMech.Lattice.whc_CompatColoring`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-compat-coloring).

## Cut coloring of a subgraph with an extra dual edge

`φ` changes value exactly across the dual edges of `H` and the extra dual edge `f0g0`.

Formalized by `StatMech.Lattice.whc_CutColoring`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-cut-coloring).

## Unit square with its bottom edge removed

The unit square with its bottom edge removed.

Formalized by `StatMech.Lattice.whc_Htest`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-htest).

## Face coloring supported at a single face

The face coloring that is true only at the face `(0, 0)`.

Formalized by `StatMech.Lattice.whc_phiWitness`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-phi-witness).

## Number of bounded faces of a lattice subgraph

The number of finite components of the face-region graph of `P`: the bounded faces of `P`.

Formalized by `StatMech.Lattice.whc_faithfulRegionCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-faithful-region-count).

## Faithful discrete Jordan statement for the face count

The face count of a finite subgraph of `ℤ²`: the bounded components of its face-region graph
are equinumerous with `Fin (nullity P.G)`, so the number of bounded faces is the cycle rank. Only
the number of faces is asserted, not which cycle bounds which face.

Formalized by `StatMech.Lattice.whc_FaithfulDiscreteJordan`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean, line 352](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CutColoring.lean#L352). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#whc-faithful-discrete-jordan).

## Closed face walk around a lattice vertex

The closed walk through the four faces having the site `(c, d)` as a corner.

Formalized by `StatMech.Lattice.jwc_vertexLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EdgeFlipClosedContour.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EdgeFlipClosedContour.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jwc-vertex-loop).

## Spanning subgraph formed by a path

The spanning subgraph formed by a path from `y` to `x` in `K`.

Formalized by `StatMech.Lattice.jwc_cyclePath`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EdgeFlipClosedContour.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EdgeFlipClosedContour.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jwc-cycle-path).

## Whitney duality in the bridge direction

Whitney's duality in the bridge direction for `P`: for every subgraph `K` of `P` and edge
`xy` of `P` not in `K` with dual edge `f0g0`, if `x` and `y` are disconnected in `K`, then
`f0` and `g0` are connected in the face-region graph of `K` with `f0g0` deleted.

Formalized by `StatMech.Lattice.jwc_KeepResidue`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/EdgeFlipClosedContour.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/EdgeFlipClosedContour.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jwc-keep-residue).

## Induced subgraphs of locally finite graphs are locally finite

An induced subgraph of a locally finite graph is locally finite.

Formalized by `StatMech.Lattice.jeb_induceLF`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jeb-induce-lf).

## Two odd-degree vertices lie in one component

In a locally finite graph with finite support, two vertices of odd degree whose other
vertices all have even degree lie in the same component (the handshake lemma applied to a
component).

Formalized by `StatMech.Lattice.jeb_two_odd_reachable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jeb-two-odd-reachable).

## Even-degree image of a planar lattice subgraph

Every site has even degree in the image of `P`.

Formalized by `StatMech.Lattice.jeb_EvenDegreeSubgraph`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jeb-even-degree-subgraph).

## Faithful discrete Jordan property for even-degree subgraphs

Every `PlanarZ2Subgraph` with all degrees even satisfies `whc_FaithfulDiscreteJordan`.

Formalized by `StatMech.Lattice.jeb_FaithfulCountResidue`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanEvenBiconditional.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jeb-faithful-count-residue).

## Symmetry of a flip relation on lattice edges

The flip relation is symmetric on lattice edges.

Formalized by `StatMech.Lattice.wcl_SymmFlip`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-symm-flip).

## Number of flips along a lattice walk

The number of steps of the walk `w` that are flips (in either direction).

Formalized by `StatMech.Lattice.wcl_flipCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-flip-count).

## Even-flip condition on closed lattice walks

Every closed lattice walk has an even number of flips.

Formalized by `StatMech.Lattice.wcl_ClosedEven`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-closed-even).

## Chosen lattice walk between two faces

A fixed lattice walk from `o` to `f`, chosen using connectedness of `ℤ²`.

Formalized by `StatMech.Lattice.wcl_chosenWalk`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-chosen-walk).

## Face coloring by parity of flips

The face coloring given by the parity of the number of flips along the chosen walk from `o`.

Formalized by `StatMech.Lattice.wcl_windingColoring`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-winding-coloring).

## Cut flip relation of a lattice graph and a dual edge

The cut flip relation: steps across a dual edge of `H` or across the extra dual edge `f0g0`.

Formalized by `StatMech.Lattice.wcl_cutFlip`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-cut-flip).

## Closed walk around a unit square

The closed walk around the unit square with corners `(0, 0)` and `(1, -1)`.

Formalized by `StatMech.Lattice.wcl_squareLoop`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-square-loop).

## Cut coloring separating the ends of a dual edge

For every graph `H` of `ℤ²` and dual edge `f0g0` such that the cut flip relation has even
loops, there is a cut coloring distinguishing `f0` from `g0`, and `f0`, `g0` are disconnected
in the face-region graph of `H` with `f0g0` deleted.

Formalized by `StatMech.Lattice.wcl_CorrectColoringResidue`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/WindingColoring.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#wcl-correct-coloring-residue).

## Cut-flip count along a walk

The number of cut flips of `H` and `f0g0` along `w`; equal to
`wcl_flipCount (wcl_cutFlip H f0 g0) w`.

Formalized by `StatMech.Lattice.jwn_cutCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanWindingConstruct.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/JordanWindingConstruct.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html#jwn-cut-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Whitney's cut–cycle duality on the square lattice](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/whitney-s-cut-cycle-duality-on-the-square-lattic)
