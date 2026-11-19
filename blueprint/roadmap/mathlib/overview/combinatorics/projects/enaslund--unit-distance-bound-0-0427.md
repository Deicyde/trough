---
declaration: theorem
origin: cited
lean: UnitDistance.Sqrt241.V2.target_of_wide_zeta_bound
statement: formalized
proof: formalized
---

# An Exponent of 1.043 for the Unit Distance Problem

[enaslund/unit-distance-bound-0.0427](https://github.com/enaslund/unit-distance-bound-0.0427) at commit [b43f0c5b](https://github.com/enaslund/unit-distance-bound-0.0427/tree/b43f0c5bfd7a3276597c6a47ad99b9e5b8d3d21f), 2026-10-10.

> This repository holds the paper *An Exponent of 1.043 for the Unit Distance Problem* by Eric Naslund, its predecessors, their computer-assisted certificates, and a Lean formalization. The papers give lower bounds for the number of unit-distance pairs among points in the Euclidean plane. Each result constructs finite sets `U_j` with `|U_j| → ∞` and `u(U_j)/|U_j|^(1+δ) → ∞`, where `u` counts unordered pairs at distance one; equivalently, `u(n) ≥ n^(1+δ)` for arbitrarily large `n`. No bound is asserted for every sufficiently large `n`.

*Quoted from [README.md](https://github.com/enaslund/unit-distance-bound-0.0427/blob/b43f0c5bfd7a3276597c6a47ad99b9e5b8d3d21f/README.md), Apache-2.0.*

## Depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)

## Proof depends on

- [Euclidean domain](../../general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Borel–Carathéodory theorem](../../../thousand-plus/analysis/30-functions-of-a-complex-variable/borel-caratheodory-theorem.md)
- [Group morphism](../../general-algebra/group-theory/part-01/group-morphism.md)
- [Direct product of groups](../../../undergraduate/group-theory/basic-definitions/direct-product-of-groups.md)
- [Ostrowski's theorem](../../../thousand-plus/number-theory/part-02/ostrowskis-theorem.md)
- [Dirichlet unit theorem](../../general-algebra/algebraic-number-theory/dirichlet-unit-theorem.md)
- [Quotient group](../../general-algebra/group-theory/part-01/quotient-group.md)
- [Principal ideal domain](../../general-algebra/divisibility-in-integral-domains/principal-ideal-domain.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`UnitDistance.Sqrt241.V2.target_of_wide_zeta_bound`](https://github.com/enaslund/unit-distance-bound-0.0427/blob/b43f0c5bfd7a3276597c6a47ad99b9e5b8d3d21f/lean/UnitDistance/Sqrt241/V2/Final.lean#L84) (theorem)

No file its headlines import, directly or not (2316 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc2, Mathlib at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).
- 2,436 .lean files; its Lean libraries `UnitDistance`, `ChallengeZeta241`, `SolutionZeta241`, `AuditSupport`, `ChallengeZeta`, `SolutionZeta` hold 2,433, declaring 30,524 names, with `sorry` in 2 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/enaslund/unit-distance-bound-0.0427/blob/b43f0c5bfd7a3276597c6a47ad99b9e5b8d3d21f/LICENSE)).

## Builds on

- Mathlib, at [06535612](https://github.com/leanprover-community/mathlib4/tree/065356127b1dc0016f66b7283ce0ce2c4055aa55).

## Placement

Placed by hand. Its README states lower bounds for the number of unit-distance pairs among points in the Euclidean plane, a counting question of combinatorial geometry; the number fields it imports are its tools.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (1329 of 2160 imports, 1.7×), Analysis (259 of 2160 imports, 0.4×). *Proof depends on* lists 8 of the 184 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [enaslund/unit-distance-bound-0.0427 at b43f0c5b](https://github.com/enaslund/unit-distance-bound-0.0427/tree/b43f0c5bfd7a3276597c6a47ad99b9e5b8d3d21f)
