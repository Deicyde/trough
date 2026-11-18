---
declaration: section
origin: cited
lean: OAI.ReflexiveFixedPoints.exists_fixedPoint_of_canonicallyReflexive
statement: formalized
proof: formalized
---

# 328. Nonexpansive fixed points in reflexive Banach spaces

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves Kirk's reflexive-space fixed-point problem: every nonexpansive selfmap of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point. The result uses the original norm, without assuming uniform convexity.

## Fixed Points of Nonexpansive Maps in Reflexive Banach Spaces

Every nonexpansive selfmap of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point. This resolves the reflexive-space fixed point problem for the given norm.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Fixed-Points-of-Nonexpansive-Maps-in-Reflexive-Banach-Spaces-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The fixed-point question asks whether reflexivity suffices for nonexpansive maps on bounded convex sets. The formalized result gives an affirmative answer: every nonexpansive self-map of a nonempty closed bounded convex subset of a real reflexive Banach space has a fixed point in the original norm. Zero and nonseparable spaces are included, with no uniform convexity, normal structure, or weak-continuity assumption.

## Lean: Nonexpansive fixed points in reflexive spaces

```lean
theorem exists_fixedPoint_of_canonicallyReflexive
    {X : Type u} [NormedAddCommGroup X] [NormedSpace ℝ X] [CompleteSpace X]
    (hX : CanonicallyReflexive X) (C : Set X)
    (hne : C.Nonempty) (hclosed : IsClosed C)
    (hbounded : Bornology.IsBounded C) (hconvex : Convex ℝ C)
    (F : C → C)
    (hF : ∀ a b : C, ‖(F a : X) - (F b : X)‖ ≤ ‖(a : X) - (b : X)‖) :
    ∃ a : C, F a = a
```

Stated in [ReflexiveFixedPoints.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ReflexiveFixedPoints.lean#L21). Proved in [lean/OAI/Analysis/Nonexpansive/Main.lean, line 40](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Nonexpansive/Main.lean#L40). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/328.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/328.md)
