---
declaration: theorem
origin: cited
lean: Erdos1054.erdos_1054.parts.i, Erdos1054.erdos_1054.parts.ii, Erdos1054.erdos_1054.parts.iii, Erdos1054.f_undefined_at_2, Erdos1054.f_undefined_at_3
statement: formalized
---

# Erdős Problem 1054

> *References:*
> - [erdosproblems.com/1054](https://www.erdosproblems.com/1054)
> - [PALOMAR-2026-10-05-000005](https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-05-000005&version=1)

*Quoted from [FormalConjectures/ErdosProblems/1054.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1054.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1054](https://www.erdosproblems.com/1054).

The file states 5 research or textbook statements: 3 solved and 2 textbook results.

## `Erdos1054.erdos_1054.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/0917cd01090b52088aa82b09c8c84689047b8171/erdos-1054/Solution.lean#L97](https://github.com/linrock/math-proofs/blob/0917cd01090b52088aa82b09c8c84689047b8171/erdos-1054/Solution.lean#L97).

> Let $f(n)$ be the minimal integer $m$ such that $n$ is the sum of the $k$ smallest divisors
> of $m$ for some $k\geq 1$. Is it true that $f(n)=o(n)$?
>
> The strong claim that $f(n)=o(n)$ was disproved by Tao in the comments to
> [468](https://www.erdosproblems.com/468), in which he proves that the upper density of
> $\{ n : f(n)\leq \delta n\}$ is $\ll \delta^2$.

```lean
theorem erdos_1054.parts.i : ¬ (fun n ↦ (f n : ℝ)) =o[atTop] (fun n ↦ (n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1054.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1054.lean#L51).

## `Erdos1054.erdos_1054.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/0917cd01090b52088aa82b09c8c84689047b8171/erdos-1054/Solution.lean#L103](https://github.com/linrock/math-proofs/blob/0917cd01090b52088aa82b09c8c84689047b8171/erdos-1054/Solution.lean#L103).

> Let $f(n)$ be the minimal integer $m$ such that $n$ is the sum of the $k$ smallest divisors
> of $m$ for some $k\geq 1$. Is it true that $f(n)=o(n)$ for almost all $n$?
>
> No: combining the Tao–Kovač small-ratio bound $\#\{n \leq X : 0 < f(n) \leq \delta n\} \ll \delta^2 X$
> with the fact that almost all odd integers are represented (or via the lower-density bound below),
> $f(n)$ is not $o(n)$ along any density-one set $A$.

```lean
theorem erdos_1054.parts.ii : ¬ ∃ (A : Set ℕ), A.HasDensity 1 ∧
    (fun (n : A) ↦ (f ↑n : ℝ)) =o[atTop] (fun n ↦ (n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1054.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1054.lean#L62).

## `Erdos1054.erdos_1054.parts.iii`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/0917cd01090b52088aa82b09c8c84689047b8171/erdos-1054/Solution.lean#L110](https://github.com/linrock/math-proofs/blob/0917cd01090b52088aa82b09c8c84689047b8171/erdos-1054/Solution.lean#L110).

> Let $f(n)$ be the minimal integer $m$ such that $n$ is the sum of the $k$ smallest divisors
> of $m$ for some $k\geq 1$. Is it true that $\limsup f(n)/n=\infty$?
>
> Yes: for every $A \geq 1$, a positive lower density of odd integers satisfy $f(n) > A n$, so
> $\limsup f(n)/n = \infty$.

```lean
theorem erdos_1054.parts.iii : ∃ (A : Set ℕ), A.HasDensity 1 ∧
    atTop.limsup (fun n ↦ (f n : EReal) / n) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1054.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1054.lean#L73).

## `Erdos1054.f_undefined_at_2`

Textbook result, proved here.

> Let $f(n)$ be the minimal integer $m$ such that $n$ is the sum of the $k$ smallest divisors
> of $m$ for some $k\geq 1$. Show that $f$ is undefined at $n=2$, i.e. we get the junk value $0$.

```lean
theorem f_undefined_at_2 : f 2 = 0
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1054.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1054.lean#L80).

## `Erdos1054.f_undefined_at_3`

Textbook result, proved here.

> Let $f(n)$ be the minimal integer $m$ such that $n$ is the sum of the $k$ smallest divisors
> of $m$ for some $k\geq 1$. Show that $f$ is undefined at $n=5$, i.e. we get the junk value $0$.

```lean
theorem f_undefined_at_3 : f 5 = 0
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1054.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1054.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1054.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1054.lean)
- [erdosproblems.com/1054](https://www.erdosproblems.com/1054)
