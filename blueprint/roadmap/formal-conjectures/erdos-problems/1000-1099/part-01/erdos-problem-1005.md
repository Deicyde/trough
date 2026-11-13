---
declaration: theorem
origin: cited
lean: Erdos1005.erdos_1005, Erdos1005.erdos_1005.variants.constant
statement: formalized
---

# Erdős Problem 1005

> *References:*
> - [erdosproblems.com/1005](https://www.erdosproblems.com/1005)
> - [Ma42] Mayer, A. E., *A mean value theorem concerning Farey series*. Quart. J. Math. Oxford
>   Ser. (1942), 48-57.
> - [Er43] Erdős, P., *A note on Farey series*. Quart. J. Math. Oxford Ser. (1943), 82-85.
> - [vD25b] van Doorn, W., *Improved bounds for the Mayer-Erdős phenomenon on similarly ordered Farey
>   fractions*. [arXiv:2509.00121](https://arxiv.org/abs/2509.00121) (2025).

*Quoted from [FormalConjectures/ErdosProblems/1005.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1005.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1005](https://www.erdosproblems.com/1005).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1005.erdos_1005`

Solved: stated here without proof.

> Let $\frac{a_1}{b_1}, \frac{a_2}{b_2}, \ldots$ be the Farey fractions of order $n \geq 4$. Let
> $f(n)$ be the largest integer such that if $1 \leq k < l \leq k + f(n)$ then $\frac{a_k}{b_k}$ and
> $\frac{a_l}{b_l}$ are similarly ordered, in other words $(a_k - a_l)(b_k - b_l) \geq 0$. Estimate
> $f(n)$: in particular, is there a constant $c > 0$ such that $f(n) = (c + o(1)) n$ for all
> large $n$?
>
> Mayer [Ma42] proved that $f(n) \to \infty$ and Erdős [Er43] that $f(n) \gg n$. Van Doorn [vD25b]
> proved $(1/12 - o(1)) n \le f(n) \le n / 4 + O(1)$ and conjectured that $f(n) = (1/4 + o(1)) n$,
> which was proved by Cipollini and GPT-5.5; see `erdos_1005.variants.constant`.

```lean
theorem erdos_1005 :
    ∃ c : ℝ, 0 < c ∧ Tendsto (fun n : ℕ => (f n : ℝ) / n) atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1005.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1005.lean#L70).

## `Erdos1005.erdos_1005.variants.constant`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1005.lean#L44](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1005.lean#L44).

> The constant in Problem 1005 is $c = 1/4$: $f(n) = (1/4 + o(1)) n$ (Cipollini and GPT-5.5;
> formalised by Cipollini, van Doorn and Aristotle).

```lean
theorem erdos_1005.variants.constant :
    Tendsto (fun n : ℕ => (f n : ℝ) / n) atTop (𝓝 (1 / 4))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1005.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1005.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1005.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1005.lean)
- [erdosproblems.com/1005](https://www.erdosproblems.com/1005)
