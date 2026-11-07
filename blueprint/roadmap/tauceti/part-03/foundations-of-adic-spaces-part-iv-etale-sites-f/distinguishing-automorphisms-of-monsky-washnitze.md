---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.washnitzerAlgebra.exists_triangularEquiv_isDistinguished_isUnit
statement: formalized
proof: formalized
---

# Distinguishing automorphisms of Monsky–Washnitzer algebras

Over a complete
nonarchimedean field `K`, every nonzero overconvergent series `f` in the variables `Option σ`,
for finite `σ`, is carried by a triangular automorphism `Y ↦ Y`, `Xᵢ ↦ Xᵢ + Y ^ α i` of
`K⟨X, Y⟩†` to a series which, as a restricted series in the variable `Y = none` over the Tate
algebra in the variables `σ`, is distinguished of some degree `s` at radius `1` with a unit
coefficient in degree `s`.

```lean
TauCeti.Dagger.washnitzerAlgebra.exists_triangularEquiv_isDistinguished_isUnit.{u_1, u_3}
  {σ : Type u_1} {K : Type u_3} [NormedField K] [IsUltrametricDist K] [CompleteSpace K] [Finite σ]
  (f : ↥(TauCeti.Dagger.washnitzerAlgebra (Option σ) K)) (hf : f ≠ 0) :
  ∃ α,
    ∃ (hα : ∀ (i : σ), α i ≠ 0),
      ∃ s,
        TauCeti.PowerSeries.IsDistinguished 1 s
            ↑(MvPowerSeries.restrictedOptionEquiv
                ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K)
                  ((TauCeti.Dagger.washnitzerAlgebra.triangularEquiv α hα) f))) ∧
          IsUnit
            ((PowerSeries.coeff s)
              ↑(MvPowerSeries.restrictedOptionEquiv
                  ((TauCeti.Dagger.washnitzerAlgebra.toTate (Option σ) K)
                    ((TauCeti.Dagger.washnitzerAlgebra.triangularEquiv α hα) f))))
```

## Depends on

- [Isomorphisms of Monsky–Washnitzer algebras from inverse substitutions](isomorphisms-of-monsky-washnitzer-algebras-from.md)
- [TauCeti.Dagger.washnitzerAlgebra](tauceti-dagger-washnitzeralgebra.md)
- [TauCeti.Dagger.washnitzerAlgebra.toTate](tauceti-dagger-washnitzeralgebra-totate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.washnitzerAlgebra.exists_triangularEquiv_isDistinguished_isUnit`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Distinguished.html#TauCeti.Dagger.washnitzerAlgebra.exists_triangularEquiv_isDistinguished_isUnit).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.washnitzerAlgebra.exists_triangularEquiv_isDistinguished_isUnit`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/Distinguished.html#TauCeti.Dagger.washnitzerAlgebra.exists_triangularEquiv_isDistinguished_isUnit)
- [Source of `TauCeti.Dagger.washnitzerAlgebra.exists_triangularEquiv_isDistinguished_isUnit` in TauCeti/RingTheory/Dagger/Distinguished.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Dagger/Distinguished.lean#L140)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
