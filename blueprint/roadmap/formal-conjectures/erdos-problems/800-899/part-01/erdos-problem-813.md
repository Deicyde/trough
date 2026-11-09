---
declaration: theorem
origin: cited
lean: Erdos813.erdos_813, Erdos813.erdos_813.variants.erdos_hajnal, Erdos813.erdos_813.variants.bucic_sudakov, Erdos813.erdos_813.variants.lower, Erdos813.erdos_813.variants.upper
statement: formalized
---

# Erdős Problem 813

> *References:*
> - [erdosproblems.com/813](https://www.erdosproblems.com/813)
> - [Er91] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Graph theory, combinatorics, and applications, Vol. 1 (Kalamazoo, MI, 1988) (1991),
>   397-406.
> - [BuSu23] Bucić, M. and Sudakov, B., *Large independent sets from local considerations*.
>   Combinatorica 43 (2023), 505-546. [arXiv:2007.03667](https://arxiv.org/abs/2007.03667)

*Quoted from [FormalConjectures/ErdosProblems/813.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/813.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/813](https://www.erdosproblems.com/813).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 2 test statements, counted here but not shown.

## `Erdos813.erdos_813`

Open: stated without proof.

> Let $h(n)$ be minimal such that every graph on $n$ vertices where every set of $7$ vertices
> contains a triangle must contain a clique on at least $h(n)$ vertices. Estimate $h(n)$. In
> particular, do there exist constants $c_1, c_2 > 0$ such that
> $$n^{1/3+c_1} \ll h(n) \ll n^{1/2-c_2}?$$
>
> The lower half has a positive answer (`Erdos813.erdos_813.variants.lower`); the upper half is
> `Erdos813.erdos_813.variants.upper`.

```lean
theorem erdos_813 :
    ∃ c₁ > (0 : ℝ), ∃ c₂ > (0 : ℝ),
      (fun n : ℕ ↦ (n : ℝ) ^ (1 / 3 + c₁ : ℝ)) =O[atTop] (fun n ↦ (h n : ℝ)) ∧
        (fun n : ℕ ↦ (h n : ℝ)) =O[atTop] (fun n : ℕ ↦ (n : ℝ) ^ (1 / 2 - c₂ : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/813.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/813.lean#L109).

## `Erdos813.erdos_813.variants.erdos_hajnal`

Solved: stated here without proof.

> Erdős and Hajnal proved (see [Er91]) that
> $$n^{1/3} \ll h(n) \ll n^{1/2}.$$

```lean
theorem erdos_813.variants.erdos_hajnal :
    (fun n : ℕ ↦ (n : ℝ) ^ (1 / 3 : ℝ)) =O[atTop] (fun n ↦ (h n : ℝ)) ∧
      (fun n : ℕ ↦ (h n : ℝ)) =O[atTop] (fun n : ℕ ↦ (n : ℝ) ^ (1 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/813.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/813.lean#L120).

## `Erdos813.erdos_813.variants.bucic_sudakov`

Solved: stated here without proof.

> Bucić and Sudakov [BuSu23] proved that $h(n) \gg n^{5/12-o(1)}$. Their result is stated for
> graphs in which every $7$ vertices contain an independent set of size $3$; it applies to $h$
> by taking complements.

```lean
theorem erdos_813.variants.bucic_sudakov :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (n : ℝ) ^ (5 / 12 - ε : ℝ) ≤ (h n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/813.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/813.lean#L131).

## `Erdos813.erdos_813.variants.lower`

Solved: stated here without proof.

> The lower half of `Erdos813.erdos_813` has a positive answer: there is a constant $c_1 > 0$
> with $n^{1/3+c_1} \ll h(n)$. This follows from the bound $h(n) \gg n^{5/12-o(1)}$ of Bucić and
> Sudakov [BuSu23], since $5/12 > 1/3$.

```lean
theorem erdos_813.variants.lower :
    ∃ c₁ > (0 : ℝ), (fun n : ℕ ↦ (n : ℝ) ^ (1 / 3 + c₁ : ℝ)) =O[atTop] (fun n ↦ (h n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/813.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/813.lean#L141).

## `Erdos813.erdos_813.variants.upper`

Open: stated without proof.

> The upper half of `Erdos813.erdos_813`: is there a constant $c_2 > 0$ with
> $h(n) \ll n^{1/2-c_2}$?

```lean
theorem erdos_813.variants.upper :
    ∃ c₂ > (0 : ℝ), (fun n : ℕ ↦ (h n : ℝ)) =O[atTop] (fun n : ℕ ↦ (n : ℝ) ^ (1 / 2 - c₂ : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/813.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/813.lean#L150).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/813.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/813.lean)
- [erdosproblems.com/813](https://www.erdosproblems.com/813)
