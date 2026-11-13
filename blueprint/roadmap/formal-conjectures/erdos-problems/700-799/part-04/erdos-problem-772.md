---
declaration: theorem
origin: cited
lean: Erdos772.erdos_772.parts.i, Erdos772.erdos_772.parts.ii, Erdos772.erdos_772.variants.alon_erdos, Erdos772.erdos_772.variants.upper_bound
statement: formalized
---

# Erdős Problem 772

> *References:*
> - [erdosproblems.com/772](https://www.erdosproblems.com/772)
> - [Er80e] Erdős, P., _Some applications of Ramsey's theorem to additive number theory_. European
>   J. Combin. (1980), 43-46.
> - [Er84d] Erdős, P., _Extremal problems in number theory, combinatorics and geometry_. Proceedings
>   of the International Congress of Mathematicians, Vol. 1, 2 (Warsaw, 1983) (1984), 51-70.
> - [AlEr85] Alon, Noga and Erdős, P., _An application of graph theory to additive number theory_.
>   European J. Combin. (1985), 201-203.

*Quoted from [FormalConjectures/ErdosProblems/772.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/772.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/772](https://www.erdosproblems.com/772).

The file states 4 research or textbook statements: 4 solved.

## `Erdos772.erdos_772.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos772.lean#L1040](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos772.lean#L1040).

> Let $k\geq 1$ and $H_k(n)$ be the maximal $r$ such that if $A\subset\mathbb{N}$ has
> $\lvert A\rvert=n$ and $\| 1_A\ast 1_A\|_\infty \leq k$ then $A$ contains a Sidon set of size at
> least $r$.
>
> Is it true that $H_k(n)/n^{1/2}\to \infty$?
>
> The answer is yes, and in fact $H_k(n) \gg_k n^{2/3}$, proved by Alon and Erdős [AlEr85].

```lean
theorem erdos_772.parts.i :
    ∀ k ≥ 1, Tendsto (fun n : ℕ ↦ (H k n : ℝ) / √n) atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/772.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/772.lean#L60).

## `Erdos772.erdos_772.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos772.lean#L1040](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos772.lean#L1040).

> Is it true that $H_k(n) > n^{1/2+c}$ for some constant $c>0$?
>
> The answer is yes, and in fact $H_k(n) \gg_k n^{2/3}$, proved by Alon and Erdős [AlEr85].

```lean
theorem erdos_772.parts.ii :
    ∀ k ≥ 1, ∃ c > 0, ∀ᶠ n : ℕ in atTop, (n : ℝ) ^ (1 / 2 + c : ℝ) < H k n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/772.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/772.lean#L72).

## `Erdos772.erdos_772.variants.alon_erdos`

Solved: stated here without proof.

> Alon and Erdős [AlEr85] proved that $H_k(n) \gg_k n^{2/3}$.

```lean
theorem erdos_772.variants.alon_erdos (k : ℕ) (hk : 1 ≤ k) :
    ∃ c > 0, ∀ᶠ n : ℕ in atTop, c * (n : ℝ) ^ (2 / 3 : ℝ) ≤ H k n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/772.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/772.lean#L78).

## `Erdos772.erdos_772.variants.upper_bound`

Solved: stated here without proof.

> Erdős [Er84d] proved that $H_k(n) \ll n^{2/3}$, where the implied constant is absolute.
>
> Since $1_A\ast 1_A$ counts ordered pairs, the bound needs $k\geq 4$: the construction of
> Erdős has at most two unordered representations of each sum, hence at most four ordered ones,
> while $k\leq 2$ forces $A$ itself to be Sidon and so $H_k(n)=n$. For $k=3$ the only collisions
> are $a+b=2c$, so the Sidon subsets of $A$ are its $3$-term-progression-free subsets, which have
> size $n^{1-o(1)}$, and the bound fails there too.

```lean
theorem erdos_772.variants.upper_bound :
    ∃ C : ℝ, ∀ k ≥ 4, ∀ᶠ n : ℕ in atTop,
      (H k n : ℝ) ≤ C * (n : ℝ) ^ (2 / 3 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/772.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/772.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/772.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/772.lean)
- [erdosproblems.com/772](https://www.erdosproblems.com/772)
