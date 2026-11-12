---
declaration: section
origin: cited
lean: OAI.PeriodicTilingThree.periodic_tiling_counterexample_and_minimality
statement: formalized
proof: formalized
---

# 155. A counterexample to periodic tiling in dimension three

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a finite translational tile in ℤ$^{3}$ that tiles space but admits no fully periodic tiling, disproving the periodic tiling conjecture in the smallest possible lattice dimension. Its unit-cube thickening gives the same counterexample in ℝ$^{3}$, even with arbitrary real translation vectors.

## A translational tile with no fully periodic tiling in dimension three

We construct a finite translational tile in ℤ$^{3}$ that admits tilings but no fully periodic tiling. Its unit-cube thickening has the same property in ℝ$^{3}$, even when arbitrary real translations are allowed. This gives a negative resolution of the periodic tiling conjecture in dimension three.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The periodic-tiling question asks whether a finite tile that tiles a lattice must admit a periodic tiling. The formalized counterexample is a finite tile in $\mathbb Z^3$ that tiles but has no complement invariant under a finite-index subgroup. Its unit-cube thickening also tiles $\mathbb R^3$ almost everywhere but admits no fully periodic tiling, even with arbitrary real translation vectors. The result also establishes that dimension three is the least lattice dimension where this failure occurs.

## Lean: Aperiodic translational tile in dimension three

Stated in [PeriodicTilingThree.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PeriodicTilingThree.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem periodic_tiling_counterexample_and_minimality :
    (∃ T : Finset (Lattice 3), T.Nonempty ∧
      (∃ A : Set (Lattice 3), Tiles T A) ∧
      (∀ A : Set (Lattice 3), Tiles T A → ¬ FullyPeriodic A) ∧
      (∃ A : Set (Space 3), AETiles (Thickening T) A) ∧
      (∀ A : Set (Space 3),
        AETiles (Thickening T) A → ¬ EuclideanFullyPeriodic A)) ∧
    IsLeast {d : ℕ | HasTileWithoutPeriodicComplement d} 3
```

Proved in [lean/OAI/Geometry/PeriodicTiling/Counterexample.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/PeriodicTiling/Counterexample.lean#L23).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/155.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/155.md)
