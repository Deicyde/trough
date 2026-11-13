---
declaration: module
origin: cited
lean: ProbabilisticTheory.NormCone, ProbabilisticTheory.NormCone.toProd, ProbabilisticTheory.NormCone.toProd_zero, ProbabilisticTheory.NormCone.toProd_add, ProbabilisticTheory.NormCone.toProd_neg, ProbabilisticTheory.NormCone.toProd_sub, ProbabilisticTheory.NormCone.toProd_smul, ProbabilisticTheory.NormCone.toProd_one
statement: formalized
proof: formalized
---

# Order-unit spaces built from a normed vector space

The module `PhyslibAlpha.ProbabilisticTheory.Examples.NormCone`, [PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean): 57 declarations (10 instances with no name), 22 with a docstring.

> The order-unit space `ℝ × V` ordered by the norm cone of `V`, and its states as the dual ball.

## i. Overview

> Any real normed vector space `V` carries a natural order-unit structure on `ℝ × V`: order unit
> `(1, 0)`, and positive cone the "ice-cream" cone `{(r, x) | ‖x‖ ≤ r}` built from `V`'s norm. States
> of this order-unit space correspond exactly to the closed unit ball of the continuous dual of `V`.
>
> The qubit is the norm cone over Euclidean `ℝ³` and the generalized bit the norm cone over `ℝ³`
> with the sup norm: same dimension, different norm, different state space.

## ii. Key results

> - `NormCone V` : the order-unit space `ℝ × V`, ordered by the ice-cream cone built from `V`'s norm.
> - `NormCone.instArchimedeanOrderUnitSpace` : `NormCone V` is an Archimedean order-unit space.
> - `NormCone.mem_effect_iff` : an explicit description of `Effect (NormCone V)`.
> - `NormCone.stateEquiv` : states of `NormCone V` correspond exactly to the closed unit ball of the
>   continuous dual of `V`.
> - `NormCone.lpStateEquiv`, `NormCone.supStateEquiv` : the states of an `ℓp` norm cone are the closed
>   `ℓq` ball, those of the sup-normed cone the `ℓ1` ball.

## iv. References

> - J. Barrett, *Information processing in generalized probabilistic theories*, Phys. Rev. A 75,
>   032304 (2007).
> - P. Janotta and H. Lal, *Generalized probabilistic theories without the no-restriction
>   hypothesis*, Phys. Rev. A 87, 052131 (2013).

## A. The ice-cream cone order

**`ProbabilisticTheory.NormCone`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L68).

> The order-unit space `ℝ × V` built from a real normed vector space `V`, ordered by the
> ice-cream cone `{(r, x) | ‖x‖ ≤ r}`, as a type synonym so its order does not clash with the
> product order on `ℝ × V`.

```lean
def NormCone (V : Type*) [NormedAddCommGroup V] [NormedSpace ℝ V]
```

**`ProbabilisticTheory.NormCone.toProd`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L75).

> The linear equivalence to the underlying product, forgetting the order.

```lean
def toProd : NormCone V ≃ ℝ × V
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L77).

```lean
instance : AddCommGroup (NormCone V)
```

**An instance with no name**, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L78).

```lean
instance : Module ℝ (NormCone V)
```

**An instance with no name**, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L79).

```lean
instance : One (NormCone V)
```

**An instance with no name**, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L80).

```lean
instance : Nontrivial (NormCone V)
```

**An instance with no name**, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L83).

> `NormCone V` is finite-dimensional when `V` is.

```lean
instance [FiniteDimensional ℝ V] : Module.Finite ℝ (NormCone V)
```

**`ProbabilisticTheory.NormCone.toProd_zero`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L86).

```lean
lemma toProd_zero : toProd (0 : NormCone V) = 0
```

**`ProbabilisticTheory.NormCone.toProd_add`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L87).

```lean
lemma toProd_add (x y : NormCone V) : toProd (x + y) = toProd x + toProd y
```

**`ProbabilisticTheory.NormCone.toProd_neg`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L88).

```lean
lemma toProd_neg (x : NormCone V) : toProd (-x) = -toProd x
```

**`ProbabilisticTheory.NormCone.toProd_sub`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L89).

```lean
lemma toProd_sub (x y : NormCone V) : toProd (x - y) = toProd x - toProd y
```

**`ProbabilisticTheory.NormCone.toProd_smul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L90).

```lean
lemma toProd_smul (c : ℝ) (x : NormCone V) : toProd (c • x) = c • toProd x
```

**`ProbabilisticTheory.NormCone.toProd_one`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L91).

```lean
lemma toProd_one : toProd (1 : NormCone V) = (1, 0)
```

**`ProbabilisticTheory.NormCone.toProd_smul_one`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L94).

> The order unit `1 : NormCone V` scaled by a real number, in coordinates.

```lean
lemma toProd_smul_one (r : ℝ) : toProd (r • (1 : NormCone V)) = (r, 0)
```

**`ProbabilisticTheory.NormCone.mk`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L98).

> Build an element of `NormCone V` from its coordinates.

```lean
def mk (r : ℝ) (v : V) : NormCone V
```

**`ProbabilisticTheory.NormCone.toProd_mk`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L100).

```lean
lemma toProd_mk (r : ℝ) (v : V) : toProd (mk r v) = (r, v)
```

**`ProbabilisticTheory.NormCone.NonnegCone`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L103).

> The ice-cream cone: `(r, x)` is nonnegative when `‖x‖ ≤ r`.

```lean
def NonnegCone (z : NormCone V) : Prop
```

**An instance with no name**, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L105).

```lean
instance : LE (NormCone V)
```

**An instance with no name**, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L106).

```lean
instance : LT (NormCone V)
```

**`ProbabilisticTheory.NormCone.le_iff`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L108).

```lean
lemma le_iff {x y : NormCone V} :
    x ≤ y ↔ ‖(toProd y).2 - (toProd x).2‖ ≤ (toProd y).1 - (toProd x).1
```

**`ProbabilisticTheory.NormCone.mk_le_mk_iff`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L112).

```lean
lemma mk_le_mk_iff {r₁ r₂ : ℝ} {v₁ v₂ : V} :
    mk r₁ v₁ ≤ mk r₂ v₂ ↔ ‖v₂ - v₁‖ ≤ r₂ - r₁
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L116).

```lean
instance : PartialOrder (NormCone V)
```

**An instance with no name**, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L129).

```lean
instance : IsOrderedAddMonoid (NormCone V)
```

**An instance with no name**, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L134).

```lean
instance : PosSMulMono ℝ (NormCone V)
```

## B. `NormCone V` is an Archimedean order-unit space

**`ProbabilisticTheory.NormCone.instOrderUnitSpace`**, an instance, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L151).

```lean
instance instOrderUnitSpace : OrderUnitSpace (NormCone V)
```

**`ProbabilisticTheory.NormCone.instArchimedeanOrderUnitSpace`**, an instance, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L160).

```lean
instance instArchimedeanOrderUnitSpace : ArchimedeanOrderUnitSpace (NormCone V)
```

## C. Effects

**`ProbabilisticTheory.NormCone.mem_effect_iff`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L177).

> The effects of `NormCone V` are the pairs `(r, v)` with `‖v‖ ≤ r` and `‖v‖ ≤ 1 - r`.

```lean
lemma mem_effect_iff {z : NormCone V} :
    z ∈ (Effect (NormCone V) : Set (NormCone V)) ↔
      ‖(toProd z).2‖ ≤ (toProd z).1 ∧ ‖(toProd z).2‖ ≤ 1 - (toProd z).1
```

## D. States correspond to the closed unit ball of the dual

**`ProbabilisticTheory.NormCone.mk_add`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L188).

```lean
lemma mk_add (r₁ r₂ : ℝ) (v₁ v₂ : V) : mk r₁ v₁ + mk r₂ v₂ = mk (r₁ + r₂) (v₁ + v₂)
```

**`ProbabilisticTheory.NormCone.mk_smul`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L191).

```lean
lemma mk_smul (c : ℝ) (r : ℝ) (v : V) : c • mk r v = mk (c * r) (c • v)
```

**`ProbabilisticTheory.NormCone.mk_neg`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L194).

```lean
lemma mk_neg (r : ℝ) (v : V) : -mk r v = mk (-r) (-v)
```

**`ProbabilisticTheory.NormCone.smul_one_eq_mk`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L197).

```lean
lemma smul_one_eq_mk (r : ℝ) : r • (1 : NormCone V) = mk r 0
```

**`ProbabilisticTheory.NormCone.mk_toProd`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L200).

```lean
lemma mk_toProd (z : NormCone V) : mk (toProd z).1 (toProd z).2 = z
```

**`ProbabilisticTheory.NormCone.neg_smul_one_le_mk_zero_iff`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L202).

```lean
lemma neg_smul_one_le_mk_zero_iff {r : ℝ} {v : V} : -(r • (1 : NormCone V)) ≤ mk 0 v ↔ ‖v‖ ≤ r
```

**`ProbabilisticTheory.NormCone.mk_zero_le_smul_one_iff`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L206).

```lean
lemma mk_zero_le_smul_one_iff {r : ℝ} {v : V} : mk 0 v ≤ r • (1 : NormCone V) ↔ ‖v‖ ≤ r
```

**`ProbabilisticTheory.NormCone.orderUnitNorm_mk_zero`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L213).

> The order-unit norm of a purely spatial coordinate `(0, v)` is exactly the norm of `v`: the
> order-unit norm restricted to this slice is the norm it was built from.

```lean
lemma orderUnitNorm_mk_zero (v : V) : orderUnitNorm (mk 0 v) = ‖v‖
```

**`ProbabilisticTheory.NormCone.mkZeroLinear`**, a def, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L220).

> The linear map `v ↦ (0, v)` from `V` into `NormCone V`.

```lean
def mkZeroLinear : V →ₗ[ℝ] NormCone V
```

**`ProbabilisticTheory.NormCone.mkZeroLinear_apply`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L225).

```lean
lemma mkZeroLinear_apply (v : V) : mkZeroLinear v = mk 0 v
```

**`ProbabilisticTheory.NormCone.apply_mk_eq`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L228).

> Every state is a "radius plus a bounded linear functional of the spatial part".

```lean
lemma apply_mk_eq (ω : 𝓢[ℝ, NormCone V]) (r : ℝ) (v : V) :
    ω (mk r v) = r + ω (mkZeroLinear v)
```

**`ProbabilisticTheory.NormCone.abs_apply_mkZeroLinear_le`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L235).

> The functional a state induces on `V`, `v ↦ ω (0, v)`, is `1`-Lipschitz.

```lean
lemma abs_apply_mkZeroLinear_le (ω : 𝓢[ℝ, NormCone V]) (v : V) :
    |ω (mkZeroLinear v)| ≤ ‖v‖
```

**`ProbabilisticTheory.NormCone.dualOfLinear`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L242).

> The linear functional `v ↦ ω (0, v)` induced by a state.

```lean
def dualOfLinear (ω : 𝓢[ℝ, NormCone V]) : V →ₗ[ℝ] ℝ
```

**`ProbabilisticTheory.NormCone.dualOfLinear_apply`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L247).

```lean
lemma dualOfLinear_apply (ω : 𝓢[ℝ, NormCone V]) (v : V) :
    dualOfLinear ω v = ω (mkZeroLinear v)
```

**`ProbabilisticTheory.NormCone.dualOf`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L251).

> The bounded linear functional on `V` induced by a state of `NormCone V`.

```lean
noncomputable def dualOf (ω : 𝓢[ℝ, NormCone V]) : V →L[ℝ] ℝ
```

**`ProbabilisticTheory.NormCone.dualOf_apply`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L254).

```lean
lemma dualOf_apply (ω : 𝓢[ℝ, NormCone V]) (v : V) : dualOf ω v = ω (mkZeroLinear v)
```

**`ProbabilisticTheory.NormCone.norm_dualOf_le`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L257).

```lean
lemma norm_dualOf_le (ω : 𝓢[ℝ, NormCone V]) : ‖dualOf ω‖ ≤ 1
```

**`ProbabilisticTheory.NormCone.stateOfDual`**, a def, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L262).

> Build a state of `NormCone V` from a bounded linear functional `f` of norm at most `1`:
> `ω (r, x) = r + f x`.

```lean
noncomputable def stateOfDual (f : V →L[ℝ] ℝ) (hf : ‖f‖ ≤ 1) : 𝓢[ℝ, NormCone V]
```

**`ProbabilisticTheory.NormCone.stateOfDual_apply`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L275).

```lean
lemma stateOfDual_apply (f : V →L[ℝ] ℝ) (hf : ‖f‖ ≤ 1) (z : NormCone V) :
    stateOfDual f hf z = (toProd z).1 + f (toProd z).2
```

**`ProbabilisticTheory.NormCone.stateEquiv`**, a def, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L280).

> States of `NormCone V` correspond exactly to the closed unit ball of the continuous dual
> of `V`.

```lean
noncomputable def stateEquiv : 𝓢[ℝ, NormCone V] ≃ {f : V →L[ℝ] ℝ // ‖f‖ ≤ 1}
```

## E. States, expanded against a basis

**`ProbabilisticTheory.NormCone.apply_mk_basis`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L302).

> A state is determined by its values on a basis.

```lean
lemma apply_mk_basis (b : Module.Basis ι ℝ V) (ω : 𝓢[ℝ, NormCone V]) (r : ℝ) (v : V) :
    ω (mk r v) = r + ∑ i, b.repr v i * ω (mk 0 (b i))
```

## F. Purity and extreme points of the dual ball

**`ProbabilisticTheory.NormCone.dualOf_mix`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L316).

> `dualOf` sends mixtures to convex combinations.

```lean
lemma dualOf_mix (φ ψ : 𝓢[ℝ, NormCone V]) (t : unitInterval) :
    dualOf (UnitalPositiveLinearMap.mix φ ψ t) =
      (t : ℝ) • dualOf φ + (1 - (t : ℝ)) • dualOf ψ
```

**`ProbabilisticTheory.NormCone.dualOf_injective`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L325).

> `dualOf` is injective.

```lean
lemma dualOf_injective : Function.Injective (dualOf (V := V))
```

**`ProbabilisticTheory.NormCone.dualOf_stateOfDual`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L330).

> `dualOf` undoes `stateOfDual`.

```lean
lemma dualOf_stateOfDual (f : V →L[ℝ] ℝ) (hf : ‖f‖ ≤ 1) :
    dualOf (stateOfDual f hf) = f
```

**`ProbabilisticTheory.NormCone.range_dualOf`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L334).

```lean
lemma range_dualOf : Set.range (dualOf (V := V)) = {g | ‖g‖ ≤ 1}
```

**`ProbabilisticTheory.NormCone.isPure_stateOfDual_iff`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L340).

> A state is pure exactly when its functional is an extreme point of the unit ball of the
> dual.

```lean
lemma isPure_stateOfDual_iff {f : V →L[ℝ] ℝ} (hf : ‖f‖ ≤ 1) :
    (stateOfDual f hf).IsPure ↔ f ∈ Set.extremePoints ℝ {g : V →L[ℝ] ℝ | ‖g‖ ≤ 1}
```

## G. States of `ℓp` and sup norm cones

**`ProbabilisticTheory.NormCone.lpStateEquiv`**, a def, [line 359](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L359).

> The states of an `ℓp` norm cone are the closed `ℓq` ball.

```lean
noncomputable def lpStateEquiv (hpq : p.HolderConjugate q)
    (hnorm : ∀ v : V, ‖v‖ = (∑ i, |b.repr v i| ^ p) ^ (1 / p)) :
    𝓢[ℝ, NormCone V] ≃ {a : Fin n → ℝ // ∑ i, |a i| ^ q ≤ 1}
```

**`ProbabilisticTheory.NormCone.lpCone_mem_effect_iff`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L365).

```lean
lemma lpCone_mem_effect_iff (hnorm : ∀ v : V, ‖v‖ = (∑ i, |b.repr v i| ^ p) ^ (1 / p))
    {z : NormCone V} : z ∈ (Effect (NormCone V) : Set (NormCone V)) ↔
      (∑ i, |b.repr (toProd z).2 i| ^ p) ^ (1 / p) ≤ (toProd z).1 ∧
        (∑ i, |b.repr (toProd z).2 i| ^ p) ^ (1 / p) ≤ 1 - (toProd z).1
```

**`ProbabilisticTheory.NormCone.supStateEquiv`**, a def, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L374).

> The states of the sup-normed norm cone are the closed `ℓ1` ball.

```lean
noncomputable def supStateEquiv {m : ℕ} :
    𝓢[ℝ, NormCone (Fin m → ℝ)] ≃ {a : Fin m → ℝ // ∑ i, |a i| ≤ 1}
```

**`ProbabilisticTheory.NormCone.supCone_mem_effect_iff`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean#L378).

```lean
lemma supCone_mem_effect_iff {m : ℕ} {z : NormCone (Fin m → ℝ)} :
    z ∈ (Effect (NormCone (Fin m → ℝ)) : Set (NormCone (Fin m → ℝ))) ↔
      ‖(toProd z).2‖ ≤ (toProd z).1 ∧ ‖(toProd z).2‖ ≤ 1 - (toProd z).1
```

## Depends on

- [Effects](../../../physlib/probabilistictheory/effect/basic.md)
- [Hölder duality in finite dimensions](../../mathematics/part-01/analysis/normed-holderdual.md)
- [Convex state spaces](../state/convex.md)

## Proof depends on

- [The metric space of states](../state/metric.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Examples/NormCone.lean)
