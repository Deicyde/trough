---
declaration: theorem
origin: cited
lean: Erdos615.erdos_615, Erdos615.erdos_615.variants.fox_loh_zhao, Erdos615.erdos_615.variants.sudakov
statement: formalized
---

# Erdős Problem 615

> A Ramsey–Turán problem of Erdős, Hajnal, Simonovits, Sós, and Szemerédi [EHSSS93]: does there
> exist a constant $c > 0$ such that every graph on $n$ vertices with at least $(1/8 - c)n^2$
> edges contains either a $K_4$ or an independent set on at least $n/\log n$ vertices? In the
> notation of Ramsey–Turán theory this asks whether
> $$\mathrm{rt}(n; 4, n/\log n) < (1/8 - c)n^2.$$
>
> This was disproved by Fox, Loh, and Zhao [FLZ15], who showed that
> $\mathrm{rt}(n; 4, ne^{-f(n)}) \geq (1/8 - o(1))n^2$ whenever
> $f(n) = o(\sqrt{\log n/\log\log n})$. In the other direction Sudakov [Su03] had shown that
> $\mathrm{rt}(n; 4, ne^{-f(n)}) = o(n^2)$ whenever $f(n)/\sqrt{\log n} \to \infty$.
>
> *References:*
> * [erdosproblems.com/615](https://www.erdosproblems.com/615)
> * [EHSSS93] Erdős, P., Hajnal, A., Simonovits, M., Sós, V. T., and Szemerédi, E.,
>   *Turán-Ramsey theorems and simple asymptotically extremal structures*. Combinatorica 13
>   (1993), 31--56.
> * [Su03] Sudakov, B., *A few remarks on Ramsey-Turán-type problems*. J. Combin. Theory Ser. B
>   88 (2003), 99--106.
> * [FLZ15] Fox, J., Loh, P.-S., and Zhao, Y., *The critical window for the classical
>   Ramsey-Turán problem*. Combinatorica 35 (2015), 435--476.

*Quoted from [FormalConjectures/ErdosProblems/615.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/615.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/615](https://www.erdosproblems.com/615).

The file states 3 research or textbook statements: 3 solved. It also has 1 test statement, counted here but not shown.

## `Erdos615.erdos_615`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos615.lean#L492](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos615.lean#L492).

> Does there exist some constant $c > 0$ such that for all sufficiently large $n$, if $G$ is a
> graph with $n$ vertices and at least $(1/8 - c)n^2$ edges then $G$ must contain either a $K_4$
> or an independent set on at least $n/\log n$ vertices?
>
> The answer is no, as shown by Fox, Loh, and Zhao [FLZ15].

```lean
theorem erdos_615 :
    ¬ ∃ c : ℝ, 0 < c ∧ ∀ᶠ (n : ℕ) in atTop,
      ∀ G : SimpleGraph (Fin n), (1 / 8 - c) * n ^ 2 ≤ G.edgeFinset.card →
        ¬ G.CliqueFree 4 ∨ (n : ℝ) / Real.log n ≤ G.indepNum
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/615.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/615.lean#L62).

## `Erdos615.erdos_615.variants.fox_loh_zhao`

Solved: stated here without proof.

> The result of Fox, Loh, and Zhao [FLZ15] disproving the problem: if $f(n) \geq 0$ satisfies
> $f(n) = o(\sqrt{\log n/\log\log n})$, then for every $\epsilon > 0$ and all sufficiently
> large $n$ there is a $K_4$-free graph on $n$ vertices with independence number at most
> $ne^{-f(n)}$ and at least $(1/8 - \epsilon)n^2$ edges; that is,
> $\mathrm{rt}(n; 4, ne^{-f(n)}) \geq (1/8 - o(1))n^2$. Applied with
> $f(n) = \log\log n$, this disproves the headline problem, since
> $ne^{-f(n)} = n/\log n = o(n)$.

```lean
theorem erdos_615.variants.fox_loh_zhao (f : ℕ → ℝ) (hf : ∀ n, 0 ≤ f n)
    (hfo : Tendsto (fun n : ℕ => f n / Real.sqrt (Real.log n / Real.log (Real.log n)))
      atTop (nhds 0)) (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop,
      ∃ G : SimpleGraph (Fin n), G.CliqueFree 4 ∧
        (G.indepNum : ℝ) ≤ n * Real.exp (-f n) ∧
        (1 / 8 - ε) * n ^ 2 ≤ G.edgeFinset.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/615.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/615.lean#L79).

## `Erdos615.erdos_615.variants.sudakov`

Solved: stated here without proof.

> The complementary result of Sudakov [Su03]: if $f(n)/\sqrt{\log n} \to \infty$ then
> $\mathrm{rt}(n; 4, ne^{-f(n)}) = o(n^2)$; that is, for every $\epsilon > 0$ and all
> sufficiently large $n$, every $K_4$-free graph on $n$ vertices with independence number at
> most $ne^{-f(n)}$ has at most $\epsilon n^2$ edges.

```lean
theorem erdos_615.variants.sudakov (f : ℕ → ℝ)
    (hf : Tendsto (fun n : ℕ => f n / Real.sqrt (Real.log n)) atTop atTop)
    (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ (n : ℕ) in atTop,
      ∀ G : SimpleGraph (Fin n), G.CliqueFree 4 →
        (G.indepNum : ℝ) ≤ n * Real.exp (-f n) →
        (G.edgeFinset.card : ℝ) ≤ ε * n ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/615.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/615.lean#L96).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/615.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/615.lean)
- [erdosproblems.com/615](https://www.erdosproblems.com/615)
