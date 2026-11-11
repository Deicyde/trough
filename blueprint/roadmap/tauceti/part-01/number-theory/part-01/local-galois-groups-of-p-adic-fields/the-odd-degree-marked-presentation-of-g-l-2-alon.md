---
declaration: theorem
origin: cited
lean: TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_finiteExtension
statement: formalized
proof: formalized
---

# The odd-degree marked presentation of `G_L(2)` along a finite extension

Let `L/K` be a
finite extension embedded in `Kˢ` by `σ`, where `K` contains a primitive square root of unity and
`L` is a finite extension of `ℚ₂` of odd degree `N`, and let `m_K : G_K(2) ≃ₜ* P` be any
presentation of `G_K(2)`. Then the marked presentation `e` of `G_L(2)` by
`⟨x₁, …, x_{N+2} ∣ x₁² x₂⁴ (x₂, x₃) (x₄, x₅) ⋯ (x_{N+1}, x_{N+2})⟩` maps to `P` by the continuous
homomorphism `φ` that `e` and `m_K` read off from `G_L(2) → G_K(2)`, the image of `φ` is open of
index dividing `[L : K]`, and the cyclotomic orientation of `G_K(2)`, read on `P` through `m_K`,
takes the value `-1` on `φ(x₁)`, the value `(1 - 4)⁻¹` on `φ(x₃)`, and the value `1` on the image
of every other marked generator.

```lean
TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_finiteExtension.{u_1, u_2} (K : Type u_1)
  (L : Type) [Field K] [Field L] [Algebra K L] [FiniteDimensional K L] [ValuativeRel L]
  [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra ℚ_[2] L] [ValuativeExtension ℚ_[2] L]
  {P : Type u_2} [Group P] [TopologicalSpace P] (σ : L →ₐ[K] SeparableClosure K)
  (hmuK : ∃ ζ, IsPrimitiveRoot ζ 2) (hodd : Odd (Module.finrank ℚ_[2] L))
  (mK : TauCeti.absoluteGaloisGroupProP 2 K ≃ₜ* P) :
  ∃ e φ,
    (∀ (x : TauCeti.absoluteGaloisGroupProP 2 L),
        φ (e x) =
          mK ((TauCeti.maximalProPQuotient.map (TauCeti.absoluteGaloisGroupExtend K L σ) ⋯) x)) ∧
      IsOpen ↑φ.range ∧
        φ.range.index ∣ Module.finrank K L ∧
          (TauCeti.cyclotomicOrientation 2 K hmuK)
                (mK.symm
                  (φ
                    (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] L + 2)
                      {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] L + 2)
                          (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] L + 2))}
                      0))) =
              -1 ∧
            ↑((TauCeti.cyclotomicOrientation 2 K hmuK)
                      (mK.symm
                        (φ
                          (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] L + 2)
                            {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] L + 2)
                                (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] L + 2))}
                            2)))) *
                  (1 - 2 ^ 2) =
                1 ∧
              ∀ (i : ℕ),
                i ≠ 0 →
                  i ≠ 2 →
                    i < Module.finrank ℚ_[2] L + 2 →
                      (TauCeti.cyclotomicOrientation 2 K hmuK)
                          (mK.symm
                            (φ
                              (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] L + 2)
                                {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] L + 2)
                                    (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] L + 2))}
                                i))) =
                        1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../../../topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The Demushkin predicate](../../../topology/profinite-and-pro-p-groups/part-01/the-demushkin-predicate.md)
- [Demushkin's theorem](demushkins-theorem.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [Labute's criterion](../../../topology/profinite-and-pro-p-groups/part-01/labutes-criterion.md)
- [Labute's normal form for `q = 2` and odd rank (Labute, Theorem 3, case (2))](../../../topology/profinite-and-pro-p-groups/part-01/labutes-normal-form-for-q-2-and-odd-rank-labute.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../../topology/algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_finiteExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/DyadicFiniteExtension.html#TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_finiteExtension).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_finiteExtension`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/DyadicFiniteExtension.html#TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_finiteExtension)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_finiteExtension` in TauCeti/NumberTheory/LocalField/ProP/Marked/DyadicFiniteExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/ProP/Marked/DyadicFiniteExtension.lean#L67)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalGaloisGroups/STATUS.md)
