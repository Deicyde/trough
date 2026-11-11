---
declaration: section
origin: cited
lean: StatMech.Lattice.Site, StatMech.Lattice.NearestNeighbour, StatMech.Lattice.hypercubicLattice, StatMech.Lattice.box, StatMech.Lattice.vertexBoundary, StatMech.Lattice.edgeBoundary, StatMech.Lattice.finite_subset_box, StatMech.Lattice.reachable_update_add
statement: formalized
proof: formalized
---

# Hypercubic lattice graphs

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html).

## Site of the hypercubic lattice

A site of the `d`-dimensional hypercubic lattice `ℤ^d`, encoded as an integer vector.

Formalized by `StatMech.Lattice.Site`, an abbreviation declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#site).

## Nearest neighbours in $\mathbb{Z}^d$

Two sites are nearest neighbours when their `ℓ¹` distance `∑ i, |x i - y i|` equals one.

Formalized by `StatMech.Lattice.NearestNeighbour`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#nearest-neighbour).

## Hypercubic lattice $\mathbb{Z}^d$

The hypercubic lattice `ℤ^d`: the simple graph on `Site d` whose edges join
nearest
neighbours.

Formalized by `StatMech.Lattice.hypercubicLattice`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#hypercubic-lattice).

## Box $(-n, n)^d$ in the hypercubic lattice

The box `[-n, n]^d` of sites whose coordinates all have absolute value at most `n`.

Formalized by `StatMech.Lattice.box`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#box).

## Inner vertex boundary of a box

The inner vertex boundary of `box d n`: sites of `box d n` that are not in `box d (n - 1)`.

Formalized by `StatMech.Lattice.vertexBoundary`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#vertex-boundary).

## Edge boundary of a set of sites

The edge boundary of a set `S` of sites: ordered nearest-neighbour pairs with exactly one
endpoint in `S`.

Formalized by `StatMech.Lattice.edgeBoundary`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#edge-boundary).

## Every finite set of sites lies in a box

Every finite set of sites lies in some box `box d R`.

Formalized by `StatMech.Lattice.finite_subset_box`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#finite-subset-box).

## Increasing one coordinate stays in the same component

In `ℤ²`, increasing one coordinate by `n` stays in the same component.

Formalized by `StatMech.Lattice.reachable_update_add`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#reachable-update-add).

## Changing one coordinate stays in the same component

In `ℤ²`, changing one coordinate stays in the same component.

Formalized by `StatMech.Lattice.reachable_update`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#reachable-update).

## Square lattice is connected

The square lattice `ℤ²` is connected.

Formalized by `StatMech.Lattice.hypercubicLattice_two_reachable`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/HypercubicLattice.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#hypercubic-lattice-two-reachable).

## Box $(-n, n)^d$ as a finite set of sites

The box `[-n, n]^d` as a finite set of sites.

Formalized by `StatMech.Lattice.boxSV_boxF`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#box-sv-box-f).

## Vertex boundary of the box $(-n, n)^d$ as a finite set

The vertex boundary of `[-n, n]^d` as a finite set of sites.

Formalized by `StatMech.Lattice.boxSV_vbF`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#box-sv-vb-f).

## Size of the vertex boundary of the box $(-n, n)^d$

The number of sites in the vertex boundary of `[-n, n]^d`.

Formalized by `StatMech.Lattice.boxSV_boundaryCard`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#box-sv-boundary-card).

## Nearest-neighbour pairs inside the box $(-n, n)^d$

The ordered pairs of nearest-neighbour sites that both lie in `[-n, n]^d`.

Formalized by `StatMech.Lattice.boxSV_edgeF`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#box-sv-edge-f).

## Number of nearest-neighbour pairs inside the box $(-n, n)^d$

The number of ordered nearest-neighbour pairs inside `[-n, n]^d`.

Formalized by `StatMech.Lattice.boxSV_edgeCard`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#box-sv-edge-card).

## Box sites with a forward neighbour in the box

Sites of `[-n, n]^d` whose successor in the first coordinate direction is still in the box.

Formalized by `StatMech.Lattice.boxSV_fwdDom`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/BoxSurfaceVolume.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#box-sv-fwd-dom).

## First index where a walk reaches a coordinate value

The first index at which the walk `w` has `k`-th coordinate equal to `r`.

Formalized by `StatMech.Lattice.pvr_firstIdxAtCoord`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PathVisitsRow.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PathVisitsRow.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#pvr-first-idx-at-coord).

## Shift of a site along a coordinate

The site obtained from `x` by adding `s` to its `j`-th coordinate.

Formalized by `StatMech.Lattice.shift`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#shift).

## Neighbour of a site in a coordinate direction

The neighbour of `x` in direction `j`, positive if the flag is `true` and negative otherwise.

Formalized by `StatMech.Lattice.candMap`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#cand-map).

## Nearest neighbours of a lattice site

The finite set of the `2d` nearest neighbours of `x`.

Formalized by `StatMech.Lattice.candFinset`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#cand-finset).

## $\ell^1$ distance on $\mathbb{Z}^d$

The `ℓ¹` (graph) distance `∑ i, |x i - y i|` between two sites.

Formalized by `StatMech.Lattice.l1dist`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/PlanarTopology.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#l1dist).

## Exterior of a box in $\mathbb{Z}^d$

The exterior of the box `[-R, R]^d`: sites with some coordinate of absolute value greater than
`R`.

Formalized by `StatMech.Lattice.exterior`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#exterior).

## Setting a set of coordinates of a lattice site

The site obtained from `p` by setting every coordinate in `T` to `v`.

Formalized by `StatMech.Lattice.setOn`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#set-on).

## Base point of the exterior of a box

The site `(R + 1, …, R + 1)`, a fixed base point of the exterior of `box d R`.

Formalized by `StatMech.Lattice.beacon`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#beacon).

## Complement of a finite set in $\mathbb{Z}^d$ has one infinite component

For `d ≥ 2`, the complement of a finite set of sites of `ℤ^d` has exactly one infinite connected
component.

Formalized by `StatMech.Lattice.unique_infinite_component`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Lattice/UniqueInfiniteComponent.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html#unique-infinite-component).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hypercubic lattice graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-families-and-operations/hypercubic-lattice-graphs)
