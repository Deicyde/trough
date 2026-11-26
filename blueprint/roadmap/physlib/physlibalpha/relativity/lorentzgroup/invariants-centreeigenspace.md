---
declaration: module
origin: cited
lean: Lorentz.Invariants.centreEigenspace, Lorentz.Invariants.mem_centreEigenspace, Lorentz.Invariants.dual_neg_one_eq_smul_id, Lorentz.Invariants.range_le_centreEigenspace, Lorentz.Invariants.range_le_centreEigenspace_neg_one, Lorentz.Invariants.mul_le_centreEigenspace, Lorentz.Invariants.mem_of_invariant_of_mem_sup_centreEigenspace_neg_one, Lorentz.centreSign
statement: formalized
proof: formalized
---

# The eigenspaces of the centre of `SL(2,ℂ)`

The module `PhyslibAlpha.Relativity.LorentzGroup.Invariants.CentreEigenspace`, [PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean): 11 declarations, 11 with a docstring.

> The subspaces on which the central element `-1` of `SL(2,ℂ)` acts by a scalar, and the Lorentz
> invariants of a half-integer spin.

## i. Overview

> The classifications of the invariant tensors contract the components with a coefficient tensor.
> This file settles, in one step and for every pattern at once, the patterns that carry no
> invariant for the crudest of reasons: they are of half-integer spin, and a half-integer spin has
> no invariant because the centre of `SL(2,ℂ)` already tells integer spin from half-integer spin
> apart.
>
> The element `-1` of `SL(2,ℂ)` covers the identity Lorentz transformation
> (`SL2C.toLorentzGroup_neg_one`), so a representation of `SL(2,ℂ)` that factors through the
> Lorentz group — a tensor of four-vector indices — sends it to the identity, while each Weyl
> index contributes a sign. A subspace with an odd number of Weyl indices therefore lies in the
> `-1` eigenspace of `repLorentz (-1)`, and a vector both fixed by the group and negated by `-1`
> is zero. `centreEigenspace` names the eigenspace, `mul_le_centreEigenspace` multiplies the two
> signs in a product of subspaces, and `mem_of_invariant_of_mem_sup_centreEigenspace_neg_one` is
> the classification modulo a Lorentz-stable subspace `S`, the form the Standard Model files use.
>
> The subspaces that arise there are spans of symbol families, so section B reads the sign of
> such a span off the sign of the value space: the covariant-derivative slots of a family
> obeying `IsLorentzCovDerivTransforms` are inert at the centre, and only the value index moves.
>
> The argument uses the central element alone: it needs neither a grading nor a light-cone
> basis. On the complex Lorentz tensors `-1` acts on each Weyl index by `-1` and on each
> four-vector index by `1`, so on the tensors with colours `c` by `(-1)` to the number of Weyl
> colours of `c`, and with an odd number of Weyl indices there are no invariant tensors but zero
> (E).

## ii. Key results

> - `centreEigenspace` : the subspace on which the centre of `SL(2,ℂ)` acts by the scalar `ε`: an
>   integer spin sits at `ε = 1` and a half-integer spin at `ε = -1`
> - `mul_le_centreEigenspace` : the sign of a product is the product of the signs
> - `mem_of_invariant_of_mem_sup_centreEigenspace_neg_one` : a subspace of half-integer spin carries
>   no Lorentz invariant beyond a Lorentz-stable submodule `S`: an invariant of the join with `S`
>   already lies in `S`
> - `complexLorentzTensor.tensorRep_neg_one` : `-1` acts on the tensors by `(-1)` to the number of
>   Weyl colours
> - `complexLorentzTensor.invariants_eq_bot_of_odd_weyl` : tensors with an odd number of Weyl
>   indices have no invariants but zero

## iv. References

> * None.

## A. The sign a subspace carries at the centre

> The centre of `SL(2,ℂ)` is `±1` and squares to the identity, so `repLorentz (-1)` is an
> involution and the only signs on offer are `±1`. A tensor of four-vector indices carries `1`,
> a Weyl index carries `-1`, and nothing else is needed of the pattern.

**`Lorentz.Invariants.centreEigenspace`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L93).

> The subspace on which the centre of `SL(2,ℂ)` acts by the scalar `ε`: an integer spin
> sits at `ε = 1` and a half-integer spin at `ε = -1`.

```lean
def centreEigenspace (repLorentz : Representation ℂ SL(2,ℂ) V) (ε : ℂ) : Submodule ℂ V
```

**`Lorentz.Invariants.mem_centreEigenspace`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L97).

> Membership of `centreEigenspace` unfolded: the centre scales the vector by `ε`.

```lean
lemma mem_centreEigenspace {repLorentz : Representation ℂ SL(2,ℂ) V} {ε : ℂ} {x : V} :
    x ∈ centreEigenspace repLorentz ε ↔ repLorentz (-1) x = ε • x
```

**`Lorentz.Invariants.dual_neg_one_eq_smul_id`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L103).

> Dualising a representation preserves the sign at the centre: `-1` is its own inverse, so
> the contragredient action of the centre is the transpose of a scalar.

```lean
lemma dual_neg_one_eq_smul_id {rep : Representation ℂ SL(2,ℂ) V} {ε : ℂ}
    (hrep : rep (-1) = ε • LinearMap.id) : rep.dual (-1) = ε • LinearMap.id
```

## B. The sign of a symbol family

> A family of symbols transforming as the covariant derivatives of a field valued in `V` carries
> at the centre the sign that `V` does. The derivative slots mix by the Lorentz matrix, which is
> the identity at the centre, so they contribute nothing; the value index moves by `rep.dual`,
> which carries the sign of `rep` by section A. Both signs that occur are recorded, `ε = 1` for
> the Lorentz-scalar value spaces and `ε = -1` for the Weyl ones.

**`Lorentz.Invariants.range_le_centreEigenspace`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L124).

> **The span of one symbol family carries the sign of its value space.**

```lean
lemma range_le_centreEigenspace {repLorentz : Representation ℂ SL(2,ℂ) A}
    {rep : Representation ℂ SL(2,ℂ) V}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] A}
    (hF : IsLorentzCovDerivTransforms repLorentz rep F) {ε : ℂ}
    (hrep : rep (-1) = ε • LinearMap.id) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (F l) ≤ centreEigenspace repLorentz ε
```

**`Lorentz.Invariants.range_le_centreEigenspace_neg_one`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L136).

> The half-integer case of `range_le_centreEigenspace`, in the form the Weyl value spaces
> state their sign.

```lean
lemma range_le_centreEigenspace_neg_one {repLorentz : Representation ℂ SL(2,ℂ) A}
    {rep : Representation ℂ SL(2,ℂ) V}
    {F : {n : ℕ} → (Fin n → Fin 1 ⊕ Fin 3) → Module.Dual ℂ V →ₗ[ℂ] A}
    (hF : IsLorentzCovDerivTransforms repLorentz rep F)
    (hrep : rep (-1) = -LinearMap.id) {n : ℕ} (l : Fin n → Fin 1 ⊕ Fin 3) :
    LinearMap.range (F l) ≤ centreEigenspace repLorentz (-1)
```

## C. Signs multiply

> The Lorentz action on the field algebra is by algebra maps, so the sign a product carries is
> the product of the signs of its factors. This is the whole of the bookkeeping: two Weyl
> indices cancel and an odd number does not.

**`Lorentz.Invariants.mul_le_centreEigenspace`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L155).

> The sign of a product is the product of the signs.

```lean
lemma mul_le_centreEigenspace {repLorentz : Representation ℂ SL(2,ℂ) A}
    (hmul : ∀ (Λ : SL(2,ℂ)) (x y : A), repLorentz Λ (x * y) = repLorentz Λ x * repLorentz Λ y)
    {W₁ W₂ : Submodule ℂ A} {ε₁ ε₂ : ℂ} (h₁ : W₁ ≤ centreEigenspace repLorentz ε₁)
    (h₂ : W₂ ≤ centreEigenspace repLorentz ε₂) :
    W₁ * W₂ ≤ centreEigenspace repLorentz (ε₁ * ε₂)
```

## D. The classification modulo a Lorentz-stable submodule

> A vector of a subspace of sign `-1` that the group fixes is negated by `-1` and fixed by it at
> once, so it is zero. Modulo a stable subspace `S` this is the case `μ = -1` of
> `reducesInvariantsTo_bot_of_apply_eq_smul`: the invariance leaves `-2` times the vector inside
> `S`, and dividing by `-2` is allowed over `ℂ`; no quotient representation is needed.

**`Lorentz.Invariants.mem_of_invariant_of_mem_sup_centreEigenspace_neg_one`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L178).

> A subspace of half-integer spin carries no Lorentz invariant beyond a Lorentz-stable
> submodule `S`: an invariant of the join with `S` already lies in `S`. The centre acts on the
> subspace by `-1 ≠ 1`, so it reduces to `⊥`.

```lean
lemma mem_of_invariant_of_mem_sup_centreEigenspace_neg_one
    {repLorentz : Representation ℂ SL(2,ℂ) A} {W : Submodule ℂ A}
    (hW : W ≤ centreEigenspace repLorentz (-1)) (S : Submodule ℂ A)
    (hS : ∀ g : SL(2,ℂ), ∀ y ∈ S, repLorentz g y ∈ S) {x : A} (hx : x ∈ W ⊔ S)
    (hinv : ∀ g : SL(2,ℂ), repLorentz g x = x) : x ∈ S
```

## E. The centre on the complex Lorentz tensors

> The element `-1` covers the identity Lorentz transformation, so it acts on the four-vector colours
> by `1`, and on each Weyl colour by `-1`. On the tensors with colours `c` it therefore acts by the
> product of these signs, `(-1)` to the number of Weyl colours of `c`
> (`TensorSpecies.tensorRep_eq_prod_smul`). With an odd number of Weyl colours this is `-1`, and an
> invariant tensor both fixed and negated by `-1` is zero.

**`Lorentz.centreSign`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L204).

> The sign by which `-1` acts on a colour: `1` on the four-vector colours and `-1` on the Weyl
> colours.

```lean
def centreSign (k : complexLorentzTensor.Color) : ℂ
```

**`Lorentz.rep_neg_one`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L208).

> The element `-1` acts on the representation of each colour by its sign.

```lean
lemma rep_neg_one (k : complexLorentzTensor.Color) :
    complexLorentzTensor.rep k (-1) = centreSign k • LinearMap.id
```

**`complexLorentzTensor.tensorRep_neg_one`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L237).

> The element `-1` acts on the tensors with colours `c` by `(-1)` to the number of Weyl colours
> of `c`.

```lean
lemma _root_.complexLorentzTensor.tensorRep_neg_one {n : ℕ}
    (c : Fin n → complexLorentzTensor.Color) :
    complexLorentzTensor.tensorRep c (-1) =
      (-1 : ℂ) ^ (Finset.univ.filter fun i => ¬ (c i = .up ∨ c i = .down)).card •
        LinearMap.id
```

**`complexLorentzTensor.invariants_eq_bot_of_odd_weyl`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean#L249).

> The tensors with an odd number of Weyl indices have no invariants but zero. The element `-1`
> negates them, and an invariant tensor is fixed by it.

```lean
lemma _root_.complexLorentzTensor.invariants_eq_bot_of_odd_weyl {n : ℕ}
    {c : Fin n → complexLorentzTensor.Color}
    (h : Odd (Finset.univ.filter fun i => ¬ (c i = .up ∨ c i = .down)).card) :
    (complexLorentzTensor.tensorRep c).invariants = ⊥
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../../../physlib/relativity/tensors/part-01/complextensor-basic.md)
- [Class IsLorentzDeriv](../islorentzderiv.md)
- [Equivariant maps out of the tensors of a species](../tensors/equivariant.md)

## Proof depends on

- [Reynolds elements for complex Lorentz tensors](invariants-reynolds.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Relativity/LorentzGroup/Invariants/CentreEigenspace.lean)
