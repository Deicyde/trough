---
declaration: structure
origin: cited
lean: TauCeti.HasZerosInRects
statement: formalized
---

# TauCeti.HasZerosInRects

The certified rectangles `Bs`, with multiplicities `ms`, account for all zeros of `f` in the
closed rectangle `Rectangle z w`. Each rectangle is given by a pair of opposite corners. The
conditions are: `f` is meromorphic on `U ⊇ Rectangle z w` without poles in the rectangle; each
`Bᵢ` lies in the rectangle and their interiors are pairwise disjoint; `f` has order `0` on the
frontier of the rectangle and of each `Bᵢ`; the zero count of `Bᵢ` is `mᵢ`; and the zero count of
the rectangle is the sum of the `mᵢ`.

```lean
TauCeti.HasZerosInRects.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] (f : ℂ → E)
  (U : Set ℂ) (z w : ℂ) (Bs : List (ℂ × ℂ)) (ms : List ℕ) : Prop
```

## Depends on

- [TauCeti.zeroCount](tauceti-zerocount.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasZerosInRects`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Counting/Certificate.html#TauCeti.HasZerosInRects).

## Sources

- [Tau Ceti documentation: `TauCeti.HasZerosInRects`](https://taucetiproject.org/docs/TauCeti/Analysis/Meromorphic/Counting/Certificate.html#TauCeti.HasZerosInRects)
- [Source of `TauCeti.HasZerosInRects` in TauCeti/Analysis/Meromorphic/Counting/Certificate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Meromorphic/Counting/Certificate.lean#L49)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
