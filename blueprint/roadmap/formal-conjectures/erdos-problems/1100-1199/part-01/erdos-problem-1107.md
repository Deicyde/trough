---
declaration: theorem
origin: cited
lean: Erdos1107.erdos_1107, Erdos1107.erdos_1107.variants.two
statement: formalized
---

# Erdős Problem 1107

> *References:*
> - [erdosproblems.com/1107](https://www.erdosproblems.com/1107)
> - [He88] Heath-Brown, D. R., Ternary quadratic forms and sums of three square-full numbers. (1988)

*Quoted from [FormalConjectures/ErdosProblems/1107.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1107.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1107](https://www.erdosproblems.com/1107).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1107.erdos_1107`

Open: stated without proof.

> Let $r \ge 2$. Is every large integer the sum of at most $r + 1$ many $r$-powerful numbers?

```lean
theorem erdos_1107 : ∀ r ≥ 2, ∀ᶠ n in atTop, SumOfRPowerful r n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1107.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1107.lean#L44).

## `Erdos1107.erdos_1107.variants.two`

Solved: stated here without proof.

> Heath-Brown [He88] proved every large integer the sum of at most three $2$-powerful numbers.

```lean
theorem erdos_1107.variants.two : ∀ᶠ n in atTop, SumOfRPowerful 2 n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1107.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1107.lean#L51).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1107.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1107.lean)
- [erdosproblems.com/1107](https://www.erdosproblems.com/1107)
