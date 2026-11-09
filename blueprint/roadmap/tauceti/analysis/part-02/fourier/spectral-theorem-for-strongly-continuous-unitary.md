---
declaration: theorem
origin: cited
lean: ContRepresentation.exists_pontryaginMeasureTransform_eq_inner
statement: formalized
proof: formalized
---

# Spectral theorem for strongly continuous unitary representations, cyclic form

For a
strongly continuous unitary representation `π` of a locally compact abelian group `G` on a
Hilbert space `H` and a vector `ξ`, the matrix coefficient `g ↦ ⟪ξ, π(g) ξ⟫` is the
Fourier–Stieltjes transform of a finite inner regular measure on the Pontryagin dual of `G`.

```lean
ContRepresentation.exists_pontryaginMeasureTransform_eq_inner.{u_1, u_2} {G : Type u_1}
  [AddCommGroup G] [TopologicalSpace G] [IsTopologicalAddGroup G] [LocallyCompactSpace G]
  [MeasurableSpace (PontryaginDual (Multiplicative G))]
  [BorelSpace (PontryaginDual (Multiplicative G))] {H : Type u_2} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] (π : ContRepresentation ℂ (Multiplicative G) H)
  (hcont : ∀ (v : H), Continuous fun g => (π (Multiplicative.ofAdd g)) v) (hπ : π.IsUnitary)
  (ξ : H) :
  ∃ μ,
    (↑μ).InnerRegular ∧
      ∀ (g : G), μ.pontryaginMeasureTransform g = inner ℂ ξ ((π (Multiplicative.ofAdd g)) ξ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContRepresentation.exists_pontryaginMeasureTransform_eq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.html#ContRepresentation.exists_pontryaginMeasureTransform_eq_inner).

## Sources

- [Tau Ceti documentation: `ContRepresentation.exists_pontryaginMeasureTransform_eq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.html#ContRepresentation.exists_pontryaginMeasureTransform_eq_inner)
- [Source of `ContRepresentation.exists_pontryaginMeasureTransform_eq_inner` in TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/Pontryagin/StronglyContinuous.lean#L292)
