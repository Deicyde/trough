---
declaration: theorem
origin: cited
lean: TauCeti.OddComponentGridDiagram.alexanderHomologyEulerChar_eq_alexanderEulerChar
statement: formalized
proof: formalized
---

# Euler--Poincaré in one Alexander degree

The alternating dimension of fully blocked grid
homology equals the alternating count of grid states.

```lean
TauCeti.OddComponentGridDiagram.alexanderHomologyEulerChar_eq_alexanderEulerChar {n : ℕ}
  (G : TauCeti.OddComponentGridDiagram n) (a : ℤ) :
  G.alexanderHomologyEulerChar a = G.alexanderEulerChar (ZMod 2) a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler–Poincaré for cubes](../khovanov-homology-of-classical-links/euler-poincare-for-cubes.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.OddComponentGridDiagram.alexanderHomologyEulerChar_eq_alexanderEulerChar`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.html#TauCeti.OddComponentGridDiagram.alexanderHomologyEulerChar_eq_alexanderEulerChar).

## Sources

- [Tau Ceti documentation: `TauCeti.OddComponentGridDiagram.alexanderHomologyEulerChar_eq_alexanderEulerChar`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.html#TauCeti.OddComponentGridDiagram.alexanderHomologyEulerChar_eq_alexanderEulerChar)
- [Source of `TauCeti.OddComponentGridDiagram.alexanderHomologyEulerChar_eq_alexanderEulerChar` in TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Grid/Homology/EulerCharacteristic.lean#L308)
