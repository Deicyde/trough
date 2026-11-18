---
declaration: def
origin: cited
lean: TauCeti.smoothSingularChainHomotopyEquivOfContraction
statement: formalized
---

# The smoothing theorem for a smoothly contractible manifold

If a smooth map
`F : ℝ × M → M` joins the identity `F (0, ·) = id` to a constant map `F (1, ·) = c`, then the
inclusion of smooth singular chains into singular chains with coefficients in `R` is a chain
homotopy equivalence. Its homotopy inverse is induced by the constant map `x ↦ c`.

```lean
TauCeti.smoothSingularChainHomotopyEquivOfContraction.{u, u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {C : Type u_3}
  [CategoryTheory.Category.{u_4, u_3} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasCoproducts C] (R : C) {F : ℝ × M → M}
  (hF : ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) I (↑⊤) F) (c : M)
  (h₀ : ∀ (x : M), F (0, x) = x) (h₁ : ∀ (x : M), F (1, x) = c) :
  HomotopyEquiv ((TauCeti.smoothSingularSubcomplex I M).toSSet.chainComplex R)
    ((TopCat.toSSet.obj ↧M).chainComplex R)
```

## Depends on

- [TauCeti.smoothSingularSubcomplex](tauceti-smoothsingularsubcomplex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.smoothSingularChainHomotopyEquivOfContraction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Contractible.html#TauCeti.smoothSingularChainHomotopyEquivOfContraction).

## Sources

- [Tau Ceti documentation: `TauCeti.smoothSingularChainHomotopyEquivOfContraction`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/SmoothSingular/Contractible.html#TauCeti.smoothSingularChainHomotopyEquivOfContraction)
- [Source of `TauCeti.smoothSingularChainHomotopyEquivOfContraction` in TauCeti/Geometry/Manifold/SmoothSingular/Contractible.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/SmoothSingular/Contractible.lean#L140)
