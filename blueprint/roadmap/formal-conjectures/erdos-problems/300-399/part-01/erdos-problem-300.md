---
declaration: theorem
origin: cited
lean: Erdos300.erdos_300, Erdos300.erdos_300.variants.erdos_graham
statement: formalized
---

# Erdős Problem 300

> *References:*
> - [erdosproblems.com/300](https://www.erdosproblems.com/300)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference "Paul
>   Erdős and his mathematics", Budapest, July 1999 (1999).
> - [Cr03] Croot, III, Ernest S., *On a coloring conjecture about unit fractions*. Ann. of Math. (2)
>   (2003), 545-556.
> - [LiSa24] Liu, Y. and Sawhney, M., *On further questions regarding unit fractions*.
>   arXiv:2404.07113 (2024).

*Quoted from [FormalConjectures/ErdosProblems/300.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/300.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/300](https://www.erdosproblems.com/300).

The file states 2 research or textbook statements: 2 solved.

## `Erdos300.erdos_300`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos300.lean#L4356](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos300.lean#L4356).

> Let $A(N)$ denote the maximal cardinality of $A\subseteq \{1,\ldots,N\}$ such that
> $\sum_{n\in S}\frac{1}{n}\neq 1$ for all $S\subseteq A$. Estimate $A(N)$.
>
> Erdős and Graham [ErGr80] believe the answer is $A(N)=(1+o(1))N$. Croot [Cr03] disproved this,
> showing the existence of some constant $c<1$ such that $A(N)\lt cN$ for all large $N$. It is
> trivial that $A(N)\geq (1-\frac{1}{e}+o(1))N$. Liu and Sawhney [LiSa24] have proved that
> $A(N)=(1-1/e+o(1))N$.

```lean
theorem erdos_300 : Tendsto (fun N : ℕ => (A N : ℝ) / N) atTop (𝓝 (1 - 1 / Real.exp 1))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/300.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/300.lean#L59).

## `Erdos300.erdos_300.variants.erdos_graham`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos300.lean#L4356](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos300.lean#L4356).

> Erdős and Graham [ErGr80] believed that $A(N)=(1+o(1))N$; this was disproved by Croot
> [Cr03].

```lean
theorem erdos_300.variants.erdos_graham :
    ¬ Tendsto (fun N : ℕ => (A N : ℝ) / N) atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/300.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/300.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/300.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/300.lean)
- [erdosproblems.com/300](https://www.erdosproblems.com/300)
