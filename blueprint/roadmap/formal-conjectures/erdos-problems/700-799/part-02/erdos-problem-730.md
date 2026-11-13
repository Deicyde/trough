---
declaration: theorem
origin: cited
lean: Erdos730.erdos_730, Erdos730.erdos_730.variants.explicit_pairs, Erdos730.erdos_730.variants.delta_ne_one
statement: formalized
---

# Erdős Problem 730

> *References:*
>   - [erdosproblems.com/730](https://www.erdosproblems.com/730)
>   - [A129515](https://oeis.org/A129515)
>   - [PALOMAR-2026-08-22-000001](https://palomar-registry.org/entry.html?id=PALOMAR-2026-08-22-000001&version=1):
>     a Lean 4 proof that there are infinitely many such pairs, checked by Comparator
>     against the statement `S.Infinite` below and registered with the Palomar registry.
>     The proof follows an argument posted on the erdosproblems.com forum
>     (Liam Price, 24 June 2026), which shows that there are infinitely many
>     consecutive pairs $(n, n+1)$.

*Quoted from [FormalConjectures/ErdosProblems/730.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/730.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/730](https://www.erdosproblems.com/730).

The file states 3 research or textbook statements: 2 solved and 1 textbook result.

## `Erdos730.erdos_730`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/03729c9cbb0b602f5a828bb850c85e84c5a6d460/ErdosProblems/Erdos730/FullDensityTheorem.lean#L40](https://github.com/williamjblair/lean-proofs/blob/03729c9cbb0b602f5a828bb850c85e84c5a6d460/ErdosProblems/Erdos730/FullDensityTheorem.lean#L40).

> Are there infinitely many pairs of integers $n < m$ such that $\binom{2n}{n}$
> and $\binom{2m}{m}$ have the same set of prime divisors?
>
> Yes: there are infinitely many consecutive pairs $(n, n+1)$. The formal proof
> registered as [PALOMAR-2026-08-22-000001] proves `S.Infinite` for this `S`.

```lean
theorem erdos_730 : S.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/730.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/730.lean#L52).

## `Erdos730.erdos_730.variants.explicit_pairs`

Textbook result, proved here.

> For example, $(87,88)$ and $(607,608)$ are such pairs.

```lean
theorem erdos_730.variants.explicit_pairs :
    {(87, 88), (607, 608)} ⊆ S
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/730.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/730.lean#L59).

## `Erdos730.erdos_730.variants.delta_ne_one`

Proved here.

> There are examples where $(n, m) ∈ S$ with $m ≠ n + 1$.
>
> (Found by AlphaProof, although it was implicit already in [A129515])

```lean
theorem erdos_730.variants.delta_ne_one : ∃ (n m : ℕ), (n, m) ∈ S ∧ m ≠ n + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/730.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/730.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/730.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/730.lean)
- [erdosproblems.com/730](https://www.erdosproblems.com/730)
