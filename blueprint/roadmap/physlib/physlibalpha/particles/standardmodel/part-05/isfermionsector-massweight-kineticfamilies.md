---
declaration: module
origin: cited
lean: StandardModel.IsFermionSector.sum_deriv_one, StandardModel.IsFermionSector.repLorentz_symbol_deriv_one, StandardModel.IsFermionSector.repLorentz_component_deriv_one, StandardModel.IsFermionSector.isVectorDualLeftWeyl_leftComp, StandardModel.IsFermionSector.isVectorDualRightWeyl_rightComp, StandardModel.IsFermionSector.repGauge_su3_d, StandardModel.IsFermionSector.repGauge_su2_d, StandardModel.IsFermionSector.repGauge_u1_d
statement: formalized
proof: formalized
---

# The kinetic terms of the fermion sector

The module `PhyslibAlpha.Particles.StandardModel.IsFermionSector.MassWeight.KineticFamilies`, [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean): 54 declarations, 54 with a docstring.

## i. Overview

> The invariants of the fermion sector at mass weight eight are the kinetic terms, and this
> file builds them. A kinetic term pairs a species with its own conjugate, one of the two
> carrying a covariant derivative, and joins their indices in the only ways available: the
> colour indices by the Kronecker delta, the isospin indices by the Kronecker delta, and the
> four-vector index against the two opposite-chirality spinor indices by the conjugate Pauli
> matrices. That last contraction is `ψ̄ σ̄^μ ∂_μ ψ`.
>
> Ten blocks arise, the five conjugate pairs each with the derivative on one factor or the
> other, and they differ only in which indices their symbols carry. So the work is done once,
> generically, in terms of `InvariantReductionToSpan`: a `KineticBlock` packages a
> block together with its three classification steps — colour, isospin, Lorentz — and from
> that package alone come the contraction, its invariance under both groups, and the reduction
> of the block down to the line through it. The ten blocks are then ten instantiations.
>
> The three stages are the same three the Yukawa sector runs, in the same order, and for the
> same reason: each contraction is a spectator of the ones after it. Where a block's symbols
> carry no colour index — the two lepton-doublet blocks and the two lepton-singlet ones — the
> colour stage is `InvariantReductionToSpan.ofFixedFamily` rather than a classification, and
> likewise for isospin where the symbols carry none. That keeps all ten blocks in one shape.
>
> The ten blocks themselves are built in `KineticTerms`, which instantiates the package.

## ii. Key results

> - `KineticBlock` : one kinetic block of the fermion sector, together with the three classifications
>   its indices admit

## iv. References

> * None.

## A. The once-derived chiral component families

> A tower with one covariant derivative mixes into every assignment of one derivative
> direction, so its Lorentz law is a sum over such assignments, with one column of the
> Lorentz matrix per slot. The value index is untouched by that sum: it still moves by the
> contragredient action, exactly as at zero derivatives. Composing the two gives the laws
> `IsVectorDualLeftWeyl` and `IsVectorDualRightWeyl` of `MassDimLTEight`, the derivative
> slot fundamental and the spinor slot dual.

**`StandardModel.IsFermionSector.sum_deriv_one`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L113).

> A sum over the assignments of one derivative direction is a single sum.

```lean
lemma sum_deriv_one {M : Type*} [AddCommMonoid M] (f : (Fin 1 → Fin 1 ⊕ Fin 3) → M) :
    ∑ p : Fin 1 → Fin 1 ⊕ Fin 3, f p = ∑ x : Fin 1 ⊕ Fin 3, f ![x]
```

**`StandardModel.IsFermionSector.repLorentz_symbol_deriv_one`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L124).

> The Lorentz transformation of a symbol with one covariant derivative: the derivative
> slot moves by the columns of the Lorentz matrix and the value index by the
> contragredient action.

```lean
lemma repLorentz_symbol_deriv_one {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ SL(2,ℂ) V}
    {X : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hX : IsLorentzCovDerivTransforms repLorentz rep X) (Λ : SL(2,ℂ))
    (μ : Fin 1 ⊕ Fin 3) (φ : Module.Dual ℂ V) :
    repLorentz Λ (X ![μ] φ)
      = ∑ ν, (((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) • X ![ν] (rep.dual Λ φ)
```

**`StandardModel.IsFermionSector.repLorentz_component_deriv_one`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L139).

> The Lorentz transformation of a component of a once-derived symbol, when the
> coordinate functionals `c` are permuted by the contragredient action with coefficients
> `m`. This is the once-derived form of the laws of `Components`.

```lean
lemma repLorentz_component_deriv_one {V : Type} [AddCommGroup V] [Module ℂ V]
    {rep : Representation ℂ SL(2,ℂ) V}
    {X : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] B}
    (hX : IsLorentzCovDerivTransforms repLorentz rep X)
    {c : Fin 2 → Module.Dual ℂ V} {m : SL(2,ℂ) → Fin 2 → Fin 2 → ℂ}
    (hc : ∀ (Λ : SL(2,ℂ)) (a : Fin 2), rep.dual Λ (c a) = ∑ β, m Λ a β • c β)
    (Λ : SL(2,ℂ)) (μ : Fin 1 ⊕ Fin 3) (a : Fin 2) :
    repLorentz Λ (X ![μ] (c a))
      = ∑ ν, ∑ β, ((((SL2C.toLorentzGroup Λ).1 ν μ : ℝ) : ℂ) * m Λ a β) • X ![ν] (c β)
```

**`StandardModel.IsFermionSector.isVectorDualLeftWeyl_leftComp`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L155).

> Every undotted component family carries a four-vector index and a dual undotted
> spinor index, at one covariant derivative.

```lean
lemma isVectorDualLeftWeyl_leftComp (i : LeftIdx) :
    IsVectorDualLeftWeyl repLorentz (fun μ => h.leftComp ![μ] i)
```

**`StandardModel.IsFermionSector.isVectorDualRightWeyl_rightComp`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L176).

> Every dotted component family carries a four-vector index and a dual dotted spinor
> index, at one covariant derivative.

```lean
lemma isVectorDualRightWeyl_rightComp (i : RightIdx) :
    IsVectorDualRightWeyl repLorentz (fun μ => h.rightComp ![μ] i)
```

## B. The gauge laws of the components at each factor

> A gauge transformation is a triple, and each of the three index laws that classify a block
> constrains one factor of it. So each of the ten symbols is read at each factor in turn:
> colour moves only a colour index, isospin only an isospin index, and hypercharge is an
> overall scalar whose power is the `6Y` of the species. A symbol eats a covector, so it
> carries the contragredient of its value space: the unbarred species come out
> anti-fundamental in colour and isospin and the barred ones fundamental, which is what makes
> every conjugate pair a fundamental against an anti-fundamental.
>
> - B.1. The down singlet
> - B.2. The conjugate down singlet
> - B.3. The up singlet
> - B.4. The conjugate up singlet
> - B.5. The quark doublet
> - B.6. The conjugate quark doublet
> - B.7. The lepton doublet
> - B.8. The conjugate lepton doublet
> - B.9. The lepton singlet
> - B.10. The conjugate lepton singlet

### B.1. The down singlet

**`StandardModel.IsFermionSector.repGauge_su3_d`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L228).

> A colour transformation moves the colour index of a down-singlet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_d (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.dComponent f l (s, c))
      = ∑ a, conj (U.1 a c) • h.dComponent f l (s, a)
```

**`StandardModel.IsFermionSector.repGauge_su2_d`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L238).

> An isospin transformation fixes a down-singlet symbol, which carries no isospin.

```lean
lemma repGauge_su2_d (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.dComponent f l j)
      = h.dComponent f l j
```

**`StandardModel.IsFermionSector.repGauge_u1_d`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L247).

> A hypercharge transformation scales a down-singlet symbol by the square of the scalar,
> the down singlet carrying `6Y = 2`.

```lean
lemma repGauge_u1_d (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.dComponent f l j)
      = (t : ℂ) ^ 2 • h.dComponent f l j
```

### B.2. The conjugate down singlet

**`StandardModel.IsFermionSector.repGauge_su3_bard`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L262).

> A colour transformation moves the colour index of a conjugate down-singlet symbol by
> the matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_bard (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.bardComponent f l (s, c))
      = ∑ a, U.1 a c • h.bardComponent f l (s, a)
```

**`StandardModel.IsFermionSector.repGauge_su2_bard`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L272).

> An isospin transformation fixes a conjugate down-singlet symbol.

```lean
lemma repGauge_su2_bard (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.bardComponent f l j)
      = h.bardComponent f l j
```

**`StandardModel.IsFermionSector.repGauge_u1_bard`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L281).

> A hypercharge transformation scales a conjugate down-singlet symbol by the square of
> the conjugate scalar, the conjugate down singlet carrying `6Y = -2`.

```lean
lemma repGauge_u1_bard (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.bardComponent f l j)
      = (star (t : ℂ)) ^ 2 • h.bardComponent f l j
```

### B.3. The up singlet

**`StandardModel.IsFermionSector.repGauge_su3_u`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L296).

> A colour transformation moves the colour index of an up-singlet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_u (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.uComponent f l (s, c))
      = ∑ a, conj (U.1 a c) • h.uComponent f l (s, a)
```

**`StandardModel.IsFermionSector.repGauge_su2_u`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L306).

> An isospin transformation fixes an up-singlet symbol.

```lean
lemma repGauge_su2_u (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.uComponent f l j)
      = h.uComponent f l j
```

**`StandardModel.IsFermionSector.repGauge_u1_u`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L315).

> A hypercharge transformation scales an up-singlet symbol by the fourth power of the
> conjugate scalar, the up singlet carrying `6Y = -4`.

```lean
lemma repGauge_u1_u (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.uComponent f l j)
      = (star (t : ℂ)) ^ 4 • h.uComponent f l j
```

### B.4. The conjugate up singlet

**`StandardModel.IsFermionSector.repGauge_su3_baru`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L330).

> A colour transformation moves the colour index of a conjugate up-singlet symbol by the
> matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_baru (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.baruComponent f l (s, c))
      = ∑ a, U.1 a c • h.baruComponent f l (s, a)
```

**`StandardModel.IsFermionSector.repGauge_su2_baru`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L340).

> An isospin transformation fixes a conjugate up-singlet symbol.

```lean
lemma repGauge_su2_baru (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 3) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.baruComponent f l j)
      = h.baruComponent f l j
```

**`StandardModel.IsFermionSector.repGauge_u1_baru`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L349).

> A hypercharge transformation scales a conjugate up-singlet symbol by the fourth power
> of the scalar, the conjugate up singlet carrying `6Y = 4`.

```lean
lemma repGauge_u1_baru (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 3) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.baruComponent f l j)
      = (t : ℂ) ^ 4 • h.baruComponent f l j
```

### B.5. The quark doublet

**`StandardModel.IsFermionSector.repGauge_su3_Q`**, a lemma, [line 364](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L364).

> A colour transformation moves the colour index of a quark-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su3_Q (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.QComponent f l (s, c, w))
      = ∑ a, conj (U.1 a c) • h.QComponent f l (s, a, w)
```

**`StandardModel.IsFermionSector.repGauge_su2_Q`**, a lemma, [line 375](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L375).

> An isospin transformation moves the isospin index of a quark-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_Q (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.QComponent f l (s, c, w))
      = ∑ a, conj (V.1 a w) • h.QComponent f l (s, c, a)
```

**`StandardModel.IsFermionSector.repGauge_u1_Q`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L386).

> A hypercharge transformation scales a quark-doublet symbol by the conjugate scalar,
> the quark doublet carrying `6Y = -1`.

```lean
lemma repGauge_u1_Q (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.QComponent f l (s, c, w))
      = star (t : ℂ) • h.QComponent f l (s, c, w)
```

### B.6. The conjugate quark doublet

**`StandardModel.IsFermionSector.repGauge_su3_barQ`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L401).

> A colour transformation moves the colour index of a conjugate quark-doublet symbol by
> the matrix itself, the index being fundamental.

```lean
lemma repGauge_su3_barQ (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barQComponent f l (s, c, w))
      = ∑ a, U.1 a c • h.barQComponent f l (s, a, w)
```

**`StandardModel.IsFermionSector.repGauge_su2_barQ`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L413).

> An isospin transformation moves the isospin index of a conjugate quark-doublet symbol
> by the matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barQ (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.barQComponent f l (s, c, w))
      = ∑ a, V.1 a w • h.barQComponent f l (s, c, a)
```

**`StandardModel.IsFermionSector.repGauge_u1_barQ`**, a lemma, [line 424](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L424).

> A hypercharge transformation scales a conjugate quark-doublet symbol by the scalar,
> the conjugate quark doublet carrying `6Y = 1`.

```lean
lemma repGauge_u1_barQ (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) (c : Fin 3) (w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barQComponent f l (s, c, w))
      = (t : ℂ) • h.barQComponent f l (s, c, w)
```

### B.7. The lepton doublet

**`StandardModel.IsFermionSector.repGauge_su3_L`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L439).

> A colour transformation fixes a lepton-doublet symbol, which carries no colour.

```lean
lemma repGauge_su3_L (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.LComponent f l j)
      = h.LComponent f l j
```

**`StandardModel.IsFermionSector.repGauge_su2_L`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L448).

> An isospin transformation moves the isospin index of a lepton-doublet symbol by the
> conjugate matrix, the index being anti-fundamental.

```lean
lemma repGauge_su2_L (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.LComponent f l (s, w))
      = ∑ a, conj (V.1 a w) • h.LComponent f l (s, a)
```

**`StandardModel.IsFermionSector.repGauge_u1_L`**, a lemma, [line 459](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L459).

> A hypercharge transformation scales a lepton-doublet symbol by the cube of the scalar,
> the lepton doublet carrying `6Y = 3`.

```lean
lemma repGauge_u1_L (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (j : Fin 2 × Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.LComponent f l j)
      = (t : ℂ) ^ 3 • h.LComponent f l j
```

### B.8. The conjugate lepton doublet

**`StandardModel.IsFermionSector.repGauge_su3_barL`**, a lemma, [line 474](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L474).

> A colour transformation fixes a conjugate lepton-doublet symbol, which carries no
> colour.

```lean
lemma repGauge_su3_barL (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (j : Fin 2 × Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.barLComponent f l j)
      = h.barLComponent f l j
```

**`StandardModel.IsFermionSector.repGauge_su2_barL`**, a lemma, [line 483](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L483).

> An isospin transformation moves the isospin index of a conjugate lepton-doublet symbol
> by the matrix itself, the index being fundamental.

```lean
lemma repGauge_su2_barL (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s w : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.barLComponent f l (s, w))
      = ∑ a, V.1 a w • h.barLComponent f l (s, a)
```

**`StandardModel.IsFermionSector.repGauge_u1_barL`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L494).

> A hypercharge transformation scales a conjugate lepton-doublet symbol by the cube of
> the conjugate scalar, the conjugate lepton doublet carrying `6Y = -3`.

```lean
lemma repGauge_u1_barL (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s w : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.barLComponent f l (s, w))
      = (star (t : ℂ)) ^ 3 • h.barLComponent f l (s, w)
```

### B.9. The lepton singlet

**`StandardModel.IsFermionSector.repGauge_su3_e`**, a lemma, [line 509](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L509).

> A colour transformation fixes a lepton-singlet symbol.

```lean
lemma repGauge_su3_e (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.eComponent f l s)
      = h.eComponent f l s
```

**`StandardModel.IsFermionSector.repGauge_su2_e`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L517).

> An isospin transformation fixes a lepton-singlet symbol.

```lean
lemma repGauge_su2_e (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.eComponent f l s)
      = h.eComponent f l s
```

**`StandardModel.IsFermionSector.repGauge_u1_e`**, a lemma, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L526).

> A hypercharge transformation scales a lepton-singlet symbol by the sixth power of the
> scalar, the lepton singlet carrying `6Y = 6`.

```lean
lemma repGauge_u1_e (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.eComponent f l s)
      = (t : ℂ) ^ 6 • h.eComponent f l s
```

### B.10. The conjugate lepton singlet

**`StandardModel.IsFermionSector.repGauge_su3_bare`**, a lemma, [line 540](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L540).

> A colour transformation fixes a conjugate lepton-singlet symbol.

```lean
lemma repGauge_su3_bare (U : specialUnitaryGroup (Fin 3) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((U, 1, 1) : GaugeGroupI) (h.bareComponent f l s)
      = h.bareComponent f l s
```

**`StandardModel.IsFermionSector.repGauge_su2_bare`**, a lemma, [line 548](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L548).

> An isospin transformation fixes a conjugate lepton-singlet symbol.

```lean
lemma repGauge_su2_bare (V : specialUnitaryGroup (Fin 2) ℂ) (f : Fin 3) {n : ℕ}
    (l : Fin n → Fin 1 ⊕ Fin 3) (s : Fin 2) :
    repGauge ((1, V, 1) : GaugeGroupI) (h.bareComponent f l s)
      = h.bareComponent f l s
```

**`StandardModel.IsFermionSector.repGauge_u1_bare`**, a lemma, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L557).

> A hypercharge transformation scales a conjugate lepton-singlet symbol by the sixth
> power of the conjugate scalar, the conjugate lepton singlet carrying `6Y = -6`.

```lean
lemma repGauge_u1_bare (t : unitary ℂ) (f : Fin 3) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3)
    (s : Fin 2) :
    repGauge ((1, 1, t) : GaugeGroupI) (h.bareComponent f l s)
      = (star (t : ℂ)) ^ 6 • h.bareComponent f l s
```

## C. Products of two components

> A block is a product of two components, and each of its index laws comes from the laws of
> the two factors: the representation respects multiplication, so the two transform
> independently and their coefficients multiply. Which slot of the classifier a factor
> occupies is decided by its variance, the fundamental one going first, so each law comes in
> two arrangements according to which factor is the barred one.

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_mul`**, a lemma, [line 578](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L578).

> A product of a component with a fundamental colour index and one with an
> anti-fundamental colour index carries one colour index of each kind.

```lean
lemma isSU3FundamentalAntiFundamental_mul
    (hmul : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
      repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    {A C : Fin 3 → B}
    (hA : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (A c) = ∑ a, U.1 a c • A a)
    (hC : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (C c) = ∑ a, conj (U.1 a c) • C a) :
    IsSU3FundamentalAntiFundamental B repGauge (fun l : Fin 2 → Fin 3 => A (l 0) * C (l 1))
```

**`StandardModel.IsFermionSector.isSU3FundamentalAntiFundamental_mul_swap`**, a lemma, [line 594](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L594).

> The same with the two factors exchanged, the anti-fundamental one first.

```lean
lemma isSU3FundamentalAntiFundamental_mul_swap
    (hmul : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
      repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    {A C : Fin 3 → B}
    (hA : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (A c) = ∑ a, conj (U.1 a c) • A a)
    (hC : ∀ (U : specialUnitaryGroup (Fin 3) ℂ) (c : Fin 3),
      repGauge ((U, 1, 1) : GaugeGroupI) (C c) = ∑ a, U.1 a c • C a) :
    IsSU3FundamentalAntiFundamental B repGauge (fun l : Fin 2 → Fin 3 => A (l 1) * C (l 0))
```

**`StandardModel.IsFermionSector.isSU2FundamentalAntiFundamental_mul`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L611).

> A product of a component with a fundamental isospin index and one with an
> anti-fundamental isospin index carries one isospin index of each kind.

```lean
lemma isSU2FundamentalAntiFundamental_mul
    (hmul : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
      repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    {A C : Fin 2 → B}
    (hA : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (A w) = ∑ a, V.1 a w • A a)
    (hC : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (C w) = ∑ a, conj (V.1 a w) • C a) :
    IsSU2FundamentalAntiFundamental B repGauge (fun l : Fin 2 → Fin 2 => A (l 0) * C (l 1))
```

**`StandardModel.IsFermionSector.isSU2FundamentalAntiFundamental_mul_swap`**, a lemma, [line 627](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L627).

> The same with the two factors exchanged, the anti-fundamental one first.

```lean
lemma isSU2FundamentalAntiFundamental_mul_swap
    (hmul : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
      repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    {A C : Fin 2 → B}
    (hA : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (A w) = ∑ a, conj (V.1 a w) • A a)
    (hC : ∀ (V : specialUnitaryGroup (Fin 2) ℂ) (w : Fin 2),
      repGauge ((1, V, 1) : GaugeGroupI) (C w) = ∑ a, V.1 a w • C a) :
    IsSU2FundamentalAntiFundamental B repGauge (fun l : Fin 2 → Fin 2 => A (l 1) * C (l 0))
```

**`StandardModel.IsFermionSector.repGauge_mul_fixed`**, a lemma, [line 645](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L645).

> A product of two components that a gauge transformation fixes is fixed by it: the
> form in which a block whose symbols carry no colour, or no isospin, supplies the
> corresponding stage.

```lean
lemma repGauge_mul_fixed
    (hmul : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
      repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    {g : GaugeGroupI} {a c : B} (ha : repGauge g a = a) (hc : repGauge g c = c) :
    repGauge g (a * c) = a * c
```

**`StandardModel.IsFermionSector.repGauge_mul_smul_fixed`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L655).

> A product of two components that a gauge transformation scales by reciprocal scalars
> is fixed by it: the form in which the hypercharges of a species and its conjugate
> cancel.

```lean
lemma repGauge_mul_smul_fixed
    (hmul : ∀ (g : GaugeGroupI) (b₁ b₂ : B),
      repGauge g (b₁ * b₂) = repGauge g b₁ * repGauge g b₂)
    {g : GaugeGroupI} {z z' : ℂ} {a c : B} (hz : z * z' = 1)
    (ha : repGauge g a = z • a) (hc : repGauge g c = z' • c) :
    repGauge g (a * c) = a * c
```

**`StandardModel.IsFermionSector.isVectorDualLeftRightWeyl_sum`**, a lemma, [line 668](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L668).

> A finite sum of families carrying one four-vector index and a pair of dual
> opposite-chirality Weyl indices is such a family again: the colour and isospin
> contractions are Lorentz spectators.

```lean
lemma isVectorDualLeftRightWeyl_sum {ι : Type} [Fintype ι]
    {T : ι → (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 → B}
    (hT : ∀ i, IsVectorDualLeftRightWeyl B repLorentz (ofDualVectorComponents (T i))) :
    IsVectorDualLeftRightWeyl B repLorentz (ofDualVectorComponents fun p => ∑ i, T i p)
```

**`StandardModel.IsFermionSector.unitary_mul_star_coe`**, a lemma, [line 677](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L677).

> A unitary scalar times its conjugate is one, in the order the hypercharge cancellation
> of a species against its conjugate needs.

```lean
lemma unitary_mul_star_coe (t : unitary ℂ) : (t : ℂ) * star (t : ℂ) = 1
```

**`StandardModel.IsFermionSector.unitary_star_mul_coe`**, a lemma, [line 680](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L680).

> The conjugate of a unitary scalar times itself is one.

```lean
lemma unitary_star_mul_coe (t : unitary ℂ) : star (t : ℂ) * (t : ℂ) = 1
```

## D. The kinetic block package

> A kinetic block is classified in three stages, and every block runs the same three: colour,
> then isospin, then Lorentz, each contraction a spectator of the ones after it. `KineticBlock`
> packages a block together with the three steps, and from the package alone come the kinetic
> term, its invariance under both groups, and the reduction of the block to the line
> through it.
>
> The colour and isospin indices of the block are listed in the order the classifiers read
> them, fundamental first; a block whose symbols carry no colour, or no isospin, simply
> ignores the corresponding pair and supplies `InvariantReductionToSpan.ofFixedFamily` for that
> stage. Each step comes with the fact that its contraction lies in the submodule it classifies, which
> is what carries the invariance of one stage through the stages after it.

**`StandardModel.IsFermionSector.KineticBlock`**, a structure, [line 709](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L709).

> One kinetic block of the fermion sector, together with the three classifications its
> indices admit. The block is indexed by the derivative direction, the pair of spinor
> indices in the order `(undotted, dotted)`, the pair of colour indices and the pair of
> isospin indices, each pair in the order `(fundamental, anti-fundamental)`.

```lean
structure KineticBlock where
  /-- The components of the block. -/
  blk : (Fin 1 ⊕ Fin 3) → Fin 2 × Fin 2 → Fin 3 → Fin 3 → Fin 2 → Fin 2 → B
  /-- The colour stage: at fixed derivative, spinor and isospin indices the colour pair is
    classified, by the delta contraction if the block carries colour and trivially if it
    does not. -/
  colourStep : ∀ (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2) (w w' : Fin 2),
    InvariantReductionToSpan (fun U : specialUnitaryGroup (Fin 3) ℂ => repGauge (U, 1, 1))
      (Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 3 => blk q l (n 0) (n 1) w w'))
  /-- The colour contraction lies in the span of the components it contracts. -/
  colourStep_mem : ∀ q l w w', (colourStep q l w w').spanningVector
    ∈ Submodule.span ℂ (Set.range fun n : Fin 2 → Fin 3 => blk q l (n 0) (n 1) w w')
  /-- The isospin stage, applied to the colour contraction. -/
  isospinStep : ∀ (q : Fin 1 ⊕ Fin 3) (l : Fin 2 × Fin 2),
    InvariantReductionToSpan (fun V : specialUnitaryGroup (Fin 2) ℂ => repGauge (1, V, 1))
      (Submodule.span ℂ
        (Set.range fun n : Fin 2 → Fin 2 => (colourStep q l (n 0) (n 1)).spanningVector))
  /-- The isospin contraction lies in the span of the colour contractions. -/
  isospinStep_mem : ∀ q l, (isospinStep q l).spanningVector
    ∈ Submodule.span ℂ
      (Set.range fun n : Fin 2 → Fin 2 => (colourStep q l (n 0) (n 1)).spanningVector)
  /-- The Lorentz stage, applied to the doubly contracted block: one four-vector index
    against a dual dotted and a dual undotted spinor index. -/
  lorentzStep : InvariantReductionToSpan (fun Λ : SL(2,ℂ) => repLorentz Λ)
    (Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
      (isospinStep p.1 p.2).spanningVector))
  /-- The Lorentz contraction lies in the span of the isospin contractions. -/
  lorentzStep_mem : lorentzStep.spanningVector
    ∈ Submodule.span ℂ (Set.range fun p : (Fin 1 ⊕ Fin 3) × Fin 2 × Fin 2 =>
      (isospinStep p.1 p.2).spanningVector)
  /-- A hypercharge transformation fixes every component of the block, the hypercharges of
    a species and its conjugate cancelling. -/
  hyper : ∀ (t : unitary ℂ) q l c c' w w',
    repGauge ((1, 1, t) : GaugeGroupI) (blk q l c c' w w') = blk q l c c' w w'
```

**`StandardModel.IsFermionSector.KineticBlock.kineticTerm`**, a def, [line 750](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L750).

> The kinetic term of a block: the conjugate Pauli contraction of its doubly contracted
> form, which is `ψ̄ σ̄^μ ∂_μ ψ` with the colour and isospin indices already joined.

```lean
noncomputable def kineticTerm : B
```

**`StandardModel.IsFermionSector.KineticBlock.blockSpan`**, a def, [line 754](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L754).

> The join, over the derivative, spinor and isospin indices, of the colour spans of the
> block: what the block submodule is reduced from.

```lean
noncomputable def blockSpan : Submodule ℂ B
```

**`StandardModel.IsFermionSector.KineticBlock.reducesInvariantsTo`**, a lemma, [line 760](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L760).

> The three stages in sequence: the block span reduces to the span of the kinetic term.

```lean
lemma reducesInvariantsTo :
    ReducesInvariantsTo (gaugeLorentzMaps repGauge repLorentz) K.blockSpan (ℂ ∙ K.kineticTerm)
```

**`StandardModel.IsFermionSector.KineticBlock.kineticTerm_mem`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L785).

> The kinetic term lies in any submodule containing every component of the block: each
> contraction lies in the span of the objects of the stage before it.

```lean
lemma kineticTerm_mem {V : Submodule ℂ B}
    (hV : ∀ q l c c' w w', K.blk q l c c' w w' ∈ V) : K.kineticTerm ∈ V
```

**`StandardModel.IsFermionSector.KineticBlock.repGauge_su3_kineticTerm`**, a lemma, [line 800](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L800).

> The kinetic term is fixed by the colour factor: the colour contractions are, and every
> later stage stays inside their span.

```lean
lemma repGauge_su3_kineticTerm (U : specialUnitaryGroup (Fin 3) ℂ) :
    repGauge ((U, 1, 1) : GaugeGroupI) K.kineticTerm = K.kineticTerm
```

**`StandardModel.IsFermionSector.KineticBlock.repGauge_su2_kineticTerm`**, a lemma, [line 811](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L811).

> The kinetic term is fixed by the isospin factor.

```lean
lemma repGauge_su2_kineticTerm (V : specialUnitaryGroup (Fin 2) ℂ) :
    repGauge ((1, V, 1) : GaugeGroupI) K.kineticTerm = K.kineticTerm
```

**`StandardModel.IsFermionSector.KineticBlock.repGauge_u1_kineticTerm`**, a lemma, [line 818](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L818).

> The kinetic term is fixed by the hypercharge factor, the hypercharges of a species and
> its conjugate cancelling on every component of the block.

```lean
lemma repGauge_u1_kineticTerm (t : unitary ℂ) :
    repGauge ((1, 1, t) : GaugeGroupI) K.kineticTerm = K.kineticTerm
```

**`StandardModel.IsFermionSector.KineticBlock.repGauge_kineticTerm`**, a lemma, [line 834](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L834).

> The kinetic term is gauge invariant: a gauge transformation is the product of its
> colour, isospin and hypercharge parts, and each fixes it.

```lean
lemma repGauge_kineticTerm (g : GaugeGroupI) : repGauge g K.kineticTerm = K.kineticTerm
```

**`StandardModel.IsFermionSector.KineticBlock.repLorentz_kineticTerm`**, a lemma, [line 840](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean#L840).

> The kinetic term is Lorentz invariant, being the conjugate Pauli contraction of a
> vector dual left-right Weyl family.

```lean
lemma repLorentz_kineticTerm (Λ : SL(2,ℂ)) :
    repLorentz Λ K.kineticTerm = K.kineticTerm
```

## Depends on

- [Families of colour and isospin components and their invariants](../part-04/gaugegroup-invariants-basic.md)
- [Invariant reduction for the gauge and Lorentz groups](../part-01/invariantreduction.md)
- [The invariants below mass weight eight (IsFermionSector/MassWeight/MassDimLTEight)](../part-06/isfermionsector-massweight-massdimlteight.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/IsFermionSector/MassWeight/KineticFamilies.lean)
