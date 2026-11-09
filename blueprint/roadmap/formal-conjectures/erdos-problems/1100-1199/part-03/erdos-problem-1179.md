---
declaration: theorem
origin: cited
lean: Erdos1179.erdos_1179, Erdos1179.erdos_1179.variants.lower_bound
statement: formalized
---

# Erdős Problem 1179

> *References:*
> - [erdosproblems.com/1179](https://www.erdosproblems.com/1179)
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [ErRe65] Erdős, P. and Rényi, A., *Probabilistic methods in group theory*. J. Analyse Math.
>   (1965), 127-138.
> - [ErHa76] Erdős, P. and Hall, R. R., *Probabilistic methods in group theory. II*. Houston J.
>   Math. (1976), 173-180.

*Quoted from [FormalConjectures/ErdosProblems/1179.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1179.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1179](https://www.erdosproblems.com/1179).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1179.erdos_1179`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1179.lean#L3564](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1179.lean#L3564).

> Let $0\lt \epsilon<1$ and let $g_\epsilon(N)$ be the minimal $k$ such that if $G$ is an abelian
> group of size $N$ and $A\subseteq G$ is a uniformly random subset of size $k$, and
> $$F_A(g) = \#\left\{ S\subseteq A : g = \sum_{x\in S}x\right\},$$
> then, with probability $\to 1$ as $N\to \infty$,
> $$\left\lvert F_A(g)-\frac{2^k}{N}\right\rvert \leq \epsilon \frac{2^k}{N}$$
> for all $g\in G$.
>
> Estimate $g_\epsilon(N)$ - in particular, is it true that for all $\epsilon>0$
> $$g_\epsilon(N)=(1+o_\epsilon(1))\log_2N?$$
>
> It is trivial that $g_\epsilon(N)\geq \log_2N$ for all $0\lt \epsilon<1$. Erdős and Rényi [ErRe65]
> proved that for all $0\lt \epsilon<1$, $g_\epsilon(N) \leq (2+o(1))\log_2N+O_\epsilon(1)$. Erdős and
> Hall [ErHa76] proved that, for all $0\lt \epsilon<1$,
> $$g_\epsilon(N)\leq \left(1+O_\epsilon\left(\frac{\log\log\log N}{\log\log N}\right)\right)
> \log_2N.$$
>
> The upper bound $g_\epsilon(N)\leq (1+o(1))\log_2 N$ is formalised as: there is a choice of sizes
> $k(N) = (1+o(1))\log_2 N$ such that, along any sequence of abelian groups with $|G|\to\infty$,
> the probability that a random $k(|G|)$-subset is $\epsilon$-balanced tends to $1$. The matching
> lower bound is `erdos_1179.variants.lower_bound`.
>
> See also [543](https://www.erdosproblems.com/543).

```lean
theorem erdos_1179 : ∀ ε : ℝ, 0 < ε → ε < 1 → ∃ k : ℕ → ℕ,
    Tendsto (fun N : ℕ ↦ (k N : ℝ) / Real.logb 2 N) atTop (nhds 1) ∧
      ∀ (G : ℕ → Type) [∀ i, AddCommGroup (G i)] [∀ i, Fintype (G i)],
        Tendsto (fun i ↦ Fintype.card (G i)) atTop atTop →
          Tendsto (fun i ↦ successProbability (G i) ε (k (Fintype.card (G i)))) atTop
            (nhds 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1179.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1179.lean#L86).

## `Erdos1179.erdos_1179.variants.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1179.lean#L3564](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1179.lean#L3564).

> It is trivial that $g_\epsilon(N)\geq \log_2N$: an $\epsilon$-balanced set $A$ with
> $\epsilon < 1$ must satisfy $|G| \leq 2^{|A|}$, since every $g$ has a representation.

```lean
theorem erdos_1179.variants.lower_bound : ∀ ε : ℝ, 0 < ε → ε < 1 →
    ∀ A : Finset G, IsBalanced ε A → Fintype.card G ≤ 2 ^ A.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1179.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1179.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1179.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1179.lean)
- [erdosproblems.com/1179](https://www.erdosproblems.com/1179)
