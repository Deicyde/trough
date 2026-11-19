---
declaration: theorem
origin: cited
lean: TauCeti.PDCode.eulerChar_toPermutationTriple
statement: formalized
proof: formalized
---

# Euler's formula for a PD-code

The underlying graph has `n` vertices and `2 * n` edges,
so its Euler characteristic is the number of faces less the number of crossings.

```lean
TauCeti.PDCode.eulerChar_toPermutationTriple {n : ℕ} (D : TauCeti.PDCode n) :
  D.toPermutationTriple.eulerChar = ↑D.faceCount - ↑n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.eulerChar_toPermutationTriple`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/Planar.html#TauCeti.PDCode.eulerChar_toPermutationTriple).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.eulerChar_toPermutationTriple`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/Planar.html#TauCeti.PDCode.eulerChar_toPermutationTriple)
- [Source of `TauCeti.PDCode.eulerChar_toPermutationTriple` in TauCeti/KnotTheory/PDCode/Planar.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/PDCode/Planar.lean#L323)
