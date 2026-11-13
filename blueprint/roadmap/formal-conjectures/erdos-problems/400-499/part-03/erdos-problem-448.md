---
declaration: theorem
origin: cited
lean: Erdos448.erdos_448, Erdos448.erdos_448.variants.erdos_tenenbaum, Erdos448.erdos_448.variants.hall_tenenbaum_upper_bound, Erdos448.erdos_448.variants.hall_tenenbaum_distribution, Erdos448.erdos_448.variants.ford
statement: formalized
---

# Erdős Problem 448

> *References:*
> - [erdosproblems.com/448](https://www.erdosproblems.com/448)
> - [OEIS A397433](https://oeis.org/A397433): the integer sequence $\tau^+(n)$
>   (the constant $\alpha$ in Ford's asymptotic is [OEIS A074738](https://oeis.org/A074738)).
> - [Er79] Erdős, Paul, Some unconventional problems in number theory. Math. Mag. (1979), 67-70.
> - [Er79e] Erdős, Paul, Some unconventional problems in number theory. Astérisque (1979), 73-82.
> - [HaTe88] Hall, Richard R. and Tenenbaum, Gérald, Divisors. (1988), xvi+167.
> - [ErTe81] Erdős, P., Tenenbaum, G., *Sur la structure de la suite des diviseurs d'un entier.*
>   Ann. Inst. Fourier (Grenoble) **31** (1981), 17–37.
> - [Fo08] Ford, Kevin, *The distribution of integers with a divisor in a given interval.*
>   Ann. of Math. (2) **168** (2008), 367–433.
> - [Te13] Tenenbaum, Gérald, *Some of Erdős' unconventional problems in number theory, thirty-four
>   years later.* Erdős Centennial, Bolyai Soc. Math. Stud. **25** (2013), 651–681.

*Quoted from [FormalConjectures/ErdosProblems/448.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/448.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/448](https://www.erdosproblems.com/448).

The file states 5 research or textbook statements: 5 solved. It also has 3 test statements, counted here but not shown.

## `Erdos448.erdos_448`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos448.lean#L35](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos448.lean#L35).

> Let $\tau(n)$ count the divisors of $n$ and $\tau^+(n)$ count the number of $k$ such that $n$ has a
> divisor in $[2^k, 2^{k+1})$. Is it true that, for all $\epsilon > 0$,
>
> $$ \tau^+(n) < \epsilon \cdot \tau(n) $$
>
> for almost all $n$?
>
> This is false, and was disproved by Erdős and Tenenbaum [ErTe81], who showed that in fact the upper
> density of the set of such $n$ is $\asymp \epsilon^{1-o(1)}$ (where the $o(1)$ in the exponent
> $\to 0$ as $\epsilon \to 0$). A more precise result was proved by Hall and Tenenbaum [HaTe88]
> (see Section 4.6), who showed that the upper density is $\ll \epsilon \log(2/\epsilon)$. Hall and
> Tenenbaum further prove that $\tau^+(n)/\tau(n)$ has a distribution function. Erdős and Graham also
> asked whether there is a good inequality known for $\sum_{n \leq x} \tau^+(n)$. This was provided by
> Ford [Fo08] who proved
>
> $$ \sum_{n \leq x} \tau^+(n) \asymp x\frac{(\log x)^{1-\alpha}}{(\log\log x)^{3/2}} $$
>
> where
>
> $$ \alpha = 1-\frac{1+\log\log 2}{\log 2} = 0.08607\cdots. $$

```lean
theorem erdos_448 :
    ¬ ∀ ε : ℝ, 0 < ε →
      {n : ℕ | (tauPlus n : ℝ) < ε * (n.divisors.card : ℝ)}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/448.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/448.lean#L86).

## `Erdos448.erdos_448.variants.erdos_tenenbaum`

Solved: stated here without proof.

> Quantitative form of the (negative) answer to `erdos_448`. Erdős and Tenenbaum [ErTe81] showed that
> the upper density of $\{n : \tau^+(n) < \epsilon \cdot \tau(n)\}$ is in fact
> $\asymp \epsilon^{1 - o(1)}$, where the $o(1)$ in the exponent tends to $0$ as $\epsilon \to 0$.
> Equivalently, $\log(\text{upper density}) / \log \epsilon \to 1$ as $\epsilon \to 0^+$.

```lean
theorem erdos_448.variants.erdos_tenenbaum :
    Tendsto
      (fun ε : ℝ =>
        Real.log ({n : ℕ | (tauPlus n : ℝ) < ε * (n.divisors.card : ℝ)}.upperDensity) / Real.log ε)
      (𝓝[>] (0 : ℝ)) (𝓝 (1 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/448.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/448.lean#L97).

## `Erdos448.erdos_448.variants.hall_tenenbaum_upper_bound`

Solved: stated here without proof.

> A more precise result of Hall and Tenenbaum [HaTe88, §4.6]: the upper density of
> $\{n : \tau^+(n) < \epsilon \cdot \tau(n)\}$ is $\ll \epsilon \cdot \log(2/\epsilon)$ as
> $\epsilon \to 0^+$.

```lean
theorem erdos_448.variants.hall_tenenbaum_upper_bound :
    (fun ε : ℝ => ({n : ℕ | (tauPlus n : ℝ) < ε * (n.divisors.card : ℝ)}).upperDensity)
      =O[𝓝[>] (0 : ℝ)] (fun ε : ℝ => ε * Real.log (2 / ε))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/448.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/448.lean#L109).

## `Erdos448.erdos_448.variants.hall_tenenbaum_distribution`

Solved: stated here without proof.

> Hall and Tenenbaum [HaTe88] further prove that $\tau^+(n)/\tau(n)$ has a distribution function:
> there is a distribution function `F` (non-decreasing, with $F(-\infty) = 0$ and $F(+\infty) = 1$)
> such that, for every continuity point $z$ of `F`, the set $\{n : \tau^+(n)/\tau(n) \le z\}$ has
> density `F z`. Tenenbaum [Te13] proved that `F` is continuous at $z = 1$ and asked to determine
> its discontinuity points, if any.

```lean
theorem erdos_448.variants.hall_tenenbaum_distribution :
    ∃ F : ℝ → ℝ, Monotone F ∧ Tendsto F atBot (𝓝 0) ∧ Tendsto F atTop (𝓝 1) ∧
      ∀ z : ℝ, ContinuousAt F z →
        {n : ℕ | (tauPlus n : ℝ) / (n.divisors.card : ℝ) ≤ z}.HasDensity (F z)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/448.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/448.lean#L121).

## `Erdos448.erdos_448.variants.ford`

Solved: stated here without proof.

> Erdős and Graham asked whether there is a good inequality for $\sum_{n \le x} \tau^+(n)$. This was
> answered by Ford [Fo08], who proved
>
> $$ \sum_{n \le x} \tau^+(n) \asymp x \cdot \frac{(\log x)^{1 - \alpha}}{(\log\log x)^{3/2}}, $$
>
> where $\alpha = 1 - \frac{1 + \log\log 2}{\log 2} = 0.08607\ldots$.

```lean
theorem erdos_448.variants.ford :
    (fun x : ℕ => ∑ n ∈ Finset.Icc 1 x, (tauPlus n : ℝ))
      =Θ[atTop]
      (fun x : ℕ =>
        let α : ℝ := 1 - (1 + Real.log (Real.log 2)) / Real.log 2
        (x : ℝ) * Real.log (x : ℝ) ^ (1 - α)
          / Real.log (Real.log (x : ℝ)) ^ ((3 : ℝ) / 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/448.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/448.lean#L133).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/448.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/448.lean)
- [erdosproblems.com/448](https://www.erdosproblems.com/448)
