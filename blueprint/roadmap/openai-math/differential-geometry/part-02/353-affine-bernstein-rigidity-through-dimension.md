---
declaration: section
origin: cited
lean: OAI.AffineBernstein.affine_bernstein
statement: formalized
proof: formalized
---

# 353. Affine Bernstein rigidity through dimension nine and a smooth dimension-ten counterexample

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every smooth locally uniformly convex affine-maximal graph of dimension three through nine, complete for its induced Euclidean metric, is an elliptic paraboloid. A smooth entire nonquadratic example in dimension ten makes this range sharp. In dimensions three through nine, the paraboloid classification also holds for connected open locally uniformly convex affine-maximal hypersurfaces complete for the affine Berwald–Blaschke metric.

## A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten

We construct a smooth nonquadratic entire graph in dimension ten that solves the classical affine maximal equation and has positive-definite Hessian everywhere. This gives a smooth counterexample to the entire-graph affine Bernstein assertion in dimension ten. Hessian positivity is pointwise; no global uniform lower bound or completeness of the Berwald–Blaschke metric is asserted.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Smooth-Nonquadratic-Affine-Maximal-Graph-in-Dimension-Ten-October-5-2026/affine-maximal-dimension-ten.pdf).

## The affine Bernstein theorem in dimensions three through nine

We prove the Euclidean-complete affine Bernstein conjecture in dimensions three through nine: a smooth locally uniformly convex affine maximal graph is an elliptic paraboloid whenever its induced Euclidean metric is complete. The same conclusion holds, without an initial graph assumption, for connected smooth open (noncompact and without boundary) affine-complete locally uniformly convex immersed hypersurfaces that are classically affine maximal in these dimensions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-affine-Bernstein-theorem-in-dimensions-three-through-nine-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the Euclidean-complete affine Bernstein theorem for graph dimensions $3\le n\le9$. If a smooth function on a nonempty open convex domain has positive-definite Hessian, satisfies the affine maximal equation, and its graph is complete in the induced Euclidean metric, then the domain is all of $\mathbb R^n$ and the function is a positive-definite quadratic polynomial plus an affine term. Its graph is therefore an elliptic paraboloid.

The paper's extension to immersed hypersurfaces without an initial graph assumption is outside this selected statement.

## Lean: Affine Bernstein classification for complete graphs in dimensions three through nine

```lean
theorem affine_bernstein
    (n : ℕ) (hn₃ : 3 ≤ n) (hn₉ : n ≤ 9)
    (Ω : Set (Space n)) (hΩne : Ω.Nonempty) (hΩopen : IsOpen Ω)
    (hΩconvex : Convex ℝ Ω) (u : Space n → ℝ)
    (hu : ContDiffOn ℝ ∞ u Ω)
    (hpos : ∀ x ∈ Ω, (hessian u x).PosDef)
    (hmax : AffineMaximalOn Ω u)
    (hcomplete : EuclideanGraphComplete Ω u) :
    Ω = univ ∧
      (∃ (A : Matrix (Fin n) (Fin n) ℝ) (b : Space n) (c : ℝ),
        A.IsSymm ∧ A.PosDef ∧
        ∀ x, u x = (1 / 2 : ℝ) * (∑ i : Fin n, ∑ j : Fin n, x i * A i j * x j)
          + (∑ i : Fin n, b i * x i) + c) ∧
      (∃ e : (Space n × ℝ) ≃ᵃ[ℝ] (Space n × ℝ),
        e '' standardParaboloid n = graph Ω u)
```

Stated in [AffineBernstein.lean, line 73](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/AffineBernstein.lean#L73). Proved in [lean/OAI/Analysis/AffineBernstein/Main.lean, line 18](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/AffineBernstein/Main.lean#L18).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/353.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/353.md)
