---
declaration: theorem
origin: cited
lean: TauCeti.exists_equiv_iso_of_biproduct_iso, TauCeti.exists_equiv_iso_of_iso_biproduct
statement: formalized
proof: formalized
---

# The Krull-Schmidt theorem with no ambient object

an isomorphism between two finite
biproducts of indecomposable objects of finite length matches their summands by a bijection of the
index sets.

```lean
TauCeti.exists_equiv_iso_of_biproduct_iso.{u, v} {A : Type u} [Ring A] {ι κ : Type} [Finite ι]
  [Finite κ] {P : ι → ModuleCat A} {Q : κ → ModuleCat A} [IsNoetherian A ↑(⨁ P)]
  [IsArtinian A ↑(⨁ P)] (e : ⨁ P ≅ ⨁ Q) (hP : ∀ (i : ι), CategoryTheory.Indecomposable (P i))
  (hQ : ∀ (j : κ), CategoryTheory.Indecomposable (Q j)) : ∃ f, ∀ (i : ι), Nonempty (P i ≅ Q (f i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Krull-Schmidt theorem](../../ring-theory/krull-schmidt/the-krull-schmidt-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_equiv_iso_of_biproduct_iso`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/KrullSchmidt.html#TauCeti.exists_equiv_iso_of_biproduct_iso).

## Other forms

**The Krull-Schmidt theorem for biproducts in `ModuleCat A`.** Formalized in Tau Ceti as [`TauCeti.exists_equiv_iso_of_iso_biproduct`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/KrullSchmidt.html#TauCeti.exists_equiv_iso_of_iso_biproduct).

```lean
TauCeti.exists_equiv_iso_of_iso_biproduct.{u, v} {A : Type u} [Ring A] {ι κ : Type} [Finite ι]
  [Finite κ] {P : ι → ModuleCat A} {Q : κ → ModuleCat A} {X : ModuleCat A} [IsNoetherian A ↑X]
  [IsArtinian A ↑X] (eP : X ≅ ⨁ P) (eQ : X ≅ ⨁ Q)
  (hP : ∀ (i : ι), CategoryTheory.Indecomposable (P i))
  (hQ : ∀ (j : κ), CategoryTheory.Indecomposable (Q j)) : ∃ e, ∀ (i : ι), Nonempty (P i ≅ Q (e i))
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_equiv_iso_of_biproduct_iso`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/KrullSchmidt.html#TauCeti.exists_equiv_iso_of_biproduct_iso)
- [Source of `TauCeti.exists_equiv_iso_of_biproduct_iso` in TauCeti/Algebra/Category/ModuleCat/KrullSchmidt.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/KrullSchmidt.lean#L111)
