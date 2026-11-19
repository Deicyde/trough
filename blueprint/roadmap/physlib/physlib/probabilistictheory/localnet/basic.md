---
declaration: module
origin: cited
lean: ProbabilisticTheory.LocalNet, ProbabilisticTheory.LocalNet.incl_refl_apply, ProbabilisticTheory.LocalNet.incl_trans_apply, ProbabilisticTheory.LocalNet.IsOrderEmbedding, ProbabilisticTheory.LocalNet.map_le_map_iff, ProbabilisticTheory.LocalNet.incl_injective, ProbabilisticTheory.LocalNet.inclLin, ProbabilisticTheory.LocalNet.directedSystem
statement: formalized
proof: formalized
---

# Local nets of observables

The module `Physlib.ProbabilisticTheory.LocalNet.Basic`, [Physlib/ProbabilisticTheory/LocalNet/Basic.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean): 19 declarations (2 instances with no name), 19 with a docstring.

> Observables of subsystems and their inclusion into larger subsystems.

## i. Overview

> Let `R` index subsystems, with `X ≤ Y` meaning that `X` is contained in `Y`. The observables of
> `X` are given by `(A X).Observables`. A local net assigns to `X ≤ Y` a channel,
> which regards an observable of `X` as one of `Y`.
>
> For a tensor product system with `H_Y ≃ H_X ⊗ H_rest`, `(A X).Observables` consists of Hermitian
> operators on `H_X`. Inclusion acts by `M ↦ M ⊗ 1`: this acts as `M` on `X` and
> as the identity on the remaining factors.
>
> The local observables can also be viewed in one space, `N.Quasilocal`, the algebraic direct limit
> of the local observable spaces. It is a real vector space and carries no norm. Completing it in a
> norm, which needs more structure than is assumed here, gives the quasilocal algebra of the physics
> literature. Inductive limits of order-unit spaces are developed in [ref: arxiv\_1705\_04663].

## ii. Key results

> - `LocalNet`: subsystem observables with channels into larger subsystems.
> - `LocalNet.IsOrderEmbedding`: the inclusion maps reflect order.
> - `LocalNet.map_le_map_iff`: inclusion preserves and reflects inequalities.
> - `LocalNet.incl_injective`: order-embedding inclusion maps are injective.
> - `LocalNet.Quasilocal`: the algebraic direct limit of the local observable spaces.
> - `LocalNet.toQuasilocal`: regard an observable of one subsystem as a quasilocal observable.
> - `LocalNet.toQuasilocal_eq_iff`: equality of quasilocal observables can be checked in a common
>   larger subsystem.
> - `LocalNet.toQuasilocal_injective`: order-embedding inclusions keep local observables distinct.
> - `LocalNet.exists_toQuasilocal_eq`, `exists_toQuasilocal_eq₂`: quasilocal observables have
>   representatives in a single subsystem, and any two have representatives in a common one.

## iv. References

> * L. Mawhinney, I. G. Todorov, *Inductive limits in the operator system and related categories*,
>   arXiv:1705.04663. [ref: arxiv\_1705\_04663]

## A. Subsystems and inclusions

**`ProbabilisticTheory.LocalNet`**, a structure, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L69).

> The observables of each subsystem, with channels into larger subsystems.

```lean
structure ProbabilisticTheory.LocalNet (R : Type*) [Preorder R] (A : R → ProbabilisticTheory) where
  /-- Regard an observable of `X` as an observable of `Y` when `X ≤ Y`. -/
  incl : ∀ {X Y : R}, X ≤ Y → Channel (A X) (A Y)
  /-- Inclusion into the same subsystem is the identity. -/
  incl_refl : ∀ X : R, incl (le_refl X) = .id (A X)
  /-- Including through an intermediate subsystem agrees with direct inclusion. -/
  incl_trans : ∀ {X Y Z : R} (h₁ : X ≤ Y) (h₂ : Y ≤ Z) (h₃ : X ≤ Z),
    incl h₃ = (incl h₂).comp (incl h₁)
```

**`ProbabilisticTheory.LocalNet.incl_refl_apply`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L84).

> An observable is unchanged by inclusion into the same subsystem.

```lean
lemma incl_refl_apply (N : LocalNet R A) (X : R) (a : (A X).Observables) :
    N.incl (le_refl X) a = a
```

**`ProbabilisticTheory.LocalNet.incl_trans_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L89).

> Including an observable through an intermediate subsystem agrees with direct inclusion.

```lean
lemma incl_trans_apply (N : LocalNet R A) (h₁ : X ≤ Y) (h₂ : Y ≤ Z) (h₃ : X ≤ Z)
    (a : (A X).Observables) :
    N.incl h₃ a = N.incl h₂ (N.incl h₁ a)
```

## B. Order-embedding inclusions

**`ProbabilisticTheory.LocalNet.IsOrderEmbedding`**, a class, [line 97](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L97).

> The inclusion maps are order embeddings if each reflects positivity.

```lean
class IsOrderEmbedding (N : LocalNet R A) : Prop where
  /-- An observable that is positive in a larger subsystem is already positive in the smaller. -/
  nonneg_of_incl_nonneg : ∀ {X Y : R} (h : X ≤ Y) {a : (A X).Observables}, 0 ≤ N.incl h a → 0 ≤ a
```

**`ProbabilisticTheory.LocalNet.map_le_map_iff`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L102).

> Inclusion in an order-embedding net preserves and reflects inequalities.

```lean
lemma map_le_map_iff (N : LocalNet R A) [N.IsOrderEmbedding] (h : X ≤ Y) {a b : (A X).Observables} :
    N.incl h a ≤ N.incl h b ↔ a ≤ b
```

**`ProbabilisticTheory.LocalNet.incl_injective`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L108).

> The inclusion maps of an order-embedding net are injective.

```lean
lemma incl_injective (N : LocalNet R A) [N.IsOrderEmbedding] (h : X ≤ Y) :
    Function.Injective (N.incl h)
```

## C. The quasilocal observable space

> For a directed family of subsystems, observables from different subsystems can be included in a
> common larger one and combined there. The direct limit identifies all such local descriptions
> consistently and supplies the resulting real vector space.

**`ProbabilisticTheory.LocalNet.inclLin`**, an abbrev, [line 126](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L126).

> The inclusions as linear maps: the transition maps of the direct limit defining
> `N.Quasilocal`.

```lean
abbrev inclLin (N : LocalNet R A) (X Y : R) (h : X ≤ Y) :
    (A X).Observables →ₗ[ℝ] (A Y).Observables
```

**`ProbabilisticTheory.LocalNet.directedSystem`**, an instance, [line 132](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L132).

> The inclusions form a directed system: including a subsystem into itself does nothing, and
> successive inclusions compose.

```lean
instance directedSystem (N : LocalNet R A) :
    DirectedSystem (fun X => (A X).Observables) fun i j h => N.inclLin i j h
```

**`ProbabilisticTheory.LocalNet.Quasilocal`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L138).

> The algebraic direct limit of the local observable spaces.

```lean
def Quasilocal (N : LocalNet R A) : Type _
```

**An instance with no name**, [line 142](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L142).

> Quasilocal observables add, as elements of a direct limit of vector spaces.

```lean
noncomputable instance : AddCommGroup N.Quasilocal
```

**An instance with no name**, [line 146](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L146).

> Quasilocal observables can be scaled by real numbers.

```lean
noncomputable instance : Module ℝ N.Quasilocal
```

## D. Embedding the local observables

> The map `toQuasilocal N i` takes an observable of subsystem `i` to the quasilocal observable it
> represents.

**`ProbabilisticTheory.LocalNet.toQuasilocal`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L158).

> Regard an observable of subsystem `i` as a quasilocal observable.

```lean
noncomputable def toQuasilocal (N : LocalNet R A) (i : R) : (A i).Observables →ₗ[ℝ] N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_incl`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L162).

> Including an observable in a larger subsystem does not change its quasilocal representation.

```lean
lemma toQuasilocal_incl {i j : R} (h : i ≤ j) (a : (A i).Observables) :
    toQuasilocal N j (N.incl h a) = toQuasilocal N i a
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_eq_of_incl_eq`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L168).

> Observables that agree in a common larger subsystem represent the same quasilocal
> observable.

```lean
lemma toQuasilocal_eq_of_incl_eq {i j k : R} (hik : i ≤ k) (hjk : j ≤ k)
    {a : (A i).Observables} {b : (A j).Observables} (h : N.incl hik a = N.incl hjk b) :
    toQuasilocal N i a = toQuasilocal N j b
```

## E. Directed families of subsystems

> If any two subsystems are contained in a common larger one, the quasilocal observable space is
> described by representatives in single subsystems.

**`ProbabilisticTheory.LocalNet.exists_incl_eq_of_toQuasilocal_eq`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L188).

> Observables representing the same quasilocal observable agree in a common larger
> subsystem.

```lean
lemma exists_incl_eq_of_toQuasilocal_eq {i j : R} {a : (A i).Observables} {b : (A j).Observables}
    (h : toQuasilocal N i a = toQuasilocal N j b) :
    ∃ (k : R) (hik : i ≤ k) (hjk : j ≤ k), N.incl hik a = N.incl hjk b
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_eq_iff`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L201).

> Two local observables represent the same quasilocal observable exactly when they agree in a
> common larger subsystem.

```lean
lemma toQuasilocal_eq_iff {i j : R} (a : (A i).Observables) (b : (A j).Observables) :
    toQuasilocal N i a = toQuasilocal N j b ↔
      ∃ (k : R) (hik : i ≤ k) (hjk : j ≤ k), N.incl hik a = N.incl hjk b
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_injective`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L207).

> Order-embedding inclusions keep distinct local observables distinct in the quasilocal space.

```lean
lemma toQuasilocal_injective [N.IsOrderEmbedding] (i : R) :
    Function.Injective (toQuasilocal N i)
```

**`ProbabilisticTheory.LocalNet.exists_toQuasilocal_eq`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L218).

> Every quasilocal observable has a representative in some subsystem.

```lean
lemma exists_toQuasilocal_eq (x : N.Quasilocal) :
    ∃ (i : R) (a : (A i).Observables), toQuasilocal N i a = x
```

**`ProbabilisticTheory.LocalNet.exists_toQuasilocal_eq₂`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean#L223).

> Any two quasilocal observables have representatives in a common subsystem.

```lean
lemma exists_toQuasilocal_eq₂ (x y : N.Quasilocal) :
    ∃ (i : R) (a b : (A i).Observables), toQuasilocal N i a = x ∧ toQuasilocal N i b = y
```

## Depends on

- [Channels between observable spaces](../channel/basic.md)

## Sources

- [Physlib/ProbabilisticTheory/LocalNet/Basic.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/Basic.lean)
