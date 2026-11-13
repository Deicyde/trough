---
declaration: theorem
origin: cited
lean: Erdos1194.erdos_1194, Erdos1194.erdos_1194.variants.exists_perfect_difference_set, Erdos1194.erdos_1194.variants.greedy_upper_bound, Erdos1194.erdos_1194.variants.limsup_eq_top
statement: formalized
---

# Erdős Problem 1194

> *References:*
> - [erdosproblems.com/1194](https://www.erdosproblems.com/1194)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   6 (1980), 89-115. [PDF](https://www.renyi.hu/~p_erdos/1980-03.pdf)
> - [HaRo66] Halberstam, H. and Roth, K. F., *Sequences. Vol. I*. Oxford University Press, Oxford
>   (1966), xx+291.
> - [Le04] Lev, Vsevolod F., *Reconstructing integer sets from their representation functions*.
>   Electron. J. Combin. 11 (2004), Research Paper 78, 6 pp.
>   [Link](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i1r78)

*Quoted from [FormalConjectures/ErdosProblems/1194.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1194.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1194](https://www.erdosproblems.com/1194).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 3 API statements, counted here but not shown.

## `Erdos1194.erdos_1194`

Open: stated without proof.

> Let $A\subset\mathbb{N}$ be such that every integer $n\geq 1$ can be written uniquely as
> $a_n-b_n$ for some $a_n,b_n\in A$. How fast must $a_n/n$ increase?
>
> A question of Erdős [Er80, p. 100]. Here $a_n$ is the larger element of the representation of
> $n$, not the $n$th element of $A$. We read "must increase" as: the answer is the set of
> non-decreasing $G$ such that every such $A$ has $a_n \geq c\,n\,G(n)$ for infinitely many $n$,
> for some $c>0$ depending on $A$.

```lean
theorem erdos_1194 :
    {G : ℕ → ℝ | Monotone G ∧ ∀ A : Set ℕ, IsPerfectDifferenceSetInt A →
      ∃ c > (0 : ℝ), HasLargeElement A (fun n ↦ c * G n * n)} = erdos_1194.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1194.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1194.lean#L100).

## `Erdos1194.erdos_1194.variants.exists_perfect_difference_set`

Solved: stated here without proof.

> Such a set is called a perfect difference set; they can be constructed, for example, by a greedy
> approach (as detailed by Lev [Le04]).
>
> Erdős [Er80, p. 100] remarks that it is easy to construct such a sequence, and [Le04, Section 3]
> constructs a perfect difference set $A\subseteq\mathbb{N}$ (positive integers) greedily.

```lean
theorem erdos_1194.variants.exists_perfect_difference_set :
    ∃ A : Set ℕ, IsPerfectDifferenceSetInt A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1194.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1194.lean#L113).

## `Erdos1194.erdos_1194.variants.greedy_upper_bound`

Solved: stated here without proof.

> The greedy construction achieves $a_n\ll n^3$.
>
> In the greedy construction of [Le04, Section 3], step $k$ adds $z_k$ and $z_k+d_k$, where $d_k$ is
> the least non-negative integer that is not yet a difference and $z_k$ is the least admissible
> positive integer. There are $O(k^3)$ excluded choices for $z_k$ and $d_k=O(k^2)$, so every element
> added by step $k$ is $O(k^3)$. As $d_1=0$ and the $d_k$ increase, $n$ is represented by step
> $n+1$, which gives $a_n\ll n^3$.

```lean
theorem erdos_1194.variants.greedy_upper_bound :
    ∃ A : Set ℕ, IsPerfectDifferenceSetInt A ∧ ∃ C : ℝ, ∀ n : ℕ, 0 < n →
      ∀ a, IsLargerElement A n a → (a : ℝ) ≤ C * (n : ℝ) ^ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1194.lean, line 127](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1194.lean#L127).

## `Erdos1194.erdos_1194.variants.limsup_eq_top`

Solved: stated here without proof.

> Erdős [Er80, p. 100] wrote it is 'easy to see' that
>
> $$\limsup_{n\to \infty}\frac{a_n}{n}=\infty.$$
>
> Indeed, since $A$ must be a Sidon set, if $a_n \leq f(n)n$ for all $n$, then all differences in
> $[1,x/f(x)]$ can be realised by differences from $A\cap [1,x]$, and hence
> $\lvert A\cap [1,x]\rvert^2 \gg x/f(x)$. Erdős (see for example [HaRo66]) proved that for
> infinitely many $x$, $\lvert A\cap [1,x]\rvert \ll (x/\log x)^{1/2}$, which is a contradiction for
> a suitable choice of $f$.
>
> Formally: for every perfect difference set $A$ and every $C$, $a_n \geq Cn$ for infinitely many
> $n$.

```lean
theorem erdos_1194.variants.limsup_eq_top :
    ∀ A : Set ℕ, IsPerfectDifferenceSetInt A → ∀ C : ℝ, HasLargeElement A (fun n ↦ C * n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1194.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1194.lean#L145).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1194.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1194.lean)
- [erdosproblems.com/1194](https://www.erdosproblems.com/1194)
