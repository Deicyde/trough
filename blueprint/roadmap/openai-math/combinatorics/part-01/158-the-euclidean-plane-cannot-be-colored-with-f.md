---
declaration: section
origin: cited
lean: OAI.EuclideanFiveColor.no_proper_five_coloring, OAI.Problem160.properColoring_seven
statement: formalized
proof: formalized
---

# 158. The Euclidean plane cannot be colored with five colors

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every five-coloring of the Euclidean plane has a monochromatic pair at distance one, with no restriction on the color classes. This advances the Hadwiger–Nelson problem: together with the classical seven-coloring, only six and seven remain possible chromatic numbers of the plane.

## The Euclidean plane is not five-colorable

We prove that every coloring of the Euclidean plane with five colors has a monochromatic unit-distance pair, with no regularity assumption on the color classes. Consequently, the chromatic number of the plane is either six or seven.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Euclidean-plane-is-not-five-colorable-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Hadwiger–Nelson problem asks for the fewest colors needed to color the plane so that points at distance one have different colors. The formalized results prove that five colors do not suffice and that seven colors do suffice. The lower bound applies to arbitrary colorings, with no measurability or continuity assumption; the upper bound includes every boundary point of the coloring regions.

## Lean: No proper five-coloring

```lean
theorem no_proper_five_coloring : ¬ ∃ coloring : ℂ → Fin 5, ProperColoring 5 coloring
```

Stated in [EuclideanFiveColor.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EuclideanFiveColor.lean#L10). Proved in [lean/OAI/Geometry/PlaneColoring/Five.lean, line 124](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/PlaneColoring/Five.lean#L124). formalization.yaml lists it as one of the repository's main results.

## Lean: Proper seven-coloring

```lean
theorem properColoring_seven : ProperColoring 7
```

Stated in [PlaneColoring.lean, line 15](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlaneColoring.lean#L15). Proved in [lean/OAI/Geometry/PlaneColoring/Seven.lean, line 36](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/PlaneColoring/Seven.lean#L36). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/158.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/158.md)
