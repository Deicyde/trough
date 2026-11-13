---
declaration: theorem
origin: cited
lean: Erdos873.erdos_873, Erdos873.erdos_873.variants.triple_upper_bound, Erdos873.erdos_873.variants.triple_lower_bound_infinitely_often, Erdos873.erdos_873.variants.supplement_all_scale
statement: formalized
---

# Erdős Problem 873

> *References:*
> - [erdosproblems.com/873](https://www.erdosproblems.com/873)
> - [Er92c] Erdős, P., Some of my forgotten problems in number theory. Hardy-Ramanujan J. 15
>   (1992), 34-50.

*Quoted from [FormalConjectures/ErdosProblems/873.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/873.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/873](https://www.erdosproblems.com/873).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos873.erdos_873`

Open: stated without proof.

> Let $A = \{a_1 < a_2 < \dots\} \subseteq \mathbb{N}$ and let $F(A,X,k)$ count the number of $i$
> such that $[a_i,a_{i+1}, \dots ,a_{i+k−1}] < X$, where the left-hand side is the least common
> multiple. Is it true that, for every $\epsilon > 0$, there exists some $k$ such that
> $F(A,X,k) < X^\epsilon$?

```lean
theorem erdos_873 : ∀ᵉ (a : ℕ → ℕ) (ε > (0 : ℝ)), 0 < a 0 → StrictMono a →
    ∃ k, ∀ X > 0, F a X k < (X^ε).toEReal
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/873.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/873.lean#L44).

## `Erdos873.erdos_873.variants.triple_upper_bound`

Solved: stated here without proof.

> The upper bound (2).

```lean
theorem erdos_873.variants.triple_upper_bound :
    ∃ C : ℝ, 0 < C ∧
      ∀ (a : ℕ → ℕ), 0 < a 0 → StrictMono a →
        ∀ᶠ X : ℝ in Filter.atTop,
          (F a X 3 : EReal) ≤
            (C * X ^ (1 / 3 : ℝ) * Real.log X).toEReal
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/873.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/873.lean#L56).

## `Erdos873.erdos_873.variants.triple_lower_bound_infinitely_often`

Solved: stated here without proof.

> The infinitely-often lower bound (3).

```lean
theorem erdos_873.variants.triple_lower_bound_infinitely_often :
    ∃ (a : ℕ → ℕ) (c : ℝ),
      0 < a 0 ∧ StrictMono a ∧ 0 < c ∧
        ∀ X₀ : ℝ, ∃ X > X₀,
          (c * X ^ (1 / 3 : ℝ) * Real.log X).toEReal ≤ (F a X 3 : EReal)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/873.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/873.lean#L66).

## `Erdos873.erdos_873.variants.supplement_all_scale`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-873-lean/blob/44cbf183239517795522bd3f18124b08c095cc6d/lean/RealBridge.lean#L138-L146](https://github.com/KitaKen1/erdos-873-lean/blob/44cbf183239517795522bd3f18124b08c095cc6d/lean/RealBridge.lean#L138-L146).

> There may be a sequence for which the lower bound in (3) holds for every $X$, that is, for
> all sufficiently large $X$ rather than only for infinitely many $X$. (Asking it for every
> $X > 0$ fails trivially: the lcm of three distinct positive integers is at least $4$, so
> $F(A,X,3) = 0$ for $X \le 4$.)

```lean
theorem erdos_873.variants.supplement_all_scale :
    ¬ ∃ (a : ℕ → ℕ) (c : ℝ),
      0 < a 0 ∧ StrictMono a ∧ 0 < c ∧
        ∀ᶠ X : ℝ in Filter.atTop,
          (c * X ^ (1 / 3 : ℝ) * Real.log X).toEReal ≤ (F a X 3 : EReal)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/873.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/873.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/873.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/873.lean)
- [erdosproblems.com/873](https://www.erdosproblems.com/873)
