---
declaration: theorem
origin: cited
lean: Erdos323.erdos_323.parts.i, Erdos323.erdos_323.parts.ii, Erdos323.erdos_323.variants.k_eq_2, Erdos323.erdos_323.variants.k_gt_2
statement: formalized
---

# Erdős Problem 323

> *Reference:* [erdosproblems.com/323](https://www.erdosproblems.com/323)

*Quoted from [FormalConjectures/ErdosProblems/323.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/323.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/323](https://www.erdosproblems.com/323).

The file states 4 research or textbook statements: 3 open and 1 solved.

## `Erdos323.erdos_323.parts.i`

Open: stated without proof.

> Is it true that $f_{k,k}(x) \gg_\epsilon x^{1-\epsilon}$ for all $\epsilon>0$?
>
> This would have significant applications to Waring's problem. Erdős and Graham describe this as
> 'unattackable by the methods at our disposal'.

```lean
theorem erdos_323.parts.i :
    ∀ k ≥ 1, ∀ ε > (0 : ℝ),
      (fun (x : ℕ) ↦ (x : ℝ) ^ (1 - ε)) =O[atTop] (fun (x : ℕ) ↦ (f k k x : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/323.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/323.lean#L47).

## `Erdos323.erdos_323.parts.ii`

Open: stated without proof.

> Is it true that if $m < k$ then $f_{k,m}(x) \gg x^{m/k}$ for sufficiently large $x$?

```lean
theorem erdos_323.parts.ii :
    ∀ k m : ℕ, 1 ≤ m → m < k →
      (fun (x : ℕ) ↦ (x : ℝ) ^ ((m : ℝ) / (k : ℝ))) =O[atTop] (fun (x : ℕ) ↦ (f k m x : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/323.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/323.lean#L56).

## `Erdos323.erdos_323.variants.k_eq_2`

Solved: stated here without proof.

> The case $k=2$ was resolved by Landau, who showed $f_{2,2}(x) \sim \frac{cx}{\sqrt{\log x}}$ for
> some constant $c>0$.

```lean
theorem erdos_323.variants.k_eq_2 :
    ∃ c > 0, (fun (x : ℕ) ↦ (f 2 2 x : ℝ)) ~[atTop]
      (fun (x : ℕ) ↦ c * (x : ℝ) / Real.sqrt (Real.log (x : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/323.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/323.lean#L66).

## `Erdos323.erdos_323.variants.k_gt_2`

Open: stated without proof.

> For $k>2$ it is not known if $f_{k,k}(x)=o(x)$.

```lean
theorem erdos_323.variants.k_gt_2 :
    ∀ k > 2, (fun (x : ℕ) ↦ (f k k x : ℝ)) =o[atTop] (fun (x : ℕ) ↦ (x : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/323.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/323.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/323.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/323.lean)
- [erdosproblems.com/323](https://www.erdosproblems.com/323)
