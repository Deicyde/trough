---
declaration: section
origin: cited
lean: OAI.PlanarFalconer.mainTarget_proved, OAI.Falconer.falconer_distance_conjecture
statement: formalized
proof: formalized
---

# 073. The Falconer distance conjecture

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the Falconer distance conjecture in every dimension *d* ≥ 2: every compact set $E\subset\mathbb R^d$ with Hausdorff dimension greater than $d/2$ determines a set of Euclidean distances of positive Lebesgue measure.

## The Falconer distance conjecture in all dimensions

We resolve the Falconer distance conjecture in every dimension. For every integer *d* ≥ 2, a compact subset of ℝ$^{d}$ with Hausdorff dimension greater than $d/2$ determines a set of Euclidean distances of positive Lebesgue measure.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Falconer-distance-conjecture-in-all-dimensions-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the Falconer distance conjecture in every dimension. For every integer $d\ge2$ and compact set $E\subset\mathbb R^d$ with Hausdorff dimension greater than $d/2$, the set $\{\lVert x-y\rVert:x,y\in E\}$ has positive Lebesgue measure. The linked statements include both this all-dimensional result and the earlier planar case.

## Lean: Planar Falconer distance theorem

Stated in [PlanarFalconer.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarFalconer.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem mainTarget_proved : MainTarget
```

Proved in [lean/OAI/MeasureTheory/Falconer/Main.lean, line 50](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MeasureTheory/Falconer/Main.lean#L50).

## Lean: Falconer distance theorem in every dimension

Stated in [FalconerAllDimensions.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FalconerAllDimensions.lean).

```lean
theorem falconer_distance_conjecture :
    ∀ (d : ℕ), 2 ≤ d → ∀ E : Set (EuclideanSpace ℝ (Fin d)), IsCompact E →
      (d : ℝ≥0∞) / 2 < dimH E →
        0 < volume {r : ℝ | ∃ x ∈ E, ∃ y ∈ E, dist x y = r}
```

Proved in [lean/OAI/MeasureTheory/Falconer/Campaign123PlanarFurstenbergProof.lean, line 47](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MeasureTheory/Falconer/Campaign123PlanarFurstenbergProof.lean#L47).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/073.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/073.md)
