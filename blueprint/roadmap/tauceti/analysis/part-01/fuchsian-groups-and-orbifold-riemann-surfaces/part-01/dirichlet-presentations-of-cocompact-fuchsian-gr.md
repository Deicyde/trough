---
declaration: theorem
origin: cited
lean: Subgroup.exists_sidePairing_relatorQuotientTo_bijective_of_compactSpace
statement: formalized
proof: formalized
---

# Dirichlet presentations of cocompact Fuchsian groups

Let `Γ ≤ PSL(2, ℝ)` be discrete
with compact orbit space, and let `p ∈ ℍ` have trivial stabilizer. The Dirichlet domain of `Γ`
centred at `p` is a compact convex polygon `P` with a side pairing by elements of `Γ`, and `Γ` is
presented by the side-pairing maps, subject to the side relations and the vertex-cycle
relations.

```lean
Subgroup.exists_sidePairing_relatorQuotientTo_bijective_of_compactSpace
  (Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)) [DiscreteTopology ↥Γ]
  [CompactSpace (MulAction.orbitRel.Quotient (↥Γ) UpperHalfPlane)] {p : UpperHalfPlane}
  (hp : p ∈ TauCeti.freeLocus (↥Γ) UpperHalfPlane) :
  ∃ n,
    ∃ (x : NeZero n),
      ∃ P σ,
        ∃ (hmap : ∀ (i : Fin n), σ.map i ∈ Γ),
          P.carrier = TauCeti.dirichletDomain (↥Γ) p ∧
            Function.Bijective ⇑(σ.relatorQuotientTo hmap)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gauss–Bonnet formula](../../../part-02/complex/part-01/the-gauss-bonnet-formula.md)
- [Poincaré's presentation theorem](poincares-presentation-theorem.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.exists_sidePairing_relatorQuotientTo_bijective_of_compactSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/SidePairing.html#Subgroup.exists_sidePairing_relatorQuotientTo_bijective_of_compactSpace).

## Sources

- [Tau Ceti documentation: `Subgroup.exists_sidePairing_relatorQuotientTo_bijective_of_compactSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/SidePairing.html#Subgroup.exists_sidePairing_relatorQuotientTo_bijective_of_compactSpace)
- [Source of `Subgroup.exists_sidePairing_relatorQuotientTo_bijective_of_compactSpace` in TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/SidePairing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/DirichletDomain/SidePairing.lean#L206)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
