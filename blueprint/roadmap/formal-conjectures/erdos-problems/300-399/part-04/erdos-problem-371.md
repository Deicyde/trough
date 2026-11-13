---
declaration: theorem
origin: cited
lean: Erdos371.erdos_371
statement: formalized
---

# Erdős Problem 371

> *References:*
> - [erdosproblems.com/371](https://www.erdosproblems.com/371)
> - [OAI26a] OpenAI, *The joint Dickman law for consecutive integers*. OpenAI Math Release preprint
>   (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-joint-Dickman-law-for-consecutive-integers-September-24-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/371.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/371.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/371](https://www.erdosproblems.com/371).

The file states 1 research or textbook statement: 1 solved.

## `Erdos371.erdos_371`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/JointDickman/PaperMain.lean#L21](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/JointDickman/PaperMain.lean#L21).

> Let $P(n)$ denote the largest prime factor of $n$. Show that the set of $n$
> with $P(n+1) > P(n)$ has density $\frac{1}{2}$.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean proof.

```lean
theorem erdos_371 :
    { n | Nat.maxPrimeFac (n + 1) > Nat.maxPrimeFac n }.HasDensity (1/2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/371.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/371.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/371.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/371.lean)
- [erdosproblems.com/371](https://www.erdosproblems.com/371)
