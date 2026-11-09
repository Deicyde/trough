---
declaration: theorem
origin: cited
lean: Erdos505.erdos_505, Erdos505.erdos_505.small_dim
statement: formalized
---

# Erdős Problem 505

> *Reference:* [erdosproblems.com/505](https://www.erdosproblems.com/505)
>
> **Borsuk's conjecture** (1933): Is every bounded set of diameter 1 in $\mathbb{R}^n$
> the union of at most $n + 1$ sets of diameter strictly less than 1?
>
> Erdős [Er44] suspected this is false for sufficiently large $n$. Confirmed
> by Kahn–Kalai [KK93], who disproved the conjecture for $n \geq 2015$.
> Grinsztajn (2026) gave a counterexample for $n = 63$; the smallest refereed
> counterexample was $n = 64$ (Jenrich–Brouwer, 2014). In September 2026 an
> internal OpenAI model gave a counterexample for $n = 9$ [OAI26], with a
> formal Lean proof; see `Borsuk.borsuk_conjecture.not_nine`.
>
> The conjecture is true for $n \leq 3$ (Eggleston [Eg55] for $n = 3$).
>
> ### References
>
> - [Bo33] Borsuk, K. (1933). *Drei Sätze über die n-dimensionale euklidische Sphäre*.
>   Fund. Math. 20, 177–190.
> - [Er44] Erdős, P. (1944). Remarks on a conjecture of Borsuk.
> - [Eg55] Eggleston, H. G. (1955). *Covering a three-dimensional set with sets of
>   smaller diameter*. J. London Math. Soc. 30, 11–24.
> - [KK93] Kahn, J., Kalai, G. (1993). *A counterexample to Borsuk's conjecture*.
>   Bull. Amer. Math. Soc. 29, 60–62.
> - [OAI26] OpenAI (2026). *A nine-dimensional counterexample to Borsuk's covering assertion*.
>   OpenAI Math Release preprint.
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
>
> This file points to the canonical formalization in
> `FormalConjectures.Wikipedia.BorsukConjecture`.
>
> ### AI disclosure
>
> Lean 4 code in this file was drafted with assistance from Claude (Anthropic).
> The mathematical content and references are the author's own work.

*Quoted from [FormalConjectures/ErdosProblems/505.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/505.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/505](https://www.erdosproblems.com/505).

The file states 2 research or textbook statements: 2 solved.

## `Erdos505.erdos_505`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/96cd54930d844e3655e6bb89b96b65516397dae9/src/v4.24.0/ErdosProblems/Erdos505.lean#L1153](https://github.com/plby/lean-proofs/blob/96cd54930d844e3655e6bb89b96b65516397dae9/src/v4.24.0/ErdosProblems/Erdos505.lean#L1153).

> **Erdős Problem 505** (disproved). Borsuk's conjecture is false for
> sufficiently large $n$: there exists a dimension $n$ and a bounded set
> $S \subseteq \mathbb{R}^n$ with at least two points that cannot be
> covered by $n + 1$ subsets each of strictly smaller diameter.
>
> Erdős [Er44] suspected this. Disproved by Kahn–Kalai [KK93] for
> $n \geq 2015$. Currently known to be false for $n = 9$ [OAI26] and for
> $n \geq 63$. A formal proof was formalised by Boris Alexeev using Aristotle.

```lean
theorem erdos_505 : type_of% borsuk_conjecture.not_forall
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/505.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/505.lean#L78).

## `Erdos505.erdos_505.small_dim`

Solved: stated here without proof.

> **Borsuk's conjecture, small dimensions**: `Borsuk.BorsukConjecture n` holds for
> $n \leq 3$. Elementary for $n \leq 1$, proved by Borsuk [Bo33] for $n = 2$ and by
> Eggleston [Eg55] for $n = 3$.

```lean
theorem erdos_505.small_dim (n : ℕ) (hn : n ≤ 3) : BorsukConjecture n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/505.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/505.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/505.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/505.lean)
- [erdosproblems.com/505](https://www.erdosproblems.com/505)
