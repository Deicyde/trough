---
declaration: theorem
origin: cited
lean: TauCeti.QuiverRep.exists_equiv_iso_of_iso_biproduct, TauCeti.QuiverRep.exists_equiv_iso_of_biproduct_iso
statement: formalized
proof: formalized
---

# The Krull-Schmidt theorem for quiver representations

If a pointwise finite-dimensional
representation of a finite quiver is isomorphic to a finite biproduct of indecomposable
representations in two ways, the two families of summands are matched by a bijection of their index
sets under which corresponding summands are isomorphic.

`TauCeti.QuiverRep.exists_indecomposable_iso_biproduct` supplies such an isomorphism.

```lean
TauCeti.QuiverRep.exists_equiv_iso_of_iso_biproduct.{u, v, w, t} {k : Type u} {Q : Type v} [Field k]
  [Quiver Q] [Finite Q] {ι κ : Type} [Finite ι] [Finite κ] {P : ι → TauCeti.QuiverRep k Q}
  {R : κ → TauCeti.QuiverRep k Q} {M : TauCeti.QuiverRep k Q} (hM : TauCeti.IsFinDim k Q M)
  (eP : M ≅ ⨁ P) (eR : M ≅ ⨁ R) (hP : ∀ (i : ι), CategoryTheory.Indecomposable (P i))
  (hR : ∀ (j : κ), CategoryTheory.Indecomposable (R j)) : ∃ e, ∀ (i : ι), Nonempty (P i ≅ R (e i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Krull-Schmidt theorem with no ambient object](../../algebra/part-01/category/the-krull-schmidt-theorem-with-no-ambient-object.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.QuiverRep.exists_equiv_iso_of_iso_biproduct`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Representation/KrullSchmidt.html#TauCeti.QuiverRep.exists_equiv_iso_of_iso_biproduct).

## Other forms

**The Krull-Schmidt theorem with no ambient representation.** Formalized in Tau Ceti as [`TauCeti.QuiverRep.exists_equiv_iso_of_biproduct_iso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Representation/KrullSchmidt.html#TauCeti.QuiverRep.exists_equiv_iso_of_biproduct_iso).

```lean
TauCeti.QuiverRep.exists_equiv_iso_of_biproduct_iso.{u, v, w, t} {k : Type u} {Q : Type v} [Field k]
  [Quiver Q] [Finite Q] {ι κ : Type} [Finite ι] [Finite κ] {P : ι → TauCeti.QuiverRep k Q}
  {R : κ → TauCeti.QuiverRep k Q} (h : TauCeti.IsFinDim k Q (⨁ P)) (e : ⨁ P ≅ ⨁ R)
  (hP : ∀ (i : ι), CategoryTheory.Indecomposable (P i))
  (hR : ∀ (j : κ), CategoryTheory.Indecomposable (R j)) : ∃ f, ∀ (i : ι), Nonempty (P i ≅ R (f i))
```

## Sources

- [Tau Ceti documentation: `TauCeti.QuiverRep.exists_equiv_iso_of_iso_biproduct`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Representation/KrullSchmidt.html#TauCeti.QuiverRep.exists_equiv_iso_of_iso_biproduct)
- [Source of `TauCeti.QuiverRep.exists_equiv_iso_of_iso_biproduct` in TauCeti/RepresentationTheory/Quiver/Representation/KrullSchmidt.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Representation/KrullSchmidt.lean#L107)
