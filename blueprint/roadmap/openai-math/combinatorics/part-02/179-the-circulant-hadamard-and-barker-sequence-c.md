---
declaration: section
origin: cited
lean: OAI.CirculantHadamard.exists_iff_order_one_or_four, OAI.CirculantHadamard.Barker.even_length_eq_two_or_four
statement: formalized
proof: formalized
---

# 179. The circulant Hadamard and Barker-sequence conjectures

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that real circulant Hadamard matrices exist exactly in orders 1 and 4, resolving the circulant Hadamard conjecture. Together with classical Barker-sequence results, this shows that binary sequences whose nontrivial aperiodic autocorrelations have magnitude at most 1 exist at lengths *n* > 1 exactly when $n\in\{2,3,4,5,7,11,13\}$.

## The circulant Hadamard conjecture

We prove the circulant Hadamard conjecture: a real circulant Hadamard matrix has order 1 or 4. As a consequence, Barker sequences of length greater than one exist exactly at lengths 2, 3, 4, 5, 7, 11, 13, proving the Barker-sequence conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-circulant-Hadamard-conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the circulant Hadamard conjecture in exact form: a real circulant Hadamard matrix of positive order $n$ exists exactly when $n=1$ or $n=4$. Explicit witnesses are supplied for both orders, with no restriction on prime factors.

It also proves the even-length part of the Barker-sequence consequence. A positive even-length sign sequence whose nonzero aperiodic autocorrelations have absolute value at most one must have length $2$ or $4$. The paper's classification of odd Barker lengths is outside this selected additional statement.

## Lean: Classification of circulant Hadamard orders

```lean
theorem exists_iff_order_one_or_four (n : ℕ) (hn : 0 < n) :
    ExistsRealCirculantHadamard n ↔ n = 1 ∨ n = 4
```

Stated in [CirculantHadamard.lean, line 24](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CirculantHadamard.lean#L24). Proved in [lean/OAI/LinearAlgebra/CirculantHadamard/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/LinearAlgebra/CirculantHadamard/Main.lean#L21). formalization.yaml lists it as one of the repository's main results.

## Lean: Classification of positive even Barker lengths

```lean
theorem even_length_eq_two_or_four {n : ℕ} (h : Fin n → ℤ)
    (hnpos : 0 < n) (hn : Even n) (hb : IsBarker h) : n = 2 ∨ n = 4
```

Stated in [EvenBarker.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/EvenBarker.lean#L21). Proved in [lean/OAI/LinearAlgebra/Barker/Main.lean, line 63](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/LinearAlgebra/Barker/Main.lean#L63).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/179.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/179.md)
