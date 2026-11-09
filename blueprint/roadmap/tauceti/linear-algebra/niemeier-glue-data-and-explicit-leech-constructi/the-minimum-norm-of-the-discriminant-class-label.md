---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.isLeast_form_self_typeADiscriminantGroupEquiv
statement: formalized
proof: formalized
---

# The minimum norm of the discriminant class labelled `a : ZMod (n + 1)`

The class
`typeADiscriminantGroupEquiv n a = a.val • ω₁` of `Aₙ` has minimum norm
`a.val (n + 1 - a.val) / (n + 1)`, the shortest norm of the Conway–Sloane glue label `[a]` of an
`Aₙ` component.

```lean
TauCeti.IntegralLattice.isLeast_form_self_typeADiscriminantGroupEquiv {n : ℕ} (a : ZMod (n + 1)) :
  IsLeast
    {q |
      ∃ x,
        Submodule.Quotient.mk x = (TauCeti.IntegralLattice.typeADiscriminantGroupEquiv n) a ∧
          ((TauCeti.IntegralLattice.typeARootLattice n).form ↑x) ↑x = q}
    (↑a.val * (↑n + 1 - ↑a.val) / (↑n + 1))
```

## Depends on

- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.isLeast_form_self_typeADiscriminantGroupEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeA/CosetMinimum.html#TauCeti.IntegralLattice.isLeast_form_self_typeADiscriminantGroupEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.isLeast_form_self_typeADiscriminantGroupEquiv`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeA/CosetMinimum.html#TauCeti.IntegralLattice.isLeast_form_self_typeADiscriminantGroupEquiv)
- [Source of `TauCeti.IntegralLattice.isLeast_form_self_typeADiscriminantGroupEquiv` in TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeA/CosetMinimum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/RootLattice/TypeA/CosetMinimum.lean#L174)
- [Tau Ceti roadmap status: Niemeier glue data and explicit Leech constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Rank24LatticeConstructions/STATUS.md)
