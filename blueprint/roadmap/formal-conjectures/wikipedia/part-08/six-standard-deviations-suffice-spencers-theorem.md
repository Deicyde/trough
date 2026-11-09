---
declaration: theorem
origin: cited
lean: SixStandardDeviations.six_standard_deviations, SixStandardDeviations.six_standard_deviations.variants.random_bound, SixStandardDeviations.six_standard_deviations.variants.universal_bound
statement: formalized
---

# Six standard deviations suffice (Spencer's theorem)

> Spencer's theorem in discrepancy theory: for every $n$ and every family of $n$ subsets
> $S_1, \dots, S_n$ of $\{1, \dots, n\}$, there is a colouring
> $\chi : \{1, \dots, n\} \to \{-1, +1\}$ such that
>
> $$\left|\sum_{j \in S_i} \chi(j)\right| \le 6\sqrt{n}$$
>
> for every $i$.
>
> A uniformly random colouring only achieves the bound $O(\sqrt{n \log n})$, so Spencer's
> theorem ("six standard deviations suffice") is a genuine improvement over the basic
> probabilistic method; its proof uses a partial-colouring argument based on the entropy
> method, and the bound $\Theta(\sqrt{n})$ is tight up to the value of the constant.
> Spencer's original argument is non-constructive; polynomial-time algorithms achieving
> $O(\sqrt{n})$ were later found by Bansal (2010) and Lovett–Meka (2012).
>
> The Komlós conjecture (the subject of a companion file in this directory) would
> strengthen this theorem: applied to the incidence vectors of the sets, scaled by
> $1/\sqrt{n}$, it would give a discrepancy bound $O(\sqrt{n})$ for any number of sets,
> not just $n$ of them.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Discrepancy_of_hypergraphs#General_hypergraphs)
> - [J. Spencer, *Six standard deviations suffice*,
>   Trans. Amer. Math. Soc. **289** (1985), 679–706](https://doi.org/10.1090/S0002-9947-1985-0784009-0)
> - [N. Bansal, *Constructive algorithms for discrepancy minimization*,
>   FOCS 2010, 3–10](https://doi.org/10.1109/FOCS.2010.7)
> - [S. Lovett and R. Meka, *Constructive discrepancy minimization by walking on the edges*,
>   SIAM J. Comput. **44** (2015), 1573–1582](https://doi.org/10.1137/130929400)

*Quoted from [FormalConjectures/Wikipedia/SixStandardDeviations.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SixStandardDeviations.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 1 test statement, counted here but not shown.

## `SixStandardDeviations.six_standard_deviations`

Solved: stated here without proof.

> **Six standard deviations suffice** (Spencer, 1985)
>
> For every $n$ and every family of $n$ subsets $S_1, \dots, S_n$ of $\{1, \dots, n\}$,
> there is a colouring $\chi : \{1, \dots, n\} \to \{-1, +1\}$ such that
> $\left|\sum_{j \in S_i} \chi(j)\right| \le 6\sqrt{n}$ for every $i$.

```lean
theorem six_standard_deviations :
    ∀ (n : ℕ) (S : Fin n → Finset (Fin n)),
      ∃ χ : Fin n → ℝ, (∀ j, χ j = 1 ∨ χ j = -1) ∧
        ∀ i, |∑ j ∈ S i, χ j| ≤ 6 * Real.sqrt n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SixStandardDeviations.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SixStandardDeviations.lean#L63).

## `SixStandardDeviations.six_standard_deviations.variants.random_bound`

Solved: stated here; a Lean proof is at [https://github.com/Lemmy00/spencer-random-coloring-lean/blob/a691214a7263c1010fdd10560091e9f8cfce903a/SpencerRandomColoring/RandomBound.lean#L37](https://github.com/Lemmy00/spencer-random-coloring-lean/blob/a691214a7263c1010fdd10560091e9f8cfce903a/SpencerRandomColoring/RandomBound.lean#L37).

> **The random colouring bound**
>
> There is a constant $K > 0$ such that for every $n$ and every family of $n$ subsets
> $S_1, \dots, S_n$ of $\{1, \dots, n\}$, there is a colouring
> $\chi : \{1, \dots, n\} \to \{-1, +1\}$ with
> $\left|\sum_{j \in S_i} \chi(j)\right| \le K \sqrt{n \log(n + 2)}$ for every $i$.
> This follows from a Chernoff bound applied to a uniformly random colouring, and is
> the benchmark that Spencer's theorem improves upon by removing the logarithmic
> factor. (The shift $n + 2$ inside the logarithm is a harmless normalization keeping
> it positive for $n \in \{0, 1\}$.)

```lean
theorem six_standard_deviations.variants.random_bound :
    ∃ K : ℝ, 0 < K ∧ ∀ (n : ℕ) (S : Fin n → Finset (Fin n)),
      ∃ χ : Fin n → ℝ, (∀ j, χ j = 1 ∨ χ j = -1) ∧
        ∀ i, |∑ j ∈ S i, χ j| ≤ K * Real.sqrt (n * Real.log (n + 2))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SixStandardDeviations.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SixStandardDeviations.lean#L85).

## `SixStandardDeviations.six_standard_deviations.variants.universal_bound`

Solved: stated here; a Lean proof is at [https://github.com/Lemmy00/spencer-universal-bound-lean/blob/e8d83c0a99f7c1be5a04aa155164bc477d2c6df3/Spencer/UniversalBound.lean#L15](https://github.com/Lemmy00/spencer-universal-bound-lean/blob/e8d83c0a99f7c1be5a04aa155164bc477d2c6df3/Spencer/UniversalBound.lean#L15).

> **A universal discrepancy bound**
>
> There is a positive universal constant $K$ such that every family of $n$ subsets
> of the `n` points has a colouring with discrepancy at most $K\sqrt{n}$ in every
> row. This qualitative form has the optimal order of growth, but it does not assert
> the constant $6$ in Spencer's theorem.

```lean
theorem six_standard_deviations.variants.universal_bound :
    ∃ K : ℝ, 0 < K ∧ ∀ (n : ℕ) (S : Fin n → Finset (Fin n)),
      ∃ χ : Fin n → ℝ, (∀ j, χ j = 1 ∨ χ j = -1) ∧
        ∀ i, |∑ j ∈ S i, χ j| ≤ K * Real.sqrt n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SixStandardDeviations.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SixStandardDeviations.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SixStandardDeviations.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SixStandardDeviations.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Discrepancy_of_hypergraphs#General_hypergraphs)
