---
declaration: theorem
origin: cited
lean: OeisA240088.conjecture
statement: formalized
---

# Ways of writing $n$ as an ordered sum of a triangular, square, and pentagonal number

> The sequence $a(n)$ counts the number of tuples $(i, j, k) \in \mathbb{N}^3$ such that
> $T_i + S_j + P_k = n$, where $T_i = i(i+1)/2$, $S_j = j^2$, and $P_k = k(3k-1)/2$:
>
> $$a(n) = |\{(i, j, k) \in \mathbb{N}^3 : i(i+1)/2 + j^2 + k(3k-1)/2 = n\}|$$
>
> *References:*
> - [A240088](https://oeis.org/A240088)
> - [On universal sums of polygonal numbers](https://doi.org/10.1007/s11425-015-4994-4)
>   by *Zhi-Wei Sun*, Sci. China Math. **58** (2015), 1367–1396.

*Quoted from [FormalConjectures/OEIS/240088.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/240088.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `OeisA240088.conjecture`

Open: stated without proof.

> It is conjectured that $a(n)$ is always positive (Conjecture 1.1 of Sun (2009)).

```lean
theorem conjecture (n : ℕ) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/240088.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/240088.lean#L69).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/240088.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/240088.lean)
- [A240088](https://oeis.org/A240088)
