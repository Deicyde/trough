---
declaration: theorem
origin: cited
lean: TauCeti.ResidueModule.isOrthonormalBasis_iff
statement: formalized
proof: formalized
---

# Serre's theorem (`TauCeti.ResidueModule.isOrthonormalBasis_iff`)

For norms with values in `‖ϖ‖ ^ ℤ ∪ {0}`, a family of the closed unit
ball is an orthonormal basis exactly when its residues are a basis of the residue module: they are
linearly independent over the residue ring and span.

```lean
TauCeti.ResidueModule.isOrthonormalBasis_iff.{u_1, u_2, u_3} {R : Type u_1} {M : Type u_2}
  {I : Type u_3} [SeminormedCommRing R] [IsUltrametricDist R] [NormOneClass R]
  [SeminormedAddCommGroup M] [IsUltrametricDist M] [_root_.Module R M] [IsBoundedSMul R M]
  (ϖ : TauCeti.NormedRing.PseudoUniformizer R)
  (hR : ∀ (a : R), TauCeti.zpowCeil ‖↑ϖ.unit‖ ‖a‖ = ‖a‖)
  (hM : ∀ (m : M), TauCeti.zpowCeil ‖↑ϖ.unit‖ ‖m‖ = ‖m‖)
  {e : I → ↥(TauCeti.unitClosedBallSubmodule R M)} :
  (TauCeti.IsOrthonormalBasis R fun i => ↑(e i)) ↔
    LinearIndependent (↥(Subring.unitClosedBall R) ⧸ TauCeti.unitBallIdeal R)
        (⇑TauCeti.ResidueModule.mk ∘ e) ∧
      Submodule.span (↥(Subring.unitClosedBall R) ⧸ TauCeti.unitBallIdeal R)
          (Set.range (⇑TauCeti.ResidueModule.mk ∘ e)) =
        ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ResidueModule.isOrthonormalBasis_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/ResidueBasis.html#TauCeti.ResidueModule.isOrthonormalBasis_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.ResidueModule.isOrthonormalBasis_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/ResidueBasis.html#TauCeti.ResidueModule.isOrthonormalBasis_iff)
- [Source of `TauCeti.ResidueModule.isOrthonormalBasis_iff` in TauCeti/Analysis/Normed/Module/Bases/ResidueBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Bases/ResidueBasis.lean#L297)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
