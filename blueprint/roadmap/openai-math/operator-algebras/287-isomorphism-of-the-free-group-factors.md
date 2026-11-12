---
declaration: section
origin: cited
lean: OAI.FreeGroupFactorMain.Interpolation.allInterpolatedIsomorphic
statement: formalized
proof: formalized
---

# 287. Isomorphism of the free group factors

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the free group factor isomorphism problem: $L(\mathbb F_2)\cong L(\mathbb F_3)$, and hence all interpolated free group factors, including $L(\mathbb F_\infty)$, are isomorphic. Their common factor has fundamental group $\mathbb R_{\gt 0}$.

## An isomorphism of the free group factors

We solve the free group factor isomorphism problem affirmatively by proving that $L(\mathbb F_2)$ and $L(\mathbb F_3)$ are isomorphic as tracial von Neumann algebras. The classical free group factor alternative then implies that all interpolated free group factors, including $L(\mathbb F_\infty)$, are isomorphic and have fundamental group $\mathbb R_{\gt 0}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The free group factor problem asks whether the von Neumann algebras of free groups of different ranks are isomorphic. The formalization proves that interpolated free group factors with any parameters $r,s>1$, including the infinite parameter, are normally trace-preservingly isomorphic. The paper's fundamental-group conclusion is a further consequence rather than a separate selected statement here.

## Lean: Isomorphism of all interpolated free group factors

Stated in [InterpolatedFactors.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InterpolatedFactors.lean).

```lean
theorem allInterpolatedIsomorphic (r s : ℝ≥0∞) (hr : 1<r) (hs : 1<s) :
    Nonempty (NormalTracialEquiv (interpolatedTrace r) (interpolatedTrace s)
      (interpolatedTopology r) (interpolatedTopology s))
```

Proved in [lean/OAI/Analysis/InterpolatedFactors/Interpolation.lean, line 101](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/InterpolatedFactors/Interpolation.lean#L101).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/287.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/287.md)
