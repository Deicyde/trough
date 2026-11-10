---
declaration: theorem
origin: cited
lean: TauCeti.finrank_rationalWeylFDRep, TauCeti.oddOrthogonalWeylDimension_eq_prod_prod_div, TauCeti.evenOrthogonalWeylDimension_eq_prod_prod_div, TauCeti.symplecticWeylDimension_eq_prod_prod_div, TauCeti.weylDimension_eq_prod_prod_div
statement: formalized
proof: formalized
---

# The Weyl dimension formula for `GL n`

over a field of characteristic zero, the rational
Weyl module of a dominant weight `λ` has dimension `∏_{i < j} (λᵢ - λⱼ + j - i) / (j - i)`, the
Weyl dimension of `λ`.

```lean
TauCeti.finrank_rationalWeylFDRep.{u} (k : Type u) [Field k] [CharZero k] (n : ℕ)
  (l : TauCeti.DominantWeight n) :
  Module.finrank k ↑(TauCeti.rationalWeylFDRep k n l).V = TauCeti.weylDimension l
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gelfand-Tsetlin dimension formula](the-gelfand-tsetlin-dimension-formula.md)
- [The inverse of Frobenius's formula](../symmetric/the-inverse-of-frobeniuss-formula.md)
- [James's submodule theorem](../symmetric/jamess-submodule-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_rationalWeylFDRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/Dimension.html#TauCeti.finrank_rationalWeylFDRep).

## Other forms

**The Weyl dimension formula for `SO (2n + 1)` in its product form.** Formalized in Tau Ceti as [`TauCeti.oddOrthogonalWeylDimension_eq_prod_prod_div`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylDimension/OddOrthogonal.html#TauCeti.oddOrthogonalWeylDimension_eq_prod_prod_div).

```lean
TauCeti.oddOrthogonalWeylDimension_eq_prod_prod_div (n : ℕ) (μ : YoungDiagram) :
  ↑(TauCeti.oddOrthogonalWeylDimension n μ) =
    ∏ i ∈ Finset.range n,
      (↑(μ.rowLen i) + ↑n - ↑i - 1 / 2) / (↑n - ↑i - 1 / 2) *
        ∏ j ∈ Finset.Ico (i + 1) n,
          ((↑(μ.rowLen i) + ↑n - ↑i - 1 / 2) ^ 2 - (↑(μ.rowLen j) + ↑n - ↑j - 1 / 2) ^ 2) /
            ((↑n - ↑i - 1 / 2) ^ 2 - (↑n - ↑j - 1 / 2) ^ 2)
```

**The Weyl dimension formula for `SO (2n)` in its product form.** Formalized in Tau Ceti as [`TauCeti.evenOrthogonalWeylDimension_eq_prod_prod_div`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylDimension/EvenOrthogonal.html#TauCeti.evenOrthogonalWeylDimension_eq_prod_prod_div).

```lean
TauCeti.evenOrthogonalWeylDimension_eq_prod_prod_div (n : ℕ) (μ : YoungDiagram) :
  ↑(TauCeti.evenOrthogonalWeylDimension n μ) =
    ∏ i ∈ Finset.range n,
      ∏ j ∈ Finset.Ico (i + 1) n,
        ((↑(μ.rowLen i) + ↑n - 1 - ↑i) ^ 2 - (↑(μ.rowLen j) + ↑n - 1 - ↑j) ^ 2) /
          ((↑n - 1 - ↑i) ^ 2 - (↑n - 1 - ↑j) ^ 2)
```

**The Weyl dimension formula for `Sp 2n` in its product form.** Formalized in Tau Ceti as [`TauCeti.symplecticWeylDimension_eq_prod_prod_div`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylDimension/Symplectic.html#TauCeti.symplecticWeylDimension_eq_prod_prod_div).

```lean
TauCeti.symplecticWeylDimension_eq_prod_prod_div (n : ℕ) (μ : YoungDiagram) :
  ↑(TauCeti.symplecticWeylDimension n μ) =
    ∏ i ∈ Finset.range n,
      ↑(TauCeti.symplecticRhoShift n μ i) / (↑n - ↑i) *
        ∏ j ∈ Finset.Ico (i + 1) n,
          (↑(TauCeti.symplecticRhoShift n μ i) ^ 2 - ↑(TauCeti.symplecticRhoShift n μ j) ^ 2) /
            ((↑n - ↑i) ^ 2 - (↑n - ↑j) ^ 2)
```

**The Weyl dimension formula in its quotient form.** Formalized in Tau Ceti as [`TauCeti.weylDimension_eq_prod_prod_div`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylDimension/Basic.html#TauCeti.weylDimension_eq_prod_prod_div).

```lean
TauCeti.weylDimension_eq_prod_prod_div {n : ℕ} (l : TauCeti.DominantWeight n) :
  ↑(TauCeti.weylDimension l) = ∏ i, ∏ j > i, (↑(↑l i) - ↑(↑l j) + (↑↑j - ↑↑i)) / (↑↑j - ↑↑i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_rationalWeylFDRep`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/Dimension.html#TauCeti.finrank_rationalWeylFDRep)
- [Source of `TauCeti.finrank_rationalWeylFDRep` in TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ClassicalGroups/WeylModule/Dimension.lean#L73)
