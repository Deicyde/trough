---
declaration: theorem
origin: cited
lean: Erdos325.erdos_325, Erdos325.erdos_325.variants.weaker, Erdos325.erdos_325.variants.wooley
statement: formalized
---

# Erdős Problem 325

> *Reference:* [erdosproblems.com/325](https://www.erdosproblems.com/325)

*Quoted from [FormalConjectures/ErdosProblems/325.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/325.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/325](https://www.erdosproblems.com/325).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos325.erdos_325`

Open: stated without proof.

> Writing $f_{k, 3}(x)$ for the number of integers $\leq x$ which are the sum of three $k$th powers,
> is it true that $f_{k, 3}(x) \gg x ^ (3 / k)$?

```lean
theorem erdos_325 :
     ∀ k : ℕ, 3 ≤ k → (fun x : ℕ => (x : ℝ) ^ (3 / k : ℝ)) =O[atTop]
      (fun x : ℕ => (cardIsSumThreePowerBelow k x : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/325.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/325.lean#L43).

## `Erdos325.erdos_325.variants.weaker`

Open: stated without proof.

> Writing $f_{k, 3}(x)$ for the number of integers $\leq x$ which are the sum of three $k$th powers,
> is it even true that $f_{k, 3}(x) \gg_{\epsilon} x ^ (3 / k - \epsilon)$?

```lean
theorem erdos_325.variants.weaker :
    ∀ ε > 0, ∀ k : ℕ, 3 ≤ k → (fun x : ℕ => (x : ℝ) ^ ((3 / k : ℝ) - ε)) =O[atTop]
      (fun x => (cardIsSumThreePowerBelow k x : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/325.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/325.lean#L53).

## `Erdos325.erdos_325.variants.wooley`

Solved: stated here without proof.

> For $k = 3$, the best known is due to Wooley [Wo15], who proved
> $f_{3, 3}(x) \gg x^{0.91709477}$.
>
> [Wo15] Wooley, Trevor D., Sums of three cubes, II. Acta Arith. (2015), 73-100.

```lean
theorem erdos_325.variants.wooley :
    (fun x : ℕ => (x : ℝ) ^ (0.91709477 : ℝ)) =O[atTop]
      (fun x => (cardIsSumThreePowerBelow 3 x : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/325.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/325.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/325.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/325.lean)
- [erdosproblems.com/325](https://www.erdosproblems.com/325)
