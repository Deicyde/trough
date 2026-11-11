---
declaration: theorem
origin: cited
lean: TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_line_stabilizer
statement: formalized
proof: formalized
---

# Chevalley's theorem with the subgroup character

A closed subgroup with finitely
generated defining ideal is the stabilizer, over every commutative value algebra, of a line in
a finite-dimensional exterior-power representation. The line lies in the weight space of a
unique character of the subgroup, including when the subgroup is nonreduced.

```lean
TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_line_stabilizer.{u, v, w} {k : Type u}
  [Field k] {H : CommHopfAlgCat k} (I : TauCeti.HopfIdeal k ↑H) (hI : I.toIdeal.FG) :
  ∃ V n,
    Module.Finite k ↥V.toSubmodule ∧
      let this := Module.addCommMonoidToAddCommGroup k;
      ∃ L,
        Module.finrank k ↥L = 1 ∧
          (∃! χ, L ≤ I.weightSpace (↥(⋀[k]^n ↥V)) χ) ∧
            ∀ (A : CommAlgCat k) (g : ↑(TauCeti.HopfAlgebra.points A)),
              g ∈ TauCeti.CommHopfAlgCat.quotientPointsSubgroup H I A ↔
                Submodule.map (TauCeti.Comodule.endOfPoint (↥(⋀[k]^n ↥V)) g.ofConv)
                    (Submodule.baseChange (↑A) L) =
                  Submodule.baseChange (↑A) L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_line_stabilizer`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/ExteriorStabilizer/Character.html#TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_line_stabilizer).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_line_stabilizer`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/ExteriorStabilizer/Character.html#TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_line_stabilizer)
- [Source of `TauCeti.HopfIdeal.exists_finite_subcomodule_exteriorPower_line_stabilizer` in TauCeti/Algebra/AlgebraicGroup/Representation/ExteriorStabilizer/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Representation/ExteriorStabilizer/Character.lean#L97)
