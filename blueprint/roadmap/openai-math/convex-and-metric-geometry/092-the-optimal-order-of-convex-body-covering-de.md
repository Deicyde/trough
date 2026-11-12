---
declaration: section
origin: cited
lean: OAI.SingleLatticeCovering.single_lattice_covering, OAI.CoveringOrder.optimal_order
statement: formalized
proof: formalized
---

# 092. The optimal order of convex-body covering density

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Determines the optimal worst-case covering density as $\Theta(n\log n)$, for both lattice and unrestricted translative coverings. Every convex body in ℝ$^{n}$, *n* ≥ 2, admits a lattice covering of density at most $Cn\log n$; centrally symmetric examples in every sufficiently large dimension require at least $cn\log n$ even without the lattice restriction, for absolute $c,C\gt 0$.

## A single-lattice covering bound of order n log n

Every convex body in ℝ$^{n}$, *n* ≥ 2, admits a covering by translates along one full-rank lattice with density at most $Cn\log n$, for an absolute constant *C*. No symmetry or boundary regularity is assumed.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-single-lattice-covering-bound-of-order-n-log-n-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Translative covering densities of order n log n

For every sufficiently large dimension *n*, we construct a centrally symmetric convex body whose translative covering density exceeds $c n\log n$, where *c* > 0 is absolute. This disproves the existence of a universal linear upper bound and matches the order of Rogers' upper bound.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives an absolute constant $C>0$ such that every convex body $K\subset\mathbb R^n$, $n\ge2$, admits a covering by translates along one full-rank lattice $L$ with density $|K|/\mathrm{covol}(L)\le Cn\log n$. The covering is exact, and no symmetry, boundary regularity, or volume normalization is assumed.

The formalization determines the order of the largest covering density in dimension $n$. For all sufficiently large $n$, the suprema of translative covering density and lattice covering density are each bounded above and below by absolute positive multiples of $n\log n$, both over all convex bodies and over centrally symmetric convex bodies.

## Lean: Single-lattice covering bound

Stated in [SingleLatticeCovering.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SingleLatticeCovering.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem single_lattice_covering :
    ∃ C : ℝ, 0 < C ∧ ∀ (n : ℕ), 2 ≤ n →
      ∀ (K : Set (Space n)), IsConvexBody K →
        ∃ (L : Submodule ℤ (Space n)) (_ : DiscreteTopology L),
          IsZLattice ℝ L ∧ LatticeCovers K L ∧
            (volume K).toReal / ZLattice.covolume L ≤ C * (n : ℝ) * Real.log (n : ℝ)
```

Proved in [lean/OAI/Geometry/LatticeCovering/Main.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/LatticeCovering/Main.lean#L25).

## Lean: Optimal order for translative and lattice covering-density suprema

Stated in [CoveringDensity.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoveringDensity.lean).

```lean
theorem CoveringOrder.optimal_order : CoveringOrder.OptimalOrder
```

Proved in [lean/OAI/Geometry/CoveringDensity/Main.lean, line 79](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/CoveringDensity/Main.lean#L79).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/092.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/092.md)
