---
declaration: theorem
origin: cited
lean: Erdos1090.erdos_1090
statement: formalized
---

# Erdős Problem 1090

> *References:*
> - [erdosproblems.com/1090](https://www.erdosproblems.com/1090)
> - [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*. Ann. Mat. Pura Appl. (4) (1975), 99-108.

*Quoted from [FormalConjectures/ErdosProblems/1090.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1090.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1090](https://www.erdosproblems.com/1090).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1090.erdos_1090`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1090.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1090.lean).

> Let $k\geq 3$. Does there exist a finite set $A\subset \mathbb{R}^2$ such that, in any $2$-colouring of $A$, there exists a line which contains at least $k$ points from $A$, and all the points of $A$ on the line have the same colour?
>
> Erdős [Er75f] says Graham and Selfridge proved the answer is yes when $k=3$. Hunter has observed that, for sufficiently large $n$, a generic projection of $[k]^n$ into $\mathbb{R}^2$ has this property, by the Hales-Jewett theorem.

```lean
theorem erdos_1090 : ∀ (k : ℕ), ∀ (hk : 3 ≤ k),
    ∃ (A : Finset (Fin 2 → ℝ)), ∀ (C : A → Fin 2),
      ∃ (S : Finset (Fin 2 → ℝ)), ∃ (hSA : S ⊆ A),
        Collinear ℝ (S : Set (Fin 2 → ℝ)) ∧ S.card ≥ k ∧
          (∀ y ∈ A, y ∈ affineSpan ℝ (S : Set (Fin 2 → ℝ)) → y ∈ S) ∧
          ∃ c, ∀ x (hx : x ∈ S), C ⟨x, hSA hx⟩ = c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1090.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1090.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1090.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1090.lean)
- [erdosproblems.com/1090](https://www.erdosproblems.com/1090)
