---
declaration: module
origin: cited
lean: GaugeFieldData.gaugeConnection, GaugeFieldData.gaugeAssignment, GaugeFieldData.repJetAlgHom, GaugeFieldData.repJetAlgHom_ιFermion, GaugeFieldData.repJetAlgHom_ιBoson, GaugeFieldData.repJetAlgHom_ιConnection, GaugeFieldData.repJetAlgHom_comp_includeConnection, GaugeFieldData.repJetAlgHom_includeConnection
statement: formalized
proof: formalized
---

# The jet gauge action on the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.GaugeAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean): 20 declarations, 11 with a docstring.

> The action of the jet gauge group on the local field algebra by algebra endomorphisms.

## i. Overview

> The jet gauge group `G.gaugeJetGroup` acts on the local field algebra `J(T)` of a field datum
> by algebra endomorphisms. It acts on the generators of a matter species by the action
> `FieldDerivSpace.repJet` of that species, and on the connection generators by the affine
> action `LocalGaugeFieldAlgebra.repJet` of the gauge-only algebra, with its Maurer–Cartan
> shift. The three generator actions form a compatible assignment, whose lift through the
> universal property of `J(T)` is the action of one jet; the representation laws follow from
> uniqueness, without unfolding the tensor-product carrier.

## ii. Key results

> - `GaugeFieldData.repJetAlgHom`, `GaugeFieldData.repJet` : the action of a jet, as an
>   algebra endomorphism and as a representation, with `repJet_ιFermion`, `repJet_ιBoson`,
>   `repJet_ιConnection` on the generators.
> - `GaugeFieldData.repJet_includeConnection` : on the connection factor the action is the
>   complexified gauge-only action.
> - `GaugeFieldData.repJet_ιConnection_affine` : the affine law of the connection generators.

## iv. References

> * None.

## A. The gauge assignment of a jet

**`GaugeFieldData.gaugeConnection`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L62).

> The connection generators after the action of a jet, the gauge-only action on the
> degree-one element, included into the local field algebra.

```lean
noncomputable def gaugeConnection (U : G.gaugeJetGroup) :
    GaugeBoson.FieldDerivSpace G →ₗ[ℝ] T.LocalFieldAlgebra
```

**`GaugeFieldData.gaugeAssignment`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L74).

> The assignment of the generators defining the action of a jet. Each matter species
> acts on its own component functions, the connection generators through the gauge-only
> action. The relations hold because the images are generators of the same kind, or lie in
> the central connection factor.

```lean
noncomputable def gaugeAssignment (U : G.gaugeJetGroup) : T.Assignment T.LocalFieldAlgebra
```

## B. The action of a jet

**`GaugeFieldData.repJetAlgHom`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L94).

> The action of a jet on the local field algebra, as an algebra endomorphism, the lift
> of its gauge assignment.

```lean
noncomputable def repJetAlgHom (U : G.gaugeJetGroup) : T.LocalFieldAlgebra →ₐ[ℂ]
  T.LocalFieldAlgebra
```

**`GaugeFieldData.repJetAlgHom_ιFermion`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L101).

```lean
lemma repJetAlgHom_ιFermion (U : G.gaugeJetGroup) (i : T.FermionSpecies)
    (x : FieldDerivSpace (T.fermion i)) :
    T.repJetAlgHom U (T.ιFermion i x)
      = T.ιFermion i (FieldDerivSpace.repJet (T.fermion i) U x)
```

**`GaugeFieldData.repJetAlgHom_ιBoson`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L108).

```lean
lemma repJetAlgHom_ιBoson (U : G.gaugeJetGroup) (j : T.BosonSpecies)
    (y : FieldDerivSpace (T.boson j)) :
    T.repJetAlgHom U (T.ιBoson j y) = T.ιBoson j (FieldDerivSpace.repJet (T.boson j) U y)
```

**`GaugeFieldData.repJetAlgHom_ιConnection`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L114).

```lean
lemma repJetAlgHom_ιConnection (U : G.gaugeJetGroup) (v : GaugeBoson.FieldDerivSpace G) :
    T.repJetAlgHom U (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repJet G U (SymmetricAlgebra.ι ℝ _ v))
```

## C. The action on the connection factor

**`GaugeFieldData.repJetAlgHom_comp_includeConnection`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L130).

> The action of a jet restricts to the complexified gauge-only action on the connection
> factor, as an equation of algebra maps out of the complexified gauge-only algebra. It is
> enough to compare them on the real generators, where it is the computation rule of the
> lift.

```lean
lemma repJetAlgHom_comp_includeConnection (U : G.gaugeJetGroup) :
    (T.repJetAlgHom U).comp T.includeConnection
      = T.includeConnection.comp (LocalGaugeFieldAlgebra.complexRepJetAlgHom G U)
```

**`GaugeFieldData.repJetAlgHom_includeConnection`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L140).

> The action of a jet restricts to the complexified gauge-only action on the connection
> factor.

```lean
lemma repJetAlgHom_includeConnection (U : G.gaugeJetGroup) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) :
    T.repJetAlgHom U (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepJet G U y)
```

**`GaugeFieldData.repJetAlgHom_includeConnection_one_tmul`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L147).

> On the real gauge-only algebra, included, a jet acts through the gauge-only action.

```lean
lemma repJetAlgHom_includeConnection_one_tmul (U : G.gaugeJetGroup) (x : LocalGaugeFieldAlgebra G) :
    T.repJetAlgHom U (T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] x))
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.repJet G U x)
```

## D. The representation

**`GaugeFieldData.repJetAlgHom_one`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L159).

> The identity jet acts as the identity.

```lean
lemma repJetAlgHom_one : T.repJetAlgHom 1 = AlgHom.id ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.repJetAlgHom_mul`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L167).

> The action of a product of jets is the composite of the actions.

```lean
lemma repJetAlgHom_mul (U V : G.gaugeJetGroup) :
    T.repJetAlgHom (U * V) = (T.repJetAlgHom U).comp (T.repJetAlgHom V)
```

**`GaugeFieldData.repJet`**, a def, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L183).

> The action of the jet gauge group on the local field algebra.

```lean
noncomputable def repJet : Representation ℂ G.gaugeJetGroup T.LocalFieldAlgebra
```

**`GaugeFieldData.repJet_apply`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L190).

```lean
lemma repJet_apply (U : G.gaugeJetGroup) (x : T.LocalFieldAlgebra) :
    T.repJet U x = T.repJetAlgHom U x
```

**`GaugeFieldData.repJet_apply_mul`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L193).

```lean
lemma repJet_apply_mul (U : G.gaugeJetGroup) (x y : T.LocalFieldAlgebra) :
    T.repJet U (x * y) = T.repJet U x * T.repJet U y
```

**`GaugeFieldData.repJet_apply_one`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L197).

```lean
lemma repJet_apply_one (U : G.gaugeJetGroup) : T.repJet U (1 : T.LocalFieldAlgebra) = 1
```

**`GaugeFieldData.repJet_ιFermion`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L201).

```lean
lemma repJet_ιFermion (U : G.gaugeJetGroup) (i : T.FermionSpecies)
    (x : FieldDerivSpace (T.fermion i)) :
    T.repJet U (T.ιFermion i x) = T.ιFermion i (FieldDerivSpace.repJet (T.fermion i) U x)
```

**`GaugeFieldData.repJet_ιBoson`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L207).

```lean
lemma repJet_ιBoson (U : G.gaugeJetGroup) (j : T.BosonSpecies) (y : FieldDerivSpace (T.boson j)) :
    T.repJet U (T.ιBoson j y) = T.ιBoson j (FieldDerivSpace.repJet (T.boson j) U y)
```

**`GaugeFieldData.repJet_ιConnection`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L212).

```lean
lemma repJet_ιConnection (U : G.gaugeJetGroup) (v : GaugeBoson.FieldDerivSpace G) :
    T.repJet U (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repJet G U (SymmetricAlgebra.ι ℝ _ v))
```

**`GaugeFieldData.repJet_includeConnection`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L220).

> The jet gauge action restricts to the complexified gauge-only action on the connection
> factor.

```lean
lemma repJet_includeConnection (U : G.gaugeJetGroup) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra G) :
    T.repJet U (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepJet G U y)
```

**`GaugeFieldData.repJet_ιConnection_affine`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean#L229).

> The affine gauge law of the connection generators. A jet carries a connection
> generator to the transported generator of its inverse plus the Maurer–Cartan shift, the
> gauge field being a connection and not a tensor. This is the generator-level form of
> `GaugeFieldData.repJet_ιConnection`, with no reference to the connection factor.

```lean
lemma repJet_ιConnection_affine (U : G.gaugeJetGroup) (v : GaugeBoson.FieldDerivSpace G) :
    T.repJet U (T.ιConnection v)
      = T.ιConnection (LocalGaugeFieldAlgebra.transport G U⁻¹ v)
        + (LocalGaugeFieldAlgebra.maurerCartanShift G U⁻¹ v : ℂ) •
          (1 : T.LocalFieldAlgebra)
```

## Depends on

- [The gauge action on the gauge-boson jet algebra](../part-01/gaugeboson-localgaugefieldalgebra-gaugeaction.md)
- [The local field algebra of a gauge theory and its universal property](localfieldalgebra-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/GaugeAction.lean)
