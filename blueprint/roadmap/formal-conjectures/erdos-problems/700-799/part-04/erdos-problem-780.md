---
declaration: theorem
origin: cited
lean: Erdos780.erdos_780, Erdos780.erdos_780.variants.sharp
statement: formalized
---

# Erdős Problem 780

> *References:*
> - [erdosproblems.com/780](https://www.erdosproblems.com/780)
> - [Er76] Erdős, Paul, _Problems and results in combinatorial analysis_. Colloquio Internazionale
>   sulle Teorie Combinatorie (Roma, 1973), Tomo II (1976), 3-17.
> - [Lo78] Lovász, L., _Kneser's conjecture, chromatic number, and homotopy_. J. Combin. Theory
>   Ser. A (1978), 319-324.
> - [AFL86] Alon, N. and Frankl, P. and Lovász, L., _The chromatic number of Kneser hypergraphs_.
>   Trans. Amer. Math. Soc. (1986), 359-370.

*Quoted from [FormalConjectures/ErdosProblems/780.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/780.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/780](https://www.erdosproblems.com/780).

The file states 2 research or textbook statements: 1 solved and 1 textbook result.

## `Erdos780.erdos_780`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos780.lean#L345](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos780.lean#L345).

> Suppose $n\geq kr+(t-1)(k-1)$ and the edges of the complete $r$-uniform hypergraph on $n$
> vertices are $t$-coloured. Prove that some colour class must contain $k$ pairwise disjoint edges.
>
> In other words, this problem asks to determine the chromatic number of the Kneser hypergraph.
> When $k=2$ this was conjectured by Kneser and proved by Lovász [Lo78]. The general case was
> proved by Alon, Frankl, and Lovász [AFL86].

```lean
theorem erdos_780 (n k r t : ℕ) (hr : 1 ≤ r) (ht : 1 ≤ t)
    (hn : k * r + (t - 1) * (k - 1) ≤ n) (c : {e : Finset (Fin n) // e.card = r} → Fin t) :
    ∃ (i : Fin t) (e : Fin k → {e : Finset (Fin n) // e.card = r}),
      (∀ j, c (e j) = i) ∧ Pairwise fun a b ↦ Disjoint (e a).1 (e b).1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/780.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/780.lean#L48).

## `Erdos780.erdos_780.variants.sharp`

Textbook result, stated without proof.

> This would be best possible: if $n=kr-1+(t-1)(k-1)$ then decomposing $[n]$ as one set $X_1$ of
> size $kr-1$ and $t-1$ sets $X_2,\ldots,X_{t}$ of size $k-1$, a colouring without $k$ pairwise
> disjoint edges is given colouring all subsets of $X_1$ in colour $1$ and assigning an edge with
> colour $2\leq i\leq t$ if $i$ is minimal such that $X_i$ intersects the edge.

```lean
theorem erdos_780.variants.sharp (k r t : ℕ) (hk : 1 ≤ k) (hr : 1 ≤ r) (ht : 1 ≤ t) :
    ∃ c : {e : Finset (Fin (k * r - 1 + (t - 1) * (k - 1))) // e.card = r} → Fin t,
      ¬ ∃ (i : Fin t) (e : Fin k → {e : Finset (Fin (k * r - 1 + (t - 1) * (k - 1))) //
          e.card = r}), (∀ j, c (e j) = i) ∧ Pairwise fun a b ↦ Disjoint (e a).1 (e b).1
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/780.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/780.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/780.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/780.lean)
- [erdosproblems.com/780](https://www.erdosproblems.com/780)
