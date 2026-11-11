---
declaration: theorem
origin: cited
lean: TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_finiteExtension
statement: formalized
proof: formalized
---

# Finite-extension compatibility of the nonexceptional marked presentation

For `L/K`
finite with `μ_p ⊆ K` and `q(L) ≠ 2`, choose the marked normal form `e` of `G_L(p)` so that its
map `φ` to any presentation `mK` of `G_K(p)` commutes with the map induced by the embedding
`σ : L →ₐ[K] Kˢ`. The image of `φ` is open of index dividing `[L : K]`, and the orientation
read through `mK` takes the prescribed values on the images of the marked generators.
No containment of `L` in the maximal pro-`p` extension of `K` is required.

```lean
TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_finiteExtension.{u_1} (p : ℕ)
  [Fact (Nat.Prime p)] (K L : Type) [Field K] [Field L] [Algebra K L] [FiniteDimensional K L]
  [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra ℚ_[p] L]
  [ValuativeExtension ℚ_[p] L] {P : Type u_1} [Group P] [TopologicalSpace P]
  (σ : L →ₐ[K] SeparableClosure K) (hmuK : ∃ ζ, IsPrimitiveRoot ζ p)
  (hq : TauCeti.localRootOfUnityOrder p L ⋯ ≠ 2) (mK : TauCeti.absoluteGaloisGroupProP p K ≃ₜ* P) :
  ∃ e φ,
    (∀ (x : TauCeti.absoluteGaloisGroupProP p L),
        φ (e x) =
          mK ((TauCeti.maximalProPQuotient.map (TauCeti.absoluteGaloisGroupExtend K L σ) ⋯) x)) ∧
      IsOpen ↑φ.range ∧
        φ.range.index ∣ Module.finrank K L ∧
          ↑((TauCeti.cyclotomicOrientation p K hmuK)
                    (mK.symm
                      (φ
                        (TauCeti.presentedProPGen p (Module.finrank ℚ_[p] L + 2)
                          {TauCeti.demushkinWordNeTwo (TauCeti.localRootOfUnityOrder p L ⋯)
                              (Module.finrank ℚ_[p] L + 2)
                              (TauCeti.freeProPGen p (Module.finrank ℚ_[p] L + 2))}
                          1)))) *
                (1 - ↑(TauCeti.localRootOfUnityOrder p L ⋯)) =
              1 ∧
            ∀ (i : ℕ),
              i ≠ 1 →
                i < Module.finrank ℚ_[p] L + 2 →
                  (TauCeti.cyclotomicOrientation p K hmuK)
                      (mK.symm
                        (φ
                          (TauCeti.presentedProPGen p (Module.finrank ℚ_[p] L + 2)
                            {TauCeti.demushkinWordNeTwo (TauCeti.localRootOfUnityOrder p L ⋯)
                                (Module.finrank ℚ_[p] L + 2)
                                (TauCeti.freeProPGen p (Module.finrank ℚ_[p] L + 2))}
                            i))) =
                    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../../topology/algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../../topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The Demushkin predicate](../../../topology/profinite-and-pro-p-groups/part-01/the-demushkin-predicate.md)
- [Demushkin's theorem](demushkins-theorem.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [Labute's criterion](../../../topology/profinite-and-pro-p-groups/part-01/labutes-criterion.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../../topology/algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [The relative successive-approximation theorem](../../../topology/profinite-and-pro-p-groups/part-02/the-relative-successive-approximation-theorem.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [The unconstrained successive-approximation theorem](../../../topology/profinite-and-pro-p-groups/part-01/the-unconstrained-successive-approximation-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_finiteExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/FiniteExtension.html#TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_finiteExtension).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_finiteExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/FiniteExtension.html#TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_finiteExtension)
- [Source of `TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_finiteExtension` in TauCeti/NumberTheory/LocalField/ProP/Marked/FiniteExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/ProP/Marked/FiniteExtension.lean#L48)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalGaloisGroups/STATUS.md)
