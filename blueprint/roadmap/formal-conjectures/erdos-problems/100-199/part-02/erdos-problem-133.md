---
declaration: theorem
origin: cited
lean: Erdos133.erdos_133, Erdos133.erdos_133.variants.isTheta, Erdos133.erdos_133.variants.lower_bound, Erdos133.erdos_133.variants.hanson_seyffarth, Erdos133.erdos_133.variants.furedi_seress, Erdos133.erdos_133.variants.asymptotic
statement: formalized
---

# Erdős Problem 133

> *References:*
> - [erdosproblems.com/133](https://www.erdosproblems.com/133)
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*. Discrete
>   Math. (1997), 227-231.
> - [HaSe84] Hanson, D. and Seyffarth, K., *$k$-saturated graphs of prescribed maximum degree*.
>   Congr. Numer. (1984), 169-182.
> - [FuSe94] Füredi, Zoltán and Seress, Ákos, *Maximal triangle-free graphs with restrictions on the
>   degrees*. J. Graph Theory (1994), 11-24.
> - [HaLe18] Haviv, Ishay and Levy, Dan, *Symmetric complete sum-free sets in cyclic groups*. Israel
>   J. Math. (2018), 931-956.

*Quoted from [FormalConjectures/ErdosProblems/133.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/133](https://www.erdosproblems.com/133).

The file states 6 research or textbook statements: 1 open and 5 solved.

## `Erdos133.erdos_133`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos133.lean#L597](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos133.lean#L597).

> Let $f(n)$ be minimal such that every triangle-free graph $G$ with $n$ vertices and diameter
> $2$ contains a vertex with degree $\geq f(n)$. What is the order of growth of $f(n)$? Does
> $f(n)/\sqrt{n}\to \infty$?
>
> Asked by Erdős and Pach. The lower bound $f(n)\geq (1-o(1))\sqrt{n}$ follows from the fact that
> a graph with maximum degree $d$ and diameter $2$ has at most $1+d+d(d-1)=d^2+1$ many vertices.
>
> Hanson and Seyffarth [HaSe84] proved that $f(n)\leq (\sqrt{2}+o(1))\sqrt{n}$ using a Cayley graph
> on $\mathbb{Z}/n\mathbb{Z}$, with the generating set given by some symmetric complete sum-free set
> of size $\sim \sqrt{n}$. An alternative construction of such a complete sum-free set was given by
> Haviv and Levy [HaLe18]. Füredi and Seress [FuSe94] proved that
> $f(n)\leq (\frac{2}{\sqrt{3}}+o(1))\sqrt{n}$. In particular $f(n)/\sqrt{n}\not\to\infty$.
>
> The precise asymptotics of $f(n)$ are unknown; Alon believes that the truth is $f(n)\sim \sqrt{n}$.

```lean
theorem erdos_133 : ¬ Tendsto (fun n : ℕ ↦ (f n : ℝ) / √n) atTop atTop
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/133.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean#L68).

## `Erdos133.erdos_133.variants.isTheta`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos133.lean#L597](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos133.lean#L597).

> The order of growth of $f(n)$ is $\sqrt{n}$.

```lean
theorem erdos_133.variants.isTheta : (fun n : ℕ ↦ (f n : ℝ)) =Θ[atTop] fun n ↦ √n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/133.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean#L75).

## `Erdos133.erdos_133.variants.lower_bound`

Solved: stated here without proof.

> The lower bound $f(n)\geq (1-o(1))\sqrt{n}$ follows from the fact that a graph with maximum degree
> $d$ and diameter $2$ has at most $d^2+1$ many vertices.

```lean
theorem erdos_133.variants.lower_bound : ∀ ε : ℝ, 0 < ε →
    ∀ᶠ n : ℕ in atTop, (1 - ε) * √n ≤ f n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/133.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean#L83).

## `Erdos133.erdos_133.variants.hanson_seyffarth`

Solved: stated here without proof.

> Hanson and Seyffarth [HaSe84] proved that $f(n)\leq (\sqrt{2}+o(1))\sqrt{n}$.

```lean
theorem erdos_133.variants.hanson_seyffarth : ∀ ε : ℝ, 0 < ε →
    ∀ᶠ n : ℕ in atTop, (f n : ℝ) ≤ (√2 + ε) * √n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/133.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean#L89).

## `Erdos133.erdos_133.variants.furedi_seress`

Solved: stated here without proof.

> Füredi and Seress [FuSe94] proved that $f(n)\leq (\frac{2}{\sqrt{3}}+o(1))\sqrt{n}$.

```lean
theorem erdos_133.variants.furedi_seress : ∀ ε : ℝ, 0 < ε →
    ∀ᶠ n : ℕ in atTop, (f n : ℝ) ≤ (2 / √3 + ε) * √n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/133.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean#L95).

## `Erdos133.erdos_133.variants.asymptotic`

Open: stated without proof.

> Is $f(n)\sim \sqrt{n}$? Alon believes that this is the truth.

```lean
theorem erdos_133.variants.asymptotic :
    (fun n : ℕ ↦ (f n : ℝ)) ~[atTop] fun n ↦ √n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/133.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/133.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/133.lean)
- [erdosproblems.com/133](https://www.erdosproblems.com/133)
