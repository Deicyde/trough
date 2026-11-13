---
declaration: theorem
origin: cited
lean: Erdos865.erdos_865, Erdos865.erdos_865.variants.k2, Erdos865.erdos_865.variants.sos, Erdos865.erdos_865.variants.upper_bound
statement: formalized
---

# Erdős Problem 865

> *References:*
> - [erdosproblems.com/865](https://www.erdosproblems.com/865)
> - [CES75] Choi, S. L. G. and Erdős, P. and Szemerédi, E., Some additive and multiplicative problems
>   in number theory. Acta Arith. (1975), 37--50.
> - [Ci26] R. Cipollini, [A sharp $5/8$ bound for an Erdős–Sós pairwise-sums problem](https://arxiv.org/html/2606.29361)
>   (2026).

*Quoted from [FormalConjectures/ErdosProblems/865.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/865.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/865](https://www.erdosproblems.com/865).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos865.erdos_865`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/865/Erdos865.lean](https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/865/Erdos865.lean); a Lean proof is at [https://github.com/mrricky22/erdos-865-lean/blob/f861539107a7adeaa97462ce7c7171127696b63a/RequestProject/Main.lean#L45](https://github.com/mrricky22/erdos-865-lean/blob/f861539107a7adeaa97462ce7c7171127696b63a/RequestProject/Main.lean#L45).

> There exists a constant $C>0$ such that, for all large $N$, if $A\subseteq \{1,\ldots,N\}$ has
> size at least $\frac{5}{8}N+C$ then there are distinct $a,b,c\in A$ such that $a+b,a+c,b+c\in A$.
>
> A problem of Erdős and Sós (also earlier considered by Choi, Erdős, and Szemerédi [CES75], but Erdős
> had forgotten this).
>
> This problem was solved in the affirmative by Cipollini and GPT Pro [Ci26].
>
> This is true. The linked proof gives it in the contrapositive and with the constant cleared:
> every triple-free $A\subseteq\{1,\ldots,N\}$ satisfies $8\lvert A\rvert\leq 5N+C$ for a fixed
> $C$, for every $N$ rather than only for large $N$. It also shows the threshold is sharp, by
> exhibiting triple-free sets of size $(5N+16)/8$ for every $N$ divisible by $8$.

```lean
theorem erdos_865 :
    ∃ C > 0, ∀ᶠ (N : ℕ) in atTop,
      ∀ A ⊆ Icc 1 N, A.card ≥ (5 / 8 : ℝ) * N + C →
      ∃ a ∈ A, ∃ b ∈ A, ∃ c ∈ A, a ≠ b ∧ a ≠ c ∧ b ≠ c ∧
      a + b ∈ A ∧ a + c ∈ A ∧ b + c ∈ A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/865.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/865.lean#L56).

## `Erdos865.erdos_865.variants.k2`

Proved here.

> It is a classical folklore fact that if $A\subseteq \{1,\ldots,2N\}$ has size $\geq N+2$ then
> there are distinct $a,b\in A$ such that $a+b\in A$, which establishes the $k=2$ case.

```lean
theorem erdos_865.variants.k2 (N : ℕ) :
    ∀ A ⊆ Icc 1 (2 * N), A.card ≥ N + 2 →
    ∃ a ∈ A, ∃ b ∈ A, a ≠ b ∧ a + b ∈ A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/865.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/865.lean#L68).

## `Erdos865.erdos_865.variants.sos`

Open: stated without proof.

> Erdős and Sós conjectured that
> $f_k(N)\sim \frac{1}{2}\left(1+\sum_{1\leq r\leq k-2}\frac{1}{4^r}\right) N$,
> where $f_k(N)$ is the minimal size of a subset of $\{1, \dots, N\}$ guaranteeing $k$ elements
> have all pairwise sums in the set.

```lean
theorem erdos_865.variants.sos :
    ∀ᵉ (k : ℕ) (hk : 2 ≤ k),
    (fun N ↦ (f N k : ℝ)) ~[atTop] (fun N ↦ (1 / 2 : ℝ) * (1 + ∑ r ∈ Icc 1 (k - 2),
      (1 / 4 : ℝ) ^ r) * N)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/865.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/865.lean#L112).

## `Erdos865.erdos_865.variants.upper_bound`

Solved: stated here without proof.

> Choi, Erdős, and Szemerédi [CES75] have proved that, for all $k\geq 3$, there exists $\epsilon_k>0$
> such that (for large enough $N$) $f_k(N)\leq \left(\frac{2}{3}-\epsilon_k\right)N$.

```lean
theorem erdos_865.variants.upper_bound (k : ℕ) (hk : 3 ≤ k) :
    ∃ ε > 0, ∀ᶠ N in atTop, (f N k : ℝ) ≤ (2 / 3 - ε) * N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/865.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/865.lean#L123).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/865.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/865.lean)
- [erdosproblems.com/865](https://www.erdosproblems.com/865)
