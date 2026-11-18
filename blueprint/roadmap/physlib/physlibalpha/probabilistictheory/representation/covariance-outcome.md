---
declaration: module
origin: cited
lean: BoundedMeasurable.inducedChannel, BoundedMeasurable.inducedChannel_apply, BoundedMeasurable.isOrderAutomorphism_inducedChannel, BoundedMeasurable.inducedAction, BoundedMeasurable.inducedAction_val, BoundedMeasurable.comap_isCovariant, ProbabilisticTheory.Measurement.IsCovariant, ProbabilisticTheory.Measurement.IsCovariant.comp
statement: formalized
proof: formalized
---

# Covariance of measurements under an action on the outcomes

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Covariance.Outcome`, [PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean): 11 declarations (1 instance with no name), 11 with a docstring.

> Covariance of measurements under a group action on outcomes, and its preservation.

## i. Overview

> A group `G` acting measurably on an outcome space `Ω` acts on the classical system of `Ω` by
> relabeling: `σ` sends an observable `f` to `x ↦ f (σ⁻¹ • x)`. The inverse makes this a left
> action. A measurement is a channel out of the classical system, so its covariance, matched to a
> symmetry action `ρ` on the physical system, is just covariance of that channel.
>
> Post-processing a measurement is composing its channel with a classical channel, so covariance is
> preserved by covariant post-processing. In particular, relabeling the outcomes along an
> equivariant map preserves covariance, and the marginals of a covariant joint measurement, for the
> diagonal action on a product of outcome spaces, are covariant.

## ii. Key results

> - `BoundedMeasurable.inducedAction` : the action of `G` on the classical system of `Ω`.
> - `BoundedMeasurable.comap_isCovariant` : relabeling along an equivariant map is covariant.
> - `Measurement.IsCovariant` : covariance of a measurement.
> - `Measurement.IsCovariant.comp` : covariant post-processing preserves covariance.
> - `Measurement.IsCovariant.mapOutcome` : equivariant relabeling preserves covariance.
> - `Measurement.IsCovariant.marginal` : marginals of a covariant joint measurement are covariant.

## iv. References

> * None.

## A. The induced action on the classical system

### A.1. The relabeling channels

**`BoundedMeasurable.inducedChannel`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L69).

> The channel on the classical system that relabels outcomes by `σ`:
> `f ↦ (x ↦ f (σ⁻¹ • x))`.

```lean
def inducedChannel (σ : G) : Channel (BoundedMeasurable Ω) (BoundedMeasurable Ω)
```

**`BoundedMeasurable.inducedChannel_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L74).

> The relabeling channel evaluates an observable at the relabeled outcome.

```lean
lemma inducedChannel_apply (σ : G) (f : BoundedMeasurable Ω) (x : Ω) :
    inducedChannel σ f x = f (σ⁻¹ • x)
```

**`BoundedMeasurable.isOrderAutomorphism_inducedChannel`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L79).

> Relabeling by `σ⁻¹` undoes relabeling by `σ`, so each relabeling channel is an
> order-automorphism.

```lean
lemma isOrderAutomorphism_inducedChannel (σ : G) :
    IsOrderAutomorphism (inducedChannel (Ω := Ω) σ)
```

### A.2. The induced action

**`BoundedMeasurable.inducedAction`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L88).

> The action of `G` on the classical system of `Ω` induced by its action on the outcomes.

```lean
noncomputable def inducedAction : G →* Symmetry (BoundedMeasurable Ω)
```

**`BoundedMeasurable.inducedAction_val`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L96).

> The channel underlying the induced action of `σ` is the relabeling channel of `σ`.

```lean
lemma inducedAction_val (σ : G) :
    (inducedAction σ : Symmetry (BoundedMeasurable Ω)).1 = inducedChannel σ
```

### A.3. The diagonal action on a product of outcome spaces

**An instance with no name**, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L104).

> The diagonal action on a product of outcome spaces is measurable.

```lean
instance : MeasurableAction G (Ω × Ω')
```

### A.4. Relabeling along an equivariant map

**`BoundedMeasurable.comap_isCovariant`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L111).

> Relabeling along an equivariant measurable map is a covariant classical channel.

```lean
lemma comap_isCovariant (g : Ω' → Ω) (hg : Measurable g)
    (hequiv : ∀ (σ : G) x, g (σ • x) = σ • g x) :
    (comap g hg).IsCovariant (inducedAction (G := G)) (inducedAction (G := G))
```

## B. Covariant measurements

### B.1. The definition of covariance

**`ProbabilisticTheory.Measurement.IsCovariant`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L134).

> A measurement is covariant for an action on its outcomes, matched to the symmetry action `ρ`
> on the system, when its channel intertwines the two actions.

```lean
def IsCovariant (ρ : G →* Symmetry E) (M : Measurement Ω E) : Prop
```

### B.2. Covariant post-processing

**`ProbabilisticTheory.Measurement.IsCovariant.comp`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L141).

> Post-processing a covariant measurement by a covariant classical channel gives a covariant
> channel.

```lean
lemma IsCovariant.comp {ρ : G →* Symmetry E} {M : Measurement Ω E}
    {K : Channel (BoundedMeasurable Ω') (BoundedMeasurable Ω)} (hM : M.IsCovariant ρ)
    (hK : K.IsCovariant (inducedAction (G := G)) inducedAction) :
    (M.toChannel.comp K).IsCovariant inducedAction ρ
```

**`ProbabilisticTheory.Measurement.IsCovariant.mapOutcome`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L149).

> Relabeling the outcomes of a covariant measurement along an equivariant map gives a
> covariant measurement.

```lean
lemma IsCovariant.mapOutcome {ρ : G →* Symmetry E} {N : Measurement Ω' E} (hN : N.IsCovariant ρ)
    (g : Ω' → Ω) (hg : Measurable g) (hequiv : ∀ (σ : G) x, g (σ • x) = σ • g x) :
    (N.mapOutcome g hg).IsCovariant ρ
```

### B.3. Marginals of a covariant joint measurement

**`ProbabilisticTheory.Measurement.IsCovariant.marginal`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean#L158).

> The first marginal of a covariant joint measurement, for the diagonal action on the product
> of outcome spaces, is covariant.

```lean
lemma IsCovariant.marginal {ρ : G →* Symmetry E} {J : Measurement (Ω × Ω') E}
    (hJ : J.IsCovariant ρ) :
    (J.mapOutcome Prod.fst measurable_fst).IsCovariant ρ
```

## Depends on

- [Post-processing of measurements](../measurement/postprocessing.md)
- [Covariant measurements and channels](covariance-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Covariance/Outcome.lean)
