---
declaration: theorem
origin: cited
lean: Erdos281.erdos_281
statement: formalized
---

# Erdős Problem 281

> *References:*
> - [erdosproblems.com/281](https://www.erdosproblems.com/281)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [DaEr36] Davenport, H. and Erdős, P., *On sequences of positive integers*. Acta
>   Arithmetica (1936), 147-151.
> - [HaRo66] Halberstam, H. and Roth, K. F., *Sequences. Vol. I*. (1966), xx+291.

*Quoted from [FormalConjectures/ErdosProblems/281.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/281.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/281](https://www.erdosproblems.com/281).

The file states 1 research or textbook statement: 1 solved.

## `Erdos281.erdos_281`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos281.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos281.lean).

> Let $n_1\lt n_2\lt \cdots$ be an infinite sequence such that, for any choice of congruence classes
> $a_i\pmod{n_i}$, the set of integers not satisfying any of the congruences $a_i\pmod{n_i}$ has
> density $0$. Is it true that for every $\epsilon>0$ there exists some $k$ such that, for every
> choice of congruence classes $a_i$, the density of integers not satisfying any of the congruences
> $a_i\pmod{n_i}$ for $1\leq i\leq k$ is less than $\epsilon$?
>
> The answer is yes; the linked Lean proof formalizes Somani's argument.

```lean
theorem erdos_281 :
    ∀ (n : ℕ → ℕ), StrictMono n → (∀ i, 0 < n i) →
      (∀ a : ResidueChoice n, Set.HasIntDensity (avoidAll n a) 0) →
        ∀ ε : ℝ, 0 < ε →
          ∃ k : ℕ, ∀ a : ResidueChoice n,
            ∃ d : ℝ, Set.HasIntDensity (avoidPrefix n a k) d ∧ d < ε
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/281.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/281.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/281.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/281.lean)
- [erdosproblems.com/281](https://www.erdosproblems.com/281)
