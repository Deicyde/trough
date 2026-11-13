---
declaration: theorem
origin: cited
lean: Arxiv.«0805.3777».isGenericRank_matrix, Arxiv.«0805.3777».isGenericRank_of_gt_critical, Arxiv.«0805.3777».isGenericRank_three_even, Arxiv.«0805.3777».isGenericRank_three_odd, Arxiv.«0805.3777».isGenericRank_four, Arxiv.«0805.3777».isGenericRank_cube, Arxiv.«0805.3777».isGenericRank_of_eq_critical, Arxiv.«0805.3777».isGenericRank_of_le_critical, Arxiv.«0805.3777».isMaxRank_two, Arxiv.«0805.3777».cprank_le_of_three_slices, Arxiv.«0805.3777».isMaxRank_three, Arxiv.«0805.3777».isMaxRank_of_le_min, Arxiv.«0805.3777».isMaxRank_three_three_five_bounds, Arxiv.«0805.3777».isMaxRank_three_three_five, Arxiv.«0805.3777».isMaxRank_le_two_mul_isGenericRank, Arxiv.«0805.3777».cprank_le_of_square_slices, Arxiv.«0805.3777».isMaxRank_cube_bounds, Arxiv.«0805.3777».isMaxRank_cube
statement: formalized
---

# Generic and maximal rank of 3-tensors

> The rank of a tensor $T \in \mathbb{C}^{m_1} \otimes \mathbb{C}^{m_2} \otimes \mathbb{C}^{m_3}$ is
> the least $r$ such that $T$ is a sum of $r$ decomposable tensors $a \otimes b \otimes c$. Mathlib
> records such a tensor as a `Holor ℂ [m₁, m₂, m₃]` and its rank as `Holor.cprank`.
>
> Two basic invariants of the format $(m_1, m_2, m_3)$ are the *generic rank*
> $\operatorname{grank}(m_1, m_2, m_3)$, the rank of a generic tensor, and the *maximal rank*
> $\operatorname{mrank}(m_1, m_2, m_3)$, the largest rank attained by a tensor of that format.
>
> Counting parameters gives the lower bound
> $\operatorname{grank}(m_1, m_2, m_3) \geq r_0(m_1, m_2, m_3) :=
> \lceil m_1m_2m_3 / (m_1 + m_2 + m_3 - 2) \rceil$. Once $m_3$ exceeds $(m_1-1)(m_2-1)$ the generic
> rank is known to be $\min(m_3, m_1m_2)$, so the interesting case is the *critical range*
> $3 \leq m_1 \leq m_2 \leq m_3 \leq (m_1-1)(m_2-1)$ [Fri12, Conjecture 5.1; BFZ24, (4.14)]. There
> the bound $r_0$ is attained in every case that has been settled, except for the formats
> $(3, 2p+1, 2p+1)$, where the generic rank is $r_0 + 1$. Friedland's conjecture, stated here as
> `isGenericRank_of_le_critical`, is that these are the only exceptions. The boundary case
> $m_3 = (m_1-1)(m_2-1)$ is settled in [Fri12, Corollary 6.4(2)] and recorded as
> `isGenericRank_of_eq_critical`.
>
> The maximal rank is much less well understood. It is known for the formats
> $2 \times m \times n$ and for a range of small formats, but no formula is known even for
> $(n, n, n)$, and $\operatorname{mrank}(3, 3, 5)$ is undetermined.
>
> Tensor rank is invariant under permuting the three factors, but `Holor ℂ [m₁, m₂, m₃]` and its
> permutations are different types and Mathlib has no transport lemma between them. Each statement
> below therefore writes the format in the order its own source uses.
>
> *References:*
> * [Fri12] S. Friedland, *On the generic and typical ranks of 3-tensors*, Linear Algebra Appl. 436
>   (2012), 478-497, https://doi.org/10.1016/j.laa.2011.05.008
>   ([arxiv/0805.3777](https://arxiv.org/abs/0805.3777)). Conjecture 5.1, and the survey of known
>   values in Section 5.
> * [BFZ24] W. Bruzda, S. Friedland, K. Życzkowski, *Rank of a tensor and quantum entanglement*,
>   Linear Multilinear Algebra 72 (2024), 1796-1859,
>   https://doi.org/10.1080/03081087.2023.2211717
>   ([arxiv/1912.06854v4](https://arxiv.org/pdf/1912.06854v4)). A survey; the numbering used below is
>   that of the arXiv v4 PDF. Conjecture 4.12 restates [Fri12, Conjecture 5.1], and Sections 4.5
>   and 4.6 collect the current status.
> * [CGG02] M. V. Catalisano, A. V. Geramita, A. Gimigliano, *Ranks of tensors, secant varieties of
>   Segre varieties and fat points*, Linear Algebra Appl. 355 (2002), 263-285,
>   https://doi.org/10.1016/S0024-3795(02)00352-X. Used for `isGenericRank_of_gt_critical`.
> * [Str83] V. Strassen, *Rank and optimal computation of generic tensors*, Linear Algebra Appl.
>   52/53 (1983), 645-685, https://doi.org/10.1016/0024-3795(83)80041-X. Used for
>   `isGenericRank_three_even` and `isGenericRank_three_odd`.
> * [AOP09] H. Abo, G. Ottaviani, C. Peterson, *Induction for secant varieties of Segre varieties*,
>   Trans. Amer. Math. Soc. 361 (2009), 767-792, https://doi.org/10.1090/S0002-9947-08-04725-9.
>   Used for `isGenericRank_four`.
> * [Lic85] T. Lickteig, *Typical tensorial rank*, Linear Algebra Appl. 69 (1985), 95-120,
>   https://doi.org/10.1016/0024-3795(85)90070-9. Used for `isGenericRank_cube`.
> * [AS79] M. D. Atkinson, N. M. Stephens, *On the maximal multiplicative complexity of a family of
>   bilinear forms*, Linear Algebra Appl. 27 (1979), 1-8,
>   https://doi.org/10.1016/0024-3795(79)90026-0. Used for `isMaxRank_two`,
>   `cprank_le_of_three_slices`, `cprank_le_of_square_slices`, `isMaxRank_of_le_min` and
>   `isMaxRank_three_three_five_bounds`.
> * [JaJa79] J. JáJá, *Optimal evaluation of pairs of bilinear forms*, SIAM J. Comput. 8 (1979),
>   443-462, https://doi.org/10.1137/0208037, and J. B. Kruskal, *Rank, decomposition, and
>   uniqueness for 3-way and N-way arrays*, in Multiway Data Analysis, North-Holland (1989), 7-18.
>   Cited by [Fri12] for `isMaxRank_two`.
> * [SMS10] T. Sumi, M. Miyazaki, T. Sakata, *About the maximal rank of 3-tensors over the real and
>   the complex number field*, Ann. Inst. Statist. Math. 62 (2010), 807-822,
>   https://doi.org/10.1007/s10463-010-0294-5 ([arxiv/0806.4048](https://arxiv.org/abs/0806.4048)).
>   Theorem 4.5 proves the first of the two bounds that [AS79] states without proof; Proposition
>   4.9(1) is the special case used for `isMaxRank_three`.
> * [Ki26] K. Kitamura, *A Lean proof that the maximal rank of complex $3 \times 3 \times 5$
>   tensors is 6*, GitHub repository (2026), https://github.com/KitaKen1/mrank-3-3-5-lean. Used
>   for `isMaxRank_three_three_five`.
> * [BT15] G. Blekherman, Z. Teitler, *On maximum, typical and generic ranks*, Math. Ann. 362
>   (2015), 1021-1031, https://doi.org/10.1007/s00208-014-1150-3
>   ([arxiv/1402.2371](https://arxiv.org/abs/1402.2371)), Theorem 1. Used for
>   `isMaxRank_le_two_mul_isGenericRank`.

*Quoted from [FormalConjectures/Arxiv/0805.3777/TensorRank.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 18 research or textbook statements: 2 open, 15 solved and 1 textbook result. It also has 1 test statement and 5 API statements, counted here but not shown.

## `Arxiv.«0805.3777».isGenericRank_matrix`

Textbook result, stated without proof.

> The generic rank of an $m \times n$ matrix is $\min(m, n)$: the 2-tensor case.

```lean
theorem isGenericRank_matrix (m n : ℕ) : IsGenericRank [m, n] (min m n)
```

Category `textbook`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L183).

## `Arxiv.«0805.3777».isGenericRank_of_gt_critical`

Solved: stated here without proof.

> Above the critical range, a generic tensor of format $(m_1, m_2, m_3)$ has rank
> $\min(m_3, m_1m_2)$ [Fri12, (5.1)].

```lean
theorem isGenericRank_of_gt_critical {m₁ m₂ m₃ : ℕ} (h₁ : 1 ≤ m₁) (h₁₂ : m₁ ≤ m₂) (h₂₃ : m₂ ≤ m₃)
    (h : (m₁ - 1) * (m₂ - 1) < m₃) :
    IsGenericRank [m₁, m₂, m₃] (min m₃ (m₁ * m₂))
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 191](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L191).

## `Arxiv.«0805.3777».isGenericRank_three_even`

Solved: stated here without proof.

> The generic rank of a $3 \times 2p \times 2p$ tensor is $\lceil 12p^2 / (4p + 1) \rceil$, the
> value $r_0$ predicted by a dimension count [Fri12, (5.3)]. The hypothesis $2 \leq p$ is the
> ordering $3 \leq 2p$ of the format.

```lean
theorem isGenericRank_three_even {p : ℕ} (hp : 2 ≤ p) :
    IsGenericRank [3, 2 * p, 2 * p] (12 * p ^ 2 ⌈/⌉ (4 * p + 1))
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 200](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L200).

## `Arxiv.«0805.3777».isGenericRank_three_odd`

Solved: stated here without proof.

> The generic rank of a $3 \times (2p+1) \times (2p+1)$ tensor is
> $\lceil 3(2p+1)^2 / (4p + 3) \rceil + 1$, one more than the value $r_0$ predicted by a dimension
> count [Fri12, (5.4)]. These are the only formats in the critical range known to exceed $r_0$. The
> case $p = 1$ says that the generic rank of a $3 \times 3 \times 3$ tensor is `5`, not `4`.

```lean
theorem isGenericRank_three_odd {p : ℕ} (hp : 1 ≤ p) :
    IsGenericRank [3, 2 * p + 1, 2 * p + 1] (3 * (2 * p + 1) ^ 2 ⌈/⌉ (4 * p + 3) + 1)
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 211](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L211).

## `Arxiv.«0805.3777».isGenericRank_four`

Solved: stated here without proof.

> The generic rank of a $4 \times m \times m$ tensor is $\lceil 4m^2 / (2m + 2) \rceil$
> [Fri12, (5.7)]. This is the case $(4, m, m)$ of `isGenericRank_of_le_critical`, settled in
> [AOP09]; see [BFZ24, Section 4.5].

```lean
theorem isGenericRank_four {m : ℕ} (hm : 3 ≤ m) :
    IsGenericRank [4, m, m] (4 * m ^ 2 ⌈/⌉ (2 * m + 2))
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 219](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L219).

## `Arxiv.«0805.3777».isGenericRank_cube`

Solved: stated here without proof.

> For $n \neq 3$ the generic rank of an $n \times n \times n$ tensor is
> $\lceil n^3 / (3n - 2) \rceil$ [Fri12, (5.8)].

```lean
theorem isGenericRank_cube {n : ℕ} (hn : 1 ≤ n) (hn3 : n ≠ 3) :
    IsGenericRank [n, n, n] (n ^ 3 ⌈/⌉ (3 * n - 2))
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 226](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L226).

## `Arxiv.«0805.3777».isGenericRank_of_eq_critical`

Solved: stated here without proof.

> The generic rank at the critical boundary is $(m_1-1)(m_2-1)+1$
> [Fri12, Corollary 6.4(2)]. By `critical_ceilDiv`, this is the dimension-count value in
> `isGenericRank_of_le_critical`.

```lean
theorem isGenericRank_of_eq_critical {m₁ m₂ : ℕ} (h₁ : 3 ≤ m₁) (h₁₂ : m₁ ≤ m₂) :
    IsGenericRank [m₁, m₂, (m₁ - 1) * (m₂ - 1)] ((m₁ - 1) * (m₂ - 1) + 1)
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 263](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L263).

## `Arxiv.«0805.3777».isGenericRank_of_le_critical`

Open: stated without proof.

> **Friedland's conjecture.** In the critical range $m_3 \leq (m_1 - 1)(m_2 - 1)$, and away from the
> formats $(3, 2p+1, 2p+1)$, the generic rank of a tensor of format $(m_1, m_2, m_3)$ is the value
> $\lceil m_1m_2m_3 / (m_1 + m_2 + m_3 - 2) \rceil$ predicted by a dimension count
> [Fri12, Conjecture 5.1]. The boundary $m_3 = (m_1-1)(m_2-1)$ is settled by
> `isGenericRank_of_eq_critical` [Fri12, (5.11)]. It is known for $m_1 \leq 4$ and for $(n, n, n)$,
> and has been verified numerically throughout the critical range for $m_3 \leq 20$
> [BFZ24, Section 4.5].

```lean
theorem isGenericRank_of_le_critical {m₁ m₂ m₃ : ℕ} (h₁ : 3 ≤ m₁) (h₁₂ : m₁ ≤ m₂) (h₂₃ : m₂ ≤ m₃)
    (h : m₃ ≤ (m₁ - 1) * (m₂ - 1)) (hexc : ∀ p : ℕ, (m₁, m₂, m₃) ≠ (3, 2 * p + 1, 2 * p + 1)) :
    IsGenericRank [m₁, m₂, m₃] (m₁ * m₂ * m₃ ⌈/⌉ (m₁ + m₂ + m₃ - 2))
```

Category `research open`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 277](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L277).

## `Arxiv.«0805.3777».isMaxRank_two`

Solved: stated here without proof.

> The maximal rank of a $2 \times m \times n$ tensor is $m + \min(m, \lfloor n/2 \rfloor)$
> [Fri12, (5.13)]; equivalently [BFZ24, (4.9)].

```lean
theorem isMaxRank_two {m n : ℕ} (hm : 2 ≤ m) (hmn : m ≤ n) :
    IsMaxRank [2, m, n] (m + min m (n / 2))
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 285](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L285).

## `Arxiv.«0805.3777».cprank_le_of_three_slices`

Solved: stated here without proof.

> Every $n \times n \times 3$ tensor has rank at most $2n - 1$ [SMS10, Theorem 4.5].

```lean
theorem cprank_le_of_three_slices {n : ℕ} (hn : 1 ≤ n) (T : Holor ℂ [n, n, 3]) :
    T.cprank ≤ 2 * n - 1
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 291](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L291).

## `Arxiv.«0805.3777».isMaxRank_three`

Solved: stated here without proof.

> The maximal rank of a $3 \times 3 \times 3$ tensor is `5`. The upper bound is
> [SMS10, Proposition 4.9(1)], a special case of `cprank_le_of_three_slices`; the lower bound is the
> generic rank `isGenericRank_three_odd` at $p = 1$.

```lean
theorem isMaxRank_three : IsMaxRank [3, 3, 3] 5
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 299](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L299).

## `Arxiv.«0805.3777».isMaxRank_of_le_min`

Solved: stated here without proof.

> For $u \leq \min(4, m)$ the maximal rank of an $m \times n \times (mn - u)$ tensor is
> $mn - \lceil u/2 \rceil$ [BFZ24, (4.24)].

```lean
theorem isMaxRank_of_le_min {m n u : ℕ} (hm : 3 ≤ m) (hmn : m ≤ n) (hu : u ≤ min 4 m) :
    IsMaxRank [m, n, m * n - u] (m * n - u ⌈/⌉ 2)
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 305](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L305).

## `Arxiv.«0805.3777».isMaxRank_three_three_five_bounds`

Solved: stated here without proof.

> The maximal rank of a $3 \times 3 \times 5$ tensor is `6` or `7` [BFZ24, (4.20)].

```lean
theorem isMaxRank_three_three_five_bounds {R : ℕ} (hR : IsMaxRank [3, 3, 5] R) :
    6 ≤ R ∧ R ≤ 7
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 311](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L311).

## `Arxiv.«0805.3777».isMaxRank_three_three_five`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/mrank-3-3-5-lean/blob/fbec93aa021bd994380cd27eb60e444e7cc85e93/lean/TensorRank335FC.lean#L3365-L3367](https://github.com/KitaKen1/mrank-3-3-5-lean/blob/fbec93aa021bd994380cd27eb60e444e7cc85e93/lean/TensorRank335FC.lean#L3365-L3367).

> Determine the maximal rank of a $3 \times 3 \times 5$ tensor. It was the one
> undetermined entry of the table of $\operatorname{mrank}(3, 3, p)$ for $p \leq 9$
> [BFZ24, (4.20)]. The answer is `6`. A Lean proof is given in [Ki26].

```lean
theorem isMaxRank_three_three_five : IsMaxRank [3, 3, 5] isMaxRank_three_three_five.answer
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 324](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L324).

## `Arxiv.«0805.3777».isMaxRank_le_two_mul_isGenericRank`

Solved: stated here without proof.

> The maximal rank is at most twice the generic rank [BT15, Theorem 1].

```lean
theorem isMaxRank_le_two_mul_isGenericRank {ds : List ℕ} {r R : ℕ} (hr : IsGenericRank ds r)
    (hR : IsMaxRank ds R) : R ≤ 2 * r
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 329](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L329).

## `Arxiv.«0805.3777».cprank_le_of_square_slices`

Solved: stated here without proof.

> Every complex $m \times n \times n$ tensor has rank at most
> $\lfloor (m+1)n/2 \rfloor$ for $m,n \geq 3$ [BFZ24, (4.22)].

```lean
theorem cprank_le_of_square_slices {m n : ℕ} (hm : 3 ≤ m) (hn : 3 ≤ n)
    (T : Holor ℂ [m, n, n]) : T.cprank ≤ (m + 1) * n / 2
```

Category `research solved`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 336](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L336).

## `Arxiv.«0805.3777».isMaxRank_cube_bounds`

Proved here.

> For $n \geq 4$, the maximal rank $R$ of a complex cubic tensor satisfies
> $\lceil n^3/(3n-2) \rceil \leq R \leq n(n+1)/2$ [BFZ24, (4.22), (4.25)-(4.28)].
> The lower bound is the generic rank; the upper bound is the square-slice estimate.

```lean
theorem isMaxRank_cube_bounds {n R : ℕ} (hn : 4 ≤ n) (hR : IsMaxRank [n, n, n] R) :
    n ^ 3 ⌈/⌉ (3 * n - 2) ≤ R ∧ R ≤ n * (n + 1) / 2
```

Category `research solved`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md), [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 344](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L344).

## `Arxiv.«0805.3777».isMaxRank_cube`

Open: stated without proof.

> **Open problem.** Determine the maximal rank of a complex $n \times n \times n$ tensor. No formula
> is known: for $n = 1, 2, 3$ the values are `1`, `3` and `5`, while for $4 \leq n \leq 7$ only
> the bounds in `isMaxRank_cube_bounds`, such as $7 \leq \operatorname{mrank}(4,4,4) \leq 10$,
> are available [BFZ24, (4.25)-(4.28)].

```lean
theorem isMaxRank_cube {n : ℕ} (hn : 1 ≤ n) :
    IsMaxRank [n, n, n] (isMaxRank_cube.answer n)
```

Category `research open`; AMS [15 Linear and multilinear algebra; matrix theory](../../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md). Declared in [FormalConjectures/Arxiv/0805.3777/TensorRank.lean, line 361](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean#L361).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/0805.3777/TensorRank.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/0805.3777/TensorRank.lean)
- [https://doi.org/10.1016/j.laa.2011.05.008](https://doi.org/10.1016/j.laa.2011.05.008)
