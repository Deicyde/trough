---
declaration: theorem
origin: cited
lean: HomologicalComplex.isIso_homologyKunneth_of_isSplitMono_of_isSplitEpi, HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat, HomologicalComplex.isIso_homologyKunneth_of_projective, HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat_right, HomologicalComplex.isIso_homologyKunneth_of_projective_right
statement: formalized
proof: formalized
---

# The Künneth theorem for split complexes

for complexes `K` and `L` of modules over a
commutative ring `R` whose cycles split off their terms and whose homology splits off their cycles,
the Künneth map `⨁_{p + q = n} Hₚ(K) ⊗ H_q(L) ⟶ Hₙ(K ⊗ L)` is an isomorphism.  This applies to
complexes of semisimple modules, for instance of vector spaces over a field
(`HomologicalComplex.isSplitMono_iCycles_of_isSemisimpleModule`), and to complexes whose cycles
split off and whose homology is projective
(`HomologicalComplex.isSplitEpi_homologyπ_of_projective`).

```lean
HomologicalComplex.isIso_homologyKunneth_of_isSplitMono_of_isSplitEpi.{u, u_3} {R : Type u}
  [CommRing R] {I : Type u_3} [Small.{u, u_3} I] [AddMonoid I] {c : ComplexShape I} [c.TensorSigns]
  [DecidableEq I] (K L : HomologicalComplex (ModuleCat R) c) (n : I)
  [∀ (i : I), CategoryTheory.IsSplitMono (K.iCycles i)]
  [∀ (i : I), CategoryTheory.IsSplitEpi (K.homologyπ i)]
  [∀ (i : I), CategoryTheory.IsSplitMono (L.iCycles i)]
  [∀ (i : I), CategoryTheory.IsSplitEpi (L.homologyπ i)] :
  CategoryTheory.IsIso (K.homologyKunneth L n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomologicalComplex.isIso_homologyKunneth_of_isSplitMono_of_isSplitEpi`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.html#HomologicalComplex.isIso_homologyKunneth_of_isSplitMono_of_isSplitEpi).

## Other forms

**The Künneth theorem when one factor has zero differentials and flat terms.** Formalized in Tau Ceti as [`HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.html#HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat).

```lean
HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat.{u} {R : Type u} [CommRing R]
  (K L : ChainComplex (ModuleCat R) ℕ) [∀ (p : ℕ), Module.Flat R ↑(K.X p)]
  (hK : ∀ (i j : ℕ), K.d i j = 0) (n : ℕ) :
  CategoryTheory.IsIso (HomologicalComplex.homologyKunneth K L n)
```

**The Künneth theorem when one factor is projective with projective homology.** Formalized in Tau Ceti as [`HomologicalComplex.isIso_homologyKunneth_of_projective`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Projective.html#HomologicalComplex.isIso_homologyKunneth_of_projective).

```lean
HomologicalComplex.isIso_homologyKunneth_of_projective.{u} {R : Type u} [CommRing R]
  (K L : ChainComplex (ModuleCat R) ℕ) [∀ (p : ℕ), Module.Projective R ↑(K.X p)]
  [∀ (p : ℕ), Module.Projective R ↑(HomologicalComplex.homology K p)] (n : ℕ) :
  CategoryTheory.IsIso (HomologicalComplex.homologyKunneth K L n)
```

**The Künneth theorem when the second factor has zero differentials and flat terms.** Formalized in Tau Ceti as [`HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat_right`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Braiding.html#HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat_right).

```lean
HomologicalComplex.isIso_homologyKunneth_of_d_eq_zero_of_flat_right.{u} {R : Type u} [CommRing R]
  (K L : ChainComplex (ModuleCat R) ℕ) [∀ (q : ℕ), Module.Flat R ↑(L.X q)]
  (hL : ∀ (i j : ℕ), L.d i j = 0) (n : ℕ) :
  CategoryTheory.IsIso (HomologicalComplex.homologyKunneth K L n)
```

**The Künneth theorem when the second factor is projective with projective homology.** Formalized in Tau Ceti as [`HomologicalComplex.isIso_homologyKunneth_of_projective_right`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Projective.html#HomologicalComplex.isIso_homologyKunneth_of_projective_right).

```lean
HomologicalComplex.isIso_homologyKunneth_of_projective_right.{u} {R : Type u} [CommRing R]
  (K L : ChainComplex (ModuleCat R) ℕ) [∀ (p : ℕ), Module.Projective R ↑(K.X p)]
  [∀ (p : ℕ), Module.Projective R ↑(HomologicalComplex.homology K p)] (n : ℕ) :
  CategoryTheory.IsIso (HomologicalComplex.homologyKunneth L K n)
```

## Sources

- [Tau Ceti documentation: `HomologicalComplex.isIso_homologyKunneth_of_isSplitMono_of_isSplitEpi`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.html#HomologicalComplex.isIso_homologyKunneth_of_isSplitMono_of_isSplitEpi)
- [Source of `HomologicalComplex.isIso_homologyKunneth_of_isSplitMono_of_isSplitEpi` in TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Homology/Monoidal/Homology/Kunneth/Basic.lean#L269)
