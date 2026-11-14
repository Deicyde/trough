---
declaration: section
origin: cited
lean: OAI.CoarseAssembly.bounded_geometry_graph_counterexample_unconditional
statement: formalized
proof: formalized
---

# 307. Failure of rational injectivity for maximal coarse assembly

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a uniformly discrete bounded-geometry space whose maximal coarse assembly map is not rationally injective. The example is a coarse disjoint union of finite connected graphs of uniformly bounded degree, with an infinite-order kernel class. A companion gives the analogous failure for reduced coarse assembly, disproving the rational coarse Novikov conjecture.

## Failure of rational injectivity for maximal coarse assembly

We construct a uniformly discrete bounded-geometry space whose maximal coarse assembly map has an infinite-order element in its kernel. The space is a coarse disjoint union of finite connected graphs of uniformly bounded degree, so maximal coarse assembly need not be rationally injective even for such graph unions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Failure-of-rational-injectivity-for-maximal-coarse-assembly-October-5-2026/paper.pdf).

## A counterexample to the coarse Novikov conjecture

We disprove the coarse Novikov conjecture: ordinary coarse assembly need not be rationally injective for uniformly discrete spaces of bounded geometry. We construct a coarse disjoint union of finite graphs of uniformly bounded degree and an infinite-order class in its degree-one coarse K-homology whose image under ordinary coarse assembly in the K-theory of the reduced, locally compact Roe algebra vanishes.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-the-coarse-Novikov-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The coarse Novikov conjecture predicts rational injectivity of the ordinary coarse assembly map for uniformly discrete spaces of bounded geometry. The formalization constructs a counterexample from a coarse disjoint union of finite connected graphs with uniformly bounded degree. Its degree-one coarse $K$-homology contains an infinite-order class whose image under ordinary coarse assembly into the reduced locally compact Roe algebra vanishes. The class remains nonzero after tensoring with $\mathbb Q$, so rational injectivity fails.

## Lean: Failure of rational injectivity for ordinary coarse assembly

```lean
theorem bounded_geometry_graph_counterexample_unconditional :
    (∀ j, Finite (FiberVertex j) ∧
      (fiberedGraph elementaryMoves chosenHolonomyUnit j).Connected) ∧
    (∃ D : ℕ, ∀ j (x : FiberVertex j),
      Nat.card {y // (fiberedGraph elementaryMoves chosenHolonomyUnit j).Adj x y} ≤ D) ∧
    ProperSpace VertexUnion ∧ UniformFiniteBalls VertexUnion ∧
      (∀ x y : VertexUnion, x ≠ y → 1 ≤ dist x y) ∧
      ∃ α : KX1 VertexUnion,
        (∀ n : ℤ, n ≠ 0 → n • α ≠ 0) ∧ constructedCoarseAssembly α = 0 ∧
        (1 : ℚ) ⊗ₜ[ℤ] α ≠ 0 ∧
        ¬ Function.Injective constructedCoarseAssembly ∧
        ¬ Function.Injective (constructedCoarseAssembly.toIntLinearMap.lTensor ℚ)
```

Stated in [CoarseAssembly.lean, line 6629](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoarseAssembly.lean#L6629). Proved in [lean/OAI/Topology/CoarseAssembly/UnconditionalConclusion.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Topology/CoarseAssembly/UnconditionalConclusion.lean#L38).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/307.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/307.md)
