---
declaration: theorem
origin: cited
lean: SparseRuler.wichmann_conjecture
statement: formalized
---

# Sparse Ruler

> A sparse ruler of length $L$ is a sequence of marks $0 = a_1 < a_2 < \dots < a_m = L$.
> A distance $k \in \mathbb{N}$ can be measured if there are $i, j \in \{1, \dots, m\}$, such that
> $k = a_j - a_i$.
>
> One question concerns the structure of *optimal* rulers. Wichmann [Wi63] gave a
> parametric family of sparse rulers and speculated that every sufficiently large optimal ruler
> is of his type. The Wikipedia article records that no optimal ruler of length $1, 13, 17, 23$
> or $58$ is a Wichmann ruler, and that every other optimal length up to $213$ is attained by one;
> non-Wichmann optimal rulers also occur alongside Wichmann ones at lengths $9, 29, 50$ and $68$.
>
> The asymptotic growth of the minimal number of marks of an optimal ruler of length $L$ — i.e.
> the limit of $l(n)^2 / n$, conjectured to lie in $[2.434\ldots, 3]$ — is the subject of
> `FormalConjectures.ErdosProblems.«170»` (there phrased via $F(N)/\sqrt{N}$), and is not
> restated here.
>
> *References:*
> - [Wi63] Wichmann, B. "A note on restricted difference bases." Journal of the London
>   Mathematical Society 38 (1963): 465-466.
> - [Wikipedia](https://en.wikipedia.org/wiki/Sparse_ruler)

*Quoted from [FormalConjectures/Wikipedia/SparseRuler.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SparseRuler.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 API statements, counted here but not shown.

## `SparseRuler.wichmann_conjecture`

Open: stated without proof.

> **Wichmann's conjecture on optimal rulers.** Every optimal ruler of sufficiently large
> length is a Wichmann ruler $W(r, s)$ (up to reflection, i.e. reversing the segment list).
> Posed by Wichmann [Wi63]. The Wikipedia article records that no optimal ruler of length
> $1, 13, 17, 23$ or $58$ is a Wichmann ruler, and that every other optimal length up to $213$ is
> attained by one; non-Wichmann optimal rulers also occur alongside Wichmann ones at lengths
> $9, 29, 50$ and $68$.

```lean
theorem wichmann_conjecture :
    ∃ N : ℕ, ∀ g : List ℕ, IsOptimal g → N < g.sum →
      ∃ r s : ℕ, g = wichmannGaps r s ∨ g = (wichmannGaps r s).reverse
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SparseRuler.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SparseRuler.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SparseRuler.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/SparseRuler.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Sparse_ruler)
