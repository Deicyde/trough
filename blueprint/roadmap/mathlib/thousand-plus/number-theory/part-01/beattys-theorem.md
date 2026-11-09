# Beatty's theorem

Mathlib records this with 2 declarations.

`Irrational.beattySeq_symmDiff_beattySeq_pos`: **Rayleigh's theorem** on Beatty sequences. Let `r` be an irrational number greater than 1, and
`1/r + 1/s = 1`. Then `B⁺_r` and `B⁺_s` partition the positive integers.

```lean
Irrational.beattySeq_symmDiff_beattySeq_pos {r s : ℝ} (hrs : r.HolderConjugate s)
  (hr : Irrational r) :
  symmDiff {x | ∃ k > 0, beattySeq r k = x} {x | ∃ k > 0, beattySeq s k = x} = {n | 0 < n}
```

`compl_beattySeq`: Generalization of Rayleigh's theorem on Beatty sequences. Let `r` be a real number greater
than 1, and `1/r + 1/s = 1`. Then the complement of `B_r` is `B'_s`.

```lean
compl_beattySeq {r s : ℝ} (hrs : r.HolderConjugate s) :
  {x | ∃ k, beattySeq r k = x}ᶜ = {x | ∃ k, beattySeq' s k = x}
```

## Depends on

- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Proof depends on

- [Field $\R$ of real numbers](../../../undergraduate/ring-theory/field-theory/field-r-of-real-numbers.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)

## Sources

- [Mathlib documentation: `Irrational.beattySeq_symmDiff_beattySeq_pos`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Rayleigh.html#Irrational.beattySeq_symmDiff_beattySeq_pos)
- [Source of `Irrational.beattySeq_symmDiff_beattySeq_pos` in Mathlib/NumberTheory/Rayleigh.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/Rayleigh.lean#L175)
- [Mathlib documentation: `compl_beattySeq`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/Rayleigh.html#compl_beattySeq)
- [Source of `compl_beattySeq` in Mathlib/NumberTheory/Rayleigh.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/Rayleigh.lean#L118)
- [1000+ theorems list: Q791663](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L895)
- [1000+ theorems project: Q791663](https://1000-plus.github.io/all.html?length=-1#Q791663)
- [Wikipedia: Beatty's theorem](https://en.wikipedia.org/wiki/Beatty's_theorem)
- [Wikidata: Q791663](https://www.wikidata.org/wiki/Q791663)
