---
declaration: theorem
origin: cited
lean: CliffordAlgebra.chirality_eq
statement: formalized
proof: formalized
---

# Frame independence of the chirality element

`Γ = -c(e₁) c(e₂) c(e₃) c(e₄)` for every
positively oriented orthonormal basis `e`.

```lean
CliffordAlgebra.chirality_eq.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  {Q : QuadraticForm ℝ V} [Fact (Module.finrank ℝ V = 4)] (o : Orientation ℝ V (Fin 4))
  (hQ : ∀ (v : V), Q v = -‖v‖ ^ 2) (b : OrthonormalBasis (Fin 4) ℝ V)
  (hb : b.toBasis.orientation = o) :
  CliffordAlgebra.chirality Q o =
    -((CliffordAlgebra.ι Q) (b 0) * (CliffordAlgebra.ι Q) (b 1) * (CliffordAlgebra.ι Q) (b 2) *
        (CliffordAlgebra.ι Q) (b 3))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CliffordAlgebra.chirality_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.html#CliffordAlgebra.chirality_eq).

## Sources

- [Tau Ceti documentation: `CliffordAlgebra.chirality_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.html#CliffordAlgebra.chirality_eq)
- [Source of `CliffordAlgebra.chirality_eq` in TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/CliffordAlgebra/Chirality.lean#L181)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
