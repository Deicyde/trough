---
declaration: section
origin: cited
lean: StatMech.CellEulerChar.Cell, StatMech.CellEulerChar.Vtx, StatMech.CellEulerChar.cellVerts, StatMech.CellEulerChar.cellEdges, StatMech.CellEulerChar.regVerts, StatMech.CellEulerChar.regEdges, StatMech.CellEulerChar.regChi, StatMech.CellEulerChar.newVerts
statement: formalized
proof: formalized
---

# Discrete Gauss–Bonnet formula for polyominoes

98 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html).

## Unit cell of the plane

A unit cell `[a, a + 1] × [b, b + 1]` of the plane, labelled by its lower left corner.

Formalized by `StatMech.CellEulerChar.Cell`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell).

## Lattice point as a vertex of the cell complex

A lattice point of `ℤ²`, used as a vertex of the cell complex.

Formalized by `StatMech.CellEulerChar.Vtx`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#vtx).

## Corners of a unit cell

The four corners of a unit cell.

Formalized by `StatMech.CellEulerChar.cellVerts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell-verts).

## Sides of a unit cell

The four sides of a unit cell, as unordered pairs of corners.

Formalized by `StatMech.CellEulerChar.cellEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell-edges).

## Vertices of a union of unit cells

The vertices of the union of the cells in `K`.

Formalized by `StatMech.CellEulerChar.regVerts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#reg-verts).

## Edges of a union of unit cells

The edges of the union of the cells in `K`.

Formalized by `StatMech.CellEulerChar.regEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#reg-edges).

## Euler characteristic of a union of unit cells

The Euler characteristic `V - E + F` of the union of the cells in `K`, with one face
per
cell.

Formalized by `StatMech.CellEulerChar.regChi`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#reg-chi).

## Number of new corners added by a cell

The number of corners of `c` that are not already vertices of the region `K`.

Formalized by `StatMech.CellEulerChar.newVerts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#new-verts).

## Number of new sides added by a cell

The number of sides of `c` that are not already edges of the region `K`.

Formalized by `StatMech.CellEulerChar.newEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#new-edges).

## Cell regions built by attaching cells along boundary arcs

Regions built from a single cell by repeatedly attaching a new cell along a boundary arc: the
new cell adds one more edge than vertex, so the Euler characteristic is unchanged.

Formalized by `StatMech.CellEulerChar.EucBuildable`, an inductive type declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/CellEulerCharacteristic.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#euc-buildable).

## Four cells around a lattice vertex

The four cells having `v` as a corner.

Formalized by `StatMech.AngleDefect.surroundCells`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#surround-cells).

## Cell degree of a lattice vertex

The number of cells of `K` having `v` as a corner.

Formalized by `StatMech.AngleDefect.cellDeg`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell-deg).

## Edge degree of a lattice vertex

The number of edges of the region `K` incident to `v`.

Formalized by `StatMech.AngleDefect.edgeDeg`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#edge-deg).

## Angle defect at a lattice vertex

The angle defect at `v`, in quarter turns: `4 - 2 · edgeDeg K v + cellDeg K v`.

Formalized by `StatMech.AngleDefect.defect`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#defect).

## Lattice edge to the right neighbour

The lattice edge from `v` to its right neighbour.

Formalized by `StatMech.AngleDefect.incidentEdgeR`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#incident-edge-r).

## Lattice edge to the left neighbour

The lattice edge from `v` to its left neighbour.

Formalized by `StatMech.AngleDefect.incidentEdgeL`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#incident-edge-l).

## Lattice edge to the upper neighbour

The lattice edge from `v` to its upper neighbour.

Formalized by `StatMech.AngleDefect.incidentEdgeU`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#incident-edge-u).

## Lattice edge to the lower neighbour

The lattice edge from `v` to its lower neighbour.

Formalized by `StatMech.AngleDefect.incidentEdgeD`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#incident-edge-d).

## Number of convex corners of a lattice region

The number of vertices of the region with defect `1` (convex corners).

Formalized by `StatMech.AngleDefect.wad_n1`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#wad-n1).

## Number of reflex corners of a lattice region

The number of vertices of the region with defect `-1` (reflex corners).

Formalized by `StatMech.AngleDefect.wad_n3`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 378](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L378). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#wad-n3).

## Number of pinch points of a lattice region

The number of vertices of the region with defect `-2` (pinch points, where two cells meet only
at a corner).

Formalized by `StatMech.AngleDefect.wad_n2d`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/AngleDefect.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#wad-n2d).

## Four corners of a unit cell

The four corners of the unit cell with lower-left corner `c`.

Formalized by `StatMech.Onsager.CellCount.cornersOf`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corners-of).

## Corner count of a lattice point

The number of cells of `S` having the lattice point `v` as a corner.

Formalized by `StatMech.Onsager.CellCount.cornerCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count).

## Vertices of a cell complex

The vertices of the cell complex `S`: all corners of its cells.

Formalized by `StatMech.Onsager.CellCount.cellVerts`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell-verts-2).

## A unit cell has four distinct corners

A cell has four distinct corners.

Formalized by `StatMech.Onsager.CellCount.cornersOf_card`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corners-of-card).

## Characterization of the corners of a unit cell

`v` is a corner of `c` iff `c` is one of the four cells around `v`.

Formalized by `StatMech.Onsager.CellCount.mem_cornersOf_iff`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#mem-corners-of-iff).

## At most four cells meet at a lattice point

At most four cells meet at a lattice point.

Formalized by `StatMech.Onsager.CellCount.cornerCount_le_four`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-le-four).

## Double counting of cell–corner incidences

Double counting of cell–corner incidences: `∑ v, cornerCount S v = 4 * S.card`.

Formalized by `StatMech.Onsager.CellCount.sum_cornerCount`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCount.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#sum-corner-count).

## Corner defect of a set of unit cells

The corner defect of `S`: the number of vertices with exactly one incident cell of `S` (convex
 corners) minus the number with exactly three (reflex corners).

Formalized by `StatMech.Onsager.CellEuler.cornerDiff`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-diff).

## Corner count after adding a cell

Adding a new cell `c` raises the corner count by one exactly at the corners of `c`.

Formalized by `StatMech.Onsager.CellEuler.cornerCount_insert`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-insert).

## Vertices of a cell complex after adding a cell

The vertices of `insert c S`.

Formalized by `StatMech.Onsager.CellEuler.cellVerts_insert`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell-verts-insert).

## Corner weight of a vertex

The weight of a vertex with `k` incident cells in the corner defect: `1` if `k = 1`, `-1` if `k
 = 3`, and `0` otherwise.

Formalized by `StatMech.Onsager.CellEuler.cornerWeight`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-weight).

## A lattice point has an incident cell iff it is a vertex

A lattice point has an incident cell iff it is a vertex of `S`.

Formalized by `StatMech.Onsager.CellEuler.cornerCount_pos_iff_mem`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-pos-iff-mem).

## Corner defect as a sum of vertex weights

The corner defect as a sum of vertex weights.

Formalized by `StatMech.Onsager.CellEuler.cornerDiff_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-diff-eq-sum).

## Change of the corner defect when a cell is added

Change of the corner defect when a new cell is added.

Formalized by `StatMech.Onsager.CellEuler.cornerDiff_insert`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-diff-insert).

## A single cell has corner defect 4

A single cell has corner defect `4`.

Formalized by `StatMech.Onsager.CellEuler.cornerDiff_singleton`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-diff-singleton).

## Corner count as a count of the four surrounding cells

The corner count at `v` counts the cells of `S` among the four cells around `v`.

Formalized by `StatMech.Onsager.CellEuler.cornerCount_eq_inter`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-eq-inter).

## Four edges of a unit cell

The four edges of cell `c`, each encoded by twice its midpoint.

Formalized by `StatMech.Onsager.CellEuler.edgesOf`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#edges-of).

## Edges of a cell complex

The edges of the cell complex `S`, encoded by doubled midpoints.

Formalized by `StatMech.Onsager.CellEuler.cellEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell-edges-2).

## Euler characteristic of a cell complex

The Euler characteristic `V - E + F` of the closed cell complex formed by the cells of `S`.

Formalized by `StatMech.Onsager.CellEuler.eulerChar`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#euler-char).

## A single cell has Euler characteristic 1

A single cell has Euler characteristic `1`.

Formalized by `StatMech.Onsager.CellEuler.eulerChar_singleton`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#euler-char-singleton).

## Change of the Euler characteristic when a cell is added

Change of the Euler characteristic when a new cell is added: new vertices minus new edges plus
 one.

Formalized by `StatMech.Onsager.CellEuler.eulerChar_insert`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEuler.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#euler-char-insert).

## Cardinality of an intersection as a sum of indicators

The size of `S ∩ T` as the sum over `T` of the indicator of `S`. See also `Finset.sum_boole`.

Formalized by `StatMech.Onsager.CellConnect.card_inter_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#card-inter-eq-sum).

## Corner count at the bottom-left corner of a new cell

The corner count at the bottom-left corner of a cell `(x, y) ∉ S`.

Formalized by `StatMech.Onsager.CellConnect.cornerCount_BL`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-bl).

## Corner count at the bottom-right corner of a new cell

The corner count at the bottom-right corner of a cell `(x, y) ∉ S`.

Formalized by `StatMech.Onsager.CellConnect.cornerCount_BR`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-br).

## Corner count at the top-left corner of a new cell

The corner count at the top-left corner of a cell `(x, y) ∉ S`.

Formalized by `StatMech.Onsager.CellConnect.cornerCount_TL`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-tl).

## Corner count at the top-right corner of a new cell

The corner count at the top-right corner of a cell `(x, y) ∉ S`.

Formalized by `StatMech.Onsager.CellConnect.cornerCount_TR`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellCornerCountLocal.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-count-tr).

## Midpoint encoding of a lattice edge

The lattice edge `{a, b}` encoded by the sum `a + b`, twice its midpoint; injective on unit
 edges.

Formalized by `StatMech.Onsager.CellEulerBound.edgeCode`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#edge-code).

## Edge codes of a unit cell are its doubled edge midpoints

The codes of the edges of a cell are `StatMech.Onsager.CellEuler.edgesOf`.

Formalized by `StatMech.Onsager.CellEulerBound.image_cellEdges_edgeCode`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#image-cell-edges-edge-code).

## Agreement of the two edge counts of a cell complex

The two edge counts of a cell complex agree.

Formalized by `StatMech.Onsager.CellEulerBound.card_cellEdges_eq_regEdges`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#card-cell-edges-eq-reg-edges).

## Agreement of the two vertex sets of a cell complex

The two vertex sets of a cell complex agree.

Formalized by `StatMech.Onsager.CellEulerBound.cellVerts_eq_regVerts`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#cell-verts-eq-reg-verts).

## Agreement of the two Euler characteristics of a cell complex

The Euler characteristic `eulerChar` agrees with `StatMech.CellEulerChar.regChi`.

Formalized by `StatMech.Onsager.CellEulerBound.eulerChar_eq_regChi`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#euler-char-eq-reg-chi).

## Top edge of a unit cell

The top edge of the cell `c`.

Formalized by `StatMech.Onsager.CellEulerBound.topEdge`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#top-edge).

## Top edges of a set of cells

The top edges of the cells of `S`.

Formalized by `StatMech.Onsager.CellEulerBound.topEdges`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#top-edges).

## Distinct cells have distinct top edges

Distinct cells have distinct top edges.

Formalized by `StatMech.Onsager.CellEulerBound.card_topEdges`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#card-top-edges).

## Open-top skeleton of a cell complex

The 1-skeleton of the cell complex `S` with the top edge of every cell removed, as a simple
 graph on its vertices.

Formalized by `StatMech.Onsager.CellEulerBound.openTopSkeleton`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#open-top-skeleton).

## Edges of the open-top skeleton

The edges of `openTopSkeleton S` are the edges of `S` other than top edges.

Formalized by `StatMech.Onsager.CellEulerBound.openTopEdgeEquiv`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#open-top-edge-equiv).

## Edge count bound for a connected open-top skeleton

If the open-top skeleton is connected, it has at least as many edges as vertices minus one.

Formalized by `StatMech.Onsager.CellEulerBound.regVerts_card_le`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#reg-verts-card-le).

## Regular Euler characteristic bound via the open-top skeleton

If the open-top skeleton of `S` is connected, then `regChi S ≤ 1`.

Formalized by `StatMech.Onsager.CellEulerBound.regChi_le_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#reg-chi-le-one).

## Euler characteristic bound via the open-top skeleton

If the open-top skeleton of `S` is connected, then `eulerChar S ≤ 1`. See also
 `StatMech.Onsager.CellEulerFaithful.eulerChar_le_one_of_skeleton_connected`, which assumes
 connectivity of the full skeleton.

Formalized by `StatMech.Onsager.CellEulerBound.eulerChar_le_one`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellEulerBound.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#euler-char-le-one).

## Corner defect of two diagonally touching cells

Two diagonally touching cells have corner defect `6`.

Formalized by `StatMech.Onsager.CellGaussBonnet.cornerDiff_cex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-diff-cex).

## Euler characteristic of two diagonally touching cells

Two diagonally touching cells have Euler characteristic `1`.

Formalized by `StatMech.Onsager.CellGaussBonnet.eulerChar_cex`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#euler-char-cex).

## Failure of the cell Gauss–Bonnet formula without a pinch term

The formula `cornerDiff S = 4 * eulerChar S` fails in general (two diagonally touching cells);
 see `StatMech.Onsager.CellGaussBonnetGlobal.cornerDiff_eq` for the correct formula with a pinch
 term.

Formalized by `StatMech.Onsager.CellGaussBonnet.gaussBonnet_stated_false`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#gauss-bonnet-stated-false).

## Indicator of a Boolean

The indicator `1` or `0` of a Boolean.

Formalized by `StatMech.Onsager.CellGaussBonnet.bI`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#b-i).

## Integer-valued corner weight

The vertex weight `cornerWeight` extended to integers.

Formalized by `StatMech.Onsager.CellGaussBonnet.icw`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#icw).

## Integer jump of the corner weight

The change of the vertex weight from `m` to `m + 1` incident cells.

Formalized by `StatMech.Onsager.CellGaussBonnet.ijump`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#ijump).

## Indicator of zero

The indicator of `m = 0`.

Formalized by `StatMech.Onsager.CellGaussBonnet.isZero`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#is-zero).

## Local change of the corner defect

The change of the corner defect when a cell is added, given which of its eight neighbours are
 present (`e, w, n, s, ne, nw, se, sw`).

Formalized by `StatMech.Onsager.CellGaussBonnet.lhsLocal`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#lhs-local).

## Number of new vertices when a cell is added

The number of new vertices when a cell is added, given its eight neighbours.

Formalized by `StatMech.Onsager.CellGaussBonnet.deltaV`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#delta-v).

## Number of new edges when a cell is added

The number of new edges when a cell is added, given its four side neighbours.

Formalized by `StatMech.Onsager.CellGaussBonnet.deltaE`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#delta-e).

## Four times the local change of the Euler characteristic

Four times the change of the Euler characteristic when a cell is added.

Formalized by `StatMech.Onsager.CellGaussBonnet.rhsStated`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#rhs-stated).

## Failure of the local identity without a pinch term

The change of the corner defect is not always four times the change of the Euler
 characteristic.

Formalized by `StatMech.Onsager.CellGaussBonnet.localIdentity_stated_false`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#local-identity-stated-false).

## Local change of the number of pinch points

The change of the number of pinch points at the four corners of a new cell, given its eight
 neighbours.

Formalized by `StatMech.Onsager.CellGaussBonnet.pinchDelta`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-delta).

## Corrected right side of the local Gauss–Bonnet identity

Four times the change of the Euler characteristic plus twice the change of the number of pinch
 points.

Formalized by `StatMech.Onsager.CellGaussBonnet.rhsCorrected`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#rhs-corrected).

## Local cell Gauss–Bonnet identity

Local cell Gauss–Bonnet identity: when a cell is added, the change of the corner defect is four
 times the change of the Euler characteristic plus twice the change of the number of pinch
 points.

Formalized by `StatMech.Onsager.CellGaussBonnet.localIdentity_corrected`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnetLocal.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#local-identity-corrected).

## Corner weight agrees with its integer version

`cornerWeight` agrees with its integer version `icw`.

Formalized by `StatMech.Onsager.CellConnect2.cornerWeight_eq_icw`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-weight-eq-icw).

## Change of a vertex weight when one more cell is incident

The change of a vertex weight when one more cell becomes incident.

Formalized by `StatMech.Onsager.CellConnect2.cornerWeight_jump`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-weight-jump).

## Boolean indicator of a decided proposition

The indicator `bI` of a decided proposition.

Formalized by `StatMech.Onsager.CellConnect2.bI_decide`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#b-i-decide).

## Change of the corner defect in terms of eight neighbours

The change of the corner defect when the cell `(x, y)` is added, in terms of its eight
 neighbours.

Formalized by `StatMech.Onsager.CellConnect2.cornerDiff_jump_sum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-diff-jump-sum).

## Non-vertices are the points with no incident cell

A lattice point is not a vertex of `S` iff no cell of `S` is incident to it.

Formalized by `StatMech.Onsager.CellConnect2.notMem_cellVerts_iff_cornerCount_zero`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#not-mem-cell-verts-iff-corner-count-zero).

## Cardinality of a set difference as a sum of indicators

The size of `s \ t` as a sum of indicators.

Formalized by `StatMech.Onsager.CellConnect2.card_sdiff_eq_sum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#card-sdiff-eq-sum).

## New vertices of an added cell match the local count

The number of new vertices when the cell `(x, y)` is added.

Formalized by `StatMech.Onsager.CellConnect2.sdiff_cellVerts_card_eq_deltaV`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#sdiff-cell-verts-card-eq-delta-v).

## Membership of a cell's bottom edge in the cell complex

The horizontal edge with doubled midpoint `(2x + 1, 2y)` belongs to `S` iff one of the two cells
 it bounds does.

Formalized by `StatMech.Onsager.CellConnect2.mem_cellEdges_bottom`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#mem-cell-edges-bottom).

## Membership of a cell's top edge in the cell complex

The horizontal edge with doubled midpoint `(2x + 1, 2y + 2)` belongs to `S` iff one of the two
 cells it bounds does.

Formalized by `StatMech.Onsager.CellConnect2.mem_cellEdges_top`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#mem-cell-edges-top).

## Membership of a cell's left edge in the cell complex

The vertical edge with doubled midpoint `(2x, 2y + 1)` belongs to `S` iff one of the two cells
 it bounds does.

Formalized by `StatMech.Onsager.CellConnect2.mem_cellEdges_left`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#mem-cell-edges-left).

## Membership of a cell's right edge in the cell complex

The vertical edge with doubled midpoint `(2x + 2, 2y + 1)` belongs to `S` iff one of the two
 cells it bounds does.

Formalized by `StatMech.Onsager.CellConnect2.mem_cellEdges_right`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#mem-cell-edges-right).

## New edges of an added cell match the local count

The number of new edges when the cell `(x, y)` is added.

Formalized by `StatMech.Onsager.CellConnect2.sdiff_cellEdges_card_eq_deltaE`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellLocalChange.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#sdiff-cell-edges-card-eq-delta-e).

## Pinch point of a set of unit cells

The lattice point `v` is a pinch point of `S`: of the four cells around `v`, exactly two
 diagonally opposite ones belong to `S`.

Formalized by `StatMech.Onsager.CellPinch.pinchAt`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-at).

## Pinch point indicator

The indicator of `v` being a pinch point of `S`.

Formalized by `StatMech.Onsager.CellPinch.pinchW`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-w).

## Number of pinch points

The number of pinch points of `S`.

Formalized by `StatMech.Onsager.CellPinch.pinchCount`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-count).

## A pinch point is a vertex

A pinch point is a vertex of `S`.

Formalized by `StatMech.Onsager.CellPinch.pinchAt_mem_cellVerts`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-at-mem-cell-verts).

## Pinch count changes only at the corners of a new cell

Adding a cell changes the pinch count only at the corners of that cell.

Formalized by `StatMech.Onsager.CellPinch.pinchCount_insert`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellPinch.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-count-insert).

## Change of the pinch indicator at the bottom-left corner of a new cell

Change of the pinch indicator at the bottom-left corner of a new cell.

Formalized by `StatMech.Onsager.CellGaussBonnetGlobal.pinch_diff_BL`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-diff-bl).

## Change of the pinch indicator at the bottom-right corner of a new cell

Change of the pinch indicator at the bottom-right corner of a new cell.

Formalized by `StatMech.Onsager.CellGaussBonnetGlobal.pinch_diff_BR`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-diff-br).

## Change of the pinch indicator at the top-left corner of a new cell

Change of the pinch indicator at the top-left corner of a new cell.

Formalized by `StatMech.Onsager.CellGaussBonnetGlobal.pinch_diff_TL`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-diff-tl).

## Change of the pinch indicator at the top-right corner of a new cell

Change of the pinch indicator at the top-right corner of a new cell.

Formalized by `StatMech.Onsager.CellGaussBonnetGlobal.pinch_diff_TR`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-diff-tr).

## Change of the pinch count in terms of eight neighbours

The change of the pinch count when a cell is added, in terms of its eight neighbours.

Formalized by `StatMech.Onsager.CellGaussBonnetGlobal.pinch_jump_sum`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#pinch-jump-sum).

## Cell Gauss–Bonnet formula

Cell Gauss–Bonnet formula: for every finite set of unit cells, convex corners minus reflex
 corners equals four times the Euler characteristic plus twice the number of pinch points.

Formalized by `StatMech.Onsager.CellGaussBonnetGlobal.cornerDiff_eq`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/SimpleGraph/Lattice/TurningNumber/CellGaussBonnet.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html#corner-diff-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrete Gauss–Bonnet formula for polyominoes](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GraphTheory/planar-graphs-and-minors/discrete-gauss-bonnet-formula-for-polyominoes)
