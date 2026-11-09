---
declaration: theorem
origin: cited
lean: Green31.green_31.lower, Green31.green_31.variants.lower_eventually, Green31.green_31.upper, Green31.green_31.variants.upper_eventually, Green31.green_31.variants.upper_li69, Green31.green_31.variants.upper_bfr23, Green31.green_31.variants.upper_cho25, Green31.green_31.variants.upper_hz26, Green31.green_31.variants.zmod_p, Green31.green_31.variants.abelian, Green31.green_31.variants.sidon_01n, Green31.green_31.variants.sidon_01n_clz01
statement: formalized
---

# Ben Green's Open Problem 31

> Write $F(N)$ for the largest Sidon subset of $[N]$.
> Improve, at least for infinitely many $N$, the bounds $N^{1/2} + O(1) \le F(N) \le N^{1/2} + N^{1/4} + O(1)$.
>
> Note: the upper bound was improved to $N^{1/2} + 0.98183 N^{1/4} + O(1)$ in [CHO25], and then to
> $N^{1/2} + 0.94349\ldots N^{1/4} + O(1)$ in [HZ26].
>
> Related to Erdős Problem 30.
>
> *References:*
> - [Gr24] [Ben Green's Open Problem 31](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.7 Problem 31)
> - [Gr01] Green, Ben. "The number of squares and $ B_h [g] $ sets."
>   Acta Arithmetica 100.4 (2001): 365-390.
> - [BFR23] Balogh, József, Zoltán Füredi, and Souktik Roy. "An upper bound on the size of Sidon sets."
>   The American Mathematical Monthly 130.5 (2023): 437-445.
> - [CHO25] Carter, Daniel, Zach Hunter, and Kevin O’Bryant. "On the diameter of finite Sidon sets."
>   Acta Mathematica Hungarica 175.1 (2025): 108-126.
> - [HZ26] Hou, Jianfeng, and Hongbin Zhao. "An Improved Upper Bound for Finite Sidon Sets via
>   Vector-Valued Smoothing." [arXiv:2607.01169](https://arxiv.org/abs/2607.01169) (2026).
> - [ET41] Erdos, Paul, and Pál Turán. "On a problem of Sidon in additive number theory, and on some
>   related problems." J. London Math. Soc 16.4 (1941): 212-215.
> - [Li69] Lindström, Bernt. “A remark on B4-Sequences.” Journal of Combinatorial Theory,
>   Series A 7 (1969): 276-277.
> - [CLZ01] Cohen, G.D., Litsyn, S., & Zémor, G. (2001). Binary B2-Sequences : A New Upper Bound.
>   J. Comb. Theory A, 94, 152-155.
> - [BS85] Babai, László, and Vera T. Sós. "Sidon sets in groups and induced subgraphs of Cayley
>   graphs." European Journal of Combinatorics 6.2 (1985): 101-114.
>   [doi:10.1016/S0195-6698(85)80001-9](https://doi.org/10.1016/S0195-6698%2885%2980001-9)

*Quoted from [FormalConjectures/GreensOpenProblems/31.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 12 research or textbook statements: 7 open and 5 solved. It also has 2 test statements and 3 API statements, counted here but not shown.

## `Green31.green_31.lower`

Open: stated without proof.

> Can we improve the lower bound $N^{1/2} + O(1)$, at least for infinitely many $N$?

```lean
theorem green_31.lower :
    -- Break the O(1) barrier
    Filter.Tendsto (fun N ↦ green_31.lower.answer N - Real.sqrt (N : ℝ)) atTop atTop ∧
    ∃ᶠ N in atTop, green_31.lower.answer N ≤ F N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L65).

## `Green31.green_31.variants.lower_eventually`

Open: stated without proof.

> Can we improve the lower bound $N^{1/2} + O(1)$, for all sufficiently large $N$?

```lean
theorem green_31.variants.lower_eventually :
    -- Break the O(1) barrier
    Filter.Tendsto (fun N ↦ green_31.variants.lower_eventually.answer N - Real.sqrt (N : ℝ)) atTop
      atTop ∧
    ∀ᶠ N in atTop, green_31.variants.lower_eventually.answer N ≤ F N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L75).

## `Green31.green_31.upper`

Open: stated without proof.

> Can we improve the upper bound $N^{1/2} + 0.94349 N^{1/4} + O(1)$ [HZ26], at least for infinitely
> many $N$?

```lean
theorem green_31.upper :
    (∃ᶠ N in atTop, F N ≤ green_31.upper.answer N) ∧
    ∃ c < (0.94349 : ℝ), ∃ C : ℝ, ∀ᶠ N in atTop, green_31.upper.answer N - Real.sqrt (N : ℝ) ≤ c *
      (N : ℝ) ^ (4⁻¹ : ℝ) + C
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L89).

## `Green31.green_31.variants.upper_eventually`

Open: stated without proof.

> Can we improve the upper bound $N^{1/2} + 0.94349 N^{1/4} + O(1)$ [HZ26], for all sufficiently
> large $N$?

```lean
theorem green_31.variants.upper_eventually :
    (∀ᶠ N in atTop, F N ≤ green_31.variants.upper_eventually.answer N) ∧
    ∃ c < (0.94349 : ℝ), ∃ C : ℝ, ∀ᶠ N in atTop, green_31.variants.upper_eventually.answer N -
      Real.sqrt (N : ℝ) ≤ c * (N : ℝ) ^ (4⁻¹ : ℝ) + C
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L102).

## `Green31.green_31.variants.upper_li69`

Solved: stated here without proof.

> [Li69] proved $F(n) \le n^{1/2} + n^{1/4} + O(1)$.

```lean
theorem green_31.variants.upper_li69 :
    ∃ C : ℝ, ∀ᶠ N in atTop, F N ≤ Real.sqrt (N : ℝ) + (N : ℝ) ^ (4⁻¹ : ℝ) + C
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L110).

## `Green31.green_31.variants.upper_bfr23`

Solved: stated here without proof.

> [BFR23] obtained a small improvement, getting an upper bound of $F(N) \le N^{1/2} + 0.998 N^{1/4}$
> for large $N$.

```lean
theorem green_31.variants.upper_bfr23 :
    ∀ᶠ N in atTop, F N ≤ Real.sqrt (N : ℝ) + (0.998 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L119).

## `Green31.green_31.variants.upper_cho25`

Solved: stated here without proof.

> The upper bound was further improved to $N^{1/2} + 0.98183 N^{1/4} + O(1)$ [CHO25].

```lean
theorem green_31.variants.upper_cho25 :
    ∃ C : ℝ, ∀ᶠ N in atTop, F N ≤ Real.sqrt (N : ℝ) + (0.98183 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ) + C
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L125).

## `Green31.green_31.variants.upper_hz26`

Solved: stated here without proof.

> [HZ26] improved the upper bound to $N^{1/2} + \gamma_0 N^{1/4} + O(1)$ with
> $\gamma_0 = 0.94349\ldots < 0.9435$.

```lean
theorem green_31.variants.upper_hz26 :
    ∃ C : ℝ, ∀ᶠ N in atTop, F N ≤ Real.sqrt (N : ℝ) + (0.9435 : ℝ) * (N : ℝ) ^ (4⁻¹ : ℝ) + C
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L134).

## `Green31.green_31.variants.zmod_p`

Open: stated without proof.

> It is not known whether or not there exists a Sidon subset of $\mathbb{Z}/p\mathbb{Z}$ of size
> $(1 + o(1))\sqrt{p}$, for all $p$ [Gr24].

```lean
theorem green_31.variants.zmod_p :
    ∃ S : (n : ℕ) → Finset (ZMod n),
    ∃ o : ℕ → ℝ,
      (o =o[atTop] fun _ : ℕ ↦ (1 : ℝ)) ∧
      (∀ p, p.Prime → IsSidon (S p : Set (ZMod p))) ∧
      (∀ p, p.Prime → ((S p).card : ℝ) = (1 + o p) * Real.sqrt (p : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L143).

## `Green31.green_31.variants.abelian`

Open: stated without proof.

> It is not known whether, if $G$ is an abelian group of size $n$, there always exists a Sidon subset
> of $G$ of size $0.01\sqrt{n}$ [Gr24].
>
> Green defines a Sidon set by $r_A(n) \le 1$ [Gr24, Section 4]. Read literally, this forbids
> $a + a = b + b$ with $a \ne b$, and the answer is trivially negative: a Sidon subset of a group
> of exponent $2$ then has at most one element. We use the definition of Babai and Sós [BS85]
> instead, see `IsGroupSidon`.

```lean
theorem green_31.variants.abelian :
    ∀ (G : Type) [AddCommGroup G] [Fintype G],
      ∃ S : Finset G, IsGroupSidon (S : Set G) ∧
        0.01 * Real.sqrt (Fintype.card G) ≤ S.card
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 213](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L213).

## `Green31.green_31.variants.sidon_01n`

Open: stated without proof.

> Another very nice old problem is whether there is a Sidon subset of $\{0, 1\}^n$ of size $N^{0.51}$,
> where $N = 2^n$ [Gr24].

```lean
theorem green_31.variants.sidon_01n :
    ∃ S : (n : ℕ) → Finset (𝔽₂ n),
      (∀ n, IsBinarySidon (S n : Set (𝔽₂ n))) ∧
      ∀ᶠ n in atTop, ((2 : ℝ) ^ n) ^ (0.51 : ℝ) ≤ (S n).card
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 233](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L233).

## `Green31.green_31.variants.sidon_01n_clz01`

Solved: stated here without proof.

> The best-known upper bound for a Sidon subset of $\{0, 1\}^n$ ($N = 2^n$) is $N^{0.5753}$ [CLZ01].

```lean
theorem green_31.variants.sidon_01n_clz01 :
    ∃ C : ℝ, ∀ n, ∀ S : Finset (𝔽₂ n),
      IsBinarySidon (S : Set (𝔽₂ n)) →
        (S.card : ℝ) ≤ C * ((2 : ℝ) ^ n) ^ (0.5753 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/31.lean, line 243](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean#L243).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/31.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/31.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.7](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.7)
