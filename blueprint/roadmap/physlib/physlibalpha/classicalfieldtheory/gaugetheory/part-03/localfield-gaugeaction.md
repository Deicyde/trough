---
declaration: module
origin: cited
lean: GaugeFieldData.gaugeConnection, GaugeFieldData.gaugeAssignment, GaugeFieldData.repJetAlgHom, GaugeFieldData.repJetAlgHom_ιFermion, GaugeFieldData.repJetAlgHom_ιBoson, GaugeFieldData.repJetAlgHom_ιConnection, GaugeFieldData.repJetAlgHom_comp_includeConnection, GaugeFieldData.repJetAlgHom_includeConnection
statement: formalized
proof: formalized
---

# The jet gauge action on the local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.GaugeAction`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean): 20 declarations, 11 with a docstring.

## i. Overview

> The jet gauge group `GJ` acts on the local field algebra `J(T)` of a field datum by algebra
> endomorphisms: on the generators of a matter species by the action
> `JetComponentSpace.repJet` of that species, and on the connection generators by the affine
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

**`GaugeFieldData.gaugeConnection`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L62).

> The connection generators after the action of a jet: the gauge-only action on the
> degree-one element, included into the local field algebra.

```lean
noncomputable def gaugeConnection (U : GJ) :
    GaugeBoson.JetComponentSpace 𝔤 →ₗ[ℝ] T.LocalFieldAlgebra
```

**`GaugeFieldData.gaugeAssignment`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L74).

> The assignment of the generators defining the action of a jet: each matter species
> acts on its own component functions, the connection generators through the gauge-only
> action. The relations hold because the images are generators of the same kind, or lie in
> the central connection factor.

```lean
noncomputable def gaugeAssignment (U : GJ) : T.Assignment T.LocalFieldAlgebra
```

## B. The action of a jet

**`GaugeFieldData.repJetAlgHom`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L94).

> The action of a jet on the local field algebra, as an algebra endomorphism: the lift
> of its gauge assignment.

```lean
noncomputable def repJetAlgHom (U : GJ) : T.LocalFieldAlgebra →ₐ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.repJetAlgHom_ιFermion`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L100).

```lean
lemma repJetAlgHom_ιFermion (U : GJ) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.repJetAlgHom U (T.ιFermion i x)
      = T.ιFermion i (JetComponentSpace.repJet (T.fermion i) U x)
```

**`GaugeFieldData.repJetAlgHom_ιBoson`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L107).

```lean
lemma repJetAlgHom_ιBoson (U : GJ) (j : T.BosonSpecies) (y : JetComponentSpace (T.boson j)) :
    T.repJetAlgHom U (T.ιBoson j y) = T.ιBoson j (JetComponentSpace.repJet (T.boson j) U y)
```

**`GaugeFieldData.repJetAlgHom_ιConnection`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L112).

```lean
lemma repJetAlgHom_ιConnection (U : GJ) (v : GaugeBoson.JetComponentSpace 𝔤) :
    T.repJetAlgHom U (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repJet jets U (SymmetricAlgebra.ι ℝ _ v))
```

## C. The action on the connection factor

**`GaugeFieldData.repJetAlgHom_comp_includeConnection`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L128).

> The action of a jet restricts to the complexified gauge-only action on the connection
> factor, as an equation of algebra maps out of the complexified gauge-only algebra: it is
> enough to compare them on the real generators, where it is the computation rule of the
> lift.

```lean
lemma repJetAlgHom_comp_includeConnection (U : GJ) :
    (T.repJetAlgHom U).comp T.includeConnection
      = T.includeConnection.comp (LocalGaugeFieldAlgebra.complexRepJetAlgHom jets U)
```

**`GaugeFieldData.repJetAlgHom_includeConnection`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L138).

> The action of a jet restricts to the complexified gauge-only action on the connection
> factor.

```lean
lemma repJetAlgHom_includeConnection (U : GJ) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) :
    T.repJetAlgHom U (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepJet jets U y)
```

**`GaugeFieldData.repJetAlgHom_includeConnection_one_tmul`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L145).

> On the real gauge-only algebra, included, a jet acts through the gauge-only action.

```lean
lemma repJetAlgHom_includeConnection_one_tmul (U : GJ) (x : LocalGaugeFieldAlgebra 𝔤) :
    T.repJetAlgHom U (T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] x))
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ] LocalGaugeFieldAlgebra.repJet jets U x)
```

## D. The representation

**`GaugeFieldData.repJetAlgHom_one`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L157).

> The identity jet acts as the identity.

```lean
lemma repJetAlgHom_one : T.repJetAlgHom 1 = AlgHom.id ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.repJetAlgHom_mul`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L165).

> The action of a product of jets is the composite of the actions.

```lean
lemma repJetAlgHom_mul (U V : GJ) :
    T.repJetAlgHom (U * V) = (T.repJetAlgHom U).comp (T.repJetAlgHom V)
```

**`GaugeFieldData.repJet`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L181).

> The action of the jet gauge group on the local field algebra.

```lean
noncomputable def repJet : Representation ℂ GJ T.LocalFieldAlgebra
```

**`GaugeFieldData.repJet_apply`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L188).

```lean
lemma repJet_apply (U : GJ) (x : T.LocalFieldAlgebra) :
    T.repJet U x = T.repJetAlgHom U x
```

**`GaugeFieldData.repJet_apply_mul`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L191).

```lean
lemma repJet_apply_mul (U : GJ) (x y : T.LocalFieldAlgebra) :
    T.repJet U (x * y) = T.repJet U x * T.repJet U y
```

**`GaugeFieldData.repJet_apply_one`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L195).

```lean
lemma repJet_apply_one (U : GJ) : T.repJet U (1 : T.LocalFieldAlgebra) = 1
```

**`GaugeFieldData.repJet_ιFermion`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L199).

```lean
lemma repJet_ιFermion (U : GJ) (i : T.FermionSpecies) (x : JetComponentSpace (T.fermion i)) :
    T.repJet U (T.ιFermion i x) = T.ιFermion i (JetComponentSpace.repJet (T.fermion i) U x)
```

**`GaugeFieldData.repJet_ιBoson`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L204).

```lean
lemma repJet_ιBoson (U : GJ) (j : T.BosonSpecies) (y : JetComponentSpace (T.boson j)) :
    T.repJet U (T.ιBoson j y) = T.ιBoson j (JetComponentSpace.repJet (T.boson j) U y)
```

**`GaugeFieldData.repJet_ιConnection`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L209).

```lean
lemma repJet_ιConnection (U : GJ) (v : GaugeBoson.JetComponentSpace 𝔤) :
    T.repJet U (T.ιConnection v)
      = T.includeConnection ((1 : ℂ) ⊗ₜ[ℝ]
          LocalGaugeFieldAlgebra.repJet jets U (SymmetricAlgebra.ι ℝ _ v))
```

**`GaugeFieldData.repJet_includeConnection`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L217).

> The jet gauge action restricts to the complexified gauge-only action on the connection
> factor.

```lean
lemma repJet_includeConnection (U : GJ) (y : ℂ ⊗[ℝ] LocalGaugeFieldAlgebra 𝔤) :
    T.repJet U (T.includeConnection y)
      = T.includeConnection (LocalGaugeFieldAlgebra.complexRepJet jets U y)
```

**`GaugeFieldData.repJet_ιConnection_affine`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean#L226).

> The affine gauge law of the connection generators: a jet carries a connection
> generator to the transported generator of its inverse plus the Maurer–Cartan shift, the
> gauge field being a connection and not a tensor. This is the generator-level form of
> `GaugeFieldData.repJet_ιConnection`, with no reference to the connection factor.

```lean
lemma repJet_ιConnection_affine (U : GJ) (v : GaugeBoson.JetComponentSpace 𝔤) :
    T.repJet U (T.ιConnection v)
      = T.ιConnection (LocalGaugeFieldAlgebra.transport jets U⁻¹ v)
        + (LocalGaugeFieldAlgebra.mcShift jets U⁻¹ v : ℂ) • (1 : T.LocalFieldAlgebra)
```

## Depends on

- [The local field algebra of a gauge theory and its universal property](localfield-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/GaugeAction.lean)
