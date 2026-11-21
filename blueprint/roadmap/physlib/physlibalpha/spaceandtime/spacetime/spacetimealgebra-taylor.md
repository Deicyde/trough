---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.star_ofDerivValues, SpaceTimeAlgebra.ofDerivValues_sum, SpaceTimeAlgebra.taylorMatrix, SpaceTimeAlgebra.taylorMatrix_apply, SpaceTimeAlgebra.star_taylorMatrix, SpaceTimeAlgebra.trace_taylorMatrix, SpaceTimeAlgebra.map_constantCoeff_iteratedPDeriv_taylorMatrix, SpaceTimeAlgebra.derivValueMatrix
statement: formalized
proof: formalized
---

# Taylor determinacy and completeness of jets

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Taylor`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean): 13 declarations, 3 with a docstring.

## i. Overview

> A jet is determined by the base-point values of its iterated derivatives, and a jet all of
> whose first derivatives vanish is the constant jet of its value. These are the two facts
> that make the jets of a matrix gauge group a faithful package of local gauge data, in the
> sense of `LocalGaugeData.Faithful`. Conversely every family of base-point Taylor data is
> realized by a jet, `ofDerivValues`, and entrywise by a matrix of jets, `taylorMatrix`: this
> is the Taylor completeness half of `LocalGaugeData.Free`. In the other direction,
> `derivValueMatrix` reads off the base-point Taylor data of a matrix of jets.

## ii. Key results

> - `SpaceTimeAlgebra.ext_of_constantCoeff_iteratedPDeriv` : Taylor determinacy.
> - `SpaceTimeAlgebra.eq_C_of_pderiv_eq_zero` : a jet with vanishing derivatives is constant.
> - `SpaceTimeAlgebra.ofDerivValues` :
>   Taylor completeness.
> - `SpaceTimeAlgebra.taylorMatrix` : Taylor completeness for matrices of jets.
> - `SpaceTimeAlgebra.derivValueMatrix` : the base-point Taylor data of a matrix of jets.

## iv. References

> * None.

## A. Taylor completeness

**`SpaceTimeAlgebra.star_ofDerivValues`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L55).

```lean
lemma star_ofDerivValues (f : Multiset (Fin 1 ⊕ Fin 3) → ℂ) :
    star (ofDerivValues f) = ofDerivValues fun s => star (f s)
```

**`SpaceTimeAlgebra.ofDerivValues_sum`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L61).

```lean
lemma ofDerivValues_sum {ι : Type} (t : Finset ι) (f : ι → Multiset (Fin 1 ⊕ Fin 3) → ℂ) :
    ofDerivValues (fun s => ∑ i ∈ t, f i s) = ∑ i ∈ t, ofDerivValues (f i)
```

**`SpaceTimeAlgebra.taylorMatrix`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L67).

> The matrix of jets with prescribed base-point Taylor data `M`, entrywise.

```lean
noncomputable def taylorMatrix {κ : Type} (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) :
    Matrix κ κ SpaceTimeAlgebra
```

**`SpaceTimeAlgebra.taylorMatrix_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L71).

```lean
lemma taylorMatrix_apply {κ : Type} (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) (i j : κ) :
    taylorMatrix M i j = ofDerivValues fun s => M s i j
```

**`SpaceTimeAlgebra.star_taylorMatrix`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L75).

```lean
lemma star_taylorMatrix {κ : Type} {M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ}
    (hM : ∀ s, star (M s) = M s) : star (taylorMatrix M) = taylorMatrix M
```

**`SpaceTimeAlgebra.trace_taylorMatrix`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L81).

```lean
lemma trace_taylorMatrix {κ : Type} [Fintype κ] {M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ}
    (hM : ∀ s, (M s).trace = 0) : (taylorMatrix M).trace = 0
```

**`SpaceTimeAlgebra.map_constantCoeff_iteratedPDeriv_taylorMatrix`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L89).

> The base-point Taylor data of `taylorMatrix M` are `M`, entrywise.

```lean
lemma map_constantCoeff_iteratedPDeriv_taylorMatrix {κ : Type}
    (M : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    (taylorMatrix M).map (fun f => constantCoeff (iteratedPDeriv s f)) = M s
```

## B. Base-point derivatives of matrices of jets

**`SpaceTimeAlgebra.derivValueMatrix`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L108).

> The base-point values of the iterated derivatives of a matrix of jets along a multiset
> of directions, taken entrywise. These are the Taylor coefficients up to the factorial
> factor, matching `SpaceTimeAlgebra.ofDerivValues`.

```lean
noncomputable def derivValueMatrix (s : Multiset (Fin 1 ⊕ Fin 3))
    (A : Matrix κ κ SpaceTimeAlgebra) : Matrix κ κ ℂ
```

**`SpaceTimeAlgebra.derivValueMatrix_cons`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L112).

```lean
lemma derivValueMatrix_cons (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (A : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix (μ ::ₘ s) A = derivValueMatrix s (A.map (pderiv μ))
```

**`SpaceTimeAlgebra.derivValueMatrix_add`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L118).

```lean
lemma derivValueMatrix_add (s : Multiset (Fin 1 ⊕ Fin 3)) (A B : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix s (A + B) = derivValueMatrix s A + derivValueMatrix s B
```

**`SpaceTimeAlgebra.derivValueMatrix_real_smul`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L123).

```lean
lemma derivValueMatrix_real_smul (s : Multiset (Fin 1 ⊕ Fin 3)) (r : ℝ)
    (A : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix s (r • A) = r • derivValueMatrix s A
```

**`SpaceTimeAlgebra.derivValueMatrix_zero_right`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L132).

```lean
lemma derivValueMatrix_zero_right (s : Multiset (Fin 1 ⊕ Fin 3)) :
    derivValueMatrix s (0 : Matrix κ κ SpaceTimeAlgebra) = 0
```

**`SpaceTimeAlgebra.derivValueMatrix_zero`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean#L140).

```lean
lemma derivValueMatrix_zero (A : Matrix κ κ SpaceTimeAlgebra) :
    derivValueMatrix 0 A = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A
```

## Depends on

- [Complex conjugation in the spacetime algebra](../../../physlib/spaceandtime/spacetime/spacetimealgebra-star.md)

## Proof depends on

- [Star, derivatives, truncation and the Euler operator on the jet ring](spacetimealgebra-basic.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Taylor.lean)
