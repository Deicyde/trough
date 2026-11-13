---
declaration: module
origin: cited
lean: StandardModel.LeptonDoubletV.weakEnd, StandardModel.LeptonDoubletV.weakEnd_tmul, StandardModel.LeptonDoubletV.weakEnd_add, StandardModel.LeptonDoubletV.weakEnd_smul, StandardModel.LeptonDoubletV.weakEnd_zero, StandardModel.LeptonDoubletV.weakEnd_neg, StandardModel.LeptonDoubletV.weakEnd_multiset_sum, StandardModel.LeptonDoubletV.weakEnd_mul
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the lepton doublet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.LeptonDoublet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean): 20 declarations, 15 with a docstring.

## i. Overview

> The infinitesimal `(1, 2)_{-3}` action of the gauge algebra on the lepton doublet: the
> weak part of the algebra element acts on the weak index and the hypercharge part scales,
> both through the physicists' factor of `i`, matching the group action
> `(star u) ^ 3 • U₂` infinitesimally. Every definition is the one the general theory
> derives from the table's datum `StandardModel.Model.leptonDoublet`; the compatibility with
> the jet gauge action —
> `LocalGaugeData.IsInfinitesimalActionOf` — is the generic
> `LocalGaugeData.MatrixRep.isInfinitesimalActionOf`. The hand-built definitions and the
> hand-written proof are kept in comments.

## ii. Key results

> - `weakEnd` : the endomorphism of the lepton doublet defined by a `2 × 2` matrix on the
>   weak index.
> - `gaugeAlgebraAction` : the infinitesimal `(1, 2)_{-3}` action of the gauge algebra.
> - `isInfinitesimalActionOf` : the gauge-algebra action is the infinitesimal action
>   underlying the jet gauge action `repJetGaugeGroupI`.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.LeptonDoubletV.weakEnd`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L63).

> The endomorphism of the lepton doublet defined by a `2 × 2` complex matrix acting on
> the weak index, with the Weyl factor untouched.

```lean
noncomputable def weakEnd (A : Matrix (Fin 2) (Fin 2) ℂ) :
    LeptonDoubletV →ₗ[ℂ] LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.weakEnd_tmul`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L80).

> The weak endomorphism on a pure spinor–weak tensor: the matrix acts on the weak
> coordinates.

```lean
lemma weakEnd_tmul (A : Matrix (Fin 2) (Fin 2) ℂ) (s : Fermion.LeftHandedWeyl)
    (v : Fin 2 → ℂ) :
    weakEnd A (s ⊗ₜ v) = s ⊗ₜ A.mulVec v
```

**`StandardModel.LeptonDoubletV.weakEnd_add`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L85).

```lean
lemma weakEnd_add (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (A + B) = weakEnd A + weakEnd B
```

**`StandardModel.LeptonDoubletV.weakEnd_smul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L89).

```lean
lemma weakEnd_smul (z : ℂ) (A : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (z • A) = z • weakEnd A
```

**`StandardModel.LeptonDoubletV.weakEnd_zero`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L93).

```lean
lemma weakEnd_zero : weakEnd 0 = 0
```

**`StandardModel.LeptonDoubletV.weakEnd_neg`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L96).

```lean
lemma weakEnd_neg (A : Matrix (Fin 2) (Fin 2) ℂ) : weakEnd (-A) = -weakEnd A
```

**`StandardModel.LeptonDoubletV.weakEnd_multiset_sum`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L99).

```lean
lemma weakEnd_multiset_sum (m : Multiset (Matrix (Fin 2) (Fin 2) ℂ)) :
    weakEnd m.sum = (m.map weakEnd).sum
```

**`StandardModel.LeptonDoubletV.weakEnd_mul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L104).

> The weak endomorphisms compose through matrix multiplication.

```lean
lemma weakEnd_mul (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (A * B) = weakEnd A ∘ₗ weakEnd B
```

**`StandardModel.LeptonDoubletV.weakEnd_one`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L109).

> The weak endomorphism of the identity matrix is the identity.

```lean
lemma weakEnd_one : weakEnd 1 = LinearMap.id
```

**`StandardModel.LeptonDoubletV.actionMatrix`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L154).

> The matrix of the infinitesimal `(1, 2)_{-3}` action of a gauge algebra element on
> the weak index: the action matrix of the datum.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 2) (Fin 2) ℂ
```

**`StandardModel.LeptonDoubletV.actionMatrix_eq`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L159).

> The action matrix is `i` times the weak part, shifted by `i` times `-3` the
> hypercharge.

```lean
lemma actionMatrix_eq (c : GaugeAlgebra) :
    actionMatrix c = Complex.I • (c.toSU2Matrix - ((3 : ℂ) • c.toU1Value) • 1)
```

**`StandardModel.LeptonDoubletV.gaugeAlgebraAction`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L174).

> **The infinitesimal action of the gauge algebra on the lepton doublet**: the
> derivative of the `(1, 2)_{-3}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot — the form consumed by the
> covariant derivative `GaugeAlgebraRealization.covDerivIter` and by
> `LocalGaugeData.IsInfinitesimalActionOf`. It is the action the general theory derives
> from the datum.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] LeptonDoubletV →ₗ[ℂ] LeptonDoubletV
```

**`StandardModel.LeptonDoubletV.gaugeAlgebraAction_apply`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L179).

> The gauge algebra acts by the weak endomorphism of its action matrix.

```lean
lemma gaugeAlgebraAction_apply (c : GaugeAlgebra) :
    gaugeAlgebraAction c = weakEnd (actionMatrix c)
```

## B. The infinitesimal action underlies the jet gauge action

> The `(1, 2)_{-3}` action of the gauge algebra is the infinitesimal action underlying the
> jet gauge action, in the sense of `LocalGaugeData.IsInfinitesimalActionOf`: this is the
> generic `LocalGaugeData.MatrixRep.isInfinitesimalActionOf`, proved once for every matrix
> representation of jets. The jet action matrix and the base-point Taylor coefficients of
> the jet action are likewise those of the datum.

**`StandardModel.LeptonDoubletV.jetActionMatrix`**, a def, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L238).

> The jet-valued matrix of the infinitesimal `(1, 2)_{-3}` action of a jet of gauge
> algebra elements: the jet action matrix of the datum.

```lean
noncomputable def jetActionMatrix (a : JetGaugeAlgebra) : Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra
```

**`StandardModel.LeptonDoubletV.jetActionMatrix_eq`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L243).

> The jet action matrix is `i` times the weak part, shifted by `i` times `-3` the
> hypercharge.

```lean
lemma jetActionMatrix_eq (a : JetGaugeAlgebra) :
    jetActionMatrix a = Complex.I • (a.toSU2Matrix - ((3 : ℂ) • a.toU1Value) • 1)
```

**`StandardModel.LeptonDoubletV.jetActionMatrix_map_cc_foldl`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L257).

> The base-point Taylor coefficients of the jet action matrix are the action matrices
> of the base-point Taylor coefficients.

```lean
lemma jetActionMatrix_map_cc_foldl (p : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    ((jetActionMatrix a).map fun f =>
        constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
      = actionMatrix (JetGaugeAlgebra.eval (JetGaugeAlgebra.iteratedDeriv p a))
```

**`StandardModel.LeptonDoubletV.repCoeff_eq`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L542).

> **The base-point Taylor coefficients of the jet gauge action** on the lepton
> doublet are the weak endomorphisms of the base-point Taylor coefficients of the
> weak matrix.

```lean
lemma repCoeff_eq (U : JetGaugeGroupI) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U x
      = weakEnd ((doubletMatrix U).map fun f =>
          constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f))
```

**`StandardModel.LeptonDoubletV.repCoeff_zero_of_eval_eq_one`**, a lemma, [line 622](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L622).

> At the base point, a gauge jet with trivial value acts trivially: the zeroth
> Taylor coefficient of the jet gauge action is the identity.

```lean
lemma repCoeff_zero_of_eval_eq_one {U : JetGaugeGroupI} (hU : U.eval = 1) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U 0 = LinearMap.id
```

**`StandardModel.LeptonDoubletV.isInfinitesimalActionOf`**, a lemma, [line 645](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L645).

> **The `(1, 2)_{-3}` action of the gauge algebra is the infinitesimal action
> underlying the jet gauge action on the lepton doublet**: its base-point Taylor
> coefficients obey the Maurer–Cartan Leibniz law and intertwine the action with the
> adjoint transports. This is the generic statement for the datum's matrix
> representation.

```lean
lemma isInfinitesimalActionOf :
    localGaugeData.IsInfinitesimalActionOf gaugeAlgebraAction repJetGaugeGroupI
```

## C. The gauge action commutes with the Lorentz action

**`StandardModel.LeptonDoubletV.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 771](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean#L771).

> The infinitesimal gauge action on the lepton doublet acts on the weak factor, the
> Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : LeptonDoubletV) :
    LeptonDoubletV.gaugeAlgebraAction c (LeptonDoubletV.repLorentzGroup Λ v) =
      LeptonDoubletV.repLorentzGroup Λ (LeptonDoubletV.gaugeAlgebraAction c v)
```

## Depends on

- [Lepton doublets](fermions-leptondoublet-basic.md)
- [The Standard Model gauge group as local gauge data](../part-04/gaugegroup-localgaugedata.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/LeptonDoublet/GaugeAlgebraAction.lean)
