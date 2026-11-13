---
declaration: theorem
origin: cited
lean: Erdos1149.erdos_1149
statement: formalized
---

# Erdős Problem 1149

> *References:*
> - [erdosproblems.com/1149](https://www.erdosproblems.com/1149)
> - [BeRi17] Bergelson, Vitaly and Richter, Florian Karl, *On the density of coprime tuples of the
>   form $(n,\lfloor f_1(n)\rfloor,\dots,\lfloor f_k(n)\rfloor)$, where $f_1,\dots,f_k$ are
>   functions from a Hardy field*. Number Theory - Diophantine Problems, Uniform Distribution and
>   Applications, Springer (2017), 109-135. [arXiv:1611.08044](https://arxiv.org/abs/1611.08044)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference "Paul
>   Erdős and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/1149.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1149.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1149](https://www.erdosproblems.com/1149).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1149.erdos_1149`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1149.lean#L136](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1149.lean#L136).

> Let $\alpha>0$ be a real number, not an integer. The density of integers $n\geq 1$ for which
> $(n,\lfloor n^\alpha\rfloor)=1$ is $6/\pi^2$.
>
> This is true, and was proved by Bergelson and Richter [BeRi17].

```lean
theorem erdos_1149 (α : ℝ) (hα : 0 < α) (hα' : α ∉ Set.range ((↑) : ℤ → ℝ)) :
    {n : ℕ | 1 ≤ n ∧ n.Coprime ⌊(n : ℝ) ^ α⌋₊}.HasDensity (6 / Real.pi ^ 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1149.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1149.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1149.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1149.lean)
- [erdosproblems.com/1149](https://www.erdosproblems.com/1149)
