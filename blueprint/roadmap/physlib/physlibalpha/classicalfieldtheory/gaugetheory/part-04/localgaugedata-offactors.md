---
declaration: module
origin: cited
lean: LocalGaugeData.FactorSpec, LocalGaugeData.FactorSpec.G, LocalGaugeData.FactorSpec.𝔤, LocalGaugeData.FactorSpec.G₀, LocalGaugeData.FactorSpec.𝔤J, LocalGaugeData.FactorSpec.instGroupG, LocalGaugeData.FactorSpec.instGroupG₀, LocalGaugeData.FactorSpec.instLieRing𝔤
statement: formalized
proof: formalized
---

# Local gauge data from a list of factors

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalGaugeData.OfFactors`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean): 43 declarations (6 instances with no name), 22 with a docstring.

## i. Overview

> A gauge group is named, as in a model-building table, by a list of symbols `U1` and
> `SU n`. This file builds the local gauge data of such a list: the product, in the order of
> the list, of the local gauge data `LocalGaugeData.u1` and `LocalGaugeData.su n` of the
> factors. The carriers are the corresponding products of `JetU1` and `JetSU n`, and of
> their Lie algebras, so that a model's gauge group is a concrete product of matrix groups.
> The list of factors of the product, in the sense of the table layer, is assembled from
> the canonical factors of the pieces (`Factors.factors`), and the gauge data is faithful
> and free because each factor is and both properties pass to products.
>
> With this, a model on any gauge group built from `U(1)` and `SU(n)` factors is a table
> alone: `LocalGaugeData.ofFactors Γ` is its gauge data and `Factors.factors Γ` is what its
> rows are charged under.

## ii. Key results

> - `LocalGaugeData.FactorSpec` : the symbols `U1` and `SU n`.
> - `LocalGaugeData.ofFactors` : the local gauge data of a list of factors.
> - `LocalGaugeData.Factors.factors` : the canonical factors of that gauge data.
> - `LocalGaugeData.instFreeOfFactors` : that gauge data is free.

## iv. References

> * None.

## A. Factor symbols and their gauge data

**`LocalGaugeData.FactorSpec`**, an inductive, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L61).

> **A factor symbol**: `U(1)` or `SU(n)`.

```lean
inductive FactorSpec
  /-- The factor `U(1)`. -/
  | U1
  /-- The factor `SU(n)`. -/
  | SU (n : ℕ)
  deriving DecidableEq, Repr
```

**`LocalGaugeData.FactorSpec.G`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L71).

> The group of jets of a factor.

```lean
def G : FactorSpec → Type
```

**`LocalGaugeData.FactorSpec.𝔤`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L76).

> The Lie algebra of a factor.

```lean
def 𝔤 : FactorSpec → Type
```

**`LocalGaugeData.FactorSpec.G₀`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L81).

> The group of a factor.

```lean
def G₀ : FactorSpec → Type
```

**`LocalGaugeData.FactorSpec.𝔤J`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L86).

> The jets of the Lie algebra of a factor.

```lean
def 𝔤J : FactorSpec → Type
```

**`LocalGaugeData.FactorSpec.instGroupG`**, an instance, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L90).

```lean
noncomputable instance instGroupG : (f : FactorSpec) → Group f.G
```

**`LocalGaugeData.FactorSpec.instGroupG₀`**, an instance, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L94).

```lean
noncomputable instance instGroupG₀ : (f : FactorSpec) → Group f.G₀
```

**`LocalGaugeData.FactorSpec.instLieRing𝔤`**, an instance, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L98).

```lean
noncomputable instance instLieRing𝔤 : (f : FactorSpec) → LieRing f.𝔤
```

**`LocalGaugeData.FactorSpec.instLieAlgebra𝔤`**, an instance, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L102).

```lean
noncomputable instance instLieAlgebra𝔤 : (f : FactorSpec) → LieAlgebra ℝ f.𝔤
```

**`LocalGaugeData.FactorSpec.instLieRing𝔤J`**, an instance, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L106).

```lean
noncomputable instance instLieRing𝔤J : (f : FactorSpec) → LieRing f.𝔤J
```

**`LocalGaugeData.FactorSpec.instLieAlgebra𝔤J`**, an instance, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L110).

```lean
noncomputable instance instLieAlgebra𝔤J : (f : FactorSpec) → LieAlgebra ℝ f.𝔤J
```

**`LocalGaugeData.FactorSpec.instFinite𝔤`**, an instance, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L114).

```lean
noncomputable instance instFinite𝔤 : (f : FactorSpec) → Module.Finite ℝ f.𝔤
```

**`LocalGaugeData.FactorSpec.data`**, an abbrev, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L119).

> The local gauge data of a factor.

```lean
noncomputable abbrev data : (f : FactorSpec) → LocalGaugeData f.G₀ f.𝔤 f.G f.𝔤J
```

**`LocalGaugeData.FactorSpec.factor`**, an abbrev, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L124).

> The canonical factor of the local gauge data of a factor symbol.

```lean
noncomputable abbrev factor : (f : FactorSpec) → Factor f.data
```

**`LocalGaugeData.FactorSpec.instFaithfulData`**, an instance, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L128).

```lean
noncomputable instance instFaithfulData : (f : FactorSpec) → f.data.Faithful
```

**`LocalGaugeData.FactorSpec.instFreeData`**, an instance, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L132).

```lean
noncomputable instance instFreeData : (f : FactorSpec) → f.data.Free
```

## B. The carriers of a list of factors

> The carriers of a list of factors are the products, in the order of the list, of the
> carriers of the factors; a one-element list has the carriers of its factor. The carriers
> are definitions rather than abbreviations, so that instance search on them goes through
> the instances below rather than through the unfolded products: this keeps the instances
> found at every use site identical to those inside the gauge data.

**`LocalGaugeData.OfFactors.G`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L153).

> The group of jets of a list of factors.

```lean
def G : List FactorSpec → Type
```

**`LocalGaugeData.OfFactors.𝔤`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L159).

> The Lie algebra of a list of factors.

```lean
def 𝔤 : List FactorSpec → Type
```

**`LocalGaugeData.OfFactors.G₀`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L165).

> The group of a list of factors.

```lean
def G₀ : List FactorSpec → Type
```

**`LocalGaugeData.OfFactors.𝔤J`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L171).

> The jets of the Lie algebra of a list of factors.

```lean
def 𝔤J : List FactorSpec → Type
```

> The carriers are written by recursion on the list rather than as a fold, so that a single
> factor has its own carrier rather than `f.G × Unit`, and so that the carrier of a list
> unfolds to the literal product of the carriers of its factors, `JetSU 3 × JetSU 2 × JetU1`
> for the Standard Model. The same recursion gives the instances and the gauge data below.

**`LocalGaugeData.OfFactors.instGroupG`**, a def, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L185).

> The group structure on the jets of a list of factors, by recursion on the list.

```lean
noncomputable def instGroupG : (Γ : List FactorSpec) → Group (G Γ)
```

**An instance with no name**, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L192).

```lean
noncomputable instance (Γ : List FactorSpec) : Group (G Γ)
```

**`LocalGaugeData.OfFactors.instGroupG₀`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L196).

> The group structure on a list of factors, by recursion on the list.

```lean
noncomputable def instGroupG₀ : (Γ : List FactorSpec) → Group (G₀ Γ)
```

**An instance with no name**, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L203).

```lean
noncomputable instance (Γ : List FactorSpec) : Group (G₀ Γ)
```

**`LocalGaugeData.OfFactors.instLieRing𝔤`**, a def, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L207).

> The Lie ring structure on the Lie algebra of a list of factors, by recursion.

```lean
noncomputable def instLieRing𝔤 : (Γ : List FactorSpec) → LieRing (𝔤 Γ)
```

**An instance with no name**, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L214).

```lean
noncomputable instance (Γ : List FactorSpec) : LieRing (𝔤 Γ)
```

**`LocalGaugeData.OfFactors.instLieAlgebra𝔤`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L218).

> The real Lie algebra structure on the Lie algebra of a list of factors, by recursion.

```lean
noncomputable def instLieAlgebra𝔤 : (Γ : List FactorSpec) → LieAlgebra ℝ (𝔤 Γ)
```

**An instance with no name**, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L226).

```lean
noncomputable instance (Γ : List FactorSpec) : LieAlgebra ℝ (𝔤 Γ)
```

**`LocalGaugeData.OfFactors.instLieRing𝔤J`**, a def, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L230).

> The Lie ring structure on the jets of the Lie algebra of a list of factors, by recursion.

```lean
noncomputable def instLieRing𝔤J : (Γ : List FactorSpec) → LieRing (𝔤J Γ)
```

**An instance with no name**, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L237).

```lean
noncomputable instance (Γ : List FactorSpec) : LieRing (𝔤J Γ)
```

**`LocalGaugeData.OfFactors.instLieAlgebra𝔤J`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L241).

> The real Lie algebra structure on the jets of the Lie algebra of a list of factors.

```lean
noncomputable def instLieAlgebra𝔤J : (Γ : List FactorSpec) → LieAlgebra ℝ (𝔤J Γ)
```

**An instance with no name**, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L249).

```lean
noncomputable instance (Γ : List FactorSpec) : LieAlgebra ℝ (𝔤J Γ)
```

**`LocalGaugeData.OfFactors.instFinite𝔤`**, an instance, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L251).

```lean
instance instFinite𝔤 : (Γ : List FactorSpec) → Module.Finite ℝ (𝔤 Γ)
```

## C. The gauge data of a list of factors

**`LocalGaugeData.trivial`**, a def, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L269).

> The trivial local gauge data, of the empty list of factors.

```lean
noncomputable def trivial : LocalGaugeData Unit Unit Unit Unit
```

**`LocalGaugeData.instFaithfulTrivial`**, an instance, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L294).

```lean
instance instFaithfulTrivial : trivial.Faithful
```

**`LocalGaugeData.instFreeTrivial`**, an instance, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L298).

```lean
instance instFreeTrivial : trivial.Free
```

**`LocalGaugeData.ofFactors`**, a def, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L305).

> **The local gauge data of a list of factors**: the product, in the order of the list,
> of the local gauge data of the factors.

```lean
noncomputable def ofFactors : (Γ : List FactorSpec) → LocalGaugeData (G₀ Γ) (𝔤 Γ) (G Γ) (𝔤J Γ)
```

**`LocalGaugeData.ofFactors_nil`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L311).

```lean
lemma ofFactors_nil : ofFactors [] = trivial
```

**`LocalGaugeData.ofFactors_singleton`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L314).

```lean
lemma ofFactors_singleton (f : FactorSpec) : ofFactors [f] = f.data
```

**`LocalGaugeData.ofFactors_cons_cons`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L317).

```lean
lemma ofFactors_cons_cons (f g : FactorSpec) (gs : List FactorSpec) :
    ofFactors (f :: g :: gs) = f.data.prod (ofFactors (g :: gs))
```

**`LocalGaugeData.instFaithfulOfFactors`**, an instance, [line 321](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L321).

> The local gauge data of a list of factors is faithful.

```lean
noncomputable instance instFaithfulOfFactors : (Γ : List FactorSpec) → (ofFactors Γ).Faithful
```

**`LocalGaugeData.instFreeOfFactors`**, an instance, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L329).

> The local gauge data of a list of factors is free.

```lean
noncomputable instance instFreeOfFactors : (Γ : List FactorSpec) → (ofFactors Γ).Free
```

## D. The canonical factors

**`LocalGaugeData.Factors.factors`**, an abbrev, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean#L343).

> **The canonical factors** of the local gauge data of a list of factors.

```lean
noncomputable abbrev Factors.factors : (Γ : List FactorSpec) → Factors (ofFactors Γ)
```

## Depends on

- [The product of local gauge data](localgaugedata-prod.md)
- [The local gauge data of `SU(n)`](localgaugedata-su-basic.md)
- [The local gauge data of `U(1)`](localgaugedata-u1.md)
- [The zero Lie algebra on `Unit`](../../../mathematics/part-01/liealgebraunit.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalGaugeData/OfFactors.lean)
