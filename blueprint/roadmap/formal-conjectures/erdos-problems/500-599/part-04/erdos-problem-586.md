---
declaration: theorem
origin: cited
lean: Erdos586.erdos_586
statement: formalized
---

# Erdős Problem 586

> *References:*
> - [erdosproblems.com/586](https://www.erdosproblems.com/586)
> - [ErGr80] Erdős, P. and Graham, R., _Old and new problems and results in combinatorial number
>   theory_. Monographies de L'Enseignement Mathematique (1980).
> - [Er96b] Erdős, Paul, _Some problems I presented or planned to present in my short talk_.
>   Analytic number theory, Vol. 1 (Allerton Park, IL, 1995) (1996), 333-335.
> - [Er97] Erdős, Paul, _Problems in number theory_. New Zealand J. Math. (1997), 155-160.
> - [Er97c] Erdős, Paul, _Some of my favorite problems and results_. The mathematics of Paul
>   Erdős, I (1997), 47-67.
> - [Er97e] Erdős, Paul, _Some of my favourite unsolved problems_. Math. Japon. (1997), 527-537.
> - [BBMST22] Balister, Paul and Bollobás, Béla and Morris, Robert and Sahasrabudhe, Julian and
>   Tiba, Marius, _On the Erdős covering problem: the density of the uncovered set_. Invent. Math.
>   (2022), 377-414.

*Quoted from [FormalConjectures/ErdosProblems/586.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/586.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/586](https://www.erdosproblems.com/586).

The file states 1 research or textbook statement: 1 solved.

## `Erdos586.erdos_586`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos586.lean#L186](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos586.lean#L186).

> Is there a covering system such that no two of the moduli divide each other?
>
> Asked by Schinzel, motivated by a question of Erdős and Selfridge (see
> [7](https://www.erdosproblems.com/7)). The answer is no, as proved by Balister, Bollobás,
> Morris, Sahasrabudhe, and Tiba [BBMST22].
>
> The moduli of a `CoveringSystem ℤ` are the ideals $(m_i)$; the modulus $m_i$ divides $m_j$
> exactly when $(m_j)\subseteq (m_i)$.

```lean
theorem erdos_586 :
    ¬ ∃ c : CoveringSystem ℤ, Pairwise fun i j ↦ ¬ c.moduli j ≤ c.moduli i
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/586.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/586.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/586.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/586.lean)
- [erdosproblems.com/586](https://www.erdosproblems.com/586)
