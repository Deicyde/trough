---
declaration: theorem
origin: cited
lean: Erdos231.erdos_231, Erdos231.erdos_231.variants.two_pow, Erdos231.erdos_231.variants.two_pow_small
statement: formalized
---

# Erdős Problem 231

> *References:*
> - [erdosproblems.com/231](https://www.erdosproblems.com/231)
> - [Er57] Erdős, Paul, *Some unsolved problems*. Michigan Math. J. (1957), 291-300.
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Ke92] Keränen, Veikko, *Abelian squares are avoidable on $4$ letters*. Automata, languages and
>   programming (Vienna, 1992) (1992), 41-52.
> - [FiPu23] Fici, Gabriele and Puzynina, Svetlana, *Abelian combinatorics on words: a survey*.
>   Comput. Sci. Rev. (2023), Paper No. 100532, 21.

*Quoted from [FormalConjectures/ErdosProblems/231.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/231.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/231](https://www.erdosproblems.com/231).

The file states 3 research or textbook statements: 3 solved. It also has 4 API statements, counted here but not shown.

## `Erdos231.erdos_231`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos231.lean#L38](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos231.lean#L38).

> Let $S$ be a string of length $2^k-1$ formed from an alphabet of $k$ characters. Must $S$ contain
> an abelian square: two consecutive blocks $x$ and $y$ such that $y$ is a permutation of $x$?
>
> Erdős initially conjectured that the answer is yes for all $k\geq 2$, but for $k=4$ this was
> disproved by de Bruijn and Erdős. Erdős then asked if there is in fact an infinite string formed
> from $\{1,2,3,4\}$ which contains no abelian squares? This is equivalent to
> [192](https://www.erdosproblems.com/192), and such a string was constructed by Keränen [Ke92]. The
> existence of this infinite string gives a negative answer to the problem for all $k\geq 4$.
>
> Containing no abelian squares is a stronger property than being squarefree (the existence of
> infinitely long squarefree strings over alphabets with $k\geq 3$ characters was established by
> Thue). We refer to a recent survey by Fici and Puzynina [FiPu23] for more background and related
> results.
>
> As stated, the answer is negative for every $k \geq 2$: the strings $121$ and $1213121$ of
> length $2^k - 1$ for $k = 2, 3$ contain no abelian square. See `erdos_231.variants.two_pow` for
> strings of length $2^k$.

```lean
theorem erdos_231 :
    ¬ ∀ k : ℕ, 2 ≤ k → ∀ S : List (Fin k), S.length = 2 ^ k - 1 → ContainsAbelianSquare S
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/231.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/231.lean#L122).

## `Erdos231.erdos_231.variants.two_pow`

Proved here.

> Perhaps Erdős meant $2^k$, where indeed there is an example for $k=4$:
>
> $$1213121412132124.$$
>
> Every string of length $2^k$ over $k$ characters contains an abelian square for $k = 2, 3$, but
> not for $k \geq 4$.

```lean
theorem erdos_231.variants.two_pow :
    ¬ ∀ k : ℕ, 2 ≤ k → ∀ S : List (Fin k), S.length = 2 ^ k → ContainsAbelianSquare S
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/231.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/231.lean#L133).

## `Erdos231.erdos_231.variants.two_pow_small`

Proved here.

> Every string of length $2^k$ over $k$ characters contains an abelian square for $k = 2, 3$.

```lean
theorem erdos_231.variants.two_pow_small (k : ℕ) (hk : k = 2 ∨ k = 3) (S : List (Fin k))
    (hS : S.length = 2 ^ k) : ContainsAbelianSquare S
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/231.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/231.lean#L140).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/231.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/231.lean)
- [erdosproblems.com/231](https://www.erdosproblems.com/231)
