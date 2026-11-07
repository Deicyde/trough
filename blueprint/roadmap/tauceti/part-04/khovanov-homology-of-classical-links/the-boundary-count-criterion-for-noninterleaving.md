---
declaration: theorem
origin: cited
lean: Function.Involutive.orbitCount_finRotate_mul_add_orbitCount_eq_iff
statement: formalized
proof: formalized
---

# The boundary-count criterion for noninterleaving

A chord diagram on a nonempty boundary
circle, with matching an involution `σ` and `m = n - orbitCount σ` bands, has exactly `m + 1`
boundary cycles if and only if no two of its bands interleave.

```lean
Function.Involutive.orbitCount_finRotate_mul_add_orbitCount_eq_iff {n : ℕ} [NeZero n]
  {σ : Equiv.Perm (Fin n)} (hinv : Function.Involutive ⇑σ) :
  TauCeti.orbitCount (finRotate n * σ) + TauCeti.orbitCount σ = n + 1 ↔ σ.IsNoncrossingMatching
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Function.Involutive.orbitCount_finRotate_mul_add_orbitCount_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/ChordDiagram.html#Function.Involutive.orbitCount_finRotate_mul_add_orbitCount_eq_iff).

## Sources

- [Tau Ceti documentation: `Function.Involutive.orbitCount_finRotate_mul_add_orbitCount_eq_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/ChordDiagram.html#Function.Involutive.orbitCount_finRotate_mul_add_orbitCount_eq_iff)
- [Source of `Function.Involutive.orbitCount_finRotate_mul_add_orbitCount_eq_iff` in TauCeti/Combinatorics/ChordDiagram.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/ChordDiagram.lean#L379)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/KhovanovHomology/STATUS.md)
