---
declaration: theorem
origin: cited
lean: Erdos847.erdos_847
statement: formalized
---

# Erdős Problem 847

> *References:*
> - [erdosproblems.com/847](https://www.erdosproblems.com/847)
> - [RRS24] Reiher, Christian and R\"odl, Vojt\v ech and Sales, Marcelo, Colouring versus density in integers and {H}ales-{J}ewett cubes. J. Lond. Math. Soc. (2) (2024)
>   [arXiv:2311.08556](https://arxiv.org/abs/2311.08556)

*Quoted from [FormalConjectures/ErdosProblems/847.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/847.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/847](https://www.erdosproblems.com/847).

The file states 1 research or textbook statement: 1 solved.

## `Erdos847.erdos_847`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos847.lean#L113](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos847.lean#L113).

> Let $A \subset \mathbb{N}$ be an infinite set for which there exists some $\epsilon > 0$ such that
> in any subset of $A$ of size $n$ there is a subset of size at least $\epsilon n$ which contains no
> three-term arithmetic progression.
>
> Is it true that $A$ is the union of a finite number of sets which contain no three-term arithmetic
> progression?
>
> A negative answer was given by Reiher, Rödl, and Sales [RRS24], who proved that, for any
> $0\lt \mu<1/2$, there exists $A\subseteq \mathbb{N}$ such that every finite colouring of $A$ contains
> a three-term arithmetic progression, and yet every subset of $A$ of size $n$ contains a subset of
> size $\geq \mu n$ without a three-term arithmetic progression.

```lean
theorem erdos_847 : ¬ ∀ (A : Set ℕ), Infinite A → HasFew3APs A →
    ∃ n, ∃ (S : Fin n → Set ℕ), (∀ i, ThreeAPFree (S i)) ∧ A = ⋃ i : Fin n, S i
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/847.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/847.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/847.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/847.lean)
- [erdosproblems.com/847](https://www.erdosproblems.com/847)
