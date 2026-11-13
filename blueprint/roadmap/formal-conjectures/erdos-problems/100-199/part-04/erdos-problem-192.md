---
declaration: theorem
origin: cited
lean: Erdos192.erdos_192
statement: formalized
---

# Erdős Problem 192

> *References:*
> - [erdosproblems.com/192](https://www.erdosproblems.com/192)
> - [ErGr79] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory: van der Waerden's theorem and related topics*. Enseign. Math. (1979), 325-344.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Ke92] Keränen, Veikko, *Abelian squares are avoidable on $4$ letters*. Automata, languages and
>   programming (Vienna, 1992) (1992), 41-52.
> - [FiPu23] Fici, Gabriele and Puzynina, Svetlana, *Abelian combinatorics on words: a survey*.
>   Comput. Sci. Rev. (2023), Paper No. 100532, 21.

*Quoted from [FormalConjectures/ErdosProblems/192.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/192.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/192](https://www.erdosproblems.com/192).

The file states 1 research or textbook statement: 1 solved.

## `Erdos192.erdos_192`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos192.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos192.lean#L39).

> Let $A=\{a_1,a_2,\ldots\}\subset \mathbb{R}^d$ be an infinite sequence such that $a_{i+1}-a_i$
> is a positive unit vector (i.e. is of the form $(0,0,\ldots,1,0,\ldots,0)$). For which $d$ must
> $A$ contain a three-term arithmetic progression?
>
> This is true for $d\leq 3$ and false for $d\geq 4$.
>
> This problem is equivalent to one on 'abelian squares' (see
> [231](https://www.erdosproblems.com/231)). In particular $A$ can be interpreted as an infinite
> string over an alphabet with $d$ letters (each letter describining which of the $d$ possible
> steps is taken at each point). An abelian square in a string $s$ is a pair of consecutive blocks
> $x$ and $y$ appearing in $s$ such that $y$ is a permutation of $x$. The connection comes from the
> observation that $p,q,r\in A\subset \mathbb{R}^d$ form a three-term arithmetic progression if and
> only if the string corresponding to the steps from $p$ to $q$ is a permutation of the string
> corresponding to the steps from $q$ to $r$.
>
> This problem is therefore equivalent to asking for which $d$ there exists an infinite string over
> $\{1,\ldots,d\}$ with no abelian squares. An infinite string without abelian squares was
> constructed when $d=4$ by Keränen [Ke92]. We refer to a recent survey by Fici and Puzynina
> [FiPu23] for more background and related results.

```lean
theorem erdos_192 : {d : ℕ | ∀ a : ℕ → Fin d → ℝ, IsPositiveUnitWalk a →
    ∃ x ∈ Set.range a, ∃ y ∈ Set.range a, ∃ z ∈ Set.range a, x ≠ y ∧ ∀ j, x j + z j = 2 * y j} =
      erdos_192.answer
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/192.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/192.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/192.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/192.lean)
- [erdosproblems.com/192](https://www.erdosproblems.com/192)
