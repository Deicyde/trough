---
declaration: theorem
origin: cited
lean: Erdos366.erdos_366, Erdos366.erdos_366.variants.three_two, Erdos366.erdos_366.variants.weaker
statement: formalized
---

# Erdős Problem 366

> *Reference:* [erdosproblems.com/366](https://www.erdosproblems.com/366)

*Quoted from [FormalConjectures/ErdosProblems/366.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/366.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/366](https://www.erdosproblems.com/366).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos366.erdos_366`

Open: stated without proof.

> Are there any $2$-full $n$ such that $n+1$ is $3$-full?

```lean
theorem erdos_366 : ∃ n > 0, (2).Full n ∧ (3).Full (n + 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/366.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/366.lean#L34).

## `Erdos366.erdos_366.variants.three_two`

Proved here.

> Erdős and Graham asked whether $(8, 9)$ is the only pair of consecutive integers $n$, $n+1$
> with $n$ $3$-full and $n+1$ $2$-full. The answer is no: $12167 = 23^3$ and
> $12168 = 2^3 3^2 13^2$ is another such pair, already known to Golomb [Go70].

```lean
theorem erdos_366.variants.three_two :
    ¬ ∀ n > 0, (3).Full n ∧ (2).Full (n + 1) → n = 8
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/366.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/366.lean#L51).

## `Erdos366.erdos_366.variants.weaker`

Open: stated without proof.

> Are there any consecutive pairs of $3$-full integers?

```lean
theorem erdos_366.variants.weaker :
    ∃ n > 0, (3).Full n ∧ (3).Full (n + 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/366.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/366.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/366.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/366.lean)
- [erdosproblems.com/366](https://www.erdosproblems.com/366)
