---
declaration: theorem
origin: cited
lean: IsSl2Triple.exists_mem_quotientPointsSubgroup_identityComponent_of_weightedDynkinDiagram_eq
statement: formalized
proof: formalized
---

# Conjugacy of dominant `sl₂` triples with equal weighted Dynkin diagrams

Over an
algebraically closed field `k` of characteristic zero, if `G = Spec H` is of finite type with
Killing Lie algebra `𝔤` and two `sl₂` triples `(h₁, e₁, f₁)` and `(h₂, e₂, f₂)` in `𝔤` have
neutral elements dominant with respect to the same root-system base `b` of a Cartan subalgebra `𝔥`
and equal weighted Dynkin diagrams, then some rational point `g` of the connected centralizer
`C_G(h₁)°` carries `(h₁, e₁, f₁)` to `(h₂, e₂, f₂)` under the adjoint action.

```lean
IsSl2Triple.exists_mem_quotientPointsSubgroup_identityComponent_of_weightedDynkinDiagram_eq.{u}
  {k : Type u} [Field k] [CharZero k] [IsAlgClosed k] {H : TauCeti.FiniteTypeCommHopfAlgCat k}
  [LieAlgebra.IsKilling k (Module.Dual k (TauCeti.Bialgebra.CotangentSpace k ↑H.obj))]
  {𝔥 : LieSubalgebra k (Module.Dual k (TauCeti.Bialgebra.CotangentSpace k ↑H.obj))}
  [𝔥.IsCartanSubalgebra] {b : (LieAlgebra.IsKilling.rootSystem 𝔥).Base}
  {h₁ h₂ : ↑b.dominantNeutralElements}
  {e₁ f₁ e₂ f₂ : Module.Dual k (TauCeti.Bialgebra.CotangentSpace k ↑H.obj)}
  (t₁ : IsSl2Triple (↑↑h₁) e₁ f₁) (t₂ : IsSl2Triple (↑↑h₂) e₂ f₂)
  (hdiag : b.weightedDynkinDiagram h₁ = b.weightedDynkinDiagram h₂) :
  ∃
    g ∈
      TauCeti.CommHopfAlgCat.quotientPointsSubgroup H.obj
        (TauCeti.centralizerHopfIdeal ↑H.obj ↑↑h₁).identityComponent ↧k,
    ((TauCeti.Comodule.basePointsRepresentation
              (Module.Dual k (TauCeti.Bialgebra.CotangentSpace k ↑H.obj)))
            g)
          ↑↑h₁ =
        ↑↑h₂ ∧
      ((TauCeti.Comodule.basePointsRepresentation
                (Module.Dual k (TauCeti.Bialgebra.CotangentSpace k ↑H.obj)))
              g)
            e₁ =
          e₂ ∧
        ((TauCeti.Comodule.basePointsRepresentation
                (Module.Dual k (TauCeti.Bialgebra.CotangentSpace k ↑H.obj)))
              g)
            f₁ =
          f₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartier's theorem](../algebraic-group/cartiers-theorem.md)
- [The global dimension of a regular local ring is its Krull dimension](../../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`IsSl2Triple.exists_mem_quotientPointsSubgroup_identityComponent_of_weightedDynkinDiagram_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/GradeTwoOrbit.html#IsSl2Triple.exists_mem_quotientPointsSubgroup_identityComponent_of_weightedDynkinDiagram_eq).

## Sources

- [Tau Ceti documentation: `IsSl2Triple.exists_mem_quotientPointsSubgroup_identityComponent_of_weightedDynkinDiagram_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/GradeTwoOrbit.html#IsSl2Triple.exists_mem_quotientPointsSubgroup_identityComponent_of_weightedDynkinDiagram_eq)
- [Source of `IsSl2Triple.exists_mem_quotientPointsSubgroup_identityComponent_of_weightedDynkinDiagram_eq` in TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/GradeTwoOrbit.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/GradeTwoOrbit.lean#L403)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
