---
declaration: module
origin: cited
lean: AAG10InnerLiftProfile, AAG11InnerLiftEnergy, AAG12InnerLiftCore
statement: formalized
---

# Counterexamples to Grad's conjecture

[lukasliehr/Grad-Conjecture](https://github.com/lukasliehr/Grad-Conjecture) at commit [1b2d0c1e](https://github.com/lukasliehr/Grad-Conjecture/tree/1b2d0c1e8e06fbabd1c388f2c87238215c8bb0f7), 2026-09-22.

## Depends on

A root module states no result, so the node has no statement edges.

## Proof depends on

- [Norms $\lVert\cdot\rVert_p$ on $\R^n$ and $\C^n$](../../../../undergraduate/topology/normed-vector-spaces-on-r-and-c/norms-lvert-cdot-rvert-p-on-r-n-and-c-n.md)
- [Parseval formula for Fourier series](../../fourier-analysis/parseval-formula-for-fourier-series.md)
- [Local extrema](../../differentiability/local-extrema.md)
- [Test functions](../../distribution-theory/test-functions.md)
- [Multilinear map](../../../linear-algebra/fundamentals/multilinear-map.md)
- [Continuity of the sum of a series of functions](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/continuity-of-the-sum-of-a-series-of-functions.md)
- [Taylor's theorem with integral form for remainder (Differential calculus)](../../../../undergraduate/multivariable-calculus/differential-calculus/taylors-theorem-with-integral-form-for-remainder.md)
- [Derivative of a composition of functions (Analysis)](../../differentiability/derivative-of-a-composition-of-functions.md)

## Root modules

The project names no main result in a blueprint, its README or a Main module, so this card stands for its root modules [`AAG10InnerLiftProfile`](https://github.com/lukasliehr/Grad-Conjecture/blob/1b2d0c1e8e06fbabd1c388f2c87238215c8bb0f7/LeanCode/Internal/PhysicalAnalysis/AAG10InnerLiftProfile.lean), [`AAG11InnerLiftEnergy`](https://github.com/lukasliehr/Grad-Conjecture/blob/1b2d0c1e8e06fbabd1c388f2c87238215c8bb0f7/LeanCode/Internal/PhysicalAnalysis/AAG11InnerLiftEnergy.lean), [`AAG12InnerLiftCore`](https://github.com/lukasliehr/Grad-Conjecture/blob/1b2d0c1e8e06fbabd1c388f2c87238215c8bb0f7/LeanCode/Internal/PhysicalAnalysis/AAG12InnerLiftCore.lean): the root of a Lean library its lakefile builds, not a theorem. Of the files they import, directly or not, `Comparator/Showcase_DefinitionSurface.lean` holds `sorry` or `admit`.

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 5,847 .lean files; its Lean libraries `GradAnalyticAlgebras`, `GradApplicationsMHS`, `GradBanachCalculus`, `GradFourierAnalysis`, `GradInternalFunctionalAnalysis`, `GradInternalNonlinearAnalysis` and 7 more hold 5,000 (the first read), declaring 30,144 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- No license file; facts only.

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).

## Placement

Of its imports of Mathlib modules in an overview area, 222 of 295 are in Analysis, 2.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (222 of 295 imports, 2.8×). *Proof depends on* lists 8 of the 96 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [lukasliehr/Grad-Conjecture at 1b2d0c1e](https://github.com/lukasliehr/Grad-Conjecture/tree/1b2d0c1e8e06fbabd1c388f2c87238215c8bb0f7)
