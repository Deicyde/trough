---
declaration: theorem
origin: cited
lean: Erdos60.erdos_60, Erdos60.erdos_60.variants.he_ma_yang, Erdos60.erdos_60.variants.two_copies
statement: formalized
---

# Erdős Problem 60

> *References:*
> - [erdosproblems.com/60](https://www.erdosproblems.com/60)
> - [HeMaYa21] He, J. and Ma, J. and Yang, T., *Some extremal results on 4-cycles*. Journal of
>   Combinatorial Theory B (2021).

*Quoted from [FormalConjectures/ErdosProblems/60.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/60.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/60](https://www.erdosproblems.com/60).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos60.erdos_60`

Open: stated without proof.

> Does every graph on $n$ vertices with $>\mathrm{ex}(n;C_4)$ edges contain $\gg n^{1/2}$ many
> copies of $C_4$?

```lean
theorem erdos_60 :
    ∃ c : ℝ, c > 0 ∧
      ∀ᶠ n : ℕ in atTop,
        ∀ (G : SimpleGraph (Fin n)) [DecidableRel G.Adj],
          (extremalNumber n (cycleGraph 4) < G.edgeFinset.card) →
          (c * Real.sqrt (n : ℝ) ≤ ({ H' : G.Subgraph | Nonempty (H'.coe ≃g cycleGraph 4) }.ncard : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/60.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/60.lean#L41).

## `Erdos60.erdos_60.variants.he_ma_yang`

Solved: stated here without proof.

> He, Ma, and Yang [HeMaYa21] proved the conjecture when $n = q^2 + q + 1$ for some $q = 2^k$: they
> showed that for large even $q$ every graph on $q^2 + q + 1$ vertices with
> $\frac{1}{2}q(q+1)^2 + 1$ edges contains at least $q - 1$ copies of $C_4$, and
> $\mathrm{ex}(q^2 + q + 1; C_4) = \frac{1}{2}q(q+1)^2$ when $q = 2^k$.

```lean
theorem erdos_60.variants.he_ma_yang :
    ∃ c : ℝ, c > 0 ∧
      ∀ (q : ℕ) (_hq : q.isPowerOfTwo),
        ∀ (G : SimpleGraph (Fin (q^2 + q + 1))) [DecidableRel G.Adj],
          (extremalNumber (q^2 + q + 1) (cycleGraph 4) < G.edgeFinset.card) →
          (c * Real.sqrt ((q^2 + q + 1) : ℝ) ≤ ({ H' : G.Subgraph | Nonempty (H'.coe ≃g cycleGraph 4) }.ncard : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/60.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/60.lean#L58).

## `Erdos60.erdos_60.variants.two_copies`

Solved: stated here without proof.

> Erdős and Simonovits conjectured that at least 2 copies of $C_4$ are guaranteed.

```lean
theorem erdos_60.variants.two_copies :
    ∀ᶠ n : ℕ in atTop,
      ∀ (G : SimpleGraph (Fin n)) [DecidableRel G.Adj],
        (extremalNumber n (cycleGraph 4) < G.edgeFinset.card) →
        (2 ≤ { H' : G.Subgraph | Nonempty (H'.coe ≃g cycleGraph 4) }.ncard)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/60.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/60.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/60.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/60.lean)
- [erdosproblems.com/60](https://www.erdosproblems.com/60)
