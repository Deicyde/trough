---
declaration: theorem
origin: cited
lean: Erdos639.erdos_639, Erdos639.erdos_639.variants.exact, Erdos639.erdos_639.variants.ten_le, Erdos639.erdos_639.variants.six_vertices
statement: formalized
---

# Erdős Problem 639

> *References:*
> - [erdosproblems.com/639](https://www.erdosproblems.com/639)
> - [Er97d] Erdős, Paul, *Some recent problems and results in graph theory*. Discrete Math.
>   (1997), 81-85.
> - [KeSu04] Keevash, Peter and Sudakov, Benny, *On the number of edges not covered by monochromatic
>   copies of a fixed graph*. J. Combin. Theory Ser. B (2004), 41-53.
> - [Py86] Pyber, L., *Clique covering of graphs*. Combinatorica (1986), 393-398.

*Quoted from [FormalConjectures/ErdosProblems/639.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/639.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/639](https://www.erdosproblems.com/639).

The file states 4 research or textbook statements: 4 solved.

## `Erdos639.erdos_639`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos639.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos639.lean).

> Is it true that if the edges of $K_n$ are 2-coloured then there are at most $n^2/4$ many edges
> which do not occur in a monochromatic triangle?
>
> Solved by Erdős, Rousseau, and Schelp for large $n$, but unpublished. Alon has observed that this
> also follows from a result of Pyber [Py86], which states that (for large enough $n$) at most
> $\lfloor n^2/4\rfloor+2$ monochromatic cliques cover all edges of a $2$-coloured $K_n$.
>
> This problem was solved completely by Keevash and Sudakov [KeSu04], who proved that the correct
> threshold is $\lfloor n^2/4\rfloor$ for all $n\geq 7$, is $\binom{n}{2}$ for $n\leq 5$, and is
> $10$ for $n=6$.
>
> Since the bound fails for small $n$ (at $n=6$ the threshold is $10 > 6^2/4$), the statement is
> formalized in the asymptotic reading in which the problem was posed and solved: for all
> sufficiently large $n$, every $2$-colouring of the edges of $K_n$ leaves at most $n^2/4$ edges
> not occurring in a monochromatic triangle. Edges of $K_n$ are the non-diagonal unordered pairs
> `Sym2 (Fin n)`; an edge $\{x, y\}$ occurs in a monochromatic triangle if and only if there is a
> third vertex $z$ with $C(\{x, z\}) = C(\{y, z\}) = C(\{x, y\})$.
>
> The linked file proves the bound for every finite vertex type with at least $10$ vertices, which
> gives the `atTop` reading below, and collects the uncovered edges as the edge set of a graph
> rather than as a set of pairs.

```lean
theorem erdos_639 :
    ∀ᶠ (n : ℕ) in atTop, ∀ C : Sym2 (Fin n) → Fin 2,
      {e : Sym2 (Fin n) | ¬e.IsDiag ∧
        ∀ x y : Fin n, e = s(x, y) →
          ¬∃ z, z ≠ x ∧ z ≠ y ∧ C s(x, z) = C e ∧ C s(y, z) = C e}.ncard ≤ n ^ 2 / 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/639.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/639.lean#L63).

## `Erdos639.erdos_639.variants.exact`

Solved: stated here without proof.

> The exact maximum number of uncovered edges is $\binom{n}{2}$ for $n\leq 5$, $10$ for
> $n=6$, and $\lfloor n^2/4\rfloor$ for $n\geq 7$ [KeSu04, Theorem 1.1].
> `IsGreatest` states both the upper bound and its attainment by a colouring.

```lean
theorem erdos_639.variants.exact :
    ∀ n : ℕ, IsGreatest
      (Set.range fun C : Sym2 (Fin n) → Fin 2 => (uncoveredEdges C).ncard)
      (if n ≤ 5 then n.choose 2 else if n = 6 then 10 else n ^ 2 / 4)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/639.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/639.lean#L81).

## `Erdos639.erdos_639.variants.ten_le`

Solved: stated here; a Lean proof is at [https://github.com/AItoBit/formal-conjectures/blob/0ad11a9f7f83c7ada19d42f1a95964465fb1195f/proofs/erdos639/Bridge639.lean](https://github.com/AItoBit/formal-conjectures/blob/0ad11a9f7f83c7ada19d42f1a95964465fb1195f/proofs/erdos639/Bridge639.lean).

> Every two-colouring of $K_n$ with $n\geq 10$ has at most
> $\lfloor n^2/4\rfloor$ uncovered edges [KeSu04, Proposition 2.1].

```lean
theorem erdos_639.variants.ten_le :
    ∀ n : ℕ, 10 ≤ n → ∀ C : Sym2 (Fin n) → Fin 2,
      (uncoveredEdges C).ncard ≤ n ^ 2 / 4
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/639.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/639.lean#L92).

## `Erdos639.erdos_639.variants.six_vertices`

Proved here.

> There is a two-colouring of $K_6$ with ten uncovered edges, exceeding $6^2/4$.

```lean
theorem erdos_639.variants.six_vertices :
    ∃ C : Sym2 (Fin 6) → Fin 2, (uncoveredEdges C).ncard = 10 ∧
      6 ^ 2 / 4 < (uncoveredEdges C).ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/639.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/639.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/639.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/639.lean)
- [erdosproblems.com/639](https://www.erdosproblems.com/639)
