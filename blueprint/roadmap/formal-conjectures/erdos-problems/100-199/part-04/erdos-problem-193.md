---
declaration: theorem
origin: cited
lean: Erdos193.erdos_193, Erdos193.erdos_193_z2
statement: formalized
---

# Erdős Problem 193

> References:
> - [erdosproblems.com/193](https://www.erdosproblems.com/193)
> - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
>   theory. Monographies de L'Enseignement Mathematique (1980).
> - [GeRa79] Gerver, Joseph L. and Ramsey, L. Thomas, "On certain sequences of lattice points."
>   Pacific J. Math. (1979), 357-363.
> - [CaKa26] Cambie, Stijn and Kalviainen, Erik, "An infinite small-step Z³-walk with no
>   collinear triple." [arXiv:2609.01766](https://arxiv.org/abs/2609.01766).

*Quoted from [FormalConjectures/ErdosProblems/193.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/193.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/193](https://www.erdosproblems.com/193).

The file states 2 research or textbook statements: 2 solved.

## `Erdos193.erdos_193`

Solved: stated here; a Lean proof is at [https://github.com/ekalvi/erdos-193/blob/fca4e1bd2b423c000a6bef18cf2f3bc0f4bd363e/formal/Hilbert193/Hilbert193/Continuity.lean#L64-L72](https://github.com/ekalvi/erdos-193/blob/fca4e1bd2b423c000a6bef18cf2f3bc0f4bd363e/formal/Hilbert193/Hilbert193/Continuity.lean#L64-L72).

> Let $S \subseteq \mathbb{Z}^3$ be a finite set and let $A = \lbrace a_1, a_2, \ldots \rbrace$ be
> an infinite $S$-walk, so that $a_{i+1} - a_i \in S$ for all $i$. Must $A$ contain three collinear
> points?
>
> Cambie and Kalviainen [CaKa26] answered this question in the negative by constructing an infinite
> walk in $\mathbb{Z}^3$ with a finite set of steps and no three collinear points.

```lean
theorem erdos_193 :
    ¬ ∀ S : Set (Fin 3 → ℤ), S.Finite →
      /- The statement's $A = \lbrace a_1, a_2, \ldots \rbrace$ is an infinite set.

      If the sequence only takes finitely many values, one value has to repeat infinitely many
      times, which would yield a trivial collinear triple (x, x, x). In this case, the conjecture
      would hold for degenerate S-walks. Another case is constant S-walks, which would render the
      conjecture trivially false (finite loop ranges have no 3 distinct points).

      Assuming the authors intend to stay away from these degenerate cases, we formalize this by
      requiring an infinite range (and require distinct points). -/
      ∀ a : ℕ → Fin 3 → ℤ, IsSWalk S a → (range a).Infinite →
      HasCollinearTriple ℚ (range (fun n ↦ (↑) ∘ a n : ℕ → Fin 3 → ℚ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/193.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/193.lean#L58).

## `Erdos193.erdos_193_z2`

Solved: stated here without proof.

> [GeRa79] showed that the answer is yes for $\mathbb{Z}^2$

```lean
theorem erdos_193_z2 :
    ∀ S : Set (Fin 2 → ℤ), S.Finite →
      ∀ a : ℕ → Fin 2 → ℤ, IsSWalk S a → (range a).Infinite →
      HasCollinearTriple ℚ (range (fun n ↦ (↑) ∘ a n : ℕ → Fin 2 → ℚ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/193.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/193.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/193.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/193.lean)
- [erdosproblems.com/193](https://www.erdosproblems.com/193)
