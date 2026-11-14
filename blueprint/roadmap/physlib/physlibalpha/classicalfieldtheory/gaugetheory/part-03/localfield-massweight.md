---
declaration: module
origin: cited
lean: GaugeFieldData.massWeightAssignment, GaugeFieldData.massWeightScale, GaugeFieldData.massWeightScale_ιFermion, GaugeFieldData.massWeightScale_ιBoson, GaugeFieldData.massWeightScale_ιConnection, GaugeFieldData.massWeightSubmodule, GaugeFieldData.mem_massWeightSubmodule_iff, GaugeFieldData.massWeightSubmoduleLE
statement: formalized
proof: formalized
---

# The mass-weight filtration and the invariants of a local field algebra

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalField.MassWeight`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean): 26 declarations, 16 with a docstring.

## i. Overview

> The local field algebra of a field datum is graded by mass weight: a generator `∂_s φ_α`
> of a field of mass weight `w` has weight `w + 2 |s|`, a connection generator `∂_s A_μ` has
> weight `2 + 2 |s|`. The grading is recorded by the algebra endomorphisms scaling each
> generator by `c` to its weight, for real `c`; the weight-`n` piece is the common
> eigenspace of eigenvalue `c ^ n`, and the filtration is the join of the pieces of weight
> at most `w`.
>
> Together with the actions of the jet gauge group and of the Lorentz group this gives the
> submodule of gauge and Lorentz invariants of mass weight at most `w`, which is what a
> Lagrangian classification describes. Everything here is generic: a model contributes only
> its datum.

## ii. Key results

> - `GaugeFieldData.massWeightScale` : the scaling of the local field algebra by `c` to the
>   mass weight of each generator.
> - `GaugeFieldData.massWeightSubmodule`, `massWeightSubmoduleLE` : the graded pieces and
>   the filtration.
> - `GaugeFieldData.gaugeInvariants`, `lorentzInvariants`, `invariantsLE` : the invariants,
>   and the invariants of mass weight at most `w`.
> - `GaugeFieldData.bosonNormSq` : the contraction `φ† φ` of a bosonic species with its
>   conjugate through a basis of its value space, the simplest invariant.
> - `GaugeFieldData.invariantsLE_map` : an isomorphism of local field algebras respecting the
>   actions and the scaling carries the invariants of one datum onto those of the other.

## iv. References

> * None.

## A. The mass-weight scaling

**`GaugeFieldData.massWeightAssignment`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L75).

> The assignment scaling each generator by `c` to its mass weight: a component function
> `∂_s φ_α` of a species of mass weight `w` by `c ^ (w + 2 |s|)`, a connection generator
> `∂_s A_μ` by `c ^ (2 + 2 |s|)`. The relations hold because the images are generators of
> the same kind.

```lean
noncomputable def massWeightAssignment (c : ℝ) : T.Assignment T.LocalFieldAlgebra
```

**`GaugeFieldData.massWeightScale`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L89).

> **The mass-weight scaling of the local field algebra**: the algebra endomorphism
> scaling each generator by `c` to its mass weight.

```lean
noncomputable def massWeightScale (c : ℝ) : T.LocalFieldAlgebra →ₐ[ℂ] T.LocalFieldAlgebra
```

**`GaugeFieldData.massWeightScale_ιFermion`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L93).

```lean
lemma massWeightScale_ιFermion (c : ℝ) (i : T.FermionSpecies)
    (x : JetComponentSpace (T.fermion i)) :
    T.massWeightScale c (T.ιFermion i x)
      = T.ιFermion i (JetComponentSpace.massWeightScale (T.fermion i).massWeight (c : ℂ) x)
```

**`GaugeFieldData.massWeightScale_ιBoson`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L100).

```lean
lemma massWeightScale_ιBoson (c : ℝ) (j : T.BosonSpecies)
    (y : JetComponentSpace (T.boson j)) :
    T.massWeightScale c (T.ιBoson j y)
      = T.ιBoson j (JetComponentSpace.massWeightScale (T.boson j).massWeight (c : ℂ) y)
```

**`GaugeFieldData.massWeightScale_ιConnection`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L107).

```lean
lemma massWeightScale_ιConnection (c : ℝ) (v : GaugeBoson.JetComponentSpace 𝔤) :
    T.massWeightScale c (T.ιConnection v)
      = T.ιConnection (GaugeBoson.JetComponentSpace.massWeightScale 𝔤 c v)
```

## B. The graded pieces and the filtration

**`GaugeFieldData.massWeightSubmodule`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L120).

> **The weight-`n` piece** of the local field algebra: the elements scaled by `c ^ n`
> under every mass-weight scaling: the equaliser of the scalings and the scalars.

```lean
noncomputable def massWeightSubmodule (n : ℕ) : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_massWeightSubmodule_iff`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L124).

```lean
lemma mem_massWeightSubmodule_iff {n : ℕ} {x : T.LocalFieldAlgebra} :
    x ∈ T.massWeightSubmodule n ↔ ∀ c : ℝ, T.massWeightScale c x = ((c : ℂ) ^ n) • x
```

**`GaugeFieldData.massWeightSubmoduleLE`**, a def, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L130).

> **The mass-weight filtration**: the join of the pieces of weight at most `w`.

```lean
noncomputable def massWeightSubmoduleLE (w : ℕ) : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.massWeightSubmodule_le_massWeightSubmoduleLE`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L133).

```lean
lemma massWeightSubmodule_le_massWeightSubmoduleLE {k w : ℕ} (h : k ≤ w) :
    T.massWeightSubmodule k ≤ T.massWeightSubmoduleLE w
```

## C. The invariants

**`GaugeFieldData.gaugeInvariants`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L144).

> **The gauge invariants**: the elements fixed by every jet of gauge transformations.

```lean
noncomputable def gaugeInvariants : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_gaugeInvariants_iff`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L148).

```lean
lemma mem_gaugeInvariants_iff {x : T.LocalFieldAlgebra} :
    x ∈ T.gaugeInvariants ↔ ∀ U : GJ, T.repJet U x = x
```

**`GaugeFieldData.lorentzInvariants`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L153).

> **The Lorentz invariants**: the elements fixed by every Lorentz transformation.

```lean
noncomputable def lorentzInvariants : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_lorentzInvariants_iff`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L157).

```lean
lemma mem_lorentzInvariants_iff {x : T.LocalFieldAlgebra} :
    x ∈ T.lorentzInvariants ↔ ∀ Λ : SL(2,ℂ), T.repLorentzGroup Λ x = x
```

**`GaugeFieldData.invariantsLE`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L163).

> **The invariants of mass weight at most `w`**: the gauge and Lorentz invariants in the
> filtration. A Lagrangian of mass dimension at most `w / 2` is an element of it.

```lean
noncomputable def invariantsLE (w : ℕ) : Submodule ℂ T.LocalFieldAlgebra
```

**`GaugeFieldData.mem_invariantsLE_iff`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L166).

```lean
lemma mem_invariantsLE_iff {w : ℕ} {x : T.LocalFieldAlgebra} :
    x ∈ T.invariantsLE w ↔ x ∈ T.massWeightSubmoduleLE w
      ∧ (∀ U : GJ, T.repJet U x = x) ∧ ∀ Λ : SL(2,ℂ), T.repLorentzGroup Λ x = x
```

**`GaugeFieldData.invariantsLE_eq_iff`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L173).

> A description of the invariants of mass weight at most `w`, element by element: an
> element of the filtration fixed by both groups is exactly an element of `Q`.

```lean
lemma invariantsLE_eq_iff (w : ℕ) (Q : Submodule ℂ T.LocalFieldAlgebra) :
    T.invariantsLE w = Q ↔ ∀ x : T.LocalFieldAlgebra,
      (x ∈ T.massWeightSubmoduleLE w ∧ (∀ U : GJ, T.repJet U x = x)
        ∧ ∀ Λ : SL(2,ℂ), T.repLorentzGroup Λ x = x) ↔ x ∈ Q
```

**`GaugeFieldData.invariantsLE_inf_eq_iff`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L181).

> A description of the invariants of mass weight at most `w` lying in a submodule `A`,
> element by element.

```lean
lemma invariantsLE_inf_eq_iff (w : ℕ) (A Q : Submodule ℂ T.LocalFieldAlgebra) :
    T.invariantsLE w ⊓ A = Q ↔ ∀ x : T.LocalFieldAlgebra,
      (x ∈ T.massWeightSubmoduleLE w ∧ x ∈ A ∧ (∀ U : GJ, T.repJet U x = x)
        ∧ ∀ Λ : SL(2,ℂ), T.repLorentzGroup Λ x = x) ↔ x ∈ Q
```

## D. The contraction of a boson with its conjugate

**`GaugeFieldData.bosonNormSq`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L197).

> **The contraction `φ† φ`** of a bosonic species with its conjugate, through a basis of
> its value space: the sum over the basis of the conjugate coordinate times the coordinate.
> For a scalar in a unitary representation it is the mass term.

```lean
noncomputable def bosonNormSq (j : T.BosonSpecies) {ι : Type} [Fintype ι] [DecidableEq ι]
    (b : Module.Basis ι ℂ (T.BosonValue j)) : T.LocalFieldAlgebra
```

## E. Transport along an isomorphism

> An isomorphism of local field algebras intertwining the jet gauge action, the Lorentz
> action and the mass-weight scaling carries the graded pieces, the filtration and the
> invariants of one datum onto those of the other. This is what relates two presentations
> of the same field content, such as a model's table and a hand-built datum.

**`GaugeFieldData.mem_massWeightSubmodule_apply_iff`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L218).

> The mass-weight scaling is respected: the weight-`n` piece is carried onto the
> weight-`n` piece.

```lean
lemma mem_massWeightSubmodule_apply_iff
    (hscale : ∀ (c : ℝ) x, e (T.massWeightScale c x) = T'.massWeightScale c (e x))
    (n : ℕ) (x : T.LocalFieldAlgebra) :
    e x ∈ T'.massWeightSubmodule n ↔ x ∈ T.massWeightSubmodule n
```

**`GaugeFieldData.massWeightSubmodule_map`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L224).

```lean
lemma massWeightSubmodule_map
    (hscale : ∀ (c : ℝ) x, e (T.massWeightScale c x) = T'.massWeightScale c (e x)) (n : ℕ) :
    (T.massWeightSubmodule n).map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.massWeightSubmodule n
```

**`GaugeFieldData.massWeightSubmoduleLE_map`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L233).

```lean
lemma massWeightSubmoduleLE_map
    (hscale : ∀ (c : ℝ) x, e (T.massWeightScale c x) = T'.massWeightScale c (e x)) (w : ℕ) :
    (T.massWeightSubmoduleLE w).map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.massWeightSubmoduleLE w
```

**`GaugeFieldData.gaugeInvariants_map`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L240).

> The gauge invariants are carried onto the gauge invariants.

```lean
lemma gaugeInvariants_map (hjet : ∀ (U : GJ) x, e (T.repJet U x) = T'.repJet U (e x)) :
    T.gaugeInvariants.map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.gaugeInvariants
```

**`GaugeFieldData.lorentzInvariants_map`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L249).

> The Lorentz invariants are carried onto the Lorentz invariants.

```lean
lemma lorentzInvariants_map
    (hlor : ∀ (Λ : SL(2,ℂ)) x, e (T.repLorentzGroup Λ x) = T'.repLorentzGroup Λ (e x)) :
    T.lorentzInvariants.map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.lorentzInvariants
```

**`GaugeFieldData.mem_massWeightSubmoduleLE_apply_iff`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L259).

> The filtration is respected, element by element.

```lean
lemma mem_massWeightSubmoduleLE_apply_iff
    (hscale : ∀ (c : ℝ) x, e (T.massWeightScale c x) = T'.massWeightScale c (e x)) (w : ℕ)
    (x : T.LocalFieldAlgebra) :
    e x ∈ T'.massWeightSubmoduleLE w ↔ x ∈ T.massWeightSubmoduleLE w
```

**`GaugeFieldData.mem_invariantsLE_apply_iff`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L267).

> The invariants of mass weight at most `w` are respected, element by element.

```lean
lemma mem_invariantsLE_apply_iff (hjet : ∀ (U : GJ) x, e (T.repJet U x) = T'.repJet U (e x))
    (hlor : ∀ (Λ : SL(2,ℂ)) x, e (T.repLorentzGroup Λ x) = T'.repLorentzGroup Λ (e x))
    (hscale : ∀ (c : ℝ) x, e (T.massWeightScale c x) = T'.massWeightScale c (e x)) (w : ℕ)
    (x : T.LocalFieldAlgebra) :
    e x ∈ T'.invariantsLE w ↔ x ∈ T.invariantsLE w
```

**`GaugeFieldData.invariantsLE_map`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean#L277).

> **The invariants of mass weight at most `w` are carried onto the invariants of mass
> weight at most `w`** by an isomorphism respecting the two actions and the scaling.

```lean
lemma invariantsLE_map (hjet : ∀ (U : GJ) x, e (T.repJet U x) = T'.repJet U (e x))
    (hlor : ∀ (Λ : SL(2,ℂ)) x, e (T.repLorentzGroup Λ x) = T'.repLorentzGroup Λ (e x))
    (hscale : ∀ (c : ℝ) x, e (T.massWeightScale c x) = T'.massWeightScale c (e x)) (w : ℕ) :
    (T.invariantsLE w).map (e : T.LocalFieldAlgebra →ₗ[ℂ] T'.LocalFieldAlgebra)
      = T'.invariantsLE w
```

## Depends on

- [Mass dimension on the gauge-boson jet algebra](../part-01/gaugeboson-localgauge-massdim.md)
- [The field symbols of the local field algebra and their transformation laws](../part-04/localfield-transformsin.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalField/MassWeight.lean)
