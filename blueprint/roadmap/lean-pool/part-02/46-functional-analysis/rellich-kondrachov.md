---
declaration: theorem
origin: cited
lean: RellichKondrachov.Geometry.Manifold.Sobolev.exists_riemannianFiniteChartData
statement: formalized
proof: formalized
---

# Rellich–Kondrachov compact embedding theorem

> Formalizes the Rellich–Kondrachov compact embedding theorem: the Sobolev embedding H¹ → L² is a compact operator on compact Riemannian manifolds. The proof builds the Euclidean core (compactness of the H¹ → L² inclusion on a fixed compact support via the Fréchet–Kolmogorov criterion and the H¹ translation estimate ‖τₐu − u‖₂ ≤ ‖a‖ · ‖∇u‖₂), glues chart contributions over a finite atlas, and specializes to the Levi-Civita Riemannian volume measure.

*Quoted from the card [LeanPool/projects/rellich-kondrachov.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/rellich-kondrachov.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RellichKondrachov.Geometry.Manifold.Sobolev.RiemannianFiniteChartData.isCompactOperator_h1ToL2_riemannianVolume`](https://leanpool.github.io/lean-pool/LeanPool/RellichKondrachov/Geometry/Manifold/Sobolev/RellichKondrachovRiemannian/Global.html#RellichKondrachov.Geometry.Manifold.Sobolev.RiemannianFiniteChartData.isCompactOperator_h1ToL2_riemannianVolume) (theorem), declared in [LeanPool/RellichKondrachov/Geometry/Manifold/Sobolev/RellichKondrachovRiemannian/Global.lean, line 113](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RellichKondrachov/Geometry/Manifold/Sobolev/RellichKondrachovRiemannian/Global.lean#L113): “On a compact Riemannian manifold, the Sobolev inclusion H¹ → L² for the Levi-Civita volume measure is a compact operator.”
- [`RellichKondrachov.Analysis.FunctionalSpaces.Sobolev.Euclidean.isCompactOperator_h1OnToL2`](https://leanpool.github.io/lean-pool/LeanPool/RellichKondrachov/Analysis/FunctionalSpaces/Sobolev/Euclidean/Rellich.html#RellichKondrachov.Analysis.FunctionalSpaces.Sobolev.Euclidean.isCompactOperator_h1OnToL2) (theorem), declared in [LeanPool/RellichKondrachov/Analysis/FunctionalSpaces/Sobolev/Euclidean/Rellich.lean, line 97](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RellichKondrachov/Analysis/FunctionalSpaces/Sobolev/Euclidean/Rellich.lean#L97): “Euclidean Rellich–Kondrachov compactness: on a fixed compact support K, the H¹ → L² inclusion restricted to functions supported in K is a compact operator.”
- [`RellichKondrachov.Geometry.Manifold.Sobolev.exists_riemannianFiniteChartData`](https://leanpool.github.io/lean-pool/LeanPool/RellichKondrachov/Geometry/Manifold/Sobolev/ChartDataRiemannian.html#RellichKondrachov.Geometry.Manifold.Sobolev.exists_riemannianFiniteChartData) (theorem; a main declaration), declared in [LeanPool/RellichKondrachov/Geometry/Manifold/Sobolev/ChartDataRiemannian.lean, line 162](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RellichKondrachov/Geometry/Manifold/Sobolev/ChartDataRiemannian.lean#L162): “On a compact Riemannian manifold there exists finite chart data equipped with explicit Lipschitz neighborhoods and a subordinate partition of unity, the input to the manifold Rellich glue.”

## Project

- Authors: Adam Benenson.
- Source: *Rellich–Kondrachov compact Sobolev embedding theorem* by Adam Benenson.
- Project repository: [abenenson/rellich-kondrachov](https://github.com/abenenson/rellich-kondrachov).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 46E35.
- In Lean Pool: [LeanPool/RellichKondrachov](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RellichKondrachov), from the card [LeanPool/projects/rellich-kondrachov.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/rellich-kondrachov.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/rellich-kondrachov.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/rellich-kondrachov.yaml)
- [Lean Pool at 701389c0: LeanPool/RellichKondrachov](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RellichKondrachov)
