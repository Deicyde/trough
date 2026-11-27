---
declaration: theorem
origin: cited
lean: ChowlaLiouvilleConjecture.chowla_liouville_conjecture, ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.one_point, ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.averaged_two_point, ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.averaged_two_point_uniform, ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.logarithmic_two_point
statement: formalized
---

# Chowla's Conjecture on Correlations of the Liouville Function

> For $n \ge 1$, the Liouville function $\lambda(n) = (-1)^{\Omega(n)}$
> (`ArithmeticFunction.liouville`) records the parity of the prime-factor count $\Omega(n)$ with
> multiplicity. In [Ch65, p. 96], Sarvadaman Chowla conjectured that $\sum_{n=1}^N \lambda(f(n)) =
> o(N)$ for every integer polynomial $f(x) \in \mathbb{Z}[x]$ not of the form $c g(x)^2$. Specializing
> to products of distinct linear factors $f(x) = \prod_{i=1}^k (x + h_i)$ yields the linear-shift
> correlation conjecture formalized here: for every $k \ge 1$ and any injective tuple of nonnegative
> shifts $h_1, \dots, h_k$, the Cesàro average $\frac{1}{N} \sum_{n=1}^N \prod_{i=1}^k \lambda(n +
> h_i)$ tends to $0$ as $N \to \infty$. Wikipedia's *Nilsequence* article mentions Chowla's conjecture
> qualitatively via its nilsequence equivalence without giving the correlation formula; the statements
> below follow [Ch65], Matomäki–Radziwiłł–Tao [MRT15], and Tao [Ta16]. Unweighted $k$-point
> correlations remain open for every $k \ge 2$.
>
> *References:*
> - [Ch65] S. Chowla, *The Riemann Hypothesis and Hilbert's Tenth Problem*, Gordon and Breach,
>   New York, 1965, p. 96.
> - [MRT15] K. Matomäki, M. Radziwiłł, and T. Tao, *An averaged form of Chowla's conjecture*,
>   Algebra & Number Theory **9** (2015), no. 9, 2167–2196.
> - [Ta16] T. Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point
>   correlations*, Forum Math. Pi **4** (2016), e8, 1–36.
> - [La09] E. Landau, *Handbuch der Lehre von der Verteilung der Primzahlen*, Vol. 2, Teubner,
>   Leipzig, 1909, §157.
> - [Wikipedia: Nilsequence](https://en.wikipedia.org/wiki/Nilsequence#Equivalent_form_for_averaged_Chowla_and_Sarnak_conjectures)

*Quoted from [FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open, 3 solved and 1 textbook result.

## `ChowlaLiouvilleConjecture.chowla_liouville_conjecture`

Open: stated without proof.

> **Chowla's Conjecture** [Ch65, p. 96]: for every $k \ge 1$ and every injective shift tuple
> `h : Fin k → ℕ`, the Cesàro average $\frac{1}{N} \sum_{n=1}^N \prod_{i < k} \lambda(n + h_i)$
> tends to $0$ as $N \to \infty$. This linear-shift correlation is the special case
> $f(x) = \prod_{i < k} (x + h_i)$ of Chowla's polynomial conjecture [Ch65]. The hypothesis `1 ≤ k`
> excludes the empty product $1$, and injectivity excludes repeated factors $\lambda(n + h)^2 = 1$.

```lean
theorem chowla_liouville_conjecture (k : ℕ) (hk : 1 ≤ k) (h : Fin k → ℕ)
    (hh : Function.Injective h) :
    Filter.Tendsto
      (fun N : ℕ ↦
        (∑ n ∈ Finset.Icc 1 N, ∏ i : Fin k, (ArithmeticFunction.liouville (n + h i) : ℝ)) /
          (N : ℝ))
      Filter.atTop (nhds 0)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean#L57).

## `ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.one_point`

Textbook result, stated without proof.

> **One-Point Liouville Average** [La09]: the $k = 1$ case
> $\frac{1}{N} \sum_{n=1}^N \lambda(n) \to 0$, equivalent to PNT.

```lean
theorem chowla_liouville_conjecture.variants.one_point :
    Filter.Tendsto
      (fun N : ℕ ↦ (∑ n ∈ Finset.Icc 1 N, (ArithmeticFunction.liouville n : ℝ)) / (N : ℝ))
      Filter.atTop (nhds 0)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean#L69).

## `ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.averaged_two_point`

Solved: stated here without proof.

> **Shift-Averaged Two-Point Chowla Theorem** [MRT15, Theorem 1.1, eq. (1-3)]: the average over
> shifts $1 \le h \le H$ of $\left|\frac{1}{N} \sum_{n=1}^N \lambda(n)\lambda(n + h)\right|$ becomes
> arbitrarily small for sufficiently large $H$ and $N$. Because `∀ᶠ H, ∀ᶠ N` lets the threshold for
> $N$ depend on $H$, this fixed-$H$-threshold statement is weaker than [MRT15]'s uniform bound across
> growing scales $H = H(N) \le N$ (see `averaged_two_point_uniform`).

```lean
theorem chowla_liouville_conjecture.variants.averaged_two_point (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ H : ℕ in Filter.atTop, ∀ᶠ N : ℕ in Filter.atTop,
      (∑ h ∈ Finset.Icc 1 H,
        |∑ n ∈ Finset.Icc 1 N,
          (ArithmeticFunction.liouville n * ArithmeticFunction.liouville (n + h) : ℝ)| /
            (N : ℝ)) / (H : ℝ) < ε
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean#L81).

## `ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.averaged_two_point_uniform`

Solved: stated here without proof.

> **Uniform Shift-Averaged Two-Point Chowla Theorem** [MRT15, Theorem 1.1, eq. (1-3)]: for any
> shift scale `H : ℕ → ℕ` with $H(N) \to \infty$ and $H(N) \le N$ eventually, the average over
> $1 \le h \le H(N)$ of $\left|\frac{1}{N} \sum_{n=1}^N \lambda(n)\lambda(n + h)\right|$ tends to $0$
> as $N \to \infty$.

```lean
theorem chowla_liouville_conjecture.variants.averaged_two_point_uniform
    (H : ℕ → ℕ) (hH_top : Filter.Tendsto H Filter.atTop Filter.atTop)
    (hH_le : ∀ᶠ N : ℕ in Filter.atTop, H N ≤ N) :
    Filter.Tendsto
      (fun N : ℕ ↦
        (∑ h ∈ Finset.Icc 1 (H N),
          |∑ n ∈ Finset.Icc 1 N,
            (ArithmeticFunction.liouville n * ArithmeticFunction.liouville (n + h) : ℝ)| /
              (N : ℝ)) / (H N : ℝ))
      Filter.atTop (nhds 0)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean#L94).

## `ChowlaLiouvilleConjecture.chowla_liouville_conjecture.variants.logarithmic_two_point`

Solved: stated here without proof.

> **Logarithmically Averaged Two-Point Chowla Theorem** [Ta16]: for every shift $a \ge 1$,
> $\frac{1}{\log N} \sum_{n=1}^N \frac{\lambda(n)\lambda(n + a)}{n} \to 0$ as $N \to \infty$.

```lean
theorem chowla_liouville_conjecture.variants.logarithmic_two_point (a : ℕ) (ha : 1 ≤ a) :
    Filter.Tendsto
      (fun N : ℕ ↦
        (∑ n ∈ Finset.Icc 1 N,
          (ArithmeticFunction.liouville n * ArithmeticFunction.liouville (n + a) : ℝ) / (n : ℝ)) /
            Real.log (N : ℝ))
      Filter.atTop (nhds 0)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean#L109).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/ChowlaLiouvilleConjecture.lean)
- [Wikipedia: Nilsequence](https://en.wikipedia.org/wiki/Nilsequence#Equivalent_form_for_averaged_Chowla_and_Sarnak_conjectures)
