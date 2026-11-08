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
- [Dimension shifting in every positive degree, `Hⁱ⁺¹(G, M) ≅ Hⁱ(G, Coind_1^G M ⧸ M)` for `i ≥ 1` and a compact group `G`, as an isomorphism of Mathlib's canonical continuous cohomology](../../../representation-theory/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree-hi-1.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](../class-field-theory/the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [Local Tate duality in degree one](../../part-02/class-field-theory/local-tate-duality-in-degree-one.md)
- [Serre's theorem at arbitrary rank, as an equivalence](../../../topology/profinite-and-pro-p-groups/part-01/serres-theorem-at-arbitrary-rank-as-an-equivalen.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Free.html#TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Free.html#TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu)
- [Source of `TauCeti.nonempty_continuousMulEquiv_freeProP_of_not_mu` in TauCeti/NumberTheory/LocalField/ProP/Free.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/Free.lean#L152)
