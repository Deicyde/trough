---
declaration: theorem
origin: cited
lean: CliffordAlgebra.bivectorExterior_hodgeStar
statement: formalized
proof: formalized
---

# The self-duality relation

the Clifford action of the Hodge dual of a two-form is the
chirality element times the action of the two-form, `c₂(⋆α) = Γ c₂(α)`.

```lean
CliffordAlgebra.bivectorExterior_hodgeStar.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] {Q : QuadraticForm ℝ V} [Fact (Module.finrank ℝ V = 4)]
  (o : Orientation ℝ V (Fin 4)) (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) (hkl : 2 + 2 = Module.finrank ℝ V)
  (x : ↥(⋀[ℝ]^2 V)) :
  (CliffordAlgebra.bivectorExterior Q) ((o.hodgeStar hkl) x) =
    CliffordAlgebra.chirality Q o * (CliffordAlgebra.bivectorExterior Q) x
```

## Depends on

- [Orientation.hodgeStar](orientation-hodgestar.md)

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.bivectorExterior_hodgeStar`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.html#CliffordAlgebra.bivectorExterior_hodgeStar).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.bivectorExterior_hodgeStar`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.html#CliffordAlgebra.bivectorExterior_hodgeStar)
- [Source of `CliffordAlgebra.bivectorExterior_hodgeStar` in TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.lean#L281)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
