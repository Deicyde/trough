---
declaration: theorem
origin: cited
lean: Erdos1063.erdos_1063.better_upper, Erdos1063.erdos_1063.variants.subexponential_upper_bound, Erdos1063.erdos_1063.variants.exists_exception, Erdos1063.erdos_1063.variants.small_values, Erdos1063.erdos_1063.variants.monier_upper_bound, Erdos1063.erdos_1063.variants.cambie_upper_bound, Erdos1063.erdos_1063.variants.exp_upper_bound
statement: formalized
---

# Erdős Problem 1063

> *References:*
>  * [erdosproblems.com/1063](https://www.erdosproblems.com/1063)
>  * [ErSe83] Erdos, P. and Selfridge, J. L., Problem 6447. Amer. Math. Monthly (1983), 710.
>  * [Gu04] Guy, Richard K., _Unsolved problems in number theory_. (2004), Problem B31.
>  * [Mo85] Monier, Jean-Marie, _Problems and Solutions: Solutions of Advanced Problems: 6447_.
>    Amer. Math. Monthly **92** (1985), 435-436.
>  * [Ku+26] Kung, P.-N., Song, L., Hwang, D., Yoon, J., Li, C.-L., Severini, S., Olšák, M.,
>    Lockhart, E., Le, Q. V., Gokturk, B., Luong, T., Pfister, T., & Peng, N. (2026). _LEAP:
>    Supercharging LLMs for Formal Mathematics with Agentic Frameworks_.
>    [arXiv:2606.03303](https://arxiv.org/abs/2606.03303).

*Quoted from [FormalConjectures/ErdosProblems/1063.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1063](https://www.erdosproblems.com/1063).

The file states 7 research or textbook statements: 1 open and 6 solved.

## `Erdos1063.erdos_1063.better_upper`

Open: stated without proof.

> Estimate $n_k$ by finding a better upper bound than Cambie's
> $n_k \leq k \cdot \operatorname{lcm}(1, \dotsc, k-1)$.
>
> The comparator takes its least common multiple in `ℕ` and casts the result. Writing the
> ascription as `((… ).lcm (fun n : ℕ => n) : ℝ)` instead puts it on the `Finset.lcm`
> application, so the coercion lands on `n` and the `lcm` is taken in `ℝ`, where `lcm` of
> non-zero elements is `1` and the whole comparator collapses to `k`.

```lean
theorem erdos_1063.better_upper :
    (fun k => (n k : ℝ)) =O[atTop] erdos_1063.better_upper.answer ∧
    erdos_1063.better_upper.answer =o[atTop] fun k =>
      (k : ℝ) * (((Finset.Icc 1 (k - 1)).lcm id : ℕ) : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1063.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean#L61).

## `Erdos1063.erdos_1063.variants.subexponential_upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5524](https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5524).

> An improved upper bound
> $n_k \ll \exp\left(\frac{k}{\log k}(\log \log k + \log \log \log k + \log 2)\right)$,
> which is $o\bigl(k \cdot \operatorname{lcm}(1, \dotsc, k - 1)\bigr)$, was formally proved in
> Lean 4 by the LEAP prover agent [Ku+26] (see the linked `formal_proof`).
> This is an improvement over another upper bound propsed [here](https://github.com/pw/erdos1063-upper-bound/blob/a28481f5b4bda374086533397269c5b550c759b8/README.md).

```lean
theorem erdos_1063.variants.subexponential_upper_bound :
    let upper_bound : ℕ → ℝ := fun k =>
      Real.exp ((k : ℝ) / Real.log k *
        (Real.log (Real.log k) + Real.log (Real.log (Real.log k)) + Real.log 2))
    (fun k => (n k : ℝ)) =O[atTop] upper_bound ∧
    upper_bound =o[atTop] fun k =>
      (k : ℝ) * (((Finset.Icc 1 (k - 1)).lcm id : ℕ) : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1063.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean#L78).

## `Erdos1063.erdos_1063.variants.exists_exception`

Solved: stated here; a Lean proof is at [https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5533](https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5533).

> Erdős and Selfridge noted that, for $n \ge 2k$ with $k \ge 2$, at least one of the numbers
> $n - i$ for $0 \le i < k$ fails to divide $\binom{n}{k}$ ([ErSe83]).

```lean
theorem erdos_1063.variants.exists_exception {n k : ℕ} (hk : 2 ≤ k) (h : 2 * k ≤ n) :
    ∃ i < k, ¬ (n - i) ∣ n.choose k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1063.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean#L95).

## `Erdos1063.erdos_1063.variants.small_values`

Proved here.

> The initial values satisfy $n_2 = 4$, $n_3 = 6$, $n_4 = 9$, and $n_5 = 12$ ([Gu04], Problem B31).

```lean
theorem erdos_1063.variants.small_values :
    n 2 = 4 ∧ n 3 = 6 ∧ n 4 = 9 ∧ n 5 = 12
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1063.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean#L101).

## `Erdos1063.erdos_1063.variants.monier_upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5537](https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5537).

> Monier observed that $n_k \le k!$ for $k \ge 3$ ([Mo85]), since $\binom{k!}{k}$ is divisible
> by $k! - i$ for $1 \le i < k$.
>
> The hypothesis `3 ≤ k` is necessary. At $k = 2$ the bound is false: $n_2 = 4$ and $2! = 2$.

```lean
theorem erdos_1063.variants.monier_upper_bound {k : ℕ} (hk : 3 ≤ k) :
    n k ≤ k !
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1063.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean#L146).

## `Erdos1063.erdos_1063.variants.cambie_upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5541](https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5541).

> [Cambie observed](https://www.erdosproblems.com/1063) the improved bound
> $n_k \le k \cdot \operatorname{lcm}(1, \dotsc, k - 1)$.
>
> The hypothesis `3 ≤ k` is necessary here too. At $k = 2$ the right hand side is
> $2 \cdot \operatorname{lcm}(1) = 2$, while $n_2 = 4$.
>
> The source writes the bound as $k[2, 3, \dotsc, k-1]$. That agrees with the range used here,
> because including $1$ does not change a least common multiple.

```lean
theorem erdos_1063.variants.cambie_upper_bound {k : ℕ} (hk : 3 ≤ k) :
    n k ≤ k * (Finset.Icc 1 (k - 1)).lcm id
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1063.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean#L162).

## `Erdos1063.erdos_1063.variants.exp_upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5545](https://github.com/lfsong-google/formal-conjectures/blob/ff33e501bb78a90ae4703e22e052f8bb38e10146/FormalConjectures/ErdosProblems/1063.lean#L5545).

> The least common multiple bound implies $n_k \le \exp((1 + o(1))k)$.

```lean
theorem erdos_1063.variants.exp_upper_bound :
    ∃ f : ℕ → ℝ, Tendsto f atTop (𝓝 0) ∧
      ∀ k, (n k : ℝ) ≤ exp ((1 + f k) * k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1063.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean#L171).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1063.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1063.lean)
- [erdosproblems.com/1063](https://www.erdosproblems.com/1063)
