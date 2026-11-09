---
declaration: theorem
origin: cited
lean: Erdos966.erdos_966
statement: formalized
---

# Erdős Problem 966

> *References:*
> - [erdosproblems.com/966](https://www.erdosproblems.com/966)
> - [Er75b] Erdős, Paul, *Problems and results in combinatorial number theory*. Journées
>   Arithmétiques de Bordeaux (Conf., Univ. Bordeaux, Bordeaux, 1974) (1975), 295-310.

*Quoted from [FormalConjectures/ErdosProblems/966.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/966.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/966](https://www.erdosproblems.com/966).

The file states 1 research or textbook statement: 1 solved.

## `Erdos966.erdos_966`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos966.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos966.lean).

> Let $k,r\geq 2$. Does there exist a set $A\subseteq \mathbb{N}$ that contains no non-trivial
> arithmetic progression of length $k+1$, yet in any $r$-colouring of $A$ there must exist a
> monochromatic non-trivial arithmetic progression of length $k$?
>
> Erdős [Er75b] reported that 'Spencer has recently shown that such a sequence exists', but gives
> no reference.

```lean
theorem erdos_966 :
    ∀ k r : ℕ, 2 ≤ k → 2 ≤ r → ∃ A : Set ℕ, A.IsAPOfLengthFree (k + 1) ∧
      ∀ coloring : A → Fin r, ContainsMonoAPofLength coloring k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/966.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/966.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/966.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/966.lean)
- [erdosproblems.com/966](https://www.erdosproblems.com/966)
