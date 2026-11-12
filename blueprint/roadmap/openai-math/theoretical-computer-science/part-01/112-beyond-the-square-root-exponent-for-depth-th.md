---
declaration: section
origin: cited
lean: OAI.DepthThreeLowerBound.exists_polynomial_time_language_depth_three_lower_bound
statement: formalized
proof: formalized
---

# 112. Beyond the square-root exponent for depth-three circuits

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a single language in deterministic polynomial time whose *n*-bit membership function requires $2^{\omega(\sqrt n)}$ total gates in unbounded-fan-in OR–AND–OR circuits, at every sufficiently large input length. This crosses the square-root-exponent threshold for explicit depth-three Boolean circuit lower bounds.

## Beyond the Square-Root Exponent for Depth-Three Boolean Circuits

We construct a language in deterministic polynomial time whose *n*-bit membership function requires $2^{\omega(\sqrt n)}$ gates in an unbounded-fan-in OR–AND–OR circuit. The bound holds at every sufficiently large input length and counts all gates, including the bottom layer.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Beyond-the-Square-Root-Exponent-for-Depth-Three-Boolean-Circuits-September-23-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives one polynomial-time Boolean language whose exact depth-three OR–AND–OR circuit size eventually exceeds $2^{A\sqrt n}$ for every fixed $A>0$. The language and its polynomial-time algorithm are fixed before $A$ is chosen, while circuits may vary with the input length. Gates have unrestricted finite fan-in and sharing, with free input negations and constants. The result does not assert a fixed exponent $n^{1/2+\varepsilon}$ or a lower bound for unrestricted depth.

## Lean: Depth-three circuit lower bound beyond every square-root constant

Stated in [DepthThree.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DepthThree.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem exists_polynomial_time_language_depth_three_lower_bound :
    ∃ (L : List Bool → Bool) (M : FiniteMultiTapeMachine) (C a : ℕ),
      0 < C ∧ 0 < a ∧
      (∀ w : List Bool, MultiTapeHaltsIn M w (L w) (C * (w.length + 1) ^ a)) ∧
      ∀ A : ℝ, 0 < A → ∃ N : ℕ, ∀ n : ℕ, N ≤ n →
        ∀ D : Circuit3 (Fin n), D.Computes (fun x => L (List.ofFn x)) →
          (2 : ℝ) ^ (A * Real.sqrt (n : ℝ)) < (D.gateCount : ℝ)
```

Proved in [lean/OAI/Computability/DepthThree/Main.lean, line 8](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Computability/DepthThree/Main.lean#L8).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/112.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/112.md)
