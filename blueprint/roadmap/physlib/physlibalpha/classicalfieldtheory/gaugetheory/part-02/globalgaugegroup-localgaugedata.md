---
declaration: module
origin: cited
lean: GlobalGaugeGroup.matrixJets, GlobalGaugeGroup.localGaugeData, GlobalGaugeGroup.localGaugeData_eval_val, GlobalGaugeGroup.localGaugeData_ofConstant_val, GlobalGaugeGroup.localGaugeData_evalLie_val, GlobalGaugeGroup.localGaugeData_ofConstantLie_val, GlobalGaugeGroup.localGaugeData_deriv_val, GlobalGaugeGroup.localGaugeData_mulCoord_val
statement: formalized
proof: formalized
---

# The local gauge data of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LocalGaugeData`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean): 12 declarations (1 instance with no name), 4 with a docstring.

> The jets of gauge transformations valued in a global gauge group, as local gauge data.

## i. Overview

> A global gauge group `G` with Lie algebra `𝔤` gives local gauge data
> `LocalGaugeData G 𝔤 GJ 𝔤J`, with `GJ` the gauge jets and `𝔤J` the Lie algebra jets.
> Evaluation is the entrywise constant coefficient, constants embed entrywise, the derivative
> and the coordinates act entrywise, the adjoint actions are conjugation `U A U⁻¹`, and the
> Maurer–Cartan form is `−(∂_μ U) U⁻¹`.
>
> Every structure map is the matrix one, so the package is a presentation by matrices of jets,
> `GlobalGaugeGroup.matrixJets`, and the laws of `LocalGaugeData` and its faithfulness come
> from `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.MatrixJets`. The
> presentation sends a generator `X` to `−i X`, so that the commutator becomes the bracket
> `i (a b − b a)` used throughout the gauge theory, and the Maurer–Cartan form `−(∂_μ U) U⁻¹`
> becomes `i (∂_μ U) U⁻¹`. For a compact group inside the unitary group these are the
> hermitian generators and the hermitian Maurer–Cartan form of physics.

## ii. Key results

> - `GlobalGaugeGroup.matrixJets` : the presentation of the jets by matrices of jets.
> - `GlobalGaugeGroup.localGaugeData` : the local gauge data of a global gauge group.

## iv. References

> * None.

## A. The presentation by matrices of jets

**`GlobalGaugeGroup.matrixJets`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L66).

> The presentation of the jets of a global gauge group by matrices of jets. A generator
> `X` of the Lie algebra is sent to `−i X`, so that the commutator becomes the bracket
> `i (a b − b a)`, and the Maurer–Cartan form `−(∂_μ U) U⁻¹` becomes `i (∂_μ U) U⁻¹`.

```lean
noncomputable def matrixJets :
    LocalGaugeData.MatrixJets κ G.group G.lieSubalgebra G.gaugeJetGroup G.jetLieSubalgebra
```

## B. The local gauge data

**`GlobalGaugeGroup.localGaugeData`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L156).

> The local gauge data of a global gauge group. The gauge jets are the invertible matrices
> of jets with value in the group and Maurer–Cartan form a Lie algebra jet, the Lie algebra
> jets are the matrices of jets with every base-point derivative in the Lie algebra, and
> every structure map is the matrix one.

```lean
noncomputable def localGaugeData :
    LocalGaugeData G.group G.lieSubalgebra G.gaugeJetGroup G.jetLieSubalgebra
```

**`GlobalGaugeGroup.localGaugeData_eval_val`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L161).

```lean
lemma localGaugeData_eval_val (U : G.gaugeJetGroup) :
    ((G.localGaugeData.eval U).1 : Matrix κ κ ℂ) =
      (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix U.1
```

**`GlobalGaugeGroup.localGaugeData_ofConstant_val`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L166).

```lean
lemma localGaugeData_ofConstant_val (g : G.group) :
    ((G.localGaugeData.ofConstant g).1 : Matrix κ κ SpaceTimeAlgebra) =
      (C : ℂ →+* SpaceTimeAlgebra).mapMatrix g.1
```

**`GlobalGaugeGroup.localGaugeData_evalLie_val`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L171).

```lean
lemma localGaugeData_evalLie_val (A : G.jetLieSubalgebra) :
    (G.localGaugeData.evalLie A).1 = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A.1
```

**`GlobalGaugeGroup.localGaugeData_ofConstantLie_val`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L176).

```lean
lemma localGaugeData_ofConstantLie_val (a : G.lieSubalgebra) :
    (G.localGaugeData.ofConstantLie a).1 = (C : ℂ →+* SpaceTimeAlgebra).mapMatrix a.1
```

**`GlobalGaugeGroup.localGaugeData_deriv_val`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L180).

```lean
lemma localGaugeData_deriv_val (μ : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    (G.localGaugeData.deriv μ A).1 = A.1.map (pderiv μ)
```

**`GlobalGaugeGroup.localGaugeData_mulCoord_val`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L184).

```lean
lemma localGaugeData_mulCoord_val (μ : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    (G.localGaugeData.mulCoord μ A).1 = (X μ : SpaceTimeAlgebra) • A.1
```

**`GlobalGaugeGroup.localGaugeData_adjointJ_val`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L188).

```lean
lemma localGaugeData_adjointJ_val (U : G.gaugeJetGroup) (A : G.jetLieSubalgebra) :
    (G.localGaugeData.adjointJ U A).1 = U.1.1 * A.1 * (U.1⁻¹).1
```

**`GlobalGaugeGroup.localGaugeData_adjoint_val`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L192).

```lean
lemma localGaugeData_adjoint_val (g : G.group) (a : G.lieSubalgebra) :
    (G.localGaugeData.adjoint g a).1 = g.1.1 * a.1 * (g.1⁻¹).1
```

**`GlobalGaugeGroup.localGaugeData_maurerCartan_val`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L197).

> The Maurer–Cartan form of a gauge jet is `−(∂_μ U) U⁻¹`.

```lean
lemma localGaugeData_maurerCartan_val (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    (G.localGaugeData.maurerCartan U μ).1 = -(U.1.1.map (pderiv μ) * (U.1⁻¹).1)
```

**An instance with no name**, [line 201](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean#L201).

> The local gauge data of a global gauge group is faithful.

```lean
instance : G.localGaugeData.Faithful
```

## Depends on

- [The gauge jets of a global gauge group](globalgaugegroup-gaugejetgroup.md)
- [Matrix jet groups](../part-04/localgaugedata-matrixjets.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LocalGaugeData.lean)
