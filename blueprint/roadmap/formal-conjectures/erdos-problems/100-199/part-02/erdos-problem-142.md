---
declaration: theorem
origin: cited
lean: Erdos142.erdos_142, Erdos142.erdos_142.variants.lower, Erdos142.erdos_142.variants.isTheta, Erdos142.erdos_142.variants.three
statement: formalized
---

# Erdős Problem 142

> *Reference:* [erdosproblems.com/142](https://www.erdosproblems.com/142)

*Quoted from [FormalConjectures/ErdosProblems/142.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/142.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/142](https://www.erdosproblems.com/142).

The file states 4 research or textbook statements: 4 open.

## `Erdos142.erdos_142`

Open: stated without proof.

> Prove an asymptotic formula for $r_k(N)$, the largest possible size of a subset
> of $\{1, \dots, N\}$ that does not contain any non-trivial $k$-term arithmetic progression.
> That is, find $f_k$ with $r_k(N) / f_k(N) \to 1$ as $N \to \infty$.

```lean
theorem erdos_142 (k : ℕ) : (fun N => (r k N : ℝ)) ~[atTop] erdos_142.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/142.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/142.lean#L42).

## `Erdos142.erdos_142.variants.lower`

Open: stated without proof.

> Show that $r_k(N) = o_k(N / \log N)$, where $r_k(N)$ the largest possible size of a subset
> of $\{1, \dots, N\}$ that does not contain any non-trivial $k$-term arithmetic progression.

```lean
theorem erdos_142.variants.lower (k : ℕ) (hk : 1 < k) :
    (fun N => (r k N : ℝ)) =o[atTop] (fun N : ℕ => N / (N : ℝ).log)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/142.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/142.lean#L50).

## `Erdos142.erdos_142.variants.isTheta`

Open: stated without proof.

> Determine the order of magnitude of $r_k(N)$, the largest possible size of a subset
> of $\{1, \dots, N\}$ that does not contain any non-trivial $k$-term arithmetic progression.
> That is, find $f_k$ with $r_k(N) \asymp_k f_k(N)$.

```lean
theorem erdos_142.variants.isTheta (k : ℕ) :
    (fun N => (r k N : ℝ)) =Θ[atTop] erdos_142.variants.isTheta.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/142.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/142.lean#L63).

## `Erdos142.erdos_142.variants.three`

Open: stated without proof.

> Prove an asymptotic formula for $r_3(N)$, the largest possible size of a subset
> of $\{1, \dots, N\}$ that does not contain any non-trivial $3$-term arithmetic progression.
> That is, find $f$ with $r_3(N) / f(N) \to 1$ as $N \to \infty$.

```lean
theorem erdos_142.variants.three : (fun N => (r 3 N : ℝ)) ~[atTop] erdos_142.variants.three.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/142.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/142.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/142.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/142.lean)
- [erdosproblems.com/142](https://www.erdosproblems.com/142)
