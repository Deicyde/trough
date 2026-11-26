---
declaration: module
origin: cited
lean: ClassicalMechanics.PhaseSpace, ClassicalMechanics.PhaseSpace.position, ClassicalMechanics.PhaseSpace.momentum, ClassicalMechanics.PhaseSpace.mk, ClassicalMechanics.PhaseSpace.position_mk, ClassicalMechanics.PhaseSpace.momentum_mk, ClassicalMechanics.PhaseSpace.contMDiff_position, ClassicalMechanics.PhaseSpace.zeroMomentum
statement: formalized
proof: formalized
---

# Canonical phase spaces

The module `Physlib.ClassicalMechanics.PhaseSpace.Basic`, [Physlib/ClassicalMechanics/PhaseSpace/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean): 20 declarations, 14 with a docstring; 1 private, not shown.

> The cotangent phase space of a configuration space and its momentum-position coordinates.

## i. Overview

> A phase-space state consists of a configuration `q` and a momentum covector at `q`.
> The cotangent bundle inherits its topology and smooth structure from Mathlib's bundle of
> continuous linear maps from the tangent bundle to the trivial real line bundle.
>
> For a normed configuration space, the phase space has global coordinates `(p, q)` with
> `p` in the continuous dual. On a real Hilbert space, the Riesz identification represents
> momentum by a vector, matching the momentum-first convention of Hamilton's equations.
> The constructors `PhaseSpace.ofNormedSpace` and `PhaseSpace.ofInnerProductSpace` build
> states directly from these momentum-position coordinates.

## ii. Key results

> - `PhaseSpace` : the cotangent phase space of a configuration space.
> - `PhaseSpace.contMDiff_position` : the configuration projection is smooth.
> - `PhaseSpace.contMDiff_zeroMomentum` : the zero-momentum section is smooth.
> - `PhaseSpace.normedSpaceDiffeomorph` : global covector-position coordinates.
> - `PhaseSpace.innerProductSpaceDiffeomorph` : global momentum-vector-position coordinates.

## iv. References

> * V. I. Arnold, Mathematical Methods of Classical Mechanics. [ref: arnold\_mechanics]

## A. States and their configurations

**`ClassicalMechanics.PhaseSpace`**, an abbrev, [line 66](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L66).

> The canonical phase space `T*Q`, whose states pair a configuration with a momentum covector.

```lean
abbrev PhaseSpace
```

**`ClassicalMechanics.PhaseSpace.position`**, an abbrev, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L79).

> The configuration of a phase-space state.

```lean
abbrev position (s : PhaseSpace I Q) : Q
```

**`ClassicalMechanics.PhaseSpace.momentum`**, an abbrev, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L82).

> The momentum covector of a state, acting on tangent vectors at its configuration.

```lean
abbrev momentum (s : PhaseSpace I Q) : TangentSpace I s.position →L[ℝ] ℝ
```

**`ClassicalMechanics.PhaseSpace.mk`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L85).

> Construct a state from a configuration and its momentum covector.

```lean
def mk (q : Q) (p : TangentSpace I q →L[ℝ] ℝ) : PhaseSpace I Q
```

**`ClassicalMechanics.PhaseSpace.position_mk`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L88).

```lean
lemma position_mk (q : Q) (p : TangentSpace I q →L[ℝ] ℝ) : (mk q p).position = q
```

**`ClassicalMechanics.PhaseSpace.momentum_mk`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L91).

```lean
lemma momentum_mk (q : Q) (p : TangentSpace I q →L[ℝ] ℝ) : (mk q p).momentum = p
```

**`ClassicalMechanics.PhaseSpace.contMDiff_position`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L94).

> The configuration projection from phase space is smooth.

```lean
lemma contMDiff_position :
    ContMDiff (I.prod 𝓘(ℝ, E →L[ℝ] ℝ)) I ∞ (position : PhaseSpace I Q → Q)
```

**`ClassicalMechanics.PhaseSpace.zeroMomentum`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L99).

> The state with zero momentum at a given configuration.

```lean
def zeroMomentum (q : Q) : PhaseSpace I Q
```

**`ClassicalMechanics.PhaseSpace.contMDiff_zeroMomentum`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L102).

> Assigning zero momentum to each configuration is a smooth section of phase space.

```lean
lemma contMDiff_zeroMomentum :
    ContMDiff I (I.prod 𝓘(ℝ, E →L[ℝ] ℝ)) ∞ (zeroMomentum : Q → PhaseSpace I Q)
```

## B. Global momentum-position coordinates

**`ClassicalMechanics.PhaseSpace.normedSpaceDiffeomorph`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L125).

> Global covector-position coordinates on the phase space of a real normed space.

```lean
noncomputable def normedSpaceDiffeomorph :
    PhaseSpace 𝓘(ℝ, E) ⟨E⟩ ≃ₘ^∞ ⟮(𝓘(ℝ, E)).prod 𝓘(ℝ, E →L[ℝ] ℝ),
      𝓘(ℝ, (E →L[ℝ] ℝ) × E)⟯ (E →L[ℝ] ℝ) × E
```

**`ClassicalMechanics.PhaseSpace.normedSpaceDiffeomorph_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L150).

```lean
lemma normedSpaceDiffeomorph_apply (s : PhaseSpace 𝓘(ℝ, E) ⟨E⟩) :
    normedSpaceDiffeomorph E s =
      (s.momentum.comp (NormedSpace.fromTangentSpace s.position).symm.toContinuousLinearMap,
        s.position)
```

**`ClassicalMechanics.PhaseSpace.normedSpaceDiffeomorph_symm_apply`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L156).

```lean
lemma normedSpaceDiffeomorph_symm_apply (p : E →L[ℝ] ℝ) (q : E) :
    (normedSpaceDiffeomorph E).symm (p, q) =
      mk q (p.comp (NormedSpace.fromTangentSpace q).toContinuousLinearMap)
```

**`ClassicalMechanics.PhaseSpace.ofNormedSpace`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L164).

> The phase-space state on a normed space with momentum covector `p` and position `q`.
> The argument order agrees with the momentum-position coordinates of Hamilton's equations.

```lean
def ofNormedSpace (p : E →L[ℝ] ℝ) (q : E) : PhaseSpace 𝓘(ℝ, E) ⟨E⟩
```

**`ClassicalMechanics.PhaseSpace.position_ofNormedSpace`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L168).

```lean
lemma position_ofNormedSpace (p : E →L[ℝ] ℝ) (q : E) :
    (ofNormedSpace p q).position = q
```

**`ClassicalMechanics.PhaseSpace.momentum_ofNormedSpace_apply`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L175).

> The constructed momentum covector acts on tangent vectors through their normed-space
> coordinates.

```lean
lemma momentum_ofNormedSpace_apply (p : E →L[ℝ] ℝ) (q : E) (v : TangentSpace 𝓘(ℝ, E) q) :
    DFunLike.coe (F := TangentSpace 𝓘(ℝ, E) q →L[ℝ] ℝ) (ofNormedSpace p q).momentum v =
      p (NormedSpace.fromTangentSpace q v)
```

**`ClassicalMechanics.PhaseSpace.innerProductSpaceDiffeomorph`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L186).

> Global momentum-vector-position coordinates, using the real Hilbert-space Riesz map.

```lean
noncomputable def innerProductSpaceDiffeomorph :
    PhaseSpace 𝓘(ℝ, E) ⟨E⟩ ≃ₘ^∞ ⟮(𝓘(ℝ, E)).prod 𝓘(ℝ, E →L[ℝ] ℝ),
      𝓘(ℝ, E × E)⟯ E × E
```

**`ClassicalMechanics.PhaseSpace.innerProductSpaceDiffeomorph_symm_apply`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L195).

> A coordinate momentum vector acts on velocities by the real inner product.

```lean
lemma innerProductSpaceDiffeomorph_symm_apply (p q : E) :
    (innerProductSpaceDiffeomorph E).symm (p, q) =
      mk q ((InnerProductSpace.toDual ℝ E p).comp
        (NormedSpace.fromTangentSpace q).toContinuousLinearMap)
```

**`ClassicalMechanics.PhaseSpace.ofInnerProductSpace`**, a def, [line 205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L205).

> The phase-space state on a real Hilbert space with momentum vector `p` and position `q`.
> The Riesz map turns `p` into a momentum covector, with the same argument order as Hamilton's
> equations.

```lean
def ofInnerProductSpace (p q : E) : PhaseSpace 𝓘(ℝ, E) ⟨E⟩
```

**`ClassicalMechanics.PhaseSpace.position_ofInnerProductSpace`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L209).

```lean
lemma position_ofInnerProductSpace (p q : E) :
    (ofInnerProductSpace p q).position = q
```

**`ClassicalMechanics.PhaseSpace.momentum_ofInnerProductSpace_apply`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean#L214).

> The momentum covector associated to `p` acts by taking the inner product with `p`.

```lean
lemma momentum_ofInnerProductSpace_apply (p q : E) (v : TangentSpace 𝓘(ℝ, E) q) :
    DFunLike.coe (F := TangentSpace 𝓘(ℝ, E) q →L[ℝ] ℝ) (ofInnerProductSpace p q).momentum v =
      inner ℝ p (NormedSpace.fromTangentSpace q v)
```

## Depends on

- [Configuration spaces](../configurationspace/basic.md)

## Sources

- [Physlib/ClassicalMechanics/PhaseSpace/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ClassicalMechanics/PhaseSpace/Basic.lean)
