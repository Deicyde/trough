---
declaration: theorem
origin: cited
lean: Erdos554.erdos_554, Erdos554.erdos_554.variants.n_eq_two, Erdos554.erdos_554.variants.lower_bound, Erdos554.erdos_554.variants.upper_bound, Erdos554.erdos_554.variants.acjmr, Erdos554.erdos_554.variants.day_johnson, Erdos554.erdos_554.variants.jenssen_skokan
statement: formalized
---

# Erdős Problem 554

> *References:*
> - [erdosproblems.com/554](https://www.erdosproblems.com/554)
> - [Er81c] Erdős, P., *Some new problems and results in graph theory and other branches of
>   combinatorial mathematics*. Combinatorics and graph theory (Calcutta, 1980), Lecture Notes in
>   Math. 885 (1981), 9-17.
> - [BoEr73] Bondy, J. A. and Erdős, P., *Ramsey numbers for cycles in graphs*. J. Combin. Theory
>   Ser. B 14 (1973), 46-54.
> - [ErGr75] Erdős, P. and Graham, R. L., *On partition theorems for finite graphs*. Infinite and
>   finite sets (Colloq., Keszthely, 1973), Colloq. Math. Soc. János Bolyai 10 (1975), 515-527.
> - [DaJo17] Day, A. N. and Johnson, J. R., *Multicolour Ramsey numbers of odd cycles*.
>   J. Combin. Theory Ser. B 124 (2017), 56-63. [arXiv:1602.07607](https://arxiv.org/abs/1602.07607)
> - [JeSk21] Jenssen, M. and Skokan, J., *Exact Ramsey numbers of odd cycles via nonlinear
>   optimisation*. Adv. Math. 376 (2021), Paper No. 107444.
>   [arXiv:1608.05705](https://arxiv.org/abs/1608.05705)
> - [ACJMR26] Axenovich, M., Cames van Batenburg, W., Janzer, O., Michel, L. and Rundström, M.,
>   *An improved upper bound for the multicolour Ramsey number of odd cycles*. J. Combin. Theory
>   Ser. B 179 (2026), 293-298. [arXiv:2510.17981](https://arxiv.org/abs/2510.17981)
>   [doi:10.1016/j.jctb.2026.04.005](https://doi.org/10.1016/j.jctb.2026.04.005)

*Quoted from [FormalConjectures/ErdosProblems/554.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/554](https://www.erdosproblems.com/554).

The file states 7 research or textbook statements: 2 open and 5 solved. It also has 3 test statements, counted here but not shown.

## `Erdos554.erdos_554`

Open: stated without proof.

> Let $R_k(G)$ denote the minimal $m$ such that if the edges of $K_m$ are $k$-coloured then there
> is a monochromatic copy of $G$. Show that
>
> $$\lim_{k\to \infty}\frac{R_k(C_{2n+1})}{R_k(K_3)}=0$$
>
> for any $n\geq 2$.
>
> A problem of Erdős and Graham. The case $n = 1$ is excluded since $C_3 = K_3$. This problem is
> #23 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_554 (n : ℕ) (hn : 2 ≤ n) :
    Tendsto (fun k : ℕ ↦ (multicolourGraphRamsey k (cycleGraph (2 * n + 1)) : ℝ) /
      (multicolourGraphRamsey k (completeGraph (Fin 3)) : ℝ)) atTop (𝓝 0)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/554.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean#L84).

## `Erdos554.erdos_554.variants.n_eq_two`

Open: stated without proof.

> The problem is open even for $n = 2$:
>
> $$\lim_{k\to \infty}\frac{R_k(C_5)}{R_k(K_3)}=0.$$

```lean
theorem erdos_554.variants.n_eq_two :
    Tendsto (fun k : ℕ ↦ (multicolourGraphRamsey k (cycleGraph 5) : ℝ) /
      (multicolourGraphRamsey k (completeGraph (Fin 3)) : ℝ)) atTop (𝓝 0)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/554.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean#L94).

## `Erdos554.erdos_554.variants.lower_bound`

Solved: stated here without proof.

> Bondy and Erdős [BoEr73] and Erdős and Graham [ErGr75] proved the lower bound
>
> $$n2^k+1\leq R_k(C_{2n+1})$$
>
> for all $n, k \geq 1$. The condition $k \geq 1$ excludes the junk value $R_0(G) = 2$.

```lean
theorem erdos_554.variants.lower_bound :
    ∀ n : ℕ, 1 ≤ n → ∀ k : ℕ, 1 ≤ k →
      n * 2 ^ k + 1 ≤ multicolourGraphRamsey k (cycleGraph (2 * n + 1))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/554.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean#L105).

## `Erdos554.erdos_554.variants.upper_bound`

Solved: stated here without proof.

> Erdős and Graham [ErGr75] (see also [BoEr73]) proved the upper bound
>
> $$R_k(C_{2n+1})\leq 2n(k+2)!$$
>
> for all $n, k \geq 1$.

```lean
theorem erdos_554.variants.upper_bound :
    ∀ n : ℕ, 1 ≤ n → ∀ k : ℕ, 1 ≤ k →
      multicolourGraphRamsey k (cycleGraph (2 * n + 1)) ≤ 2 * n * (k + 2).factorial
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/554.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean#L116).

## `Erdos554.erdos_554.variants.acjmr`

Solved: stated here without proof.

> Axenovich, Cames van Batenburg, Janzer, Michel and Rundström [ACJMR26, Theorem 1.1] proved that
>
> $$R_k(C_{2n+1}) \leq (4n-2)^k k^{k/n}+1$$
>
> for all $n, k \geq 1$. For $n \geq 2$ this improves the upper bound in
> `Erdos554.erdos_554.variants.upper_bound`, since $k^{k/n}$ grows much more slowly than $(k+2)!$.

```lean
theorem erdos_554.variants.acjmr :
    ∀ n : ℕ, 1 ≤ n → ∀ k : ℕ, 1 ≤ k →
      (multicolourGraphRamsey k (cycleGraph (2 * n + 1)) : ℝ) ≤
        (4 * n - 2 : ℝ) ^ k * (k : ℝ) ^ ((k : ℝ) / n) + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/554.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean#L128).

## `Erdos554.erdos_554.variants.day_johnson`

Solved: stated here without proof.

> Day and Johnson [DaJo17] proved that for every $n \geq 1$ there is a constant $c_n > 0$ such that
>
> $$R_k(C_{2n+1}) > 2n(2+c_n)^{k-1}$$
>
> for all sufficiently large $k$. So the lower bound in `Erdos554.erdos_554.variants.lower_bound`
> is not sharp for fixed $n$ and large $k$.

```lean
theorem erdos_554.variants.day_johnson :
    ∀ n : ℕ, 1 ≤ n → ∃ c > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      (2 * n : ℝ) * (2 + c) ^ (k - 1) <
        (multicolourGraphRamsey k (cycleGraph (2 * n + 1)) : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/554.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean#L141).

## `Erdos554.erdos_554.variants.jenssen_skokan`

Solved: stated here without proof.

> Jenssen and Skokan [JeSk21] proved that the lower bound in
> `Erdos554.erdos_554.variants.lower_bound` is sharp for fixed $k$ and large $n$: for every
> $k \geq 2$,
>
> $$R_k(C_{2n+1}) = n2^k+1$$
>
> for all sufficiently large $n$.

```lean
theorem erdos_554.variants.jenssen_skokan :
    ∀ k : ℕ, 2 ≤ k → ∀ᶠ n : ℕ in atTop,
      multicolourGraphRamsey k (cycleGraph (2 * n + 1)) = n * 2 ^ k + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/554.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean#L155).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/554.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/554.lean)
- [erdosproblems.com/554](https://www.erdosproblems.com/554)
