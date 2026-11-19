---
declaration: theorem
origin: cited
lean: TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_eq_smul_T_mul_det_weightMatrix
statement: formalized
proof: formalized
---

# The graded Euler characteristic of fully blocked grid homology is the normalized grid determinant

```lean
TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_eq_smul_T_mul_det_weightMatrix {n : ℕ}
  (G : TauCeti.OddComponentGridDiagram n) :
  G.gradedHomologyEulerChar =
    (Equiv.Perm.sign (↑G).O.toPerm * (↑n + 1).negOnePow) •
      (LaurentPolynomial.T (↑G).alexanderTwoShift * (↑G).weightMatrix.det)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler--Poincaré in one Alexander degree](euler-poincare-in-one-alexander-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_eq_smul_T_mul_det_weightMatrix`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.html#TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_eq_smul_T_mul_det_weightMatrix).

## Sources

- [Tau Ceti documentation: `TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_eq_smul_T_mul_det_weightMatrix`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.html#TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_eq_smul_T_mul_det_weightMatrix)
- [Source of `TauCeti.OddComponentGridDiagram.gradedHomologyEulerChar_eq_smul_T_mul_det_weightMatrix` in TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.lean#L352)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
