---
declaration: theorem
origin: cited
lean: Erdos1189.erdos_1189.parts.i, Erdos1189.erdos_1189.parts.ii, Erdos1189.erdos_1189.parts.iii, Erdos1189.erdos_1189.parts.iv, Erdos1189.erdos_1189.variants.sun, Erdos1189.erdos_1189.variants.simpson, Erdos1189.erdos_1189.variants.bbmst
statement: formalized
---

# Erdős Problem 1189

> *References:*
> - [erdosproblems.com/1189](https://www.erdosproblems.com/1189)
> - [Er80] Erdős, P., *A survey of problems in combinatorial number theory*. Ann. Discrete Math. 6
>   (1980), 89-115. [PDF](https://www.renyi.hu/~p_erdos/1980-03.pdf)
> - [Si85] Simpson, R. J., *Regular coverings of the integers by arithmetic progressions*. Acta Arith.
>   45 (1985), 145-152.
> - [Su07] Sun, Z.-W., *On covering numbers*. Combinatorial Number Theory, de Gruyter (2007),
>   443-453. [arXiv:math/0601017](https://arxiv.org/abs/math/0601017)
> - [BBMST24] Balister, P., Bollobás, B., Morris, R., Sahasrabudhe, J. and Tiba, M., *The structure
>   and number of Erdős covering systems*. J. Eur. Math. Soc. 26 (2024), 75-109.
>   [arXiv:1904.04806](https://arxiv.org/abs/1904.04806)
>
> See also [erdosproblems.com/1188](https://www.erdosproblems.com/1188), which counts minimal
> covering systems with bounded moduli.

*Quoted from [FormalConjectures/ErdosProblems/1189.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1189](https://www.erdosproblems.com/1189).

The file states 7 research or textbook statements: 3 open and 4 solved. It also has 1 test statement, counted here but not shown.

## `Erdos1189.erdos_1189.parts.i`

Open: stated without proof.

> Call a set of distinct integers $1\lt n_1\lt \cdots\lt n_k$ a covering set if there is a choice of
> $a_i\pmod{n_i}$ for $1\leq i\leq k$ such that every integer satisfies at least one of these
> congruences. A set is an irreducible covering set if no proper subset is a covering set.
>
> How many irreducible covering sets of size $k$ are there?
>
> This is the first part of the questions of Erdős [Er80, p. 95]. We read "how many" as asking for
> the asymptotics of $\log I(k)$, where $I(k)$ is the number of irreducible covering sets of size
> $k$; this is the scale on which the number of minimal covering systems is known [BBMST24].

```lean
theorem erdos_1189.parts.i :
    (fun k : ℕ ↦ Real.log (irreducibleCount k : ℝ)) ~[atTop] erdos_1189.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1189.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean#L93).

## `Erdos1189.erdos_1189.parts.ii`

Open: stated without proof.

> Call a set of distinct integers $1\lt n_1\lt \cdots\lt n_k$ a covering set if there is a choice of
> $a_i\pmod{n_i}$ for $1\leq i\leq k$ such that every integer satisfies at least one of these
> congruences. A set is an irreducible covering set if no proper subset is a covering set.
>
> What is the minimum and maximum that $n_k$ can be?
>
> This is the second part. Here $n_k$ is the largest element of an irreducible covering set of
> size $k$. The answer is a pair (minimum, maximum), stated for each $k$ for which an irreducible
> covering set of size $k$ exists.

```lean
theorem erdos_1189.parts.ii (k : ℕ)
    (hk : ∃ M : Finset ℕ, IsIrreducibleCoveringSet M ∧ M.card = k) :
    IsLeast (largestModulus k) (erdos_1189.parts.ii.answer k).1 ∧
      IsGreatest (largestModulus k) (erdos_1189.parts.ii.answer k).2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1189.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean#L111).

## `Erdos1189.erdos_1189.parts.iii`

Open: stated without proof.

> Call a set of distinct integers $1\lt n_1\lt \cdots\lt n_k$ a covering set if there is a choice of
> $a_i\pmod{n_i}$ for $1\leq i\leq k$ such that every integer satisfies at least one of these
> congruences. A set is an irreducible covering set if no proper subset is a covering set.
>
> Determine or estimate $\max \sum\frac{1}{n_i}$, where the maximum ranges over all irreducible
> covering sets of size $k$.
>
> This is the third part. We read "determine or estimate" as an estimate up to constant factors.
> In [Er80, p. 95] the maximum is taken over the irreducible covering sets
> $1\lt n_1\lt \cdots\lt n_k\leq x$, as a function of $x$; we follow the problem page, which takes it over
> the irreducible covering sets of size $k$.

```lean
theorem erdos_1189.parts.iii :
    maxReciprocalSum =Θ[atTop] erdos_1189.parts.iii.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1189.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean#L133).

## `Erdos1189.erdos_1189.parts.iv`

Solved: stated here without proof.

> Call a set of distinct integers $1\lt n_1\lt \cdots\lt n_k$ a covering set if there is a choice of
> $a_i\pmod{n_i}$ for $1\leq i\leq k$ such that every integer satisfies at least one of these
> congruences. A set is an irreducible covering set if no proper subset is a covering set.
>
> Are there infinitely many $n$ such that the divisors of $n$ (which are $>1$) form an irreducible
> covering set?
>
> This is the fourth part. Sun [Su07, Theorem 1.4(i) and Corollary 1.3] proved that the answer is
> yes: see `erdos_1189.variants.sun`.

```lean
theorem erdos_1189.parts.iv :
    {n : ℕ | IsIrreducibleCoveringSet (n.divisors.filter (1 < ·))}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1189.lean, line 149](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean#L149).

## `Erdos1189.erdos_1189.variants.sun`

Solved: stated here without proof.

> The divisors of $12$ (which are $>1$) are an example of an irreducible covering set. Sun [Su07]
> proved more generally that, for any odd prime $p$, the divisors (which are $>1$) of $2^{p-1}p$
> form an irreducible covering set, settling the final question.
>
> That $n=12$ is an example is already noted in [Er80, p. 95].

```lean
theorem erdos_1189.variants.sun (p : ℕ) (hp : p.Prime) (hodd : Odd p) :
    IsIrreducibleCoveringSet ((2 ^ (p - 1) * p).divisors.filter (1 < ·))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1189.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean#L161).

## `Erdos1189.erdos_1189.variants.simpson`

Solved: stated here without proof.

> Simpson [Si85] proved $n_k\leq 2^{k-1}$.
>
> Here $n_k$ is the largest element of an irreducible covering set of size $k$. The bound follows
> from Simpson's theorem [Si85] (see [BBMST24, Theorem 2.4]), as stated in [BBMST24, Section 1].

```lean
theorem erdos_1189.variants.simpson (M : Finset ℕ) (hM : IsIrreducibleCoveringSet M) :
    ∀ n ∈ M, n ≤ 2 ^ (M.card - 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1189.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean#L172).

## `Erdos1189.erdos_1189.variants.bbmst`

Solved: stated here without proof.

> Let $I(k)$ count the number of irreducible covering sets of size $k$. Balister, Bollobás, Morris,
> Sahasrabudhe, and Tiba [BBMST24] proved that
>
> $$I(k) \leq \exp\left((c+o(1))\frac{k^{3/2}}{(\log k)^{1/2}}\right)$$
>
> by proving that the right-hand side is an asymptotic for the number of minimal covering systems
> on $k$ moduli.
>
> Here $c = 4\sqrt{\tau}/3$ [BBMST24, Theorem 1.1]. The bound for $I(k)$ follows because each
> irreducible covering set is the set of moduli of a minimal covering system. The $o(1)$ is stated
> with an arbitrary $\varepsilon > 0$.

```lean
theorem erdos_1189.variants.bbmst (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ k : ℕ in atTop, (irreducibleCount k : ℝ) ≤
      Real.exp ((4 * Real.sqrt bbmstTau / 3 + ε) *
        ((k : ℝ) ^ (3 / 2 : ℝ) / Real.sqrt (Real.log k)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1189.lean, line 192](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean#L192).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1189.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1189.lean)
- [erdosproblems.com/1189](https://www.erdosproblems.com/1189)
