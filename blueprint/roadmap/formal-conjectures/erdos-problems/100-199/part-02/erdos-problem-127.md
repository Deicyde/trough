---
declaration: theorem
origin: cited
lean: Erdos127.erdos_127, Erdos127.erdos_127.variants.edwards, Erdos127.erdos_127.variants.alon_upper
statement: formalized
---

# Erdős Problem 127

> *References:*
> - [erdosproblems.com/127](https://www.erdosproblems.com/127)
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*. Discrete
>   Math. (1997), 227-231.
> - [Ed73] Edwards, C. S., *Some extremal properties of bipartite subgraphs*. Canadian J. Math.
>   (1973), 475-485.
> - [Al96] Alon, Noga, *Bipartite subgraphs*. Combinatorica (1996), 301-311.

*Quoted from [FormalConjectures/ErdosProblems/127.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/127.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/127](https://www.erdosproblems.com/127).

The file states 3 research or textbook statements: 3 solved.

## `Erdos127.erdos_127`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos127.lean#L585](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos127.lean#L585).

> Let $f(m)$ be maximal such that every graph with $m$ edges must contain a bipartite graph with
>
> $$\geq \frac{m}{2}+\frac{\sqrt{8m+1}-1}{8}+f(m)$$
>
> edges. Is there an infinite sequence of $m_i$ such that $f(m_i)\to \infty$?
>
> Conjectured by Erdős, Kohayakava, and Gyárfás [Er97b]. Edwards [Ed73] proved that $f(m)\geq 0$
> always. Note that $f(\binom{n}{2})= 0$, taking $K_n$. Solved by Alon [Al96], who showed
> $f(n^2/2)\gg n^{1/2}$, and also showed that $f(m)\ll m^{1/4}$ for all $m$. The best possible
> constant in $f(m)\leq Cm^{1/4}$ is unknown.

```lean
theorem erdos_127 : ∃ m : ℕ → ℕ, Tendsto m atTop atTop ∧
    Tendsto (fun i => f (m i)) atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/127.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/127.lean#L58).

## `Erdos127.erdos_127.variants.edwards`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos127.lean#L89](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos127.lean#L89).

> Edwards [Ed73] proved that every graph with $m$ edges contains a bipartite subgraph with at
> least $\frac{m}{2}+\frac{\sqrt{8m+1}-1}{8}$ edges.

```lean
theorem erdos_127.variants.edwards {V : Type*} [Finite V] (G : SimpleGraph V) :
    ∃ H : SimpleGraph V, H ≤ G ∧ H.IsBipartite ∧
      (G.edgeSet.ncard : ℝ) / 2 + (√(8 * G.edgeSet.ncard + 1) - 1) / 8 ≤ H.edgeSet.ncard
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/127.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/127.lean#L67).

## `Erdos127.erdos_127.variants.alon_upper`

Solved: stated here without proof.

> Alon [Al96] showed that $f(m)\ll m^{1/4}$ for all $m$.

```lean
theorem erdos_127.variants.alon_upper : ∃ C : ℝ, ∀ m : ℕ, (f m : ℝ) ≤ C * (m : ℝ) ^ (1 / 4 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/127.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/127.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/127.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/127.lean)
- [erdosproblems.com/127](https://www.erdosproblems.com/127)
