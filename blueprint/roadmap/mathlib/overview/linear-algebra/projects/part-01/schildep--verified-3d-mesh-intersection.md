---
declaration: module
origin: cited
lean: Web
statement: formalized
proof: formalized
---

# verified-3d-mesh-intersection

*Formally verified 3D mesh intersection - trust 93 lines of spec, not 1000+ lines of AI-written code*

[schildep/verified-3d-mesh-intersection](https://github.com/schildep/verified-3d-mesh-intersection) at commit [c537025f](https://github.com/schildep/verified-3d-mesh-intersection/tree/c537025f69511110108acc9608dc1cdb19025057), 2026-07-28.

> To my knowledge, this is the first formally verified implementation of a 3D constructive solid geometry (CSG) operation: mesh intersection, implemented in Lean 4 and verified against [a concise specification](https://github.com/schildep/verified-3d-mesh-intersection/blob/c537025f69511110108acc9608dc1cdb19025057/README.md#background-and-formalization) that pins down the surface of the resulting mesh exactly and guarantees practical well-formedness conditions on the triangulation. (See also [related work](https://github.com/schildep/verified-3d-mesh-intersection/blob/c537025f69511110108acc9608dc1cdb19025057/README.md#related-work).)

*Quoted from [README.md](https://github.com/schildep/verified-3d-mesh-intersection/blob/c537025f69511110108acc9608dc1cdb19025057/README.md), MIT, Copyright (c) 2026 P Schilde.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Helly's theorem](../../../../thousand-plus/geometry-and-topology/52-convex-and-discrete-geometry/hellys-theorem.md)
- [Carathéodory's theorem](../../../analysis/convexity/caratheodorys-theorem.md)
- [Extreme point](../../../../undergraduate/affine-and-euclidean-geometry/convexity/extreme-point.md)
- [Cross product](../../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/low-dimensions/cross-product.md)
- [Affine span](../../../geometry/affine-and-euclidean-geometry/affine-span.md)
- [Finite](../../../combinatorics/pigeonhole-principles/finite.md)
- [Convex hull of a subset of an affine real space](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Affine subspace](../../../geometry/affine-and-euclidean-geometry/affine-subspace.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Web`](https://github.com/schildep/verified-3d-mesh-intersection/blob/c537025f69511110108acc9608dc1cdb19025057/Web.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (7 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.15.0, Mathlib at [e9ae2a61](https://github.com/leanprover-community/mathlib4/tree/e9ae2a61ef5c99d6edac84f0d04f6324c5d97f67).
- 200 .lean files; its Lean libraries `CSG`, `Web` hold 200, declaring 4,244 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: MIT ([LICENSE](https://github.com/schildep/verified-3d-mesh-intersection/blob/c537025f69511110108acc9608dc1cdb19025057/LICENSE)).

## Builds on

- Mathlib, at [e9ae2a61](https://github.com/leanprover-community/mathlib4/tree/e9ae2a61ef5c99d6edac84f0d04f6324c5d97f67).

## Placement

10 of the 31 Mathlib concepts its files name are in Linear algebra.

## Mathlib use

*Proof depends on* lists 8 of the 31 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [schildep/verified-3d-mesh-intersection at c537025f](https://github.com/schildep/verified-3d-mesh-intersection/tree/c537025f69511110108acc9608dc1cdb19025057)
