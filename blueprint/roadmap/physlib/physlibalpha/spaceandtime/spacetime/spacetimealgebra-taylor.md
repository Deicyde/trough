---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.star_ofDerivValues, SpaceTimeAlgebra.ofDerivValues_sum, SpaceTimeAlgebra.taylorMatrix, SpaceTimeAlgebra.taylorMatrix_apply, SpaceTimeAlgebra.star_taylorMatrix, SpaceTimeAlgebra.trace_taylorMatrix, SpaceTimeAlgebra.map_constantCoeff_iteratedPDeriv_taylorMatrix
statement: formalized
proof: formalized
---

# Taylor determinacy and completeness of jets

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Taylor`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean): 7 declarations, 2 with a docstring.

## i. Overview

> A jet is determined by the base-point values of its iterated derivatives, and a jet all of
> whose first derivatives vanish is the constant jet of its value. These are the two facts
> that make the jets of a matrix gauge group a faithful package of local gauge data, in the
> sense of `LocalGaugeData.Faithful`. Conversely every family of base-point Taylor data is
> realized by a jet, `ofDerivValues`, and entrywise by a matrix of jets, `taylorMatrix`: this
> is the Taylor completeness half of `LocalGaugeData.Free`.

## ii. Key results

> - `SpaceTimeAlgebra.ext_of_constantCoeff_iteratedPDeriv` : Taylor determinacy.
> - `SpaceTimeAlgebra.eq_C_of_pderiv_eq_zero` : a jet with vanishing derivatives is constant.
> - `SpaceTimeAlgebra.ofDerivValues` :
>   Taylor completeness.
> - `SpaceTimeAlgebra.taylorMatrix` : Taylor completeness for matrices of jets.

## iv. References

> * None.

## A. Taylor completeness

**`SpaceTimeAlgebra.star_ofDerivValues`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L52).

```lean
lemma star_ofDerivValues (f : Multiset (Fin 1 ⊕ Fin 3) → ℂ) :
    star (ofDerivValues f) = ofDerivValues fun s => star (f s)
```

**`SpaceTimeAlgebra.ofDerivValues_sum`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L58).

```lean
lemma ofDerivValues_sum {ι : Type} (t : Finset ι) (f : ι → Multiset (Fin 1 ⊕ Fin 3) → ℂ) :
    ofDerivValues (fun s => ∑ i ∈ t, f i s) = ∑ i ∈ t, ofDerivValues (f i)
```

**`SpaceTimeAlgebra.taylorMatrix`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L64).

> The matrix of jets with prescribed base-point Taylor data `M`, entrywise.

```lean
noncomputable def taylorMatrix {κ : Type} (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) :
    Matrix κ κ SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.taylorMatrix_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L68).

```lean
lemma taylorMatrix_apply {κ : Type} (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) (i j : κ) :
    taylorMatrix M i j = ofDerivValues fun s => M s i j
```

**`SpaceTimeAlgebra.star_taylorMatrix`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L72).

```lean
lemma star_taylorMatrix {κ : Type} {M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ}
    (hM : ∀ s, star (M s) = M s) : star (taylorMatrix M) = taylorMatrix M
```

**`SpaceTimeAlgebra.trace_taylorMatrix`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L78).

```lean
lemma trace_taylorMatrix {κ : Type} [Fintype κ] {M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ}
    (hM : ∀ s, (M s).trace = 0) : (taylorMatrix M).trace = 0
```

**`SpaceTimeAlgebra.map_constantCoeff_iteratedPDeriv_taylorMatrix`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L86).

> The base-point Taylor data of `taylorMatrix M` are `M`, entrywise.

```lean
lemma map_constantCoeff_iteratedPDeriv_taylorMatrix {κ : Type}
    (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (taylorMatrix M).map (fun f => constantCoeff (iteratedPDeriv s f)) = M s
```

## Depends on

- [Complex conjugation in the spacetime algebra](../../../physlib/spaceandtime/spacetime/spacetimealgebra-star.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean)
