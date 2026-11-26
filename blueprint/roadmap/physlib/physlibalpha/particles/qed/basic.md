---
declaration: module
origin: cited
lean: QED.indexList, QED.indexList_zero, QED.indexList_singleton, QED.mem_indexList, QED.indexList_length, QED.classRep, QED.classRep_mem, QED.derivSum
statement: formalized
proof: formalized
---

# The jet algebras of quantum electrodynamics

The module `PhyslibAlpha.Particles.QED.Basic`, [PhyslibAlpha/Particles/QED/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean): 145 declarations (5 instances with no name), 98 with a docstring.

> The jet algebras of the photon, of the Dirac electron and of QED, with their gauge, Lorentz
> and mass-weight actions.

## i. Overview

> This file contains the basic definitions of the jet-algebra formulation of
> quantum electrodynamics. These are the jet algebras of the photon and of the Dirac
> electron, their tensor product (the QED jet algebra), the data of a gauge
> transformation as seen by jets, the gauge actions on all three algebras, and
> the evaluation of the photon jet algebra on an honest electromagnetic
> potential.
>
> The *fields* of QED (the jet coordinates, the field strength, the γ matrices
> and the covariant derivatives) are defined on top of these algebras in
> `PhyslibAlpha.Particles.QED.Fields`, and the Lagrangian in
> `PhyslibAlpha.Particles.QED.Lagrangian`. All
> theorems about them are proved in the definition-free files
> `PhyslibAlpha.Particles.QED.FermionStatistics`, `PhyslibAlpha.Particles.QED.FieldStrength`,
> `PhyslibAlpha.Particles.QED.GammaMatrices`, `PhyslibAlpha.Particles.QED.GaugeInvariance` and
> `PhyslibAlpha.Particles.QED.Evaluation`.
>
> The design choices:
>
> * The photon jet algebra is the free commutative algebra on formal symbols
>   `∂_s A_μ`, one for every multiset `s` of spacetime directions and every
>   Lorentz index `μ`, built directly on the electromagnetic potential of
>   `Physlib.Electromagnetism`.  It deliberately does not use
>   the hypercharge boson of the Standard Model. The `B` boson is the
>   gauge boson of `U(1)_Y` before electroweak symmetry breaking, the photon is
>   the mixed combination `A = cos θ_W B + sin θ_W W³`, and the two are not the
>   same field.  Building directly on `ElectromagneticPotential` also avoids
>   inheriting the Standard Model charge normalisation `6Y`, which has no
>   meaning for `U(1)_em`.
>
> * The electron jet algebra is the free *exterior* algebra on formal symbols
>   `∂_s ψ_α`, `∂_s ψ̄_α` with `α : Fin 2 ⊕ Fin 2` a Dirac index in the chiral
>   representation; the exterior product implements fermionic statistics.  A
>   faithful QED matter sector needs a Dirac electron, equivalently two Weyl
>   spinors of the same chirality with charges `±1`. This is what makes the
>   dimension-three mass term `m ψ̄ ψ` possible, as a single Weyl fermion admits no
>   such term.
>
> * A gauge transformation is recorded by its jets: the derivative jets
>   `∂_s χ` of the real gauge function together with the derivative jets
>   `∂_s (exp (I e χ))` of its unitary phase, related by the formal Leibniz
>   identity `∂_μ u = I e (∂_μ χ) u`.  The action on the photon coordinates is
>   the affine shift `∂_s A_μ ↦ ∂_s A_μ + ∂_s ∂_μ χ`, and on the electron
>   coordinates the Leibniz expansion of `∂_s (ū ψ)` over
>   `Multiset.antidiagonal s`, whose multiplicities are exactly the multinomial
>   coefficients of the Leibniz rule.
>
> The gauge-theory framework of `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory` builds the
> analogous algebras for a general gauge group from representation-theoretic data.

## ii. Key results

> - `Photon.JetGenerators`, `Photon.JetAlgebra`, `Photon.JetAlgebra.coord` :
>   the photon jet coordinates `∂_s A_μ` and their polynomial algebra.
> - `Photon.JetAlgebra.gaugeAction` : the affine gauge action on the photon jet
>   algebra.
> - `Photon.JetAlgebra.evalPotential` : the evaluation of the photon jet
>   algebra on an electromagnetic potential.
> - `GaugeJet` : the jets of a `U(1)_em` gauge transformation with coupling `e`.
> - `Electron.JetGenerators`, `Electron.JetAlgebra` : the electron jet
>   coordinates `∂_s ψ_α`, `∂_s ψ̄_α` and their exterior algebra.
> - `Electron.JetAlgebra.gaugeAction` : the Leibniz gauge action on the
>   electron jet algebra.
> - `JetAlgebra` : the QED jet algebra, the tensor product of the complexified
>   photon jet algebra with the electron jet algebra.
> - `JetAlgebra.gaugeAction` : the gauge action on the QED jet algebra.
> - `JetAlgebra.lorentzAction` : the Lorentz action on the QED jet algebra,
>   through the covering map `Lorentz.SL2C.toLorentzGroup` on the photon factor
>   and the Dirac spinor representation `Electron.JetAlgebra.spinorRep` on the
>   electron factor.
> - `JetAlgebra.massScale` : the mass-weight scaling on the QED jet algebra.

## iv. References

> The concrete electromagnetic side is
> `Physlib/Electromagnetism/Kinematics/GaugeTransformation.lean` and
> `Physlib/Electromagnetism/Dynamics/KineticTerm.lean`.

## A. Transport of derivative indices along a Lorentz transformation

> A jet coordinate carries a multiset of derivative indices, each of which
> transforms with `Λ⁻¹` under a Lorentz transformation (the chain rule for
> `x ↦ Λ⁻¹ x`).  To sum over the transformed indices without summing over
> functions on a multiset, the transport recurses along the *canonical sorted
> list* of the multiset, threading the chosen indices through a continuation.

**`QED.indexList`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L151).

> The canonical sorted list of a multiset of spacetime directions, sorted
> through `Fin 1 ⊕ Fin 3 ≃ Fin 4`.

```lean
noncomputable def indexList (s : Multiset (Fin 1 ⊕ Fin 3)) : List (Fin 1 ⊕ Fin 3)
```

**`QED.indexList_zero`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L156).

```lean
lemma indexList_zero : indexList 0 = []
```

**`QED.indexList_singleton`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L160).

```lean
lemma indexList_singleton (μ : Fin 1 ⊕ Fin 3) : indexList {μ} = [μ]
```

**`QED.mem_indexList`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L164).

> The list of derivative directions has the elements of the multiset.

```lean
lemma mem_indexList {t : Multiset (Fin 1 ⊕ Fin 3)} {a : Fin 1 ⊕ Fin 3} :
    a ∈ indexList t ↔ a ∈ t
```

**`QED.indexList_length`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L174).

> The list of derivative directions has the length of the multiset.

```lean
lemma indexList_length (t : Multiset (Fin 1 ⊕ Fin 3)) :
    (indexList t).length = Multiset.card t
```

**`QED.classRep`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L180).

> The canonical representative of a nonempty multiset of spacetime
> directions, the head of its canonical sorted list.

```lean
noncomputable def classRep (t : Multiset (Fin 1 ⊕ Fin 3)) : Fin 1 ⊕ Fin 3
```

**`QED.classRep_mem`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L184).

> The representative of a nonempty multiset of directions lies in it.

```lean
lemma classRep_mem {t : Multiset (Fin 1 ⊕ Fin 3)} (ht : t ≠ 0) : classRep t ∈ t
```

**`QED.derivSum`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L200).

> The Lorentz transport of a family indexed by derivative multisets along a
> list of derivative directions. Each direction in the list is summed against
> a row of `Λ⁻¹`, and the chosen directions accumulate in the multiset
> argument of the continuation `k`.

```lean
noncomputable def derivSum {M : Type*} [AddCommMonoid M] [Module ℝ M]
    (Λ : LorentzGroup 3) :
    List (Fin 1 ⊕ Fin 3) → (Multiset (Fin 1 ⊕ Fin 3) → M) → M
```

**`QED.derivSum_nil`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L207).

```lean
lemma derivSum_nil {M : Type*} [AddCommMonoid M] [Module ℝ M]
    (Λ : LorentzGroup 3) (k : Multiset (Fin 1 ⊕ Fin 3) → M) :
    derivSum Λ [] k = k 0
```

**`QED.derivSum_cons`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L212).

```lean
lemma derivSum_cons {M : Type*} [AddCommMonoid M] [Module ℝ M]
    (Λ : LorentzGroup 3) (σ : Fin 1 ⊕ Fin 3) (l : List (Fin 1 ⊕ Fin 3))
    (k : Multiset (Fin 1 ⊕ Fin 3) → M) :
    derivSum Λ (σ :: l) k =
      ∑ τ, (Λ⁻¹).1 τ σ • derivSum Λ l fun t => k (t + {τ})
```

## B. The jet algebra of the photon

### B.1. The jet coordinates

> A jet coordinate is a formal symbol `∂_s A_μ`, where `s` is a *multiset* of
> spacetime directions: for a smooth potential the partial derivatives commute,
> so only the number of times each direction occurs matters.  The jet algebra is
> the algebra of real polynomials in these symbols.

**`QED.Photon.JetGenerators`**, an inductive, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L235).

> The jet coordinates of the electromagnetic potential, the symbol `∂_s A_μ`,
> the `s`-th derivative of the `μ`-th covariant component.

```lean
inductive JetGenerators where
  /-- The jet coordinate `∂_s A_μ`. -/
  | dA (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) : JetGenerators
  deriving DecidableEq
```

**`QED.Photon.JetGenerators.massWeight`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L242).

> The mass weight (twice the mass dimension) of a photon jet coordinate.
> The potential has mass dimension one and each derivative adds one.

```lean
def JetGenerators.massWeight : JetGenerators → ℕ
```

**`QED.Photon.JetGenerators.indexClass`**, a def, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L248).

> The symmetrized-index class of a photon jet coordinate. Under a gauge
> transformation `∂_s A_μ` shifts by `∂_s ∂_μ χ`, which depends only on the
> multiset `s + {μ}`.  Coordinates in a common class shift together.

```lean
def JetGenerators.indexClass : JetGenerators → Multiset (Fin 1 ⊕ Fin 3)
```

**`QED.Photon.JetGenerators.classProj`**, a def, [line 253](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L253).

> The canonical jet coordinate of a symmetrized-index class. The coordinate
> whose Lorentz index is the canonical representative of the class.

```lean
noncomputable def JetGenerators.classProj (j : JetGenerators) : JetGenerators
```

**`QED.Photon.JetAlgebra`**, an abbrev, [line 257](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L257).

> The jet algebra of the photon, real polynomials in the jet coordinates.

```lean
abbrev JetAlgebra : Type
```

**`QED.Photon.JetAlgebra.coord`**, a def, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L262).

> The jet coordinate `∂_s A_μ` as an element of the jet algebra.

```lean
noncomputable def coord (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) : JetAlgebra
```

### B.2. The gauge action on the photon jet algebra

> A `U(1)_em` gauge transformation sends `A_μ ↦ A_μ + ∂_μ χ`, hence on jet
> coordinates `∂_s A_μ ↦ ∂_s A_μ + ∂_s ∂_μ χ`.  All that the photon jet algebra
> sees of the gauge function `χ` is the family of its symmetrised derivatives at
> the base point, which is what `GaugeJet` records; the shift of `∂_s A_μ` is
> then the value of that family at `s + {μ}`.

**`QED.Photon.JetAlgebra.GaugeJet`**, an abbrev, [line 280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L280).

> A photon gauge jet, the family `s ↦ ∂_s χ` of symmetrised derivatives of a
> gauge function at the base point.  This is all the photon jet algebra sees of
> a gauge transformation.

```lean
abbrev GaugeJet : Type
```

**`QED.Photon.JetAlgebra.gaugeAction`**, a def, [line 284](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L284).

> The gauge action on the photon jet algebra, the algebra map determined by
> `∂_s A_μ ↦ ∂_s A_μ + ∂_s ∂_μ χ`.

```lean
noncomputable def gaugeAction (c : GaugeJet) : JetAlgebra →ₐ[ℝ] JetAlgebra
```

**`QED.Photon.JetAlgebra.gaugeAction_coord`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L289).

```lean
lemma gaugeAction_coord (c : GaugeJet) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    gaugeAction c (coord s μ) = coord s μ + MvPolynomial.C (c (s + {μ}))
```

**`QED.Photon.JetAlgebra.gaugeAction_C`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L295).

> The gauge action on the photon jet algebra fixes the constants.

```lean
lemma gaugeAction_C (c : GaugeJet) (r : ℝ) :
    gaugeAction c (MvPolynomial.C r) = MvPolynomial.C r
```

### B.3. Iterated derivatives indexed by a multiset

> To evaluate a jet coordinate on a potential we must differentiate along a
> multiset of directions, so we must choose an order; we choose the canonical
> one, sorting `s` through `Fin 1 ⊕ Fin 3 ≃ Fin 4`.  For a `C^∞` potential the
> choice is immaterial, by Clairaut's theorem (`SpaceTime.deriv_commute`).

**`QED.Photon.JetAlgebra.derivMultiset`**, a def, [line 312](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L312).

> The iterated partial derivative `∂_s f` along a multiset `s` of spacetime
> directions, taken in the canonical order obtained by sorting `s`.

```lean
noncomputable def derivMultiset (s : Multiset (Fin 1 ⊕ Fin 3)) (f : SpaceTime 3 → ℝ) :
    SpaceTime 3 → ℝ
```

**`QED.Photon.JetAlgebra.derivMultiset_zero`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L318).

```lean
lemma derivMultiset_zero (f : SpaceTime 3 → ℝ) : derivMultiset 0 f = f
```

**`QED.Photon.JetAlgebra.derivMultiset_singleton`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L322).

```lean
lemma derivMultiset_singleton (μ : Fin 1 ⊕ Fin 3) (f : SpaceTime 3 → ℝ) :
    derivMultiset {μ} f = ∂_ μ f
```

### B.4. Evaluation on a potential

> `ElectromagneticPotential` stores the contravariant components `A^μ`, whereas
> a gauge potential carries a lower index, so the jet coordinate `∂_s A_μ`
> evaluates to the `s`-th derivative of `A_μ = η_{μμ} A^μ`.

**`QED.Photon.JetAlgebra.coPotential`**, a def, [line 337](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L337).

> The covariant components `A_μ = η_{μμ} A^μ` of an electromagnetic potential.

```lean
noncomputable def coPotential (A : ElectromagneticPotential 3) (μ : Fin 1 ⊕ Fin 3) :
    SpaceTime 3 → ℝ
```

**`QED.Photon.JetAlgebra.evalPotential`**, a def, [line 343](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L343).

> The evaluation of the photon jet algebra at an electromagnetic potential `A`,
> the algebra map sending the formal jet coordinate `∂_s A_μ` to the honest
> function `∂_s A_μ` on spacetime.

```lean
noncomputable def evalPotential (A : ElectromagneticPotential 3) :
    JetAlgebra →ₐ[ℝ] (SpaceTime 3 → ℝ)
```

**`QED.Photon.JetAlgebra.evalPotential_coord`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L349).

```lean
lemma evalPotential_coord (A : ElectromagneticPotential 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) :
    evalPotential A (coord s μ) = derivMultiset s (coPotential A μ)
```

### B.5. The Lorentz action on the photon jet algebra

> Under a Lorentz transformation the potential transforms as a covector field,
> `A'(x) = (Λ⁻¹)ᵀ A (Λ⁻¹ x)`, so every lower index of the jet coordinate
> `∂_s A_μ`, the index `μ` and each derivative index in `s`, is summed
> against a row of `Λ⁻¹`.

**`QED.Photon.JetAlgebra.lorentzAction`**, a def, [line 367](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L367).

> The Lorentz action on the photon jet algebra, the algebra map transporting
> every lower index of `∂_s A_μ` with `Λ⁻¹`.

```lean
noncomputable def lorentzAction (Λ : LorentzGroup 3) : JetAlgebra →ₐ[ℝ] JetAlgebra
```

**`QED.Photon.JetAlgebra.lorentzAction_coord`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L373).

```lean
lemma lorentzAction_coord (Λ : LorentzGroup 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) :
    lorentzAction Λ (coord s μ) =
      derivSum Λ (indexList s) fun t => ∑ ν, (Λ⁻¹).1 ν μ • coord t ν
```

**`QED.Photon.JetAlgebra.lorentzAction_coord_zero`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L380).

> The Lorentz action on an underived photon coordinate `A_μ`.

```lean
lemma lorentzAction_coord_zero (Λ : LorentzGroup 3) (μ : Fin 1 ⊕ Fin 3) :
    lorentzAction Λ (coord 0 μ) = ∑ ν, (Λ⁻¹).1 ν μ • coord 0 ν
```

**`QED.Photon.JetAlgebra.lorentzAction_coord_singleton`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L385).

> The Lorentz action on a once-derived photon coordinate `∂_σ A_μ`.

```lean
lemma lorentzAction_coord_singleton (Λ : LorentzGroup 3) (σ μ : Fin 1 ⊕ Fin 3) :
    lorentzAction Λ (coord {σ} μ) =
      ∑ τ, ∑ ν, ((Λ⁻¹).1 τ σ * (Λ⁻¹).1 ν μ) • coord {τ} ν
```

### B.6. The mass-weight scaling on the photon jet algebra

**`QED.Photon.JetAlgebra.massScale`**, a def, [line 402](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L402).

> The mass-weight scaling on the photon jet algebra, the algebra map
> multiplying each jet coordinate by `c` to the power of its mass weight.

```lean
noncomputable def massScale (c : ℝ) : JetAlgebra →ₐ[ℝ] JetAlgebra
```

**`QED.Photon.JetAlgebra.massScale_coord`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L406).

```lean
lemma massScale_coord (c : ℝ) (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    massScale c (coord s μ) = c ^ (2 + 2 * Multiset.card s) • coord s μ
```

### B.7. The formal total derivative on the photon jet algebra

**`QED.Photon.JetAlgebra.jetDeriv`**, a def, [line 420](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L420).

> The formal total spacetime derivative on the photon jet algebra in the
> direction `ρ`, the derivation appending the derivative index,
> `∂_s A_μ ↦ ∂_{s + {ρ}} A_μ`.

```lean
noncomputable def jetDeriv (ρ : Fin 1 ⊕ Fin 3) : JetAlgebra →ₗ[ℝ] JetAlgebra
```

**`QED.Photon.JetAlgebra.jetDeriv_coord`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L425).

```lean
lemma jetDeriv_coord (ρ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (μ : Fin 1 ⊕ Fin 3) :
    jetDeriv ρ (coord s μ) = coord (s + {ρ}) μ
```

**`QED.Photon.JetAlgebra.jetDeriv_one`**, a lemma, [line 432](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L432).

```lean
lemma jetDeriv_one (ρ : Fin 1 ⊕ Fin 3) : jetDeriv ρ (1 : JetAlgebra) = 0
```

**`QED.Photon.JetAlgebra.jetDeriv_mul`**, a lemma, [line 436](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L436).

> The total derivative is a derivation on the photon jet algebra.

```lean
lemma jetDeriv_mul (ρ : Fin 1 ⊕ Fin 3) (x y : JetAlgebra) :
    jetDeriv ρ (x * y) = jetDeriv ρ x * y + x * jetDeriv ρ y
```

**`QED.Photon.JetAlgebra.jetDeriv_baseChange_mul`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L444).

> The Leibniz rule for the complexified total derivative.

```lean
lemma jetDeriv_baseChange_mul (ρ : Fin 1 ⊕ Fin 3) (x y : ℂ ⊗[ℝ] JetAlgebra) :
    LinearMap.baseChange ℂ (jetDeriv ρ) (x * y) =
      LinearMap.baseChange ℂ (jetDeriv ρ) x * y +
        x * LinearMap.baseChange ℂ (jetDeriv ρ) y
```

## C. The gauge jet of a `U(1)_em` transformation

> A gauge transformation with gauge function `χ` acts on the photon by
> `A_μ ↦ A_μ + ∂_μ χ` and on a field of charge `q` by `ψ ↦ exp (I q e χ) ψ`.
> All that the jet algebras see of `χ` are its derivative jets `c s = ∂_s χ`,
> and all they see of the phase are the derivative jets
> `u s = ∂_s (exp (I e χ))`.  The two families are not independent:
> differentiating the exponential gives `∂_μ u = I e (∂_μ χ) u`, whose `s`-th
> derivative is a Leibniz sum over the splittings of `s`.
> `Multiset.antidiagonal` counts each splitting with its multiplicity, which is
> exactly the multinomial weight of the Leibniz rule.

**`QED.sum_map_antidiagonal_ite`**, a lemma, [line 484](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L484).

> Summing an indicator supported on the splittings `(0, t)` over the
> antidiagonal of `t` picks out `f t`. The splitting `(0, t)` occurs exactly
> once in `Multiset.antidiagonal t`.

```lean
lemma sum_map_antidiagonal_ite {M : Type*} [AddCommMonoid M]
    (t : Multiset (Fin 1 ⊕ Fin 3)) (f : Multiset (Fin 1 ⊕ Fin 3) → M) :
    ((t.antidiagonal).map fun p => if p.1 = 0 then f p.2 else 0).sum = f t
```

**`QED.phaseAct`**, a def, [line 495](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L495).

> The Leibniz convolution of a phase family against a module-valued family
> of jets, over the antidiagonal of the derivative multiset. It is the formal
> expansion `∂_s (u ⬝ f) = ∑_{x + y = s} (∂_x u) (∂_y f)`, with the
> multiplicities of `Multiset.antidiagonal` supplying the multinomial
> weights.

```lean
noncomputable def phaseAct {M : Type*} [AddCommMonoid M] [Module ℂ M]
    (u : Multiset (Fin 1 ⊕ Fin 3) → ℂ) (f : Multiset (Fin 1 ⊕ Fin 3) → M) :
    Multiset (Fin 1 ⊕ Fin 3) → M
```

**`QED.phaseAct_zero_arg`**, a lemma, [line 507](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L507).

```lean
lemma phaseAct_zero_arg : phaseAct u f 0 = u 0 • f 0
```

**`QED.phaseAct_eq_sum`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L512).

> The convolution as a literal antidiagonal sum of products, for
> scalar-valued families.

```lean
lemma phaseAct_eq_sum (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct u v s = (s.antidiagonal.map fun p => u p.1 * v p.2).sum
```

**`QED.phaseAct_add_singleton`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L517).

> The Leibniz rule of the convolution. Differentiating a convolution
> differentiates one factor at a time.

```lean
lemma phaseAct_add_singleton (a : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct u f (s + {a}) =
      phaseAct u (fun t => f (t + {a})) s +
        phaseAct (fun t => u (t + {a})) f s
```

**`QED.phaseAct_add_left`**, a lemma, [line 534](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L534).

> The convolution is additive in the jets acting.

```lean
lemma phaseAct_add_left (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct (fun t => u₁ t + u₂ t) f s = phaseAct u₁ f s + phaseAct u₂ f s
```

**`QED.phaseAct_smul_left`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L540).

> The convolution commutes with scaling the jets acting.

```lean
lemma phaseAct_smul_left (c : ℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct (fun t => c * u t) f s = c • phaseAct u f s
```

**`QED.phaseAct_smul_right`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L548).

> The convolution commutes with scaling the jets acted on.

```lean
lemma phaseAct_smul_right (c : ℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct u (fun t => c • f t) s = c • phaseAct u f s
```

**`QED.phaseAct_assoc`**, a lemma, [line 557](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L557).

> Associativity of the convolution. Acting by `u` after `v` is acting by
> the convolution `u ⋆ v`.

```lean
lemma phaseAct_assoc (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct u (phaseAct v f) s = phaseAct (phaseAct u v) f s
```

**`QED.phaseAct_comm`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L564).

> Commutativity of the scalar convolution.

```lean
lemma phaseAct_comm (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct u v s = phaseAct v u s
```

**`QED.map_phaseAct`**, a lemma, [line 577](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L577).

> A linear map passes through the convolution.

```lean
lemma map_phaseAct {N : Type*} [AddCommMonoid N] [Module ℂ N] (L : M →ₗ[ℂ] N)
    (s : Multiset (Fin 1 ⊕ Fin 3)) :
    L (phaseAct u f s) = phaseAct u (fun t => L (f t)) s
```

**`QED.phaseAct_indicator`**, a lemma, [line 586](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L586).

> The convolution against the indicator of the empty multiset is the
> identity. The splitting `(0, t)` occurs exactly once in the
> antidiagonal.

```lean
lemma phaseAct_indicator (s : Multiset (Fin 1 ⊕ Fin 3)) :
    phaseAct (fun t => if t = 0 then 1 else 0) f s = f s
```

**`QED.star_phaseAct`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L596).

> The star of a convolution is the convolution of the stars.

```lean
lemma star_phaseAct (s : Multiset (Fin 1 ⊕ Fin 3)) :
    star (phaseAct u v s) =
      phaseAct (fun t => star (u t)) (fun t => star (v t)) s
```

**`QED.GaugeJet`**, a structure, [line 612](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L612).

> The jets of a `U(1)_em` gauge transformation with coupling `e`. The
> derivative jets `χjet s = ∂_s χ` of the real gauge function and
> `phase s = ∂_s (exp (I e χ))` of its unitary phase at the base point,
> subject to the two identities every honest gauge function satisfies.
> The phase has unit norm at the base point, and its derivatives obey the
> formal Leibniz expansion of `∂_μ (exp (I e χ)) = I e (∂_μ χ) exp (I e χ)`.

```lean
structure GaugeJet (e : ℝ) where
  /-- The derivative jets `∂_s χ` of the gauge function. -/
  χjet : Multiset (Fin 1 ⊕ Fin 3) → ℝ
  /-- The derivative jets `∂_s (exp (I e χ))` of the unitary phase. -/
  phase : Multiset (Fin 1 ⊕ Fin 3) → ℂ
  /-- The phase is unitary at the base point. -/
  phase_zero_unitary : phase 0 * star (phase 0) = 1
  /-- The formal Leibniz identity `∂_s ∂_μ u = I e ∂_s ((∂_μ χ) u)`. -/
  phase_deriv : ∀ (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3),
    phase (s + {μ}) = Complex.I * e *
      ((s.antidiagonal.map fun p => (χjet (p.1 + {μ}) : ℂ) * phase p.2).sum)
```

### C.1. Low-order consequences of the Leibniz identity

> The QED Lagrangian only involves jet coordinates of derivative order at most
> one, so its gauge invariance only uses the Leibniz identity at order zero,
> together with unitarity at the base point.

**`QED.GaugeJet.phase_singleton`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L640).

> The first derivative of the phase, the `s = 0` case of the Leibniz
> identity, `∂_μ u = I e (∂_μ χ) u` at the base point.

```lean
lemma phase_singleton (μ : Fin 1 ⊕ Fin 3) :
    g.phase {μ} = Complex.I * e * (g.χjet {μ} * g.phase 0)
```

**`QED.GaugeJet.star_phase_singleton`**, a lemma, [line 646](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L646).

> The first derivative of the conjugate phase,
> `∂_μ ū = -I e (∂_μ χ) ū` at the base point.

```lean
lemma star_phase_singleton (μ : Fin 1 ⊕ Fin 3) :
    star (g.phase {μ}) = -(Complex.I * e * (g.χjet {μ} * star (g.phase 0)))
```

**`QED.GaugeJet.trivial`**, a def, [line 653](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L653).

> The trivial gauge jet, the jets of the constant gauge function `χ = 0`.

```lean
noncomputable def trivial (e : ℝ) : GaugeJet e
```

### C.2. The commutative monoid of gauge jets

> Gauge jets compose: the gauge functions add and the phases convolve by the
> Leibniz rule.  Closure of the two axioms under this product is a consistency
> check on the axiomatisation of `GaugeJet`.

**`QED.GaugeJet.ext`**, a lemma, [line 678](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L678).

> Two gauge jets agree when their gauge-function jets and phase jets agree.

```lean
lemma ext {g₁ g₂ : GaugeJet e} (h1 : g₁.χjet = g₂.χjet)
    (h2 : g₁.phase = g₂.phase) : g₁ = g₂
```

**An instance with no name**, [line 686](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L686).

> The composite of two gauge jets. The gauge functions add and the phases
> convolve by the Leibniz rule.

```lean
noncomputable instance : Mul (GaugeJet e)
```

**`QED.GaugeJet.mul_χjet`**, a lemma, [line 729](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L729).

```lean
lemma mul_χjet (g₁ g₂ : GaugeJet e) : (g₁ * g₂).χjet = g₁.χjet + g₂.χjet
```

**`QED.GaugeJet.mul_phase`**, a lemma, [line 732](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L732).

```lean
lemma mul_phase (g₁ g₂ : GaugeJet e) :
    (g₁ * g₂).phase = phaseAct g₁.phase g₂.phase
```

**An instance with no name**, [line 735](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L735).

```lean
noncomputable instance : One (GaugeJet e)
```

**`QED.GaugeJet.one_χjet`**, a lemma, [line 738](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L738).

```lean
lemma one_χjet : (1 : GaugeJet e).χjet = 0
```

**`QED.GaugeJet.one_phase`**, a lemma, [line 741](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L741).

```lean
lemma one_phase :
    (1 : GaugeJet e).phase = fun s => if s = 0 then (1 : ℂ) else 0
```

**An instance with no name**, [line 746](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L746).

> The gauge jets form a commutative monoid. The gauge symmetry data of
> QED composes associatively, with the trivial gauge jet as the unit.

```lean
noncomputable instance : CommMonoid (GaugeJet e)
```

## D. The jet algebra of the electron

### D.1. The jet coordinates

> A jet coordinate is a formal symbol `∂_s ψ_α` or `∂_s ψ̄_α`, where `s` is a
> *multiset* of spacetime directions (partial derivatives of a smooth field
> commute) and `α : Fin 2 ⊕ Fin 2` is a Dirac spinor index in the chiral
> representation: `Sum.inl` indexes the left-handed and `Sum.inr` the
> right-handed Weyl component.

**`QED.Electron.JetGenerators`**, an inductive, [line 783](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L783).

> The jet coordinates of the Dirac electron, the symbols `∂_s ψ_α` and
> `∂_s ψ̄_α`, the `s`-th derivatives of the Dirac components and their
> conjugates.  The electron has electric charge `-1`; its conjugate has
> charge `+1`.

```lean
inductive JetGenerators where
  /-- The jet coordinate `∂_s ψ_α` of the electron. -/
  | dψ (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) : JetGenerators
  /-- The jet coordinate `∂_s ψ̄_α` of the conjugate electron. -/
  | dbarψ (s : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) : JetGenerators
  deriving DecidableEq
```

**`QED.Electron.JetGenerators.massWeight`**, a def, [line 792](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L792).

> The mass weight (twice the mass dimension) of an electron jet coordinate.
> A fermion has mass dimension `3/2` and each derivative adds one.

```lean
def JetGenerators.massWeight : JetGenerators → ℕ
```

**`QED.Electron.FieldDerivSpace`**, an abbrev, [line 798](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L798).

> The field-derivative space of the electron, the free complex module on the
> jet coordinates.

```lean
abbrev FieldDerivSpace : Type
```

**`QED.Electron.JetAlgebra`**, an abbrev, [line 803](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L803).

> The jet algebra of the electron, the exterior algebra on the free module
> over the jet coordinates.  The exterior product implements the fermionic
> anticommutativity of the electron field.

```lean
abbrev JetAlgebra : Type
```

**`QED.Electron.JetAlgebra.ofGenerator`**, a def, [line 809](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L809).

> The jet coordinate `∂_s ψ_α` or `∂_s ψ̄_α` as an element of the jet
> algebra.

```lean
noncomputable def ofGenerator (j : JetGenerators) : JetAlgebra
```

### D.2. The gauge action on the electron jet algebra

> A gauge transformation sends the electron (charge `-1`) to `ū ψ` and its
> conjugate to `u ψ̄`, where `u = exp (I e χ)`.  On jet coordinates this is the
> Leibniz expansion
>
> `∂_s ψ_α ↦ ∑_{x + y = s} (∂_x ū) (∂_y ψ_α)`,
>
> the sum running over `Multiset.antidiagonal s`, whose multiplicities are the
> multinomial coefficients of the Leibniz rule.  The action is linear on the jet
> component space and extends functorially to an algebra map of the exterior
> algebra.

**`QED.Electron.JetAlgebra.gaugeActionGenerator`**, a def, [line 831](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L831).

> The gauge action on a single electron jet coordinate, the Leibniz
> expansion of `∂_s (ū ψ_α)` and `∂_s (u ψ̄_α)` over the splittings of `s`.

```lean
noncomputable def gaugeActionGenerator {e : ℝ} (g : GaugeJet e) :
    JetGenerators → FieldDerivSpace
```

**`QED.Electron.JetAlgebra.gaugeActionCS`**, a def, [line 840](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L840).

> The gauge action on the field-derivative space, the linear extension of the
> Leibniz expansion on the jet coordinates.

```lean
noncomputable def gaugeActionCS {e : ℝ} (g : GaugeJet e) :
    FieldDerivSpace →ₗ[ℂ] FieldDerivSpace
```

**`QED.Electron.JetAlgebra.gaugeActionCS_single`**, a lemma, [line 845](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L845).

```lean
lemma gaugeActionCS_single {e : ℝ} (g : GaugeJet e) (j : JetGenerators) :
    gaugeActionCS g (Finsupp.single j 1) = gaugeActionGenerator g j
```

**`QED.Electron.JetAlgebra.gaugeAction`**, a def, [line 851](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L851).

> The gauge action on the electron jet algebra, the algebra map induced by
> the Leibniz expansion on the jet coordinates.

```lean
noncomputable def gaugeAction {e : ℝ} (g : GaugeJet e) :
    JetAlgebra →ₐ[ℂ] JetAlgebra
```

**`QED.Electron.JetAlgebra.gaugeAction_ofGenerator_dψ`**, a lemma, [line 857](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L857).

> The gauge action on an electron coordinate `∂_t ψ_α`, the Leibniz expansion of
> `∂_t (ū ψ_α)`.

```lean
lemma gaugeAction_ofGenerator_dψ {e : ℝ} (g : GaugeJet e)
    (t : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ofGenerator (.dψ t α)) =
      (t.antidiagonal.map fun p =>
        star (g.phase p.1) • ofGenerator (.dψ p.2 α)).sum
```

**`QED.Electron.JetAlgebra.gaugeAction_ofGenerator_dbarψ`**, a lemma, [line 870](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L870).

> The gauge action on a conjugate electron coordinate `∂_t ψ̄_α`, the Leibniz
> expansion of `∂_t (u ψ̄_α)`.

```lean
lemma gaugeAction_ofGenerator_dbarψ {e : ℝ} (g : GaugeJet e)
    (t : Multiset (Fin 1 ⊕ Fin 3)) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ofGenerator (.dbarψ t α)) =
      (t.antidiagonal.map fun p =>
        g.phase p.1 • ofGenerator (.dbarψ p.2 α)).sum
```

### D.3. The action on the low-order jet coordinates

> The QED Lagrangian involves only the jet coordinates of derivative order at
> most one, for which the antidiagonal sums are short: `antidiagonal 0` is the
> single splitting `(0, 0)`, and `antidiagonal {μ}` the two splittings
> `(0, {μ})` and `({μ}, 0)`.

**`QED.Electron.JetAlgebra.antidiagonal_singleton`**, a lemma, [line 893](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L893).

> The two splittings of a single derivative direction.

```lean
lemma antidiagonal_singleton (μ : Fin 1 ⊕ Fin 3) :
    ({μ} : Multiset (Fin 1 ⊕ Fin 3)).antidiagonal = {(0, {μ}), ({μ}, 0)}
```

**`QED.Electron.JetAlgebra.gaugeAction_ofGenerator_dψ_zero`**, a lemma, [line 901](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L901).

```lean
lemma gaugeAction_ofGenerator_dψ_zero {e : ℝ} (g : GaugeJet e) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ofGenerator (.dψ 0 α)) =
      star (g.phase 0) • ofGenerator (.dψ 0 α)
```

**`QED.Electron.JetAlgebra.gaugeAction_ofGenerator_dbarψ_zero`**, a lemma, [line 908](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L908).

```lean
lemma gaugeAction_ofGenerator_dbarψ_zero {e : ℝ} (g : GaugeJet e) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ofGenerator (.dbarψ 0 α)) =
      g.phase 0 • ofGenerator (.dbarψ 0 α)
```

**`QED.Electron.JetAlgebra.gaugeAction_ofGenerator_dψ_singleton`**, a lemma, [line 915](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L915).

> The gauge action on a once-derived electron coordinate `∂_μ ψ_α`.

```lean
lemma gaugeAction_ofGenerator_dψ_singleton {e : ℝ} (g : GaugeJet e)
    (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ofGenerator (.dψ {μ} α)) =
      star (g.phase 0) • ofGenerator (.dψ {μ} α) +
        star (g.phase {μ}) • ofGenerator (.dψ 0 α)
```

**`QED.Electron.JetAlgebra.gaugeAction_ofGenerator_dbarψ_singleton`**, a lemma, [line 924](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L924).

> The gauge action on a once-derived conjugate electron coordinate `∂_μ ψ̄_α`.

```lean
lemma gaugeAction_ofGenerator_dbarψ_singleton {e : ℝ} (g : GaugeJet e)
    (μ : Fin 1 ⊕ Fin 3) (α : Fin 2 ⊕ Fin 2) :
    gaugeAction g (ofGenerator (.dbarψ {μ} α)) =
      g.phase 0 • ofGenerator (.dbarψ {μ} α) +
        g.phase {μ} • ofGenerator (.dbarψ 0 α)
```

### D.4. The Lorentz action on the electron jet algebra

> Under `M : SL(2,ℂ)` the Dirac spinor transforms in the chiral basis by the
> block-diagonal matrix `S(M) = ((M, 0), (0, (M†)⁻¹))`, its conjugate by the
> entrywise conjugate of `S(M)`, and every derivative index by `Λ(M)⁻¹`, where
> `Λ(M)` is the image of `M` under the covering map
> `Lorentz.SL2C.toLorentzGroup`.

**`QED.Electron.JetAlgebra.spinorRep`**, a def, [line 948](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L948).

> The Dirac spinor representation of `SL(2,ℂ)` in the chiral basis. The two
> Weyl components transform in the two conjugate-dual fundamental
> representations, `S(M) = ((M, 0), (0, (M†)⁻¹))`, the assignment being fixed
> by the conventions of `Lorentz.SL2C.toLorentzGroup`.

```lean
noncomputable def spinorRep (M : SL(2,ℂ)) :
    Matrix (Fin 2 ⊕ Fin 2) (Fin 2 ⊕ Fin 2) ℂ
```

**`QED.Electron.JetAlgebra.lorentzActionGenerator`**, a def, [line 955](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L955).

> The Lorentz action on a single electron jet coordinate. The spinor index
> is rotated by the spinor representation (its conjugate for `∂_s ψ̄`) and the
> derivative indices are transported with `Λ(M)⁻¹`.

```lean
noncomputable def lorentzActionGenerator (M : SL(2,ℂ)) :
    JetGenerators → FieldDerivSpace
```

**`QED.Electron.JetAlgebra.lorentzActionCS`**, a def, [line 963](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L963).

> The Lorentz action on the field-derivative space.

```lean
noncomputable def lorentzActionCS (M : SL(2,ℂ)) :
    FieldDerivSpace →ₗ[ℂ] FieldDerivSpace
```

**`QED.Electron.JetAlgebra.lorentzActionCS_single`**, a lemma, [line 968](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L968).

```lean
lemma lorentzActionCS_single (M : SL(2,ℂ)) (j : JetGenerators) :
    lorentzActionCS M (Finsupp.single j 1) = lorentzActionGenerator M j
```

**`QED.Electron.JetAlgebra.lorentzAction`**, a def, [line 974](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L974).

> The Lorentz action on the electron jet algebra, the algebra map induced by
> the action on the jet coordinates.

```lean
noncomputable def lorentzAction (M : SL(2,ℂ)) : JetAlgebra →ₐ[ℂ] JetAlgebra
```

**`QED.Electron.JetAlgebra.lorentzAction_ofGenerator_dψ_zero`**, a lemma, [line 978](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L978).

```lean
lemma lorentzAction_ofGenerator_dψ_zero (M : SL(2,ℂ)) (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (ofGenerator (.dψ 0 α)) =
      ∑ β, spinorRep M α β • ofGenerator (.dψ 0 β)
```

**`QED.Electron.JetAlgebra.lorentzAction_ofGenerator_dbarψ_zero`**, a lemma, [line 988](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L988).

```lean
lemma lorentzAction_ofGenerator_dbarψ_zero (M : SL(2,ℂ)) (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (ofGenerator (.dbarψ 0 α)) =
      ∑ β, star (spinorRep M α β) • ofGenerator (.dbarψ 0 β)
```

**`QED.Electron.JetAlgebra.lorentzAction_ofGenerator_dψ_singleton`**, a lemma, [line 998](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L998).

> The Lorentz action on a once-derived electron coordinate `∂_σ ψ_α`.

```lean
lemma lorentzAction_ofGenerator_dψ_singleton (M : SL(2,ℂ)) (σ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (ofGenerator (.dψ {σ} α)) =
      ∑ τ, ∑ β, ((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ σ : ℝ) • spinorRep M α β) •
        ofGenerator (.dψ {τ} β)
```

**`QED.Electron.JetAlgebra.lorentzAction_ofGenerator_dbarψ_singleton`**, a lemma, [line 1015](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1015).

> The Lorentz action on a once-derived conjugate electron coordinate `∂_σ ψ̄_α`.

```lean
lemma lorentzAction_ofGenerator_dbarψ_singleton (M : SL(2,ℂ)) (σ : Fin 1 ⊕ Fin 3)
    (α : Fin 2 ⊕ Fin 2) :
    lorentzAction M (ofGenerator (.dbarψ {σ} α)) =
      ∑ τ, ∑ β, ((((Lorentz.SL2C.toLorentzGroup M)⁻¹).1 τ σ : ℝ) •
          star (spinorRep M α β)) • ofGenerator (.dbarψ {τ} β)
```

### D.5. The mass-weight scaling on the electron jet algebra

**`QED.Electron.JetAlgebra.massScaleCS`**, a def, [line 1040](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1040).

> The mass-weight scaling on the field-derivative space, the diagonal map
> multiplying each jet coordinate by `c` to the power of its mass weight.

```lean
noncomputable def massScaleCS (c : ℝ) : FieldDerivSpace →ₗ[ℂ] FieldDerivSpace
```

**`QED.Electron.JetAlgebra.massScale`**, a def, [line 1045](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1045).

> The mass-weight scaling on the electron jet algebra.

```lean
noncomputable def massScale (c : ℝ) : JetAlgebra →ₐ[ℂ] JetAlgebra
```

**`QED.Electron.JetAlgebra.massScale_ofGenerator`**, a lemma, [line 1049](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1049).

```lean
lemma massScale_ofGenerator (c : ℝ) (j : JetGenerators) :
    massScale c (ofGenerator j) = (c : ℂ) ^ j.massWeight • ofGenerator j
```

### D.6. The formal total derivative on the electron jet algebra

> The total derivative extends from the jet coordinates to the whole exterior
> algebra as an *even* derivation, `∂_ρ (x y) = (∂_ρ x) y + x (∂_ρ y)` with no
> Koszul signs.  It is constructed by lifting `ι x ↦ (ι x, ι (∂_ρ x))` to an
> algebra homomorphism into the trivial square-zero extension of the jet
> algebra, following
> `Physlib.Particles.StandardModel.Fermions.LeptonSinglet.JetAlgebra.JetDeriv`.

**`QED.Electron.JetGenerators.shift`**, a def, [line 1070](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1070).

> The jet coordinate with one further derivative in the direction `ρ`.

```lean
def JetGenerators.shift (ρ : Fin 1 ⊕ Fin 3) : JetGenerators → JetGenerators
```

**`QED.Electron.JetAlgebra.jetDerivCS`**, a def, [line 1078](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1078).

> The total derivative on the field-derivative space, the shift of the
> derivative multi-index.

```lean
noncomputable def jetDerivCS (ρ : Fin 1 ⊕ Fin 3) :
    FieldDerivSpace →ₗ[ℂ] FieldDerivSpace
```

**`QED.Electron.JetAlgebra.jetDerivCS_single`**, a lemma, [line 1084](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1084).

```lean
lemma jetDerivCS_single (ρ : Fin 1 ⊕ Fin 3) (j : JetGenerators) :
    jetDerivCS ρ (Finsupp.single j 1) =
      Finsupp.single (JetGenerators.shift ρ j) 1
```

**`QED.Electron.JetAlgebra.jetDerivGen`**, a def, [line 1091](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1091).

> The generator map of the total derivative into the trivial square-zero
> extension of the jet algebra, `ι x ↦ (ι x, ι (∂_ρ x))`.

```lean
noncomputable def jetDerivGen (ρ : Fin 1 ⊕ Fin 3) :
    FieldDerivSpace →ₗ[ℂ] TrivSqZeroExt JetAlgebra JetAlgebra
```

**`QED.Electron.JetAlgebra.jetDerivGen_fst`**, a lemma, [line 1102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1102).

```lean
lemma jetDerivGen_fst (ρ : Fin 1 ⊕ Fin 3) (x : FieldDerivSpace) :
    (jetDerivGen ρ x).fst = ExteriorAlgebra.ι ℂ x
```

**`QED.Electron.JetAlgebra.jetDerivGen_snd`**, a lemma, [line 1106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1106).

```lean
lemma jetDerivGen_snd (ρ : Fin 1 ⊕ Fin 3) (x : FieldDerivSpace) :
    (jetDerivGen ρ x).snd = ExteriorAlgebra.ι ℂ (jetDerivCS ρ x)
```

**`QED.Electron.JetAlgebra.jetDerivGen_mul_self`**, a lemma, [line 1111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1111).

> The generator map squares to zero, as degree-one elements of the exterior
> algebra anticommute.

```lean
lemma jetDerivGen_mul_self (ρ : Fin 1 ⊕ Fin 3) (x : FieldDerivSpace) :
    jetDerivGen ρ x * jetDerivGen ρ x = 0
```

**`QED.Electron.JetAlgebra.jetDerivHom`**, a def, [line 1122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1122).

> The lift of the total derivative to the trivial square-zero extension of
> the jet algebra, the algebra homomorphism `x ↦ (x, ∂_ρ x)`.

```lean
noncomputable def jetDerivHom (ρ : Fin 1 ⊕ Fin 3) :
    JetAlgebra →ₐ[ℂ] TrivSqZeroExt JetAlgebra JetAlgebra
```

**`QED.Electron.JetAlgebra.jetDerivHom_ι`**, a lemma, [line 1127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1127).

```lean
lemma jetDerivHom_ι (ρ : Fin 1 ⊕ Fin 3) (x : FieldDerivSpace) :
    jetDerivHom ρ (ExteriorAlgebra.ι ℂ x) = jetDerivGen ρ x
```

**`QED.Electron.JetAlgebra.jetDerivHom_fst`**, a lemma, [line 1133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1133).

> The first component of the square-zero lift is the identity.

```lean
lemma jetDerivHom_fst (ρ : Fin 1 ⊕ Fin 3) (x : JetAlgebra) :
    (jetDerivHom ρ x).fst = x
```

**`QED.Electron.JetAlgebra.jetDeriv`**, a def, [line 1144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1144).

> The formal total spacetime derivative on the electron jet algebra in the
> direction `ρ`, the even derivation extending the shift
> `∂_s ψ_α ↦ ∂_{s + {ρ}} ψ_α` of the jet coordinates.

```lean
noncomputable def jetDeriv (ρ : Fin 1 ⊕ Fin 3) : JetAlgebra →ₗ[ℂ] JetAlgebra
```

**`QED.Electron.JetAlgebra.jetDeriv_apply`**, a lemma, [line 1150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1150).

> The total derivative is the second component of its square-zero lift.

```lean
lemma jetDeriv_apply (ρ : Fin 1 ⊕ Fin 3) (x : JetAlgebra) :
    jetDeriv ρ x = (jetDerivHom ρ x).snd
```

**`QED.Electron.JetAlgebra.jetDeriv_ι`**, a lemma, [line 1154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1154).

```lean
lemma jetDeriv_ι (ρ : Fin 1 ⊕ Fin 3) (x : FieldDerivSpace) :
    jetDeriv ρ (ExteriorAlgebra.ι ℂ x) =
      ExteriorAlgebra.ι ℂ (jetDerivCS ρ x)
```

**`QED.Electron.JetAlgebra.jetDeriv_ofGenerator`**, a lemma, [line 1162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1162).

> The total derivative appends the derivative index to each jet
> coordinate.

```lean
lemma jetDeriv_ofGenerator (ρ : Fin 1 ⊕ Fin 3) (j : JetGenerators) :
    jetDeriv ρ (ofGenerator j) = ofGenerator (JetGenerators.shift ρ j)
```

**`QED.Electron.JetAlgebra.jetDeriv_one`**, a lemma, [line 1168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1168).

```lean
lemma jetDeriv_one (ρ : Fin 1 ⊕ Fin 3) : jetDeriv ρ (1 : JetAlgebra) = 0
```

**`QED.Electron.JetAlgebra.jetDeriv_mul`**, a lemma, [line 1173](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1173).

> The total derivative is an even derivation. The Leibniz rule holds on the
> electron jet algebra with no Koszul signs.

```lean
lemma jetDeriv_mul (ρ : Fin 1 ⊕ Fin 3) (x y : JetAlgebra) :
    jetDeriv ρ (x * y) = jetDeriv ρ x * y + x * jetDeriv ρ y
```

## E. The jet algebra of QED

**`QED.JetAlgebra`**, a def, [line 1203](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1203).

> The jet algebra of quantum electrodynamics, the tensor product of the
> complexified photon jet algebra with the electron jet algebra.
>
> This is a `def` rather than an `abbrev`, and its algebraic structure is fixed
> by the single `Ring` and `Algebra` instances below, so that every algebraic
> class projects from one root.  On the bare tensor product `One`, `Mul`,
> `Zero`, `Add`, `SMul` and `Module` are instead supplied by standalone
> `TensorProduct.*` instances rather than as projections of the semiring; those
> are definitionally the projections, but not syntactically, so a generic lemma
> whose type argument is not pinned by an explicit argument (such as `one_pow`)
> cannot be unified against a goal.  Rooting the structure here keeps the
> generic algebraic lemmas usable.

```lean
def JetAlgebra : Type
```

**An instance with no name**, [line 1205](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1205).

```lean
noncomputable instance : Ring JetAlgebra
```

**An instance with no name**, [line 1208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1208).

```lean
noncomputable instance : Algebra ℂ JetAlgebra
```

### E.1. Pure tensors and their arithmetic

**`QED.JetAlgebra.tmul`**, a def, [line 1226](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1226).

> A pure tensor, as an element of the jet algebra.
>
> Writing `a ⊗ₜ[ℂ] b` builds an element of the *underlying* tensor product,
> which is only definitionally an element of `JetAlgebra`.  A goal mixing such
> a term with the jet algebra's own operations is then not type-correct at
> `instances` transparency, and no rewrite can fire on it.  This constructor
> keeps pure tensors typed at `JetAlgebra`.

```lean
noncomputable def tmul (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra) :
    JetAlgebra
```

**`QED.JetAlgebra.one_eq_tmul`**, a lemma, [line 1232](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1232).

> The unit of the QED jet algebra is the pure tensor of the units.

```lean
lemma one_eq_tmul : (1 : JetAlgebra) = (1 : ℂ ⊗[ℝ] Photon.JetAlgebra) ⊗ⱼ 1
```

**`QED.JetAlgebra.tmul_mul_tmul`**, a lemma, [line 1237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1237).

> Multiplication of pure tensors. `Algebra.TensorProduct.tmul_mul_tmul` does
> not rewrite here, even though it is definitionally the same statement.

```lean
lemma tmul_mul_tmul (a₁ a₂ : ℂ ⊗[ℝ] Photon.JetAlgebra)
    (b₁ b₂ : Electron.JetAlgebra) :
    (a₁ ⊗ⱼ b₁) * (a₂ ⊗ⱼ b₂) = (a₁ * a₂) ⊗ⱼ (b₁ * b₂)
```

**`QED.JetAlgebra.zero_tmul`**, a lemma, [line 1243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1243).

```lean
lemma zero_tmul (b : Electron.JetAlgebra) :
    (0 : ℂ ⊗[ℝ] Photon.JetAlgebra) ⊗ⱼ b = 0
```

**`QED.JetAlgebra.tmul_zero`**, a lemma, [line 1247](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1247).

```lean
lemma tmul_zero (a : ℂ ⊗[ℝ] Photon.JetAlgebra) :
    a ⊗ⱼ (0 : Electron.JetAlgebra) = 0
```

**`QED.JetAlgebra.add_tmul`**, a lemma, [line 1251](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1251).

```lean
lemma add_tmul (a₁ a₂ : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra) :
    (a₁ + a₂) ⊗ⱼ b = a₁ ⊗ⱼ b + a₂ ⊗ⱼ b
```

**`QED.JetAlgebra.tmul_add`**, a lemma, [line 1255](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1255).

```lean
lemma tmul_add (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b₁ b₂ : Electron.JetAlgebra) :
    a ⊗ⱼ (b₁ + b₂) = a ⊗ⱼ b₁ + a ⊗ⱼ b₂
```

**`QED.JetAlgebra.sub_tmul`**, a lemma, [line 1259](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1259).

```lean
lemma sub_tmul (a₁ a₂ : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra) :
    (a₁ - a₂) ⊗ⱼ b = a₁ ⊗ⱼ b - a₂ ⊗ⱼ b
```

**`QED.JetAlgebra.tmul_sub`**, a lemma, [line 1263](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1263).

```lean
lemma tmul_sub (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b₁ b₂ : Electron.JetAlgebra) :
    a ⊗ⱼ (b₁ - b₂) = a ⊗ⱼ b₁ - a ⊗ⱼ b₂
```

**`QED.JetAlgebra.neg_tmul`**, a lemma, [line 1267](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1267).

```lean
lemma neg_tmul (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra) :
    (-a) ⊗ⱼ b = -(a ⊗ⱼ b)
```

**`QED.JetAlgebra.tmul_neg`**, a lemma, [line 1271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1271).

```lean
lemma tmul_neg (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra) :
    a ⊗ⱼ (-b) = -(a ⊗ⱼ b)
```

**`QED.JetAlgebra.tmul_sum`**, a lemma, [line 1275](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1275).

> Pure tensors are additive in the electron factor.

```lean
lemma tmul_sum {ι : Type*} (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (s : Finset ι)
    (f : ι → Electron.JetAlgebra) : a ⊗ⱼ (∑ i ∈ s, f i) = ∑ i ∈ s, a ⊗ⱼ f i
```

**`QED.JetAlgebra.sum_tmul`**, a lemma, [line 1280](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1280).

> Pure tensors are additive in the photon factor.

```lean
lemma sum_tmul {ι : Type*} (s : Finset ι) (f : ι → ℂ ⊗[ℝ] Photon.JetAlgebra)
    (b : Electron.JetAlgebra) : (∑ i ∈ s, f i) ⊗ⱼ b = ∑ i ∈ s, f i ⊗ⱼ b
```

**`QED.JetAlgebra.tmul_smul`**, a lemma, [line 1285](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1285).

```lean
lemma tmul_smul (r : ℂ) (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra) :
    a ⊗ⱼ (r • b) = r • (a ⊗ⱼ b)
```

**`QED.JetAlgebra.smul_tmul'`**, a lemma, [line 1289](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1289).

```lean
lemma smul_tmul' (r : ℂ) (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra) :
    (r • a) ⊗ⱼ b = r • (a ⊗ⱼ b)
```

**`QED.JetAlgebra.real_smul_tmul`**, a lemma, [line 1293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1293).

> An `ℝ`-scalar on the photon factor is a `ℂ`-scalar of the jet algebra.

```lean
lemma real_smul_tmul (r : ℝ) (a : ℂ ⊗[ℝ] Photon.JetAlgebra)
    (b : Electron.JetAlgebra) :
    (r • a) ⊗ⱼ b = (r : ℂ) • (a ⊗ⱼ b)
```

**`QED.JetAlgebra.tmul_C_eq_smul_one`**, a lemma, [line 1300](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1300).

> A constant of the photon factor is a scalar of the jet algebra.

```lean
lemma tmul_C_eq_smul_one (r : ℝ) :
    ((1 : ℂ) ⊗ₜ[ℝ] (MvPolynomial.C r : Photon.JetAlgebra)) ⊗ⱼ
        (1 : Electron.JetAlgebra) = (r : ℂ) • (1 : JetAlgebra)
```

**`QED.JetAlgebra.induction_on`**, a lemma, [line 1317](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1317).

> Induction on the jet algebra, stated for `JetAlgebra` itself.  Using
> `TensorProduct.inductionOn` directly leaves the sum and the pure tensors in
> the goals carrying the tensor product's structure rather than the jet
> algebra's, which makes those goals unrewritable.

```lean
lemma induction_on {motive : JetAlgebra → Prop} (x : JetAlgebra)
    (tmul : ∀ (a : ℂ ⊗[ℝ] Photon.JetAlgebra) (b : Electron.JetAlgebra),
      motive (a ⊗ⱼ b))
    (add : ∀ x y : JetAlgebra, motive x → motive y → motive (x + y)) : motive x
```

### E.2. The inclusions of the two factors

**`QED.JetAlgebra.inclA`**, an abbrev, [line 1330](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1330).

> The photon factor included into the QED jet algebra.

```lean
noncomputable abbrev inclA : (ℂ ⊗[ℝ] Photon.JetAlgebra) →ₐ[ℂ] JetAlgebra
```

**`QED.JetAlgebra.inclE`**, an abbrev, [line 1334](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1334).

> The electron factor included into the QED jet algebra.

```lean
noncomputable abbrev inclE : Electron.JetAlgebra →ₐ[ℂ] JetAlgebra
```

### E.3. The gauge action on the QED jet algebra

> A gauge jet acts on the photon factor by the affine shift
> `∂_s A_μ ↦ ∂_s A_μ + ∂_s ∂_μ χ`, complexified, and on the electron factor by
> the Leibniz expansion of `∂_s (ū ψ)` and `∂_s (u ψ̄)`; the action on the full
> jet algebra is the tensor product of the two, an algebra map.

**`QED.JetAlgebra.gaugeActionPhoton`**, a def, [line 1350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1350).

> The gauge action on the complexified photon jet algebra, the
> complexification of the affine action `∂_s A_μ ↦ ∂_s A_μ + ∂_s ∂_μ χ`.

```lean
noncomputable def gaugeActionPhoton (c : Photon.JetAlgebra.GaugeJet) :
    (ℂ ⊗[ℝ] Photon.JetAlgebra) →ₐ[ℂ] ℂ ⊗[ℝ] Photon.JetAlgebra
```

**`QED.JetAlgebra.gaugeActionPhoton_tmul`**, a lemma, [line 1355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1355).

```lean
lemma gaugeActionPhoton_tmul (c : Photon.JetAlgebra.GaugeJet) (x : ℂ)
    (p : Photon.JetAlgebra) :
    gaugeActionPhoton c (x ⊗ₜ[ℝ] p) = x ⊗ₜ[ℝ] Photon.JetAlgebra.gaugeAction c p
```

**`QED.JetAlgebra.gaugeAction`**, a def, [line 1363](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1363).

> The gauge action on the QED jet algebra, the tensor product of the affine
> action on the photon factor with the Leibniz phase rotation on the electron
> factor.

```lean
noncomputable def gaugeAction {e : ℝ} (g : GaugeJet e) :
    JetAlgebra →ₐ[ℂ] JetAlgebra
```

**`QED.JetAlgebra.gaugeAction_tmul`**, a lemma, [line 1369](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1369).

> The gauge action on a pure tensor acts on each factor.

```lean
lemma gaugeAction_tmul {e : ℝ} (g : GaugeJet e) (a : ℂ ⊗[ℝ] Photon.JetAlgebra)
    (b : Electron.JetAlgebra) :
    gaugeAction g (a ⊗ⱼ b) =
      gaugeActionPhoton g.χjet a ⊗ⱼ Electron.JetAlgebra.gaugeAction g b
```

### E.4. The Lorentz action on the QED jet algebra

> An `M : SL(2,ℂ)` acts on the photon factor through its image `Λ(M)` in the
> Lorentz group, complexified, and on the electron factor through the spinor
> representation; the action on the full jet algebra is the tensor product of
> the two.

**`QED.JetAlgebra.lorentzActionPhoton`**, a def, [line 1387](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1387).

> The Lorentz action on the complexified photon jet algebra.

```lean
noncomputable def lorentzActionPhoton (Λ : LorentzGroup 3) :
    (ℂ ⊗[ℝ] Photon.JetAlgebra) →ₐ[ℂ] ℂ ⊗[ℝ] Photon.JetAlgebra
```

**`QED.JetAlgebra.lorentzActionPhoton_tmul`**, a lemma, [line 1392](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1392).

```lean
lemma lorentzActionPhoton_tmul (Λ : LorentzGroup 3) (x : ℂ) (p : Photon.JetAlgebra) :
    lorentzActionPhoton Λ (x ⊗ₜ[ℝ] p) = x ⊗ₜ[ℝ] Photon.JetAlgebra.lorentzAction Λ p
```

**`QED.JetAlgebra.lorentzAction`**, a def, [line 1398](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1398).

> The Lorentz action on the QED jet algebra, the tensor product of the
> photon action through the covering map with the electron spinor action.

```lean
noncomputable def lorentzAction (M : SL(2,ℂ)) : JetAlgebra →ₐ[ℂ] JetAlgebra
```

**`QED.JetAlgebra.lorentzAction_tmul`**, a lemma, [line 1403](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1403).

> The Lorentz action on a pure tensor acts on each factor.

```lean
lemma lorentzAction_tmul (M : SL(2,ℂ)) (a : ℂ ⊗[ℝ] Photon.JetAlgebra)
    (b : Electron.JetAlgebra) :
    lorentzAction M (a ⊗ⱼ b) =
      lorentzActionPhoton (Lorentz.SL2C.toLorentzGroup M) a ⊗ⱼ
        Electron.JetAlgebra.lorentzAction M b
```

> …

### E.5. The mass-weight scaling on the QED jet algebra

**`QED.JetAlgebra.massScalePhoton`**, a def, [line 1423](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1423).

> The mass-weight scaling on the complexified photon jet algebra.

```lean
noncomputable def massScalePhoton (c : ℝ) :
    (ℂ ⊗[ℝ] Photon.JetAlgebra) →ₐ[ℂ] ℂ ⊗[ℝ] Photon.JetAlgebra
```

**`QED.JetAlgebra.massScalePhoton_tmul`**, a lemma, [line 1428](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1428).

```lean
lemma massScalePhoton_tmul (c : ℝ) (x : ℂ) (p : Photon.JetAlgebra) :
    massScalePhoton c (x ⊗ₜ[ℝ] p) = x ⊗ₜ[ℝ] Photon.JetAlgebra.massScale c p
```

**`QED.JetAlgebra.massScale`**, a def, [line 1435](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1435).

> The mass-weight scaling on the QED jet algebra, the algebra map
> multiplying each jet coordinate by `c` to the power of its mass weight,
> i.e. `c` squared to the power of its mass dimension.

```lean
noncomputable def massScale (c : ℝ) : JetAlgebra →ₐ[ℂ] JetAlgebra
```

**`QED.JetAlgebra.massScale_tmul`**, a lemma, [line 1439](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1439).

> The mass-weight scaling on a pure tensor scales each factor.

```lean
lemma massScale_tmul (c : ℝ) (a : ℂ ⊗[ℝ] Photon.JetAlgebra)
    (b : Electron.JetAlgebra) :
    massScale c (a ⊗ⱼ b) =
      massScalePhoton c a ⊗ⱼ Electron.JetAlgebra.massScale c b
```

### E.6. The formal total derivative on the QED jet algebra

**`QED.JetAlgebra.jetDeriv`**, a def, [line 1454](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1454).

> The formal total spacetime derivative on the QED jet algebra in the
> direction `ρ`, the Leibniz extension of the total derivatives of the photon
> and electron factors.

```lean
noncomputable def jetDeriv (ρ : Fin 1 ⊕ Fin 3) : JetAlgebra →ₗ[ℂ] JetAlgebra
```

**`QED.JetAlgebra.jetDeriv_tmul`**, a lemma, [line 1460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1460).

> The total derivative of a pure tensor obeys the Leibniz rule.

```lean
lemma jetDeriv_tmul (ρ : Fin 1 ⊕ Fin 3) (a : ℂ ⊗[ℝ] Photon.JetAlgebra)
    (b : Electron.JetAlgebra) :
    jetDeriv ρ (a ⊗ⱼ b) =
      (LinearMap.baseChange ℂ (Photon.JetAlgebra.jetDeriv ρ) a) ⊗ⱼ b +
        a ⊗ⱼ Electron.JetAlgebra.jetDeriv ρ b
```

**`QED.JetAlgebra.jetDeriv_one`**, a lemma, [line 1467](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1467).

```lean
lemma jetDeriv_one (ρ : Fin 1 ⊕ Fin 3) : jetDeriv ρ (1 : JetAlgebra) = 0
```

**`QED.JetAlgebra.jetDeriv_mul`**, a lemma, [line 1479](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean#L1479).

> The total derivative is an even derivation on the QED jet algebra. The
> Leibniz rule holds with no Koszul signs.

```lean
lemma jetDeriv_mul (ρ : Fin 1 ⊕ Fin 3) (x y : JetAlgebra) :
    jetDeriv ρ (x * y) = jetDeriv ρ x * y + x * jetDeriv ρ y
```

## Depends on

- [The Electromagnetic Potential (EMPotential)](../../../physlib/electromagnetism/kinematics/empotential.md)
- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../../physlib/relativity/sl2c/basic.md)

## Proof depends on

- [Sums over the antidiagonal of a multiset](../../mathematics/part-01/multisetantidiagonal.md)

## Sources

- [PhyslibAlpha/Particles/QED/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/QED/Basic.lean)
