---
declaration: theorem
origin: cited
lean: Erdos1205.erdos_1205, Erdos1205.erdos_1205.variants.upper_bound
statement: formalized
---

# Erdős Problem 1205

> *References:*
> - [erdosproblems.com/1205](https://www.erdosproblems.com/1205)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115. [PDF](https://www.renyi.hu/~p_erdos/1980-03.pdf)

*Quoted from [FormalConjectures/ErdosProblems/1205.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1205.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1205](https://www.erdosproblems.com/1205).

The file states 2 research or textbook statements: 2 solved. It also has 2 API statements, counted here but not shown.

## `Erdos1205.erdos_1205`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1205.lean#L1065](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1205.lean#L1065).

> Let $F(x)$ be maximal such that there exists, for all $n\leq x$, a congruence class
> $a_n\pmod{n}$ such that every $m\leq x$ satisfies at least $F(x)$ of these congruences.
>
> Estimate $F(x)$.
>
> Erdős [Er80, p. 108] describes $F(x)\to\infty$ as a simple exercise and asks how fast $F(x)$
> tends to infinity. The estimate $F(x)\sim\log x$ comes from the argument given on
> erdosproblems.com/1205 (a pigeonhole upper bound and a probabilistic lower bound), not from a
> paper.

```lean
theorem erdos_1205 : (fun x : ℕ ↦ (F x : ℝ)) ~[atTop] erdos_1205.answer
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1205.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1205.lean#L95).

## `Erdos1205.erdos_1205.variants.upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1205.lean#L235](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1205.lean#L235).

> The pigeonhole principle implies $F(x)\leq \sum_{n\leq x}\frac{1}{n}= \log x+O(1)$.
>
> We state the exact pigeonhole bound $F(x)\leq H_x+1$, where $H_x=\sum_{n\leq x}\frac{1}{n}$ is
> the $x$-th harmonic number. The $+1$ is needed, since $F(3)\geq 2>H_3$. By Mathlib's
> `harmonic_le_one_add_log` this gives $F(x)\leq\log x+2$.

```lean
theorem erdos_1205.variants.upper_bound (x : ℕ) : (F x : ℝ) ≤ (harmonic x : ℝ) + 1
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1205.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1205.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1205.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1205.lean)
- [erdosproblems.com/1205](https://www.erdosproblems.com/1205)
