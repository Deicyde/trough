---
declaration: theorem
origin: cited
lean: Erdos341.erdos_341
statement: formalized
---

# Erdős Problem 341

> *References:*
> * [erdosproblems.com/341](https://www.erdosproblems.com/341)
> * [Ben Green's Open Problem 7](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.1)
> * [Li26] Li, Z., *Counterexamples to Erdős Problem 341* (2026),
>   https://github.com/LiAlreadyExists/Erdos-341/blob/main/paper/Erdos341.pdf

*Quoted from [FormalConjectures/ErdosProblems/341.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/341.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/341](https://www.erdosproblems.com/341).

The file states 1 research or textbook statement: 1 solved.

## `Erdos341.erdos_341`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos341.lean#L12](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos341.lean#L12).

> Let $A=\{a_1 < \cdots < a_k\}$ be a finite set of integers and extend it to an infinite
> sequence $\overline{A}=\{a_1 < a_2 < \cdots \}$ by defining $a_{n+1}$ for $n \geq k$ to be
> the least integer exceeding $a_n$ which is not of the form $a_i + a_j$ with $i,j \leq n$.
> Is it true that the sequence of differences $a_{m+1}-a_m$ is eventually periodic?
>
> This problem is discussed under Problem 7 on Green's open problems list.
>
> The answer is no: Li [Li26] (with GPT-5.6 Sol) showed that the greedy extension of the seed set
> $A = \{1, 2, 3, 5, 7, 13, 22, 27, 28, 32, 36, 40, 47, 48, 52, 63, 71, 77, 81, 89, 97\}$ has a
> sequence of differences that is not eventually periodic. The linked formal proof
> exhibits such a sequence `a : ℕ → ℕ` (strictly increasing, with the greedy rule holding from
> some index on, and with `n ↦ a (n + 1) - a n` not eventually periodic); casting it to `ℤ`
> gives a counterexample to the statement below.

```lean
theorem erdos_341 :
    ¬ ∀ (a : ℕ → ℤ),
      (∀ᶠ n in atTop,
        IsLeast { x | a n < x ∧ x ∉ { a i + a j | (i ≤ n) (j ≤ n) } } (a (n + 1))) →
      let d := fun i ↦ a (i + 1) - a i
      ∃ p > 0, ∀ᶠ m in atTop, d (m + p) = d m
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/341.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/341.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/341.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/341.lean)
- [erdosproblems.com/341](https://www.erdosproblems.com/341)
