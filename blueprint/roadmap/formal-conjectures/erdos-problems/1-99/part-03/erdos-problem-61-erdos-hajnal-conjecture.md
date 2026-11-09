---
declaration: theorem
origin: cited
lean: Erdos61.erdos_61, Erdos61.erdos_61.variants.erha89, Erdos61.erdos_61.variants.bnss23, Erdos61.erdos_61.variants.p5, Erdos61.erdos_61.variants.c5
statement: formalized
---

# Erdős Problem 61 -- Erdős–Hajnal Conjecture

> *Reference:* [erdosproblems.com/61](https://www.erdosproblems.com/61)

*Quoted from [FormalConjectures/ErdosProblems/61.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/61.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/61](https://www.erdosproblems.com/61).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos61.erdos_61`

Open: stated without proof.

> The Erdős–Hajnal Conjecture states that there is a constant $c(H) > 0$ for each
> $H$ such that we can take $f(n) = n^{c(H)}$ in the above formulation.

```lean
theorem erdos_61 :
    ∀ {α : Type*} [Fintype α] [DecidableEq α] (H : SimpleGraph α),
      ∃ c > (0 : ℝ), IsErdosHajnalLowerBound H (fun n : ℕ => (n : ℝ) ^ c)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/61.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/61.lean#L49).

## `Erdos61.erdos_61.variants.erha89`

Solved: stated here without proof.

> Erdős and Hajnal [ErHa89] proved that we can take $f(n) = \exp(c_H \sqrt{\log n})$
> for some constant $c_H > 0$ depending on $H$.
>
> [ErHa89] Erdős, P. and Hajnal, A., Ramsey-type theorems. Discrete Appl. Math. (1989), 37-52.

```lean
theorem erdos_61.variants.erha89 :
    ∀ {α : Type*} [Fintype α] [DecidableEq α] (H : SimpleGraph α),
      ∃ c > (0 : ℝ), IsErdosHajnalLowerBound H (fun n : ℕ => exp (c * sqrt (log n)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/61.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/61.lean#L61).

## `Erdos61.erdos_61.variants.bnss23`

Solved: stated here without proof.

> Bucić, Nguyen, Scott, and Seymour [BNSS23] improved this to
> $f(n) = \exp(c_H \sqrt{\log n \log \log n})$ for some constant $c_H > 0$ depending on $H$.
>
> [BNSS23] Bucić, M. and Nguyen, T. and Scott, A. and Seymour, P., A loglog step towards Erdos-Hajnal

```lean
theorem erdos_61.variants.bnss23 :
    ∀ {α : Type*} [Fintype α] [DecidableEq α] (H : SimpleGraph α),
      ∃ c > (0 : ℝ), IsErdosHajnalLowerBound H (fun n : ℕ => exp (c * sqrt (log n * log (log n))))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/61.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/61.lean#L73).

## `Erdos61.erdos_61.variants.p5`

Solved: stated here without proof.

> Nguyen, Scott, and Seymour [NSS23] proved the conjecture for $H = P_5$, the path on five
> vertices: every $P_5$-free graph on $n$ vertices has a clique or independent set of
> polynomial size.
>
> [NSS23] Nguyen, T., Scott, A. and Seymour, P., Induced subgraph density. VII. The
> five-vertex path. [arXiv:2312.15333](https://arxiv.org/abs/2312.15333)

```lean
theorem erdos_61.variants.p5 :
    ∃ c > (0 : ℝ), IsErdosHajnalLowerBound (pathGraph 5) (fun n : ℕ => (n : ℝ) ^ c)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/61.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/61.lean#L87).

## `Erdos61.erdos_61.variants.c5`

Solved: stated here without proof.

> Chudnovsky, Scott, Seymour, and Spirkl [CSSS23] proved the conjecture for $H = C_5$, the
> cycle on five vertices: every graph with no induced five-cycle has a clique or independent
> set of polynomial size.
>
> [CSSS23] Chudnovsky, M., Scott, A., Seymour, P. and Spirkl, S., Erdős–Hajnal for graphs with
> no 5-hole. Proc. Lond. Math. Soc. (3) 126 (2023), 997–1014.

```lean
theorem erdos_61.variants.c5 :
    ∃ c > (0 : ℝ), IsErdosHajnalLowerBound (cycleGraph 5) (fun n : ℕ => (n : ℝ) ^ c)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/61.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/61.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/61.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/61.lean)
- [erdosproblems.com/61](https://www.erdosproblems.com/61)
