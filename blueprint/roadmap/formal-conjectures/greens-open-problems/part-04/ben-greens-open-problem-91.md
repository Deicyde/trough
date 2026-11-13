---
declaration: theorem
origin: cited
lean: Green91.green_91, Green91.green_91.variants.fknss, Green91.green_91.variants.all_friendly
statement: formalized
---

# Ben Green's Open Problem 91

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.91)
> - [FKNSS22] Ferber, A., Kwan, M., Narayanan, B., Sah, A. and Sawhney, M., *Friendly bisections of
>   random graphs*. Comm. Amer. Math. Soc. 2 (2022), 380--416.
>   [arXiv:2105.13337](https://arxiv.org/abs/2105.13337)
> - [MSS24] Minzer, D., Sah, A. and Sawhney, M., *On perfectly friendly bisections of random
>   graphs*. Ann. Probab. 52 (2024), 2281--2341.
>   [arXiv:2305.03543](https://arxiv.org/abs/2305.03543)

*Quoted from [FormalConjectures/GreensOpenProblems/91.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/91.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `Green91.green_91`

Solved: stated here without proof.

> Take a random graph $G(n, \frac{1}{2})$. Is there almost surely a bipartition of $G$ into two sets
> of $n/2$ vertices with the property that $99\%$ of vertices have more neighbours on their own side
> than on the other?
>
> We read "almost surely" as "with probability tending to $1$ as $n \to \infty$", and "$99\%$ of
> vertices" as at least $\frac{99}{100} n$ vertices. A bisection is the partition into a set `s` with
> $\lfloor n/2 \rfloor$ elements and its complement; for odd $n$ the parts have sizes differing by
> one, as in [FKNSS22]. [Gr24] writes that the question "was apparently asked by Füredi in 1988".
> The answer is yes
> [FKNSS22, Theorem 1.1], see `green_91.variants.fknss`.

```lean
theorem green_91 :
    Tendsto (fun n : ℕ ↦ prob n fun G ↦
      ∃ s : Finset (Fin n), s.card = n / 2 ∧ (99 / 100 : ℝ) * n ≤ numFriendly G s)
      atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/91.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/91.lean#L81).

## `Green91.green_91.variants.fknss`

Solved: stated here without proof.

> **Ferber, Kwan, Narayanan, Sah and Sawhney.** With high probability, $G(n, \frac{1}{2})$ admits a
> bisection in which $n - o(n)$ vertices are friendly [FKNSS22, Theorem 1.1]. A vertex is friendly
> if it has more neighbours in its own part than across, and a bisection is a partition into two
> parts whose sizes differ by at most one. This implies `green_91`.

```lean
theorem green_91.variants.fknss :
    ∃ f : ℕ → ℝ, f =o[atTop] (fun n : ℕ ↦ (n : ℝ)) ∧
      Tendsto (fun n : ℕ ↦ prob n fun G ↦
        ∃ s : Finset (Fin n), s.card = n / 2 ∧ (n : ℝ) - f n ≤ numFriendly G s)
        atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/91.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/91.lean#L94).

## `Green91.green_91.variants.all_friendly`

Solved: stated here without proof.

> Is there almost surely a bipartition of $G(n, \frac{1}{2})$ into two sets of $n/2$ vertices with
> the property that all vertices have more neighbours on their own side than on the other?
>
> [Gr24] reports that the authors of [FKNSS22] believe this may be true. Minzer, Sah and Sawhney
> [MSS24, Theorem 1.3] prove it, conditional on a numerical hypothesis [MSS24, Assumption 1.5] that
> they check by computer, partly with interval arithmetic and partly in floating point only. Under
> the same hypothesis they find the critical margin: for every $\varepsilon > 0$, with high
> probability there is a bisection in which every vertex has at least
> $(\gamma - \varepsilon)\sqrt{n}$ more neighbours in its own part than in the other, but none with
> $(\gamma + \varepsilon)\sqrt{n}$. Here $\gamma = \gamma_{\mathrm{crit}} / \sqrt{2} \approx 0.17566$,
> and $\gamma_{\mathrm{crit}}$ is defined by an optimisation problem for Gaussian tail
> probabilities [MSS24, Definition 1.2].

```lean
theorem green_91.variants.all_friendly :
    Tendsto (fun n : ℕ ↦ prob n fun G ↦
      ∃ s : Finset (Fin n), s.card = n / 2 ∧ ∀ v, 0 < friendliness G s v)
      atTop (𝓝 1)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/91.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/91.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/91.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/91.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.91)
