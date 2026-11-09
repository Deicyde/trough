---
declaration: theorem
origin: cited
lean: Erdos714.erdos_714
statement: formalized
---

# Erdős Problem 714

> *References:*
> - [erdosproblems.com/714](https://www.erdosproblems.com/714)
> - [Br66] Brown, W. G., *On graphs that do not contain a Thomsen graph*. Canad. Math. Bull. (1966),
>   281-285.
> - [ERS66] Erdős, P. and Rényi, A. and Sós, V. T., *On a problem of graph theory*. Studia Sci. Math.
>   Hungar. (1966), 215--235.
> - [KST54] Kövari, T. and Sós, V. T. and Turán, P., *On a problem of K. Zarankiewicz*. Colloq. Math.
>   (1954), 50-57.

*Quoted from [FormalConjectures/ErdosProblems/714.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/714.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/714](https://www.erdosproblems.com/714).

The file states 1 research or textbook statement: 1 open.

## `Erdos714.erdos_714`

Open: stated without proof.

> Is it true that $$\mathrm{ex}(n; K_{r,r}) \gg n^{2-1/r}?$$

```lean
theorem erdos_714 :
    ∀ r : ℕ, 2 ≤ r → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop,
      c * (n : ℝ) ^ ((2 : ℝ) - 1 / (r : ℝ)) ≤
        (extremalNumber n (completeBipartiteGraph (Fin r) (Fin r)) : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/714.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/714.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/714.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/714.lean)
- [erdosproblems.com/714](https://www.erdosproblems.com/714)
