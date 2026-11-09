---
declaration: theorem
origin: cited
lean: Erdos777.erdos_777.parts.i, Erdos777.erdos_777.parts.ii, Erdos777.erdos_777.parts.iii
statement: formalized
---

# Erdős Problem 777

> *References:*
> - [erdosproblems.com/777](https://www.erdosproblems.com/777)
> - [Gu83] Guy, R. K., *A miscellany of Erdős problems*. Amer. Math. Monthly (1983), 118-120.
> - [AlFr85] Alon, N. and Frankl, P., *The maximum number of disjoint pairs in a family of
>   subsets*. Graphs Combin. (1985), 13-21.
> - [ADGS15] Alon, N., Das, S., Glebov, R. and Sudakov, B., *Comparable pairs in families of
>   sets*. J. Combin. Theory Ser. B (2015), 164-185. [arXiv](https://arxiv.org/abs/1411.4196)

*Quoted from [FormalConjectures/ErdosProblems/777.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/777.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/777](https://www.erdosproblems.com/777).

The file states 3 research or textbook statements: 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos777.erdos_777.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos777.lean#L1759](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos777.lean#L1759).

> If $\mathcal{F}$ is a family of subsets of $\{1,\ldots,n\}$ then we write $G_{\mathcal{F}}$ for the
> graph on $\mathcal{F}$ where $A\sim B$ if $A$ and $B$ are comparable - that is, $A\subseteq B$ or
> vice versa.
>
> Is it true that, if $\epsilon>0$ and $n$ is sufficiently large, whenever
> $m\leq (2-\epsilon)2^{n/2}$ the graph $G_\mathcal{F}$ has $<2^{n}$ many edges?
>
> A problem of Daykin and Erdős [Gu83]; here $m=\lvert\mathcal{F}\rvert$. The answer is yes, which
> follows from Theorem 1.4 and Corollary 1.5 of Alon, Das, Glebov, and Sudakov [ADGS15].

```lean
theorem erdos_777.parts.i :
    ∀ ε : ℝ, 0 < ε → ∃ n₀ : ℕ, ∀ n : ℕ, n₀ ≤ n → ∀ 𝓕 : Finset (Finset (Fin n)),
      (𝓕.card : ℝ) ≤ (2 - ε) * (2 : ℝ) ^ ((n : ℝ) / 2) → comparableEdges 𝓕 < 2 ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/777.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/777.lean#L72).

## `Erdos777.erdos_777.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos777.lean#L353](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos777.lean#L353).

> If $\mathcal{F}$ is a family of subsets of $\{1,\ldots,n\}$ then we write $G_{\mathcal{F}}$ for the
> graph on $\mathcal{F}$ where $A\sim B$ if $A$ and $B$ are comparable - that is, $A\subseteq B$ or
> vice versa.
>
> Is it true that if $G_{\mathcal{F}}$ has $\geq cm^2$ edges then $m\ll_c 2^{n/2}$?
>
> The answer is no, by Alon and Frankl [AlFr85, Example 6.1]: for every $d\geq 1$ there are
> families with $m\gg n^d2^{n/2}$ and at least $2^{-2d-1}\binom{m}{2}$ comparable pairs. Here
> $m=\lvert\mathcal{F}\rvert$, and the question is read as: for every $c>0$ there is $C=C(c)$ such
> that $m\leq C2^{n/2}$ for all $n$ and all such families, so the answer is the negation.

```lean
theorem erdos_777.parts.ii :
    ¬ ∀ c : ℝ, 0 < c → ∃ C : ℝ, 0 < C ∧ ∀ n : ℕ, ∀ 𝓕 : Finset (Finset (Fin n)),
      c * (𝓕.card : ℝ) ^ 2 ≤ comparableEdges 𝓕 →
        (𝓕.card : ℝ) ≤ C * (2 : ℝ) ^ ((n : ℝ) / 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/777.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/777.lean#L92).

## `Erdos777.erdos_777.parts.iii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos777.lean#L945](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos777.lean#L945).

> If $\mathcal{F}$ is a family of subsets of $\{1,\ldots,n\}$ then we write $G_{\mathcal{F}}$ for the
> graph on $\mathcal{F}$ where $A\sim B$ if $A$ and $B$ are comparable - that is, $A\subseteq B$ or
> vice versa.
>
> Is it true that, for any $\epsilon>0$, there exists some $\delta>0$ such that if there are
> $>m^{2-\delta}$ edges then $m<(2+\epsilon)^{n/2}$?
>
> The answer is yes, proved by Alon and Frankl [AlFr85, Theorem 1.4, the case $k=1$]. Here
> $m=\lvert\mathcal{F}\rvert$.

```lean
theorem erdos_777.parts.iii :
    ∀ ε : ℝ, 0 < ε → ∃ δ : ℝ, 0 < δ ∧ ∀ n : ℕ, ∀ 𝓕 : Finset (Finset (Fin n)),
      (𝓕.card : ℝ) ^ (2 - δ) < comparableEdges 𝓕 →
        (𝓕.card : ℝ) < (2 + ε) ^ ((n : ℝ) / 2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/777.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/777.lean#L112).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/777.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/777.lean)
- [erdosproblems.com/777](https://www.erdosproblems.com/777)
