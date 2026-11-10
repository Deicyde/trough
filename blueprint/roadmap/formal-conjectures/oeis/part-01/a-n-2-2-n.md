---
declaration: theorem
origin: cited
lean: OeisA1146.divisibility_fact, OeisA1146.conjecture
statement: formalized
---

# $a(n) = 2^(2^n)$

> *References:*
> - [A001146](https://oeis.org/A001146)

*Quoted from [FormalConjectures/OEIS/1146.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/1146.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 4 test statements and 1 API statement, counted here but not shown.

## `OeisA1146.divisibility_fact`

Proved here.

> The forward direction: if $k = a(n)$ for $n \ge 2$, then $k^4 - 1$ divides $2^k - 1$.

```lean
theorem divisibility_fact (n : ℕ) (hn : 2 ≤ n) : (((a n)^4 - 1) : ℕ) ∣ (2^(a n) - 1 : ℕ)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/1146.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/1146.lean#L65).

## `OeisA1146.conjecture`

Open: stated without proof.

> I conjecture that { $a(n)$ ; $n>1$ } are the numbers such that $n^4-1$ divides $2^n-1$,
> intersection of A247219 and A247165. - M. F. Hasler, Jul 25 2015
> This formalizes the reverse direction.

```lean
theorem conjecture :
  ∀ k : ℕ, ((k^4 - 1) : ℕ) ∣ (2^k - 1 : ℕ) → k > 1 → ∃ n : ℕ, 2 ≤ n ∧ k = a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/1146.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/1146.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/1146.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/1146.lean)
- [A001146](https://oeis.org/A001146)
