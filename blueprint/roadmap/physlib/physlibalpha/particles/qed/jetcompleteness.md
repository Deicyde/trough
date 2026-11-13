---
declaration: module
origin: cited
lean: QED.Photon.JetGenerators.indexClass_dA, QED.Photon.JetGenerators.indexClass_ne_zero, QED.Photon.JetGenerators.indexClass_classProj, QED.Photon.JetGenerators.classProj_idem, QED.Photon.JetGenerators.classProj_eq_classProj_iff, QED.Photon.JetAlgebra.coord_sub_classProj, QED.Photon.JetAlgebra.fieldStrength_mem_range, QED.Photon.JetAlgebra.gaugeInvariant_iff_mem_adjoin_fieldStrength
statement: formalized
proof: formalized
---

# Completeness of the field strength for gauge invariance

The module `PhyslibAlpha.Particles.QED.JetCompleteness`, [PhyslibAlpha/Particles/QED/JetCompleteness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean): 8 declarations, 6 with a docstring.

## i. Overview

> The classification of the gauge invariants of the photon jet algebra:
> **an element of the photon jet algebra is invariant under every gauge
> transformation if and only if it is a polynomial in the derivatives
> `∂_s F_{μν}` of the field strength** —
> `gaugeInvariant_iff_mem_adjoin_fieldStrength`.
>
> One direction is the gauge invariance of the field strength.  For the other,
> the gauge action translates all jet coordinates with the same symmetrized
> index class `s + {μ}` by a common arbitrary amount, so an invariant is a
> polynomial in differences of same-class coordinates
> (`MvPolynomial.mem_adjoin_range_X_sub_X_of_forall_aeval_add_eq`), and every
> such difference is a derivative of the field strength.
>
> This is the abelian counterpart of the fixed-algebra theorems of
> `Physlib.Particles.StandardModel.GaugeBosons.Gluons.JetCompleteness`.
>
> This file contains no definitions, only theorems about the jet algebras of
> `PhyslibAlpha.Particles.QED.Basic`.

## ii. Key results

> - `Photon.JetAlgebra.gaugeInvariant_iff_mem_adjoin_fieldStrength` : **the
>   gauge invariants of the photon jet algebra are exactly the polynomials in
>   the derivatives of the field strength**.

## iv. References

> The class projection is defined in `PhyslibAlpha.Particles.QED.Basic`; the
> translation-invariance engine is `PhyslibAlpha.Mathematics.MvPolynomialTranslation`;
> the non-abelian analogue is
> `Physlib.Particles.StandardModel.GaugeBosons.Gluons.JetCompleteness`.

> …

> …

> …

> …

## A. The symmetrized-index class projection

**`QED.Photon.JetGenerators.indexClass_dA`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L76).

```lean
lemma indexClass_dA (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3) :
    (JetGenerators.dA s μ).indexClass = s + {μ}
```

**`QED.Photon.JetGenerators.indexClass_ne_zero`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L79).

```lean
lemma indexClass_ne_zero (j : JetGenerators) : j.indexClass ≠ 0
```

**`QED.Photon.JetGenerators.indexClass_classProj`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L88).

> Erasing the class representative and putting it back as the Lorentz index
> preserves the class.

```lean
lemma indexClass_classProj (j : JetGenerators) :
    j.classProj.indexClass = j.indexClass
```

**`QED.Photon.JetGenerators.classProj_idem`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L94).

> The class projection is idempotent.

```lean
lemma classProj_idem (j : JetGenerators) : j.classProj.classProj = j.classProj
```

**`QED.Photon.JetGenerators.classProj_eq_classProj_iff`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L101).

> Two jet coordinates have the same class projection exactly when they lie
> in the same symmetrized-index class.

```lean
lemma classProj_eq_classProj_iff (j j' : JetGenerators) :
    j.classProj = j'.classProj ↔ j.indexClass = j'.indexClass
```

## B. Differences of same-class coordinates are field strengths

**`QED.Photon.JetAlgebra.coord_sub_classProj`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L121).

> A jet coordinate minus the canonical coordinate of its class is a
> derivative of the field strength.

```lean
lemma coord_sub_classProj (s : Multiset (Fin 1 ⊕ Fin 3)) (μ : Fin 1 ⊕ Fin 3)
    (h : (JetGenerators.dA s μ).classProj ≠ JetGenerators.dA s μ) :
    (X (JetGenerators.dA s μ) : JetAlgebra) - X ((JetGenerators.dA s μ).classProj) =
      fieldStrength (s.erase (classRep (s + {μ}))) (classRep (s + {μ})) μ
```

**`QED.Photon.JetAlgebra.fieldStrength_mem_range`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L145).

> Every field-strength jet lies in the range of the field-strength family.

```lean
lemma fieldStrength_mem_range (t : Multiset (Fin 1 ⊕ Fin 3)) (μ ν : Fin 1 ⊕ Fin 3) :
    fieldStrength t μ ν ∈ Set.range (fun p :
        Multiset (Fin 1 ⊕ Fin 3) × (Fin 1 ⊕ Fin 3) × (Fin 1 ⊕ Fin 3) =>
        fieldStrength p.1 p.2.1 p.2.2)
```

## C. The completeness theorem

**`QED.Photon.JetAlgebra.gaugeInvariant_iff_mem_adjoin_fieldStrength`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean#L163).

> **Completeness of the field strength for gauge invariance**: an element of
> the photon jet algebra is invariant under every gauge transformation if and
> only if it is a polynomial in the derivatives `∂_s F_{μν}` of the field
> strength.  The field strength does not just provide *some* gauge invariants
> — it generates *all* of them.

```lean
lemma gaugeInvariant_iff_mem_adjoin_fieldStrength (x : JetAlgebra) :
    (∀ c : GaugeJet, gaugeAction c x = x) ↔
      x ∈ Algebra.adjoin ℝ (Set.range fun p :
        Multiset (Fin 1 ⊕ Fin 3) × (Fin 1 ⊕ Fin 3) × (Fin 1 ⊕ Fin 3) =>
        fieldStrength p.1 p.2.1 p.2.2)
```

## Depends on

- [The fields of quantum electrodynamics](fields.md)

## Proof depends on

- [Polynomials invariant under fiberwise translations of variables](../../mathematics/part-01/mvpolynomialtranslation.md)
- [Gauge invariance of quantum electrodynamics](gaugeinvariance.md)

## Sources

- [PhyslibAlpha/Particles/QED/JetCompleteness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/QED/JetCompleteness.lean)
