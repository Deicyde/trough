---
declaration: theorem
origin: cited
lean: TauCeti.GTree.IsEllipticSubgroup.of_fg, TauCeti.GTree.isEllipticSubgroup_closure, TauCeti.GTree.isHyperbolic_mul_of_disjoint
statement: formalized
proof: formalized
---

# Serre's lemma (`TauCeti.GTree.IsEllipticSubgroup.of_fg`)

A finitely generated subgroup all of whose elements are elliptic fixes a
vertex.

```lean
TauCeti.GTree.IsEllipticSubgroup.of_fg.{u, v, w} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {H : Subgroup G} (hH : H.FG) (h : ∀ g ∈ H, T.IsElliptic g) : T.IsEllipticSubgroup H
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Helly's theorem for subtrees](../../combinatorics/graph/hellys-theorem-for-subtrees.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GTree.IsEllipticSubgroup.of_fg`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.IsEllipticSubgroup.of_fg).

## Other forms

**Serre's lemma.** Formalized in Tau Ceti as [`TauCeti.GTree.isEllipticSubgroup_closure`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isEllipticSubgroup_closure).

```lean
TauCeti.GTree.isEllipticSubgroup_closure.{u, v, w} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {S : Set G} (hS : S.Finite) (h₁ : ∀ s ∈ S, T.IsElliptic s)
  (h₂ : S.Pairwise fun s t => T.IsElliptic (s * t)) : T.IsEllipticSubgroup (Subgroup.closure S)
```

**Serre's lemma on pairs of elliptic elements.** Formalized in Tau Ceti as [`TauCeti.GTree.isHyperbolic_mul_of_disjoint`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isHyperbolic_mul_of_disjoint).

```lean
TauCeti.GTree.isHyperbolic_mul_of_disjoint.{u, v, w} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {s t : G} (hs : T.IsElliptic s) (ht : T.IsElliptic t)
  (hst : Disjoint (MulAction.fixedBy T.V s) (MulAction.fixedBy T.V t)) : T.IsHyperbolic (s * t)
```

## Sources

- [Tau Ceti documentation: `TauCeti.GTree.IsEllipticSubgroup.of_fg`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.IsEllipticSubgroup.of_fg)
- [Source of `TauCeti.GTree.IsEllipticSubgroup.of_fg` in TauCeti/GroupTheory/GTree/FixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GTree/FixedPoint.lean#L239)
