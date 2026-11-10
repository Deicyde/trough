---
declaration: theorem
origin: cited
lean: OeisA102371.conjecture
statement: formalized
---

# Conjectures associated with A102371

> The sequence $a(n)$ is defined by the recurrence relation $a(1)=1$,
> and for $n>1$, $a(n) = a(n-1) \operatorname{XOR} (a(n-1) + n)$.
> The conjecture asks if $a(n) = 2^n - 1 - \operatorname{A105033}(n-1)$ for $n \ge 1$.
>
> *References:*
> - [A102371](https://oeis.org/A102371)

*Quoted from [FormalConjectures/OEIS/102371.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/102371.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA102371.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a102371/blob/d80fba9/lean/OeisA102371FC.lean#L490-L497](https://github.com/KitaKen1/oeis-a102371/blob/d80fba9/lean/OeisA102371FC.lean#L490-L497).

> Do we have $a(n) = 2^n - 1 - \operatorname{A105033}(n-1)$ for $n \ge 1$?
>
> Note: The OEIS comment suggests $n-1$ which means this applies at least for $n \ge 1$,
> as we assume $\operatorname{A105033}(\mathbb{N})$ is defined on $\mathbb{N}$.
> We include the case $n=1$ which relies on $A105033(0)$, which is 0.

```lean
theorem conjecture : ∀ n : ℕ, 0 < n → a n = 2^n - 1 - OeisA105033.a (n - 1)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/102371.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/102371.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/102371.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/102371.lean)
- [A102371](https://oeis.org/A102371)
