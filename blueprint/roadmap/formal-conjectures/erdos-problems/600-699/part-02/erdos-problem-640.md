---
declaration: theorem
origin: cited
lean: Erdos640.erdos_640, Erdos640.erdos_640.variants.three
statement: formalized
---

# Erdős Problem 640

> *References:*
> - [erdosproblems.com/640](https://www.erdosproblems.com/640)
> - [Er97d] Erdős, Paul, *Some recent problems and results in graph theory*. Discrete Math.
>   (1997), 81–85, p.84.

*Quoted from [FormalConjectures/ErdosProblems/640.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/640.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/640](https://www.erdosproblems.com/640).

The file states 2 research or textbook statements: 1 open and 1 textbook result.

## `Erdos640.erdos_640`

Open: stated without proof.

> For every $k \geq 3$, does there exist $f(k)$ such that every finite graph of chromatic
> number at least $f(k)$ has an odd cycle whose vertices induce a graph of chromatic
> number at least $k$? The cycle may have chords in the ambient graph.

```lean
theorem erdos_640 :
    ∀ k : ℕ, 3 ≤ k → ∃ N : ℕ, ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
      (N : ℕ∞) ≤ G.chromaticNumber → HasHighChromaticOddCycle G k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/640.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/640.lean#L46).

## `Erdos640.erdos_640.variants.three`

Textbook result, stated without proof. A Lean proof is at [https://github.com/AItoBit/formal-conjectures/blob/0e6191e205ebdc112d8d5c8ec8ff9a3f7f1b0616/proofs/erdos640/Erdos640.lean](https://github.com/AItoBit/formal-conjectures/blob/0e6191e205ebdc112d8d5c8ec8ff9a3f7f1b0616/proofs/erdos640/Erdos640.lean).

> Every finite graph of chromatic number at least $3$ has an odd cycle whose vertices
> induce a graph of chromatic number at least $3$.

```lean
theorem erdos_640.variants.three (n : ℕ) (G : SimpleGraph (Fin n))
    (hG : (3 : ℕ∞) ≤ G.chromaticNumber) : HasHighChromaticOddCycle G 3
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/640.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/640.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/640.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/640.lean)
- [erdosproblems.com/640](https://www.erdosproblems.com/640)
