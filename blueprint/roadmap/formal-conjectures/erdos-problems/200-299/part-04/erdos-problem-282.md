---
declaration: theorem
origin: cited
lean: Erdos282.erdos_282, Erdos282.erdos_282.variants.general, Erdos282.erdos_282.variants.fibonacci, Erdos282.erdos_282.variants.graham, Erdos282.erdos_282.variants.sq
statement: formalized
---

# Erdős Problem 282

> *Reference:* [erdosproblems.com/282](https://www.erdosproblems.com/282)

*Quoted from [FormalConjectures/ErdosProblems/282.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/282.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/282](https://www.erdosproblems.com/282).

The file states 5 research or textbook statements: 4 open and 1 textbook result. It also has 3 test statements, counted here but not shown.

## `Erdos282.erdos_282`

Open: stated without proof.

> Let $A\subseteq \mathbb{N}$ be an infinite set and consider the following
> greedy algorithm for a rational $x\in (0,1)$: choose the minimal $n\in A$ not used
> so far such that $n\geq 1/x$ and repeat with $x$ replaced by $x-\frac{1}{n}$. If this
> terminates after finitely many steps then this produces a representation of
> $x$ as the sum of distinct unit fractions with denominators from $A$.
>
> Does this process always terminate if $x$ has odd denominator and $A$ is the
> set of odd numbers?

```lean
theorem erdos_282 {x : ℚ} (hx : x ∈ Set.Ioo 0 1) (hx_den : Odd x.den) :
    greedyUnitFractionRem { n | Odd n } x =ᶠ[atTop] 0
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/282.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/282.lean#L67).

## `Erdos282.erdos_282.variants.general`

Open: stated without proof.

> More generally, for which pairs $x$ and $A$ does this process terminate?

```lean
theorem erdos_282.variants.general (x : ℚ) (A : Set ℕ) :
      greedyUnitFractionRem A x =ᶠ[atTop] 0 ↔ (x, A) ∈ erdos_282.variants.general.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/282.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/282.lean#L75).

## `Erdos282.erdos_282.variants.fibonacci`

Textbook result, stated without proof.

> In 1202 Fibonacci observed that this process terminates for any $x$ when $A=\mathbb{N}$.

```lean
theorem erdos_282.variants.fibonacci {x : ℚ} (hx : x ∈ Set.Ioo 0 1) :
    greedyUnitFractionRem .univ x =ᶠ[atTop] 0
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/282.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/282.lean#L81).

## `Erdos282.erdos_282.variants.graham`

Open: stated without proof.

> Graham has shown that $\frac{m}{n}$ is the sum of distinct unit fractions
> with denominators $\equiv a\pmod{d}$ if and only if
>
> $$\left(\frac{n}{(n,a,d)},\frac{d}{(a,d)}\right)=1.$$
>
> Does the greedy algorithm always
> terminate in such cases?

```lean
theorem erdos_282.variants.graham :
    ∀ x : ℚ, x ∈ Set.Ioo 0 1 → ∀ a d : ℕ, 1 < d →
      (x.den / x.den.gcd (a.gcd d)).gcd (d / a.gcd d) = 1 →
      greedyUnitFractionRem { n | n ≡ a [MOD d] } x =ᶠ[atTop] 0
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/282.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/282.lean#L93).

## `Erdos282.erdos_282.variants.sq`

Open: stated without proof.

> Graham has also shown that $x$ is the sum of distinct unit fractions with
> square denominators if and only if $x\in [0,\pi^2/6-1)\cup [1,\pi^2/6)$. Does the
> greedy algorithm for this always terminate? Erdős and Graham believe not - indeed, perhaps it
> fails to terminate almost always.

```lean
theorem erdos_282.variants.sq :
    ∀ x : ℚ, (x : ℝ) ∈ Set.Ico 0 (π ^ 2 / 6 - 1) ∪ Set.Ico 1 (π ^ 2 / 6) →
      greedyUnitFractionRem { n | IsSquare n } x =ᶠ[atTop] 0
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/282.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/282.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/282.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/282.lean)
- [erdosproblems.com/282](https://www.erdosproblems.com/282)
