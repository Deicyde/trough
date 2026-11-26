---
declaration: module
origin: cited
lean: Physlib.CondensedMatter.Crystal.Symmetry, Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_eq_of_toEquiv_eq, Physlib.CondensedMatter.Crystal.Symmetry.ext, Physlib.CondensedMatter.Crystal.Symmetry.coe_toEquiv, Physlib.CondensedMatter.Crystal.Symmetry.map_vadd, Physlib.CondensedMatter.Crystal.Symmetry.mul_apply, Physlib.CondensedMatter.Crystal.Symmetry.one_apply, Physlib.CondensedMatter.Crystal.Symmetry.inv_apply_apply
statement: formalized
proof: formalized
---

# Symmetries of a crystal

The module `Physlib.CondensedMatter.Crystal.Symmetry.Basic`, [Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean): 25 declarations (5 instances with no name), 12 with a docstring.

> The operations that leave a crystal unchanged form its symmetry group.

## i. Overview

> A crystal looks the same after certain operations, its symmetries. The simplest are
> translations by lattice vectors. Other symmetries rotate or reflect the lattice, or exchange
> sites within a unit cell. In graphene, inversion through the centre of a bond exchanges the
> two carbon atoms of a unit cell.
>
> A symmetry permutes the sites and transforms the lattice vectors by an automorphism `A` of the
> translation group, so that
>
> `φ (a +ᵥ x) = A a +ᵥ φ x`.
>
> The same `A` applies everywhere in the crystal. For example, a quarter turn of a square lattice
> sends a step to the right to a step upwards.
>
> With one site per cell the symmetries are the affine equivalences of the sites. With several
> sites per cell a symmetry may also exchange the sites within a cell. The definition captures the
> periodic structure alone. It does not require symmetries to preserve distances, bonds or atomic
> species.
>
> Lattice translations form a normal subgroup of the symmetry group.

## ii. Key results

> - `Crystal.Symmetry` : a permutation of sites compatible with lattice translations.
> - `Crystal.Symmetry.latticeAut` : the induced automorphism of the translation group.
> - `Crystal.Symmetry.conj_translation` : conjugation transforms a translation by `a` into one
>   by `latticeAut a`.
> - `Crystal.Symmetry.translations` : the normal subgroup of lattice translations.

## iv. References

> * None.

## A. Crystal symmetries

**`Physlib.CondensedMatter.Crystal.Symmetry`**, a structure, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L72).

> A permutation of crystal sites compatible with lattice translations.
>
> The site permutation `φ` and the automorphism `A = latticeAut` satisfy
> `φ (a +ᵥ x) = A a +ᵥ φ x` for every lattice vector `a` and site `x`.

```lean
structure Symmetry (C : Crystal G) extends C.Site ≃ C.Site where
  /-- The automorphism induced on the translation group by the site permutation. -/
  latticeAut : G ≃+ G
  /-- Translating a site by `a` translates its image by `latticeAut a`. -/
  map_vadd' : ∀ (a : G) (x : C.Site), toEquiv (a +ᵥ x) = latticeAut a +ᵥ toEquiv x
```

**`Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_eq_of_toEquiv_eq`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L83).

> The action on sites uniquely determines the action on lattice vectors.

```lean
lemma latticeAut_eq_of_toEquiv_eq {φ ψ : Symmetry C} (h : φ.toEquiv = ψ.toEquiv) :
    φ.latticeAut = ψ.latticeAut
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L91).

> A crystal symmetry is an equivalence of its sites.

```lean
instance : EquivLike (Symmetry C) C.Site C.Site
```

**`Physlib.CondensedMatter.Crystal.Symmetry.ext`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L105).

> Two symmetries are equal if they agree on every site.

```lean
lemma ext {φ ψ : Symmetry C} (h : ∀ x, φ x = ψ x) : φ = ψ
```

**`Physlib.CondensedMatter.Crystal.Symmetry.coe_toEquiv`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L107).

```lean
lemma coe_toEquiv (φ : Symmetry C) : ⇑φ.toEquiv = φ
```

**`Physlib.CondensedMatter.Crystal.Symmetry.map_vadd`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L111).

> A symmetry maps the translation of a site by `a` to the translation of its image
> by `latticeAut a`.

```lean
lemma map_vadd (φ : Symmetry C) (a : G) (x : C.Site) : φ (a +ᵥ x) = φ.latticeAut a +ᵥ φ x
```

## B. The symmetry group

### B.1. Composition and inverses

**An instance with no name**, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L119).

> Crystal symmetries form a group under composition of their site permutations.

```lean
instance : Group (Symmetry C)
```

**`Physlib.CondensedMatter.Crystal.Symmetry.mul_apply`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L131).

```lean
lemma mul_apply (φ ψ : Symmetry C) (x : C.Site) : (φ * ψ) x = φ (ψ x)
```

**`Physlib.CondensedMatter.Crystal.Symmetry.one_apply`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L133).

```lean
lemma one_apply (x : C.Site) : (1 : Symmetry C) x = x
```

**`Physlib.CondensedMatter.Crystal.Symmetry.inv_apply_apply`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L135).

```lean
lemma inv_apply_apply (φ : Symmetry C) (x : C.Site) : φ⁻¹ (φ x) = x
```

**`Physlib.CondensedMatter.Crystal.Symmetry.apply_inv_apply`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L138).

```lean
lemma apply_inv_apply (φ : Symmetry C) (x : C.Site) : φ (φ⁻¹ x) = x
```

### B.2. Actions on sites and lattice vectors

**`Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_mul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L143).

```lean
lemma latticeAut_mul (φ ψ : Symmetry C) :
    (φ * ψ).latticeAut = ψ.latticeAut.trans φ.latticeAut
```

**`Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_one`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L146).

```lean
lemma latticeAut_one : (1 : Symmetry C).latticeAut = AddEquiv.refl G
```

**`Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_inv`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L148).

```lean
lemma latticeAut_inv (φ : Symmetry C) : φ⁻¹.latticeAut = φ.latticeAut.symm
```

**An instance with no name**, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L151).

> The symmetry group acts on crystal sites by permutations.

```lean
instance : MulAction (Symmetry C) C.Site
```

**`Physlib.CondensedMatter.Crystal.Symmetry.smul_site`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L156).

```lean
lemma smul_site (φ : Symmetry C) (x : C.Site) : φ • x = φ x
```

**An instance with no name**, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L159).

> The symmetry group acts on lattice vectors by automorphisms of the translation group.

```lean
instance : DistribMulAction (Symmetry C) G
```

**`Physlib.CondensedMatter.Crystal.Symmetry.smul_vector`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L166).

```lean
lemma smul_vector (φ : Symmetry C) (a : G) : φ • a = φ.latticeAut a
```

## C. Lattice translations

**`Physlib.CondensedMatter.Crystal.Symmetry.translationHom`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L171).

> The group homomorphism sending each lattice vector to its translation symmetry.

```lean
def translationHom (C : Crystal G) : Multiplicative G →* Symmetry C
```

**`Physlib.CondensedMatter.Crystal.Symmetry.translation`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L178).

> The symmetry that translates every site by the lattice vector `a`.

```lean
def translation (C : Crystal G) (a : G) : Symmetry C
```

**`Physlib.CondensedMatter.Crystal.Symmetry.translation_apply`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L181).

```lean
lemma translation_apply (a : G) (x : C.Site) : translation C a x = a +ᵥ x
```

**`Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_translation`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L183).

```lean
lemma latticeAut_translation (a : G) :
    (translation C a).latticeAut = AddEquiv.refl G
```

**`Physlib.CondensedMatter.Crystal.Symmetry.conj_translation`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L187).

> Conjugation by `φ` maps the translation by `a` to the translation by `φ.latticeAut a`.

```lean
lemma conj_translation (φ : Symmetry C) (a : G) :
    φ * translation C a * φ⁻¹ = translation C (φ.latticeAut a)
```

**`Physlib.CondensedMatter.Crystal.Symmetry.translations`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L193).

> The subgroup consisting of all lattice translations.

```lean
def translations (C : Crystal G) : Subgroup (Symmetry C)
```

**An instance with no name**, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean#L195).

```lean
instance : (translations C).Normal
```

## Depends on

- [Crystals, cells and sites (Physlib)](basic.md)

## Sources

- [Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/CondensedMatter/Crystal/Symmetry/Basic.lean)
