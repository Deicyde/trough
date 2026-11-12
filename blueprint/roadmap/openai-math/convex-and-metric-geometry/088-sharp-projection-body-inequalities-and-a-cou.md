---
declaration: section
origin: cited
lean: OAI.PettyProjection.petty_projection_volume, OAI.ProjectionCounterexample.universal_simplex_upper_bound_false, OAI.Paper092.product_counterexample
statement: formalized
proof: formalized
---

# 088. Sharp projection-body inequalities and a counterexample to simplex maximization

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Petty's projection-volume conjecture in the remaining dimensions *n* ≥ 4: ellipsoids uniquely minimize projection-body volume at fixed body volume. Also establishes the full Lutwak–Petty projection inequalities. In contrast, products of simplices exceed Brannen's proposed simplex maximum for normalized projection-body volume by an exponential factor in every sufficiently large dimension.

## Petty’s projection-volume conjecture in dimensions at least four

We prove that ellipsoids uniquely minimize the volume of the projection body among convex bodies of fixed volume in every dimension at least four. This proves Petty's projection-volume conjecture in these dimensions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Pettys-projection-volume-conjecture-in-dimensions-at-least-four-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## A product counterexample to the simplex maximum for projection-body volume

The product of two ten-dimensional simplices has larger normalized projection-body volume than a twenty-dimensional simplex. This gives a counterexample to Brannen's proposed simplex maximum.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Petty's projection-volume conjecture predicts

$\displaystyle \frac{|\Pi K|}{|K|^{n-1}}\ge \kappa_{n-1}^{n}\kappa_n^{2-n},$

with equality exactly for ellipsoids; here $\kappa_j$ is the volume of the Euclidean unit ball in dimension $j$. The formalization establishes this for every convex body $K\subset\mathbb R^n$ and every $n\ge4$.

Other inequalities in the projection-body family are not included.

Brannen's simplex-maximization conjecture predicts that a simplex maximizes normalized projection-body volume $|\Pi K|/|K|^{n-1}$ in dimension $n$. The formalized counterexample is the product of two ten-dimensional simplices. Its normalized projection volume, divided by that of a twenty-dimensional simplex, is

$\displaystyle \frac{22{,}355{,}476}{22{,}020{,}096}>1.$

Thus the proposed maximum fails in dimension $20$. The paper's exponential-factor result for every sufficiently large dimension is not included.

## Lean: Petty's projection-volume inequality

Stated in [PettyProjectionVolume.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PettyProjectionVolume.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem petty_projection_volume (n : ℕ) (hn : 4 ≤ n)
    (K : Set (Space n)) (hK : IsConvexBody K) :
    pettyConstant n ≤ projectionRatio K ∧
      (projectionRatio K = pettyConstant n ↔ IsEllipsoid K)
```

Proved in [lean/OAI/Geometry/ProjectionBodies/Main.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/ProjectionBodies/Main.lean#L11).

## Lean: Failure of the simplex upper bound in dimension 20

Stated in [ProjectionCounterexample.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ProjectionCounterexample.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem universal_simplex_upper_bound_false :
    ¬ (∀ P : Set (E 20), IsConvexBody P → ratio P ≤ ratio (simplex 20))
```

Proved in [lean/OAI/Geometry/ProjectionBody/Counterexample.lean, line 96](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/ProjectionBody/Counterexample.lean#L96).

## Lean: Explicit product-of-simplices counterexample

Stated in [ProjectionVolume.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ProjectionVolume.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem product_counterexample :
    (IsCompact productWitness ∧ Convex ℝ productWitness ∧
      (interior productWitness).Nonempty) ∧
    normalizedProjectionVolume productWitness / simplexConstant 20 =
      (121 * (Nat.choose 20 10 : ℝ)) / (21 * (2 : ℝ) ^ 20) ∧
    normalizedProjectionVolume productWitness / simplexConstant 20 =
      (22355476 : ℝ) / 22020096 ∧
    1 < normalizedProjectionVolume productWitness / simplexConstant 20 ∧
    (volume (projectionBody productWitness)).toReal >
      simplexConstant 20 * (volume productWitness).toReal ^ 19
```

Proved in [lean/OAI/Geometry/ProjectionVolume/ProductCounterexample.lean, line 31](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/ProjectionVolume/ProductCounterexample.lean#L31).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/088.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/088.md)
