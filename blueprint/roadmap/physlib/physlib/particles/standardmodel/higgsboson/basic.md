---
declaration: module
origin: cited
lean: StandardModel.HiggsVec.stabilizer_ofReal, StandardModel.HiggsVec, StandardModel.HiggsVec.orthonormBasis, StandardModel.HiggsVec.ofReal, StandardModel.HiggsVec.ofReal_normSq, StandardModel.HiggsVec.repGaugeGroupI, StandardModel.HiggsVec.repGaugeGroupI_apply, StandardModel.HiggsVec.repGaugeGroupI_apply_eq_U1_mul_SU2
statement: formalized
proof: formalized
---

# The Higgs field

The module `Physlib.Particles.StandardModel.HiggsBoson.Basic`, [Physlib/Particles/StandardModel/HiggsBoson/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean): 59 declarations (2 instances with no name), 24 with a docstring, 1 listed as significant.

## i. Overview

> The Higgs field describes is the underlying field of the Higgs boson.
> It is a map from SpaceTime to a 2-dimensional complex vector space.
> In this module we define the Higgs field and prove some basic properties.

## ii. Key results

> - `HiggsVec`: The 2-dimensional complex vector space which is the target space of the Higgs field.
>   This vector space is equipped with an action of the global gauge group of the Standard Model.
> - `HiggsBundle`: The trivial vector bundle over `SpaceTime` with fiber `HiggsVec`.
> - `HiggsField`: The type of smooth sections of the `HiggsBundle`, i.e., the type of Higgs fields.
> - `stabilizer_ofReal`: The stability group of the Higgs vacuum `(0, √a)`, i.e. the gauge
>   group left unbroken by it, is `SU(3) × U(1)_EM`.

## iv. References

> * The particle data group has properties of the Higgs boson Review of Particle Physics, PDG.
>   [ref: ParticleDataGroup:2018ovx]

## A. The Higgs vector space

> The target space of the Higgs field is a 2-dimensional complex vector space.
> In this section we will define this vector space, and the action of the
> global gauge group on it.

### A.1. Definition of the Higgs vector space

**`StandardModel.HiggsVec`**, an abbrev, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L101).

> The vector space `HiggsVec` is defined to be the complex Euclidean space of dimension 2.
> For a given spacetime point a Higgs field gives a value in `HiggsVec`.

```lean
abbrev HiggsVec
```

### A.2. Orthonormal basis

> We define an orthonormal basis of `HiggsVec`.

**`StandardModel.HiggsVec.orthonormBasis`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L114).

> An orthonormal basis of `HiggsVec`.

```lean
def orthonormBasis : OrthonormalBasis (Fin 2) ℂ HiggsVec
```

### A.3. Generating Higgs vectors from real numbers

> Given a real number `a` we define the Higgs vector corresponding to that real number
> as `(0, √a)`. This has the property that its norm-squared is equal to `a`.
> Following the textbook convention, the non-zero entry sits in the second (lower) component,
> which is the electrically neutral component of the Higgs doublet
> (see `GaugeGroupI.electromagnetismU1`).

**`StandardModel.HiggsVec.ofReal`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L131).

> Generating a Higgs vector `(0, √a)` from a real number `a`, such that the norm-squared of
> that Higgs vector is `a`.

```lean
def ofReal (a : ℝ) : HiggsVec
```

**`StandardModel.HiggsVec.ofReal_normSq`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L135).

```lean
lemma ofReal_normSq {a : ℝ} (ha : 0 ≤ a) : ‖ofReal a‖ ^ 2 = a
```

### A.4. Action of the gauge group on `HiggsVec`

> The gauge group of the Standard Model acts on `HiggsVec` by matrix multiplication.

#### A.4.1. Definition of the representation

**`StandardModel.HiggsVec.repGaugeGroupI`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L156).

> The representation of the gauge group `GaugeGroupI` on `HiggsVec`: the `SU(2)`
> factor acts by matrix multiplication, and the `U(1)` factor by scalar
> multiplication with its third power. Hypercharges are normalised as `6Y`, so the
> power `3` corresponds to the textbook hypercharge `Y = 1/2`.

```lean
def repGaugeGroupI : Representation ℂ GaugeGroupI HiggsVec
```

**`StandardModel.HiggsVec.repGaugeGroupI_apply`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L172).

```lean
lemma repGaugeGroupI_apply (g : StandardModel.GaugeGroupI) (φ : HiggsVec) :
    repGaugeGroupI g φ = (WithLp.toLp 2 <| g.toU1 ^ 3 • (g.toSU2.1 *ᵥ φ.ofLp))
```

**`StandardModel.HiggsVec.repGaugeGroupI_apply_eq_U1_mul_SU2`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L175).

```lean
lemma repGaugeGroupI_apply_eq_U1_mul_SU2 (g : StandardModel.GaugeGroupI) (φ : HiggsVec) :
    repGaugeGroupI g φ = (WithLp.toLp 2 <| g.toSU2.1 *ᵥ (g.toU1 ^ 3 • φ.ofLp))
```

**`StandardModel.HiggsVec.repGaugeGroupI_apply_eq_U1_smul_SU2`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L179).

```lean
lemma repGaugeGroupI_apply_eq_U1_smul_SU2 (g : StandardModel.GaugeGroupI) (φ : HiggsVec) :
    repGaugeGroupI g φ = (WithLp.toLp 2 <| (g.toU1 ^ 3 • g.toSU2.1) *ᵥ φ.ofLp)
```

#### A.4.2. Unitary nature of the action

> The action of `StandardModel.GaugeGroupI` on `HiggsVec` is unitary.

**`StandardModel.HiggsVec.repGaugeGroupI_inner`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L194).

```lean
lemma repGaugeGroupI_inner (g : StandardModel.GaugeGroupI) (φ ψ : HiggsVec) :
    ⟪repGaugeGroupI g φ, repGaugeGroupI g ψ⟫_ℂ = ⟪φ, ψ⟫_ℂ
```

**`StandardModel.HiggsVec.repGaugeGroupI_norm`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L203).

```lean
lemma repGaugeGroupI_norm (g : StandardModel.GaugeGroupI) (φ : HiggsVec) :
    ‖repGaugeGroupI g φ‖ = ‖φ‖
```

#### A.4.3. Group properties of the representation applied to vectors

**`StandardModel.HiggsVec.repGaugeGroupI_mul_apply`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L213).

```lean
lemma repGaugeGroupI_mul_apply (g₁ g₂ : StandardModel.GaugeGroupI) (φ : HiggsVec) :
    repGaugeGroupI (g₁ * g₂) φ = repGaugeGroupI g₁ (repGaugeGroupI g₂ φ)
```

**`StandardModel.HiggsVec.repGaugeGroupI_inv_apply_eq_iff`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L217).

```lean
lemma repGaugeGroupI_inv_apply_eq_iff (g : StandardModel.GaugeGroupI) (φ ψ : HiggsVec) :
    repGaugeGroupI g⁻¹ φ = ψ ↔ φ = repGaugeGroupI g ψ
```

### A.5. The Gauge orbit of a Higgs vector

> We show that two Higgs vectors are in the same gauge orbit if and only if they have the same norm.

#### A.5.1. The rotation matrix to ofReal

> We define an element of `GaugeGroupI` which takes a given Higgs vector to the
> corresponding `ofReal` Higgs vector.

**`StandardModel.HiggsVec.toRealGroupElem`**, a def, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L244).

> Given a Higgs vector, a rotation matrix which puts the first component of the
> vector to zero, and the second component to a non-negative real.

```lean
def toRealGroupElem (φ : HiggsVec) : GaugeGroupI
```

**`StandardModel.HiggsVec.toRealGroupElem_apply_self`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L275).

```lean
lemma toRealGroupElem_apply_self (φ : HiggsVec) :
    repGaugeGroupI (toRealGroupElem φ) φ = ofReal (‖φ‖ ^ 2)
```

#### A.5.2. Members of orbits

> Members of the orbit of a Higgs vector under the action of `GaugeGroupI` are exactly those
> Higgs vectors with the same norm.

**`StandardModel.HiggsVec.exists_repGaugeGroupI_eq_iff_norm_eq`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L308).

> Two Higgs vectors are in the same gauge orbit (i.e. related by `repGaugeGroupI`)
> if and only if they have the same norm.

```lean
lemma exists_repGaugeGroupI_eq_iff_norm_eq (φ : HiggsVec) (ψ : HiggsVec) :
    (∃ g : GaugeGroupI, repGaugeGroupI g φ = ψ) ↔ ‖ψ‖ = ‖φ‖
```

### A.6. The stability group of a Higgs vector

> The stability group of a Higgs vector `φ` is the subgroup `repGaugeGroupI.stabilizer φ` of
> `GaugeGroupI` fixing `φ`, i.e. the gauge group left unbroken when the Higgs field takes the
> value `φ`. For the vacuum `ofReal a = (0, √a)` with `a > 0` it is `SU(3) × U(1)_EM`, and for
> any other non-zero Higgs vector it is a conjugate of this subgroup. The subgroup fixing every
> Higgs vector is `SU(3) × ℤ₆`.

**`StandardModel.HiggsVec.mem_stabilizer_ofReal_iff`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L333).

> A gauge transformation fixes the non-zero Higgs vector `ofReal a = (0, √a)` if and only if
> its `SU(2)` part is `diag(u³, ū³)`, where `u` is its `U(1)` part.

```lean
lemma mem_stabilizer_ofReal_iff {a : ℝ} (ha : 0 < a) (g : GaugeGroupI) :
    g ∈ repGaugeGroupI.stabilizer (ofReal a) ↔
    GaugeGroupI.toSU2 g = GaugeGroupI.diagSU2 (GaugeGroupI.toU1 g ^ 3)
```

**`StandardModel.HiggsVec.stabilizer_ofReal`**, a theorem, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L366). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The Higgs vacuum breaks electroweak symmetry down to color and electromagnetism: the
> stability group of the non-zero Higgs vector `ofReal a = (0, √a)` is the subgroup
> `SU(3) × U(1)_EM` of `GaugeGroupI`, with elements `(h, diag(u³, ū³), u)`.

```lean
theorem stabilizer_ofReal {a : ℝ} (ha : 0 < a) :
    repGaugeGroupI.stabilizer (ofReal a) = UnbrokenGaugeGroupI.incl.range
```

**`StandardModel.HiggsVec.exists_stabilizer_eq_conj_unbrokenGaugeGroupI`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L377).

> The stability group of any non-zero Higgs vector is conjugate to `SU(3) × U(1)_EM`.

```lean
lemma exists_stabilizer_eq_conj_unbrokenGaugeGroupI (φ : HiggsVec) (hφ : φ ≠ 0) :
    ∃ g : GaugeGroupI, repGaugeGroupI.stabilizer φ =
      UnbrokenGaugeGroupI.incl.range.map (MulAut.conj g)
```

**`StandardModel.HiggsVec.mem_iInf_stabilizer_iff`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L390).

> The gauge transformations fixing every Higgs vector are those of the form
> `(h, α⁻³ I₂, α)` with `h ∈ SU(3)` arbitrary and `α` a sixth root of unity, i.e. the subgroup
> `SU(3) × ℤ₆` of `GaugeGroupI`. Here `ℤ₆` sits inside `SU(2) × U(1)`: it is the image there of
> the central `ℤ₆` used for `GaugeGroupℤ₆`, whose elements also carry the `SU(3)` part `α² I₃`,
> so this subgroup contains the central `ℤ₆`.

```lean
lemma mem_iInf_stabilizer_iff (g : GaugeGroupI) :
    g ∈ ⨅ φ, repGaugeGroupI.stabilizer φ ↔
    ∃ α : rootsOfUnity 6 ℂ, GaugeGroupI.toSU2 g = gaugeGroupℤ₆SU2OfRoot α ∧
      GaugeGroupI.toU1 g = gaugeGroupℤ₆UnitaryOfRoot α
```

### A.7. The electromagnetic U(1) and the phase of the first component

**`StandardModel.HiggsVec.electromagnetismU1_repGaugeGroupI_apply`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L432).

> The electromagnetic `U(1)` acts on a Higgs vector as `diag(u⁶, 1)`: the upper component
> has electric charge `+1` and the lower component is neutral.

```lean
lemma electromagnetismU1_repGaugeGroupI_apply (g : unitary ℂ) (φ : HiggsVec) :
    repGaugeGroupI (StandardModel.GaugeGroupI.electromagnetismU1 g) φ =
    (WithLp.toLp 2 <| !![g.1 ^ 6, 0; 0, 1] *ᵥ φ.ofLp)
```

**`StandardModel.HiggsVec.electromagnetismU1_repGaugeGroupI_ofReal`**, a lemma, [line 446](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L446).

> The electromagnetic `U(1)` leaves the Higgs vector `ofReal a = (0, √a)` invariant:
> the Higgs vacuum is electrically neutral, so electromagnetism is unbroken.

```lean
lemma electromagnetismU1_repGaugeGroupI_ofReal (g : unitary ℂ) (a : ℝ) :
    repGaugeGroupI (StandardModel.GaugeGroupI.electromagnetismU1 g) (ofReal a) = ofReal a
```

**`StandardModel.HiggsVec.exists_electromagnetismU1_fst_eq_norm`**, a lemma, [line 456](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L456).

> There is an element of the electromagnetic `U(1)` making the first (charged) component of a
> Higgs vector real and non-negative. It fixes second components, and so the Higgs vacuum
> `ofReal a`. This is used to gauge-fix two-Higgs-doublet configurations to
> `Φ1 = (0, ‖Φ1‖)`.

```lean
lemma exists_electromagnetismU1_fst_eq_norm (φ : HiggsVec) :
    ∃ g : unitary ℂ,
      (repGaugeGroupI (StandardModel.GaugeGroupI.electromagnetismU1 g) φ).ofLp 0 = ‖φ.ofLp 0‖
```

### A.8. To real scalars

**`StandardModel.HiggsVec.toRealScalars`**, a def, [line 481](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L481).

> The underlying real values of the Higgs vector.

```lean
def toRealScalars : HiggsVec →ₗ[ℝ] (Fin 4 → ℝ)
```

**`StandardModel.HiggsVec.toRealScalars_smul_real`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L494).

```lean
lemma toRealScalars_smul_real (a : ℝ) (φ : HiggsVec) :
    toRealScalars (a • φ) = a • toRealScalars φ
```

**`StandardModel.HiggsVec.ofReal_toRealScalars`**, a lemma, [line 497](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L497).

```lean
lemma ofReal_toRealScalars (a : ℝ) :
    toRealScalars (ofReal a) = !₄[0, 0, Real.sqrt a, 0]
```

**`StandardModel.HiggsVec.ofReal_toRealScalars_norm`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L502).

```lean
lemma ofReal_toRealScalars_norm (φ : HiggsVec) :
    toRealScalars (ofReal (‖φ‖ ^ 2)) = !₄[0, 0, ‖φ‖, 0]
```

## B. The Higgs bundle

> We define the Higgs bundle as the trivial vector bundle with base `SpaceTime` and fiber `HiggsVec`.
> The Higgs field will then be defined as smooth sections of this bundle.

### B.1. Definition of the Higgs bundle

> We define the Higgs bundle.

**`StandardModel.HiggsBundle`**, an abbrev, [line 528](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L528).

> The `HiggsBundle` is defined as the trivial vector bundle with base `SpaceTime` and
> fiber `HiggsVec`. Thus as a manifold it corresponds to `ℝ⁴ × ℂ²`.

```lean
abbrev HiggsBundle
```

### B.2. Instance of a vector bundle

> We given the Higgs bundle an instance of a smooth vector bundle.

**An instance with no name**, [line 539](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L539).

> The instance of a smooth vector bundle with total space `HiggsBundle` and fiber `HiggsVec`.

```lean
instance : ContMDiffVectorBundle ⊤ HiggsVec HiggsBundle (Lorentz.Vector.asSmoothManifold 3)
```

## C. The Higgs fields

> Higgs fields are smooth sections of the Higgs bundle.
> This corresponds to smooth maps from `SpaceTime` to `HiggsVec`.
> We here define the type of Higgs fields and create an API around them.

**`StandardModel.HiggsField`**, an abbrev, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L556).

> The type `HiggsField` is defined such that elements are smooth sections of the trivial
> vector bundle `HiggsBundle`. Such elements are Higgs fields. Since `HiggsField` is
> trivial as a vector bundle, a Higgs field is equivalent to a smooth map
> from `SpaceTime` to `HiggsVec`.

```lean
abbrev HiggsField : Type
```

### C.1. Relations between `HiggsField` and `HiggsVec`

#### C.1.1. The constant Higgs field

> We define the constant Higgs field associated to a given Higgs vector.

**`StandardModel.HiggsField.const`**, a def, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L578).

> Given a vector in `HiggsVec` the constant Higgs field with value equal to that
> section.

```lean
def const : HiggsVec →ₗ[ℝ] HiggsField
```

**`StandardModel.HiggsField.const_apply`**, a lemma, [line 595](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L595).

> For all spacetime points, the constant Higgs field defined by a Higgs vector,
> returns that Higgs Vector.

```lean
lemma const_apply (φ : HiggsVec) (x : SpaceTime) : const φ x = φ
```

#### C.1.2. The map from `HiggsField` to `SpaceTime → HiggsVec`

**`StandardModel.HiggsField.toHiggsVec`**, a def, [line 604](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L604).

> Given a `HiggsField`, the corresponding map from `SpaceTime` to `HiggsVec`.

```lean
def toHiggsVec (φ : HiggsField) : SpaceTime → HiggsVec
```

**`StandardModel.HiggsField.toHiggsVec_smooth`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L606).

```lean
lemma toHiggsVec_smooth (φ : HiggsField) :
    ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, HiggsVec) ⊤ φ.toHiggsVec
```

**`StandardModel.HiggsField.const_toHiggsVec_apply`**, a lemma, [line 610](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L610).

```lean
lemma const_toHiggsVec_apply (φ : HiggsField) (x : SpaceTime) :
    const (φ.toHiggsVec x) x = φ x
```

### C.2. Smoothness properties of components

> We prove some smoothness properties of the components of a Higgs field.

**`StandardModel.HiggsField.contDiff`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L622).

```lean
lemma contDiff (φ : HiggsField) :
    ContDiff ℝ ⊤ φ
```

**`StandardModel.HiggsField.toVec_smooth`**, a lemma, [line 626](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L626).

```lean
lemma toVec_smooth (φ : HiggsField) :
    ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, EuclideanSpace ℂ (Fin 2)) ⊤ φ
```

**`StandardModel.HiggsField.apply_smooth`**, a lemma, [line 630](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L630).

```lean
lemma apply_smooth (φ : HiggsField) :
    ∀ i, ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, ℂ) ⊤ (fun (x : SpaceTime) => (φ x i))
```

**`StandardModel.HiggsField.apply_re_smooth`**, a lemma, [line 634](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L634).

```lean
lemma apply_re_smooth (φ : HiggsField) (i : Fin 2) :
    ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, ℝ) ⊤ (reCLM ∘ (fun (x : SpaceTime) => (φ x i)))
```

**`StandardModel.HiggsField.apply_im_smooth`**, a lemma, [line 638](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L638).

```lean
lemma apply_im_smooth (φ : HiggsField) (i : Fin 2) :
    ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, ℝ) ⊤ (imCLM ∘ (fun (x : SpaceTime) => (φ x i)))
```

### C.3. The pointwise inner product

> The pointwise inner product on the Higgs field.

**An instance with no name**, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L652).

```lean
instance : Inner (SpaceTime → ℂ) (HiggsField)
```

#### C.3.1. Basic equalities

**`StandardModel.HiggsField.inner_apply`**, a lemma, [line 661](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L661).

```lean
lemma inner_apply (φ1 φ2 : HiggsField) (x : SpaceTime) :
    ⟪φ1, φ2⟫_(SpaceTime → ℂ) x = ⟪φ1 x, φ2 x⟫_ℂ
```

**`StandardModel.HiggsField.inner_eq_expand`**, a lemma, [line 664](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L664).

```lean
lemma inner_eq_expand (φ1 φ2 : HiggsField) :
    ⟪φ1, φ2⟫_(SpaceTime → ℂ) = fun x => equivRealProdCLM.symm (((φ1 x 0).re * (φ2 x 0).re
    + (φ1 x 1).re * (φ2 x 1).re+ (φ1 x 0).im * (φ2 x 0).im + (φ1 x 1).im * (φ2 x 1).im),
    ((φ1 x 0).re * (φ2 x 0).im + (φ1 x 1).re * (φ2 x 1).im
    - (φ1 x 0).im * (φ2 x 0).re - (φ1 x 1).im * (φ2 x 1).re))
```

**`StandardModel.HiggsField.inner_expand_conj`**, a lemma, [line 674](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L674).

> Expands the inner product on Higgs fields in terms of complex components of the
> Higgs fields.

```lean
lemma inner_expand_conj (φ1 φ2 : HiggsField) (x : SpaceTime) :
    ⟪φ1, φ2⟫_(SpaceTime → ℂ) x = conj (φ1 x 0) * φ2 x 0 + conj (φ1 x 1) * φ2 x 1
```

#### C.3.2. Symmetry properties

**`StandardModel.HiggsField.inner_symm`**, a lemma, [line 684](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L684).

```lean
lemma inner_symm (φ1 φ2 : HiggsField) :
    conj ⟪φ2, φ1⟫_(SpaceTime → ℂ) = ⟪φ1, φ2⟫_(SpaceTime → ℂ)
```

#### C.3.3. Linearity conditions

**`StandardModel.HiggsField.inner_add_left`**, a lemma, [line 694](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L694).

```lean
lemma inner_add_left (φ1 φ2 φ3 : HiggsField) :
    ⟪φ1 + φ2, φ3⟫_(SpaceTime → ℂ) = ⟪φ1, φ3⟫_(SpaceTime → ℂ) + ⟪φ2, φ3⟫_(SpaceTime → ℂ)
```

**`StandardModel.HiggsField.inner_add_right`**, a lemma, [line 698](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L698).

```lean
lemma inner_add_right (φ1 φ2 φ3 : HiggsField) :
    ⟪φ1, φ2 + φ3⟫_(SpaceTime → ℂ) = ⟪φ1, φ2⟫_(SpaceTime → ℂ) + ⟪φ1, φ3⟫_(SpaceTime → ℂ)
```

**`StandardModel.HiggsField.inner_zero_left`**, a lemma, [line 703](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L703).

```lean
lemma inner_zero_left (φ : HiggsField) :
    ⟪0, φ⟫_(SpaceTime → ℂ) = 0
```

**`StandardModel.HiggsField.inner_zero_right`**, a lemma, [line 708](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L708).

```lean
lemma inner_zero_right (φ : HiggsField) :
    ⟪φ, 0⟫_(SpaceTime → ℂ) = 0
```

**`StandardModel.HiggsField.inner_neg_left`**, a lemma, [line 712](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L712).

```lean
lemma inner_neg_left (φ1 φ2 : HiggsField) :
    ⟪-φ1, φ2⟫_(SpaceTime → ℂ) = -⟪φ1, φ2⟫_(SpaceTime → ℂ)
```

**`StandardModel.HiggsField.inner_neg_right`**, a lemma, [line 716](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L716).

```lean
lemma inner_neg_right (φ1 φ2 : HiggsField) :
    ⟪φ1, -φ2⟫_(SpaceTime → ℂ) = -⟪φ1, φ2⟫_(SpaceTime → ℂ)
```

#### C.3.4. Smoothness of the inner product

**`StandardModel.HiggsField.inner_smooth`**, a lemma, [line 726](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L726).

```lean
lemma inner_smooth (φ1 φ2 : HiggsField) : ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, ℂ) ⊤
    ⟪φ1, φ2⟫_(SpaceTime → ℂ)
```

### C.4. The pointwise norm

> We define the pointwise norm-squared of a Higgs field.

**`StandardModel.HiggsField.normSq`**, a def, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L745).

> Given an element `φ` of `HiggsField`, `normSq φ` is defined as the
> the function `SpaceTime → ℝ` obtained by taking the square norm of the
> pointwise Higgs vector. In other words, `normSq φ x = ‖φ x‖ ^ 2`.
>
> The notation `‖φ‖_H^2` is used for the `normSq φ`.

```lean
def normSq (φ : HiggsField) : SpaceTime → ℝ
```

#### C.4.1. Basic equalities

**`StandardModel.HiggsField.inner_self_eq_normSq`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L756).

```lean
lemma inner_self_eq_normSq (φ : HiggsField) (x : SpaceTime) :
    ⟪φ, φ⟫_(SpaceTime → ℂ) x = ‖φ‖_H^2 x
```

**`StandardModel.HiggsField.normSq_eq_inner_self_re`**, a lemma, [line 760](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L760).

```lean
lemma normSq_eq_inner_self_re (φ : HiggsField) (x : SpaceTime) :
    φ.normSq x = (⟪φ, φ⟫_(SpaceTime → ℂ) x).re
```

**`StandardModel.HiggsField.normSq_expand`**, a lemma, [line 765](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L765).

> The expansion of the norm squared of into components.

```lean
lemma normSq_expand (φ : HiggsField) :
    φ.normSq = fun x => (conj (φ x 0) * (φ x 0) + conj (φ x 1) * (φ x 1)).re
```

#### C.4.2. Positivity

**`StandardModel.HiggsField.normSq_nonneg`**, a lemma, [line 776](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L776).

```lean
lemma normSq_nonneg (φ : HiggsField) (x : SpaceTime) : 0 ≤ ‖φ‖_H^2 x
```

#### C.4.3. On the zero section

**`StandardModel.HiggsField.normSq_zero`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L785).

```lean
lemma normSq_zero : ‖0‖_H^2 = 0
```

#### C.4.4. Smoothness of the norm-squared

**`StandardModel.HiggsField.normSq_smooth`**, a lemma, [line 796](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L796).

> The norm squared of the Higgs field is a smooth function on space-time.

```lean
lemma normSq_smooth (φ : HiggsField) : ContMDiff 𝓘(ℝ, SpaceTime) 𝓘(ℝ, ℝ) ⊤ φ.normSq
```

#### C.4.5. Norm-squared of constant Higgs fields

**`StandardModel.HiggsField.const_normSq`**, a lemma, [line 807](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean#L807).

```lean
lemma const_normSq (φ : HiggsVec) (x : SpaceTime) :
    ‖const φ‖_H^2 x = ‖φ‖ ^ 2
```

### C.5. The action of the gauge group on Higgs fields

> The results in this section are currently informal.

## Depends on

- [The unbroken gauge group](../gaugegroup/unbroken.md)
- [Spacetime](../../../spaceandtime/spacetime/basic.md)

## Sources

- [Physlib/Particles/StandardModel/HiggsBoson/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/HiggsBoson/Basic.lean)
