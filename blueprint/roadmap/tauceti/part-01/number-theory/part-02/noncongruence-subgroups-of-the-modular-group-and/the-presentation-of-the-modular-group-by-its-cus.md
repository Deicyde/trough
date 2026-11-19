---
declaration: def
origin: cited
lean: TauCeti.ModularGroup.modularEquiv
statement: formalized
---

# The presentation of the modular group by its cusp generator

`PSL(2, ℤ)` is the triangle
group `Δ(3, 2, ∞)` with `x`, `y`, `z` sent to `U = S T⁻¹`, `S` and `T`, the elements of orders `3`,
`2` and `∞` that the permutation action on the cosets of a finite-index subgroup turns into a
permutation triple. It is `TauCeti.ModularGroup.triangleGroupEquiv` precomposed with the mirror
automorphism `TauCeti.TriangleGroup.mirror`.

```lean
TauCeti.ModularGroup.modularEquiv :
  TauCeti.TriangleGroup 3 2 0 ≃* Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℤ
```

## Depends on

- [TauCeti.ModularGroup.U](tauceti-modulargroup-u.md)

## Proof depends on

- [The angle condition of Poincaré's theorem](../../../analysis/part-03/complex/part-01/the-angle-condition-of-poincares-theorem.md)
- [The cusp condition of Poincaré's theorem](../../../analysis/part-03/complex/part-01/the-cusp-condition-of-poincares-theorem.md)
- [The Gauss–Bonnet formula](../../../analysis/part-03/complex/part-02/the-gauss-bonnet-formula.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Poincaré's presentation theorem](../../../analysis/part-03/complex/part-03/poincares-presentation-theorem.md)
- [TauCeti.ModularGroup.R](tauceti-modulargroup-r.md)
- [TauCeti.TriangleGroup.mirror](tauceti-trianglegroup-mirror.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularGroup.modularEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/TriangleGroup.html#TauCeti.ModularGroup.modularEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularGroup.modularEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/TriangleGroup.html#TauCeti.ModularGroup.modularEquiv)
- [Source of `TauCeti.ModularGroup.modularEquiv` in TauCeti/Analysis/Complex/Fuchsian/LevelOne/TriangleGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Fuchsian/LevelOne/TriangleGroup.lean#L344)
- [Tau Ceti roadmap status: Noncongruence subgroups of the modular group and their modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NoncongruenceModularForms/STATUS.md)
