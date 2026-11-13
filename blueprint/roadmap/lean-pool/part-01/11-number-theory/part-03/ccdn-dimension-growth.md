---
declaration: theorem
origin: cited
lean: CCDN.projective_dimension_growth
statement: formalized
proof: formalized
---

# Polynomial degree bounds for rational points on varieties

> Proves the six main results of Castryck, Cluckers, Dittmann and Nguyen on dimension growth, uniform rational-point counts on curves and hypersurfaces, a lower-bound curve construction, and two-torsion in number-field class groups. Preserves the determinant method, Hilbert-function degree and dimension, bounded birational projections, and the required Bombieri-Vaaler and Mertens dependencies. Imports the main-result closure, excluding the separate intermediate-statement and counterexample library.

*Quoted from the card [LeanPool/projects/ccdn-dimension-growth.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ccdn-dimension-growth.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CCDN.projective_dimension_growth`](https://leanpool.github.io/lean-pool/LeanPool/CCDN/ProjectiveDimensionGrowth.html#CCDN.projective_dimension_growth) (theorem; a main declaration), declared in [LeanPool/CCDN/ProjectiveDimensionGrowth.lean, line 141](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN/ProjectiveDimensionGrowth.lean#L141): “For every ambient projective dimension n, a constant depending only on n bounds the rational points of height at most B on every integral projective variety of degree d at least five by C d^(2n^2+5n-5) B^dim(X), for B at least one.”
- [`CCDN.projectiveCurveBound`](https://leanpool.github.io/lean-pool/LeanPool/CCDN/ProjectiveCurveBound.html#CCDN.projectiveCurveBound) (theorem), declared in [LeanPool/CCDN/ProjectiveCurveBound.lean, line 25](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN/ProjectiveCurveBound.lean#L25): “In ambient dimension n at least two and for B at least one, every integral projective curve of degree d has at most C(n) d^4 B^(2/d) rational points of height at most B, uniformly in its coefficients.”
- [`CCDN.affineCurveBound`](https://leanpool.github.io/lean-pool/LeanPool/CCDN/AffineCurveBound.html#CCDN.affineCurveBound) (theorem), declared in [LeanPool/CCDN/AffineCurveBound.lean, line 24](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN/AffineCurveBound.lean#L24): “In ambient dimension n at least two and for B at least one, every integral affine curve of degree d has at most C(n) d^3 B^(1/d) (log B+d) integer points in the box of radius B.”
- [`CCDN.affine_hypersurface_dimension_growth`](https://leanpool.github.io/lean-pool/LeanPool/CCDN/AffineHypersurfaceDimensionGrowth.html#CCDN.affine_hypersurface_dimension_growth) (theorem), declared in [LeanPool/CCDN/AffineHypersurfaceDimensionGrowth.lean, line 27](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN/AffineHypersurfaceDimensionGrowth.lean#L27): “In N at least three variables, an affine hypersurface of degree d at least five whose top form is absolutely irreducible has at most C(N) d^(3N+9) B^(N-2) integer points in the box of radius B, for B at least one.”
- [`CCDN.projective_integral_curve_lower_bound`](https://leanpool.github.io/lean-pool/LeanPool/CCDN/ProjectiveCurveLowerBound.html#CCDN.projective_integral_curve_lower_bound) (theorem), declared in [LeanPool/CCDN/ProjectiveCurveLowerBound.lean, line 28](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN/ProjectiveCurveLowerBound.lean#L28): “For every positive degree d, an integral projective plane curve and a radius B at least one attain at least d^2 B^(2/d)/5 rational points of height at most B.”
- [`CCDN.classGroup_two_torsion_bound`](https://leanpool.github.io/lean-pool/LeanPool/CCDN/ClassGroupBound.html#CCDN.classGroup_two_torsion_bound) (theorem), declared in [LeanPool/CCDN/ClassGroupBound.lean, line 30](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN/ClassGroupBound.lean#L30): “For number fields K of degree n at least three, the two-torsion cardinality is at most C(n) |disc K|^(1/2-1/(2n)) (log |disc K|)^(1-(n mod 2)).”

## Project

- Authors: Jason Davies, Ralf Stephan, PrimeNumberTheoremAnd contributors.
- Source: *The dimension growth conjecture, polynomial in the degree and without logarithmic factors*, [doi:10.2140/ant.2020.14.2261](https://doi.org/10.2140/ant.2020.14.2261), [arXiv:1904.13109](https://arxiv.org/abs/1904.13109).
- Project repository: [jasondavies/ccdn-dimension-growth](https://github.com/jasondavies/ccdn-dimension-growth), at commit [bb025e72](https://github.com/jasondavies/ccdn-dimension-growth/tree/bb025e7207f3a35a21b898629f5678b72aa7e44f).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11D45, 14G05, 11R29.
- In Lean Pool: [LeanPool/CCDN](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN), from the card [LeanPool/projects/ccdn-dimension-growth.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ccdn-dimension-growth.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/ccdn-dimension-growth.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/ccdn-dimension-growth.yaml)
- [Lean Pool at 701389c0: LeanPool/CCDN](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/CCDN)
