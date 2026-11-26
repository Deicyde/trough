---
declaration: module
origin: cited
lean: StandardModel.globalGaugeGroup, StandardModel.gaugeGroupEquiv, StandardModel.gaugeGroupEquiv_val, StandardModel.su3Block, StandardModel.su2Block, StandardModel.u1Phase, StandardModel.su3Block_gaugeGroupEquiv, StandardModel.su2Block_gaugeGroupEquiv
statement: formalized
proof: formalized
---

# The Standard Model gauge group as a global gauge group

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.GlobalGaugeGroup`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean): 27 declarations (1 instance with no name), 27 with a docstring.

> The gauge group `SU(3) × SU(2) × U(1)` as block-diagonal `6 × 6` complex matrices.

## i. Overview

> The global gauge group of the Standard Model is the product `SU(3) × (SU(2) × U(1))` of global
> gauge groups, made of the block-diagonal matrices `diag(g₃, g₂, u)`. Its elements are the
> elements of `GaugeGroupI`, through `StandardModel.gaugeGroupEquiv`. Taking the `SU(3)` block,
> the `SU(2)` block and the phase `u` are continuous homomorphisms.
>
> The representations of the three factors are pulled back along the projections to the blocks.
> The `SU(3)` and `SU(2)` blocks act on the fundamental representations, and the phase `u` is the
> hypercharge character. The matter fields of the Standard Model are built from these.

## ii. Key results

> - `StandardModel.globalGaugeGroup` : the global gauge group `SU(3) × SU(2) × U(1)`.
> - `StandardModel.gaugeGroupEquiv` : its elements are those of `GaugeGroupI`.
> - The instance `CompactSpace globalGaugeGroup.group` : the global gauge group is compact.
> - `StandardModel.su3Block`, `StandardModel.su2Block`, `StandardModel.u1Phase` : the blocks of
>   its elements, which on the image of `gaugeGroupEquiv` are the three factors
>   (`StandardModel.su3Block_gaugeGroupEquiv` and its companions).
> - `StandardModel.su3Fund`, `StandardModel.su2Fund` : the fundamental representations of the
>   `SU(3)` and `SU(2)` factors, as continuous matrix representations of the global gauge group,
>   with derivatives `StandardModel.derivMat_su3Fund` and `StandardModel.derivMat_su2Fund`.
> - `StandardModel.hypercharge` : the hypercharge character, with derivative the `u(1)` entry
>   (see `StandardModel.hypercharge_exp`).

## iv. References

> * None.

## A. The global gauge group

> The product of the global gauge groups `SU 3`, `SU 2` and `U1`, its identification with
> `GaugeGroupI` and its compactness.

**`StandardModel.globalGaugeGroup`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L74).

> The global gauge group of the Standard Model, `SU(3) × SU(2) × U(1)` as the
> block-diagonal matrices `diag(g₃, g₂, u)` on `ℂ³ ⊕ ℂ² ⊕ ℂ`.

```lean
def globalGaugeGroup : GlobalGaugeGroup (Fin 3 ⊕ (Fin 2 ⊕ Fin 1))
```

**`StandardModel.gaugeGroupEquiv`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L79).

> The gauge group `GaugeGroupI` of the Standard Model is its global gauge group, through the
> block-diagonal matrices.

```lean
noncomputable def gaugeGroupEquiv : GaugeGroupI ≃* globalGaugeGroup.group
```

**`StandardModel.gaugeGroupEquiv_val`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L86).

> An element of `GaugeGroupI` is the block-diagonal matrix of its three components.

```lean
lemma gaugeGroupEquiv_val (g : GaugeGroupI) :
    (((gaugeGroupEquiv g : globalGaugeGroup.group) : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄) =
      fromBlocks (g.1 : Matrix (Fin 3) (Fin 3) ℂ) 0 0
        (fromBlocks (g.2.1 : Matrix (Fin 2) (Fin 2) ℂ) 0 0 (scalar (Fin 1) (g.2.2 : ℂ)))
```

**An instance with no name**, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L94).

> The global gauge group of the Standard Model is compact, being a product of the compact
> groups `SU(3)`, `SU(2)` and `U(1)`.

```lean
instance : CompactSpace globalGaugeGroup.group
```

## B. The blocks of the global gauge group

> The `SU(3)` block, the `SU(2)` block and the phase of an element, as homomorphisms, read off
> the matrix and continuous.

**`StandardModel.su3Block`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L108).

> The `SU(3)` block `g₃` of an element `diag(g₃, g₂, u)` of the global gauge group.

```lean
noncomputable def su3Block : globalGaugeGroup.group →* Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.su2Block`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L113).

> The `SU(2)` block `g₂` of an element `diag(g₃, g₂, u)` of the global gauge group.

```lean
noncomputable def su2Block : globalGaugeGroup.group →* Matrix (Fin 2) (Fin 2) ℂ
```

**`StandardModel.u1Phase`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L118).

> The phase `u` of an element `diag(g₃, g₂, u)` of the global gauge group.

```lean
noncomputable def u1Phase : globalGaugeGroup.group →* ℂˣ
```

**`StandardModel.su3Block_gaugeGroupEquiv`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L124).

> The `SU(3)` block of the image of a gauge transformation is its colour factor.

```lean
lemma su3Block_gaugeGroupEquiv (g : GaugeGroupI) :
    su3Block (gaugeGroupEquiv g) = (g.toSU3.1 : Matrix (Fin 3) (Fin 3) ℂ)
```

**`StandardModel.su2Block_gaugeGroupEquiv`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L133).

> The `SU(2)` block of the image of a gauge transformation is its isospin factor.

```lean
lemma su2Block_gaugeGroupEquiv (g : GaugeGroupI) :
    su2Block (gaugeGroupEquiv g) = (g.toSU2.1 : Matrix (Fin 2) (Fin 2) ℂ)
```

**`StandardModel.u1Phase_gaugeGroupEquiv`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L142).

> The phase of the image of a gauge transformation is its hypercharge factor.

```lean
lemma u1Phase_gaugeGroupEquiv (g : GaugeGroupI) :
    ((u1Phase (gaugeGroupEquiv g) : ℂˣ) : ℂ) = (g.toU1.1 : ℂ)
```

**`StandardModel.globalGaugeGroup_val_eq_fromBlocks`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L149).

> An element of the global gauge group is the block-diagonal matrix of its blocks.

```lean
lemma globalGaugeGroup_val_eq_fromBlocks (g : globalGaugeGroup.group) :
    ((g : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄) =
      fromBlocks (su3Block g) 0 0 (fromBlocks (su2Block g) 0 0
        (scalar (Fin 1) (u1Phase g : ℂ)))
```

**`StandardModel.su3Block_eq`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L157).

> The `SU(3)` block is the upper-left `3 × 3` block of the matrix.

```lean
lemma su3Block_eq (g : globalGaugeGroup.group) :
    su3Block g = toBlocks₁₁ ((g : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄)
```

**`StandardModel.su2Block_eq`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L162).

> The `SU(2)` block is the middle `2 × 2` block of the matrix.

```lean
lemma su2Block_eq (g : globalGaugeGroup.group) :
    su2Block g = toBlocks₁₁ (toBlocks₂₂ ((g : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄))
```

**`StandardModel.u1Phase_eq`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L167).

> The phase is the lower-right entry of the matrix.

```lean
lemma u1Phase_eq (g : globalGaugeGroup.group) :
    (u1Phase g : ℂ) = toBlocks₂₂ (toBlocks₂₂ ((g : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄)) 0 0
```

**`StandardModel.continuous_globalGaugeGroup_val`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L173).

> The matrix of an element of the global gauge group depends continuously on it.

```lean
lemma continuous_globalGaugeGroup_val :
    Continuous fun g : globalGaugeGroup.group => ((g : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄)
```

**`StandardModel.continuous_su3Block`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L178).

> The `SU(3)` block depends continuously on the gauge transformation.

```lean
lemma continuous_su3Block : Continuous fun g => su3Block g
```

**`StandardModel.continuous_su2Block`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L184).

> The `SU(2)` block depends continuously on the gauge transformation.

```lean
lemma continuous_su2Block : Continuous fun g => su2Block g
```

**`StandardModel.continuous_u1Phase`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L190).

> The phase depends continuously on the gauge transformation.

```lean
lemma continuous_u1Phase : Continuous fun g => (u1Phase g : ℂ)
```

## C. The representations of the factors

> The fundamental representations of the `SU(3)` and `SU(2)` factors are the blocks of a gauge
> transformation `diag(g₃, g₂, u)`, which act by `g₃` and `g₂`. The hypercharge character is the
> phase `u`, and its derivative is the entry of the `U(1)` block of a Lie algebra element.

**`StandardModel.continuous_toHomUnits`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L206).

> A continuous monoid homomorphism from the global gauge group to a monoid, which takes
> values in the units, is a continuous homomorphism to the units.

```lean
lemma continuous_toHomUnits {M : Type} [Monoid M] [TopologicalSpace M]
    {f : globalGaugeGroup.group →* M} (hf : Continuous f) : Continuous f.toHomUnits
```

**`StandardModel.su3Fund`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L213).

> The fundamental representation of the `SU(3)` factor, as a continuous representation of the
> global gauge group. A gauge transformation `diag(g₃, g₂, u)` acts by `g₃`.

```lean
noncomputable def su3Fund : globalGaugeGroup.group →ₜ* (Matrix (Fin 3) (Fin 3) ℂ)ˣ
```

**`StandardModel.su2Fund`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L218).

> The fundamental representation of the `SU(2)` factor, as a continuous representation of the
> global gauge group. A gauge transformation `diag(g₃, g₂, u)` acts by `g₂`.

```lean
noncomputable def su2Fund : globalGaugeGroup.group →ₜ* (Matrix (Fin 2) (Fin 2) ℂ)ˣ
```

**`StandardModel.su3Fund_val`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L224).

> A gauge transformation acts on the fundamental representation of the `SU(3)` factor by
> its `SU(3)` block.

```lean
lemma su3Fund_val (g : globalGaugeGroup.group) :
    ((su3Fund g : (Matrix (Fin 3) (Fin 3) ℂ)ˣ) : Matrix (Fin 3) (Fin 3) ℂ) = su3Block g
```

**`StandardModel.su2Fund_val`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L230).

> A gauge transformation acts on the fundamental representation of the `SU(2)` factor by
> its `SU(2)` block.

```lean
lemma su2Fund_val (g : globalGaugeGroup.group) :
    ((su2Fund g : (Matrix (Fin 2) (Fin 2) ℂ)ˣ) : Matrix (Fin 2) (Fin 2) ℂ) = su2Block g
```

**`StandardModel.derivMat_su3Fund`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L235).

> The Lie algebra acts on the fundamental representation of the `SU(3)` factor by its
> `SU(3)` block.

```lean
lemma derivMat_su3Fund (c : globalGaugeGroup.lieSubalgebra) :
    derivMat su3Fund c = (c : 𝕄).toBlocks₁₁
```

**`StandardModel.derivMat_su2Fund`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L244).

> The Lie algebra acts on the fundamental representation of the `SU(2)` factor by its
> `SU(2)` block.

```lean
lemma derivMat_su2Fund (c : globalGaugeGroup.lieSubalgebra) :
    derivMat su2Fund c = (c : 𝕄).toBlocks₂₂.toBlocks₁₁
```

**`StandardModel.hypercharge`**, a def, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L257).

> The hypercharge character of the global gauge group is the phase `u` of an element
> `diag(g₃, g₂, u)`. Its derivative is the entry of the `U(1)` block of a Lie algebra
> element, see `hypercharge_exp`.

```lean
noncomputable def hypercharge : globalGaugeGroup.group →ₜ* ℂˣ
```

**`StandardModel.hypercharge_exp`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean#L265).

> The hypercharge character of the exponential of a Lie algebra element is the exponential of
> the entry of its `U(1)` block, that is `hypercharge (exp (t c)) = exp (t z)` with `z` the
> derivative of the hypercharge at `c`.

```lean
lemma hypercharge_exp (c : globalGaugeGroup.lieSubalgebra) (t : ℝ)
    (g : globalGaugeGroup.group)
    (hg : ((g : GL (Fin 3 ⊕ (Fin 2 ⊕ Fin 1)) ℂ) : 𝕄) =
      NormedSpace.exp (t • (c : 𝕄))) :
    ((hypercharge g : ℂˣ) : ℂ) = Complex.exp (t * (c : 𝕄).toBlocks₂₂.toBlocks₂₂ 0 0)
```

## Depends on

- [The Standard Model Gauge Group](../../../../physlib/particles/standardmodel/gaugegroup/basic.md)
- [The product of global gauge groups](../../../classicalfieldtheory/gaugetheory/part-02/globalgaugegroup-prod.md)
- [The global gauge group SU(n)](../../../classicalfieldtheory/gaugetheory/part-02/globalgaugegroup-su.md)
- [The global gauge group U(1)](../../../classicalfieldtheory/gaugetheory/part-02/globalgaugegroup-u1.md)
- [Matter fields from matrix representations of a global gauge group](../../../classicalfieldtheory/gaugetheory/part-06/matterfield-ofmatrixrep.md)

## Proof depends on

- [Conditions for the reduction of invariants](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-realization-conditions.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/GaugeGroup/GlobalGaugeGroup.lean)
