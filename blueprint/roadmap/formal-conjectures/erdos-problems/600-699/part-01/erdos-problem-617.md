---
declaration: theorem
origin: cited
lean: Erdos617.erdos_617, Erdos617.erdos_617.variants.r_eq_3, Erdos617.erdos_617.variants.r_eq_4, Erdos617.erdos_617.variants.r2
statement: formalized
---

# Erdős Problem 617

> *References:*
> - [erdosproblems.com/617](https://www.erdosproblems.com/617)
> - [ErGy99] Erdős, Paul and Gyárfás, András, Split and balanced colorings of complete graphs.
>   Discrete Math. (1999), 79-86.

*Quoted from [FormalConjectures/ErdosProblems/617.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/617.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/617](https://www.erdosproblems.com/617).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos617.erdos_617`

Open: stated without proof.

> Let $r\geq 3$. If the edges of $K_{r^2+1}$ are $r$-coloured then there exist $r+1$ vertices with at
> least one colour missing on the edges of the induced $K_{r+1}$.
>
> In other words, there is no balanced colouring.
>
> A conjecture of Erdős and Gyárfás [ErGy99].

```lean
theorem erdos_617 (r : ℕ) (hr : r ≥ 3) {V : Type} [Fintype V] [DecidableEq V]
    (hV : Fintype.card V = r^2 + 1) (coloring : Sym2 V → Fin r) :
    ∃ (S : Finset V) (k : Fin r),
      S.card = r + 1 ∧
      ∀ u ∈ S, ∀ v ∈ S, u ≠ v → coloring s(u, v) ≠ k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/617.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/617.lean#L42).

## `Erdos617.erdos_617.variants.r_eq_3`

Solved: stated here without proof.

> Erdős and Gyárfás [ErGy99] proved the conjecture for $r=3$.

```lean
theorem erdos_617.variants.r_eq_3 (r : ℕ) (hr : r ≥ 3) {V : Type} [Fintype V] [DecidableEq V]
    (hV : Fintype.card V = 3^2 + 1) (coloring : Sym2 V → Fin 3) :
    ∃ (S : Finset V) (k : Fin 3),
      S.card = 3 + 1 ∧
      ∀ u ∈ S, ∀ v ∈ S, u ≠ v → coloring s(u, v) ≠ k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/617.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/617.lean#L53).

## `Erdos617.erdos_617.variants.r_eq_4`

Solved: stated here without proof.

> Erdős and Gyárfás [ErGy99] proved the conjecture for $r=4$.

```lean
theorem erdos_617.variants.r_eq_4 (r : ℕ) (hr : r ≥ 3) {V : Type} [Fintype V] [DecidableEq V]
    (hV : Fintype.card V = 4^2 + 1) (coloring : Sym2 V → Fin 4) :
    ∃ (S : Finset V) (k : Fin 4),
      S.card = 4 + 1 ∧
      ∀ u ∈ S, ∀ v ∈ S, u ≠ v → coloring s(u, v) ≠ k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/617.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/617.lean#L64).

## `Erdos617.erdos_617.variants.r2`

Solved: stated here without proof.

> Erdős and Gyárfás [ErGy99] showed this property fails for infinitely many $r$ if we replace $r^2+1$
> by $r^2$.

```lean
theorem erdos_617.variants.r2 :
    {r : ℕ | ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V), Fintype.card V = r^2 ∧
      ∃ (coloring : Sym2 V → Fin r),
        ∀ (S : Finset V), S.card = r + 1 →
          ∀ (k : Fin r), ∃ u ∈ S, ∃ v ∈ S, u ≠ v ∧ coloring s(u, v) = k}.Infinite
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/617.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/617.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/617.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/617.lean)
- [erdosproblems.com/617](https://www.erdosproblems.com/617)
