---
declaration: module
origin: cited
lean: CheckAxioms
statement: formalized
proof: formalized
---

# Hironaka

[MingchenXia/hironaka](https://github.com/MingchenXia/hironaka) at commit [1dcf2958](https://github.com/MingchenXia/hironaka/tree/1dcf29586578031c66fa9cd7061b8004f3b807dd), 2026-10-25.

> Lean 4 / Mathlib proofs of principalization and resolution of singularities in complex-analytic geometry, including canonical marked-ideal resolution, and de Jong's alteration theorem for schemes over every field.

*Quoted from [README.md](https://github.com/MingchenXia/hironaka/blob/1dcf29586578031c66fa9cd7061b8004f3b807dd/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Maximum modulus principle](../../analysis/complex-analysis/maximum-modulus-principle.md)
- [Quotient space (Fundamentals)](../../linear-algebra/fundamentals/quotient-space.md)
- [Splitting field](../../general-algebra/field-theory/splitting-field.md)
- [Smooth map between manifolds](../../geometry/differentiable-manifolds/part-01/smooth-map-between-manifolds.md)
- [$C^k$ function](../../analysis/differentiability/c-k-function.md)
- [Closure](../general-topology/part-01/closure.md)
- [Multilinear map](../../linear-algebra/fundamentals/multilinear-map.md)
- [Topological space](../general-topology/part-01/topological-space.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`CheckAxioms`](https://github.com/MingchenXia/hironaka/blob/1dcf29586578031c66fa9cd7061b8004f3b807dd/scripts/CheckAxioms.lean): the root of a Lean library its lakefile builds, not a theorem. No file it imports, directly or not (1561 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 3,662 .lean files; its Lean libraries `Hironaka`, `CheckAxioms` hold 1,561, declaring 12,287 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/MingchenXia/hironaka/blob/1dcf29586578031c66fa9cd7061b8004f3b807dd/LICENSE)).

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- `DeJongAlterations`.

## Placement

Of its imports of Mathlib modules in an overview area, 121 of 825 are in Topology, 2.0 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Topology (121 of 825 imports, 2.0×), Analysis (413 of 825 imports, 1.8×), General algebra (143 of 825 imports, 0.5×). *Proof depends on* names 8 of the 98 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [MingchenXia/hironaka at 1dcf2958](https://github.com/MingchenXia/hironaka/tree/1dcf29586578031c66fa9cd7061b8004f3b807dd)
