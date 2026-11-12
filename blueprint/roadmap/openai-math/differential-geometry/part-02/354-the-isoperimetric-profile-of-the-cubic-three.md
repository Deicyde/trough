---
declaration: section
origin: cited
lean: OAI.CubicTorus.unit_cubic_isoperimetric
statement: formalized
proof: formalized
---

# 354. The isoperimetric profile of the cubic three-torus

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Determines the isoperimetric profile of the unit cubic flat three-torus and classifies every finite-perimeter minimizer: balls, circular tubes around shortest closed geodesics, coordinate slabs, and their complements. The transition volumes are $4\pi/81$ and $1/\pi$, with exactly the adjacent two types minimizing at each transition.

## The Isoperimetric Conjecture for the Cubic Flat Three-Torus

We prove the isoperimetric conjecture for the cubic flat three-torus and classify all minimizers, including the equality cases at the transition volumes $4\pi/81$ and $1/\pi$. The minimizing regions are balls, circular tubes about shortest closed geodesics, coordinate slabs, and their complements.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Isoperimetric-Conjecture-for-the-Cubic-Flat-Three-Torus-September-24-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization determines the isoperimetric profile and all minimizers in the unit cubic flat three-torus. At every volume $0<V<1$, a minimizer exists, and the minimizers, up to null-set changes, are exactly balls, circular tubes about shortest closed geodesics, coordinate slabs, and their complements in the appropriate volume ranges.

The classification includes all equality cases at the transition volumes $4\pi/81$ and $1/\pi$, and every minimizer has the stated candidate-profile perimeter.

## Lean: Isoperimetric profile and all minimizers in the cubic flat three-torus

Stated in [CubicTorus.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CubicTorus.lean).

```lean
theorem unit_cubic_isoperimetric (V : ℝ) (hV : V ∈ Ioo 0 1) :
    (∃ E : Set Torus, IsMinimizerAt V E) ∧
    (∀ E : Set Torus, IsMinimizerAt V E →
      perimeter E = ENNReal.ofReal (candidateProfile V)) ∧
    (∀ E : Set Torus, IsMinimizerAt V E ↔ StandardRegionAt V E)
```

Proved in [lean/OAI/Geometry/CubicTorus/Main.lean, line 1103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/CubicTorus/Main.lean#L1103).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/354.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/354.md)
