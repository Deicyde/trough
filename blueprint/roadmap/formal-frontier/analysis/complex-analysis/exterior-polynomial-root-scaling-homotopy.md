---
declaration: def
origin: cited
lean: Polynomial.normalizedCircleMapScaleRootsHomotopy
statement: formalized
---

# Exterior polynomial root-scaling homotopy

([`Polynomial.normalizedCircleMapScaleRootsHomotopy`](https://github.com/FormalFrontier/complex-analysis/blob/c22c803e257c294edf0528a584b66e2735316717/ComplexAnalysis/Analysis/Complex/PolynomialExterior.lean)).
If `p.eval w ≠ 0` whenever `1 ≤ ‖w‖`, root scaling over the real unit interval
joins the normalized leading monomial to the canonical normalized boundary map.
Its characteristic value is `normalize ((p.scaleRoots (t : ℂ)).eval z)`.
The leading coefficient's arbitrary phase is retained; the corresponding degree
statement is `Circle.degree (p.normalizedCircleMap _) = (p.natDegree : ℤ)`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/complex-analysis/blob/c22c803e257c294edf0528a584b66e2735316717/README.md#headline-results) of [FormalFrontier/complex-analysis](https://github.com/FormalFrontier/complex-analysis) at commit [c22c803e](https://github.com/FormalFrontier/complex-analysis/tree/c22c803e257c294edf0528a584b66e2735316717), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `Polynomial.normalizedCircleMapScaleRootsHomotopy` (def), declared in [ComplexAnalysis/Analysis/Complex/PolynomialExterior.lean, line 58](https://github.com/FormalFrontier/complex-analysis/blob/c22c803e257c294edf0528a584b66e2735316717/ComplexAnalysis/Analysis/Complex/PolynomialExterior.lean#L58).

Read from the source at commit [c22c803e](https://github.com/FormalFrontier/complex-analysis/tree/c22c803e257c294edf0528a584b66e2735316717), without running Lean.

## Sources

- [complex-analysis at c22c803e: README, headline results](https://github.com/FormalFrontier/complex-analysis/blob/c22c803e257c294edf0528a584b66e2735316717/README.md#headline-results)
- [Source of `Polynomial.normalizedCircleMapScaleRootsHomotopy` in ComplexAnalysis/Analysis/Complex/PolynomialExterior.lean](https://github.com/FormalFrontier/complex-analysis/blob/c22c803e257c294edf0528a584b66e2735316717/ComplexAnalysis/Analysis/Complex/PolynomialExterior.lean#L58)
