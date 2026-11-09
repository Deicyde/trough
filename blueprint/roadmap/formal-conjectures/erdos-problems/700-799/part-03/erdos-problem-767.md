---
declaration: theorem
origin: cited
lean: Erdos767.erdos_767, Erdos767.erdos_767.variants.czipszer, Erdos767.erdos_767.variants.posa
statement: formalized
---

# Erdős Problem 767

> *References:*
> - [erdosproblems.com/767](https://www.erdosproblems.com/767)
> - [Er64c] Erdős, P., _Extremal problems in graph theory_. Theory of Graphs and its Applications
>   (Proc. Sympos. Smolenice, 1963) (1964), 29-36.
> - [Er69b] Erdős, P., _Problems and results in chromatic graph theory_. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [Er75] Erdős, P., _Some recent progress on extremal problems in graph theory_. Congr. Numer.
>   (1975), 3-14.
> - [Ji04] Jiang, Tao, _A note on a conjecture about cycles with many incident chords_. J. Graph
>   Theory (2004), 180-182.

*Quoted from [FormalConjectures/ErdosProblems/767.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/767.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/767](https://www.erdosproblems.com/767).

The file states 3 research or textbook statements: 3 solved.

## `Erdos767.erdos_767`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos767.lean#L1566](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos767.lean#L1566).

> Let $g_k(n)$ be the maximal number of edges possible on a graph with $n$ vertices which does not
> contain a cycle with $k$ chords incident to a vertex on the cycle. Is it true that
> $$g_k(n)=(k+1)n-(k+1)^2$$
> for $n$ sufficiently large?
>
> The answer is yes: the conjectured equality was proved for $n\geq 3k+3$ by Jiang [Ji04].

```lean
theorem erdos_767 :
    ∀ k ≥ 1, ∀ n ≥ 3 * k + 3, g k n = (k + 1) * n - (k + 1) ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/767.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/767.lean#L64).

## `Erdos767.erdos_767.variants.czipszer`

Solved: stated here without proof.

> Czipszer proved that $g_k(n)\leq (k+1)n$.

```lean
theorem erdos_767.variants.czipszer (k n : ℕ) : g k n ≤ (k + 1) * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/767.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/767.lean#L70).

## `Erdos767.erdos_767.variants.posa`

Solved: stated here without proof.

> Pósa proved that $g_1(n)=2n-4$ for $n\geq 4$.

```lean
theorem erdos_767.variants.posa (n : ℕ) (hn : 4 ≤ n) : g 1 n = 2 * n - 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/767.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/767.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/767.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/767.lean)
- [erdosproblems.com/767](https://www.erdosproblems.com/767)
