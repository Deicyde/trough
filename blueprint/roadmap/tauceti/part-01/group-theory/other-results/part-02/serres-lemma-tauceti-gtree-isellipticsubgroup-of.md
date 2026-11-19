---
declaration: theorem
origin: cited
lean: TauCeti.GTree.IsEllipticSubgroup.of_fg, TauCeti.GTree.isEllipticSubgroup_closure, TauCeti.GTree.isEllipticSubgroup_sSup, TauCeti.GTree.isEllipticSubgroup_closure_iUnion, TauCeti.GTree.isEllipticSubgroup_iSup, TauCeti.GTree.isEllipticSubgroup_closure_union, TauCeti.GTree.IsEllipticSubgroup.sup, TauCeti.GTree.isHyperbolic_mul_of_disjoint
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

- [TauCeti.GTree](../../free-groups-equations-over-groups-and-limit-grou/tauceti-gtree.md)

## Proof depends on

- [Helly's theorem for subtrees](../../../combinatorics/graph/hellys-theorem-for-subtrees.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GTree.IsEllipticSubgroup.of_fg`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.IsEllipticSubgroup.of_fg).

## Other forms

**Serre's lemma.** Formalized in Tau Ceti as [`TauCeti.GTree.isEllipticSubgroup_closure`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isEllipticSubgroup_closure).

```lean
TauCeti.GTree.isEllipticSubgroup_closure.{u, v, w} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {S : Set G} (hS : S.Finite) (h₁ : ∀ s ∈ S, T.IsElliptic s)
  (h₂ : S.Pairwise fun s t => T.IsElliptic (s * t)) : T.IsEllipticSubgroup (Subgroup.closure S)
```

**Serre's lemma for a finite set of subgroups.** Formalized in Tau Ceti as [`TauCeti.GTree.isEllipticSubgroup_sSup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isEllipticSubgroup_sSup).

```lean
TauCeti.GTree.isEllipticSubgroup_sSup.{u, v, w} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {ℋ : Set (Subgroup G)} (hℋ : ℋ.Finite) (hH : ∀ H ∈ ℋ, T.IsEllipticSubgroup H)
  (h : ℋ.Pairwise fun H K => ∀ a ∈ H, ∀ b ∈ K, T.IsElliptic (a * b)) : T.IsEllipticSubgroup (sSup ℋ)
```

**Serre's lemma for finitely many generating sets.** Formalized in Tau Ceti as [`TauCeti.GTree.isEllipticSubgroup_closure_iUnion`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isEllipticSubgroup_closure_iUnion).

```lean
TauCeti.GTree.isEllipticSubgroup_closure_iUnion.{u, v, w, u_1} {G : Type w} [Group G]
  {T : TauCeti.GTree G} {ι : Type u_1} [Finite ι] {S : ι → Set G}
  (hS : ∀ (i : ι), T.IsEllipticSubgroup (Subgroup.closure (S i)))
  (h : Pairwise fun i j => ∀ a ∈ S i, ∀ b ∈ S j, T.IsElliptic (a * b)) :
  T.IsEllipticSubgroup (Subgroup.closure (⋃ i, S i))
```

**Serre's lemma for finitely many subgroups.** Formalized in Tau Ceti as [`TauCeti.GTree.isEllipticSubgroup_iSup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isEllipticSubgroup_iSup).

```lean
TauCeti.GTree.isEllipticSubgroup_iSup.{u, v, w, u_1} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {ι : Type u_1} [Finite ι] {H : ι → Subgroup G} (hH : ∀ (i : ι), T.IsEllipticSubgroup (H i))
  (h : Pairwise fun i j => ∀ a ∈ H i, ∀ b ∈ H j, T.IsElliptic (a * b)) :
  T.IsEllipticSubgroup (⨆ i, H i)
```

**Serre's lemma for two generating sets.** Formalized in Tau Ceti as [`TauCeti.GTree.isEllipticSubgroup_closure_union`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isEllipticSubgroup_closure_union).

```lean
TauCeti.GTree.isEllipticSubgroup_closure_union.{u, v, w} {G : Type w} [Group G]
  {T : TauCeti.GTree G} {S S' : Set G} (hS : T.IsEllipticSubgroup (Subgroup.closure S))
  (hS' : T.IsEllipticSubgroup (Subgroup.closure S')) (h : ∀ a ∈ S, ∀ b ∈ S', T.IsElliptic (a * b)) :
  T.IsEllipticSubgroup (Subgroup.closure (S ∪ S'))
```

**Serre's lemma for two subgroups.** Formalized in Tau Ceti as [`TauCeti.GTree.IsEllipticSubgroup.sup`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.IsEllipticSubgroup.sup).

```lean
TauCeti.GTree.IsEllipticSubgroup.sup.{u, v, w} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {H K : Subgroup G} (hH : T.IsEllipticSubgroup H) (hK : T.IsEllipticSubgroup K)
  (h : ∀ a ∈ H, ∀ b ∈ K, T.IsElliptic (a * b)) : T.IsEllipticSubgroup (H ⊔ K)
```

**Serre's lemma on pairs of elliptic elements.** Formalized in Tau Ceti as [`TauCeti.GTree.isHyperbolic_mul_of_disjoint`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.isHyperbolic_mul_of_disjoint).

```lean
TauCeti.GTree.isHyperbolic_mul_of_disjoint.{u, v, w} {G : Type w} [Group G] {T : TauCeti.GTree G}
  {s t : G} (hs : T.IsElliptic s) (ht : T.IsElliptic t)
  (hst : Disjoint (MulAction.fixedBy T.V s) (MulAction.fixedBy T.V t)) : T.IsHyperbolic (s * t)
```

## Sources

- [Tau Ceti documentation: `TauCeti.GTree.IsEllipticSubgroup.of_fg`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GTree/FixedPoint.html#TauCeti.GTree.IsEllipticSubgroup.of_fg)
- [Source of `TauCeti.GTree.IsEllipticSubgroup.of_fg` in TauCeti/GroupTheory/GTree/FixedPoint.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/GTree/FixedPoint.lean#L317)
