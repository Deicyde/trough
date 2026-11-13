---
declaration: theorem
origin: cited
lean: Bugeaud07.problem_10_7
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Confined Powers of Non-Pisot Numbers

> *References:*
>   - [Bug12a] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [Bug12b] Bugeaud, Yann, and Nikolay Moshchevitin. "On fractional parts of powers
>     of real numbers close to 1." Mathematische Zeitschrift 271.3 (2012): 627-637.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_7.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_7.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Bugeaud07.problem_10_7`

Open: stated without proof.

> Problem 10.7. Let $\varepsilon$ be a positive real number. Are there arbitrarily
> large real numbers $\alpha$ such that $\alpha$ is not a Pisot number and all the
> fractional parts $\{\alpha^n\}$, $n \ge 1$, are lying in an interval of length
> $\varepsilon / \alpha$? [Bug12b]

```lean
theorem problem_10_7 :
    ∀ ε : ℝ, 0 < ε → ∀ M : ℝ, ∃ α : ℝ, M < α ∧ ¬ IsPisot α ∧
      ∃ c : ℝ, ∀ n : ℕ, 1 ≤ n → Int.fract (α ^ n) ∈ Set.Icc c (c + ε / α)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_7.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_7.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_7.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_7.lean)
