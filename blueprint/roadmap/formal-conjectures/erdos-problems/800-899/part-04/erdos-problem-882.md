---
declaration: theorem
origin: cited
lean: Erdos882.erdos_882, Erdos882.erdos_882.variants.lower_bound, Erdos882.erdos_882.variants.lower_bound_explicit, Erdos882.erdos_882.variants.sandor, Erdos882.erdos_882.variants.greedy
statement: formalized
---

# Erdős Problem 882

> *References:*
> - [erdosproblems.com/882](https://www.erdosproblems.com/882)
> - [Er98] Erdős, Paul, *Some of my new and almost new problems and results in combinatorial
>   number theory*. Number theory (Eger, 1996) (1998), 169-180.
> - [ELRSS99] Erdős, P., Lev, V., Rauzy, G., Sándor, C. and Sárközy, A., *Greedy algorithm,
>   arithmetic progressions, subset sums and divisibility*. Discrete Math. (1999), 119-135.
> - [Erdős Problem 1](https://www.erdosproblems.com/1) for the upper bound.
> - [Alexeev] Boris Alexeev's sorry-free Lean 4 formalisation of the lower bound,
>   [plby/lean-proofs](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos882.lean).

*Quoted from [FormalConjectures/ErdosProblems/882.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/882.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/882](https://www.erdosproblems.com/882).

The file states 5 research or textbook statements: 5 solved. It also has 2 test statements, counted here but not shown.

## `Erdos882.erdos_882`

Solved: stated here without proof.

> What is the size of the largest $A\subseteq \{1,\ldots,n\}$ such that in the set
> $$\left\{ \sum_{a\in S} a : \emptyset\neq S\subseteq A\right\}$$
> no two distinct elements divide each other?
>
> A problem of Erdős and Sárközy. The answer is $(1+o(1))\log_2 n$: the lower bound
> $\lvert A\rvert > \log_2 n - 1$ is achieved by the construction of Erdős, Lev, Rauzy, Sándor
> and Sárközy [ELRSS99] (see `erdos_882.variants.lower_bound`), while
> [Erdős Problem 1](https://www.erdosproblems.com/1) gives
> $\lvert A\rvert \leq \log_2 n + \tfrac{1}{2}\log_2\log n + O(1)$.

```lean
theorem erdos_882 :
    Filter.Tendsto (fun n : ℕ => (maxAntichainCard n : ℝ) / Real.logb 2 n)
      Filter.atTop (nhds 1)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/882.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/882.lean#L64).

## `Erdos882.erdos_882.variants.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/ToshiDad/erdos-882/blob/6ea233aed4b3efce92e2754177ef15c4085f8732/Erdos882.lean#L394](https://github.com/ToshiDad/erdos-882/blob/6ea233aed4b3efce92e2754177ef15c4085f8732/Erdos882.lean#L394).

> Erdős, Lev, Rauzy, Sándor and Sárközy [ELRSS99] proved that
> $\lvert A\rvert > \log_2 n - 1$ is achievable, taking
> $A = \{2^m - 2^{m-1}, 2^m - 2^{m-2}, \ldots, 2^m - 1\}$.
>
> The key property of this construction is that distinct nonempty subsets have subset sums
> which never divide one another.
>
> The linked theorem `no_div` is phrased in terms of index sets $S \subseteq \{0, \ldots, m-1\}$,
> i.e. $\sum_{i \in S_1} (2^m - 2^i) \nmid \sum_{i \in S_2} (2^m - 2^i)$ for distinct nonempty
> $S_1, S_2$; it transfers to subsets of `A m` via the injectivity of $i \mapsto 2^m - 2^i$
> (see `card_A`).

```lean
theorem erdos_882.variants.lower_bound (m : ℕ) : IsSubsetSumAntichain (A m)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/882.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/882.lean#L114).

## `Erdos882.erdos_882.variants.lower_bound_explicit`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos882.lean#L561](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos882.lean#L561).

> The lower bound of [ELRSS99] in quantitative form: for every $n \geq 1$ there is a subset-sum
> antichain $A \subseteq \{1, \ldots, n\}$ with $\lvert A\rvert > \log_2 n - 1$, namely $A_m$
> with $m = \lfloor \log_2 n \rfloor$ (by `erdos_882.variants.lower_bound`, `A_subset_Icc`
> and `card_A`).
>
> A sorry-free Lean 4 proof of this statement is the theorem `erdos_882` of [Alexeev].
> That formalisation expresses the antichain condition as primitivity of the *set* of nonempty
> subset sums (no element divides another one). For $A \subseteq \{1, \ldots, n\}$ this is
> equivalent to `IsSubsetSumAntichain A`: if two distinct subsets had the same sum, then
> removing their common elements would leave two disjoint nonempty subsets with a common sum
> $t \geq 1$, so that $t$ and $2t$ would both be nonempty subset sums.

```lean
theorem erdos_882.variants.lower_bound_explicit (n : ℕ) (hn : 0 < n) :
    Real.logb 2 n - 1 < (maxAntichainCard n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/882.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/882.lean#L133).

## `Erdos882.erdos_882.variants.sandor`

Solved: stated here without proof.

> Sándor's construction (reported without reference in [Er98]) is claimed to achieve
> $\lvert A\rvert = (1-o(1))\log_2 n$ with $A = \{2^i + m 2^m : 0 \leq i < m\}$ and
> $n = 2^{m-1} + m 2^m$.

```lean
theorem erdos_882.variants.sandor (m : ℕ) (hm : 1 ≤ m) :
    IsSubsetSumAntichain ((Finset.range m).image (fun i => 2 ^ i + m * 2 ^ m))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/882.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/882.lean#L143).

## `Erdos882.erdos_882.variants.greedy`

Solved: stated here without proof.

> The greedy algorithm shows that $\lvert A\rvert \geq (1-o(1))\log_3 n$ is possible.

```lean
theorem erdos_882.variants.greedy :
    ∀ᶠ n : ℕ in Filter.atTop, (Real.logb 3 n - 1 : ℝ) ≤ (maxAntichainCard n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/882.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/882.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/882.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/882.lean)
- [erdosproblems.com/882](https://www.erdosproblems.com/882)
