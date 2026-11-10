---
declaration: theorem
origin: cited
lean: Erdos29.erdos_29
statement: formalized
---

# Erdős Problem 29

> *References:*
> - [erdosproblems.com/29](https://www.erdosproblems.com/29)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Er89d] Erdős, P., *Some old and new problems on additive and combinatorial number theory*.
>   Combinatorial Mathematics: Proceedings of the Third International Conference (New York, 1985)
>   (1989), 181-186.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős,
>   I (1997), 47-67.
> - [JPSZ24] Jain, V. and Pham, H. T. and Sawhney, M. and Zakharov, D., *An explicit economical
>   additive basis*. arXiv:2405.08650 (2024).

*Quoted from [FormalConjectures/ErdosProblems/29.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/29.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/29](https://www.erdosproblems.com/29).

The file states 1 research or textbook statement: 1 solved.

## `Erdos29.erdos_29`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos29.lean#L104](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos29.lean#L104).

> Is there an explicit construction of a set $A\subseteq \mathbb{N}$ such that $A+A=\mathbb{N}$ but
> $1_A\ast 1_A(n)=o(n^\epsilon)$ for every $\epsilon>0$?
>
> The existence of such a set was asked by Sidon to Erdős in 1932. Erdős (eventually) proved the
> existence of such a set using probabilistic methods. This problem asks for a constructive
> solution. An explicit construction was given by Jain, Pham, Sawhney, and Zakharov [JPSZ24].
>
> The formal statement records the existence of such a set; the linked formal proof exhibits an
> explicit construction.

```lean
theorem erdos_29 : ∃ A : Set ℕ, A + A = Set.univ ∧ ∀ ε : ℝ, 0 < ε →
    (fun n : ℕ => (sumRep A n : ℝ)) =o[atTop] fun n : ℕ => (n : ℝ) ^ ε
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/29.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/29.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/29.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/29.lean)
- [erdosproblems.com/29](https://www.erdosproblems.com/29)
