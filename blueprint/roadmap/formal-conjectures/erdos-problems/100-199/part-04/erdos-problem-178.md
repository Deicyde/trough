---
declaration: theorem
origin: cited
lean: Erdos178.erdos_178
statement: formalized
---

# Erdős Problem 178

> *References:*
> - [erdosproblems.com/178](https://www.erdosproblems.com/178)
> - [ErGr79] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number theory: van der Waerden's theorem and related topics*. Enseign. Math. (1979), 325-344.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number theory*. Monographies de L'Enseignement Mathématique (1980).
> - [Be81] Beck, József, *Balancing families of integer sequences*. Combinatorica (1981), 209-216.
> - [Be17] Beck, József, *A discrepancy problem: balancing infinite dimensional vectors*. Number theory—Diophantine problems, uniform distribution and applications (2017), 61-82.

*Quoted from [FormalConjectures/ErdosProblems/178.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/178.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/178](https://www.erdosproblems.com/178).

The file states 1 research or textbook statement: 1 solved.

## `Erdos178.erdos_178`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos178.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos178.lean).

> Let $A_1,A_2,\ldots$ be an infinite collection of infinite sets of integers, say
> $A_i=\{a_{i1}\lt a_{i2}\lt \cdots\}$. Does there exist some $f:\mathbb{N}\to\{-1,1\}$ such that
> $$\max_{m, 1\leq i\leq d} \left\lvert \sum_{1\leq j\leq m} f(a_{ij})\right\rvert \ll_d 1$$
> for all $d\geq 1$?
>
> Erdős remarks 'it seems certain that the answer is affirmative'. This was solved by Beck [Be81]. Recently Beck [Be17] proved that one can replace $\ll_d 1$ with $\ll d^{4+\epsilon}$ for any $\epsilon>0$.

```lean
theorem erdos_178 :
    ∀ (a : ℕ → ℕ → ℕ) (ha : ∀ i, StrictMono (a i)),
    ∃ f : ℕ → ℤ, (∀ n, f n = 1 ∨ f n = -1) ∧
      ∀ d : ℕ, ∃ C : ℕ, ∀ m i : ℕ, i < d →
        |∑ j ∈ range m, f (a i j)| ≤ ↑C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/178.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/178.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/178.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/178.lean)
- [erdosproblems.com/178](https://www.erdosproblems.com/178)
