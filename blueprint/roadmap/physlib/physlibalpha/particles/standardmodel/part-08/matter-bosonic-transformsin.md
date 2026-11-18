---
declaration: module
origin: cited
lean: StandardModel.BosonicAlgebra.repJetGaugeGroupI_iteratedJetDeriv_ofField, StandardModel.BosonicAlgebra.transformsIn_iteratedJetDeriv_ofField, StandardModel.BosonicAlgebra.repJetGaugeGroupI_iteratedJetDeriv_ofConjField, StandardModel.BosonicAlgebra.transformsIn_iteratedJetDeriv_ofConjField
statement: formalized
proof: formalized
---

# The transformation law of the bosonic generators

The module `PhyslibAlpha.Particles.StandardModel.Matter.Bosonic.TransformsIn`, [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean): 4 declarations, 4 with a docstring; 2 private, not shown.

## i. Overview

> `BosonicAlgebra.repJetGaugeGroupI_ofField` records that the undifferentiated generator
> `ψ_φ` transforms by the value of the gauge transformation at the base point. Its derivatives
> do not: a jet of gauge transformations mixes `∂_s ψ_φ` with the lower generators
> `∂_{s₂} ψ_φ`, weighted by the base-point Taylor coefficients
> `GaugeAlgebraRealization.repDualCoeff` of the gauge jet at the complementary multiset `s₁`.
> This file proves that all-orders Leibniz law, in the form `LocalGaugeData.TransformsIn`
> demands.
>
> All the work is in `StandardModel.repDual_basis_tmul`, the corresponding statement on the
> jet component space. The symmetric algebra contributes only linearity: the generators are
> the image of the component space under `SymmetricAlgebra.ι`, and a multiset sum passes
> through a linear map.
>
> The conjugate generators are the same statement for the conjugate action
> `JetComponentSpace.repConj M.repJet` on
> the jets of the conjugate field, which is what the conjugate half of the component space
> carries; so they are an instance of the same lemma, not a second proof.

## ii. Key results

> - `BosonicAlgebra.repJetGaugeGroupI_iteratedJetDeriv_ofField` : the transformation law of
>   the derivative generators `∂_s ψ_φ`.
> - `BosonicAlgebra.repJetGaugeGroupI_iteratedJetDeriv_ofConjField` : the transformation
>   law of the conjugate derivative generators `∂_s ψ̄_φ`.
> - `BosonicAlgebra.transformsIn_iteratedJetDeriv_ofField`,
>   `BosonicAlgebra.transformsIn_iteratedJetDeriv_ofConjField` : the same, packaged as
>   `LocalGaugeData.TransformsIn`.

## iv. References

> * None.

## A. Multiset sums of generators

## B. The transformation law of the derivative generators

### B.1. The field

**`StandardModel.BosonicAlgebra.repJetGaugeGroupI_iteratedJetDeriv_ofField`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean#L119).

> The transformation law of the derivative generators of a matter field: a jet of gauge
> transformations mixes `∂_s ψ_φ` with the lower generators, each splitting `s = s₁ + s₂` of
> the derivative multiset contributing the base-point Taylor coefficient of the gauge jet at
> `s₁` acting on the target index of `∂_{s₂} ψ_φ`. There is no inhomogeneous term: unlike a
> gauge field, a matter field transforms linearly.

```lean
lemma repJetGaugeGroupI_iteratedJetDeriv_ofField
    (U : GJ) (φ : Module.Dual ℂ M.V) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repJetGaugeGroupI M U (iteratedJetDeriv s (ofField φ)) =
      (s.antidiagonal.map fun p =>
        iteratedJetDeriv p.2
          (ofField (GaugeAlgebraRealization.repDualCoeff M.repJet U⁻¹ p.1 φ))).sum
```

**`StandardModel.BosonicAlgebra.transformsIn_iteratedJetDeriv_ofField`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean#L139).

> The derivative generators of a matter field transform in the representation `rep`
> carried by its jets, in the sense demanded by `LocalGaugeData.TransformsIn`.

```lean
lemma transformsIn_iteratedJetDeriv_ofField :
    LocalGaugeData.TransformsIn (repJetGaugeGroupI M) M.repJet
      fun s => (iteratedJetDeriv s).comp (ofField (M := M))
```

### B.2. The conjugate field

**`StandardModel.BosonicAlgebra.repJetGaugeGroupI_iteratedJetDeriv_ofConjField`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean#L154).

> The transformation law of the derivative generators of the conjugate matter field. It
> is the law of the field itself for the conjugate action `JetComponentSpace.repConj M.repJet` on
> the jets of the
> conjugate field — the physicists' `ψ̄ ↦ ψ̄ U†` and its derivatives.

```lean
lemma repJetGaugeGroupI_iteratedJetDeriv_ofConjField
    (U : GJ) (φ : Module.Dual ℂ (ConjModule M.V))
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    repJetGaugeGroupI M U (iteratedJetDeriv s (ofConjField φ)) =
      (s.antidiagonal.map fun p =>
        iteratedJetDeriv p.2
          (ofConjField
            (GaugeAlgebraRealization.repDualCoeff (JetComponentSpace.repConj M.repJet) U⁻¹ p.1
              φ))).sum
```

**`StandardModel.BosonicAlgebra.transformsIn_iteratedJetDeriv_ofConjField`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean#L179).

> The derivative generators of the conjugate matter field transform in the conjugate
> representation `JetComponentSpace.repConj M.repJet`, in the sense demanded by
> `LocalGaugeData.TransformsIn`.

```lean
lemma transformsIn_iteratedJetDeriv_ofConjField :
    LocalGaugeData.TransformsIn (repJetGaugeGroupI M) (JetComponentSpace.repConj M.repJet)
      fun s => (iteratedJetDeriv s).comp (ofConjField (M := M))
```

## Depends on

- [The gauge action on the bosonic algebra](matter-bosonic-gaugeaction.md)
- [The formal total derivative on the bosonic algebra](matter-bosonic-jetderiv.md)

## Proof depends on

- [The transformation law of a derivative symbol](../../../classicalfieldtheory/gaugetheory/part-06/matterfield-jetcomponent-transformsin.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Matter/Bosonic/TransformsIn.lean)
