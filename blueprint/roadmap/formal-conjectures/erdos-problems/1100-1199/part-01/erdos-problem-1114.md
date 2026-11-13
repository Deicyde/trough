---
declaration: theorem
origin: cited
lean: Erdos1114.erdos_1114, Erdos1114.erdos_1114.variants.rolle
statement: formalized
---

# Erdős Problem 1114

> *References:*
> - [erdosproblems.com/1114](https://www.erdosproblems.com/1114)
> - [Ba60b] Bálint, Elemér, *Proof of a conjecture of P. Erdős* (Hungarian: *Erdős Pál egy
>   sejtésének bizonyítása*). Mat. Lapok 11 (1960), 33-40.
> - [Lo76] Lorch, L., *Some monotonicity properties of polynomials with equally spaced zeros*.
>   Acta Math. Acad. Sci. Hungar. 27 (1976), 293-300.

*Quoted from [FormalConjectures/ErdosProblems/1114.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1114.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1114](https://www.erdosproblems.com/1114).

The file states 2 research or textbook statements: 1 solved and 1 textbook result.

## `Erdos1114.erdos_1114`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1114.lean#L1606](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1114.lean#L1606).

> Let $f(x)\in \mathbb{R}[x]$ be a polynomial of degree $n$ whose roots $\{a_0\lt \cdots\lt a_n\}$ are
> all real and form an arithmetic progression.
>
> The differences between consecutive zeros of $f'(x)$, beginning from the midpoint of $(a_0,a_n)$
> towards the endpoints, are monotonically increasing.
>
> Proved by Bálint [Ba60b]; some generalisations were given by Lorch [Lo76]. We take $f$ of
> degree $N+1$ with the $N+1$ roots $a+jd$ ($0\le j\le N$, $d>0$), since the number of roots must
> equal the degree, and read "increasing" as non-decreasing. Here `b k` is the zero of $f'$ in
> $(a+kd,a+(k+1)d)$, which exists and is the only zero there by Rolle's theorem (see
> `erdos_1114.variants.rolle`).

```lean
theorem erdos_1114 {N : ℕ} (hN : 0 < N) {a d : ℝ} (hd : 0 < d) {f : ℝ[X]} {b : ℕ → ℝ}
    (hdegree : f.natDegree = N + 1)
    (hroots : ∀ j : ℕ, j ≤ N → f.eval (a + d * j) = 0)
    (hb : ∀ k : ℕ, k < N → b k ∈ Set.Ioo (a + d * k) (a + d * (k + 1)))
    (hderiv : ∀ k : ℕ, k < N → f.derivative.eval (b k) = 0) :
    RightGapMonotone N b ∧ GapSymmetric N b
```

Category `research solved`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [26 Real functions](../../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/ErdosProblems/1114.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1114.lean#L70).

## `Erdos1114.erdos_1114.variants.rolle`

Textbook result, stated without proof.

> All the zeros of $f'(x)$ are all distinct real numbers in $(a_0,a_n)$ by Rolle's theorem.
>
> Precisely, for $f$ as in `erdos_1114` (degree $N+1$, roots $a+jd$ for $0\le j\le N$), each
> interval $(a+kd,a+(k+1)d)$ with $k\lt N$ contains exactly one zero of $f'$, and every zero of $f'$
> lies in one of these intervals.

```lean
theorem erdos_1114.variants.rolle {N : ℕ} {a d : ℝ} (hd : 0 < d) {f : ℝ[X]}
    (hdegree : f.natDegree = N + 1)
    (hroots : ∀ j : ℕ, j ≤ N → f.eval (a + d * j) = 0) :
    (∀ k : ℕ, k < N →
      ∃! x : ℝ, x ∈ Set.Ioo (a + d * k) (a + d * (k + 1)) ∧ f.derivative.eval x = 0) ∧
    (∀ x : ℝ, f.derivative.eval x = 0 →
      ∃ k : ℕ, k < N ∧ x ∈ Set.Ioo (a + d * k) (a + d * (k + 1)))
```

Category `textbook`; AMS [12 Field theory and polynomials](../../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [26 Real functions](../../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/ErdosProblems/1114.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1114.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1114.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1114.lean)
- [erdosproblems.com/1114](https://www.erdosproblems.com/1114)
