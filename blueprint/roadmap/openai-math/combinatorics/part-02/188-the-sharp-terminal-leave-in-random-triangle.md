---
declaration: section
origin: cited
lean: OAI.SharpTerminalLeave.sharp_terminal_leave
statement: formalized
proof: formalized
---

# 188. The sharp terminal leave in random triangle removal

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Starting from the complete graph on *n* vertices, repeatedly delete a uniformly chosen remaining triangle. The terminal edge count is asymptotic to $n^{3/2}/(2\sqrt2)$, with mean-square convergence after normalization by $n^{3/2}$. This proves the triangle case of the Joos–Kühn sharp-constant conjecture.

## The sharp terminal leave in random triangle removal

Starting from the complete graph on *n* vertices, repeatedly remove the three edges of a uniformly chosen remaining triangle. We prove that the number of edges left at termination, divided by $n^{3/2}$, converges in $L^{2}$ to $1/(2\sqrt2)$. This proves the triangle case of the sharp-constant conjecture of Joos and Kühn. In particular, the same limit holds in probability and for the normalized expectation.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026/The-Sharp-Terminal-Leave-in-Random-Triangle-Removal-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

Start with the complete graph on $n$ vertices and repeatedly delete the three edges of a uniformly chosen remaining triangle. The formalization proves that the number of edges at termination, divided by $n^{3/2}$, converges in $L^2$ to $1/(2\sqrt2)$. It also states convergence in probability and convergence of the normalized expectation to the same constant. This is the triangle case of the sharp terminal-leave conjecture of Joos and Kühn.

## Lean: Sharp terminal edge count in random triangle removal

```lean
theorem sharp_terminal_leave :
    Tendsto (fun n => expectation n (fun G =>
      (normalizedLeave n G - sharpConstant) ^ 2)) atTop (𝓝 0) ∧
    (∀ ε : ℝ, 0 < ε →
      Tendsto (fun n => probability n (fun G =>
        ε < |normalizedLeave n G - sharpConstant|)) atTop (𝓝 0)) ∧
    Tendsto (fun n => expectation n (fun G => (G.card : ℝ)) / normalization n)
      atTop (𝓝 sharpConstant)
```

Stated in [TriangleRemoval.lean, line 55](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/TriangleRemoval.lean#L55). Proved in [lean/OAI/Combinatorics/TriangleRemoval/Main.lean, line 79](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/TriangleRemoval/Main.lean#L79).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/188.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/188.md)
