---
declaration: theorem
origin: cited
lean: Erdos850.erdos_850
statement: formalized
---

# Erdős Problem 850

> *Reference:* [erdosproblems.com/850](https://www.erdosproblems.com/850)

*Quoted from [FormalConjectures/ErdosProblems/850.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/850.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/850](https://www.erdosproblems.com/850).

The file states 1 research or textbook statement: 1 open.

## `Erdos850.erdos_850`

Open: stated without proof.

> Can there exist two distinct integers $x$ and $y$ such that $x,y$ have the same prime factors,
> $x+1,y+1$ have the same prime factors, and $x+2,y+2$ also have the same prime factors?

```lean
theorem erdos_850 :
    ∃ x y : ℕ, x ≠ y ∧ x.primeFactors = y.primeFactors
      ∧ (x + 1).primeFactors = (y + 1).primeFactors
      ∧ (x + 2).primeFactors = (y + 2).primeFactors
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/850.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/850.lean#L34).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/850.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/850.lean)
- [erdosproblems.com/850](https://www.erdosproblems.com/850)
