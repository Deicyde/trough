---
declaration: module
origin: cited
lean: KIP126, KIP126.AdamsComputation, KIP126.AdamsSynthetic
statement: formalized
---

# Mathematics and scope

[GAIR-NLP/Kervaire126](https://github.com/GAIR-NLP/Kervaire126) at commit [565e2df6](https://github.com/GAIR-NLP/Kervaire126/tree/565e2df6bb614112023c765bd4f160f110f64a5b), 2026-11-06.

> **Project blog coming soon.**

*Quoted from [README.md](https://github.com/GAIR-NLP/Kervaire126/blob/565e2df6bb614112023c765bd4f160f110f64a5b/README.md), Apache-2.0.*

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Urysohn's lemma](../general-topology/part-02/urysohns-lemma.md)
- [Abelian category](../../general-algebra/category-theory/abelian-category.md)
- [The category of modules over a ring](../../linear-algebra/fundamentals/the-category-of-modules-over-a-ring.md)
- [Monoidal category](../../general-algebra/category-theory/monoidal-category.md)
- [The category of topological spaces](../general-topology/part-01/the-category-of-topological-spaces.md)
- [Direct sum](../../../undergraduate/linear-algebra/fundamentals/direct-sum.md)
- [Functor](../../general-algebra/category-theory/functor.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`KIP126`](https://github.com/GAIR-NLP/Kervaire126/blob/565e2df6bb614112023c765bd4f160f110f64a5b/KIP126.lean), [`KIP126.AdamsComputation`](https://github.com/GAIR-NLP/Kervaire126/blob/565e2df6bb614112023c765bd4f160f110f64a5b/KIP126/AdamsComputation.lean), [`KIP126.AdamsSynthetic`](https://github.com/GAIR-NLP/Kervaire126/blob/565e2df6bb614112023c765bd4f160f110f64a5b/KIP126/AdamsSynthetic.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `KIP126/AdamsComputation/Internal/NuCofiberArchive/Realization.lean`, `KIP126/AdamsComputation/Standard.lean`, `KIP126/AdamsComputation/Table/D2.lean`, `KIP126/AdamsComputation/Table/Relations.lean`, `KIP126/AdamsSynthetic/Completed/Acyclic.lean`, `KIP126/AdamsSynthetic/Completed/Adams.lean`, `KIP126/AdamsSynthetic/Completed/AdamsScope.lean`, `KIP126/AdamsSynthetic/Completed/Background.lean`, `KIP126/AdamsSynthetic/Completed/Coefficients.lean`, `KIP126/AdamsSynthetic/Completed/Completion.lean`, `KIP126/AdamsSynthetic/Completed/Completion/Classical.lean`, `KIP126/AdamsSynthetic/Completed/Filtration.lean`, `KIP126/AdamsSynthetic/Completed/FirstQuotientCompatibility.lean`, `KIP126/AdamsSynthetic/Completed/Foundations.lean`, `KIP126/AdamsSynthetic/Completed/HomotopyCoproduct.lean`, `KIP126/AdamsSynthetic/Completed/MappingOperations.lean`, `KIP126/AdamsSynthetic/Completed/Separation.lean`, `KIP126/AdamsSynthetic/Completed/ShiftOperations.lean`, `KIP126/AdamsSynthetic/Completed/SpectrumScope/Basic.lean`, `KIP126/AdamsSynthetic/Completed/SphereCoproduct.lean` hold `sorry` or `admit`.

## Project

- Lean v4.32.2, Mathlib at [905b9581](https://github.com/leanprover-community/mathlib4/tree/905b95818eb32af7874a58b427f50c1711a5e96c).
- 1,402 .lean files; its Lean libraries `KIP126` hold 1,402, declaring 4,428 names, with `sorry` in 44 files and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/GAIR-NLP/Kervaire126/blob/565e2df6bb614112023c765bd4f160f110f64a5b/LICENSE)).

## Builds on

- Mathlib, at [905b9581](https://github.com/leanprover-community/mathlib4/tree/905b95818eb32af7874a58b427f50c1711a5e96c).

## Placement

Of its imports of Mathlib modules in an overview area, 103 of 439 are in Topology, 3.1 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Topology (103 of 439 imports, 3.1×), Linear algebra (47 of 439 imports, 1.8×), General algebra (247 of 439 imports, 1.6×). *Proof depends on* names 8 of the 42 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [GAIR-NLP/Kervaire126 at 565e2df6](https://github.com/GAIR-NLP/Kervaire126/tree/565e2df6bb614112023c765bd4f160f110f64a5b)
