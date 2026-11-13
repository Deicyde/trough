---
declaration: theorem
origin: cited
lean: Green43.green_43, Green43.green_43.variants.alon_peres, Green43.green_43.variants.range_N051_N052, Green43.green_43.variants.range_N051_N052_linear, Green43.green_43.variants.general_exponent, Green43.green_43.variants.general_exponent_lt_half
statement: formalized
---

# Ben Green's Open Problem 43

> *References:*
> - [Gr24] [Ben Green's Open Problem 43](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.43)
> - [Gr18] Green, Ben. "A note on multiplicative functions on progressions to large moduli."
>   Proc. Roy. Soc. Edinburgh Sect. A 148 (2018), no. 1, 63–77. (Problem 43 is formulated here,
>   [Gr18, Section 4].)
> - [AP92] Alon, Noga, and Yuval Peres. "Uniform dilations." Geometric and Functional Analysis
>   2 (1992), no. 1, 1–28. (Source of the favourite variant in [Gr24, Comments to Problem 43].)

*Quoted from [FormalConjectures/GreensOpenProblems/43.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 5 open and 1 solved. It also has 3 test statements, counted here but not shown.

## `Green43.green_43`

Open: stated without proof.

> Let $N$ be a large integer. For each prime $p$ with $N^{0.51} \leq p < 2N^{0.51}$, pick some
> residue $a(p) \in \mathbb{Z}/p\mathbb{Z}$. Is it true that
>
> $$\#\{n \in [N] : n \equiv a(p) \pmod{p} \text{ for some } p\} \gg N^{1-o(1)}?$$

```lean
theorem green_43 : SievedLowerBoundExp (0.51 : ℝ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/43.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean#L69).

## `Green43.green_43.variants.alon_peres`

Open: stated without proof.

> [Gr24, Comments to Problem 43; AP92] One of Green's favourite related conjectures: if
> `A ⊆ ℤ/pℤ` is a set of size `⌊p/2⌋`, does some dilation `n A` (`n` an integer) have no gaps of
> length more than `p^{0.49}`?
>
> The question is asymptotic, so it is stated for all sufficiently large primes `p` (see the
> large-prime discussion in [AP92, §2]); for small primes it fails trivially, e.g. `p = 3`, `A = {0}`.

```lean
theorem green_43.variants.alon_peres :
    ∀ᶠ p : ℕ in atTop, p.Prime → ∀ A : Finset (ZMod p), A.card = p / 2 →
    ∃ n : ZMod p, ∀ L : ℕ, (p : ℝ) ^ (0.49 : ℝ) < (L : ℝ) → ¬ HasGap (Dilate n A) L
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/43.lean, line 140](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean#L140).

## `Green43.green_43.variants.range_N051_N052`

Open: stated without proof.

> [Gr24, Comments to Problem 43] A minor variant of Problem 43: the same question but with `p`
> ranging over `N^{0.51} ≤ p < N^{0.52}`. Obtaining the lower bound `N^{1-o(1)}` here is no harder
> than Problem 43, but is not known.

```lean
theorem green_43.variants.range_N051_N052 :
    SievedLowerBound (fun N => (N : ℝ) ^ (0.51 : ℝ)) (fun N => (N : ℝ) ^ (0.52 : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/43.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean#L151).

## `Green43.green_43.variants.range_N051_N052_linear`

Open: stated without proof.

> [Gr24, Comments to Problem 43] For the range `N^{0.51} ≤ p < N^{0.52}` there may even be a
> linear lower bound `c N`.

```lean
theorem green_43.variants.range_N051_N052_linear :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ N : ℕ in atTop, ∀ a : ℕ → ℤ,
      c * N ≤ sievedCard N a ((N : ℝ) ^ (0.51 : ℝ)) ((N : ℝ) ^ (0.52 : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/43.lean, line 160](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean#L160).

## `Green43.green_43.variants.general_exponent`

Open: stated without proof.

> [Gr24, Comments to Problem 43] One can replace the exponent `0.51` by any other exponent `α`:
> does the lower bound `N^{1-o(1)}` hold for sieving primes in `[N^α, 2 N^α)` for every exponent
> `0 < α < 1`? Problem 43 is the case `α = 0.51`; the regime `α < 1/2` is the solved special case
> `green_43.variants.general_exponent_lt_half`, while progress for `α ≈ 1` would imply Kakeya.

```lean
theorem green_43.variants.general_exponent :
    ∀ α : ℝ, 0 < α → α < 1 → SievedLowerBoundExp α
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/43.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean#L173).

## `Green43.green_43.variants.general_exponent_lt_half`

Solved: stated here without proof.

> [Gr24, Comments to Problem 43] For exponents `α < 1/2` the lower bound `N^{1-o(1)}` is
> straightforward (by an inclusion–exclusion or Cauchy–Schwarz argument). This is the solved
> special case of `green_43.variants.general_exponent`.

```lean
theorem green_43.variants.general_exponent_lt_half :
    ∀ α : ℝ, 0 < α → α < 1 / 2 → SievedLowerBoundExp α
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/43.lean, line 183](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean#L183).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/43.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/43.lean)
- [Ben Green's Open Problem 43](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.43)
