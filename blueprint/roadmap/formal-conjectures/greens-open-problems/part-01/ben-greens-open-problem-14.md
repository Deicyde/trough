---
declaration: theorem
origin: cited
lean: Green14.green_14_polynomial, Green14.green_14_polynomial_k_eq_3, Green14.green_14_quadratic, Green14.green_14_lower_bound_green, Green14.green_14_lower_bound_hunter, Green14.green_14_lower_bound_brown_landman_robertson, Green14.green_14_lower_bound_li_shu, Green14.green_14_upper_bound_schoen, Green14.green_14_upper_bound_kelley_meka, Green14.green_14_variant_2r2, Green14.W_3_3, Green14.W_3_4, Green14.W_3_5, Green14.W_3_6, Green14.W_3_7, Green14.W_3_8, Green14.W_3_9, Green14.W_3_10, Green14.W_3_11, Green14.W_3_12, Green14.W_3_13, Green14.W_3_14, Green14.W_3_15, Green14.W_3_16, Green14.W_3_17, Green14.W_3_18, Green14.W_3_19, Green14.W_3_20_lower, Green14.W_3_20, Green14.W_3_21_lower, Green14.W_3_21_eq, Green14.W_3_22_lower, Green14.W_3_22_eq, Green14.W_3_23_lower, Green14.W_3_23_eq, Green14.W_3_24_lower, Green14.W_3_24_eq, Green14.W_3_25_lower, Green14.W_3_25_eq, Green14.W_3_26_lower, Green14.W_3_26_eq, Green14.W_3_27_lower, Green14.W_3_27_eq, Green14.W_3_28_lower, Green14.W_3_28_eq, Green14.W_3_29_lower, Green14.W_3_29_eq, Green14.W_3_30_lower, Green14.W_3_30_eq, Green14.W_3_31_lower, Green14.W_3_32_lower, Green14.W_3_33_lower, Green14.W_3_34_lower, Green14.W_3_35_lower, Green14.W_3_36_lower, Green14.W_3_37_lower, Green14.W_3_38_lower, Green14.W_3_39_lower
statement: formalized
---

# Ben Green's Open Problem 14

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.14)
> - [AKS14] Ahmed, Tanbir, Oliver Kullmann, and Hunter Snevily. "On the van der Waerden numbers
>   w (2; 3, t)." Discrete Applied Mathematics 174 (2014): 27-51.
> - [KeMe23] Kelley, Zander, and Raghu Meka. "Strong bounds for 3-progressions." 2023 IEEE 64th
>   Annual Symposium on Foundations of Computer Science (FOCS). IEEE, 2023.
> - [Hu22] Hunter, Zach. "Improved lower bounds for van der Waerden numbers." Combinatorica 42.
>   Suppl 2 (2022): 1231-1252.
> - [Gr21] Green, Ben. "New lower bounds for van der Waerden numbers." Forum of Mathematics,
>   Pi. Vol. 10. Cambridge University Press, 2022.
> - [Sc20] Schoen, Tomasz. "A subexponential upper bound for van der Waerden numbers W (3, k)."
>   arXiv preprint arXiv:2006.02877 (2020).
> - [BLR08] Brown, Tom, Bruce M. Landman, and Aaron Robertson. "Bounds on some van der Waerden
>   numbers." Journal of Combinatorial Theory, Series A 115.7 (2008): 1304-1309.
> - [LiSh10] Li, Yusheng, and Jinlong Shu. "A lower bound for off-diagonal van der Waerden numbers."
>   Advances in Applied Mathematics 44.3 (2010): 243-247.
> - [Ko15] Kouril, Michal. "Leveraging FPGA clusters for SAT computations." Parallel Computing:
>   On the Road to Exascale (2015): 525-532.
> - [CCH23] Chowdhury, Md Solimul, Cayden R. Codel, and Marijn J. H. Heule. "A linear weight
>   transfer rule for local search." NASA Formal Methods (NFM 2023), Springer (2023).

*Quoted from [FormalConjectures/GreensOpenProblems/14.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 58 research or textbook statements: 9 open and 49 solved.

## `Green14.green_14_polynomial`

Solved: stated here without proof.

> Is $W(k, r)$ a polynomial in $r$, for fixed $k$?
>
> We formulate this as asking if $W(k, r)$ has polynomial growth in $r$.
> The answer is no, already for $k = 4$. Every red $k$-term progression with $k \ge 3$ contains a
> red $3$-term progression, so `mixedMonoAPGuaranteeSet k r ⊆ mixedMonoAPGuaranteeSet 3 r`, and
> both sets are nonempty by van der Waerden's theorem, so $W(3, r) \le W(k, r)$. Polynomial
> growth for one $k \ge 4$ would therefore force polynomial growth for $k = 3$, contradicting
> `green_14_polynomial_k_eq_3` [Gr21, p.3].

```lean
theorem green_14_polynomial :
    ¬ ∀ k ≥ 4, ∃ d : ℕ, (fun r => (W k r : ℝ)) =O[atTop] fun r => (r : ℝ) ^ d
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L78).

## `Green14.green_14_polynomial_k_eq_3`

Solved: stated here without proof.

> We know $W(3, r)$ does not have polynomial growth in $r$ [Gr21, p.3].

```lean
theorem green_14_polynomial_k_eq_3 :
    ¬ ∃ d : ℕ, (fun r => (W 3 r : ℝ)) =O[atTop] fun r => (r : ℝ) ^ d
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L84).

## `Green14.green_14_quadratic`

Solved: stated here without proof.

> Is $W(3, r) \ll r^2$?
>
> [Gr21] proves a superpolynomial lower bound $W(3, r) \gg \exp(c(\log r)^{4/3-o(1)})$.

```lean
theorem green_14_quadratic :
    ¬ (fun r => (W 3 r : ℝ)) =O[atTop] fun r => (r : ℝ) ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L94).

## `Green14.green_14_lower_bound_green`

Solved: stated here without proof.

> [Gr21] proved a lower bound of shape $W(3, r) \gg \exp(c(\log r)^{4/3-o(1)})$.

```lean
theorem green_14_lower_bound_green :
    ∃ c : ℝ, 0 < c ∧ ∃ (o : ℕ → ℝ) (_ : Tendsto o atTop (𝓝 0)),
    (fun (r : ℕ) => Real.exp (c * (Real.log r)^(4/3 - o r))) =O[atTop] fun r => (W 3 r : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L100).

## `Green14.green_14_lower_bound_hunter`

Solved: stated here without proof.

> [Hu22] improved this to $W(3, r) \gg \exp(c(\log r)^{2-o(1)})$.

```lean
theorem green_14_lower_bound_hunter :
    ∃ c : ℝ, 0 < c ∧ ∃ (o : ℕ → ℝ) (_ : Tendsto o atTop (𝓝 0)),
    (fun (r : ℕ) => Real.exp (c * (Real.log r)^(2 - o r))) =O[atTop] (fun r => (W 3 r : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L107).

## `Green14.green_14_lower_bound_brown_landman_robertson`

Solved: stated here without proof.

> [BLR08] proved $W(3, r) \gg r^{2 - 1/\log \log r}$.

```lean
theorem green_14_lower_bound_brown_landman_robertson :
    (fun (r : ℕ) => (r : ℝ)^(2 - 1 / Real.log (Real.log r))) =O[atTop] (fun r => (W 3 r : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L114).

## `Green14.green_14_lower_bound_li_shu`

Solved: stated here without proof.

> [LiSh10] proved $W(3, r) \gg (r / \log r)^2$.

```lean
theorem green_14_lower_bound_li_shu :
    (fun (r : ℕ) => ((r : ℝ) / Real.log r)^2) =O[atTop] (fun r => (W 3 r : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L120).

## `Green14.green_14_upper_bound_schoen`

Solved: stated here without proof.

> [Sc20] proves the upper bound $W(3, r) < \exp(r^{1-c})$ for some $c > 0$.

```lean
theorem green_14_upper_bound_schoen :
    ∃ c : ℝ, 0 < c ∧
    (fun (r : ℕ) => ((W 3 r) : ℝ)) =O[atTop] (fun r => Real.exp ((r : ℝ) ^ (1 - c)))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L126).

## `Green14.green_14_upper_bound_kelley_meka`

Solved: stated here without proof.

> [KeMe23] gives a corresponding upper bound $W(3, r) \ll \exp(C(\log r)^C)$.

```lean
theorem green_14_upper_bound_kelley_meka :
    ∃ C : ℝ,
    (fun (r : ℕ) => ((W 3 r) : ℝ)) =O[atTop] (fun r => Real.exp (C * (Real.log r)^C))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L133).

## `Green14.green_14_variant_2r2`

Open: stated without proof.

> It remains an interesting open problem to actually write down a colouring showing (say)
> $W(3, r) \ge 2r^2$ for some $r$. [Gr24]

```lean
theorem green_14_variant_2r2 :
    -- Provide a pair (r, associated coloring) that avoids the monochromatic APs
    -- To show $W(3, r) > 2r^2 - 1$, we need a coloring of $\{1, \ldots, 2r^2 - 1\}$
    -- that avoids monochromatic APs of length 3 and $r$.
    let ans : Σ r : ℕ, Icc 1 (2 * r^2 - 1) → Fin 2 := green_14_variant_2r2.answer
    let r := ans.1
    let c := ans.2
    3 ≤ r ∧
    ¬ ((∃ s : Finset (Icc 1 (2 * r^2 - 1)), ({(s' : ℕ) | s' ∈ s}).IsAPOfLength 3 ∧ ∀ x ∈ s, c x = 0) ∨
       (∃ s : Finset (Icc 1 (2 * r^2 - 1)), ({(s' : ℕ) | s' ∈ s}).IsAPOfLength r ∧ ∀ x ∈ s, c x = 1))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L145).

## `Green14.W_3_3`

Solved: stated here; a Lean proof is at [https://github.com/Konamiu/formal-conjectures/blob/d6a68af97f6ca7856d892569d88ab1ecc8e927bf/FormalConjectures/GreensOpenProblems/14.lean#L289](https://github.com/Konamiu/formal-conjectures/blob/d6a68af97f6ca7856d892569d88ab1ecc8e927bf/FormalConjectures/GreensOpenProblems/14.lean#L289).

> $W(3, 3) = 9$ from [AKS14].

```lean
theorem W_3_3 : W 3 3 = 9
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L162).

## `Green14.W_3_4`

Solved: stated here; a Lean proof is at [https://github.com/Konamiu/formal-conjectures/blob/d6a68af97f6ca7856d892569d88ab1ecc8e927bf/FormalConjectures/GreensOpenProblems/14.lean#L301](https://github.com/Konamiu/formal-conjectures/blob/d6a68af97f6ca7856d892569d88ab1ecc8e927bf/FormalConjectures/GreensOpenProblems/14.lean#L301).

> $W(3, 4) = 18$ from [AKS14].

```lean
theorem W_3_4 : W 3 4 = 18
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 168](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L168).

## `Green14.W_3_5`

Solved: stated here; a Lean proof is at [https://github.com/Konamiu/formal-conjectures/blob/d6a68af97f6ca7856d892569d88ab1ecc8e927bf/FormalConjectures/GreensOpenProblems/14.lean#L313](https://github.com/Konamiu/formal-conjectures/blob/d6a68af97f6ca7856d892569d88ab1ecc8e927bf/FormalConjectures/GreensOpenProblems/14.lean#L313).

> $W(3, 5) = 22$ from [AKS14].

```lean
theorem W_3_5 : W 3 5 = 22
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 174](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L174).

## `Green14.W_3_6`

Solved: stated here without proof.

> $W(3, 6) = 32$ from [AKS14].

```lean
theorem W_3_6 : W 3 6 = 32
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 178](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L178).

## `Green14.W_3_7`

Solved: stated here without proof.

> $W(3, 7) = 46$ from [AKS14].

```lean
theorem W_3_7 : W 3 7 = 46
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 182](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L182).

## `Green14.W_3_8`

Solved: stated here without proof.

> $W(3, 8) = 58$ from [AKS14].

```lean
theorem W_3_8 : W 3 8 = 58
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 186](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L186).

## `Green14.W_3_9`

Solved: stated here without proof.

> $W(3, 9) = 77$ from [AKS14].

```lean
theorem W_3_9 : W 3 9 = 77
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L190).

## `Green14.W_3_10`

Solved: stated here without proof.

> $W(3, 10) = 97$ from [AKS14].

```lean
theorem W_3_10 : W 3 10 = 97
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 194](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L194).

## `Green14.W_3_11`

Solved: stated here without proof.

> $W(3, 11) = 114$ from [AKS14].

```lean
theorem W_3_11 : W 3 11 = 114
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L198).

## `Green14.W_3_12`

Solved: stated here without proof.

> $W(3, 12) = 135$ from [AKS14].

```lean
theorem W_3_12 : W 3 12 = 135
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 202](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L202).

## `Green14.W_3_13`

Solved: stated here without proof.

> $W(3, 13) = 160$ from [AKS14].

```lean
theorem W_3_13 : W 3 13 = 160
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 206](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L206).

## `Green14.W_3_14`

Solved: stated here without proof.

> $W(3, 14) = 186$ from [AKS14].

```lean
theorem W_3_14 : W 3 14 = 186
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 210](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L210).

## `Green14.W_3_15`

Solved: stated here without proof.

> $W(3, 15) = 218$ from [AKS14].

```lean
theorem W_3_15 : W 3 15 = 218
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 214](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L214).

## `Green14.W_3_16`

Solved: stated here without proof.

> $W(3, 16) = 238$ from [AKS14].

```lean
theorem W_3_16 : W 3 16 = 238
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 218](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L218).

## `Green14.W_3_17`

Solved: stated here without proof.

> $W(3, 17) = 279$ from [AKS14].

```lean
theorem W_3_17 : W 3 17 = 279
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 222](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L222).

## `Green14.W_3_18`

Solved: stated here without proof.

> $W(3, 18) = 312$ from [AKS14].

```lean
theorem W_3_18 : W 3 18 = 312
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 226](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L226).

## `Green14.W_3_19`

Solved: stated here without proof.

> $W(3, 19) = 349$ from [AKS14].

```lean
theorem W_3_19 : W 3 19 = 349
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 230](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L230).

## `Green14.W_3_20_lower`

Solved: stated here; a Lean proof is at [https://github.com/DomTheDeveloper/formal-conjectures/blob/013a0f04de0057d2bd1034c7cc4caf10ac8dc2cf/FormalConjectures/GreensOpenProblems/Green14FastKernel20.lean](https://github.com/DomTheDeveloper/formal-conjectures/blob/013a0f04de0057d2bd1034c7cc4caf10ac8dc2cf/FormalConjectures/GreensOpenProblems/Green14FastKernel20.lean).

> $W(3, 20) \ge 389$ from [AKS14, Table 2], proved by an explicit good partition.
> A kernel-checked Lean proof from the certificate was given by Dominic Dabish.

```lean
theorem W_3_20_lower : W 3 20 ≥ 389
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 239](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L239).

## `Green14.W_3_20`

Solved: stated here without proof.

> $W(3, 20) = 389$, conjectured in [AKS14, Table 2] and established by Kouril [Ko15] using
> FPGA-based SAT solving.

```lean
theorem W_3_20 : W 3 20 = 389
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 244](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L244).

## `Green14.W_3_21_lower`

Solved: stated here without proof.

> $W(3, 21) \ge 416$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_21_lower : W 3 21 ≥ 416
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 248](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L248).

## `Green14.W_3_21_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 21) = 416$.

```lean
theorem W_3_21_eq : W 3 21 = 416
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 252](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L252).

## `Green14.W_3_22_lower`

Solved: stated here without proof.

> $W(3, 22) \ge 464$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_22_lower : W 3 22 ≥ 464
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 256](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L256).

## `Green14.W_3_22_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 22) = 464$.

```lean
theorem W_3_22_eq : W 3 22 = 464
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 260](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L260).

## `Green14.W_3_23_lower`

Solved: stated here without proof.

> $W(3, 23) \ge 516$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_23_lower : W 3 23 ≥ 516
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 264](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L264).

## `Green14.W_3_23_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 23) = 516$.

```lean
theorem W_3_23_eq : W 3 23 = 516
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 268](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L268).

## `Green14.W_3_24_lower`

Solved: stated here without proof.

> $W(3, 24) \ge 593$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_24_lower : W 3 24 ≥ 593
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 272](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L272).

## `Green14.W_3_24_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 24) = 593$.

```lean
theorem W_3_24_eq : W 3 24 = 593
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 276](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L276).

## `Green14.W_3_25_lower`

Solved: stated here without proof.

> $W(3, 25) \ge 656$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_25_lower : W 3 25 ≥ 656
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 280](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L280).

## `Green14.W_3_25_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 25) = 656$.

```lean
theorem W_3_25_eq : W 3 25 = 656
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 284](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L284).

## `Green14.W_3_26_lower`

Solved: stated here without proof.

> $W(3, 26) \ge 727$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_26_lower : W 3 26 ≥ 727
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 288](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L288).

## `Green14.W_3_26_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 26) = 727$.

```lean
theorem W_3_26_eq : W 3 26 = 727
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 292](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L292).

## `Green14.W_3_27_lower`

Solved: stated here without proof.

> $W(3, 27) \ge 770$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_27_lower : W 3 27 ≥ 770
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 296](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L296).

## `Green14.W_3_27_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 27) = 770$.

```lean
theorem W_3_27_eq : W 3 27 = 770
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 300](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L300).

## `Green14.W_3_28_lower`

Solved: stated here without proof.

> $W(3, 28) \ge 827$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_28_lower : W 3 28 ≥ 827
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 304](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L304).

## `Green14.W_3_28_eq`

Open: stated without proof.

> [AKS14, Table 2] conjectures that $W(3, 28) = 827$.

```lean
theorem W_3_28_eq : W 3 28 = 827
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 308](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L308).

## `Green14.W_3_29_lower`

Solved: stated here without proof.

> $W(3, 29) \ge 868$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_29_lower : W 3 29 ≥ 868
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 312](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L312).

## `Green14.W_3_29_eq`

Solved: stated here without proof.

> [AKS14, Table 2] conjectures that $W(3, 29) = 868$. This is false: Chowdhury, Codel, and Heule
> [CCH23, Section 6.3] found a good partition of $\{1, \ldots, 868\}$, so $W(3, 29) \geq 869$.

```lean
theorem W_3_29_eq : ¬ W 3 29 = 868
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 317](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L317).

## `Green14.W_3_30_lower`

Solved: stated here without proof.

> $W(3, 30) \ge 903$ from [AKS14, Table 2], proved by an explicit good partition.

```lean
theorem W_3_30_lower : W 3 30 ≥ 903
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 321](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L321).

## `Green14.W_3_30_eq`

Solved: stated here without proof.

> [AKS14, Table 2] conjectures that $W(3, 30) = 903$. This is false: Chowdhury, Codel, and Heule
> [CCH23, Section 6.3] found a good partition of $\{1, \ldots, 903\}$, so $W(3, 30) \geq 904$.

```lean
theorem W_3_30_eq : ¬ W 3 30 = 903
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 326](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L326).

## `Green14.W_3_31_lower`

Solved: stated here without proof.

> $W(3, 31) > 930$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_31_lower : W 3 31 > 930
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 332](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L332).

## `Green14.W_3_32_lower`

Solved: stated here without proof.

> $W(3, 32) > 1006$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_32_lower : W 3 32 > 1006
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 336](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L336).

## `Green14.W_3_33_lower`

Solved: stated here without proof.

> $W(3, 33) > 1063$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_33_lower : W 3 33 > 1063
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 340](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L340).

## `Green14.W_3_34_lower`

Solved: stated here without proof.

> $W(3, 34) > 1143$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_34_lower : W 3 34 > 1143
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 344](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L344).

## `Green14.W_3_35_lower`

Solved: stated here without proof.

> $W(3, 35) > 1204$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_35_lower : W 3 35 > 1204
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 348](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L348).

## `Green14.W_3_36_lower`

Solved: stated here without proof.

> $W(3, 36) > 1257$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_36_lower : W 3 36 > 1257
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 352](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L352).

## `Green14.W_3_37_lower`

Solved: stated here without proof.

> $W(3, 37) > 1338$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_37_lower : W 3 37 > 1338
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 356](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L356).

## `Green14.W_3_38_lower`

Solved: stated here without proof.

> $W(3, 38) > 1378$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_38_lower : W 3 38 > 1378
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 360](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L360).

## `Green14.W_3_39_lower`

Solved: stated here without proof.

> $W(3, 39) > 1418$ from [AKS14, Table 3], proved by an explicit good partition.

```lean
theorem W_3_39_lower : W 3 39 > 1418
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/14.lean, line 364](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean#L364).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/14.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/14.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.14)
