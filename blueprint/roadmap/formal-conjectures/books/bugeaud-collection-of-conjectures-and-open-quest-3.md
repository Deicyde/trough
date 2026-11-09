---
declaration: theorem
origin: cited
lean: Bugeaud05.problem_10_5, Bugeaud05.problem_10_5_moreover
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Lacunary Sequences in Real Number Fields

> The following problems were proposed and discussed by Dubickas as Conjecture 2 in [Dub09].
>
> *References:*
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [Dub09] Dubickas, Artūras. "An approximation property of lacunary sequences."
>     Israel Journal of Mathematics 170.1 (2009): 95-111.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Bugeaud05.problem_10_5`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/bugeaud-10-5-lacunary/blob/fa5533b0229a19f2092c777cadb43ef4b0f2600b/lean/Bugeaud105/Compatibility.lean#L18-L19](https://github.com/KitaKen1/bugeaud-10-5-lacunary/blob/fa5533b0229a19f2092c777cadb43ef4b0f2600b/lean/Bugeaud105/Compatibility.lean#L18-L19).

> Problem 10.5 (first part). Let $\mathbb{K}$ be a real number field. Then, for any
> $\varepsilon > 0$, there exists a lacunary sequence $(t_n)_{n \ge 1}$ of positive numbers
> in $\mathbb{K}$ such that
>
> $$\limsup_{n \to \infty} \{\xi t_n\} \ge 1 - \varepsilon,$$
>
> for any real number $\xi$ not in $\mathbb{K}$.
>
> This follows from the stronger `problem_10_5_moreover` via
> `problem_10_5_of_moreover`. A Lean 4 formalization by Kenta Kitamura
> ([KitaKen1 on GitHub](https://github.com/KitaKen1)) is available at
> [KitaKen1/bugeaud-10-5-lacunary](https://github.com/KitaKen1/bugeaud-10-5-lacunary).

```lean
theorem problem_10_5 (K : IntermediateField ℚ ℝ) [FiniteDimensional ℚ K]
    {ε : ℝ} (hε : 0 < ε) :
    ∃ t : ℕ → K, (∀ n, 0 < (t n : ℝ)) ∧
      IsLacunaryReal (fun k => (t k : ℝ)) ∧
      ∀ ξ : ℝ, ξ ∉ K →
        (1 - ε) ≤ limsup (fun n => Int.fract (ξ * (t n : ℝ))) atTop
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean#L54).

## `Bugeaud05.problem_10_5_moreover`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/bugeaud-10-5-lacunary/blob/fa5533b0229a19f2092c777cadb43ef4b0f2600b/lean/Bugeaud105/Compatibility.lean#L14-L16](https://github.com/KitaKen1/bugeaud-10-5-lacunary/blob/fa5533b0229a19f2092c777cadb43ef4b0f2600b/lean/Bugeaud105/Compatibility.lean#L14-L16).

> Problem 10.5 ("moreover" clause). With the same hypotheses as `problem_10_5`, the
> sequence $(t_n)$ can be chosen so that, for any real $\xi$ not in $\mathbb{K}$, each
> subinterval of $[0, 1]$ of length $\varepsilon$ contains a limit point of the sequence
> $(\{\xi t_n\})_{n \ge 1}$. This is strictly stronger than `problem_10_5`: the limsup
> bound is the special case at the subinterval $[1 - \varepsilon, 1]$.
>
> A Lean 4 formalization by Kenta Kitamura
> ([KitaKen1 on GitHub](https://github.com/KitaKen1)) proves this statement using the
> explicit positive integer sequence
>
> $$t_{Jk+r} = (J+r)2^k \qquad (k \ge 0,\ 0 \le r < J).$$
>
> Here $Q$ is a positive integer chosen so that $Q > 1/\varepsilon$, and $J = 10Q!$.
> Since $\mathbb{K}$ contains $\mathbb{Q}$, every term belongs to $\mathbb{K}$.
> The proof verifies that this sequence is lacunary and has the required cluster-point
> property simultaneously for every $\xi \notin \mathbb{K}$. See
> [KitaKen1/bugeaud-10-5-lacunary](https://github.com/KitaKen1/bugeaud-10-5-lacunary).

```lean
theorem problem_10_5_moreover (K : IntermediateField ℚ ℝ) [FiniteDimensional ℚ K]
    {ε : ℝ} (hε : 0 < ε) :
    ∃ t : ℕ → K, (∀ n, 0 < (t n : ℝ)) ∧
      IsLacunaryReal (fun k => (t k : ℝ)) ∧
      ∀ ξ : ℝ, ξ ∉ K → ∀ a, a ∈ Set.Icc (0 : ℝ) (1 - ε) →
        ∃ y ∈ Set.Icc a (a + ε),
          MapClusterPt y atTop (fun n => Int.fract (ξ * (t n : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_5.lean)
