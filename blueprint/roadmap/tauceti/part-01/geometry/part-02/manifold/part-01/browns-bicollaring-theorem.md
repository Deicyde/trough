---
declaration: theorem
origin: cited
lean: TauCeti.brownBicollaring, TauCeti.IsLocallyBicollaredWithSides.exists_isBicollar, TauCeti.IsLocallyBicollared.exists_isBicollar, TauCeti.IsLocallyBicollared.isBicollared_of_not_isPreconnected_compl_range, TauCeti.IsLocallyFlat.isBicollared_of_not_isPreconnected_compl_range
statement: formalized
proof: formalized
---

# Brown's bicollaring theorem

every locally flat embedding of the standard `n`-sphere
in the standard `(n + 1)`-sphere is globally bicollared, including `n = 0`.

```lean
TauCeti.brownBicollaring (n : ℕ) : TauCeti.BrownBicollaring n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brown's collaring theorem, for a compact domain](browns-collaring-theorem-for-a-compact-domain.md)
- [The Jordan–Brouwer separation theorem](../../../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.brownBicollaring`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocallyFlat/Brown.html#TauCeti.brownBicollaring).

## Other forms

**Brown's bicollaring theorem, for a compact domain.** Formalized in Tau Ceti as [`TauCeti.IsLocallyBicollaredWithSides.exists_isBicollar`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocallyFlat/TwoSided.html#TauCeti.IsLocallyBicollaredWithSides.exists_isBicollar).

```lean
TauCeti.IsLocallyBicollaredWithSides.exists_isBicollar.{u_1, u_2} {M : Type u_1} {N : Type u_2}
  [TopologicalSpace M] [TopologicalSpace N] {f : N → M} {A B : Set M} [CompactSpace N] [T2Space M]
  (h : TauCeti.IsLocallyBicollaredWithSides f A B) (hf : Function.Injective f) (hA : IsOpen A)
  (hB : IsOpen B) (hAB : Disjoint A B) :
  ∃ b,
    TauCeti.IsBicollar f b ∧
      Set.MapsTo b (Set.univ ×ˢ Set.Ioi 0) A ∧ Set.MapsTo b (Set.univ ×ˢ Set.Iio 0) B
```

**Brown's bicollaring theorem for separating maps.** Formalized in Tau Ceti as [`TauCeti.IsLocallyBicollared.exists_isBicollar`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocallyFlat/Separation.html#TauCeti.IsLocallyBicollared.exists_isBicollar).

```lean
TauCeti.IsLocallyBicollared.exists_isBicollar.{u_1, u_2} {M : Type u_1} {N : Type u_2}
  [TopologicalSpace M] [TopologicalSpace N] {f : N → M} {A B : Set M} [CompactSpace N]
  [PreconnectedSpace N] [LocallyConnectedSpace N] [T2Space M] [PreconnectedSpace M]
  (h : TauCeti.IsLocallyBicollared f) (hf : Function.Injective f) (hA : IsOpen A) (hB : IsOpen B)
  (hAB : Disjoint A B) (hcompl : (Set.range f)ᶜ = A ∪ B) (hA₀ : A.Nonempty) (hB₀ : B.Nonempty) :
  ∃ b,
    TauCeti.IsBicollar f b ∧
      Set.MapsTo b (Set.univ ×ˢ Set.Ioi 0) A ∧ Set.MapsTo b (Set.univ ×ˢ Set.Iio 0) B
```

**Brown's bicollaring theorem for separating maps, in terms of connectedness.** Formalized in Tau Ceti as [`TauCeti.IsLocallyBicollared.isBicollared_of_not_isPreconnected_compl_range`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocallyFlat/Separation.html#TauCeti.IsLocallyBicollared.isBicollared_of_not_isPreconnected_compl_range).

```lean
TauCeti.IsLocallyBicollared.isBicollared_of_not_isPreconnected_compl_range.{u_1, u_2} {M : Type u_1}
  {N : Type u_2} [TopologicalSpace M] [TopologicalSpace N] {f : N → M} [CompactSpace N]
  [PreconnectedSpace N] [LocallyConnectedSpace N] [T2Space M] [PreconnectedSpace M]
  (h : TauCeti.IsLocallyBicollared f) (hf : Function.Injective f)
  (hsep : ¬IsPreconnected (Set.range f)ᶜ) : TauCeti.IsBicollared f
```

**Brown's bicollaring theorem for separating spheres.** Formalized in Tau Ceti as [`TauCeti.IsLocallyFlat.isBicollared_of_not_isPreconnected_compl_range`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocallyFlat/Sphere.html#TauCeti.IsLocallyFlat.isBicollared_of_not_isPreconnected_compl_range).

```lean
TauCeti.IsLocallyFlat.isBicollared_of_not_isPreconnected_compl_range {n : ℕ} (hn : n ≠ 0)
  {f : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  (hf : TauCeti.IsLocallyFlat (EuclideanSpace ℝ (Fin n)) ℝ f)
  (hsep : ¬IsPreconnected (Set.range f)ᶜ) : TauCeti.IsBicollared f
```

## Sources

- [Tau Ceti documentation: `TauCeti.brownBicollaring`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocallyFlat/Brown.html#TauCeti.brownBicollaring)
- [Source of `TauCeti.brownBicollaring` in TauCeti/Geometry/Manifold/LocallyFlat/Brown.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/LocallyFlat/Brown.lean#L37)
