---
declaration: module
origin: cited
lean: Proetale
statement: formalized
---

# Proétale cohomology in Lean

[chrisflav/proetale](https://github.com/chrisflav/proetale) at commit [c815a076](https://github.com/chrisflav/proetale/tree/c815a07678fc5937809e6d4c8af78a107b064056), 2026-07-14.

> This repository contains a (WIP) formalisation of (pro)étale cohomology in Lean following the paper [[BS13]](https://arxiv.org/abs/1309.1198) by Bhatt and Scholze.

*Quoted from [README.md](https://github.com/chrisflav/proetale/blob/c815a07678fc5937809e6d4c8af78a107b064056/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Comma category](../../general-algebra/category-theory/comma-category.md)
- [The category of algebras over a ring](../../general-algebra/algebras-over-a-ring/the-category-of-algebras-over-a-ring.md)
- [Maximal ideal](../../general-algebra/ideals-and-quotients/maximal-ideal.md)
- [Prime ideal](../../general-algebra/ideals-and-quotients/prime-ideal.md)
- [Ring morphism](../../general-algebra/rings/ring-morphism.md)
- [Small category](../../general-algebra/category-theory/small-category.md)
- [Localization](../../general-algebra/rings/localization.md)
- [Connected components](../../../undergraduate/topology/topology-and-metric-spaces/connected-components.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root module [`Proetale`](https://github.com/chrisflav/proetale/blob/c815a07678fc5937809e6d4c8af78a107b064056/Proetale.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files it imports, directly or not, `Comparator/Challenge.lean`, `Comparator/Solution.lean`, `Proetale/Algebra/Bijective.lean`, `Proetale/Algebra/HenselianLocalRing.lean`, `Proetale/Algebra/IndBijectiveOnStalks.lean`, `Proetale/Algebra/IndEtale.lean`, `Proetale/Algebra/IndWeaklyEtale.lean`, `Proetale/Algebra/IndZariski.lean`, `Proetale/Algebra/IntegralLocal.lean`, `Proetale/Algebra/WContractible.lean`, `Proetale/Algebra/WLocalization/Basic.lean`, `Proetale/Algebra/WStrictLocalization.lean`, `Proetale/Algebra/WeaklyEtaleField.lean`, `Proetale/Mathlib/AlgebraicGeometry/Sites/Small.lean`, `Proetale/Mathlib/CategoryTheory/MorphismProperty/Ind.lean`, `Proetale/Mathlib/CategoryTheory/MorphismProperty/IndSpreads.lean`, `Proetale/Mathlib/CategoryTheory/Sites/InducedTopology.lean`, `Proetale/Mathlib/RingTheory/Henselian.lean`, `Proetale/Mathlib/Topology/Connected/TotallyDisconnected.lean`, `Proetale/Morphisms/ProAffineEtale.lean` hold `sorry` or `admit`.

## Project

- Lean v4.30.0, Mathlib at [9a568f0b](https://github.com/leanprover-community/mathlib4/tree/9a568f0b75d28670664e6d6862d6e01c4625e380).
- 157 .lean files; its Lean libraries `Proetale`, `Definitions`, `Challenge`, `Solution` hold 148, declaring 1,011 names, with `sorry` in 26 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/chrisflav/proetale/blob/c815a07678fc5937809e6d4c8af78a107b064056/LICENSE)).

## Builds on

- Mathlib, at [9a568f0b](https://github.com/leanprover-community/mathlib4/tree/9a568f0b75d28670664e6d6862d6e01c4625e380).
- `upstreamer` (https://github.com/chrisflav/upstreamer) at `f0cd4b14`.

## Placement

Of its imports of Mathlib modules in an overview area, 35 of 265 are in Geometry, 5.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (35 of 265 imports, 5.6×), General algebra (184 of 265 imports, 2.0×), Topology (38 of 265 imports, 1.9×). *Proof depends on* lists 8 of the 42 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [chrisflav/proetale at c815a076](https://github.com/chrisflav/proetale/tree/c815a07678fc5937809e6d4c8af78a107b064056)
