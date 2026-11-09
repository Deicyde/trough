---
declaration: theorem
origin: cited
lean: CategoryTheory.Functor.homologyEulerChar_cubeComplex, ChainComplex.eulerChar_eq_homologyEulerChar, CochainComplex.eulerChar_eq_homologyEulerChar, HomologicalComplex.eulerChar_forgetFG_eq_homologyEulerChar, ChainComplex.sum_range_finrank_X_eq_sum_range_finrank_homology
statement: formalized
proof: formalized
---

# Euler–Poincaré for cubes

Over a Noetherian ring with the rank-nullity property, such as
`ℤ` or a field, the Euler characteristic of the cohomology of the cube complex of a cube of finite
free modules is the sum of the ranks of the vertices `F(S)`, each with the sign `(-1) ^ #S`. Over
`ℤ` the rank of a cohomology group is the rank of its free part, so torsion does not
contribute.

```lean
CategoryTheory.Functor.homologyEulerChar_cubeComplex.{w, v, u} {ι : Type w} [Fintype ι]
  [LinearOrder ι] {R : Type u} [Ring R] (F : CategoryTheory.Functor (Finset ι) (ModuleCat R))
  [∀ (S : Finset ι), Module.Free R ↑(F.obj S)] [∀ (S : Finset ι), Module.Finite R ↑(F.obj S)]
  [IsNoetherianRing R] [HasRankNullity.{v, u} R] :
  HomologicalComplex.homologyEulerChar F.cubeComplex =
    ∑ S, ↑(↑S.card).negOnePow * ↑(Module.finrank R ↑(F.obj S))
```

## Depends on

- [CategoryTheory.Functor.cubeComplex](../../knot-theory/khovanov-homology-of-classical-links/categorytheory-functor-cubecomplex.md)

## Proof depends on

- [The Euler–Poincaré theorem in abelian `K₀`](../../category-theory/grothendieck-group/the-euler-poincare-theorem-in-abelian-k0.md)

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Functor.homologyEulerChar_cubeComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/EulerCharacteristic.html#CategoryTheory.Functor.homologyEulerChar_cubeComplex).

## Other forms

**Euler--Poincaré for a bounded chain complex of vector spaces.** Formalized in Tau Ceti as [`ChainComplex.eulerChar_eq_homologyEulerChar`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/ChainComplex.html#ChainComplex.eulerChar_eq_homologyEulerChar).

```lean
ChainComplex.eulerChar_eq_homologyEulerChar.{u, v} {k : Type u} [DivisionRing k]
  (K : ChainComplex (ModuleCat k) ℕ) [∀ (n : ℕ), Module.Finite k ↑(K.X n)]
  (hK : ∀ᶠ (n : ℕ) in Filter.atTop, CategoryTheory.Limits.IsZero (K.X n)) :
  HomologicalComplex.eulerChar K = HomologicalComplex.homologyEulerChar K
```

**Euler--Poincaré for a bounded cochain complex of finitely generated modules.** Formalized in Tau Ceti as [`CochainComplex.eulerChar_eq_homologyEulerChar`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/Finite.html#CochainComplex.eulerChar_eq_homologyEulerChar).

```lean
CochainComplex.eulerChar_eq_homologyEulerChar.{u, v} {R : Type u} [Ring R] [IsNoetherianRing R]
  [HasRankNullity.{v, u} R] (K : CochainComplex (ModuleCat R) ℤ)
  (hK : ∀ (n : ℤ), Module.Finite R ↑(K.X n)) (a b : ℤ) [K.IsStrictlyGE a] [K.IsStrictlyLE b] :
  HomologicalComplex.eulerChar K = HomologicalComplex.homologyEulerChar K
```

**Euler--Poincaré for a bounded cochain complex of finitely generated modules.** Formalized in Tau Ceti as [`HomologicalComplex.eulerChar_forgetFG_eq_homologyEulerChar`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/Finite.html#HomologicalComplex.eulerChar_forgetFG_eq_homologyEulerChar).

```lean
HomologicalComplex.eulerChar_forgetFG_eq_homologyEulerChar.{u, v} {R : Type u} [Ring R]
  [IsNoetherianRing R] (K : CochainComplex (FGModuleCat R) ℤ) [HasRankNullity.{v, u} R] (a b : ℤ)
  [K.IsStrictlyGE a] [K.IsStrictlyLE b] :
  (((CategoryTheory.forget₂ (FGModuleCat R) (ModuleCat R)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj
        K).eulerChar =
    (((CategoryTheory.forget₂ (FGModuleCat R) (ModuleCat R)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj
        K).homologyEulerChar
```

**Euler--Poincaré for a chain complex of vector spaces indexed by `ℕ`.** Formalized in Tau Ceti as [`ChainComplex.sum_range_finrank_X_eq_sum_range_finrank_homology`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/EulerCharacteristic/ChainComplex.html#ChainComplex.sum_range_finrank_X_eq_sum_range_finrank_homology).

```lean
ChainComplex.sum_range_finrank_X_eq_sum_range_finrank_homology.{u, v} {k : Type u} [DivisionRing k]
  (K : ChainComplex (ModuleCat k) ℕ) {n : ℕ} (hfinite : ∀ i ≤ n, Module.Finite k ↑(K.X i))
  (hn : K.d (n + 1) n = 0) :
  ∑ i ∈ Finset.range (n + 1), (-1) ^ i * ↑(Module.finrank k ↑(K.X i)) =
    ∑ i ∈ Finset.range (n + 1), (-1) ^ i * ↑(Module.finrank k ↑(HomologicalComplex.homology K i))
```

## Sources

- [Tau Ceti documentation: `CategoryTheory.Functor.homologyEulerChar_cubeComplex`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Cube/EulerCharacteristic.html#CategoryTheory.Functor.homologyEulerChar_cubeComplex)
- [Source of `CategoryTheory.Functor.homologyEulerChar_cubeComplex` in TauCeti/Algebra/Homology/Cube/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Homology/Cube/EulerCharacteristic.lean#L157)
