---
declaration: theorem
origin: cited
lean: Erdos361.erdos_361
statement: formalized
---

# Erdős Problem 361

> *Reference:* [erdosproblems.com/361](https://www.erdosproblems.com/361)

*Quoted from [FormalConjectures/ErdosProblems/361.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/361.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/361](https://www.erdosproblems.com/361).

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Erdos361.erdos_361`

Open: stated without proof.

> Let $c > 0$ and $n$ be some large integer. What is the size of the largest set
> $A \subseteq \{1, \ldots, \lfloor c n \rfloor\}$ such that $n$ is not a sum of a subset of $A$?
> Does this depend on $n$ in an irregular way?

```lean
theorem erdos_361 (c : ℝ) (hc : 0 < c) :
    subsetSumAvoidanceNumber c = erdos_361.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/361.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/361.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/361.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/361.lean)
- [erdosproblems.com/361](https://www.erdosproblems.com/361)
