---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuasiLocal.AlgebraNet, ProbabilisticTheory.QuasiLocal.AlgebraNet.Quasilocal, ProbabilisticTheory.QuasiLocal.AlgebraNet.of, ProbabilisticTheory.QuasiLocal.AlgebraNet.of_incl, ProbabilisticTheory.QuasiLocal.AlgebraNet.exists_of, ProbabilisticTheory.QuasiLocal.AlgebraNet.moveHom, ProbabilisticTheory.QuasiLocal.AlgebraNet.moveHom_of
statement: formalized
proof: formalized
---

# Nets of algebras over the finite regions of a lattice and their quasi-local algebra

The module `PhyslibAlpha.ProbabilisticTheory.QuasiLocal.AlgebraNet`, [PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean): 8 declarations (1 instance with no name), 6 with a docstring.

> A net of `*`-algebras over the finite regions of a set of sites has a quasi-local algebra: the
> direct limit of the local algebras.

## i. Overview

> The observables of an infinite system are those of finite regions, extended by the identity. A
> *net of algebras* assigns to each finite region `X` of a set of sites a unital `*`-algebra `A X`,
> and to each pair of regions `X ≤ Y` a unital `*`-homomorphism `A X → A Y`, with the identity
> for `X = Y` and composition respected. The finite regions are directed under inclusion: any two
> regions lie in a third. The *quasi-local algebra* is the direct limit: its elements are the
> observables of some finite region, two of them being identified when they agree in a common larger
> region. It is a unital complex `*`-algebra, and each local algebra maps into it.
>
> Nothing about the nature of the local algebras enters: they may be commutative, giving a
> classical system, or matrix algebras, giving a quantum system, or anything in between. The
> constructions that follow, the states and thermodynamic limits, the symmetries and the dynamics,
> are made once for every net.

## ii. Key results

> - `AlgebraNet` : a net of unital `*`-algebras over the finite regions of a set of sites.
> - `AlgebraNet.Quasilocal` : the quasi-local algebra, as the direct limit.
> - `AlgebraNet.of` : the embedding of a local algebra as a unital `*`-homomorphism.
> - `AlgebraNet.of_incl` : the local algebras embed compatibly.
> - `AlgebraNet.exists_of` : every quasi-local observable is supported in a finite region.
> - `AlgebraNet.moveHom` : a map of the quasi-local algebra induced by region-moving local maps.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1,
>   Section 2.6.

## A. Nets of algebras

**`ProbabilisticTheory.QuasiLocal.AlgebraNet`**, a structure, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L64).

> A net of unital complex `*`-algebras over the finite regions of a set of sites: the algebra of
> each region, and the inclusion of the algebra of a region in that of a larger region.

```lean
structure AlgebraNet (S : Type*) where
  /-- The algebra of observables of a finite region. -/
  A : Finset S → Type*
  [ring : ∀ X, Ring (A X)]
  [algebra : ∀ X, Algebra ℂ (A X)]
  [starRing : ∀ X, StarRing (A X)]
  [starModule : ∀ X, StarModule ℂ (A X)]
  /-- The inclusion of the algebra of a region in the algebra of a larger region. -/
  incl : ∀ {X Y : Finset S}, X ≤ Y → A X →⋆ₐ[ℂ] A Y
  /-- The inclusion of a region in itself is the identity. -/
  incl_refl : ∀ (X : Finset S) (a : A X), incl (le_refl X) a = a
  /-- Inclusions compose. -/
  incl_trans : ∀ {X Y Z : Finset S} (h₁ : X ≤ Y) (h₂ : Y ≤ Z) (a : A X),
    incl (h₁.trans h₂) a = incl h₂ (incl h₁ a)
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L86).

```lean
instance : DirectedSystem N.A (fun X Y (h : X ≤ Y) => N.incl h)
```

## B. The quasi-local algebra

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.Quasilocal`**, an abbrev, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L96).

> **The quasi-local algebra** of a net: the direct limit of the algebras of the finite
> regions.

```lean
abbrev Quasilocal : Type _
```

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.of`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L104).

> The embedding of the algebra of a region in the quasi-local algebra, as a unital
> `*`-homomorphism.

```lean
noncomputable def of (X : Finset S) : N.A X →⋆ₐ[ℂ] N.Quasilocal
```

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.of_incl`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L110).

> The embeddings of the local algebras are compatible with the inclusions.

```lean
lemma of_incl {X Y : Finset S} (h : X ≤ Y) (a : N.A X) : N.of Y (N.incl h a) = N.of X a
```

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.exists_of`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L115).

> Every element of the quasi-local algebra is an observable of some finite region.

```lean
lemma exists_of (x : N.Quasilocal) : ∃ (X : Finset S) (a : N.A X), N.of X a = x
```

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.moveHom`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L121).

> A map of the quasi-local algebra induced by maps of the local algebras that move regions: a
> monotone map `ρ` of regions and, for each region `X`, a unital `*`-homomorphism of its algebra
> into that of `ρ X`, natural with respect to the inclusions.

```lean
noncomputable def moveHom (ρ : Finset S → Finset S) (hρ : Monotone ρ)
    (φ : ∀ X, N.A X →⋆ₐ[ℂ] N.A (ρ X))
    (hφ : ∀ {X Y : Finset S} (h : X ≤ Y) (a : N.A X), φ Y (N.incl h a) = N.incl (hρ h) (φ X a)) :
    N.Quasilocal →⋆ₐ[ℂ] N.Quasilocal
```

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.moveHom_of`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean#L136).

```lean
lemma moveHom_of (ρ : Finset S → Finset S) (hρ : Monotone ρ) (φ : ∀ X, N.A X →⋆ₐ[ℂ] N.A (ρ X))
    (hφ : ∀ {X Y : Finset S} (h : X ≤ Y) (a : N.A X), φ Y (N.incl h a) = N.incl (hρ h) (φ X a))
    (X : Finset S) (a : N.A X) : N.moveHom ρ hρ φ hφ (N.of X a) = N.of (ρ X) (φ X a)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/AlgebraNet.lean)
