---
declaration: theorem
origin: cited
lean: Erdos83.erdos_83, Erdos83.erdos_83.variants.extremal, Erdos83.erdos_83.variants.ahlswede_khachatrian
statement: formalized
---

# Erdős Problem 83

> *References:*
> - [erdosproblems.com/83](https://www.erdosproblems.com/83)
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*.
>   Eureka (1992), 44-48.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [ErKoRa61] Erdős, P. and Ko, Chao and Rado, R., *Intersection theorems for systems of finite
>   sets*. Quart. J. Math. Oxford Ser. (2) (1961), 313-320.
> - [AhKh97] Ahlswede, Rudolf and Khachatrian, Levon H., *The complete intersection theorem for
>   systems of finite sets*. European J. Combin. (1997), 125-136.

*Quoted from [FormalConjectures/ErdosProblems/83.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/83.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/83](https://www.erdosproblems.com/83).

The file states 3 research or textbook statements: 3 solved.

## `Erdos83.erdos_83`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos83.lean#L36](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos83.lean#L36).

> Suppose that we have a family $\mathcal{F}$ of subsets of $[4n]$ such that $\lvert A\rvert=2n$
> for all $A\in\mathcal{F}$ and for every $A,B\in \mathcal{F}$ we have
> $\lvert A\cap B\rvert \geq 2$. Then
> $$\lvert \mathcal{F}\rvert \leq \frac{1}{2}\left(\binom{4n}{2n}-\binom{2n}{n}^2\right).$$
>
> Conjectured by Erdős, Ko, and Rado [ErKoRa61]. This inequality would be best possible, as shown
> by taking $\mathcal{F}$ to be the collection of all subsets of $[4n]$ of size $2n$ containing at
> least $n+1$ elements from $[2n]$.
>
> Proved by Ahlswede and Khachatrian [AhKh97], who more generally showed the following. Let
> $2\leq t\leq k\leq m$ and let $r\geq 0$ be such that
> $$\frac{1}{r+1}\leq \frac{m-2k+2t-2}{(t-1)(k-t+1)}< \frac{1}{r}.$$
> The largest possible family of subsets of $[m]$ of size $k$, such that the pairwise
> intersections have size at least $t$, is the family of all subsets of $[m]$ of size $k$ which
> contain at least $t+r$ elements from $\{1,\ldots,t+2r\}$.
>
> The number $\binom{4n}{2n}-\binom{2n}{n}^2$ is even, so the bound is an integer.

```lean
theorem erdos_83 (n : ℕ) (F : Finset (Finset (Fin (4 * n)))) (hF : ∀ A ∈ F, A.card = 2 * n)
    (hinter : ∀ A ∈ F, ∀ B ∈ F, 2 ≤ (A ∩ B).card) :
    F.card ≤ ((4 * n).choose (2 * n) - (2 * n).choose n ^ 2) / 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/83.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/83.lean#L65).

## `Erdos83.erdos_83.variants.extremal`

Solved: stated here without proof.

> The bound in [erdős_83](https://www.erdosproblems.com/83) is attained by the family of all
> subsets of $[4n]$ of size $2n$ containing at least $n+1$ elements from $[2n]$.

```lean
theorem erdos_83.variants.extremal (n : ℕ) :
    ∃ F : Finset (Finset (Fin (4 * n))), (∀ A ∈ F, A.card = 2 * n) ∧
      (∀ A ∈ F, ∀ B ∈ F, 2 ≤ (A ∩ B).card) ∧
      F.card = ((4 * n).choose (2 * n) - (2 * n).choose n ^ 2) / 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/83.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/83.lean#L75).

## `Erdos83.erdos_83.variants.ahlswede_khachatrian`

Solved: stated here without proof.

> The complete intersection theorem of Ahlswede and Khachatrian [AhKh97]: for $2\leq t\leq k\leq m$,
> every family of $k$-subsets of $[m]$ with pairwise intersections of size at least $t$ is at most
> as large as one of the families of all $k$-subsets of $[m]$ containing at least $t+r$ elements of
> $\{1,\ldots,t+2r\}$, $r \geq 0$.

```lean
theorem erdos_83.variants.ahlswede_khachatrian (m k t : ℕ) (ht : 2 ≤ t) (htk : t ≤ k)
    (hkm : k ≤ m) (F : Finset (Finset (Fin m))) (hF : ∀ A ∈ F, A.card = k)
    (hinter : ∀ A ∈ F, ∀ B ∈ F, t ≤ (A ∩ B).card) :
    ∃ r : ℕ, F.card ≤ ({A : Finset (Fin m) | A.card = k ∧
      t + r ≤ (A.filter fun i : Fin m => (i : ℕ) < t + 2 * r).card} : Finset _).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/83.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/83.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/83.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/83.lean)
- [erdosproblems.com/83](https://www.erdosproblems.com/83)
