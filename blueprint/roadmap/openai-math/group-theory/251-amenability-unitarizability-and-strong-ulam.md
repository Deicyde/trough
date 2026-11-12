---
declaration: section
origin: cited
lean: OAI.Dixmier.current_main_theorem, OAI.Dixmier.main_theorem_all_universes
statement: formalized
proof: formalized
---

# 251. Amenability, unitarizability, and strong Ulam stability

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves Dixmier's problem for all discrete groups: amenability is equivalent to every uniformly bounded Hilbert-space representation being similar to a unitary representation. For countable discrete groups, amenability is also equivalent to strong Ulam stability: sufficiently accurate unitary approximate representations are uniformly close in operator norm to genuine representations on the same, possibly infinite-dimensional, Hilbert space.

## Unitarizability implies amenability for discrete groups

We prove that a discrete group is amenable if and only if every uniformly bounded representation on a complex Hilbert space is similar to a unitary representation. This resolves Dixmier's unitarizability problem affirmatively for discrete groups.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## Strong Ulam Stability Characterizes Amenability

A countable discrete group is amenable if and only if it is strongly Ulam stable: every sufficiently accurate unitary almost representation, on any complex Hilbert space, is uniformly close in operator norm to a genuine representation on the same space. We prove the converse to Kazhdan's amenable stability theorem, answering the question of Burger, Ozawa, and Thom. The inclusion of infinite-dimensional Hilbert spaces is essential.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/strong-ulam-stability.pdf).

## The Lean formalization

Dixmier's unitarizability problem asks whether a discrete group is amenable exactly when every uniformly bounded Hilbert-space representation is similar to a unitary one. The formalization establishes this equivalence for every discrete group.

For every nonamenable group and every $\varepsilon>0$, it also gives a nonunitarizable representation with uniform operator bound at most $1+\varepsilon$. The Hilbert space can be chosen separable for countable groups; a separate linked statement records a separable witness with uniform bound $101$ in that case.

## Lean: Unitarizability for all discrete groups

Stated in [DixmierAllDiscrete.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DixmierAllDiscrete.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem current_main_theorem : CurrentMainTheorem.{u,v}
```

Proved in [lean/OAI/Analysis/Unitarizability/AllDiscrete.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Unitarizability/AllDiscrete.lean#L12).

## Lean: Separable nonunitarizable witnesses for countable nonamenable groups

Stated in [Dixmier.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Dixmier.lean).

```lean
theorem main_theorem_all_universes : MainTheorem.{u,v}
```

Proved in [lean/OAI/Analysis/Unitarizability/UniverseTransport.lean, line 55](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Unitarizability/UniverseTransport.lean#L55).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/251.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/251.md)
