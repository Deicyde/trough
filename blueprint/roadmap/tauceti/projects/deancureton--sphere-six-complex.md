---
declaration: theorem
origin: cited
lean: SphereSixComplex.sphere_six_admits_complex_structure
statement: formalized
proof: formalized
---

# A Complex Structure on the Six-Sphere

[deancureton/sphere-six-complex](https://github.com/deancureton/sphere-six-complex) at commit [b783b990](https://github.com/deancureton/sphere-six-complex/tree/b783b990d46c5f5ce02a4ecbbb2c02408b452cde), 2026-10-08.

> A Lean formalization of the construction in [the paper](https://alpo.ge/s6.pdf) ([local copy](https://github.com/deancureton/sphere-six-complex/blob/b783b990d46c5f5ce02a4ecbbb2c02408b452cde/references/s6.pdf)): a compact complex threefold diffeomorphic to the standard smooth six-sphere.

*Quoted from [README.md](https://github.com/deancureton/sphere-six-complex/blob/b783b990d46c5f5ce02a4ecbbb2c02408b452cde/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Product of vector spaces](../../mathlib/undergraduate/linear-algebra/fundamentals/product-of-vector-spaces.md)
- [Path connectedness](../../mathlib/undergraduate/topology/topology-and-metric-spaces/path-connectedness.md)
- [Open map](../../mathlib/overview/topology/general-topology/part-01/open-map.md)
- [Product of manifolds](../../mathlib/overview/geometry/differentiable-manifolds/part-01/product-of-manifolds.md)
- [Schwarz lemma](../../mathlib/overview/analysis/complex-analysis/schwarz-lemma.md)
- [Analyticity of holomorphic functions](../../mathlib/overview/analysis/complex-analysis/analyticity-of-holomorphic-functions.md)
- [Chain complex](../../mathlib/overview/general-algebra/homological-algebra/chain-complex.md)
- [Urysohn's lemma](../../mathlib/overview/topology/general-topology/part-02/urysohns-lemma.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`SphereSixComplex.sphere_six_admits_complex_structure`](https://github.com/deancureton/sphere-six-complex/blob/b783b990d46c5f5ce02a4ecbbb2c02408b452cde/SphereSixComplex/Final.lean#L39) (theorem)

No file its headlines import, directly or not (710 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc3, Mathlib at [6b7abb3c](https://github.com/leanprover-community/mathlib4/tree/6b7abb3c7686292736be2955bd3eb9ebf63b456a).
- 764 .lean files; its Lean libraries `SphereSixComplex`, `ForMathlib`, `ChallengeDefs`, `Challenge`, `Solution` hold 719, declaring 8,351 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: failing.
- License: Apache-2.0 ([LICENSE](https://github.com/deancureton/sphere-six-complex/blob/b783b990d46c5f5ce02a4ecbbb2c02408b452cde/LICENSE)).

## Builds on

- Mathlib, at [6b7abb3c](https://github.com/leanprover-community/mathlib4/tree/6b7abb3c7686292736be2955bd3eb9ebf63b456a).
- `DifferentialGeometry` (https://github.com/deancureton/differential-geometry.git) at `67e3631e`.
- `JordanCurveTheorem` (https://github.com/Paul-Lez/jordan-curve-theorem.git) at `61a188ba`.
- `SmoothSixSphere` (https://github.com/deancureton/lean-proofs.git) at `613af5fc`.
- [TauCeti](../README.md) at `6175f404`.
- `VanKampen`.

## Placement

Its Lake manifest requires `TauCeti`, whose modules 27 files of the project import.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (33 of 220 imports, 6.4×), Topology (58 of 220 imports, 3.5×), Analysis (64 of 220 imports, 1.1×). *Proof depends on* lists 8 of the 65 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [deancureton/sphere-six-complex at b783b990](https://github.com/deancureton/sphere-six-complex/tree/b783b990d46c5f5ce02a4ecbbb2c02408b452cde)
