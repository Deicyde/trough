---
declaration: theorem
origin: cited
lean: Erdos63.erdos_63
statement: formalized
---

# Erdős Problem 63

> *References:*
> - [erdosproblems.com/63](https://www.erdosproblems.com/63)
> - [dBEr51] de Bruijn, N. G. and Erdős, P., *A colour problem for infinite graphs and a problem
>   in the theory of relations*. Indag. Math. (1951), 369--373.
> - [ErHa66] Erdős, P. and Hajnal, A., *On chromatic number of graphs and set-systems*.
>   Acta Math. Acad. Sci. Hungar. (1966), 61-99.
> - [LiMo20] Liu, Hong and Montgomery, Richard, *A solution to Erdős and Hajnal's odd cycle problem*.
>   arXiv:2010.15802 (2020).
> - [Re24] Reiher, C., *Graphs of large girth*. arXiv:2403.13571 (2024).

*Quoted from [FormalConjectures/ErdosProblems/63.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/63.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/63](https://www.erdosproblems.com/63).

The file states 1 research or textbook statement: 1 solved.

## `Erdos63.erdos_63`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos63.lean#L46](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos63.lean#L46).

> Does every graph with infinite chromatic number contain a cycle of length $2^n$ for infinitely
> many $n$?
>
> Conjectured by Mihók and Erdős. Solved affirmatively following the work of Liu and Montgomery
> [LiMo20].
>
> The linked formal proof (Codex) states the conclusion as `{n | HasCycleLength G (2 ^ n)}.Infinite`,
> with `HasCycleLength G m` unfolding to `m ∈ G.cycleLengths`.

```lean
theorem erdos_63 :
    ∀ {V : Type*} (G : SimpleGraph V), G.chromaticNumber = ⊤ →
      ∀ N : ℕ, ∃ n ≥ N, 2 ^ n ∈ G.cycleLengths
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/63.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/63.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/63.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/63.lean)
- [erdosproblems.com/63](https://www.erdosproblems.com/63)
