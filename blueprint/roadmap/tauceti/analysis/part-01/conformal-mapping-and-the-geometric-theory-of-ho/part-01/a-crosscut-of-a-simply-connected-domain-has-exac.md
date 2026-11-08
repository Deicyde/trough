---
declaration: theorem
origin: cited
lean: Path.IsCrosscut.natCard_connectedComponents_sdiff_range_eq_two
statement: formalized
proof: formalized
---

# A crosscut of a simply connected domain has exactly two sides

If `γ` is a crosscut of a
simply connected open set `U ⊆ ℂ`, then `U \ range γ` has exactly two connected components.

```lean
Path.IsCrosscut.natCard_connectedComponents_sdiff_range_eq_two {x y : ℂ} {γ : Path x y} {U : Set ℂ}
  (hγ : γ.IsCrosscut U) (hUo : IsOpen U) (hUs : IsSimplyConnected U) :
  Nat.card (ConnectedComponents ↑(U \ Set.range ⇑γ)) = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Borsuk's separation theorem](borsuks-separation-theorem.md)
- [The converse of Cauchy's theorem](../../../../number-theory/part-01/bounded-laplace-and-ordered-dirichlet-boundary-c/the-converse-of-cauchys-theorem.md)
- [Generalized winding number (HW Def 2.1)](../../contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [The homology Cauchy theorem (roadmap `homologyCauchyTheorem`, Layer 3)](../../contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem-roadmap-homologycauc.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)

## Lean

Formalized in Tau Ceti as [`Path.IsCrosscut.natCard_connectedComponents_sdiff_range_eq_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PrimeEnd/Crosscut/TwoSides.html#Path.IsCrosscut.natCard_connectedComponents_sdiff_range_eq_two).

## Sources

- [Tau Ceti documentation: `Path.IsCrosscut.natCard_connectedComponents_sdiff_range_eq_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/PrimeEnd/Crosscut/TwoSides.html#Path.IsCrosscut.natCard_connectedComponents_sdiff_range_eq_two)
- [Source of `Path.IsCrosscut.natCard_connectedComponents_sdiff_range_eq_two` in TauCeti/Analysis/Complex/Conformal/PrimeEnd/Crosscut/TwoSides.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/PrimeEnd/Crosscut/TwoSides.lean#L135)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
