---
declaration: theorem
origin: cited
lean: Erdos324.erdos_324, Erdos324.erdos_324.variants.quintic
statement: formalized
---

# Erdős Problem 324

> *Reference:* [erdosproblems.com/324](https://www.erdosproblems.com/324)

*Quoted from [FormalConjectures/ErdosProblems/324.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/324.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/324](https://www.erdosproblems.com/324).

The file states 2 research or textbook statements: 2 open.

## `Erdos324.erdos_324`

Open: stated without proof.

> Does there exist a polynomial $f(x)\in\mathbb{Z}[x]$ such that all the sums $f(a)+f(b)$ with
> $a < b$ nonnegative integers are distinct?

```lean
theorem erdos_324 :
    ∃ f : ℤ[X], {(a, b) : ℕ × ℕ | a < b}.InjOn fun (a, b) => f.eval (a : ℤ) + f.eval (b : ℤ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/324.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/324.lean#L37).

## `Erdos324.erdos_324.variants.quintic`

Open: stated without proof.

> Probably $f(x) = x^5$ has the property that the sums $f(a)+f(b)$ with
> $a < b$ nonnegative integers are distinct.

```lean
theorem erdos_324.variants.quintic : {(a, b) : ℕ × ℕ | a < b}.InjOn fun (a, b) => a ^ 5 + b ^ 5
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/324.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/324.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/324.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/324.lean)
- [erdosproblems.com/324](https://www.erdosproblems.com/324)
