---
declaration: def
origin: cited
lean: TauCeti.DenseCompactification.projectiveClosure
statement: formalized
---

# The projective closure of an affine scheme of finite type

For an ideal `J` of
`R[Y₀, …, Yₙ₋₁]`, the projective scheme `Proj (R[X₀, …, Xₙ] ⧸ Jʰ)`, where `Jʰ` is the
homogenization of `J` with respect to `X₀`, together with the embedding of
`Spec (R[Y₀, …, Yₙ₋₁] ⧸ J)` as its standard chart `D₊(X₀)`, is a dense compactification of
`Spec (R[Y₀, …, Yₙ₋₁] ⧸ J) ⟶ Spec R`.

```lean
TauCeti.DenseCompactification.projectiveClosure.{u} {R : Type u} [CommRing R] {n : ℕ}
  (J : Ideal (MvPolynomial (Fin n) R)) :
  TauCeti.DenseCompactification
    (AlgebraicGeometry.Spec.map (CommRingCat.ofHom (algebraMap R (MvPolynomial (Fin n) R ⧸ J))))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DenseCompactification.projectiveClosure`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.html#TauCeti.DenseCompactification.projectiveClosure).

## Sources

- [Tau Ceti documentation: `TauCeti.DenseCompactification.projectiveClosure`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.html#TauCeti.DenseCompactification.projectiveClosure)
- [Source of `TauCeti.DenseCompactification.projectiveClosure` in TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Compactification/ProjectiveClosure.lean#L63)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
