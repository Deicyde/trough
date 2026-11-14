---
declaration: section
origin: cited
lean: OAI.HigherDimensionalBallPacking.main_theorem, OAI.HigherDimensionalBallPacking.packing_necessity
statement: formalized
proof: formalized
---

# 343. Symplectic ball packing in higher dimensions

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the Siegel–Yao conjecture for arbitrary capacities in every dimension $2n\ge6$. Finitely many closed symplectic balls of capacities $R_1,\ldots,R_k$ embed disjointly into an open ball of capacity *R* exactly when $\sum_iR_i^n\lt R^n$ and $R_i+R_j\lt R$ for every distinct pair *i*, *j*.

## Symplectic Ball Packings in Higher Dimensions

We prove that, for all integers *n* ≥ 3 and *k* ≥ 1 and all positive real capacities $R_1,\ldots,R_k$, the closed standard symplectic $2n$-balls of these capacities embed disjointly into the interior of a ball of capacity *R* > 0 if and only if

$\displaystyle \sum_{i=1}^k R_i^n\lt R^n, \qquad R_i+R_j\lt R\quad(i\ne j).$

Capacity is *π* times the squared Euclidean radius, and each embedding is defined on a neighborhood of its closed source ball. This proves Siegel and Yao's Conjecture A.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Symplectic-Ball-Packings-in-Higher-Dimensions-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves Siegel and Yao's ball-packing criterion in every symplectic dimension $2n$ with $n\ge3$. For $k\ge1$ closed standard balls of positive capacities $R_1,\ldots,R_k$, disjoint symplectic embeddings into the interior of a ball of capacity $R$ exist exactly when
$\sum_i R_i^n<R^n$ and $R_i+R_j<R$ for all $i\ne j$.
Capacity is $\pi$ times squared Euclidean radius, and each embedding is defined on a neighborhood of its closed source ball. The linked statements include both the full equivalence and the necessity direction.

## Lean: Exact criterion for higher-dimensional symplectic ball packings

```lean
theorem main_theorem (n k : ℕ) (hn : 3 ≤ n) (hk : 1 ≤ k)
    (R : ℝ) (r : Fin k → ℝ) (hR : 0 < R) (hr : ∀ i, 0 < r i) :
    HasPacking n k R r ↔ PackingInequalities n k R r
```

Stated in [BallPacking.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BallPacking.lean#L36). Proved in [lean/OAI/Geometry/BallPacking/Main.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/BallPacking/Main.lean#L17).

## Lean: Necessity of the volume and pairwise capacity inequalities

```lean
theorem packing_necessity (n k : ℕ) (hn : 3 ≤ n) (hk : 1 ≤ k)
    (R : ℝ) (r : Fin k → ℝ) (hR : 0 < R) (hr : ∀ i, 0 < r i)
    (hp : HasPacking n k R r) : PackingInequalities n k R r
```

Stated in [BallPackingNecessity.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BallPackingNecessity.lean#L38). Proved in [lean/OAI/Geometry/BallPacking/Necessity/PackingNecessity.lean, line 402](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/BallPacking/Necessity/PackingNecessity.lean#L402).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/343.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/343.md)
