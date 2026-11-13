---
declaration: theorem
origin: cited
lean: Erdos1119.erdos_1119, Erdos1119.erdos_1119.variants.easy_case, Erdos1119.erdos_1119.variants.erdos_wetzel, Erdos1119.erdos_1119.variants.erdos_wetzel_ch
statement: formalized
---

# Erdős Problem 1119

> *References:*
> - [erdosproblems.com/1119](https://www.erdosproblems.com/1119)
> - [Ha74] Hayman, W. K., Research problems in function theory: new problems. (1974), 155--180.
> - [Er64g] Erdős, P., An interpolation problem associated with the continuum hypothesis.
>   Michigan Math. J. (1964), 9--10.
> - [KuSh17] Kumar, Ashutosh and Shelah, Saharon, On a question about families of entire
>   functions. Fund. Math. (2017), 279--288.
> - [ScWe24] Schilhan, Jonathan and Weinert, Thilo, Wetzel families and the continuum.
>   J. Lond. Math. Soc. (2) (2024), Paper No. e12918, 27.

*Quoted from [FormalConjectures/ErdosProblems/1119.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1119.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1119](https://www.erdosproblems.com/1119).

The file states 4 research or textbook statements: 4 solved. It also has 1 test statement, counted here but not shown.

## `Erdos1119.erdos_1119`

Solved: stated here without proof.

> Let $\mathfrak{m}$ be an infinite cardinal with $\aleph_0 < \mathfrak{m} < \mathfrak{c} =
> 2^{\aleph_0}$. Let $\{f_\alpha\}$ be a family of entire functions such that, for every
> $z_0 \in \mathbb{C}$, there are at most $\mathfrak{m}$ distinct values of $f_\alpha(z_0)$.
> Must $\{f_\alpha\}$ have cardinality at most $\mathfrak{m}$?
>
> This is Problem 2.46 in [Ha74], where it is attributed to Erdős. The question is
> **independent of ZFC**: the headline statement is neither provable nor refutable from the
> usual axioms of set theory, so its `sorry` cannot be filled either way.
>
> The answer is yes if $\mathfrak{m}^+ < \mathfrak{c}$ (see
> `erdos_1119.variants.easy_case`), so the question reduces to the case
> $\mathfrak{m}^+ = \mathfrak{c}$, where it is undecidable: Kumar and Shelah [KuSh17]
> produced a model of $\mathfrak{c} = \aleph_2$ in which the answer is yes (with
> $\mathfrak{m} = \aleph_1$), while Schilhan and Weinert [ScWe24] produced a different
> model of $\mathfrak{c} = \aleph_2$ in which the answer is no.

```lean
theorem erdos_1119 :
    ∀ (m : Cardinal.{0}), ℵ₀ < m → m < 𝔠 →
    ∀ F : Set (ℂ → ℂ), (∀ f ∈ F, Differentiable ℂ f) →
      (∀ z₀ : ℂ, #{y : ℂ | ∃ f ∈ F, f z₀ = y} ≤ m) →
      #F ≤ m
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1119.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1119.lean#L59).

## `Erdos1119.erdos_1119.variants.easy_case`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1119.lean#L203](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1119.lean#L203).

> The 'easy' case of Erdős Problem 1119: if moreover $\mathfrak{m}^+ < \mathfrak{c}$, then
> any family of entire functions taking at most $\mathfrak{m}$ distinct values at each
> point has cardinality at most $\mathfrak{m}$. In [Ha74] it is written that this is
> 'easy to see'.

```lean
theorem erdos_1119.variants.easy_case (m : Cardinal.{0}) (hm : ℵ₀ < m)
    (hsucc : succ m < 𝔠) (F : Set (ℂ → ℂ))
    (hF : ∀ f ∈ F, Differentiable ℂ f)
    (hval : ∀ z₀ : ℂ, #{y : ℂ | ∃ f ∈ F, f z₀ = y} ≤ m) :
    #F ≤ m
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1119.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1119.lean#L92).

## `Erdos1119.erdos_1119.variants.erdos_wetzel`

Solved: stated here without proof.

> Erdős's theorem [Er64g], answering a question of Wetzel: if $\mathfrak{c} > \aleph_1$,
> then every family of entire functions taking only countably many distinct values at each
> point $z_0 \in \mathbb{C}$ is itself countable.

```lean
theorem erdos_1119.variants.erdos_wetzel (h : ℵ_ 1 < 𝔠) (F : Set (ℂ → ℂ))
    (hF : ∀ f ∈ F, Differentiable ℂ f)
    (hval : ∀ z₀ : ℂ, {y : ℂ | ∃ f ∈ F, f z₀ = y}.Countable) :
    F.Countable
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1119.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1119.lean#L105).

## `Erdos1119.erdos_1119.variants.erdos_wetzel_ch`

Solved: stated here without proof.

> Erdős [Er64g] also showed that the previous statement fails under the continuum
> hypothesis: if $\mathfrak{c} = \aleph_1$, then there is an **uncountable** family of
> entire functions taking only countably many distinct values at each point
> $z_0 \in \mathbb{C}$.

```lean
theorem erdos_1119.variants.erdos_wetzel_ch (h : 𝔠 = ℵ_ 1) :
    ∃ F : Set (ℂ → ℂ), (∀ f ∈ F, Differentiable ℂ f) ∧
      (∀ z₀ : ℂ, {y : ℂ | ∃ f ∈ F, f z₀ = y}.Countable) ∧
      ¬ F.Countable
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1119.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1119.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1119.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1119.lean)
- [erdosproblems.com/1119](https://www.erdosproblems.com/1119)
