---
declaration: theorem
origin: cited
lean: TemperedFundamentalGroups.SemistableReduction.Statement.strongA, TemperedFundamentalGroups.TateOrbicurve.nondegenerate_of_normalForm, TemperedFundamentalGroups.TateOrbicurve.nondegenerate_of_goodTate, TemperedFundamentalGroups.TateOrbicurve.nondegenerate_of_isTate1, TemperedFundamentalGroups.SemistableReduction.crossingX1, TemperedFundamentalGroups.isOpenEmbedding_temperedPi1Map, TemperedFundamentalGroups.temperedPi1Map_injective, TemperedFundamentalGroups.mem_range_temperedPi1Map
statement: formalized
proof: formalized
---

# tempered-fundamental-groups

[lana-agents/tempered-fundamental-groups](https://github.com/lana-agents/tempered-fundamental-groups) at commit [80bbc808](https://github.com/lana-agents/tempered-fundamental-groups/tree/80bbc80877bdd8ce1628a7be43d70204e0d12d02), 2026-11-03.

> Tempered fundamental groups, developed over integral models.

*Quoted from [README.md](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/README.md), Apache-2.0.*

## Depends on

- [Irreducible element](../../divisibility-in-integral-domains/irreducible-element.md)
- [10.18 Local rings](../../../../../stacks/preliminaries/part-01/10-commutative-algebra/part-01/10-18-local-rings.md)
- [Set](../../../data-structures/sets/set.md)
- [Subgroup](../../group-theory/part-01/subgroup.md)

## Proof depends on

- [Rational fraction fields with one indeterminate over a field](../../../../undergraduate/ring-theory/field-theory/rational-fraction-fields-with-one-indeterminate.md)
- [Hilbert basis theorem](../../polynomials-and-power-series/hilbert-basis-theorem.md)
- [Primitive element theorem](../../../../thousand-plus/algebra/12-field-theory-and-polynomials/primitive-element-theorem.md)
- [Transcendental elements](../../../../undergraduate/ring-theory/field-theory/transcendental-elements.md)
- [Rupture field](../../field-theory/rupture-field.md)
- [Local ring](../../rings/local-ring.md)
- [Algebraically closed field](../../field-theory/algebraically-closed-field.md)
- [Field of fractions of an integral domain](../../field-theory/field-of-fractions-of-an-integral-domain.md)

## Main results

Its Lean names are 8 of the 113 theorems its README names in code:

- [`TemperedFundamentalGroups.SemistableReduction.Statement.strongA`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/SemistableReduction/StrongAProof.lean#L43) (theorem)
- [`TemperedFundamentalGroups.TateOrbicurve.nondegenerate_of_normalForm`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/Andre/TateRestrictIUT.lean#L103) (theorem)
- [`TemperedFundamentalGroups.TateOrbicurve.nondegenerate_of_goodTate`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/Andre/TheoremBGoodTate.lean#L70) (theorem)
- [`TemperedFundamentalGroups.TateOrbicurve.nondegenerate_of_isTate1`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/Andre/TateRestrictIUT.lean#L82) (theorem)
- [`TemperedFundamentalGroups.SemistableReduction.crossingX1`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/SemistableReduction/CrossingX1Proof.lean#L415) (theorem)
- [`TemperedFundamentalGroups.isOpenEmbedding_temperedPi1Map`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/Tempered/CoverImage.lean#L546) (theorem)
- [`TemperedFundamentalGroups.temperedPi1Map_injective`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/Tempered/CoverImage.lean#L533) (theorem)
- [`TemperedFundamentalGroups.mem_range_temperedPi1Map`](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/TemperedFundamentalGroups/Tempered/CoverImage.lean#L537) (theorem)

No file its headlines import, directly or not (523 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.32.0, Mathlib at [81a5d257](https://github.com/leanprover-community/mathlib4/tree/81a5d257c8e410db227a6665ed08f64fea08e997).
- 1,036 .lean files; its Lean libraries `TemperedFundamentalGroups` hold 1,036, declaring 16,672 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/lana-agents/tempered-fundamental-groups/blob/80bbc80877bdd8ce1628a7be43d70204e0d12d02/LICENSE)).

## Builds on

- Mathlib, at [81a5d257](https://github.com/leanprover-community/mathlib4/tree/81a5d257c8e410db227a6665ed08f64fea08e997).
- `oka` (https://github.com/lana-agents/oka) at `405aadd7`.
- `pi1` (https://github.com/lana-agents/pi1) at `d7e705ff`.
- `«continuous-kummer-theory»` (https://github.com/lana-agents/continuous-kummer-theory) at `1d5194fc`.
- `«elliptic-curves»` (https://github.com/lana-agents/elliptic-curves) at `e70086a9`.
- `«formal-schemes»` (https://github.com/lana-agents/formal-schemes) at `e58ecf04`.

## Placement

2 of the 3 Mathlib concepts its headline statements name are in General algebra.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: General algebra (186 of 233 imports, 2.2×). *Proof depends on* names 8 of the 105 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [lana-agents/tempered-fundamental-groups at 80bbc808](https://github.com/lana-agents/tempered-fundamental-groups/tree/80bbc80877bdd8ce1628a7be43d70204e0d12d02)
