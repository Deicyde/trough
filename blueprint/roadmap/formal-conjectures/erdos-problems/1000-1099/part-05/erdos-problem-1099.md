---
declaration: theorem
origin: cited
lean: Erdos1099.erdos_1099, Erdos1099.erdos_1099.variants.factorial, Erdos1099.erdos_1099.variants.lcm, Erdos1099.erdos_1099.variants.ratio_sum
statement: formalized
---

# Erdős Problem 1099

> *References:*
> - [erdosproblems.com/1099](https://www.erdosproblems.com/1099)
> - [Er81h] Erdős, P., *Some problems and results on additive and multiplicative number theory*.
>   Analytic number theory (Philadelphia, Pa., 1980) (1981), 171-182.
> - [Vo84] Vose, Michael D., *Integers with consecutive divisors in small ratio*. J. Number Theory
>   (1984), 233-238.
> - [Te87] Tenenbaum, Gérald, *Sur un problème extrémal en arithmétique*. Ann. Inst. Fourier
>   (1987), 1-18.

*Quoted from [FormalConjectures/ErdosProblems/1099.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1099.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1099](https://www.erdosproblems.com/1099).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1099.erdos_1099`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1099.lean#L63](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1099.lean#L63).

> Let $1=d_1\lt \cdots\lt d_{\tau(n)}=n$ be the divisors of $n$, and for $\alpha>1$ let
> $$h_\alpha(n) = \sum_i \left( \frac{d_{i+1}}{d_i}-1\right)^\alpha.$$
> Is it true that
> $$\liminf_{n\to \infty}h_\alpha(n) \ll_\alpha 1?$$
>
> Erdős [Er81h] remarks that $n!$ or the least common multiple of $\{1,\ldots,n\}$ would be good
> candidates for an infinite sequence of $n$ with $h_\alpha(n)$ bounded.
>
> The $\liminf$ is trivially $\geq 1$, just considering the term $i=1$. A positive answer to the
> main question was provided by Vose [Vo84] by constructing a specific sequence. Tenenbaum [Te87]
> proved that the two explicit sequences mentioned above satisfy this property.
>
> The statement "$\liminf h_\alpha(n)$ is finite" is formalised as "$h_\alpha(n)\leq C$ for
> infinitely many $n$".

```lean
theorem erdos_1099 :
    ∀ α : ℝ, 1 < α → ∃ C : ℝ, ∃ᶠ n : ℕ in atTop, h α n ≤ C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1099.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1099.lean#L66).

## `Erdos1099.erdos_1099.variants.factorial`

Solved: stated here without proof.

> Is $h_\alpha(n!)$ bounded? Tenenbaum [Te87, Théorème 1] proved that it is, for every
> $\alpha > 1$.

```lean
theorem erdos_1099.variants.factorial : ∀ α : ℝ, 1 < α →
    ∃ C : ℝ, ∀ n : ℕ, h α n.factorial ≤ C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1099.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1099.lean#L73).

## `Erdos1099.erdos_1099.variants.lcm`

Solved: stated here without proof.

> Is $h_\alpha(\mathrm{lcm}(1,\ldots,n))$ bounded? Tenenbaum [Te87, Théorème 1] proved that it
> is, for every $\alpha > 1$.

```lean
theorem erdos_1099.variants.lcm : ∀ α : ℝ, 1 < α →
    ∃ C : ℝ, ∀ n : ℕ, h α ((Finset.Icc 1 n).lcm id) ≤ C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1099.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1099.lean#L80).

## `Erdos1099.erdos_1099.variants.ratio_sum`

Solved: stated here without proof.

> Erdős remarks that this problem occurred to him when considering $\sum_i \frac{d_{i+1}}{d_i}$.
> It is easy to see that $\sum_{i} \frac{d_{i+1}}{d_i}> \tau(n)+\log n$, and Erdős asked whether
> $$\liminf \left(\sum_{i} \frac{d_{i+1}}{d_i}-\tau(n)-\log n\right)\lt \infty,$$
> which follows from the affirmative answer to the main question.

```lean
theorem erdos_1099.variants.ratio_sum : ∃ C : ℝ, ∃ᶠ n : ℕ in atTop,
    ∑ i : Fin (n.divisors.card - 1), ((Nat.nth (· ∣ n) (i + 1) : ℝ) / Nat.nth (· ∣ n) i) -
      n.divisors.card - Real.log n ≤ C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1099.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1099.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1099.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1099.lean)
- [erdosproblems.com/1099](https://www.erdosproblems.com/1099)
