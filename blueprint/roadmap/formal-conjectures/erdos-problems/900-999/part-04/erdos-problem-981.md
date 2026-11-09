---
declaration: theorem
origin: cited
lean: Erdos981.erdos_981, Erdos981.erdos_981.variants.first_time
statement: formalized
---

# Erdős Problem 981

> *References:*
> - [erdosproblems.com/981](https://www.erdosproblems.com/981)
> - [El69] Elliott, P. D. T. A., *A conjecture of Erdős concerning character sums*.
>   Indag. Math. 31 (1969), 164–171.
> - [TaZh25] [arxiv/2512.24631](https://arxiv.org/abs/2512.24631)
>   **Average first-passage times for character sums** by *Quanyu Tang and Hao Zhang*

*Quoted from [FormalConjectures/ErdosProblems/981.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/981.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/981](https://www.erdosproblems.com/981).

The file states 2 research or textbook statements: 2 solved.

## `Erdos981.erdos_981`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos981.lean#L42](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos981.lean#L42).

> Let $\epsilon > 0$ and $f_\epsilon(p)$ be the smallest integer $m$
> such that $\sum_{n\leq N} \left(\frac{n}{p}\right)\lt \epsilon N$ for all $N\geq m$. Prove that
>
> $$\sum_{p\lt x}f_\epsilon(p)\sim c_\epsilon \frac{x}{\log x}$$
>
> for some $c_\epsilon > 0$.
>
> Proved by Elliott [El69].

```lean
theorem erdos_981 (ε : ℝ) (hε : 0 < ε) :
    ∃ c > (0 : ℝ), Tendsto (fun x ↦ (∑ p : Nat.primesBelow ⌈x⌉₊, f ε p) * log x / x) atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/981.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/981.lean#L71).

## `Erdos981.erdos_981.variants.first_time`

Solved: stated here without proof.

> Let $\epsilon > 0$ and $f_\epsilon(p)$ be the smallest integer $m$ such that $\sum_{n\leq m} \left(\frac{n}{p}\right)\lt \epsilon m$. Prove that
>
> $$\sum_{p\lt x}f_\epsilon(p)\sim c_\epsilon \frac{x}{\log x}$$
>
> for some $c_\epsilon > 0$.
>
> Proved by Tang and Zhang [TaZh25].

```lean
theorem erdos_981.variants.first_time (ε : ℝ) (hε : 0 < ε) :
    ∃ c > (0 : ℝ), Tendsto (fun x ↦ (∑ p : Nat.primesBelow ⌈x⌉₊, f' ε p) * log x / x) atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/981.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/981.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/981.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/981.lean)
- [erdosproblems.com/981](https://www.erdosproblems.com/981)
