---
declaration: theorem
origin: cited
lean: Bugeaud01.problem_10_1, Bugeaud01.problem_10_2, Bugeaud01.problem_10_3, Bugeaud01.waldschmidt
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Fractional Parts of Powers

> Chapter 10 of the book collects open questions. This file formalizes Problems 10.1,
> 10.2, 10.3 and the unnumbered conjecture by Waldschmidt.
>
> *References:*
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [Har19] Hardy, Gr H. "A problem of Diophantine approximation."
>     J. Indian Math. Soc 11 (1919): 162-166.
>   - [Kok45] Koksma, J. F. "Sur la théorie métrique des approximations diophantiques."
>     Indag. Math 7 (1945): 54-70.
>   - [Mah53] Mahler, Kurt. "On the approximation of logarithms of algebraic numbers."
>     Philosophical Transactions of the Royal Society of London. Series A,
>     Mathematical and Physical Sciences 245.898 (1953): 371-398.
>   - [Wal03](http://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Cetraro.pdf)
>     Waldschmidt, Michel. "Linear independence measures for logarithms of algebraic numbers."
>     Diophantine Approximation: Lectures given at the CIME Summer School held in Cetraro, Italy,
>     June 28–July 6, 2000. Berlin, Heidelberg: Springer Berlin Heidelberg, 2003. 249-344.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 4 open. It also has 1 test statement, counted here but not shown.

## `Bugeaud01.problem_10_1`

Open: stated without proof.

> Problem 10.1. Are there a transcendental number $\alpha$ and a positive real
> number $\xi$ such that $\lVert \xi \alpha^n \rVert$ tends to~$0$ as~$n$ tends to infinity? [Har19]
> (Trivial for $|\alpha| < 1$)

```lean
theorem problem_10_1 :
    ∃ (α ξ : ℝ), 1 < |α| ∧ Transcendental ℚ α ∧ 0 < ξ ∧
      Filter.Tendsto (fun n : ℕ ↦ distToNearestInt (ξ * α ^ n)) Filter.atTop (nhds 0)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean#L52).

## `Bugeaud01.problem_10_2`

Open: stated without proof.

> Problem 10.2. To prove that $\lVert e^n \rVert$ does not tend to 0 as n tends to
> infinity.

```lean
theorem problem_10_2 :
    ¬ Filter.Tendsto (fun n : ℕ ↦ distToNearestInt (Real.exp n)) Filter.atTop (nhds 0)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean#L62).

## `Bugeaud01.problem_10_3`

Open: stated without proof.

> Problem 10.3. To prove that there exists a positive real number~$c$ such
> that $\lVert e^n \rVert > e^{−cn}$, for every~$n \ge 1$. Posed by Mahler [Mah53].

```lean
theorem problem_10_3 :
    ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 1 ≤ n → Real.exp (-c * n) < distToNearestInt (Real.exp n)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean#L71).

## `Bugeaud01.waldschmidt`

Open: stated without proof.

> Waldschmidt [Wal03] conjectured that a stronger result holds, namely
> that there exists a positive real number~$c$ such that $\lVert e^n \rVert > n^{-c}$ for
> every~$n \ge 2$. This is supported by metrical results [Kok45].
>
> Note: the bound $n^{-c}$ equals $1$ when $n = 1$ for all $c$, while the distance to the nearest
> integer is always at most $1/2$, so the conjecture must start at $n \ge 2$.

```lean
theorem waldschmidt :
    ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 2 ≤ n → (n : ℝ) ^ (-c) < distToNearestInt (Real.exp n)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/IntDistanceDistribution.lean)
- [Wal03](http://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Cetraro.pdf)
