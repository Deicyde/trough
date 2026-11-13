---
declaration: theorem
origin: cited
lean: Erdos291.erdos_291.parts.i, Erdos291.erdos_291.parts.ii, Erdos291.erdos_291.variants.steinerberger_generalization, Erdos291.erdos_291.variants.shiu_heuristic_asymptotic, Erdos291.erdos_291.variants.shiu_heuristic_density_zero, Erdos291.erdos_291.variants.wu_yan
statement: formalized
---

# Erdős Problem 291

> *References:*
> - [erdosproblems.com/291](https://www.erdosproblems.com/291)
> - [ErGr80, p.34] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
>   theory. Monographies de L'Enseignement Mathematique (1980).
> - [Sh16] P. Shiu, The denominators of harmonic numbers. arXiv:1607.02863 (2016).
> - [WuYa22] Wu, Bing-Ling and Yan, Xiao-Hui, On the denominators of harmonic numbers. {IV}. C. R.
>   Math. Acad. Sci. Paris (2022), 53--57.

*Quoted from [FormalConjectures/ErdosProblems/291.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/291](https://www.erdosproblems.com/291).

The file states 6 research or textbook statements: 3 open and 3 solved. It also has 2 test statements, counted here but not shown.

## `Erdos291.erdos_291.parts.i`

Open: stated without proof.

> Let $n\geq 1$ and define $L_n$ to be the least common multiple of $\{1,\ldots,n\}$ and $a_n$ by
> $\sum_{1\leq k\leq n}\frac{1}{k}=\frac{a_n}{L_n}$.
>
> Is it true that $(a_n,L_n)=1$ occurs for infinitely many $n$?

```lean
theorem erdos_291.parts.i :
    { n : ℕ | Nat.gcd (a n) (L n) = 1 }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/291.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean#L63).

## `Erdos291.erdos_291.parts.ii`

Solved: stated here without proof.

> Is it true that $(a_n,L_n)>1$ occurs for infinitely many $n$?
>
> Steinerberger has observed that the answer to the second question is trivially yes: for example, any
> $n$ which begins with a $2$ in base $3$ has $3\mid (a_n,L_n)$.

```lean
theorem erdos_291.parts.ii :
    { n : ℕ | Nat.gcd (a n) (L n) > 1 }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/291.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean#L74).

## `Erdos291.erdos_291.variants.steinerberger_generalization`

Solved: stated here without proof.

> More generally, if the leading digit of $n$ in base $p$ is $p-1$ then $p\mid (a_n,L_n)$. There is
> in fact a necessary and sufficient condition: a prime $p\leq n$ divides $(a_n,L_n)$ if and only if
> $p$ divides the numerator of $1+\cdots+\frac{1}{k}$, where $k$ is the leading digit of $n$ in base
> $p$. This can be seen by writing $a_n = \frac{L_n}{1}+\cdots+\frac{L_n}{n}$ and observing that the
> right-hand side is congruent to $1+\cdots+1/k$ modulo $p$. (The previous claim about $p-1$ follows
> immediately from Wolstenholme's theorem.)

```lean
theorem erdos_291.variants.steinerberger_generalization (n p : ℕ) (hp : p.Prime) (hpn : p ≤ n) :
    let k := n / p ^ Nat.log p n;
    p ∣ Nat.gcd (a n) (L n) ↔ (p : ℤ) ∣ (∑ i ∈ Finset.Icc 1 k, (1 : ℚ) / i).num
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/291.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean#L87).

## `Erdos291.erdos_291.variants.shiu_heuristic_asymptotic`

Open: stated without proof.

> This leads to a heuristic prediction (see for example a preprint of Shiu [Sh16]) of
> $\asymp\frac{x}{\log x}$ for the number of $n\in [1,x]$ such that $(a_n,L_n)=1$.

```lean
theorem erdos_291.variants.shiu_heuristic_asymptotic :
    Asymptotics.IsTheta atTop
      (fun x : ℕ ↦ ((((Finset.Icc 1 x).filter (fun n ↦ Nat.gcd (a n) (L n) = 1)).card : ℝ)))
      (fun x : ℕ ↦ (x : ℝ) / Real.log x)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/291.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean#L97).

## `Erdos291.erdos_291.variants.shiu_heuristic_density_zero`

Open: stated without proof.

> In particular, there should be infinitely many $n$, but the set of such $n$ should have
> density zero. Unfortunately this heuristic is difficult to turn into a proof.

```lean
theorem erdos_291.variants.shiu_heuristic_density_zero :
    Filter.Tendsto (fun N : ℕ ↦
      ((((Finset.Icc 1 N).filter (fun n ↦ Nat.gcd (a n) (L n) = 1)).card : ℝ) / (N : ℝ)))
      atTop (nhds 0)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/291.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean#L108).

## `Erdos291.erdos_291.variants.wu_yan`

Solved: stated here without proof.

> Wu and Yan [WuYa22] have proved, conditional on $\frac{1}{\log p}$ being linearly independent
> over $\mathbb{Q}$ for any finite collection of primes $p$ (itself a consequence of Schanuel's
> conjecture), that the set of $n$ for which $(a_n,L_n)>1$ has upper density $1$.

```lean
theorem erdos_291.variants.wu_yan
    (h_indep : LinearIndependent ℚ (fun p : {p : ℕ // p.Prime} ↦ 1 / Real.log (p : ℝ))) :
    atTop.limsup (fun N : ℕ ↦
      ((((Finset.Icc 1 N).filter (fun n ↦ Nat.gcd (a n) (L n) > 1)).card : ℝ) /
        (N : ℝ) : EReal)) = 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/291.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/291.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/291.lean)
- [erdosproblems.com/291](https://www.erdosproblems.com/291)
