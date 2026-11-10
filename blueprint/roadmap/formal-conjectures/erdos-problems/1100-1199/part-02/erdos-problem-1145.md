---
declaration: theorem
origin: cited
lean: Erdos1145.erdos_1145
statement: formalized
---

# Erdős Problem 1145

> *References:*
> - [erdosproblems.com/28](https://www.erdosproblems.com/28)
> - [erdosproblems.com/1145](https://www.erdosproblems.com/1145)

*Quoted from [FormalConjectures/ErdosProblems/1145.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1145.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1145](https://www.erdosproblems.com/1145).

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Erdos1145.erdos_1145`

Open: stated without proof.

> Let $A=\{1\leq a_1 < a_2 < \cdots\}$ and $B=\{1\leq b_1 < b_2 < \cdots\}$ be sets of integers with
> $a_n/b_n\to 1$.
>
> If $A+B$ contains all sufficiently large positive integers then is it true that
> $\limsup 1_A\ast 1_B(n)=\infty$?
>
> A conjecture of Erdős and Sárközy.

```lean
theorem erdos_1145 : Erdos1145Prop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1145.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1145.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1145.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1145.lean)
- [erdosproblems.com/1145](https://www.erdosproblems.com/1145)
