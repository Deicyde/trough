---
declaration: theorem
origin: cited
lean: ClaudesCycles.cube_hamiltonian_arc_decomposition, ClaudesCycles.cube_hamiltonian_arc_decomposition_impossible_m2, ClaudesCycles.cube_hamiltonian_arc_decomposition_even
statement: formalized
---

# Claude's Cycles

> *Reference:* [Claude's Cycles](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf)
> by *Donald E. Knuth* (2026)
>
> Fix `m ≥ 2`. Consider the directed graph with vertex set `(ZMod m)³`, where from each vertex
> `(i, j, k)` there are directed arcs to `(i+1, j, k)`, `(i, j+1, k)`, and `(i, j, k+1)`
> (arithmetic mod `m`). The goal is to partition all `3m³` directed arcs into three
> edge-disjoint directed Hamiltonian cycles (each of length `m³`).
>
> Knuth describes an explicit construction, found by Claude (Anthropic), that achieves this
> decomposition for all odd `m ≥ 3`. The case `m = 2` is known to be impossible [Aub82].
> The even case `m > 2` is also settled. Knuth's paper says so in its final section, added in the
> 14 April 2026 revision: "Breaking news: The problem for even values of m is no longer in doubt!"
> Ho Boon Suan's algorithm [Ho26] is proved correct for even `m ≥ 8` in [GPT26], and
> Aquino-Michaels [AM26] gives a decomposition for the even case that is simpler. The statement
> below starts at `m = 4`, which is below the range [GPT26] covers, so it also rests on the
> explicit solutions in [Kn26], whose header gives even `m ≥ 4`.
>
> ## References
>
> - [Knu26] D. E. Knuth, "Claude's Cycles" (2026).
> - [Aub82] J. Aubert, B. Schneider, "Graphes orientés indécomposables en circuits hamiltoniens",
>   J. Combin. Theory Ser. B 32 (1982), 347–349.
> - [Ho26] Ho Boon Suan, closed-form construction for even `m`,
>   <https://cs.stanford.edu/~knuth/even_closed_form.c>
> - [GPT26] A proof that [Ho26] yields three `m³`-cycles for every even `m ≥ 8`, 14 pages,
>   <https://cs.stanford.edu/~knuth/even_closed_form_proof_final.pdf>
> - [AM26] K. Aquino-Michaels, "Completing Claude's cycles: Multi-agent structured exploration on
>   an open combinatorial problem", <https://github.com/no-way-labs/residue>
> - [Kn26] Explicit even solutions for even `m ≥ 4`, recorded with [Knu26],
>   <https://cs.stanford.edu/~knuth/even_solution.py>
> - [KM26] K. Morrison, a Lean formalisation of the odd case,
>   <https://github.com/kim-em/KnuthClaudeLean>

*Quoted from [FormalConjectures/Paper/ClaudesCycles.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ClaudesCycles.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 2 test statements and 2 API statements, counted here but not shown.

## `ClaudesCycles.cube_hamiltonian_arc_decomposition`

Solved: stated here; a Lean proof is at [https://github.com/kim-em/KnuthClaudeLean/blob/bdda6025fb7954f614ed9a7ac7382455fd064940/Solution.lean#L5](https://github.com/kim-em/KnuthClaudeLean/blob/bdda6025fb7954f614ed9a7ac7382455fd064940/Solution.lean#L5).

> For odd `m > 1`, the cube digraph on `(ZMod m)³` has a Hamiltonian arc decomposition
> into three directed cycles [Knu26].

```lean
theorem cube_hamiltonian_arc_decomposition {m : ℕ} [NeZero m] (hm : Odd m) (hm' : 1 < m) :
    HasHamiltonianArcDecomposition m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ClaudesCycles.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ClaudesCycles.lean#L122).

## `ClaudesCycles.cube_hamiltonian_arc_decomposition_impossible_m2`

Solved: stated here without proof.

> The case `m = 2` is impossible: the cube digraph on `(ZMod 2)³` does not have a
> Hamiltonian arc decomposition [Aub82].

```lean
theorem cube_hamiltonian_arc_decomposition_impossible_m2 :
    ¬ HasHamiltonianArcDecomposition 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ClaudesCycles.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ClaudesCycles.lean#L129).

## `ClaudesCycles.cube_hamiltonian_arc_decomposition_even`

Solved: stated here without proof.

> For even `m > 2`, the cube digraph on `(ZMod m)³` has a Hamiltonian arc decomposition.
> Knuth records this as settled in the final section of [Knu26], by [Ho26] with the proof in
> [GPT26] for even `m ≥ 8`, and by [AM26] for the even case generally.

```lean
theorem cube_hamiltonian_arc_decomposition_even :
    ∀ᵉ (m : ℕ) (_ : NeZero m) (_ : Even m) (_ : 2 < m),
      HasHamiltonianArcDecomposition m
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ClaudesCycles.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ClaudesCycles.lean#L137).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/ClaudesCycles.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/ClaudesCycles.lean)
- [Claude's Cycles](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf)
