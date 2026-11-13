---
declaration: theorem
origin: cited
lean: Erdos376.erdos_376, Erdos376.erdos_376.variants.prime
statement: formalized
---

# Erdős Problem 376

> *Reference:* [erdosproblems.com/376](https://www.erdosproblems.com/376)

*Quoted from [FormalConjectures/ErdosProblems/376.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/376.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/376](https://www.erdosproblems.com/376).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos376.erdos_376`

Open: stated without proof.

> Are there infinitely many $n$ such that ${2n\choose n}$ is coprime to $105$?

```lean
theorem erdos_376 : { (n : ℕ) | n.centralBinom.Coprime 105 }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/376.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/376.lean#L34).

## `Erdos376.erdos_376.variants.prime`

Solved: stated here without proof.

> Erdős, Graham, Ruzsa, and Straus [EGRS75] have shown that, for any two odd primes $p$ and $q$,
> there are infinite many $n$ such that ${2n\choose n}$ is coprime to $pq$.

```lean
theorem erdos_376.variants.prime {p q : ℕ} (h₁ : p.Prime)
    (h₂ : Odd p) (h₃ : q.Prime) (h₄ : Odd q) :
    { (n : ℕ) | n.centralBinom.Coprime (p * q) }.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/376.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/376.lean#L42).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/376.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/376.lean)
- [erdosproblems.com/376](https://www.erdosproblems.com/376)
