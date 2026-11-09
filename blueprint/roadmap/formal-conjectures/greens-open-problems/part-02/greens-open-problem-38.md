---
declaration: theorem
origin: cited
lean: Green38.green_38.lower, Green38.green_38.upper, Green38.green_38.variants.best_lower, Green38.green_38.variants.lower_itty_rosin_carstensen_reichman, Green38.green_38.variants.best_upper
statement: formalized
---

# Green's Open Problem 38

> *References:*
> - [100 open problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.38)
> - [La79] Lovász, László. "On the Shannon capacity of a graph."
>   IEEE Transactions on Information theory 25.1 (1979): 1-7.
> - [Po20] Polak, Sven. "New methods in coding theory: Error-correcting codes and the Shannon capacity."
>   arXiv preprint arXiv:2005.02945 (2020).
> - [IRCR26] Itty, Nathaniel and Rosin, Christopher D. and Carstensen, Chase and Reichman, Daniel.
>   "Improved lower bounds for the Shannon capacity of odd cycles." arXiv:2607.21517 (2026).
> - [Ga26] Gao, Yu. "A recursive construction improving the lower bound on the Shannon capacity of
>   $C_7$." arXiv:2607.27869 (2026).
> - [BPZ26] Buys, Pjotr and Polak, Sven and Zuiddam, Jeroen. "Lean-verified lower bounds for the
>   Shannon capacity of odd cycles." arXiv:2607.29681 (2026). Lean formalisation:
>   https://github.com/spectra-research/shannon-capacity-lean

*Quoted from [FormalConjectures/GreensOpenProblems/38.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/38.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 3 test statements, counted here but not shown.

## `Green38.green_38.lower`

Solved: stated here without proof.

> Can we improve the lower bound? The answer sequence must be eventually nonnegative, since
> `=O` compares norms.
>
> Yes. Itty, Rosin, Carstensen and Reichman [IRCR26] found a valid set of size $134753$ in
> $\mathbb{F}_7^{10}$ (an independent set in the tenth strong power of $C_7$). Taking products
> gives valid sets of size $134753^{\lfloor n/10 \rfloor}$ in $\mathbb{F}_7^n$, see
> `green_38.variants.lower_itty_rosin_carstensen_reichman`, so the growth rate is at least
> $134753^{1/10} > 3.258020 > C_1$ (note $134753 > 367^2 = 134689$). Gao [Ga26] and then Buys,
> Polak and Zuiddam [BPZ26] improved the rate further, to $3.258789\ldots$ and $3.2588\ldots$
> respectively; the latter is formalised in Lean. The exact growth rate remains open.

```lean
theorem green_38.lower :
    (∀ᶠ n in atTop, 0 ≤ green_38.lower.answer n) ∧ green_38.lower.answer ≤ᶠ[atTop]
      LargestAdmissibleCardinality ∧
    ∃ c > C₁, (fun n ↦ c ^ n) =O[atTop] green_38.lower.answer
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/38.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/38.lean#L95).

## `Green38.green_38.upper`

Open: stated without proof.

> Can we improve the best upper bound? The base `c` must be positive, since `=O` compares
> norms.

```lean
theorem green_38.upper :
    LargestAdmissibleCardinality ≤ᶠ[atTop] green_38.upper.answer ∧
    ∃ c : ℝ, 0 < c ∧ c < C₂ ∧ green_38.upper.answer =O[atTop] (fun n ↦ c ^ n)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/38.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/38.lean#L106).

## `Green38.green_38.variants.best_lower`

Solved: stated here without proof.

> The lower bound $(C_1 - o(1))^n \leqslant |A|$ where $C_1 = 367^{1/5} \approx 3.2578$, from a
> valid set of size $367$ in $\mathbb{F}_7^5$ [Po20, Section 9.1]. This was the best known bound
> when Green's list was written; it has since been improved, see `green_38.lower`.

```lean
theorem green_38.variants.best_lower :
    ∀ ε ∈ Set.Ioo (0 : ℝ) C₁, ∀ᶠ n in atTop, (C₁ - ε) ^ n ≤ LargestAdmissibleCardinality n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/38.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/38.lean#L116).

## `Green38.green_38.variants.lower_itty_rosin_carstensen_reichman`

Solved: stated here without proof.

> Itty, Rosin, Carstensen and Reichman [IRCR26] found a valid set of size $134753$ in
> $\mathbb{F}_7^{10}$. Products of copies of it, padded with zero coordinates, give
> $134753^{\lfloor n/10 \rfloor} \leqslant |A|$ in $\mathbb{F}_7^n$.

```lean
theorem green_38.variants.lower_itty_rosin_carstensen_reichman (n : ℕ) :
    (134753 : ℝ) ^ (n / 10) ≤ LargestAdmissibleCardinality n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/38.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/38.lean#L125).

## `Green38.green_38.variants.best_upper`

Solved: stated here without proof.

> The current best upper bound is $|A| \leqslant (C_2 + o(1))^n$ where
> $C_2 = \frac{7 \cos(\pi/7)}{1 + \cos(\pi/7)} \approx 3.3177$ [La79, Corollary 5].

```lean
theorem green_38.variants.best_upper :
    ∀ ε > 0, ∀ᶠ n in atTop, LargestAdmissibleCardinality n ≤ (C₂ + ε) ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/38.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/38.lean#L132).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/38.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/38.lean)
- [100 open problems](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.38)
