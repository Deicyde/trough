---
declaration: theorem
origin: cited
lean: Erdos45.erdos_45
statement: formalized
---

# Erdős Problem 45

> *References:*
> - [erdosproblems.com/45](https://www.erdosproblems.com/45)
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and geometry*.
>   Resenhas (1995), 165-186.
> - [Er96b] Erdős, Paul, *Some problems I presented or planned to present in my short talk*. Analytic
>   number theory, Vol. 1 (Allerton Park, IL, 1995) (1996), 333-335.
> - [Cr03] Croot, III, Ernest S., *On a coloring conjecture about unit fractions*. Ann. of Math. (2)
>   (2003), 545-556.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.

*Quoted from [FormalConjectures/ErdosProblems/45.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/45.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/45](https://www.erdosproblems.com/45).

The file states 1 research or textbook statement: 1 solved.

## `Erdos45.erdos_45`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos45.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos45.lean).

> Let $k\geq 2$. Is there an integer $n_k$ such that, if $D=\{ 1\lt d\lt n_k : d\mid n_k\}$, then for any
> $k$-colouring of $D$ there is a monochromatic subset $D'\subseteq D$ such that
> $\sum_{d\in D'}\frac{1}{d}=1$?
>
> This follows from the colouring result of Croot [Cr03]. Croot's result allows for
> $n_k \leq e^{C^k}$ for some constant $C>1$ (simply taking $n_k$ to be the lowest common multiple of
> some interval $[1,C^k]$). Sawhney has observed that there is also a doubly exponential lower bound,
> and hence this bound is essentially sharp.

```lean
theorem erdos_45 :
    ∀ k : ℕ, 2 ≤ k → ∃ n : ℕ, ∀ colouring : ℕ → Fin k,
      ∃ colour : Fin k, ∃ D' ⊆ {d ∈ n.divisors | 1 < d ∧ d < n},
        (∀ d ∈ D', colouring d = colour) ∧ D'.reciprocalSum = 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/45.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/45.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/45.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/45.lean)
- [erdosproblems.com/45](https://www.erdosproblems.com/45)
