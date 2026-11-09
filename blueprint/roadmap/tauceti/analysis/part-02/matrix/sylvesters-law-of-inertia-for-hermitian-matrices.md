---
declaration: theorem
origin: cited
lean: Matrix.IsHermitian.signature_congr
statement: formalized
proof: formalized
---

# Sylvester's law of inertia for Hermitian matrices

The signature is unchanged by
`*`-congruence `A ↦ P * A * Pᴴ` with `P` invertible.

```lean
Matrix.IsHermitian.signature_congr.{u_1, u_3} {ι : Type u_1} [Fintype ι] {𝕜 : Type u_3} [RCLike 𝕜]
  {A : Matrix ι ι 𝕜} [DecidableEq ι] {P : Matrix ι ι 𝕜} (hP : IsUnit P.det) (hA : A.IsHermitian) :
  ⋯.signature = hA.signature
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.IsHermitian.signature_congr`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HermitianSignature/Basic.html#Matrix.IsHermitian.signature_congr).

## Sources

- [Tau Ceti documentation: `Matrix.IsHermitian.signature_congr`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/HermitianSignature/Basic.html#Matrix.IsHermitian.signature_congr)
- [Source of `Matrix.IsHermitian.signature_congr` in TauCeti/Analysis/Matrix/HermitianSignature/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/HermitianSignature/Basic.lean#L145)
