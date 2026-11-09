---
declaration: theorem
origin: cited
lean: Erdos775.erdos_775, Erdos775.erdos_775.variants.gao, Erdos775.erdos_775.variants.spencer, Erdos775.erdos_775.variants.moon_moser
statement: formalized
---

# Erdős Problem 775

> *References:*
> - [erdosproblems.com/775](https://www.erdosproblems.com/775)
> - [Ga25] Gao, J., *On cliques in hypergraphs*. arXiv:2510.14804 (2025).
> - [MoMo65] Moon, J. W. and Moser, L., *On cliques in graphs*. Israel J. Math. (1965), 23-28.
> - [Sp71] Spencer, J. H., *On cliques in graphs*. Israel J. Math. (1971), 419-421.

*Quoted from [FormalConjectures/ErdosProblems/775.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/775.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/775](https://www.erdosproblems.com/775).

The file states 4 research or textbook statements: 4 solved.

## `Erdos775.erdos_775`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos775.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos775.lean).

> Is there a $3$-uniform hypergraph on $n$ vertices which contains at least $n-O(1)$ different
> sizes of cliques (maximal complete subgraphs)?
>
> The answer is no, as proved by Gao [Ga25]: more generally, for any $k\geq 3$, every $k$-uniform
> hypergraph on $n$ vertices contains at most $n-f_k(n)$ different sizes of cliques, where
> $f_k(n)\to \infty$ as $n\to \infty$.

```lean
theorem erdos_775 :
    ¬ ∃ C : ℕ, ∃ᶠ n : ℕ in atTop, ∃ H : UniformHypergraph (Fin n) 3,
      n - C ≤ (UniformHypergraph.cliqueSizes H).ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/775.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/775.lean#L46).

## `Erdos775.erdos_775.variants.gao`

Solved: stated here without proof.

> The answer is no, as proved by Gao [Ga25]: more generally, for any $k\geq 3$, every $k$-uniform
> hypergraph on $n$ vertices contains at most $n-f_k(n)$ different sizes of cliques, where
> $f_k(n)\to \infty$ as $n\to \infty$.

```lean
theorem erdos_775.variants.gao :
    ∃ f : ℕ → ℕ, Tendsto f atTop atTop ∧
      ∀ᶠ n : ℕ in atTop, ∀ H : UniformHypergraph (Fin n) 3,
        (UniformHypergraph.cliqueSizes H).ncard + f n ≤ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/775.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/775.lean#L57).

## `Erdos775.erdos_775.variants.spencer`

Solved: stated here without proof.

> For graphs, Spencer [Sp71] constructed a graph which contains cliques of at least
> $n-\log_2n+O(1)$ different sizes.

```lean
theorem erdos_775.variants.spencer :
    ∃ C : ℝ, ∀ n : ℕ, ∃ G : SimpleGraph (Fin n),
      (n : ℝ) - Real.logb 2 (n : ℝ) - C ≤ ((SimpleGraph.cliqueSizes G).ncard : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/775.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/775.lean#L68).

## `Erdos775.erdos_775.variants.moon_moser`

Solved: stated here without proof.

> For graphs, Spencer [Sp71] constructed a graph which contains cliques of at least
> $n-\log_2n+O(1)$ different sizes, which Moon and Moser [MoMo65] showed to be best possible.

```lean
theorem erdos_775.variants.moon_moser :
    ∃ C : ℝ, ∀ n : ℕ, ∀ G : SimpleGraph (Fin n),
      ((SimpleGraph.cliqueSizes G).ncard : ℝ) ≤ (n : ℝ) - Real.logb 2 (n : ℝ) + C
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/775.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/775.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/775.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/775.lean)
- [erdosproblems.com/775](https://www.erdosproblems.com/775)
