---
declaration: theorem
origin: cited
lean: Erdos686.erdos_686, Erdos686.erdos_686.variants.square, Erdos686.erdos_686.variants.four, Erdos686.erdos_686.variants.four_two, Erdos686.erdos_686.variants.four_three, Erdos686.erdos_686.variants.nine, Erdos686.erdos_686.variants.twenty_five, Erdos686.erdos_686.variants.non_square
statement: formalized
---

# Erdős Problem 686

> *References:*
> - [erdosproblems.com/686](https://www.erdosproblems.com/686)
> - [Er79d] Erdős, P., *Some unconventional problems in number theory*. Acta Math.
>   Acad. Sci. Hungar. (1979), 71-80.

*Quoted from [FormalConjectures/ErdosProblems/686.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/686](https://www.erdosproblems.com/686).

The file states 8 research or textbook statements: 4 open and 4 solved.

## `Erdos686.erdos_686`

Open: stated without proof.

> Can every integer $N≥2$ be written as
> $$N=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
> for some $k≥2$ and $m≥n+k$?

```lean
theorem erdos_686 :
    ∀ N ≥ (2 : ℕ), ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (N : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L39).

## `Erdos686.erdos_686.variants.square`

Open: stated without proof.

> Can every square $N≥2$ be written as
> $$N=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
> for some $k≥2$ and $m≥n+k$?

```lean
theorem erdos_686.variants.square :
    ∀ N ≥ (2 : ℕ),  (IsSquare N) → ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (N : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L50).

## `Erdos686.erdos_686.variants.four`

Open: stated without proof.

> Can $4$ be written as
> $$4=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
> for some $k≥2$ and $m≥n+k$?

```lean
theorem erdos_686.variants.four :
    ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (4 : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L61).

## `Erdos686.erdos_686.variants.four_two`

Proved here.

> The number $4$ cannot be written as
> $$4=\frac{\prod_{1\leq i\leq 2}(m+i)}{\prod_{1\leq i\leq 2}(n+i)}$$
> for $m≥n+2$!

```lean
theorem erdos_686.variants.four_two :
    ¬ ∃ᵉ (n : ℕ) (m ≥ n + 2),
      (4 : ℚ) = (∏ i ∈ Finset.Icc 1 2, (m + i)) / (∏ i ∈ Finset.Icc 1 2, (n + i))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L72).

## `Erdos686.erdos_686.variants.four_three`

Solved: stated here without proof.

> The number $4$ cannot be written as
> $$4=\frac{\prod_{1\leq i\leq 3}(m+i)}{\prod_{1\leq i\leq 3}(n+i)}$$
> for $m≥n+3$!
>
> See [comment section on erdosproblems.com](https://www.erdosproblems.com/forum/thread/686#post-4599)

```lean
theorem erdos_686.variants.four_three :
    ¬ ∃ᵉ (n : ℕ) (m ≥ n + 3),
      (4 : ℚ) = (∏ i ∈ Finset.Icc 1 3, (m + i)) / (∏ i ∈ Finset.Icc 1 3, (n + i))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L93).

## `Erdos686.erdos_686.variants.nine`

Proved here.

> Can $9$ be written as
> $$9=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
> for some $k≥2$ and $m≥n+k$?

```lean
theorem erdos_686.variants.nine :
    ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (9 : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L104).

## `Erdos686.erdos_686.variants.twenty_five`

Open: stated without proof.

> Can $25$ be written as
> $$25=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
> for some $k≥2$ and $m≥n+k$?

```lean
theorem erdos_686.variants.twenty_five :
    ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (25 : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L117).

## `Erdos686.erdos_686.variants.non_square`

Proved here.

> Can every non-square $N≥2$ be written as
> $$N=\frac{\prod_{1\leq i\leq k}(m+i)}{\prod_{1\leq i\leq k}(n+i)}$$
> for some $k≥2$ and $m≥n+k$?

```lean
theorem erdos_686.variants.non_square :
    ∀ N ≥ (2 : ℕ), (¬ IsSquare N) → ∃ᵉ (k ≥ 2) (n : ℕ) (m ≥ n + k),
      (N : ℚ) = (∏ i ∈ Finset.Icc 1 k, (m + i)) / (∏ i ∈ Finset.Icc 1 k, (n + i))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/686.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean#L128).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/686.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/686.lean)
- [erdosproblems.com/686](https://www.erdosproblems.com/686)
