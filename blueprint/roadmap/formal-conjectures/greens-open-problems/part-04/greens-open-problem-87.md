---
declaration: theorem
origin: cited
lean: Green87.green_87.variants.exists_tendsto, Green87.green_87.decreasing, Green87.green_87.variants.order, Green87.green_87.asymptotic
statement: formalized
---

# Green's Open Problem 87

> References:
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.87)
> - [BW15] Britnell, John R., and Mark Wildon. "Computing derangement probabilities of the symmetric
>   group acting on k-sets." arXiv preprint arXiv:1511.04106 (2015).
> - [EFG16] Eberhard, Sean, Kevin Ford, and Ben Green. "Permutations fixing a k-set." International
>   Mathematics Research Notices 2016.21 (2016): 6713-6731. arXiv:1507.04465.
> - [GS26] Green, Ben, and Mehtaab Sawhney. "The proportion of permutations fixing a k-set."
>   arXiv preprint arXiv:2604.28116 (2026).
> - [Ve26] Veljjanoski, Daniel. "p(k) for permutations fixing a k-set: values and checks for
>   k ≤ 121." https://github.com/veljjanoski/green87-fixing-k-set (2026).

*Quoted from [FormalConjectures/GreensOpenProblems/87.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/87.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved.

## `Green87.green_87.variants.exists_tendsto`

Solved: stated here without proof.

> For every $k$, $i(n, k)$ converges as $n \to \infty$ [BW15, Section 2]; the limit is
> $p(k)$ in Green's notation. It is the probability that the random multiset with
> $\mathrm{Pois}(1/j)$ parts of size $j$ ($1 \le j \le k$, independent) has a sub-multiset
> of total size $k$.

```lean
theorem green_87.variants.exists_tendsto (k : ℕ) :
    ∃ L : ℝ, Tendsto (fun n ↦ i n k) atTop (𝓝 L)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/87.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/87.lean#L56).

## `Green87.green_87.decreasing`

Open: stated without proof.

> Let $p(k)$ be the limit, as $n \to \infty$, of the probability that a random permutation of
> $[n]$ preserves some set of size $k$. Is $p(k)$ a decreasing function of $k$?
>
> This is a conjecture of Peter Cameron (2010), see [BW15]. The statement is taken in the strict
> sense, as in [BW15]: they verified $p(k) > p(k + 1)$ for $k < 30$, and the values computed
> numerically in [Ve26] satisfy it for $k < 121$. Note $p(0) = 1$, since the empty set is always
> fixed, and $p(1) = 1 - 1/e$. The limit $p$ is quantified inside the statement; it exists and is
> unique by `green_87.variants.exists_tendsto`.

```lean
theorem green_87.decreasing :
    ∀ p : ℕ → ℝ, (∀ k, Tendsto (fun n ↦ i n k) atTop (𝓝 (p k))) → StrictAnti p
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/87.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/87.lean#L73).

## `Green87.green_87.variants.order`

Solved: stated here without proof.

> $p(k)$ is bounded above and below by constant multiples of $k^{-\delta} (\log k)^{-3/2}$.
> [EFG16, Theorem 1.1] proves this for $i(n, k)$ uniformly in $1 \le k \le n/2$ (with
> $(1 + \log k)^{-3/2}$); letting $n \to \infty$ gives the statement for $p$.

```lean
theorem green_87.variants.order :
    ∀ p : ℕ → ℝ, (∀ k, Tendsto (fun n ↦ i n k) atTop (𝓝 (p k))) →
      p =Θ[atTop] fun k : ℕ ↦ (k : ℝ) ^ (-δ) * (Real.log k) ^ (-(3 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/87.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/87.lean#L81).

## `Green87.green_87.asymptotic`

Open: stated without proof.

> Is $p(k) = (C + o(1)) k^{-\delta} (\log k)^{-3/2}$ for some absolute constant $C$?
>
> Green and Sawhney [GS26] proved $p(k) = (1 + o(1)) f(\{\log_2 k\}) k^{-\delta} (\log k)^{-3/2}$
> for an explicit smooth, positive $f$ on $\mathbb{R} / \mathbb{Z}$ with
> $\max f / \min f < 1 + 2 \cdot 10^{-7}$. The question is therefore equivalent to whether $f$ is
> constant; they conjecture that it is not, so the expected answer is no, but this has not been
> proved.

```lean
theorem green_87.asymptotic :
    ∀ p : ℕ → ℝ, (∀ k, Tendsto (fun n ↦ i n k) atTop (𝓝 (p k))) →
      ∃ C : ℝ, 0 < C ∧
        p ~[atTop] fun k : ℕ ↦ C * (k : ℝ) ^ (-δ) * (Real.log k) ^ (-(3 / 2 : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/87.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/87.lean#L94).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/87.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/87.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.87)
