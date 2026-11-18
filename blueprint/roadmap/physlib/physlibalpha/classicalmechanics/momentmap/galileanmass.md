---
declaration: module
origin: cited
lean: ClassicalMechanics.GalileanAlgebra, ClassicalMechanics.GalileanAlgebra.bracket, ClassicalMechanics.GalileanAlgebra.bracket_antisymm, ClassicalMechanics.GalileanAlgebra.bracket_jacobi, ClassicalMechanics.GalileanAlgebra.bracket_boost_translation, ClassicalMechanics.GalileanTorsor, ClassicalMechanics.GalileanTorsor.pair, ClassicalMechanics.GalileanAlgebra.cocycle
statement: formalized
proof: formalized
---

# The mass as a cohomology class of the Galilean Lie algebra (Souriau)

The module `PhyslibAlpha.ClassicalMechanics.MomentMap.GalileanMass`, [PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean): 35 declarations (3 instances with no name), 32 with a docstring; 2 private, not shown.

> The total mass as a non-trivial cohomology class of the Galilean Lie algebra (Souriau).

## i. Overview

> In chapter 12 of Structure des systèmes dynamiques (Dunod 1970), Souriau computes the moment of
> the Galilean group acting on the evolution space of a system of material points. The moment is a
> torsor `μ = {l, g, p, E}` (12.122)-(12.123): `l` is the angular momentum and `p` the momentum
> (12.140), and `g = m R - p t` with `R` the centre of gravity (12.141). The Lagrange form `σ` of the
> system satisfies (12.134), `σ(Z_V(y))(Z'_V(y)) = μ[Z, Z'] + m f₀(Z)(Z')`, where
> `f₀(Z)(Z') = ⟨β, γ'⟩ - ⟨β', γ⟩` (12.130) and `m = Σ_j m_j` is the total mass (12.135). Souriau
> remarks (12.136) that the total mass can be interpreted as characterising the corresponding
> cohomology class of the Galilean group, and that this class is never zero.
>
> This file proves these facts at the level of the Lie algebra for `N` free material points in
> `ℝ³ = Fin 3 → ℝ` (no forces, `F_j = 0`; with the choice `B_j = 0` of (12.49), which (12.135)
> imposes on an isolated system, (12.44) gives `E_j = 0` and (12.45) reduces to (12.40)). An element
> `Z = (ω, β, γ, ε)` of the Galilean Lie algebra (12.74), (12.118) is a rotation `ω` (an axial
> vector), a change of velocity `β`, a space translation `γ` and a time translation `ε`; it acts on
> the evolution space, whose points are `y = (t, r_j, v_j)` (12.76), by the affine vector field
> (12.119). The bracket is Souriau's (6.12 b), `[Z, Z']_V = [Z_V, Z'_V]`, where the bracket of two
> vector fields is (2.45), here `DZ'_V(Z_V) - DZ_V(Z'_V)` (`EvolutionSpace.vectorField_bracket`);
> this is the usual Lie bracket of vector fields (Mathlib's `VectorField.lieBracket`). The matrices
> (12.74) are not formalised; on them this bracket reads `[Z, Z'] = Z'Z - ZZ'`, as in (11.22 a), the
> opposite of the usual matrix commutator.
>
> What is not formalised here:
> - the Galilean group itself, its action (12.73), (12.76) and its cocycle `θ₀` (12.126)-(12.128),
>   hence the statement of p. 151 that `θ₀` is not a coboundary of the group (definition (11.19)),
>   used in (12.136). The algebra-level result of this file implies it, because the derivative of a
>   group coboundary `Δ(μ₀)` is `μ₀[Z, Z']` (p. 116, note (1)); this implication is not formalised.
>   Physlib has `GalileanGroup` in `Physlib.SpaceAndTime.GalileanGroup.Basic`, whose rotation part
>   ranges over the full orthogonal group; Souriau's group (12.73) takes `A ∈ SO(3)` and is
>   connected (p. 139). Both have the same Lie algebra, with which this file works in dimension `3`,
>   in Souriau's parametrisation; the file links it to neither group;
> - `GalileanAlgebra` has no vector space or `LieRing` structure here, only `Zero` and `Add`; the
>   Jacobi identity is proved as an equation;
> - that the vector field (12.119), taken as printed, is the derivative (6.11) of the action (12.76);
> - the reading of (12.135) as the solution of the system (12.124), (12.134) for a general isolated
>   system (`B_j = 0`, `Σ_j E_j = 0`, `Σ_j r_j × E_j = 0`): for free points the explicit moment and
>   `m = Σ_j m_j` are verified, not derived; the uniqueness of `m` in (12.134) follows from
>   `lagrangeForm_vectorField` and `smul_cocycle_isCoboundary_iff` but is not stated;
> - the dimension `1` of (12.131), the second half of (12.136) (Hamilton's Lagrangian is not
>   invariant), forces, the converse of (12.48), the invariance of `σ` (12.72), (12.76), and the
>   uniqueness of the moment up to a constant (the constant in `E` is a choice);
> - the evolution space is presymplectic, not symplectic (p. 148, (12.114));
>   `EvolutionSpace.lagrangeForm_motion` shows that `σ` is degenerate, and `σ` depends on the point
>   `y` through the velocities. The setting of `PhyslibAlpha.ClassicalMechanics.MomentMap.Basic`
>   (a constant non-degenerate form on a vector space) therefore does not apply; the moment and the
>   cocycle are computed explicitly.

## ii. Key results

> - `GalileanAlgebra.bracket_jacobi`: the Jacobi identity for Souriau's bracket.
> - `GalileanAlgebra.cocycle_cyclic`: (12.129), `f₀` satisfies the cyclic identity.
> - `GalileanAlgebra.smul_cocycle_isCoboundary_iff`: `M f₀` is an algebra coboundary,
>   `M f₀(Z)(Z') = μ₀[Z, Z']` for some torsor `μ₀`, if and only if `M = 0`.
> - `EvolutionSpace.hasDerivAt_moment`: (12.124), the moment of the free points.
> - `EvolutionSpace.moment_motion`: (12.121), the moment is constant along the free motions.
> - `EvolutionSpace.lagrangeForm_vectorField`: (12.134) with `m = Σ_j m_j` (12.135).
> - `EvolutionSpace.totalMass_cocycle_not_coboundary`: (12.136) at the level of the algebra, for a
>   non-zero total mass the cocycle of the system is not a coboundary.
> - `EvolutionSpace.moment_g`, `EvolutionSpace.centerOfMass_motion`: (12.141), `g = m R - p t`, and
>   the uniform motion of the centre of gravity of free points.

## iv. References

> - J.-M. Souriau, Structure des systèmes dynamiques, Dunod, Paris, 1970: pp. 132-133
>   (12.40)-(12.49), pp. 139-140 (12.72)-(12.76), p. 148 (12.114), pp. 150-153 (12.118)-(12.141);
>   p. 27 (2.45), p. 50 (6.12 b) and p. 113 (11.22 a) for the bracket; p. 50 (6.13 b), p. 109
>   (11.16), p. 114 (11.24) and p. 116, note (1), for the coboundaries of the algebra.
>
> * J.-M. Souriau, *Structure des systèmes dynamiques*, Maîtrises de mathématiques, Dunod,
>   Paris, 1970: chapter 12, pp. 132-153, and pp. 27, 50, 109, 113-116 for the conventions (2.45),
>   (6.12), (6.13), (11.16), (11.22), (11.24). The equation numbers refer to this edition.
>   [ref: Souriau1970]

## A. The Galilean Lie algebra

**`ClassicalMechanics.GalileanAlgebra`**, a structure, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L122).

> An element `Z = (ω, β, γ, ε)` of the Lie algebra of the Galilean group, in Souriau's
> parametrisation (12.74), (12.118).

```lean
structure GalileanAlgebra where
  /-- The infinitesimal rotation, as an axial vector. -/
  ω : ℝ³
  /-- The change of velocity (infinitesimal boost). -/
  β : ℝ³
  /-- The space translation. -/
  γ : ℝ³
  /-- The time translation. -/
  ε : ℝ
```

**An instance with no name**, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L134).

```lean
instance : Zero GalileanAlgebra
```

**An instance with no name**, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L136).

```lean
instance : Add GalileanAlgebra
```

**`ClassicalMechanics.GalileanAlgebra.bracket`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L140).

> Souriau's bracket on the Galilean Lie algebra. It is the bracket of the vector fields (12.119)
> in the convention (6.12 b), (2.45), see `EvolutionSpace.vectorField_bracket`.

```lean
def bracket (Z Z' : GalileanAlgebra) : GalileanAlgebra
```

**`ClassicalMechanics.GalileanAlgebra.bracket_antisymm`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L145).

> The bracket is antisymmetric.

```lean
lemma bracket_antisymm (Z Z' : GalileanAlgebra) : bracket Z Z' + bracket Z' Z = 0
```

**`ClassicalMechanics.GalileanAlgebra.bracket_jacobi`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L158).

> The Jacobi identity for Souriau's bracket.

```lean
lemma bracket_jacobi (Z Z' Z'' : GalileanAlgebra) :
    bracket Z (bracket Z' Z'') + bracket Z' (bracket Z'' Z) + bracket Z'' (bracket Z Z') = 0
```

**`ClassicalMechanics.GalileanAlgebra.bracket_boost_translation`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L177).

> A change of velocity and a space translation commute.

```lean
lemma bracket_boost_translation (β γ : ℝ³) : bracket ⟨0, β, 0, 0⟩ ⟨0, 0, γ, 0⟩ = 0
```

## B. Torsors

**`ClassicalMechanics.GalileanTorsor`**, a structure, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L191).

> A torsor `μ = {l, g, p, E}`, an element of the dual of the Galilean Lie algebra (12.123).

```lean
structure GalileanTorsor where
  /-- The angular momentum part. -/
  l : ℝ³
  /-- The part paired with the changes of velocity. -/
  g : ℝ³
  /-- The momentum part. -/
  p : ℝ³
  /-- The energy part. -/
  E : ℝ
```

**`ClassicalMechanics.GalileanTorsor.pair`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L203).

> The pairing (12.122) of a torsor with an element of the Lie algebra,
> `μ(Z) = ⟨l, ω⟩ - ⟨g, β⟩ + ⟨p, γ⟩ - E ε`.

```lean
def GalileanTorsor.pair (μ : GalileanTorsor) (Z : GalileanAlgebra) : ℝ
```

## C. The cocycle `f₀`

**`ClassicalMechanics.GalileanAlgebra.cocycle`**, a def, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L215).

> The 2-form `f₀(Z)(Z') = ⟨β, γ'⟩ - ⟨β', γ⟩` of (12.130).

```lean
def cocycle (Z Z' : GalileanAlgebra) : ℝ
```

**`ClassicalMechanics.GalileanAlgebra.cocycle_antisymm`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L218).

> `f₀` is antisymmetric.

```lean
lemma cocycle_antisymm (Z Z' : GalileanAlgebra) : cocycle Z Z' = -cocycle Z' Z
```

**`ClassicalMechanics.GalileanAlgebra.cocycle_cyclic`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L223).

> (12.129): `f₀(Z)([Z', Z'']) + f₀(Z')([Z'', Z]) + f₀(Z'')([Z, Z']) = 0`.

```lean
lemma cocycle_cyclic (Z Z' Z'' : GalileanAlgebra) :
    cocycle Z (bracket Z' Z'') + cocycle Z' (bracket Z'' Z) + cocycle Z'' (bracket Z Z') = 0
```

**`ClassicalMechanics.GalileanAlgebra.cocycle_boost_translation`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L238).

> `f₀` is not zero: its value on a change of velocity and a space translation along the same
> axis is `1`.

```lean
lemma cocycle_boost_translation :
    cocycle ⟨0, ![1, 0, 0], 0, 0⟩ ⟨0, 0, ![1, 0, 0], 0⟩ = 1
```

**`ClassicalMechanics.GalileanAlgebra.smul_cocycle_isCoboundary_iff`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L246).

> `M f₀` is a coboundary of the algebra, `M f₀(Z)(Z') = μ₀[Z, Z']` for some torsor `μ₀` ((11.24)
> with `Z_{g*}(μ) = μ ∘ Ad(Z)` (11.16) and `Ad(Z)(Z') = [Z, Z']` (6.13 b); by p. 116, note (1), this
> is also the derivative of the group coboundary `Δ(μ₀)` of (11.19)), if and only if `M = 0`.

```lean
lemma smul_cocycle_isCoboundary_iff (M : ℝ) :
    (∃ μ₀ : GalileanTorsor, ∀ Z Z' : GalileanAlgebra, M * cocycle Z Z' = μ₀.pair (bracket Z Z'))
      ↔ M = 0
```

**`ClassicalMechanics.GalileanAlgebra.cocycle_not_coboundary`**, a lemma, [line 266](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L266).

> `f₀` is not a coboundary of the algebra: no torsor `μ₀` satisfies `f₀(Z)(Z') = μ₀[Z, Z']` for
> all `Z`, `Z'`.

```lean
lemma cocycle_not_coboundary :
    ¬ ∃ μ₀ : GalileanTorsor, ∀ Z Z' : GalileanAlgebra, cocycle Z Z' = μ₀.pair (bracket Z Z')
```

## D. The evolution space of free material points

**`ClassicalMechanics.EvolutionSpace`**, a structure, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L283).

> A point, or a tangent vector, of the evolution space of `N` material points,
> `y = (t, r_j, v_j)` (12.76).

```lean
structure EvolutionSpace (N : ℕ) where
  /-- The time. -/
  t : ℝ
  /-- The positions. -/
  r : Fin N → ℝ³
  /-- The velocities. -/
  v : Fin N → ℝ³
```

**An instance with no name**, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L295).

```lean
instance : Sub (EvolutionSpace N)
```

**`ClassicalMechanics.EvolutionSpace.vectorField`**, a def, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L301).

> The vector field `Z_V` of `Z` on the evolution space (12.119): `δt = ε`,
> `δr_j = ω × r_j + β t + γ`, `δv_j = ω × v_j + β`.

```lean
def vectorField (Z : GalileanAlgebra) (y : EvolutionSpace N) : EvolutionSpace N
```

**`ClassicalMechanics.EvolutionSpace.linearPart`**, a def, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L306).

> The differential of the affine vector field `Z_V` (its linear part), applied to a tangent vector
> `w`.

```lean
def linearPart (Z : GalileanAlgebra) (w : EvolutionSpace N) : EvolutionSpace N
```

**`ClassicalMechanics.EvolutionSpace.vectorField_bracket`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L311).

> Souriau's bracket is the bracket of the vector fields in the convention (6.12 b), (2.45):
> `[Z, Z']_V = DZ'_V(Z_V) - DZ_V(Z'_V)`.

```lean
lemma vectorField_bracket (Z Z' : GalileanAlgebra) (y : EvolutionSpace N) :
    vectorField (bracket Z Z') y
      = linearPart Z' (vectorField Z y) - linearPart Z (vectorField Z' y)
```

**`ClassicalMechanics.EvolutionSpace.lagrangeForm`**, a def, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L330).

> The Lagrange form of `N` free material points of masses `m j` at `y`, (12.40) with `F_j = 0`:
> `σ(dy)(δy) = Σ_j ⟨m_j dv_j, δr_j - v_j δt⟩ - ⟨m_j δv_j, dr_j - v_j dt⟩`.

```lean
def lagrangeForm (m : Fin N → ℝ) (y dy δy : EvolutionSpace N) : ℝ
```

**`ClassicalMechanics.EvolutionSpace.lagrangeForm_antisymm`**, a lemma, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L334).

> `σ` is antisymmetric.

```lean
lemma lagrangeForm_antisymm (m : Fin N → ℝ) (y dy δy : EvolutionSpace N) :
    lagrangeForm m y dy δy = -lagrangeForm m y δy dy
```

**`ClassicalMechanics.EvolutionSpace.lagrangeForm_motion`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L340).

> (12.41)-(12.43): the velocity `(1, v_j, 0)` of the free motion through `y` lies in the kernel
> of `σ` (one direction of (12.48)).

```lean
lemma lagrangeForm_motion (m : Fin N → ℝ) (y δy : EvolutionSpace N) :
    lagrangeForm m y ⟨1, y.v, 0⟩ δy = 0
```

## E. The moment

**`ClassicalMechanics.EvolutionSpace.moment`**, a def, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L353).

> The moment of `N` free material points ((12.125) for one point of unit mass; (12.135) for `N`
> points, with `E_j = 0` in its last line and the additive constant of `E` chosen to be `0`):
> `l = Σ m_j r_j × v_j`, `g = Σ m_j (r_j - v_j t)`, `p = Σ m_j v_j`, `E = ½ Σ m_j ‖v_j‖²`.

```lean
def moment (m : Fin N → ℝ) (y : EvolutionSpace N) : GalileanTorsor
```

**`ClassicalMechanics.EvolutionSpace.line`**, a def, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L358).

> The line `s ↦ y + s dy` of the evolution space.

```lean
def line (y dy : EvolutionSpace N) (s : ℝ) : EvolutionSpace N
```

**`ClassicalMechanics.EvolutionSpace.motion`**, a def, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L362).

> The free motion through `y`: `t + s`, `r_j + s v_j`, `v_j`.

```lean
def motion (y : EvolutionSpace N) (s : ℝ) : EvolutionSpace N
```

**`ClassicalMechanics.EvolutionSpace.pair_moment`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L366).

> `μ(Z)` as a sum over the material points.

```lean
lemma pair_moment (m : Fin N → ℝ) (y : EvolutionSpace N) (Z : GalileanAlgebra) :
    (moment m y).pair Z = ∑ j, m j * ((y.r j ⨯₃ y.v j) ⬝ᵥ Z.ω - (y.r j - y.t • y.v j) ⬝ᵥ Z.β
      + y.v j ⬝ᵥ Z.γ - (1 / 2 : ℝ) * Z.ε * (y.v j ⬝ᵥ y.v j))
```

**`ClassicalMechanics.EvolutionSpace.hasDerivAt_moment`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L397).

> (12.124): `σ(dy)(Z_V(y)) = dμ(Z)(dy)`, stated as the derivative at `s = 0` of
> `s ↦ μ(y + s dy)(Z)`; `μ` is a moment of the action (12.120).

```lean
lemma hasDerivAt_moment (m : Fin N → ℝ) (y dy : EvolutionSpace N) (Z : GalileanAlgebra) :
    HasDerivAt (fun s => (moment m (line y dy s)).pair Z) (lagrangeForm m y dy (vectorField Z y))
      0
```

**`ClassicalMechanics.EvolutionSpace.moment_motion`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L419).

> (12.121): the moment is constant along every free motion.

```lean
lemma moment_motion (m : Fin N → ℝ) (y : EvolutionSpace N) (s : ℝ) :
    moment m (motion y s) = moment m y
```

## F. The cocycle of the system and the mass

**`ClassicalMechanics.EvolutionSpace.totalMass`**, a def, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L433).

> The total mass `m = Σ_j m_j` (12.135).

```lean
def totalMass (m : Fin N → ℝ) : ℝ
```

**`ClassicalMechanics.EvolutionSpace.centerOfMass`**, a def, [line 437](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L437).

> The centre of gravity `R = (Σ_j m_j r_j) / m`, named in (12.141) (the formula is the usual one,
> not printed there); for `m = 0` the value is `0`, by the convention `0⁻¹ = 0`.

```lean
def centerOfMass (m : Fin N → ℝ) (y : EvolutionSpace N) : ℝ³
```

**`ClassicalMechanics.EvolutionSpace.lagrangeForm_vectorField`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L441).

> (12.134) with `m = Σ_j m_j` (12.135): `σ(Z_V(y))(Z'_V(y)) = μ[Z, Z'] + m f₀(Z)(Z')`.

```lean
lemma lagrangeForm_vectorField (m : Fin N → ℝ) (y : EvolutionSpace N) (Z Z' : GalileanAlgebra) :
    lagrangeForm m y (vectorField Z y) (vectorField Z' y)
      = (moment m y).pair (bracket Z Z') + totalMass m * cocycle Z Z'
```

**`ClassicalMechanics.EvolutionSpace.totalMass_cocycle_not_coboundary`**, a lemma, [line 453](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L453).

> (12.136) at the level of the algebra: for a non-zero total mass, the cocycle `m f₀` of the
> system is not a coboundary of the algebra.

```lean
lemma totalMass_cocycle_not_coboundary (m : Fin N → ℝ) (hM : totalMass m ≠ 0) :
    ¬ ∃ μ₀ : GalileanTorsor, ∀ Z Z' : GalileanAlgebra,
      totalMass m * cocycle Z Z' = μ₀.pair (bracket Z Z')
```

**`ClassicalMechanics.EvolutionSpace.moment_g`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L459).

> (12.141): `g = m R - p t`, with `R` the centre of gravity, for a non-zero total mass.

```lean
lemma moment_g (m : Fin N → ℝ) (hM : totalMass m ≠ 0) (y : EvolutionSpace N) :
    (moment m y).g = totalMass m • centerOfMass m y - y.t • (moment m y).p
```

**`ClassicalMechanics.EvolutionSpace.centerOfMass_motion`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean#L471).

> Along a free motion the centre of gravity moves uniformly with velocity `p / m` (p. 153, after
> (12.141)). Souriau deduces this for any isolated system from the constancy of `g` and `p`; here it
> is proved directly from the free motion. For `m = 0` both sides are `0`.

```lean
lemma centerOfMass_motion (m : Fin N → ℝ) (y : EvolutionSpace N) (s : ℝ) :
    centerOfMass m (motion y s) = centerOfMass m y + s • ((totalMass m)⁻¹ • (moment m y).p)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalMechanics/MomentMap/GalileanMass.lean)
