---
declaration: module
origin: cited
lean: HasRieszDecomposition.exists_isBinaryJointEffect, HasRieszDecomposition.jointlyMeasurable, Bidual.apply_mono, Bidual.sub_le_of_forall_effect, Bidual.exists_sub_eq_sum, Bidual.effectValues, Bidual.convex_effectValues, Bidual.mem_closure_effectValues
statement: formalized
proof: formalized
---

# Classical theories are those without incompatibility

The module `PhyslibAlpha.ProbabilisticTheory.Classical.Compatibility`, [PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean): 39 declarations, 29 with a docstring.

> Kuramochi's theorem: a system is classical exactly when all yes/no measurements are compatible.

## i. Overview

> In classical probability every two yes/no questions can be asked at once. In quantum theory they
> cannot: spin along `x` and spin along `z` have no joint measurement. Compatibility of all pairs of
> yes/no measurements characterizes classical theories: it holds exactly when the positive
> functionals form a lattice, that is, when the state space is a Choquet simplex.
>
> When observables have the Riesz decomposition, every two yes/no measurements have a joint
> measurement. Conversely, compatibility in `E` passes to the bidual of `E`, where increasing families
> have suprema. There, a maximal decomposition turns compatibility into Riesz decomposition, and the
> least upper bound of two positive functionals on the bidual restricts to one on `E`. For the other
> direction, a lattice of positive functionals yields interpolants between observables; when the
> observables are complete, these give joint effects exactly.

## ii. Key results

> - `HasRieszDecomposition.exists_isBinaryJointEffect` : Riesz decomposition makes every two yes/no
>   measurements compatible.
> - `Bidual.exists_effect_near` : effects of `E` approximate effects of the bidual on finitely many
>   positive functionals.
> - `Bidual.exists_isBinaryJointEffect` : compatibility passes from `E` to its bidual.
> - `Bidual.hasRieszDecomposition` : compatibility in the bidual gives Riesz decomposition there.
> - `isClassical_of_jointlyMeasurable` : if every two yes/no measurements are compatible, the
>   positive functionals form a lattice.
> - `isClassical_iff_jointlyMeasurable` : **Kuramochi's theorem**: on a complete Archimedean
>   order-unit space, the positive functionals form a lattice exactly when every two yes/no
>   measurements are compatible.

## iv. References

> - Y. Kuramochi, *Compatibility of any pair of 2-outcome measurements characterizes the Choquet
>   simplex*, Positivity 24 (2020), 1479–1486. <https://arxiv.org/abs/1912.00563>
> - M. Plávala, *All measurements in a probabilistic theory are compatible if and only if the state
>   space is a simplex*, Phys. Rev. A 94 (2016), 042108.

## A. Riesz decomposition gives compatibility

**`HasRieszDecomposition.exists_isBinaryJointEffect`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L75).

> With Riesz decomposition, every two effects have a joint effect: split `e ≤ f + (1 - f)`.

```lean
lemma _root_.HasRieszDecomposition.exists_isBinaryJointEffect (hE : HasRieszDecomposition E)
    (e f : Effect E) : ∃ g : E, Effect.IsBinaryJointEffect e f g
```

**`HasRieszDecomposition.jointlyMeasurable`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L88).

> With Riesz decomposition, every two yes/no measurements are jointly measurable.

```lean
lemma _root_.HasRieszDecomposition.jointlyMeasurable
    (hF : HasRieszDecomposition F) (e f : Effect F) :
    Measurement.JointlyMeasurable (Effect.binaryMeasurement e)
      (Effect.binaryMeasurement f)
```

## B. Approximating effects of the bidual

**`Bidual.apply_mono`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L106).

> An element of the bidual that is nonnegative is monotone in the positive functional.

```lean
lemma apply_mono {x : Bidual E} (hx : 0 ≤ x) {φ ψ : E →ₚ[ℝ] ℝ} (h : φ ≤ ψ) : x φ ≤ x ψ
```

**`Bidual.sub_le_of_forall_effect`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L111).

> If `P - N` is at most `m` on the effects of `E`, it is at most `m` on every effect of the
> bidual.

```lean
lemma sub_le_of_forall_effect {x : Bidual E} (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (P N : E →ₚ[ℝ] ℝ) {m : ℝ}
    (hm : ∀ a : E, 0 ≤ a → a ≤ 1 → P a - N a ≤ m) : x P - x N ≤ m
```

**`Bidual.exists_sub_eq_sum`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L120).

> A real combination of positive functionals is a difference `P - N` of positive functionals, also
> in its values on the bidual.

```lean
lemma exists_sub_eq_sum {ι : Type*} [Fintype ι] (φ : ι → E →ₚ[ℝ] ℝ) (w : ι → ℝ) :
    ∃ P N : E →ₚ[ℝ] ℝ, (∀ a, P a - N a = ∑ i, w i * φ i a) ∧
      ∀ x : Bidual E, x P - x N = ∑ i, w i * x (φ i)
```

**`Bidual.effectValues`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L130).

> The values of the effects of `E` on the positive functionals in `S`.

```lean
def effectValues (S : Finset (E →ₚ[ℝ] ℝ)) : Set (S → ℝ)
```

**`Bidual.convex_effectValues`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L133).

```lean
lemma convex_effectValues (S : Finset (E →ₚ[ℝ] ℝ)) : Convex ℝ (effectValues S)
```

**`Bidual.mem_closure_effectValues`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L140).

> The values of an effect of the bidual lie in the closure of the values of effects of `E`.

```lean
lemma mem_closure_effectValues {x : Bidual E} (hx0 : 0 ≤ x) (hx1 : x ≤ 1)
    (S : Finset (E →ₚ[ℝ] ℝ)) : (fun φ : S => x φ.1) ∈ closure (effectValues S)
```

**`Bidual.exists_effect_near`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L157).

> Effects of `E` approximate an effect of the bidual on finitely many positive functionals.

```lean
lemma exists_effect_near {x : Bidual E} (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (S : Finset (E →ₚ[ℝ] ℝ))
    {ε : ℝ} (hε : 0 < ε) : ∃ a : E, 0 ≤ a ∧ a ≤ 1 ∧ ∀ φ ∈ S, |φ a - x φ| < ε
```

## C. Compatibility in the bidual

**`Bidual.jointCandidates`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L170).

> The functions on positive functionals that are additive, positively homogeneous, lie between
> `-φ 1` and `2 • φ 1`, and satisfy the joint-effect conditions for `x` and `y` up to `1 / (n + 1)` on
> the finite set `S`.

```lean
def jointCandidates (x y : Bidual E) (i : Finset (E →ₚ[ℝ] ℝ) × ℕ) :
    Set ((E →ₚ[ℝ] ℝ) → ℝ)
```

**`Bidual.isClosed_jointCandidates`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L177).

```lean
lemma isClosed_jointCandidates (x y : Bidual E) (i : Finset (E →ₚ[ℝ] ℝ) × ℕ) :
    IsClosed (jointCandidates x y i)
```

**`Bidual.mem_jointCandidates_of_near`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L192).

> The values of an approximate joint effect of approximations of `x` and `y`: a candidate.

```lean
lemma mem_jointCandidates_of_near {x y : Bidual E} {i : Finset (E →ₚ[ℝ] ℝ) × ℕ} {a b c : E}
    {δ : ℝ} (hδ : δ • (∑ φ ∈ i.1, φ 1) ≤ 1 / (i.2 + 1) / 4) (hδ1 : δ ≤ 1)
    (ha : ∀ φ ∈ i.1, |φ a - x φ| < 1 / (i.2 + 1) / 4)
    (hb : ∀ φ ∈ i.1, |φ b - y φ| < 1 / (i.2 + 1) / 4) (ha1 : a ≤ 1)
    (hc : -(δ • (1 : E)) ≤ c ∧ c ≤ a + δ • 1 ∧ c ≤ b + δ • 1 ∧ a + b - 1 ≤ c + δ • 1) :
    (fun φ => φ c) ∈ jointCandidates x y i
```

**`Bidual.jointCandidates_nonempty`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L224).

> Approximate compatibility of the observables provides candidates for a joint effect in the
> bidual.

```lean
lemma jointCandidates_nonempty
    (hE : ∀ (e f : Effect E) (δ : ℝ), 0 < δ → ∃ g : E, Effect.IsApproxBinaryJointEffect e f δ g)
    (x y : Effect (Bidual E)) (i : Finset (E →ₚ[ℝ] ℝ) × ℕ) :
    (jointCandidates (x : Bidual E) y i).Nonempty
```

**`Bidual.jointCandidates_antitone`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L243).

```lean
lemma jointCandidates_antitone (x y : Bidual E) {i j : Finset (E →ₚ[ℝ] ℝ) × ℕ} (h : i ≤ j) :
    jointCandidates x y j ⊆ jointCandidates x y i
```

**`Bidual.nonempty_iInter_jointCandidates`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L253).

> Compatibility of the observables makes all candidate sets meet.

```lean
lemma nonempty_iInter_jointCandidates
    (hE : ∀ (e f : Effect E) (δ : ℝ), 0 < δ → ∃ g : E, Effect.IsApproxBinaryJointEffect e f δ g)
    (x y : Effect (Bidual E)) : (⋂ i, jointCandidates (x : Bidual E) y i).Nonempty
```

**`Bidual.exists_isBinaryJointEffect_of_mem`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L268).

> A function in all candidate sets is a joint effect in the bidual.

```lean
lemma exists_isBinaryJointEffect_of_mem {x y : Effect (Bidual E)} {z : (E →ₚ[ℝ] ℝ) → ℝ}
    (hz : z ∈ ⋂ i, jointCandidates (x : Bidual E) y i) :
    ∃ z' : Bidual E, Effect.IsBinaryJointEffect x y z'
```

**`Bidual.exists_isBinaryJointEffect`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L288).

> **Compatibility passes to the bidual.** If every two effects of `E` have joint effects up to any
> error, every two effects of the bidual have a joint effect.

```lean
lemma exists_isBinaryJointEffect
    (hE : ∀ (e f : Effect E) (δ : ℝ), 0 < δ → ∃ g : E, Effect.IsApproxBinaryJointEffect e f δ g)
    (x y : Effect (Bidual E)) : ∃ z : Bidual E, Effect.IsBinaryJointEffect x y z
```

## D. Riesz decomposition in the bidual

**`Bidual.gauge`**, a def, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L296).

> The least `t ≥ 0` with `x ≤ t • 1`.

```lean
noncomputable def gauge (x : Bidual E) : ℝ
```

**`Bidual.gauge_set_nonempty`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L298).

```lean
lemma gauge_set_nonempty (x : Bidual E) : {t : ℝ | 0 ≤ t ∧ x ≤ t • 1}.Nonempty
```

**`Bidual.gauge_nonneg`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L302).

```lean
lemma gauge_nonneg (x : Bidual E) : 0 ≤ gauge x
```

**`Bidual.gauge_le`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L305).

```lean
lemma gauge_le {x : Bidual E} {t : ℝ} (ht : 0 ≤ t) (h : x ≤ t • 1) : gauge x ≤ t
```

**`Bidual.le_gauge_smul`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L308).

```lean
lemma le_gauge_smul (x : Bidual E) : x ≤ gauge x • 1
```

**`Bidual.gauge_zero`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L318).

```lean
lemma gauge_zero : gauge (0 : Bidual E) = 0
```

**`Bidual.eq_zero_of_gauge_eq_zero`**, a lemma, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L321).

```lean
lemma eq_zero_of_gauge_eq_zero {x : Bidual E} (hx : 0 ≤ x) (h : gauge x = 0) : x = 0
```

**`Bidual.inv_gauge_smul_mem`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L324).

```lean
lemma inv_gauge_smul_mem {x : Bidual E} (hx : 0 ≤ x) (h : 0 < gauge x) :
    (gauge x)⁻¹ • x ∈ (Effect (Bidual E) : Set (Bidual E))
```

**`Bidual.eq_zero_of_le_inv_smul`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L331).

> A nonnegative element below `c⁻¹ • r` and `d⁻¹ • w` vanishes when `r` and `w` have no nonzero
> common lower bound.

```lean
lemma eq_zero_of_le_inv_smul {r w z : Bidual E} {c d : ℝ} (hc : 0 < c) (hd : 0 < d) (hz0 : 0 ≤ z)
    (hzr : z ≤ c⁻¹ • r) (hzw : z ≤ d⁻¹ • w) (horth : ∀ y, 0 ≤ y → y ≤ r → y ≤ w → y = 0) :
    z = 0
```

**`Bidual.gauge_mul_le_of_orthogonal`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L348).

> Compatible nonnegative elements `r` and `w` with no nonzero common lower bound are spread
> apart: `r / gauge r + w / gauge w ≤ 1`.

```lean
lemma gauge_mul_le_of_orthogonal {r w : Bidual E} (hr : 0 ≤ r) (hw : 0 ≤ w)
    (horth : ∀ c, 0 ≤ c → c ≤ r → c ≤ w → c = 0) (φ : E →ₚ[ℝ] ℝ) :
    gauge r * w φ ≤ gauge w * (gauge r * φ 1 - r φ)
```

**`Bidual.eq_zero_of_orthogonal`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L368).

> A nonnegative element below `w₁ + w₂` that has no nonzero common lower bound with `w₁` nor with
> `w₂` vanishes.

```lean
lemma eq_zero_of_orthogonal {r w₁ w₂ : Bidual E} (hr : 0 ≤ r) (hw₁ : 0 ≤ w₁) (hw₂ : 0 ≤ w₂)
    (hle : r ≤ w₁ + w₂) (o₁ : ∀ c, 0 ≤ c → c ≤ r → c ≤ w₁ → c = 0)
    (o₂ : ∀ c, 0 ≤ c → c ≤ r → c ≤ w₂ → c = 0) : r = 0
```

**`Bidual.decompositions`**, a def, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L390).

> Pairs of pieces of `u` below `v₁` and `v₂`.

```lean
def decompositions (v₁ v₂ u : Bidual E) : Set (Bidual E × Bidual E)
```

**`Bidual.exists_upperBound_of_isChain`**, a lemma, [line 395](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L395).

> A chain of decompositions has an upper bound among the decompositions: its supremum.

```lean
lemma exists_upperBound_of_isChain {v₁ v₂ u : Bidual E} {C : Set (Bidual E × Bidual E)}
    (hCA : C ⊆ decompositions v₁ v₂ u) (hC : IsChain (· ≤ ·) C) {y : Bidual E × Bidual E}
    (hy : y ∈ C) : ∃ ub ∈ decompositions v₁ v₂ u, ∀ z ∈ C, z ≤ ub
```

**`Bidual.orthogonal_fst_of_maximal`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L420).

> The remainder of a maximal decomposition has no nonzero common lower bound with the room left
> below `v₁`.

```lean
lemma orthogonal_fst_of_maximal {v₁ v₂ u : Bidual E} {p : Bidual E × Bidual E}
    (hp : Maximal (· ∈ decompositions v₁ v₂ u) p) :
    ∀ c, 0 ≤ c → c ≤ u - p.1 - p.2 → c ≤ v₁ - p.1 → c = 0
```

**`Bidual.orthogonal_snd_of_maximal`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L433).

> The remainder of a maximal decomposition has no nonzero common lower bound with the room left
> below `v₂`.

```lean
lemma orthogonal_snd_of_maximal {v₁ v₂ u : Bidual E} {p : Bidual E × Bidual E}
    (hp : Maximal (· ∈ decompositions v₁ v₂ u) p) :
    ∀ c, 0 ≤ c → c ≤ u - p.1 - p.2 → c ≤ v₂ - p.2 → c = 0
```

**`Bidual.hasRieszDecomposition`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L445).

> **Riesz decomposition in the bidual.** When every two effects of the bidual are compatible,
> a maximal decomposition of `u` below `v₁ + v₂` leaves no remainder.

```lean
lemma hasRieszDecomposition : HasRieszDecomposition (Bidual E)
```

## E. Compatibility makes the dual cone a lattice

**`Bidual.ofEPos`**, a def, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L470).

> An observable as a positive map into the bidual.

```lean
def _root_.Bidual.ofEPos : E →ₚ[ℝ] Bidual E
```

**`ProbabilisticTheory.isClassical_of_bidual`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L475).

> If the bidual has Riesz decomposition, the positive functionals on `E` form a lattice: the least
> upper bound in the bidual, restricted to `E`, is the least upper bound.

```lean
lemma isClassical_of_bidual (hF : HasRieszDecomposition (Bidual E)) :
    IsClassical E
```

**`ProbabilisticTheory.isClassical_of_approxJoint`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L492).

> If every two effects have joint effects up to any error, the positive functionals form a
> lattice.

```lean
lemma isClassical_of_approxJoint
    (h : ∀ (e f : Effect E) (δ : ℝ), 0 < δ → ∃ g : E, Effect.IsApproxBinaryJointEffect e f δ g) :
    IsClassical E
```

**`ProbabilisticTheory.isClassical_of_jointlyMeasurable`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L501).

> **Compatibility characterizes classicality (Kuramochi).** If every two yes/no measurements are
> jointly measurable, the positive functionals form a lattice: the state space is a Choquet
> simplex.

```lean
lemma isClassical_of_jointlyMeasurable {F : Type*} [ArchimedeanOrderUnitSpace F]
    (h : ∀ e f : Effect F, Measurement.JointlyMeasurable (Effect.binaryMeasurement e)
      (Effect.binaryMeasurement f)) : IsClassical F
```

## F. The characterization

**`ProbabilisticTheory.IsClassical.exists_isBinaryJointEffect`**, a lemma, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L518).

> On a complete Archimedean order-unit space whose positive functionals form a lattice, every two
> effects have a joint effect.

```lean
lemma IsClassical.exists_isBinaryJointEffect (hF : IsClassical F) (e f : Effect F) :
    ∃ g : F, Effect.IsBinaryJointEffect e f g
```

**`ProbabilisticTheory.isClassical_iff_jointlyMeasurable`**, a lemma, [line 530](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean#L530).

> **Kuramochi's theorem.** On a complete Archimedean order-unit space, the positive functionals
> form a lattice — the state space is a Choquet simplex — exactly when every two yes/no measurements
> are jointly measurable.

```lean
lemma isClassical_iff_jointlyMeasurable :
    IsClassical F ↔ ∀ e f : Effect F,
      Measurement.JointlyMeasurable (Effect.binaryMeasurement e)
        (Effect.binaryMeasurement f)
```

## Depends on

- [Classical systems](basic.md)
- [Compatibility of measurements](../measurement/compatibility.md)
- [The bidual of a system](../orderunit/bidual.md)

## Proof depends on

- [Positive majorants](../../mathematics/part-02/order/positivedual-majorant.md)
- [Interpolation of complete observables](../orderunit/interpolation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Compatibility.lean)
