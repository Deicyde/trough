---
declaration: section
origin: cited
lean: OAI.ForestSpace.main_theorem, OAI.SegmentLenses.midpoint_lens_main, OAI.DiamondDistortion.headline_all_pairs, OAI.ExactModuli.exact_main, OAI.ExactModuli.kadets_werner_existence, OAI.ExactModuli.exact_example, OAI.BoundedTreePotentials.TreeCalculus.main_counterexample, OAI.IndependentProducts.main_general
statement: formalized
---

# 331. Reflexive midpoint convexity and diamond distortion

7 manuscripts and 12 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a real reflexive Banach space with an asymptotically midpoint uniformly convex norm but no equivalent asymptotically uniformly convex norm, extending Baudier's separation to reflexive spaces. In the same space, depth-*k* countably branching diamonds require distortion at least $\sqrt{1+k/12}$, so midpoint uniform convexity does not force uniformly bounded diamond distortion even under reflexivity.

## Asymptotic midpoint uniform convexity and unbounded diamond distortion in a reflexive tree space

We construct a separable reflexive real Banach space whose given norm is asymptotically midpoint uniformly convex but which admits no asymptotically uniformly convex equivalent norm. Its averaged midpoint modulus is at least $\sqrt{1+t^2/12}-1$, and the countably branching diamond of depth *k* has distortion at least $\sqrt{1+k/12}$ in this space. This gives a negative answer to the reflexive diamond converse for asymptotic uniform convexifiability.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Asymptotic-midpoint-uniform-convexity-and-unbounded-diamond-distortion-in-a-reflexive-tree-space-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Midpoint lenses in segment spaces

For a real segment-forest dual with unbounded finite component heights and the real infinite-height coordinate predual, we bound the tail of an arbitrary displacement in a symmetric lens by $2\sqrt{R^2-\|x\|^2}$, where *R* is the lens radius and *x* is its finitely supported center. Both given norms are asymptotically midpoint uniformly convex, although neither space admits an equivalent asymptotically uniformly convex norm. The finite-height forest dual is reflexive.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Midpoint-lenses-in-segment-spaces-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Distortion of countably branching diamonds from midpoint and tree energies

We derive quantitative distortion bounds for countably branching diamond graphs from midpoint estimates and direct tree energies. In the dual of a finite-height segment forest, every distortion-*D* embedding of the depth-*k* diamond satisfies $D^2\ge1+k/4$. The same bound holds in the infinite-height coordinate predual. We also obtain power-type distortion bounds for path-cost and recursive tree norms.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Diamond-distortion-from-midpoint-and-tree-energies-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Exact asymptotic moduli in a Daugavet subspace of L1

For an infinite-dimensional real subspace of $L^{1}$ whose unit ball is totally bounded in measure and whose norm has the Daugavet property, we compute the averaged midpoint and one-sided asymptotic moduli at every unit center. They are $\max\{t/2,t-1\}$ and $\max\{0,t-2\}$, respectively. The same weak-neighborhood geometry excludes every equivalent asymptotically uniformly convex norm. A quantitative realization of the Kadets–Werner construction supplies a space with both hypotheses.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Exact-asymptotic-moduli-in-a-Daugavet-subspace-of-L1-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Midpoint convexity from bounded tree potentials and path costs

Four real Banach spaces defined by bounded tree potentials satisfy the averaged asymptotic midpoint bound $\widehat\delta(t)\ge\sqrt{1+t^2/4}-1$ for $0\lt t\lt 1$, while none admits an asymptotically uniformly convex (AUC) renorming. On finite-height trees, the globally constrained norm equals the least additive cost of a Hilbert vector and root paths. The quadratic path and segment-start outer Hilbert sums are reflexive and asymptotically midpoint uniformly convex, and admit no equivalent AUC norm.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Independent products in real L1: asymptotic midpoint convexity without AUC renormings

For a countably branching tree, the closed real $L^{1}$ spans of products of independent exponential or Gaussian-square multipliers along its paths have positive averaged asymptotic midpoint moduli and admit no equivalent asymptotically uniformly convex norm. The renorming obstruction holds for every positive nonconstant mean-one multiplier with finite second moment.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Independent-products-in-real-L1-asymptotic-midpoint-convexity-without-AUC-renormings-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## Midpoint convexity from two recursive potentials

We study tree norms computed by two least nonnegative fields whose difference is the vector. For Euclidean child aggregation, two root-sum spaces have an averaged asymptotic midpoint modulus of at least $t^3/128$ for $0\lt t\lt 1$, including a reflexive joining-root space. A reflexive construction with a fixed zero root also satisfies a homogeneous cubic estimate. These spaces admit no equivalent asymptotically uniformly convex norm. We also obtain sixth-power and cubic estimates when the aggregation exponent depends on the height of a finite component.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/manuscript.pdf); the Lean below formalizes results from it.

## The Lean formalization

The paper constructs a Banach space whose midpoint geometry is asymptotically uniformly convex even though no equivalent norm is asymptotically uniformly convex in the usual one-sided sense. The formalization proves that the full dual of the specified segment-norm completion is infinite-dimensional, separable, and reflexive; its averaged midpoint modulus is at least $\sqrt{1+t^2/12}-1$ for every $t>0$, while every equivalent norm fails asymptotic uniform convexity. It also proves that an embedding of a depth-$k$ countably branching diamond has distortion at least $\sqrt{1+k/12}$.

The general-forest and word-forest results use the closed span of the coordinate functionals. Their conclusions retain the finite-ancestor and equivalent-norm hypotheses, including the scale $\alpha/(2\beta)$ when $0<\alpha\le\beta$ and the new norm lies between $\alpha$ and $\beta$ times the original norm; they do not identify that span with the full dual or assert reflexivity for every forest.

The paper controls midpoint lenses in Banach spaces defined by tree-segment norms. The formalization proves the following estimate in both the full dual of the finite-height forest space and the coordinate predual of the infinite-tree space. If $x$ is supported on a finite ancestral set $H$, $R\ge0$, and $\|x+y\|,\|x-y\|\le R$, then the part of $y$ outside $H$ has norm at most $2\sqrt{R^2-\|x\|^2}$.

The formalization also covers selected consequences for averaged midpoint moduli and separated families of vectors, together with reflexivity and renorming obstructions. This scope concerns the segment-space results; the companion results on diamond energies remain separate.

The paper studies embeddings of countably branching diamond graphs into Banach spaces built from tree segments. The formalization proves that every embedding of the depth-$k$ diamond with distortion $D$, at any positive scale, satisfies $1+k/4\le D^2$ in either of two spaces: the full dual of the completed finite-height forest space and the closed coordinate span in the dual of the infinite-tree space. The bound applies to all pairs of vertices and is unconditional.

The formalization also contains selected graph deductions under explicit companion assumptions. Twenty-two of those companion inputs are assumed in these deductions; the diamond distortion bound above does not require them.

The paper exhibits a real $L_1$ subspace with positive averaged midpoint convexity but no equivalent asymptotically uniformly convex norm. For every closed infinite-dimensional subspace whose unit ball is precompact in measure and which has the Daugavet property, the formalization computes the moduli at every unit vector: the averaged midpoint modulus is $\max(t/2,t-1)$ and the usual one-sided asymptotic modulus is $\max(0,t-2)$ for every $t>0$. The same formulas hold after taking the infimum over unit vectors, and every equivalent norm fails asymptotic uniform convexity.

The formalization also constructs such a subspace on a countable product of unit intervals and proves that it has the stated measure-precompactness and Daugavet properties, so the modulus formulas apply to an actual example.

The paper constructs Banach spaces from bounded tree potentials and path costs to separate averaged midpoint convexity from asymptotic uniform convexity. For the specified tree-potential completions, the formalization proves completeness, separability, infinite dimension, and an averaged midpoint modulus of at least $\sqrt{1+t^2/4}-1$ for $0<t<1$. No space linearly isomorphic to one of these completions is asymptotically uniformly convex.

The formalization also covers selected path-cost duality and comparison results, clipping and energy estimates, and further renorming obstructions. These retain their stated support, head, and tail hypotheses; the remaining auxiliary assertions of the paper are outside this scope.

The paper forms a real $L_1$ space from the closed span of products of independent multipliers along tree paths. For a positive, nonconstant multiplier of mean one and finite second moment, the formalization proves that this space is infinite-dimensional and has no equivalent asymptotically uniformly convex norm.

For every $t>0$, the averaged midpoint modulus nevertheless has explicit positive lower bounds. If $G$ is a standard real Gaussian, the exponential-multiplier bound is $\frac{7t}{480}\mathbb E[(|G|-20/t)_+]$, where $u_+=\max(u,0)$. For squared-Gaussian multipliers, the bounds are $\frac18\Pr(|G|\ge4\sqrt2(2+\sqrt2)/t)$ and $\frac14\Pr(|G|\ge8\sqrt6/t)$.

The paper constructs three Banach spaces from recursive tree potentials: a root-sum space, a zero-root space, and a joined space. The formalization proves that all three are infinite-dimensional and have no equivalent asymptotically uniformly convex norm. The root-sum and joined spaces have averaged midpoint modulus at least $t^3/128$ for $0<t<1$, and the root-sum modulus is positive for every $t>0$. The zero-root estimate retains its finite ancestral support and tail hypotheses, and the zero-root and joined spaces are reflexive.

The formalization also covers a separated-midpoint result for the joined space and a variable-exponent model with its recursive norm, duality, projections, renorming obstruction, and sixth- and third-order stability estimates. The separation, sequence, support, and head assumptions in these results are essential parts of their statements.

## Lean: Reflexive tree space, midpoint modulus, and diamond distortion

```lean
theorem main_theorem :
    (¬FiniteDimensional ℝ (FullDual Vertex)) ∧
    TopologicalSpace.SeparableSpace (FullDual Vertex) ∧
    Reflexive (FullDual Vertex) ∧
    (∀ (α β : ℝ) (R : EquivalentNorm (FullDual Vertex) α β), ¬IsAUC R.N) ∧
    (∀ t : ℝ, 0 < t →
      Real.sqrt (1+t^2/12)-1 ≤ averageModulus (FullDual Vertex) norm t) ∧
    (∀ (k : ℕ) (f : (Diamond.diamond k).V → FullDual Vertex) (C : ℝ),
      Diamond.EmbeddingBound k f C → Real.sqrt (1+(k:ℝ)/12) ≤ C)
```

Stated in [ForestSpace.lean, line 453](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ForestSpace.lean#L453). Proved in [lean/OAI/Analysis/ForestSpace/Main.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/ForestSpace/Main.lean#L16). formalization.yaml lists it as one of the repository's main results.

## Lean: Midpoint-lens tail estimate

```lean
theorem midpoint_lens_main :
    (∀ (H : Finset ForestVertex) (_ : Ancestral ForestAncestor H)
      (x y : X) (_ : x = head H x) (R : ℝ) (_ : 0 ≤ R)
      (_ : ‖x + y‖ ≤ R) (_ : ‖x - y‖ ≤ R),
      ‖tail H y‖ ≤ 2 * Real.sqrt (R ^ 2 - ‖x‖ ^ 2)) ∧
    (∀ (H : Finset InfiniteVertex) (_ : Ancestral List.IsPrefix H)
      (x y : BInfinite) (_ : x.val = head H x.val) (R : ℝ) (_ : 0 ≤ R)
      (_ : ‖x + y‖ ≤ R) (_ : ‖x - y‖ ≤ R),
      ‖tail H y.val‖ ≤ 2 * Real.sqrt (R ^ 2 - ‖x‖ ^ 2))
```

Stated in [MidpointLenses.lean, line 328](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/MidpointLenses.lean#L328). Proved in [lean/OAI/Analysis/SegmentLenses/Main.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/SegmentLenses/Main.lean#L7). formalization.yaml lists it as one of the repository's main results.

## Lean: All-pairs diamond distortion bound

```lean
theorem headline_all_pairs :
    (∀ (k : ℕ) (f : Diamond.Vertex k → ForestDual) (D s : ℝ),
      0 < s → (∀ u v,s*Diamond.distance k u v ≤ ‖f u-f v‖ ∧
        ‖f u-f v‖ ≤ D*s*Diamond.distance k u v) → 1+(k:ℝ)/4 ≤ D^2) ∧
    (∀ (k : ℕ) (f : Diamond.Vertex k → InfinitePredual) (D s : ℝ),
      0 < s → (∀ u v,s*Diamond.distance k u v ≤ ‖f u-f v‖ ∧
        ‖f u-f v‖ ≤ D*s*Diamond.distance k u v) → 1+(k:ℝ)/4 ≤ D^2)
```

Stated in [DiamondDistortion.lean, line 302](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DiamondDistortion.lean#L302). Proved in [lean/OAI/Analysis/DiamondDistortion/Descent.lean, line 104](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/DiamondDistortion/Descent.lean#L104). formalization.yaml lists it as one of the repository's main results.

## Lean: Exact asymptotic moduli and a Daugavet example

```lean
theorem exact_main {Ω : Type u_1} [MeasurableSpace Ω] (μ : Measure Ω)
    [IsProbabilityMeasure μ] (E : Submodule ℝ (Lp ℝ 1 μ))
    (_hclosed : IsClosed (E : Set (Lp ℝ 1 μ))) (hdim : ¬ FiniteDimensional ℝ E)
    (hprecompact : MeasurePrecompactBall μ E) (hdaugavet : Daugavet E) :
    (∀ (x : E), ‖x‖ = 1 → ∀ t : ℝ, 0 < t →
      H (normSeminorm ℝ E) x t = max (t / 2) (t - 1) ∧
      D (normSeminorm ℝ E) x t = max 0 (t - 2)) ∧
    (∀ t : ℝ, 0 < t →
      averagedModulus (normSeminorm ℝ E) t = max (t / 2) (t - 1) ∧
      oneSidedModulus (normSeminorm ℝ E) t = max 0 (t - 2)) ∧
    (∀ N : Seminorm ℝ E, EquivalentNorm N → ¬ AUC N)
```

Stated in [DaugavetModuli.lean, line 72](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DaugavetModuli.lean#L72). Its proof is in [lean/OAI/Analysis/Daugavet/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Daugavet/Main.lean) or a file it imports further down, which this chapter does not read.

```lean
theorem kadets_werner_existence :
    ∃ E : Submodule ℝ (Lp ℝ 1 kwMeasure),
      IsClosed (E : Set (Lp ℝ 1 kwMeasure)) ∧ (¬ FiniteDimensional ℝ E) ∧
      MeasurePrecompactBall kwMeasure E ∧ UnitSliceProperty E ∧ Daugavet E
```

Stated in [DaugavetModuli.lean, line 85](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DaugavetModuli.lean#L85). Proved in [lean/OAI/Analysis/Daugavet/Main.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Daugavet/Main.lean#L11).

```lean
theorem exact_example :
    ∃ E : Submodule ℝ (Lp ℝ 1 kwMeasure),
      IsClosed (E : Set (Lp ℝ 1 kwMeasure)) ∧ (¬ FiniteDimensional ℝ E) ∧
      MeasurePrecompactBall kwMeasure E ∧ UnitSliceProperty E ∧ Daugavet E ∧
      (∀ (x : E), ‖x‖ = 1 → ∀ t : ℝ, 0 < t →
        H (normSeminorm ℝ E) x t = max (t / 2) (t - 1) ∧
        D (normSeminorm ℝ E) x t = max 0 (t - 2)) ∧
      (∀ t : ℝ, 0 < t →
        averagedModulus (normSeminorm ℝ E) t = max (t / 2) (t - 1) ∧
        oneSidedModulus (normSeminorm ℝ E) t = max 0 (t - 2)) ∧
      (∀ N : Seminorm ℝ E, EquivalentNorm N → ¬ AUC N)
```

Stated in [DaugavetModuli.lean, line 91](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DaugavetModuli.lean#L91). Proved in [lean/OAI/Analysis/Daugavet/Main.lean, line 22](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Daugavet/Main.lean#L22). formalization.yaml lists it as one of the repository's main results.

## Lean: Tree-potential midpoint convexity and renorming obstruction

```lean
theorem TreeCalculus.main_counterexample (r : Bool) (k : QuadraticKind) :
    (CompleteSpace (TestCompletion (treeTestFamily r k)) ∧
      TopologicalSpace.SeparableSpace (TestCompletion (treeTestFamily r k)) ∧
      ¬Module.Finite ℝ (TestCompletion (treeTestFamily r k))) ∧
    (∀ t : ℝ, 0 < t → t < 1 →
      Real.sqrt (1 + t ^ 2 / 4) - 1 ≤
        averagedModulusReal (TestCompletion (treeTestFamily r k)) t) ∧
    (∀ (Y : Type u) [NormedAddCommGroup Y] [NormedSpace ℝ Y],
      (TestCompletion (treeTestFamily r k) ≃L[ℝ] Y) → ¬IsAUCReal Y)
```

Stated in [BoundedTreePotentials.lean, line 339](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BoundedTreePotentials.lean#L339). Proved in [lean/OAI/Analysis/TreePotential/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/TreePotential/Main.lean#L12). formalization.yaml lists it as one of the repository's main results.

## Lean: Independent-product spaces and positive midpoint moduli

```lean
theorem main_general (μ : Measure ℝ) (hμ : MultiplierHypotheses μ) :
    ¬ FiniteDimensional ℝ (productSpan μ) ∧
    ∀ N : Seminorm ℝ (productSpan μ),
      IsEquivalentNorm (productSpan μ) N → ¬ IsAUC (productSpan μ) N
```

Stated in [IndependentProducts.lean, line 89](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IndependentProducts.lean#L89). Proved in [lean/OAI/Analysis/ProductSpaces/WeakNullity.lean, line 203](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/ProductSpaces/WeakNullity.lean#L203). formalization.yaml lists it as one of the repository's main results.

```lean
theorem main_exponential (t : ℝ) (ht : 0 < t) :
    (7 * t / 30) * excessConstant (10 / t) ≤
      averagedMidpointModulus (productSpan exponentialLaw)
        (normSeminorm ℝ (productSpan exponentialLaw)) t ∧
    0 < (7 * t / 30) * excessConstant (10 / t)
```

Stated in [IndependentProducts.lean, line 95](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IndependentProducts.lean#L95). Proved in [lean/OAI/Analysis/ProductSpaces/Main.lean, line 54](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/ProductSpaces/Main.lean#L54). formalization.yaml lists it as one of the repository's main results.

```lean
theorem main_gaussian_24 (t : ℝ) (ht : 0 < t) :
    gaussianTail (4 * Real.sqrt 2 * (2 + Real.sqrt 2) / t) / 8 ≤
      averagedMidpointModulus (productSpan gaussianSquareLaw)
        (normSeminorm ℝ (productSpan gaussianSquareLaw)) t ∧
    0 < gaussianTail (4 * Real.sqrt 2 * (2 + Real.sqrt 2) / t) / 8
```

Stated in [IndependentProducts.lean, line 102](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IndependentProducts.lean#L102). Its proof is in [lean/OAI/Analysis/ProductSpaces/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/ProductSpaces/Main.lean) or a file it imports further down, which this chapter does not read.

```lean
theorem main_gaussian_12 (t : ℝ) (ht : 0 < t) :
    gaussianTail (8 * Real.sqrt 6 / t) / 4 ≤
      averagedMidpointModulus (productSpan gaussianSquareLaw)
        (normSeminorm ℝ (productSpan gaussianSquareLaw)) t ∧
    0 < gaussianTail (8 * Real.sqrt 6 / t) / 4
```

Stated in [IndependentProducts.lean, line 109](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IndependentProducts.lean#L109). Its proof is in [lean/OAI/Analysis/ProductSpaces/Main.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/ProductSpaces/Main.lean) or a file it imports further down, which this chapter does not read.

## Lean: Recursive-potential spaces and midpoint convexity

```lean
theorem main : MainClaim
```

Stated in [RecursivePotentials.lean, line 955](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/RecursivePotentials.lean#L955). Proved in [lean/OAI/Analysis/RecursivePotentials/Challenge.lean, line 259](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/RecursivePotentials/Challenge.lean#L259). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/331.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/331.md)
