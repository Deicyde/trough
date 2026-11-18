---
declaration: section
origin: cited
lean: OAI.FiniteFactor.main_theorem, OAI.BackwardIntertwiners.direct_algebra_corollary, OAI.ContinuousCircleWeight.main_theorem, OAI.Hyperinvariant.main_theorem, OAI.Invariant233.Results.prescribed_irrational_counterexample, OAI.Invariant233.Results.product_realization, OAI.FiniteFactor.productBrown
statement: formalized
proof: formalized
---

# 293. Invariant projections, hyperinvariant subspaces, and transitive algebras

2 manuscripts and 7 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a nonzero norm-quasinilpotent operator on every infinite-dimensional separable complex Hilbert space with no nonzero proper closed subspace invariant under every commuting operator. The construction also gives operators with no nontrivial invariant projection in the hyperfinite type II$_{1}$ factor.

## Invariant-projection counterexamples for every irrational rotation

For every irrational angle, we construct a continuous nonnegative circle weight with exactly one zero and logarithmic integral $-\infty$ whose weighted rotation has no nontrivial invariant projection in the associated hyperfinite type II$_{1}$ factor. This answers negatively the question of Zhu, Fang, and Shi, with the angle prescribed in advance. The resulting operator is nonzero and norm-quasinilpotent.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf); the Lean below formalizes results from it.

## Backward intertwiners and a transitive commutant

We give a negative answer to the hyperinvariant-subspace problem by constructing, on every infinite-dimensional separable complex Hilbert space, a nonzero bounded norm-quasinilpotent operator with no nonzero proper closed hyperinvariant subspace. Its commutant is a proper strongly closed unital transitive complex operator algebra.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

For every irrational rotation angle $\theta\in(0,1)$, the formalization constructs a continuous nonnegative circle weight with a single zero and logarithmic integral $-\infty$ whose weighted rotation is nonzero and quasinilpotent. In its associated hyperfinite type $\mathrm{II}_1$ factor, the operator has no nontrivial invariant projection: $(1-p)Tp=0$ forces $p=0$ or $p=1$. The linked statements also include an earlier existence construction, a product realization, and the selected product model's Brown measure $\delta_0$.

The formalization for the companion paper [Backward intertwiners and a transitive commutant](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Backward-intertwiners-and-a-transitive-commutant-September-27-2026/paper.pdf) gives, on every separable infinite-dimensional complex Hilbert space, a nonzero quasinilpotent operator whose commutant is transitive, proper, and closed in the strong operator topology. Thus no nontrivial closed subspace is invariant under every operator in the commutant.

The hyperinvariant-subspace problem asks whether every bounded operator on a complex Hilbert space has a nontrivial closed subspace invariant under every operator that commutes with it. The formalization gives a negative answer on every separable infinite-dimensional complex Hilbert space: there is a nonzero quasinilpotent operator with a transitive commutant. Its commutant is a proper unital operator algebra closed in the strong operator topology. The construction therefore has no nonzero proper closed hyperinvariant subspace.

## Lean: Finite-factor invariant-projection counterexample

```lean
theorem main_theorem : MainTarget.{0}
```

Stated in [FiniteFactor.lean, line 41](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FiniteFactor.lean#L41). Proved in [lean/OAI/Analysis/FiniteFactor/Main.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/FiniteFactor/Main.lean#L11).

## Lean: Quasinilpotent operator with transitive commutant

```lean
theorem direct_algebra_corollary (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    [CompleteSpace H] [TopologicalSpace.SeparableSpace H] (hInf : ¬FiniteDimensional ℂ H) :
    Hyperinvariant233.FullClaim (H:=H)
```

Stated in [BackwardIntertwiners.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BackwardIntertwiners.lean#L36). Proved in [lean/OAI/Analysis/BackwardIntertwiners/AlgebraCorollary.lean, line 78](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/BackwardIntertwiners/AlgebraCorollary.lean#L78). formalization.yaml lists it as one of the repository's main results.

## Lean: Continuous-weight invariant-projection counterexample

```lean
theorem main_theorem : MainStatement
```

Stated in [ContinuousCircleWeight.lean, line 50](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ContinuousCircleWeight.lean#L50). Proved in [lean/OAI/Analysis/RotationWeights/Main.lean, line 267](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/RotationWeights/Main.lean#L267).

## Lean: Quasinilpotent operator with a transitive commutant

```lean
theorem main_theorem (hInf : ¬FiniteDimensional ℂ H) : FullClaim (H := H)
```

Stated in [HyperinvariantSubspaces.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HyperinvariantSubspaces.lean#L38). Proved in [lean/OAI/Analysis/Hyperinvariant/Main.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Hyperinvariant/Main.lean#L15).

## Lean: Invariant-projection counterexamples for every irrational rotation

```lean
theorem prescribed_irrational_counterexample (θ : ℝ)
    (hθ0 : 0 < θ) (hθ1 : θ < 1) (hθ : Irrational θ) :
    ∃ f : C(Circle, ℝ), Rotation.IsContinuousCounterexample θ f
```

Stated in [IrrationalRotation.lean, line 838](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IrrationalRotation.lean#L838). Proved in [lean/OAI/Analysis/IrrationalRotation/PrescribedAngle.lean, line 17](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/IrrationalRotation/PrescribedAngle.lean#L17).

```lean
theorem product_realization :
    ∃ θ c : ℕ → ℝ, ProductModel.IsCounterexampleRealization θ c
```

Stated in [IrrationalRotation.lean, line 843](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IrrationalRotation.lean#L843). Proved in [lean/OAI/Analysis/IrrationalRotation/Main.lean, line 670](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/IrrationalRotation/Main.lean#L670).

## Lean: Brown measure of the selected product weighted shift

```lean
theorem productBrown : ProductBrownClaim
```

Stated in [ProductBrown.lean, line 752](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ProductBrown.lean#L752). Proved in [lean/OAI/Analysis/BrownMeasure/Main.lean, line 14](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/BrownMeasure/Main.lean#L14).

## Lean: Quasinilpotent operator without a hyperinvariant subspace

States the `OAI.Hyperinvariant.main_theorem` quoted above. Stated in [HyperinvariantSubspaces.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HyperinvariantSubspaces.lean#L38).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/293.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/293.md)
