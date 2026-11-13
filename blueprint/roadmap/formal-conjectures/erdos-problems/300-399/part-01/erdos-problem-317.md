---
declaration: theorem
origin: cited
lean: Erdos317.erdos_317, Erdos317.erdos_317.variants.claim2, Erdos317.claim2_inequality, Erdos317.erdos_317.variants.counterexample
statement: formalized
---

# Erdős Problem 317

> *Reference:* [erdosproblems.com/317](https://www.erdosproblems.com/317)

*Quoted from [FormalConjectures/ErdosProblems/317.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/317.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/317](https://www.erdosproblems.com/317).

The file states 4 research or textbook statements: 2 open and 2 textbook results.

## `Erdos317.erdos_317`

Open: stated without proof.

> Is there some constant $c>0$ such that for every $n\geq 1$ there exists some $\delta_k\in \{-1,0,1\}$ for $1\leq k\leq n$ with
>
> $$0< \left\lvert \sum_{1\leq k\leq n}\frac{\delta_k}{k}\right\rvert < \frac{c}{2^n}?$$

```lean
theorem erdos_317 :
    ∃ c > 0, ∀ n ≥ 1, ∃ δ : Fin n → ℚ,
      Set.range δ ⊆ {-1, 0, 1} ∧
      letI lhs : ℝ := |∑ k, (δ k) / (k + 1)|
      0 < lhs ∧ lhs < c / 2^n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/317.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/317.lean#L37).

## `Erdos317.erdos_317.variants.claim2`

Open: stated without proof.

> Is it true that for sufficiently large $n$, for any $\delta_k\in \{-1,0,1\}$,
>
> $$\left\lvert \sum_{1\leq k\leq n}\frac{\delta_k}{k}\right\rvert > \frac{1}{[1,\ldots,n]}$$
>
> whenever the left-hand side is not zero?

```lean
theorem erdos_317.variants.claim2 :
    ∀ᶠ n in atTop, ∀ δ : (Fin n) → ℚ, δ '' Set.univ ⊆ {-1,0,1} →
    letI lhs := |∑ k, ((δ k : ℚ) / (k + 1))|
    lhs ≠ 0 → lhs > 1 / (Icc 1 n).lcm id
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/317.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/317.lean#L50).

## `Erdos317.claim2_inequality`

Textbook result, stated without proof.

> Inequality in `erdos_317.variants.claim2` is obvious, the problem is strict inequality.

```lean
lemma claim2_inequality : ∀ᶠ n in atTop,
    ∀ δ : (Fin n) → ℚ, δ '' Set.univ ⊆ {-1,0,1} →
    letI lhs := |∑ k, ((δ k : ℚ) / (k + 1))|
    lhs ≠ 0 → lhs ≥ 1 / (Icc 1 n).lcm id
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/317.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/317.lean#L60).

## `Erdos317.erdos_317.variants.counterexample`

Textbook result, proved here.

> `erdos_317.variants.claim2` fails for small $n$, for example
>
> $$\frac{1}{2}-\frac{1}{3}-\frac{1}{4}=-\frac{1}{12}.$$

```lean
theorem erdos_317.variants.counterexample : ¬ (∀  δ : (Fin 4) → ℚ, δ '' Set.univ ⊆ {-1,0,1} →
    letI lhs := |∑ k, ((δ k : ℚ) / (k + 1))|
    lhs ≠ 0 → lhs > (1 : ℚ) / ((Icc 1 4).lcm id : ℕ))
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/317.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/317.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/317.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/317.lean)
- [erdosproblems.com/317](https://www.erdosproblems.com/317)
