---
declaration: section
origin: cited
lean: OAI.WeakPinned.main, OAI.PlanarUnitDistances.main
statement: formalized
proof: formalized
---

# 167. Planar distinct distances and unit-distance bounds

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the weak pinned Erdős distance conjecture: for every fixed *ε* > 0, all but $o(n)$ points of any *n*-point planar set determine at least $n^{1-\varepsilon}$ distinct nonzero distances. A complementary theorem bounds the number of unit-distance pairs by $O(n^{4/3-\delta})$ for an absolute *δ* > 0.

## The weak pinned planar distance theorem

We prove the weak pinned Erdős distinct-distance conjecture. For every fixed *ε* > 0, all but $o(n)$ points of any *n*-point planar set determine at least $n^{1-\varepsilon}$ distinct nonzero distances.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-weak-pinned-planar-distance-theorem-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A power saving for planar unit distances

We prove a power saving for the planar unit-distance problem: for some absolute $\beta\lt 4/3$, every set of *n* points in the Euclidean plane determines $O(n^\beta)$ unordered pairs at unit distance.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result shows that large repeated distance fibers are rare in arbitrary finite planar point sets. For each fixed $s>0$, the largest possible fraction of ordered distinct pairs $(x,y)$ whose distance from the pin $x$ occurs at least $n^s$ times tends to zero as the set size $n$ grows. Consequently, for every $\varepsilon>0$, the fraction of pins determining fewer than $n^{1-\varepsilon}$ distances tends uniformly to zero. The separate unit-distance power-saving theorem is not included.

The planar unit-distance problem asks how many pairs at distance one can occur among $n$ points. The formalization proves that there are absolute constants $C>0$ and $1\le\beta<4/3$ such that every finite planar point set of size $n$ determines at most $Cn^\beta$ unordered unit-distance pairs. The same constants work for every $n$, giving a fixed power improvement over the classical exponent $4/3$.

## Lean: Weak pinned planar distance theorem

```lean
theorem main (s : ℝ) (hs : 0<s) : Tendsto (fun n : ℕ => F n s) atTop (𝓝 0)
```

Stated in [PinnedDistances.lean, line 29](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PinnedDistances.lean#L29). Proved in [lean/OAI/Geometry/PinnedDistances/Main.lean, line 29](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/PinnedDistances/Main.lean#L29). formalization.yaml lists it as one of the repository's main results.

## Lean: Power saving for planar unit distances

```lean
theorem main : ∃ C β : ℝ, 0 < C ∧ 1 ≤ β ∧ β < (4 : ℝ) / 3 ∧
    ∀ n : ℕ, (u n : ℝ) ≤ C * (n : ℝ) ^ β
```

Stated in [PlanarUnitDistances.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarUnitDistances.lean#L19). Proved in [lean/OAI/Geometry/UnitDistances/Main.lean, line 129](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/UnitDistances/Main.lean#L129).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/167.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/167.md)
