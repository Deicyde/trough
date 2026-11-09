---
declaration: theorem
origin: cited
lean: Erdos979.erdos_979, Erdos979.erdos_979.variants.k2, Erdos979.erdos_979.variants.k3
statement: formalized
---

# Erdős Problem 979

> *Reference:* [erdosproblems.com/979](https://www.erdosproblems.com/979)

*Quoted from [FormalConjectures/ErdosProblems/979.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/979.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/979](https://www.erdosproblems.com/979).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos979.erdos_979`

Open: stated without proof.

> Let $k ≥ 2$, and let $f_k(n)$ count the number of solutions to $n = p_1^k + \dots + p_k^k$,
> where the $p_i$ are prime numbers. Is it true that $\limsup f_k(n) = \infty$?

```lean
theorem erdos_979 :
    ∀ k ≥ 2, Filter.limsup (fun n => (solutionSet n k).encard) Filter.atTop = ⊤
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/979.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/979.lean#L38).

## `Erdos979.erdos_979.variants.k2`

Solved: stated here without proof.

> Erdős [Er37b] proved that if $f_2(n)$ counts the number of solutions to $n = p_1^2 + p_2^2$, where $p_1$ and $p_2$ are prime numbers, then $\limsup f_2(n) = \infty$.
>
> [Er37b] Erdős, Paul, On the Sum and Difference of Squares of Primes. J. London Math. Soc. (1937), 133--136.

```lean
theorem erdos_979.variants.k2 :
    Filter.limsup (fun n => (solutionSet n 2).encard) Filter.atTop = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/979.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/979.lean#L48).

## `Erdos979.erdos_979.variants.k3`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-979-k3/blob/930fcc877fa4a2b4fc7c59614cbbab04a6d834ca/lean/K3Lean/Erdos979K3Final.lean#L46-L47](https://github.com/KitaKen1/erdos-979-k3/blob/930fcc877fa4a2b4fc7c59614cbbab04a6d834ca/lean/K3Lean/Erdos979K3Final.lean#L46-L47).

> Erdős (unpublished)

```lean
theorem erdos_979.variants.k3 :
    Filter.limsup (fun n => (solutionSet n 3).encard) Filter.atTop = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/979.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/979.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/979.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/979.lean)
- [erdosproblems.com/979](https://www.erdosproblems.com/979)
