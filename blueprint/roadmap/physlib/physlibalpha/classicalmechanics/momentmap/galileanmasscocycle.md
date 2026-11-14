---
declaration: module
origin: cited
lean: ClassicalMechanics.ofLp_orthogonal_smul, ClassicalMechanics.ofLp_real_smul, ClassicalMechanics.orthogonal_transpose_mul_self, ClassicalMechanics.orthogonal_mul_transpose_self, ClassicalMechanics.orthogonal_inv_val, ClassicalMechanics.orthogonal_det_mul_self, ClassicalMechanics.orthogonal_det_inv, ClassicalMechanics.orthogonal_mulVec_dotProduct
statement: formalized
proof: formalized
---

# The mass cocycle of the Galilean group (Souriau)

The module `PhyslibAlpha.ClassicalMechanics.MomentMap.GalileanMassCocycle`, [PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean): 59 declarations (9 instances with no name), 52 with a docstring; 3 private, not shown.

> Souriau's mass cocycle of the Galilean group is a cocycle but not a coboundary.

## i. Overview

> This file is the group level of `PhyslibAlpha.ClassicalMechanics.MomentMap.GalileanMass`, which
> treats chapter 12 of Souriau's Structure des systèmes dynamiques (Dunod 1970) at the level of the
> Lie algebra. The group is Physlib's `GalileanGroup 3` (`Physlib.SpaceAndTime.GalileanGroup.Basic`),
> `a = (R, b, c, e)` (rotation, velocity, space translation, time translation), whose action
> `(t, x) ↦ (t + e, R x + b t + c)` is Souriau's (12.76); `EvolutionSpace.smul_time_position` shows
> that the action on the evolution space below is that action on each material point.
>
> For `N` free material points, the file defines the action of the group on the evolution space
> (12.76), the adjoint action on the Lie algebra (6.24) in components, and the coadjoint action on
> the torsors (11.15). It proves that the group preserves the Lagrange form (12.76), that the
> adjoint action satisfies (6.25), and that the moment of the free points is equivariant up to the
> total mass times Souriau's cocycle `θ₀(a) = {c × b, c - b e, b, ½ ‖b‖²}` (12.126)-(12.127).
> `θ₀` is a 1-cocycle (12.128) and is not a coboundary, on Souriau's group (`det R = 1`) as on the
> whole group (p. 151), so the class of the system is not zero for a non-zero total mass (12.136);
> its derivative at the identity is the 2-cocycle `f₀` of `GalileanMass` (12.130).
>
> The rotation part of `GalileanGroup` ranges over `O(3)`, whereas Souriau's (12.73) takes it in
> `SO(3)`. The rotation vector `ω`, an axial vector, is then transformed with the factor `det R`
> (`orthogonal_mulVec_cross`). The identities proved for all `a` ((12.76), (12.77), (6.25), (11.15),
> (12.126)-(12.128)) restrict to Souriau's group `properGalileanGroup`, where `det R = 1` and the
> factor disappears. A negative statement does not restrict: a cocycle that is not a coboundary of
> the larger group could be one of the smaller, so the statements of p. 151 and (12.136) are also
> proved on `properGalileanGroup`. The adjoint and coadjoint actions in components are not printed
> in chapter 12; they are computed here from (6.24), (6.28) and (11.15).
>
> The cohomology vocabulary is Mathlib's: `θ₀` is a `groupCohomology.IsCocycle₁` for the coadjoint
> action, which is (11.19 ♡), and "the class is not zero" is `¬ groupCohomology.IsCoboundary₁`,
> which is (11.19 ◇). As in `PhyslibAlpha.ClassicalMechanics.MomentMap.Cohomology`, Souriau's
> requirement that a cocycle be differentiable is not part of these definitions. This does not
> weaken the non-coboundary statements: a coboundary `a ↦ a • μ₀ - μ₀` of (11.19 ◇) is polynomial in
> the entries of `a`, hence differentiable.
>
> What is not formalised here:
> - the identification of the law of `GalileanGroup` with the product of the matrices (12.73) (it
>   was checked numerically outside Lean);
> - the identification of the adjoint action in components with the conjugation `a Z a⁻¹` (6.28) of
>   the matrices (12.73), (12.74); it is characterised instead by (6.25), `vectorField_smul`,
>   together with the injectivity of `Z ↦ Z_V` for `N ≥ 1`, `vectorField_injective`;
> - that the vector field `Z_V` (12.119), taken as printed in `GalileanMass`, is the derivative at
>   the identity of the action in the direction `Z` (6.11); the characterisation of the adjoint
>   action by (6.25) rests on this printed formula;
> - the Lie group structure (12.75) and any manifold: the derivative (12.130) is taken along curves;
> - that `θ₀` is a symplectic cocycle (11.30), the dimension `1` of (12.131), forces, and the second
>   half of (12.136) (Hamilton's Lagrangian is not invariant);
> - (12.126) is printed for one point of unit mass; here it is proved for `N` points and the moment
>   of `GalileanMass`, whose additive constant is zero.

## ii. Key results

> - `EvolutionSpace.lagrangeForm_smul`: (12.76), the group preserves the Lagrange form.
> - `EvolutionSpace.vectorField_smul`: (6.25), `(a • Z)_V(a • y) = D(a_V)(y)(Z_V(y))`.
> - `GalileanTorsor.coadjoint_pair`: (11.15), `(a • μ)(Z) = μ(a⁻¹ • Z)`.
> - `EvolutionSpace.moment_smul_sub`: (12.126)-(12.127), `μ(a • y) - a • μ(y) = m θ₀(a)`.
> - `isCocycle₁_massCocycle`: (12.128); `isCocycle₁_massCocycle_proper` on Souriau's group.
> - `isCoboundary₁_smul_massCocycle_proper_iff`, `not_isCoboundary₁_massCocycle_proper`: p. 151 on
>   Souriau's group `properGalileanGroup`, `M θ₀` is a coboundary if and only if `M = 0`;
>   `isCoboundary₁_smul_massCocycle_iff`, `not_isCoboundary₁_massCocycle`: the same on the whole
>   group.
> - `EvolutionSpace.not_isCoboundary₁_moment_smul_sub_proper`: (12.136) at the level of Souriau's
>   group; `EvolutionSpace.not_isCoboundary₁_moment_smul_sub` on the whole group.
> - `hasDerivAt_massCocycle`: (12.130), `f₀ = D(θ₀)(e)`.

## iv. References

> - J.-M. Souriau, Structure des systèmes dynamiques, Dunod, Paris, 1970: pp. 139-140
>   (12.73)-(12.77), p. 151 (12.126)-(12.130), pp. 152-153 (12.132)-(12.136); pp. 52-53 (6.24),
>   (6.25), (6.28); p. 108 (11.15), p. 109 (11.17), p. 111 (the order of the arguments of the
>   derivative of a cocycle), p. 112 (11.19), p. 113 (11.22 b).
>
> * J.-M. Souriau, *Structure des systèmes dynamiques*, Maîtrises de mathématiques, Dunod,
>   Paris, 1970, chapters 6, 11 and 12. The equation numbers refer to this edition.
>   [ref: Souriau1970]

## A. Orthogonal matrices and the cross product

**`ClassicalMechanics.ofLp_orthogonal_smul`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L125).

> On coordinates, the action of `O(3)` on `EuclideanSpace ℝ (Fin 3)` is the matrix product.

```lean
lemma ofLp_orthogonal_smul (v : EuclideanSpace ℝ (Fin 3)) :
    WithLp.ofLp (R • v) = R.1 *ᵥ WithLp.ofLp v
```

**`ClassicalMechanics.ofLp_real_smul`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L130).

> On coordinates, the real scalar multiplication of `EuclideanSpace ℝ (Fin 3)`. Stated apart
> from `WithLp.ofLp_smul`, which would also rewrite the action of `O(3)`.

```lean
lemma ofLp_real_smul (k : ℝ) (v : EuclideanSpace ℝ (Fin 3)) :
    WithLp.ofLp (k • v) = k • WithLp.ofLp v
```

**`ClassicalMechanics.orthogonal_transpose_mul_self`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L134).

> An orthogonal matrix satisfies `Rᵀ R = 1`.

```lean
lemma orthogonal_transpose_mul_self : R.1ᵀ * R.1 = 1
```

**`ClassicalMechanics.orthogonal_mul_transpose_self`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L140).

> An orthogonal matrix satisfies `R Rᵀ = 1`.

```lean
lemma orthogonal_mul_transpose_self : R.1 * R.1ᵀ = 1
```

**`ClassicalMechanics.orthogonal_inv_val`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L146).

> The inverse of an orthogonal matrix is its transpose.

```lean
lemma orthogonal_inv_val : (R⁻¹).1 = R.1ᵀ
```

**`ClassicalMechanics.orthogonal_det_mul_self`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L153).

> The determinant of an orthogonal matrix is `1` or `-1`: its square is `1`.

```lean
lemma orthogonal_det_mul_self : R.1.det * R.1.det = 1
```

**`ClassicalMechanics.orthogonal_det_inv`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L158).

> The inverse of an orthogonal matrix has the same determinant.

```lean
lemma orthogonal_det_inv : (R⁻¹).1.det = R.1.det
```

**`ClassicalMechanics.orthogonal_mulVec_dotProduct`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L162).

> An orthogonal matrix preserves the dot product.

```lean
lemma orthogonal_mulVec_dotProduct (u v : ℝ³) : (R.1 *ᵥ u) ⬝ᵥ (R.1 *ᵥ v) = u ⬝ᵥ v
```

**`ClassicalMechanics.dotProduct_transpose_mulVec`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L167).

> Moving an orthogonal matrix to the other side of a dot product: `⟨x, Rᵀ y⟩ = ⟨R x, y⟩`.

```lean
lemma dotProduct_transpose_mulVec (x y : ℝ³) : x ⬝ᵥ (R.1ᵀ *ᵥ y) = (R.1 *ᵥ x) ⬝ᵥ y
```

**`ClassicalMechanics.orthogonal_adjugate`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L180).

> The adjugate of an orthogonal matrix is `det R • Rᵀ`.

```lean
lemma orthogonal_adjugate : adjugate R.1 = R.1.det • R.1ᵀ
```

**`ClassicalMechanics.orthogonal_mulVec_cross`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L188).

> An orthogonal matrix maps the cross product to `det R` times the cross product of the images:
> `R (u × v) = det R • (R u × R v)`. A rotation (`det R = 1`) preserves the cross product.

```lean
lemma orthogonal_mulVec_cross (u v : ℝ³) :
    R.1 *ᵥ (u ⨯₃ v) = R.1.det • ((R.1 *ᵥ u) ⨯₃ (R.1 *ᵥ v))
```

**`ClassicalMechanics.orthogonal_transpose_mulVec_cross`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L194).

> The same for the transpose: `Rᵀ (u × v) = det R • (Rᵀ u × Rᵀ v)`.

```lean
lemma orthogonal_transpose_mulVec_cross (u v : ℝ³) :
    R.1ᵀ *ᵥ (u ⨯₃ v) = R.1.det • ((R.1ᵀ *ᵥ u) ⨯₃ (R.1ᵀ *ᵥ v))
```

**`ClassicalMechanics.cross_dotProduct_det_smul_transpose_mulVec`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L200).

> `⟨u × v, det R • Rᵀ w⟩ = ⟨R u × R v, w⟩`: the angular momentum paired with an axial vector.

```lean
lemma cross_dotProduct_det_smul_transpose_mulVec (u v w : ℝ³) :
    (u ⨯₃ v) ⬝ᵥ (R.1.det • (R.1ᵀ *ᵥ w)) = ((R.1 *ᵥ u) ⨯₃ (R.1 *ᵥ v)) ⬝ᵥ w
```

## B. The action on the evolution space

**An instance with no name**, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L220).

> The action (12.76) of the Galilean group on the evolution space of `N` material points,
> `t* = t + e`, `r_j* = R r_j + b t + c`, `v_j* = R v_j + b`, for
> `a = (R, b, c, e)` (rotation, velocity, space translation, time translation).

```lean
instance : SMul (GalileanGroup 3) (EvolutionSpace N)
```

**`ClassicalMechanics.EvolutionSpace.smul_t`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L227).

```lean
lemma smul_t (a : GalileanGroup 3) (y : EvolutionSpace N) :
    (a • y).t = y.t + a.timeTranslation.val
```

**`ClassicalMechanics.EvolutionSpace.smul_r`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L231).

```lean
lemma smul_r (a : GalileanGroup 3) (y : EvolutionSpace N) (j : Fin N) :
    (a • y).r j = a.rotation.1 *ᵥ y.r j + y.t • WithLp.ofLp a.velocity
      + WithLp.ofLp a.spaceTranslation
```

**`ClassicalMechanics.EvolutionSpace.smul_v`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L236).

```lean
lemma smul_v (a : GalileanGroup 3) (y : EvolutionSpace N) (j : Fin N) :
    (a • y).v j = a.rotation.1 *ᵥ y.v j + WithLp.ofLp a.velocity
```

**An instance with no name**, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L240).

> The Galilean group acts on the evolution space (12.77).

```lean
instance : MulAction (GalileanGroup 3) (EvolutionSpace N)
```

**`ClassicalMechanics.EvolutionSpace.tangentSMul`**, a def, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L265).

> The differential of the affine map `y ↦ a • y`, applied to a tangent vector `dy`:
> `(dt, R dr_j + b dt, R dv_j)`.

```lean
def tangentSMul (a : GalileanGroup 3) (dy : EvolutionSpace N) : EvolutionSpace N
```

**`ClassicalMechanics.EvolutionSpace.smul_line`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L271).

> The action is affine with linear part `tangentSMul a`: it maps the line `s ↦ y + s dy` to the
> line `s ↦ a • y + s (tangentSMul a dy)`.

```lean
lemma smul_line (a : GalileanGroup 3) (y dy : EvolutionSpace N) (s : ℝ) :
    a • line y dy s = line (a • y) (tangentSMul a dy) s
```

**`ClassicalMechanics.EvolutionSpace.smul_time_position`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L286).

> On each material point, the action is Physlib's action of the Galilean group on
> `Time × Space 3`: the time and the position of the `j`th point of `a • y` are the images of those
> of `y`.

```lean
lemma smul_time_position (a : GalileanGroup 3) (y : EvolutionSpace N) (j : Fin N) :
    a • ((⟨y.t⟩ : Time), Space.vectorToSpace (WithLp.toLp 2 (y.r j)))
      = ((⟨(a • y).t⟩ : Time), Space.vectorToSpace (WithLp.toLp 2 ((a • y).r j)))
```

**`ClassicalMechanics.EvolutionSpace.lagrangeForm_smul`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L297).

> (12.76 ♣): the Galilean group preserves the Lagrange form of free material points,
> `σ(a • y)(a dy)(a δy) = σ(y)(dy)(δy)`.

```lean
lemma lagrangeForm_smul (m : Fin N → ℝ) (a : GalileanGroup 3) (y dy δy : EvolutionSpace N) :
    lagrangeForm m (a • y) (tangentSMul a dy) (tangentSMul a δy) = lagrangeForm m y dy δy
```

## C. The adjoint action

**An instance with no name**, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L324).

> The adjoint action (6.24) of the Galilean group on its Lie algebra, in components: with
> `ω* = det R • R ω`, `a • (ω, β, γ, ε) = (ω*, R β - ω* × b, R γ + ε b - e R β - ω* × (c - e b), ε)`.
> It is the conjugation `Z ↦ a Z a⁻¹` (6.28) of the matrices (12.73), (12.74) with `R` taken in
> `O(3)`; this identification is not proved here, the action is characterised by (6.25)
> (`EvolutionSpace.vectorField_smul`). The factor `det R` is `1` for a rotation; it makes `ω` an
> axial vector under reflections.

```lean
instance : SMul (GalileanGroup 3) GalileanAlgebra
```

**`ClassicalMechanics.GalileanAlgebra.smul_ω`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L334).

```lean
lemma smul_ω (a : GalileanGroup 3) (Z : GalileanAlgebra) :
    (a • Z).ω = a.rotation.1.det • (a.rotation.1 *ᵥ Z.ω)
```

**`ClassicalMechanics.GalileanAlgebra.smul_β`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L338).

```lean
lemma smul_β (a : GalileanGroup 3) (Z : GalileanAlgebra) :
    (a • Z).β = a.rotation.1 *ᵥ Z.β
      - (a.rotation.1.det • (a.rotation.1 *ᵥ Z.ω)) ⨯₃ WithLp.ofLp a.velocity
```

**`ClassicalMechanics.GalileanAlgebra.smul_γ`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L343).

```lean
lemma smul_γ (a : GalileanGroup 3) (Z : GalileanAlgebra) :
    (a • Z).γ = a.rotation.1 *ᵥ Z.γ + Z.ε • WithLp.ofLp a.velocity
      - a.timeTranslation.val • (a.rotation.1 *ᵥ Z.β)
      - (a.rotation.1.det • (a.rotation.1 *ᵥ Z.ω)) ⨯₃
        (WithLp.ofLp a.spaceTranslation - a.timeTranslation.val • WithLp.ofLp a.velocity)
```

**`ClassicalMechanics.GalileanAlgebra.smul_ε`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L350).

```lean
lemma smul_ε (a : GalileanGroup 3) (Z : GalileanAlgebra) : (a • Z).ε = Z.ε
```

**An instance with no name**, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L353).

> The adjoint action is an action of the Galilean group on its Lie algebra.

```lean
instance : MulAction (GalileanGroup 3) GalileanAlgebra
```

**`ClassicalMechanics.GalileanAlgebra.inv_smul_eq`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L376).

> The adjoint action of `a⁻¹` in closed form:
> `a⁻¹ • Z = (det R • Rᵀ ω, Rᵀ (β + ω × b), Rᵀ (γ - ε b + e β + ω × c), ε)`.

```lean
lemma inv_smul_eq (a : GalileanGroup 3) (Z : GalileanAlgebra) :
    a⁻¹ • Z = ⟨a.rotation.1.det • (a.rotation.1ᵀ *ᵥ Z.ω),
      a.rotation.1ᵀ *ᵥ (Z.β + Z.ω ⨯₃ WithLp.ofLp a.velocity),
      a.rotation.1ᵀ *ᵥ (Z.γ - Z.ε • WithLp.ofLp a.velocity + a.timeTranslation.val • Z.β
        + Z.ω ⨯₃ WithLp.ofLp a.spaceTranslation), Z.ε⟩
```

**`ClassicalMechanics.EvolutionSpace.vectorField_smul`**, a lemma, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L405).

> (6.25): the vector field of `a • Z` at `a • y` is the image of the vector field of `Z` at `y`,
> `(a • Z)_V(a • y) = D(a_V)(y)(Z_V(y))`.

```lean
lemma vectorField_smul (a : GalileanGroup 3) (Z : GalileanAlgebra) (y : EvolutionSpace N) :
    vectorField (a • Z) (a • y) = tangentSMul a (vectorField Z y)
```

**`ClassicalMechanics.EvolutionSpace.vectorField_injective`**, a lemma, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L421).

> For `N ≥ 1` the map `Z ↦ Z_V` is injective, so (6.25) characterises the adjoint action.

```lean
lemma vectorField_injective [NeZero N] {Z Z' : GalileanAlgebra}
    (h : ∀ y : EvolutionSpace N, vectorField Z y = vectorField Z' y) : Z = Z'
```

## D. Torsors and the coadjoint action

**`ClassicalMechanics.GalileanTorsor.equivProd`**, a def, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L457).

> The torsors as `ℝ³ × ℝ³ × ℝ³ × ℝ`, to transfer the vector space structure.

```lean
def equivProd : GalileanTorsor ≃ ℝ³ × ℝ³ × ℝ³ × ℝ
```

**An instance with no name**, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L464).

> The torsors form an additive group, component by component.

```lean
instance : AddCommGroup GalileanTorsor
```

**An instance with no name**, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L467).

> The torsors form a real vector space, component by component.

```lean
instance : Module ℝ GalileanTorsor
```

**`ClassicalMechanics.GalileanTorsor.pair_add`**, a lemma, [line 470](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L470).

> The pairing is additive in the torsor.

```lean
lemma pair_add (μ ν : GalileanTorsor) (Z : GalileanAlgebra) :
    (μ + ν).pair Z = μ.pair Z + ν.pair Z
```

**`ClassicalMechanics.GalileanTorsor.pair_sub`**, a lemma, [line 477](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L477).

> The pairing is additive in the torsor: subtraction.

```lean
lemma pair_sub (μ ν : GalileanTorsor) (Z : GalileanAlgebra) :
    (μ - ν).pair Z = μ.pair Z - ν.pair Z
```

**`ClassicalMechanics.GalileanTorsor.pair_zero`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L484).

> The zero torsor pairs to zero.

```lean
lemma pair_zero (Z : GalileanAlgebra) : (0 : GalileanTorsor).pair Z = 0
```

**`ClassicalMechanics.GalileanTorsor.pair_smul`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L489).

> The pairing is linear in the torsor.

```lean
lemma pair_smul (k : ℝ) (μ : GalileanTorsor) (Z : GalileanAlgebra) :
    (k • μ).pair Z = k * μ.pair Z
```

**`ClassicalMechanics.GalileanTorsor.ext_pair`**, a lemma, [line 496](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L496).

> A torsor is determined by its values on the Lie algebra.

```lean
lemma ext_pair {μ ν : GalileanTorsor} (h : ∀ Z, μ.pair Z = ν.pair Z) : μ = ν
```

**An instance with no name**, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L509).

> The coadjoint action (11.15) of the Galilean group on the torsors, in closed form:
> `a • {l, g, p, E} = {det R • R l - b × R g + c × R p, R g - e R p, R p, E + ⟨R p, b⟩}`.
> It is characterised by `(a • μ)(Z) = μ(a⁻¹ • Z)` (`coadjoint_pair`).

```lean
instance : SMul (GalileanGroup 3) GalileanTorsor
```

**`ClassicalMechanics.GalileanTorsor.coadjoint_pair`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L517).

> (11.15): `(a • μ)(Z) = μ(a⁻¹ • Z)`.

```lean
lemma coadjoint_pair (a : GalileanGroup 3) (μ : GalileanTorsor) (Z : GalileanAlgebra) :
    (a • μ).pair Z = μ.pair (a⁻¹ • Z)
```

**An instance with no name**, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L542).

> The coadjoint action is an action of the Galilean group on the torsors.

```lean
instance : MulAction (GalileanGroup 3) GalileanTorsor
```

**An instance with no name**, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L548).

> The coadjoint action is additive; it is linear by `coadjoint_smul_real`.

```lean
instance : DistribMulAction (GalileanGroup 3) GalileanTorsor
```

**`ClassicalMechanics.GalileanTorsor.coadjoint_smul_real`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L555).

> The coadjoint action commutes with the real scalar multiplication: it is a linear
> representation, as in (11.14)-(11.15).

```lean
lemma coadjoint_smul_real (a : GalileanGroup 3) (k : ℝ) (μ : GalileanTorsor) :
    a • (k • μ) = k • (a • μ)
```

## E. The cocycle `θ₀` and the mass

**`ClassicalMechanics.massCocycle`**, a def, [line 569](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L569).

> Souriau's cocycle `θ₀(a) = {c × b, c - b e, b, ½ ‖b‖²}` of the Galilean group (12.127), for
> `a = (R, b, c, e)`.

```lean
def massCocycle (a : GalileanGroup 3) : GalileanTorsor
```

**`ClassicalMechanics.massCocycle_one`**, a lemma, [line 575](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L575).

> `θ₀(1) = 0`.

```lean
lemma massCocycle_one : massCocycle 1 = 0
```

**`ClassicalMechanics.isCocycle₁_massCocycle`**, a lemma, [line 584](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L584).

> (12.128): `θ₀` satisfies the cocycle identity (11.19 ♡) for the coadjoint action,
> `θ₀(a a') = a • θ₀(a') + θ₀(a)` (`groupCohomology.IsCocycle₁`). The differentiability also
> required by (11.19) is not part of this statement.

```lean
lemma isCocycle₁_massCocycle : groupCohomology.IsCocycle₁ massCocycle
```

**`ClassicalMechanics.eq_zero_of_smul_massCocycle_boost`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L623).

> The witness of p. 151: if `a • μ₀ - μ₀ = M θ₀(a)` for the pure boost `a = (1, e₁, 0, 0)`,
> then `M = 0`. This boost has `R = 1`, so it lies in Souriau's group `properGalileanGroup`.

```lean
lemma eq_zero_of_smul_massCocycle_boost (M : ℝ) (μ₀ : GalileanTorsor)
    (h : (⟨1, WithLp.toLp 2 ![1, 0, 0], 0, 0⟩ : GalileanGroup 3) • μ₀ - μ₀
      = M • massCocycle ⟨1, WithLp.toLp 2 ![1, 0, 0], 0, 0⟩) : M = 0
```

**`ClassicalMechanics.isCoboundary₁_smul_massCocycle_iff`**, a lemma, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L641).

> `M θ₀` is a coboundary of Physlib's Galilean group (rotations in `O(3)`),
> `M θ₀(a) = a • μ₀ - μ₀` for some torsor `μ₀` (11.19 ◇), if and only if `M = 0`. For Souriau's
> group (12.73) see `isCoboundary₁_smul_massCocycle_proper_iff`, which this lemma does not
> imply.

```lean
lemma isCoboundary₁_smul_massCocycle_iff (M : ℝ) :
    groupCohomology.IsCoboundary₁ (fun a : GalileanGroup 3 => M • massCocycle a) ↔ M = 0
```

**`ClassicalMechanics.not_isCoboundary₁_massCocycle`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L652).

> `θ₀` is not a coboundary of Physlib's Galilean group (rotations in `O(3)`). Souriau's
> statement (p. 151) is on his group (12.73) and is `not_isCoboundary₁_massCocycle_proper`; it is
> not implied by this one.

```lean
lemma not_isCoboundary₁_massCocycle : ¬ groupCohomology.IsCoboundary₁ massCocycle
```

**`ClassicalMechanics.properGalileanGroup`**, a def, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L659).

> Souriau's Galilean group (12.73): the elements of `GalileanGroup 3` whose rotation part has
> determinant `1`, that is `R ∈ SO(3)`.

```lean
def properGalileanGroup : Subgroup (GalileanGroup 3)
```

**`ClassicalMechanics.isCocycle₁_massCocycle_proper`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L676).

> (12.128) on Souriau's group (12.73): the restriction of `θ₀` to `properGalileanGroup` satisfies
> the cocycle identity (11.19 ♡).

```lean
lemma isCocycle₁_massCocycle_proper :
    groupCohomology.IsCocycle₁ (fun a : properGalileanGroup => massCocycle a)
```

**`ClassicalMechanics.isCoboundary₁_smul_massCocycle_proper_iff`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L682).

> p. 151 on Souriau's group (12.73): `M θ₀` is a coboundary of `properGalileanGroup`,
> `M θ₀(a) = a • μ₀ - μ₀` for some torsor `μ₀` (11.19 ◇), if and only if `M = 0`.

```lean
lemma isCoboundary₁_smul_massCocycle_proper_iff (M : ℝ) :
    groupCohomology.IsCoboundary₁ (fun a : properGalileanGroup => M • massCocycle a) ↔
      M = 0
```

**`ClassicalMechanics.not_isCoboundary₁_massCocycle_proper`**, a lemma, [line 696](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L696).

> p. 151 on Souriau's group (12.73): `θ₀` is not a coboundary of `properGalileanGroup`, so it
> defines a non-zero cohomology class of Souriau's Galilean group.

```lean
lemma not_isCoboundary₁_massCocycle_proper :
    ¬ groupCohomology.IsCoboundary₁ (fun a : properGalileanGroup => massCocycle a)
```

**`ClassicalMechanics.EvolutionSpace.moment_smul_sub`**, a lemma, [line 709](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L709).

> (12.126)-(12.127) for `N` points: with the moment of `GalileanMass` (additive constant zero)
> and `m = Σ_j m_j` (12.135), `μ(a • y) - a • μ(y) = m θ₀(a)`, independently of `y`. Souriau
> prints (12.126) for one point of unit mass; for `N` points this is (12.132) with `μ₀ = 0`.

```lean
lemma moment_smul_sub (m : Fin N → ℝ) (a : GalileanGroup 3) (y : EvolutionSpace N) :
    moment m (a • y) - a • moment m y = totalMass m • massCocycle a
```

**`ClassicalMechanics.EvolutionSpace.not_isCoboundary₁_moment_smul_sub`**, a lemma, [line 736](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L736).

> (12.132) and (12.136) at the level of the group, on Physlib's Galilean group (rotations in
> `O(3)`): for a non-zero total mass, the cocycle `a ↦ μ(a • y) - a • μ(y)` of the system is not a
> coboundary. For Souriau's group (12.73) see `not_isCoboundary₁_moment_smul_sub_proper`, which this
> lemma does not imply.

```lean
lemma not_isCoboundary₁_moment_smul_sub (m : Fin N → ℝ) (hM : totalMass m ≠ 0)
    (y : EvolutionSpace N) :
    ¬ groupCohomology.IsCoboundary₁
      (fun a : GalileanGroup 3 => moment m (a • y) - a • moment m y)
```

**`ClassicalMechanics.EvolutionSpace.not_isCoboundary₁_moment_smul_sub_proper`**, a lemma, [line 747](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L747).

> (12.132) and (12.136) at the level of the group, on Souriau's group (12.73): for a non-zero
> total mass, the cocycle `a ↦ μ(a • y) - a • μ(y)` of the system, restricted to
> `properGalileanGroup`, is not a coboundary.

```lean
lemma not_isCoboundary₁_moment_smul_sub_proper (m : Fin N → ℝ) (hM : totalMass m ≠ 0)
    (y : EvolutionSpace N) :
    ¬ groupCohomology.IsCoboundary₁
      (fun a : properGalileanGroup => moment m (a • y) - a • moment m y)
```

## F. The derivative of `θ₀` at the identity

**`ClassicalMechanics.hasDerivAt_massCocycle`**, a lemma, [line 798](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L798).

> (12.130), `f₀ = D(θ₀)(e)`: along a curve `s ↦ γ s` of the Galilean group through the identity
> whose velocity, space translation and time translation are differentiable at `0`, with derivatives
> `b'`, `c'` and `e'`, the derivative at `0` of `s ↦ θ₀(γ s)(Z)` is `f₀(Z')(Z)` with
> `Z' = (0, b', c', 0)`. It depends neither on the rotation part of the curve nor on `e'`.

```lean
lemma hasDerivAt_massCocycle (γ : ℝ → GalileanGroup 3) (hγ : γ 0 = 1)
    {b' c' : EuclideanSpace ℝ (Fin 3)} {e' : ℝ} (hb : HasDerivAt (fun s => (γ s).velocity) b' 0)
    (hc : HasDerivAt (fun s => (γ s).spaceTranslation) c' 0)
    (he : HasDerivAt (fun s => (γ s).timeTranslation.val) e' 0) (Z : GalileanAlgebra) :
    HasDerivAt (fun s => (massCocycle (γ s)).pair Z)
      (GalileanAlgebra.cocycle ⟨0, WithLp.ofLp b', WithLp.ofLp c', 0⟩ Z) 0
```

**`ClassicalMechanics.hasDerivAt_massCocycle_line`**, a lemma, [line 823](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean#L823).

> (12.130) along the curve `s ↦ (1, s b', s c', s e')`, which satisfies the hypotheses of
> `hasDerivAt_massCocycle`.

```lean
lemma hasDerivAt_massCocycle_line (b' c' : EuclideanSpace ℝ (Fin 3)) (e' : ℝ)
    (Z : GalileanAlgebra) :
    HasDerivAt (fun s : ℝ => (massCocycle ⟨1, s • b', s • c', ⟨s * e'⟩⟩).pair Z)
      (GalileanAlgebra.cocycle ⟨0, WithLp.ofLp b', WithLp.ofLp c', 0⟩ Z) 0
```

## Depends on

- [The Galilean group](../../../physlib/spaceandtime/galileangroup/basic.md)
- [The mass as a cohomology class of the Galilean Lie algebra (Souriau)](galileanmass.md)

## Sources

- [PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMassCocycle.lean)
