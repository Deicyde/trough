---
declaration: section
origin: cited
lean: OAI.RVM.global_classical_solution
statement: formalized
proof: formalized
---

# 362. Global smoothness for relativistic Vlasov–Maxwell

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves large-data global existence and uniqueness for the three-dimensional, one-species relativistic Vlasov–Maxwell system. Smooth admissible initial data may be arbitrary provided the particle density is compactly supported and the electromagnetic fields have finite energy and bounded derivatives of every order; the solution remains smooth on every finite time interval.

## Global classical solutions of the three-dimensional relativistic Vlasov–Maxwell system

We prove global existence and uniqueness for arbitrary smooth admissible initial data in the three-dimensional, one-species relativistic Vlasov–Maxwell system. The particle density is initially compactly supported, and the electromagnetic fields have finite energy and bounded derivatives of all orders. The solution remains smooth on every finite time interval. This resolves the large-data global classical regularity problem for this model, without size or symmetry restrictions on the data.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Global-classical-solutions-of-the-three-dimensional-relativistic-Vlasov-Maxwell-system-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives global existence and uniqueness for the three-dimensional one-species relativistic Vlasov–Maxwell system. The initial particle density is nonnegative, smooth, and compactly supported; the initial fields have bounded derivatives of all orders, finite energy, and satisfy both Gauss constraints. The solution is smooth on every finite time interval, has compact particle phase support there, and is unique among classical solutions. No smallness, symmetry, or neutrality assumption is imposed.

## Lean: Global classical Vlasov–Maxwell solutions

```lean
theorem global_classical_solution (d : Datum) (hd : Admissible d) :
    ∃ s : Solution, Classical d s ∧ SmoothOnFiniteHorizons s ∧
      ∀ s' : Solution, Classical d s' → SameNonnegativeTime s s'
```

Stated in [VlasovMaxwell.lean, line 103](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/VlasovMaxwell.lean#L103). Proved in [lean/OAI/Analysis/VlasovMaxwell/Main.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/VlasovMaxwell/Main.lean#L44). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/362.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/362.md)
