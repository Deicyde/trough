---
declaration: module
origin: cited
lean: StandardModel.AlgebraRealization.id
statement: formalized
proof: formalized
---

# The jet algebra of the Standard Model is a Standard Model (Realization)

The module `PhyslibAlpha.Particles.StandardModel.JetAlgebra.Realization`, [PhyslibAlpha/Particles/StandardModel/JetAlgebra/Realization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Realization.lean): 1 declaration, 1 with a docstring.

## i. Overview

> `AlgebraRealization` asks an algebra for an equivariant algebra map out of the jet algebra
> of the Standard Model. The jet algebra therefore carries one for free — the identity — and
> that is all this file records. The four compatibility laws hold by definition, and the two
> multiplicativity laws are the ones the jet gauge action and the Lorentz action were shown
> to satisfy when they were built.
>
> It is the point at which the abstract theory of `AlgebraRealization` — its covariant
> reduction, its mass-weight filtration and its classification of invariants — becomes a
> theory of the concrete algebra in which a Standard Model Lagrangian is written, and it is
> the first file on the concrete side of that divide. What the instance then buys, once the
> covariant reduction is available, is [`CovJetAlgebra/Basic.lean`](jetalgebra-covjetalgebra-basic.md);
> what it buys for the classification is
> [`AlgebraRealization.lean`](../part-07/jetalgebra-algebrarealization.md).

## ii. Key results

> - `StandardModel.AlgebraRealization.id` : the jet algebra of the Standard Model is a
>   Standard Model, along the identity algebra map.

## iv. References

> * None.

## A. The identity realization

**`StandardModel.AlgebraRealization.id`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Realization.lean#L58).

> The jet algebra of the Standard Model is a Standard Model: it is one along the identity
> algebra map.

```lean
noncomputable def id : AlgebraRealization JetAlgebra JetAlgebra.repJetGaugeGroupI
    JetAlgebra.repLorentzGroup JetAlgebra.massWeightPoly
```

## Depends on

- [The algebra valued Standard model](../part-09/realization-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/JetAlgebra/Realization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/JetAlgebra/Realization.lean)
