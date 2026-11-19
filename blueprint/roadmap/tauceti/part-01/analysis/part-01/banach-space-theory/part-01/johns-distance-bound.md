---
declaration: theorem
origin: cited
lean: TauCeti.banachMazurDist_le_sqrt_finrank
statement: formalized
proof: formalized
---

# John's distance bound

A finite-dimensional normed space `F` is at Banach–Mazur distance at
most `√n` from any inner product space `E` of the same dimension `n`.

```lean
TauCeti.banachMazurDist_le_sqrt_finrank.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [FiniteDimensional 𝕜 E] [FiniteDimensional 𝕜 F] (h : Module.finrank 𝕜 E = Module.finrank 𝕜 F) :
  TauCeti.banachMazurDist 𝕜 E F ≤ √↑(Module.finrank 𝕜 E)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [John's theorem](johns-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.banachMazurDist_le_sqrt_finrank`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.html#TauCeti.banachMazurDist_le_sqrt_finrank).

## Sources

- [Tau Ceti documentation: `TauCeti.banachMazurDist_le_sqrt_finrank`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.html#TauCeti.banachMazurDist_le_sqrt_finrank)
- [Source of `TauCeti.banachMazurDist_le_sqrt_finrank` in TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/JohnEllipsoid.lean#L472)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
