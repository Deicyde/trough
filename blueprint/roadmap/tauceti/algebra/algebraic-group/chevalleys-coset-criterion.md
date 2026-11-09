---
declaration: theorem
origin: cited
lean: TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_coset_matrixCoefficient
statement: formalized
proof: formalized
---

# Chevalley's coset criterion

A closed subgroup with finitely generated defining ideal
admits a finite exterior-power representation and a unimodular vector whose matrix coefficients
detect its left cosets over every commutative value algebra, including nonreduced algebras.

```lean
TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_coset_matrixCoefficient.{u, v, x}
  {k : Type u} [Field k] {H : CommHopfAlgCat k} (I : TauCeti.HopfIdeal k ↑H) (hI : I.toIdeal.FG) :
  ∃ V n,
    Module.Finite k ↥V.toSubmodule ∧
      let this := Module.addCommMonoidToAddCommGroup k;
      ∃ m,
        Module.IsUnimodular k m ∧
          ∀ (A : CommAlgCat k) (g h : ↑(TauCeti.HopfAlgebra.points A)),
            ↑g = ↑h ↔
              ∃ c,
                ∀ (φ : Module.Dual k ↥(⋀[k]^n ↥V)),
                  h.ofConv (TauCeti.Comodule.matrixCoefficient φ m) =
                    ↑c * g.ofConv (TauCeti.Comodule.matrixCoefficient φ m)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chevalley's theorem with the subgroup character](chevalleys-theorem-with-the-subgroup-character.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_coset_matrixCoefficient`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/LineFibers.html#TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_coset_matrixCoefficient).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_coset_matrixCoefficient`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/LineFibers.html#TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_coset_matrixCoefficient)
- [Source of `TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_coset_matrixCoefficient` in TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/LineFibers.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/LineFibers.lean#L108)
