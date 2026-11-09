---
declaration: theorem
origin: cited
lean: Erdos147.erdos_147, Erdos147.erdos_147.variants.janzer_even, Erdos147.erdos_147.variants.cubic, Erdos147.erdos_147.variants.janzer_conjecture
statement: formalized
---

# Erdős Problem 147

> *References:*
> - [erdosproblems.com/147](https://www.erdosproblems.com/147)
> - [ErSi84] Erdős, P. and Simonovits, M., *Cube-supersaturated graphs and related problems*.
>   Progress in graph theory (Waterloo, Ont., 1982) (1984), 203-218.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős,
>   I (1997), 47-67.
> - [Ja23] Janzer, Oliver, *Rainbow Turán number of even cycles, repeated patterns and blow-ups of
>   cycles*. Israel J. Math. (2023), 813--840.
> - [Ja23b] Janzer, Oliver, *Disproof of a conjecture of Erdős and Simonovits on the Turán number
>   of graphs with minimum degree 3*. Int. Math. Res. Not. IMRN (2023), 8478--8494.

*Quoted from [FormalConjectures/ErdosProblems/147.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/147.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/147](https://www.erdosproblems.com/147).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos147.erdos_147`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos147.lean#L799](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos147.lean#L799).

> If $H$ is bipartite with minimum degree $r$ then there exists $\epsilon=\epsilon(H)>0$ such that
> $$\mathrm{ex}(n;H) \gg n^{2-\frac{1}{r-1}+\epsilon}.$$
>
> Conjectured by Erdős and Simonovits [ErSi84]. A probabilistic argument shows that there exists
> some $\epsilon=\epsilon(H)>0$ such that $\mathrm{ex}(n;H) \gg n^{2-\frac{2}{r}+\epsilon}$.
>
> This conjecture was disproved by Janzer [Ja23] for even $r\geq 4$. The case $r=3$ was disproved
> by Janzer [Ja23b], who constructed, for any $\epsilon>0$, a $3$-regular bipartite graph $H$ such
> that $\mathrm{ex}(n;H)\ll n^{\frac{4}{3}+\epsilon}$.
>
> In [Ja23] Janzer conjectures that the above lower bound is sharp, in that for any $r\geq 3$ and
> $\epsilon>0$ there exists an $r$-regular graph $H$ such that
> $\mathrm{ex}(n;H) \ll n^{2-\frac{2}{r}+\epsilon}$. Janzer's result proves this for even
> $r\geq 4$.
>
> See also [113](https://www.erdosproblems.com/113), [146](https://www.erdosproblems.com/146), and
> [714](https://www.erdosproblems.com/714).
>
> The conjecture is stated for minimum degree $r \geq 2$ (for $r = 1$ the exponent
> $2 - \frac{1}{r-1}$ is not meaningful).

```lean
theorem erdos_147 :
    ¬ ∀ (V : Type) [Fintype V] [Nonempty V] (H : SimpleGraph V) [DecidableRel H.Adj],
      H.IsBipartite → 2 ≤ H.minDegree → ∃ ε : ℝ, 0 < ε ∧
        (fun n : ℕ => (n : ℝ) ^ (2 - 1 / ((H.minDegree : ℝ) - 1) + ε)) =O[atTop]
          fun n : ℕ => (extremalNumber n H : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/147.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/147.lean#L68).

## `Erdos147.erdos_147.variants.janzer_even`

Solved: stated here without proof.

> Janzer [Ja23] disproved the conjecture for even $r\geq 4$: for any even $r \geq 4$ and
> $\epsilon>0$ there exists a nonempty $r$-regular bipartite graph $H$ such that
> $\mathrm{ex}(n;H) \ll n^{2-\frac{2}{r}+\epsilon}$.

```lean
theorem erdos_147.variants.janzer_even (r : ℕ) (hr : 4 ≤ r) (heven : Even r) (ε : ℝ)
    (hε : 0 < ε) :
    ∃ (q : ℕ) (H : SimpleGraph (Fin q)), 0 < q ∧ H.IsBipartite ∧ H.IsRegularOfDegree r ∧
      (fun n : ℕ => (extremalNumber n H : ℝ)) =O[atTop]
        fun n : ℕ => (n : ℝ) ^ (2 - 2 / (r : ℝ) + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/147.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/147.lean#L82).

## `Erdos147.erdos_147.variants.cubic`

Solved: stated here without proof.

> Janzer [Ja23b] constructed, for any $\epsilon>0$, a nonempty $3$-regular bipartite graph $H$
> such that $\mathrm{ex}(n;H)\ll n^{\frac{4}{3}+\epsilon}$.

```lean
theorem erdos_147.variants.cubic (ε : ℝ) (hε : 0 < ε) :
    ∃ (q : ℕ) (H : SimpleGraph (Fin q)), 0 < q ∧ H.IsBipartite ∧ H.IsRegularOfDegree 3 ∧
      (fun n : ℕ => (extremalNumber n H : ℝ)) =O[atTop]
        fun n : ℕ => (n : ℝ) ^ (4 / 3 + ε : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/147.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/147.lean#L95).

## `Erdos147.erdos_147.variants.janzer_conjecture`

Open: stated without proof.

> Janzer [Ja23] conjectures that for any $r\geq 3$ and $\epsilon>0$ there exists a nonempty
> $r$-regular graph $H$ such that $\mathrm{ex}(n;H) \ll n^{2-\frac{2}{r}+\epsilon}$.

```lean
theorem erdos_147.variants.janzer_conjecture : ∀ r : ℕ, 3 ≤ r → ∀ ε : ℝ, 0 < ε →
    ∃ (q : ℕ) (H : SimpleGraph (Fin q)), 0 < q ∧ H.IsRegularOfDegree r ∧
      (fun n : ℕ => (extremalNumber n H : ℝ)) =O[atTop]
        fun n : ℕ => (n : ℝ) ^ (2 - 2 / (r : ℝ) + ε)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/147.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/147.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/147.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/147.lean)
- [erdosproblems.com/147](https://www.erdosproblems.com/147)
