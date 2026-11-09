---
declaration: theorem
origin: cited
lean: Erdos713.erdos_713.parts.i, Erdos713.erdos_713.parts.ii
statement: formalized
---

# Erdős Problem 713

> *References:*
> - [erdosproblems.com/713](https://www.erdosproblems.com/713)
> - [Er67d] Erdős, P., *Some recent results on extremal problems in graph theory. {R}esults*. (1967),
>   117--123 (English); pp. 124--130 (French).
> - [ErSi70] Erdős, P. and Simonovits, M., *Some extremal problems in graph theory*. Combinatorial
>   theory and its applications, I-III (Proc. Colloq., Balatonfüred, 1969) (1970), 377-390.
> - [FrFu87] Frankl, P. and Füredi, Z., *Exact solution of some Turán-type problems*. J. Combin.
>   Theory Ser. A (1987), 226--262.
> - [FuGe21] Füredi, Zoltán and Gerbner, Dániel, *Hypergraphs without exponents*. J. Combin. Theory
>   Ser. A (2021), Paper No. 105517, 9.

*Quoted from [FormalConjectures/ErdosProblems/713.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/713.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/713](https://www.erdosproblems.com/713).

The file states 2 research or textbook statements: 2 open.

## `Erdos713.erdos_713.parts.i`

Open: stated without proof.

> Is it true that, for every bipartite graph $G$, there exists some $\alpha\in [1,2)$ and $c>0$ such that $$\mathrm{ex}(n;G)\sim cn^\alpha?$$
>
> The condition that $G$ have at least two edges excludes degenerate forbidden graphs whose
> extremal number is eventually zero, for which the displayed asymptotic with $c>0$ is impossible.

```lean
theorem erdos_713.parts.i :
    ∀ (q : ℕ) (G : SimpleGraph (Fin q)), G.IsBipartite → 2 ≤ G.edgeFinset.card →
      ∃ α c : ℝ, α ∈ Set.Ico 1 2 ∧ 0 < c ∧
        Asymptotics.IsEquivalent atTop
          (fun n : ℕ => (extremalNumber n G : ℝ))
          (fun n : ℕ => c * (n : ℝ) ^ α)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/713.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/713.lean#L49).

## `Erdos713.erdos_713.parts.ii`

Open: stated without proof.

> Must $\alpha$ be rational?
>
> The same nondegeneracy condition on $G$ is used as in part (i). Rationality means that the real
> number $\alpha$ lies in the image of the canonical embedding $\mathbb{Q}\to\mathbb{R}$.

```lean
theorem erdos_713.parts.ii :
    ∀ (q : ℕ) (G : SimpleGraph (Fin q)), G.IsBipartite → 2 ≤ G.edgeFinset.card →
      ∀ α c : ℝ, α ∈ Set.Ico 1 2 → 0 < c →
        Asymptotics.IsEquivalent atTop
          (fun n : ℕ => (extremalNumber n G : ℝ))
          (fun n : ℕ => c * (n : ℝ) ^ α) →
        α ∈ Set.range ((↑) : ℚ → ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/713.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/713.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/713.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/713.lean)
- [erdosproblems.com/713](https://www.erdosproblems.com/713)
