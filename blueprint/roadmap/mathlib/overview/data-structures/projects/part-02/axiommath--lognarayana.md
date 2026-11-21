---
declaration: theorem
origin: cited
lean: List.isUltraLogConcave_fiberDescentPolynomial, List.isLogConcave_fiberDescentPolynomial, List.exists_isLaminar_basisGeneratingPolynomial_eq_fiberTopPolynomial, List.isLorentzian_fiberTopPolynomial, isUltraLogConcave_finsum_prod_narayanaPolynomial, List.isLorentzian_fiberPeakPolynomial, MvPolynomial.IsHomogeneous.hasOnlyNegativeRoots_narayanaTransform, MvPolynomial.splits_narayanaTransform_of_isRealStable
statement: formalized
proof: formalized
---

# LogNarayana

*Log-Concavity in Narayana Transforms and Stack-Sorting Fibers*

[AxiomMath/LogNarayana](https://github.com/AxiomMath/LogNarayana) at commit [0dc63da6](https://github.com/AxiomMath/LogNarayana/tree/0dc63da69e510d52428ae4cbbe3c603ae63f082e), 2026-11-17.

> This is a Lean formalization of log-concavity and real-rootedness for stack-sorting fibers and Narayana transforms.

*Quoted from [README.md](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/README.md), Apache-2.0.*

## Depends on

- [Finite set](../../sets/finite-set.md)
- [List](../../list-like-structures/list.md)
- [Polynomial in several indeterminates](../../../general-algebra/polynomials-and-power-series/polynomial-in-several-indeterminates.md)
- [Set](../../sets/set.md)

## Proof depends on

- [Tree](../../trees/tree.md)
- [Catalan numbers](../../../combinatorics/enumerative-combinatorics/catalan-numbers.md)
- [Ordered ring](../../../general-algebra/rings/ordered-ring.md)
- [Finitely supported function](../../maps/finitely-supported-function.md)
- [Integration by parts](../../../../undergraduate/single-variable-real-analysis/integration/integration-by-parts.md)
- [Convex hull of a subset of an affine real space](../../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-hull-of-a-subset-of-an-affine-real-space.md)
- [Polynomial derivative](../../../../undergraduate/ring-theory/polynomial-rings/polynomial-derivative.md)
- [Dual of a normed space](../../../analysis/normed-vector-spaces-banach-spaces/dual-of-a-normed-space.md)

## Main results

Its Lean names are 8 of the 71 theorems its README names in code:

- [`List.isUltraLogConcave_fiberDescentPolynomial`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/StackSorting/FiberMatroid/Basic.lean#L635) (theorem)
- [`List.isLogConcave_fiberDescentPolynomial`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/StackSorting/FiberMatroid/Basic.lean#L660) (theorem)
- [`List.exists_isLaminar_basisGeneratingPolynomial_eq_fiberTopPolynomial`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/StackSorting/FiberMatroid/Basic.lean#L480) (theorem)
- [`List.isLorentzian_fiberTopPolynomial`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/StackSorting/FiberMatroid/Basic.lean#L551) (theorem)
- [`isUltraLogConcave_finsum_prod_narayanaPolynomial`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/Nestohedron/NarayanaSum.lean#L172) (theorem)
- [`List.isLorentzian_fiberPeakPolynomial`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/StackSorting/Peaks.lean#L304) (theorem)
- [`MvPolynomial.IsHomogeneous.hasOnlyNegativeRoots_narayanaTransform`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/Narayana/RealRootedTransform/Basic.lean#L679) (theorem)
- [`MvPolynomial.splits_narayanaTransform_of_isRealStable`](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LogNarayana/Narayana/RealRootedTransform/Basic.lean#L695) (theorem)

No file its headlines import, directly or not (67 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.33.0, Mathlib at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).
- 108 .lean files; its Lean libraries `LogNarayana`, `Challenge`, `Solution` hold 108, declaring 674 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/AxiomMath/LogNarayana/blob/0dc63da69e510d52428ae4cbbe3c603ae63f082e/LICENSE)).

## Builds on

- Mathlib, at [db584cd6](https://github.com/leanprover-community/mathlib4/tree/db584cd6d46c92f209a44c0f1c829460d327499d).

## Placement

3 of the 4 Mathlib concepts its headline statements name are in Data structures.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Combinatorics (3 of 8 imports, 8.7×), Analysis (2 of 8 imports, 0.9×), Data structures (1 of 8 imports, 0.9×). *Proof depends on* lists 8 of the 42 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [AxiomMath/LogNarayana at 0dc63da6](https://github.com/AxiomMath/LogNarayana/tree/0dc63da69e510d52428ae4cbbe3c603ae63f082e)
