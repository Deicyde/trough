---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.integral_divergence_of_hasFDerivAt_off_countable
mathlib_file: Mathlib/MeasureTheory/Integral/DivergenceTheorem.lean
---

# Divergence theorem

**Divergence theorem** for Bochner integral. If `f : ℝⁿ⁺¹ → Eⁿ⁺¹` is continuous on a rectangular
box `[a, b] : Set ℝⁿ⁺¹`, `a ≤ b`, is differentiable on its interior with derivative
`f' : ℝⁿ⁺¹ → ℝⁿ⁺¹ →L[ℝ] Eⁿ⁺¹` and the divergence `fun x ↦ ∑ i, f' x eᵢ i` is integrable on `[a, b]`,
where `eᵢ = Pi.single i 1` is the `i`-th basis vector, then its integral is equal to the sum of
integrals of `f` over the faces of `[a, b]`, taken with appropriate signs.

Moreover, the same is true if the function is not differentiable at countably many
points of the interior of `[a, b]`.

We represent both faces `x i = a i` and `x i = b i` as the box
`face i = [a ∘ Fin.succAbove i, b ∘ Fin.succAbove i]` in `ℝⁿ`, where
`Fin.succAbove : Fin n ↪o Fin (n + 1)` is the order embedding with range `{i}ᶜ`. The restrictions
of `f : ℝⁿ⁺¹ → Eⁿ⁺¹` to these faces are given by `f ∘ backFace i` and `f ∘ frontFace i`, where
`backFace i = Fin.insertNth i (a i)` and `frontFace i = Fin.insertNth i (b i)` are embeddings
`ℝⁿ → ℝⁿ⁺¹` that take `y : ℝⁿ` and insert `a i` (resp., `b i`) as `i`-th coordinate.

```lean
MeasureTheory.integral_divergence_of_hasFDerivAt_off_countable.{u} {E : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {n : ℕ} (a b : Fin (n + 1) → ℝ) (hle : a ≤ b)
  (f : (Fin (n + 1) → ℝ) → Fin (n + 1) → E)
  (f' : (Fin (n + 1) → ℝ) → (Fin (n + 1) → ℝ) →L[ℝ] Fin (n + 1) → E) (s : Set (Fin (n + 1) → ℝ))
  (hs : s.Countable) (Hc : ContinuousOn f (Set.Icc a b))
  (Hd : ∀ x ∈ (Set.univ.pi fun i => Set.Ioo (a i) (b i)) \ s, HasFDerivAt f (f' x) x)
  (Hi :
    MeasureTheory.IntegrableOn (fun x => ∑ i, (f' x) (Pi.single i 1) i) (Set.Icc a b)
      MeasureTheory.volume) :
  ∫ (x : Fin (n + 1) → ℝ) in Set.Icc a b, ∑ i, (f' x) (Pi.single i 1) i =
    ∑ i,
      ((∫ (x : Fin n → ℝ) in Set.Icc (a ∘ i.succAbove) (b ∘ i.succAbove),
          f (i.insertNth (b i) x) i) -
        ∫ (x : Fin n → ℝ) in Set.Icc (a ∘ i.succAbove) (b ∘ i.succAbove), f (i.insertNth (a i) x) i)
```

## Depends on

- [Bochner integral](../part-01/bochner-integral.md)
- [Differentiable function between normed vector spaces](../../differentiability/differentiable-function-between-normed-vector-sp.md)
- [Lebesgue measure (Measures and integral calculus)](../part-01/lebesgue-measure.md)
- [Product of finitely many measures](product-of-finitely-many-measures.md)

## Proof depends on

- [Algebra of endomorphisms of a vector space](../../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md)
- [Hausdorff space](../../../topology/general-topology/part-01/hausdorff-space.md)
- [Measurable function](../part-01/measurable-function.md)
- [Order topology](../../../topology/topological-algebra/order-topology.md)
- [Pointwise convergence](../../../../undergraduate/single-variable-real-analysis/sequences-and-series-of-functions/pointwise-convergence.md)
- [Riemann sums](../../../../undergraduate/single-variable-real-analysis/integration/riemann-sums.md)
- [Ring structure $\Z$](../../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `MeasureTheory.integral_divergence_of_hasFDerivAt_off_countable`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Integral/DivergenceTheorem.html#MeasureTheory.integral_divergence_of_hasFDerivAt_off_countable)
- [Source of `MeasureTheory.integral_divergence_of_hasFDerivAt_off_countable` in Mathlib/MeasureTheory/Integral/DivergenceTheorem.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/MeasureTheory/Integral/DivergenceTheorem.lean#L252)
- [Mathlib overview: Analysis › Measures and integral calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L363)
- [1000+ theorems list: Q338886](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L373)
- [1000+ theorems project: Q338886](https://1000-plus.github.io/all.html?length=-1#Q338886)
- [Wikipedia: Divergence theorem](https://en.wikipedia.org/wiki/Divergence_theorem)
- [Wikidata: Q338886](https://www.wikidata.org/wiki/Q338886)
