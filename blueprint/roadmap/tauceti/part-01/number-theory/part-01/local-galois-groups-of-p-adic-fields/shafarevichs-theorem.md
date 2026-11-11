---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu
statement: formalized
proof: formalized
---

# Shafarevich's theorem

If a finite compatible extension `K` of `ℚ_[p]` contains no
primitive `p`th root of unity, its maximal pro-`p` Galois group `G_K(p)` is the free pro-`p` group
on `[K : ℚ_[p]] + 1` generators.

```lean
TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu (p : ℕ) [Fact (Nat.Prime p)] (K : Type)
  [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Algebra ℚ_[p] K]
  [ValuativeExtension ℚ_[p] K] (hmu : ¬∃ ζ, IsPrimitiveRoot ζ p) :
  Nonempty
    (TauCeti.absoluteGaloisGroupProP p K ≃ₜ* TauCeti.freeProP p (Fin (Module.finrank ℚ_[p] K + 1)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../../../topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [Dimension shifting in every positive degree](../../../representation-theory/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../class-field-theory/the-local-invariant.md)
- [Local Tate duality in degree one](../../part-02/class-field-theory/local-tate-duality-in-degree-one.md)
- [Serre's theorem at arbitrary rank, as an equivalence](../../../topology/profinite-and-pro-p-groups/part-01/serres-theorem-at-arbitrary-rank-as-an-equivalen.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Free.html#TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Free.html#TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu)
- [Source of `TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu` in TauCeti/NumberTheory/LocalField/ProP/Free.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/ProP/Free.lean#L152)
