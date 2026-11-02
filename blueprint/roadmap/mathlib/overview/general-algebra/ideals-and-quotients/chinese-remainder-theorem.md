---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Ideal.quotientInfRingEquivPiQuotient, ZMod.chineseRemainder
mathlib_file: Mathlib/RingTheory/Ideal/Quotient/Operations.lean
---

# Chinese remainder theorem

Mathlib records this with 2 declarations.

`Ideal.quotientInfRingEquivPiQuotient`: **Chinese Remainder Theorem**. Eisenbud Ex.2.6.
Similar to Atiyah-Macdonald 1.10 and Stacks 00DT

```lean
Ideal.quotientInfRingEquivPiQuotient.{u_2, u_3} {R : Type u_2} [CommRing R] {ι : Type u_3}
  [Finite ι] (f : ι → Ideal R) (hf : Pairwise (Function.onFun IsCoprime f)) :
  R ⧸ ⨅ i, f i ≃+* ((i : ι) → R ⧸ f i)
```

`ZMod.chineseRemainder`: The **Chinese remainder theorem**. For a pair of coprime natural numbers, `m` and `n`,
  the rings `ZMod (m * n)` and `ZMod m × ZMod n` are isomorphic.

See `Ideal.quotientInfRingEquivPiQuotient` for the Chinese remainder theorem for ideals in any
ring.

```lean
ZMod.chineseRemainder {m n : ℕ} (h : m.Coprime n) : ZMod (m * n) ≃+* ZMod m × ZMod n
```

## Depends on

- [Associative algebra over a commutative ring](../algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Characteristic p](../field-theory/characteristic-p.md)
- [Coprime element](../divisibility-in-integral-domains/coprime-element.md)
- [Euclid's' algorithm](../divisibility-in-integral-domains/euclids-algorithm.md)
- [Quotient ring](quotient-ring.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)
- [Sum of subspaces](../../../undergraduate/linear-algebra/fundamentals/sum-of-subspaces.md)

## Sources

- [Mathlib documentation: `Ideal.quotientInfRingEquivPiQuotient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Ideal/Quotient/Operations.html#Ideal.quotientInfRingEquivPiQuotient)
- [Source of `Ideal.quotientInfRingEquivPiQuotient` in Mathlib/RingTheory/Ideal/Quotient/Operations.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/Ideal/Quotient/Operations.lean#L245)
- [Mathlib documentation: `ZMod.chineseRemainder`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/ZMod/Basic.html#ZMod.chineseRemainder)
- [Source of `ZMod.chineseRemainder` in Mathlib/Data/ZMod/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Data/ZMod/Basic.lean#L883)
- [Mathlib overview: General algebra › Ideals and quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L79)
- [Mathlib undergraduate list: Ring Theory › Ideals and Quotients](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L136)
- [1000+ theorems list: Q193878](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L171)
- [1000+ theorems project: Q193878](https://1000-plus.github.io/?length=-1#Q193878)
- [Wikipedia: Chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
- [Wikidata: Q193878](https://www.wikidata.org/wiki/Q193878)
