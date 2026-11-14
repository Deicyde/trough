---
declaration: section
origin: cited
lean: OAI.BoundedHochschild.KadisonRingrose.main_result
statement: formalized
proof: formalized
---

# 295. The Kadison–Ringrose cohomology conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that every bounded Hochschild cocycle of degree at least two on a complex von Neumann algebra, with coefficients in the algebra itself, has a bounded primitive. Equivalently, all higher bounded Hochschild cohomology groups vanish, resolving the Kadison–Ringrose conjecture.

## Vanishing of higher bounded Hochschild cohomology

We prove that every bounded Hochschild cocycle of degree at least two on a complex von Neumann algebra, with values in the algebra itself, has a bounded primitive. Together with the established degree-one inner-derivation theorem, this resolves the Kadison–Ringrose cohomology conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves vanishing of bounded Hochschild cohomology in every degree at least two for a complex von Neumann algebra with coefficients in itself. Every bounded multilinear cocycle of such a degree is the Hochschild differential of a bounded multilinear cochain one degree lower. No separability or type restriction is imposed. The degree-one inner-derivation theorem is outside this selected statement.

## Lean: Bounded primitives for all Hochschild cocycles of degree at least two

```lean
theorem main_result
    {M : Type u} [CStarAlgebra M] [PartialOrder M] [StarOrderedRing M] [WStarAlgebra M]
    (n : ℕ) (f : Cochain M (n + 2))
    (hf : ∀ x : Fin (n + 3) → M, differentialValue f x = 0) :
    ∃ g : Cochain M (n + 1), ∀ x : Fin (n + 2) → M,
      differentialValue g x = f x
```

Stated in [KadisonRingrose.lean, line 30](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KadisonRingrose.lean#L30). Proved in [lean/OAI/Analysis/BoundedHochschild/MainResult.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/BoundedHochschild/MainResult.lean#L13).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/295.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/295.md)
