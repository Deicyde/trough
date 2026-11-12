---
declaration: section
origin: cited
lean: OAI.SymmetricMahler.symmetric_mahler, OAI.SymmetricMahler.symmetric_mahler_equality, OAI.GeneralMahler.general_mahler, OAI.SymmetricPolar.symmetric_polar_main
statement: formalized
proof: formalized
---

# 087. The Mahler conjectures, functional inequalities and polar-product symplectic width

3 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the symmetric and nonsymmetric geometric Mahler conjectures in every dimension, with Hanner polytopes and simplices as the respective volume-product minimizers and all equality cases classified. The corresponding sharp functional Mahler inequalities also hold. For *n* ≥ 2, every symmetric polar product $K\times K^\circ$ in dimension $2n$ has Gromov width 4.

## The symmetric Mahler conjecture and its equality cases

We resolve the symmetric Mahler conjecture positively, including its equality classification. Every origin-symmetric convex body in ℝ$^{n}$ has volume product at least $4^n/n!$, with equality exactly for invertible linear images of Hanner polytopes.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-symmetric-Mahler-conjecture-and-its-equality-cases-September-22-2026/paper.pdf); the Lean below formalizes results from it.

## The Mahler Conjecture for General Convex Bodies

We resolve the Mahler conjecture for general convex bodies positively. For every convex body $K\subset\mathbb R^n$, *n* ≥ 1, with Santaló point $s(K)$, $|K|\,|(K-s(K))^\circ|\ge (n+1)^{n+1}/(n!)^2$, with equality exactly for simplices.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Mahler-Conjecture-for-General-Convex-Bodies-September-22-2026/paper.pdf); the Lean below formalizes results from it.

## Symplectic Balls in Symmetric Polar Products

For every integer *n* ≥ 2 and every origin-symmetric convex body $K\subset\mathbb R^n$, we prove that the Gromov width of $\mathop{\mathrm{int}}\nolimits K\times\mathop{\mathrm{int}}\nolimits K^\circ$ is 4. We construct smooth symplectic embeddings of standard balls of every capacity $0\lt c\lt 4$ into this polar product. Volume preservation then resolves the symmetric Mahler conjecture positively in every dimension.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The symmetric Mahler conjecture predicts $|K||K^\circ|\ge4^n/n!$ for every origin-symmetric convex body $K\subset\mathbb R^n$. The formalization establishes this for every $n\ge1$ and characterizes equality exactly by invertible linear images of Hanner bodies, built from intervals using Cartesian products and convex-hull joins.

The nonsymmetric Mahler conjecture and the functional inequalities are not included.

The general Mahler conjecture gives a sharp lower bound for the volume product of a convex body and its polar. For every $n\ge1$ and compact convex body $K\subset\mathbb R^n$ with nonempty interior, the formalization proves
$\inf_{z\in\mathrm{int}\,K}|K|\,|(K-z)^\circ|\ge (n+1)^{n+1}/(n!)^2$.
Equality holds exactly when $K$ is a simplex. The paper's functional inequality is outside this selected statement.

For an origin-symmetric convex body $K\subset\mathbb R^n$, $n\ge2$, the formalized result determines the symplectic ball capacity of $\mathrm{int}\,K\times\mathrm{int}\,K^\circ$: its Gromov width is $4$, and every ball of capacity $0<c<4$ embeds symplectically into it. The normalization assigns capacity $\pi r^2$ to a ball of radius $r$.

No boundary smoothness or strict convexity is assumed. An embedding at capacity exactly $4$ is not asserted.

## Lean: Symmetric Mahler inequality

Stated in [MahlerConjecture.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MahlerConjecture.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem symmetric_mahler {n : ℕ} (hn : 1 ≤ n)
    {K : Set (Fin n → ℝ)} (hK : IsCompact K) (hconv : Convex ℝ K)
    (hsym : ∀ x ∈ K, -x ∈ K) (hint : (interior K).Nonempty) :
    (4:ℝ)^n/(Nat.factorial n:ℝ) ≤
      (volume K).toReal*(volume (coordinatePolar K)).toReal
```

Proved in [lean/OAI/Analysis/Mahler/MainTheorem.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Mahler/MainTheorem.lean#L12).

## Lean: Symmetric Mahler equality characterization

Stated in [SymmetricMahlerEquality.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SymmetricMahlerEquality.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem symmetric_mahler_equality {n : ℕ} (hn : 1 ≤ n)
    {K : Set (Fin n → ℝ)} (hK : IsCompact K) (hconv : Convex ℝ K)
    (hsym : ∀ x ∈ K, -x ∈ K) (hint : (interior K).Nonempty) :
    ((volume K).toReal * (volume (coordinatePolar K)).toReal =
      (4 : ℝ)^n / (Nat.factorial n : ℝ)) ↔ IsLinearHanner K
```

Proved in [lean/OAI/Analysis/Mahler/Classification.lean, line 534](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Mahler/Classification.lean#L534).

## Lean: General Mahler inequality and simplex equality cases

Stated in [GeneralMahler.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GeneralMahler.lean).

```lean
theorem general_mahler {n : ℕ} (hn : 1 ≤ n)
    (K : Set (EuclideanSpace ℝ (Fin n)))
    (hcompact : IsCompact K) (hconvex : Convex ℝ K)
    (hinterior : (interior K).Nonempty) :
    ((n : ℝ) + 1) ^ (n + 1) / (Nat.factorial n : ℝ) ^ 2 ≤ volumeProduct K ∧
      (volumeProduct K = ((n : ℝ) + 1) ^ (n + 1) / (Nat.factorial n : ℝ) ^ 2 ↔
        ∃ vertices : Fin (n + 1) → EuclideanSpace ℝ (Fin n),
          AffineIndependent ℝ vertices ∧ K = convexHull ℝ (range vertices))
```

Proved in [lean/OAI/Geometry/Convex/GeneralMahler/Theorem.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/Convex/GeneralMahler/Theorem.lean#L17).

## Lean: Gromov width of symmetric polar products

Stated in [SymmetricPolar.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SymmetricPolar.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem symmetric_polar_main {n : ℕ} (hn : 2 ≤ n)
    (K : Set (Position n)) (hK : IsSymmetricConvexBody K) :
    gromovWidth (polarProduct K) = 4 ∧
      ∀ c : ℝ, 0 < c → c < 4 →
        HasSymplecticEmbedding (capacityBall n c) (polarProduct K)
```

Proved in [lean/OAI/Geometry/PolarProducts/Main.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/PolarProducts/Main.lean#L7).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/087.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/087.md)
