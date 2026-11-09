# Helly's theorem

**Helly's theorem** for finite families of convex sets in its classical form.

If `F` is a family of `n` convex sets in a vector space of finite dimension `d`, with `n ≥ d + 1`,
and any `d + 1` sets of `F` intersect nontrivially, then all sets of `F` intersect nontrivially.

```lean
Convex.helly_theorem.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3} [Field 𝕜]
  [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [AddCommGroup E] [_root_.Module 𝕜 E]
  [FiniteDimensional 𝕜 E] {F : ι → Set E} {s : Finset ι} (h_card : Module.finrank 𝕜 E + 1 ≤ s.card)
  (h_convex : ∀ i ∈ s, Convex 𝕜 (F i))
  (h_inter : ∀ I ⊆ s, I.card = Module.finrank 𝕜 E + 1 → (⋂ i ∈ I, F i).Nonempty) :
  (⋂ i ∈ s, F i).Nonempty
```

## Depends on

- [Cardinal](../../../overview/logic-and-computation/set-theory/cardinals/cardinal.md)
- [Convex subsets](../../../undergraduate/affine-and-euclidean-geometry/convexity/convex-subsets.md)
- [Field](../../../overview/general-algebra/field-theory/field.md)
- [Finite-dimensionality](../../../overview/linear-algebra/finite-dimensional-vector-spaces/finite-dimensionality.md)
- [Linear independence](../../../undergraduate/linear-algebra/fundamentals/linear-independence.md)

## Proof depends on

- [Euclidean domain](../../../overview/general-algebra/divisibility-in-integral-domains/euclidean-domain.md)
- [Radon's theorem](radons-theorem.md)

## Sources

- [Mathlib documentation: `Convex.helly_theorem`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Convex/Radon.html#Convex.helly_theorem)
- [Source of `Convex.helly_theorem` in Mathlib/Analysis/Convex/Radon.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Convex/Radon.lean#L141)
- [1000+ theorems list: Q1632433](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1812)
- [1000+ theorems project: Q1632433](https://1000-plus.github.io/all.html?length=-1#Q1632433)
- [Wikipedia: Helly's theorem](https://en.wikipedia.org/wiki/Helly's_theorem)
- [Wikidata: Q1632433](https://www.wikidata.org/wiki/Q1632433)
