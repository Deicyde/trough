---
declaration: theorem
origin: cited
lean: UnionClosed.union_closed, UnionClosed.union_closed.variants.yu, UnionClosed.union_closed.variants.univ_card, UnionClosed.union_closed.variants.family_card, UnionClosed.union_closed.variants.univ_card_two, UnionClosed.union_closed.variants.singleton_mem, UnionClosed.union_closed.variants.sharpness, UnionClosed.union_closed.variants.cardinality_even_of_union_closed_tight
statement: formalized
---

# Union-closed sets conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Union-closed_sets_conjecture)
>
> In this file, we:
> * state the conjecture
> * state three solved variants of the conjecture, without proof
> * prove two solved variants of the conjecture
> * prove the conjecture is sharp

*Quoted from [FormalConjectures/Wikipedia/UnionClosed.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 2 open and 6 solved. It also has 2 API statements, counted here but not shown.

## `UnionClosed.union_closed`

Open: stated without proof.

> For every finite union-closed family of sets, other than the family containing only the empty set,
> there exists an element that belongs to at least half of the sets in the family.

```lean
theorem union_closed
    [Nonempty n]
    (h_ne_singleton_empty : A ≠ {∅})
    (h_union_closed : IsUnionClosed A) :
    ∃ i : n, (1 / 2 : ℚ) * #A ≤ #{x ∈ A | i ∈ x}
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L59).

## `UnionClosed.union_closed.variants.yu`

Solved: stated here without proof.

> Yu [Yu23] showed that the union-closed sets conjecture holds with a constant of approximately
> 0.38234 instead of 1/2.
> [Yu23] Yu, Lei (2023). "Dimension-free bounds for the union-closed sets conjecture". Entropy. 25 (5): 767.

```lean
theorem union_closed.variants.yu
    [Nonempty n]
    (h_ne_singleton_empty : A ≠ {∅})
    (h_union_closed : IsUnionClosed A) :
    ∃ i : n, (0.38234 : ℚ) * #A ≤ #{x ∈ A | i ∈ x}
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L72).

## `UnionClosed.union_closed.variants.univ_card`

Solved: stated here without proof.

> Vuckovic and Zivkovic [Vu17] showed that the union-closed sets conjecture holds for set families
> whose universal set has cardinality at most 12.
> [Vu17] Vuckovic, Bojan; Zivkovic, Miodrag (2017). "The 12-Element Case of Frankl's Conjecture" (PDF). IPSI BGD Transactions on Internet Research. 13 (1): 65.

```lean
theorem union_closed.variants.univ_card
    [Fintype n] [Nonempty n]
    (h_ne_singleton_empty : A ≠ {∅})
    (h_union_closed : IsUnionClosed A)
    (h_card : Fintype.card n ≤ 12) :
    ∃ i : n, (1 / 2 : ℚ) * #A ≤ #{x ∈ A | i ∈ x}
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L85).

## `UnionClosed.union_closed.variants.family_card`

Solved: stated here without proof.

> Roberts and Simpson [Ro10] showed that the union-closed sets conjecture holds for set families of
> size at most 46.
> Their method, however, combined with the result of [Vu17], further shows that it holds for `#A ≤ 50`
> as well.
> [Ro10] Roberts, Ian; Simpson, Jamie (2010). "A note on the union-closed sets conjecture" (PDF). Australas. J. Combin. 47: 265–267.
> [Vu17] Vuckovic, Bojan; Zivkovic, Miodrag (2017). "The 12-Element Case of Frankl's Conjecture" (PDF). IPSI BGD Transactions on Internet Research. 13 (1): 65.

```lean
theorem union_closed.variants.family_card
    [Nonempty n]
    (h_ne_singleton_empty : A ≠ {∅})
    (h_union_closed : IsUnionClosed A)
    (hA : #A ≤ 50) :
    ∃ i : n, (1 / 2 : ℚ) * #A ≤ #{x ∈ A | i ∈ x}
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L102).

## `UnionClosed.union_closed.variants.univ_card_two`

Proved here.

> We can show the union-closed sets conjecture is true for the case where the universal set has
> cardinality 2, by brute force.

```lean
theorem union_closed.variants.univ_card_two (A : Finset (Finset (Fin 2)))
    (h_ne_singleton_empty : A ≠ {∅})
    (h_union_closed : IsUnionClosed A) :
    ∃ i, (1 / 2 : ℚ) * #A ≤ #{x ∈ A | i ∈ x}
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L115).

## `UnionClosed.union_closed.variants.singleton_mem`

Proved here.

> We can show the union-closed sets conjecture is true for the case where the set family contains
> some singleton.

```lean
theorem union_closed.variants.singleton_mem
    (h_union_closed : IsUnionClosed A)
    (i : n) (hi : {i} ∈ A) :
    ∃ i, (1 / 2 : ℚ) * #A ≤ #{x ∈ A | i ∈ x}
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L126).

## `UnionClosed.union_closed.variants.sharpness`

Proved here.

> The union-closed sets conjecture is sharp in the sense that if we replace the constant `1/2` with
> any larger constant, then the conjecture fails.

```lean
theorem union_closed.variants.sharpness [Fintype n] (c : ℝ) (hc : 1 / 2 < c) :
    ¬ (∀ A : Finset (Finset n), A ≠ {∅} → IsUnionClosed A →
        ∃ i : n, c * #A ≤ #{x ∈ A | i ∈ x})
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L155).

## `UnionClosed.union_closed.variants.cardinality_even_of_union_closed_tight`

Open: stated without proof.

> The union-closed sets conjecture is tight for a union-closed family `A` if the largest number of
> sets in `A` containing a common element is exactly half of the sets in `A`, that is,
> $\max_i |\{X \in A : i \in X\}| = |A| / 2$.
>
> If the union-closed sets conjecture is tight for some family `A` then $|A| = 2^k$ for some $k$.
> This is the first part of Conjecture 3 in the reference below; its second part (that the
> family then contains the power set of a $k$-element set as a "submatrix") is not formalized here.
>
> Reference: Conjecture 3 in https://www.nieuwarchief.nl/serie5/pdf/naw5-2023-24-4-225.pdf.

```lean
theorem union_closed.variants.cardinality_even_of_union_closed_tight
    [Nonempty n]
    (h_ne_singleton_empty : A ≠ {∅})
    (h_ne_empty : A ≠ ∅)
    (h_union_closed : IsUnionClosed A)
    (h_tight : IsGreatest (Set.range fun i : n => (#{x ∈ A | i ∈ x} : ℚ)) ((1 / 2 : ℚ) * #A)) :
    ∃ k, #A = 2 ^ k
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/UnionClosed.lean, line 216](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean#L216).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/UnionClosed.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/UnionClosed.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Union-closed_sets_conjecture)
