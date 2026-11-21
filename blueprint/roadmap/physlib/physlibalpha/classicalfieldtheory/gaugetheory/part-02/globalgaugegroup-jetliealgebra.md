---
declaration: module
origin: cited
lean: GlobalGaugeGroup.jetLieAlgebra, GlobalGaugeGroup.mem_jetLieAlgebra, GlobalGaugeGroup.mem_jetLieAlgebra_iff, GlobalGaugeGroup.mem_jetLieAlgebra_of, GlobalGaugeGroup.map_pderiv_mem_jetLieAlgebra, GlobalGaugeGroup.commutator_mem_jetLieAlgebra, GlobalGaugeGroup.jetLieSubalgebra, GlobalGaugeGroup.mem_jetLieSubalgebra
statement: formalized
proof: formalized
---

# The Lie algebra jets of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.JetLieAlgebra`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean): 12 declarations (2 instances with no name), 7 with a docstring.

> The Taylor series at a point of the infinitesimal gauge transformations.

## i. Overview

> An infinitesimal gauge transformation of a global gauge group `G` with Lie algebra `𝔤` is a
> smooth map from spacetime into `𝔤`. Its jet at the base point is a matrix of formal power
> series in the spacetime coordinates, all of whose base-point derivatives `∂_s A (0)` lie in
> `𝔤`. These Lie algebra jets form a Lie algebra under the commutator, since by the Leibniz
> rule each base-point derivative of a commutator is a sum of commutators of base-point
> derivatives.
>
> Membership is checked through `mem_jetLieAlgebra_of`: a property of matrices of jets that is
> preserved by every derivative, and that places the value in `𝔤`, places every base-point
> derivative in `𝔤`. This is how the gauge jets are shown to act on the Lie algebra jets in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.GaugeJetGroup`.

## ii. Key results

> - `GlobalGaugeGroup.jetLieAlgebra` : the Lie algebra jets, as a real subspace.
> - `GlobalGaugeGroup.mem_jetLieAlgebra_iff` : a matrix of jets is a Lie algebra jet exactly
>   when its value lies in the Lie algebra and its derivatives are Lie algebra jets.
> - `GlobalGaugeGroup.mem_jetLieAlgebra_of` : the induction principle for Lie algebra jets.
> - `GlobalGaugeGroup.jetLieSubalgebra` : the Lie algebra jets, as a Lie subalgebra.

## iv. References

> * None.

## A. The Lie algebra jets

**`GlobalGaugeGroup.jetLieAlgebra`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L67).

> The real subspace of matrices of jets all of whose base-point derivatives lie in the
> Lie algebra.

```lean
def jetLieAlgebra : Submodule ℝ (Matrix κ κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.mem_jetLieAlgebra`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L79).

```lean
lemma mem_jetLieAlgebra {A : Matrix κ κ SpaceTimeAlgebra} :
    A ∈ G.jetLieAlgebra ↔ ∀ s, derivValueMatrix s A ∈ G.lieAlgebra
```

**`GlobalGaugeGroup.mem_jetLieAlgebra_iff`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L84).

> A matrix of jets is a Lie algebra jet exactly when its value lies in the Lie algebra and
> its derivatives are Lie algebra jets.

```lean
lemma mem_jetLieAlgebra_iff {A : Matrix κ κ SpaceTimeAlgebra} :
    A ∈ G.jetLieAlgebra ↔
      (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A ∈ G.lieAlgebra ∧
        ∀ μ, A.map (pderiv μ) ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.mem_jetLieAlgebra_of`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L97).

> An induction principle for Lie algebra jets: a property of matrices of jets that is
> preserved by every derivative, and that forces the value into the Lie algebra, forces
> every base-point derivative into the Lie algebra.

```lean
lemma mem_jetLieAlgebra_of {P : Matrix κ κ SpaceTimeAlgebra → Prop}
    (h0 : ∀ A, P A → (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A ∈ G.lieAlgebra)
    (hd : ∀ A, P A → ∀ μ, P (A.map (pderiv μ))) {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : P A) : A ∈ G.jetLieAlgebra
```

## B. Closure properties

**`GlobalGaugeGroup.map_pderiv_mem_jetLieAlgebra`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L112).

```lean
lemma map_pderiv_mem_jetLieAlgebra {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) (μ : Fin 1 ⊕ Fin 3) : A.map (pderiv μ) ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.commutator_mem_jetLieAlgebra`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L118).

> The Lie algebra jets are closed under the commutator: by the Leibniz rule each
> base-point derivative of a commutator is a sum of commutators of base-point derivatives.

```lean
lemma commutator_mem_jetLieAlgebra {A B : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) (hB : B ∈ G.jetLieAlgebra) : A * B - B * A ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.jetLieSubalgebra`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L131).

> The Lie algebra jets, as a Lie subalgebra of matrices of jets under the commutator.

```lean
def jetLieSubalgebra : LieSubalgebra ℝ (Matrix κ κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.mem_jetLieSubalgebra`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L138).

```lean
lemma mem_jetLieSubalgebra {A : Matrix κ κ SpaceTimeAlgebra} :
    A ∈ G.jetLieSubalgebra ↔ A ∈ G.jetLieAlgebra
```

**An instance with no name**, [line 141](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L141).

```lean
noncomputable instance : LieRing G.jetLieSubalgebra
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L143).

```lean
noncomputable instance : LieAlgebra ℝ G.jetLieSubalgebra
```

**`GlobalGaugeGroup.mapMatrix_C_mem_jetLieAlgebra`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L146).

> A constant matrix in the Lie algebra is a Lie algebra jet.

```lean
lemma mapMatrix_C_mem_jetLieAlgebra {a : Matrix κ κ ℂ} (ha : a ∈ G.lieAlgebra) :
    (C : ℂ →+* SpaceTimeAlgebra).mapMatrix a ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.X_smul_mem_jetLieAlgebra`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean#L156).

> The Lie algebra jets are closed under multiplication by a coordinate.

```lean
lemma X_smul_mem_jetLieAlgebra (μ : Fin 1 ⊕ Fin 3) {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) : (X μ : SpaceTimeAlgebra) • A ∈ G.jetLieAlgebra
```

## Depends on

- [Global gauge groups](globalgaugegroup-basic.md)
- [Taylor determinacy and completeness of jets](../../../spaceandtime/spacetime/spacetimealgebra-taylor.md)

## Proof depends on

- [Matrices over the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-matrix.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetLieAlgebra.lean)
