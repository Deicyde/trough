---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.Cfg, CondensedMatter.QuasiLocal.restr, CondensedMatter.QuasiLocal.Agree, CondensedMatter.QuasiLocal.glue, CondensedMatter.QuasiLocal.restr_glue, CondensedMatter.QuasiLocal.agree_glue, CondensedMatter.QuasiLocal.agree_iff_glue, CondensedMatter.QuasiLocal.agree_refl
statement: formalized
proof: formalized
---

# Local algebras of a system with a finite configuration space at each site

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.Local`, [PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean): 24 declarations (1 instance with no name), 7 with a docstring.

> The algebra of operators of a finite region is the algebra of matrices on the configurations of
> its sites, and a larger region contains it through `M ↦ M ⊗ 1`.

## i. Overview

> Every site `s` of a system carries a finite set `Ω s`: the basis states of its local Hilbert
> space, such as the two `σ^z` values of a spin, the occupation numbers of a fermion mode, or the
> orbitals of an atom. A configuration of a finite region `X` assigns a value to each of its sites,
> and the Hilbert space of the region is spanned by these configurations. This is the tensor
> product of the local spaces. The operators of the region are the complex matrices indexed by its
> configurations, a finite-dimensional C*-algebra, and the operators of a larger region `Y ⊇ X`
> contain them as `M ↦ M ⊗ 1`: `M` acts on the sites of `X` and the identity on the others.
> This is an injective unital `*`-homomorphism, compatible with composition.
>
> The sites may be the sites of an infinite crystal, and the regions are its finite subsets, so
> that the quasi-local algebra of the infinite system is the limit of the local ones. Only finite
> site spaces are used.

## ii. Key results

> - `Cfg` : the configurations of a region.
> - `Alg` : the algebra of operators of a region.
> - `inclStarAlg` : the inclusion `M ↦ M ⊗ 1` as a unital `*`-homomorphism.
> - `inclMat_trans`, `inclMat_refl` : functoriality of the inclusions.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 6.1.

## A. Configurations of a region and gluing

**`CondensedMatter.QuasiLocal.Cfg`**, an abbrev, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L71).

> The configurations of a region: a value of the local configuration space at each of its
> sites.

```lean
abbrev Cfg (X : Finset S) : Type _
```

**`CondensedMatter.QuasiLocal.restr`**, an abbrev, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L76).

> The restriction of a configuration of a region to a subregion.

```lean
abbrev restr {X Y : Finset S} (h : X ≤ Y) (c : Cfg Ω Y) : Cfg Ω X
```

**`CondensedMatter.QuasiLocal.Agree`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L79).

> Two configurations of a region agree outside a subregion.

```lean
def Agree {X Y : Finset S} (_h : X ≤ Y) (c c' : Cfg Ω Y) : Prop
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L81).

```lean
instance {X Y : Finset S} (h : X ≤ Y) (c c' : Cfg Ω Y) : Decidable (Agree h c c')
```

**`CondensedMatter.QuasiLocal.glue`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L85).

> Replace the values of `c` inside the subregion `X` by those of `a`.

```lean
def glue {X Y : Finset S} (_h : X ≤ Y) (c : Cfg Ω Y) (a : Cfg Ω X) : Cfg Ω Y
```

**`CondensedMatter.QuasiLocal.restr_glue`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L90).

```lean
lemma restr_glue {X Y : Finset S} (h : X ≤ Y) (c : Cfg Ω Y) (a : Cfg Ω X) :
    restr h (glue h c a) = a
```

**`CondensedMatter.QuasiLocal.agree_glue`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L96).

```lean
lemma agree_glue {X Y : Finset S} (h : X ≤ Y) (c : Cfg Ω Y) (a : Cfg Ω X) :
    Agree h c (glue h c a)
```

**`CondensedMatter.QuasiLocal.agree_iff_glue`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L102).

```lean
lemma agree_iff_glue {X Y : Finset S} (h : X ≤ Y) {c c' : Cfg Ω Y} :
    Agree h c c' ↔ glue h c (restr h c') = c'
```

**`CondensedMatter.QuasiLocal.agree_refl`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L116).

```lean
lemma agree_refl {X Y : Finset S} (h : X ≤ Y) (c : Cfg Ω Y) : Agree h c c
```

**`CondensedMatter.QuasiLocal.Agree.symm`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L121).

```lean
lemma Agree.symm {X Y : Finset S} {h : X ≤ Y} {c c' : Cfg Ω Y} (hc : Agree h c c') :
    Agree h c' c
```

**`CondensedMatter.QuasiLocal.Agree.trans`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L127).

```lean
lemma Agree.trans {X Y : Finset S} {h : X ≤ Y} {c c' c'' : Cfg Ω Y} (hc : Agree h c c')
    (hc' : Agree h c' c'') : Agree h c c''
```

**`CondensedMatter.QuasiLocal.eq_of_agree_of_restr_eq`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L132).

```lean
lemma eq_of_agree_of_restr_eq {X Y : Finset S} {h : X ≤ Y} {c c' : Cfg Ω Y} (hc : Agree h c c')
    (hr : restr h c = restr h c') : c = c'
```

## B. The operator `M ⊗ 1`

**`CondensedMatter.QuasiLocal.Alg`**, an abbrev, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L147).

> The operators on the sites of a region: matrices indexed by configurations.

```lean
abbrev Alg (X : Finset S) : Type _
```

**`CondensedMatter.QuasiLocal.inclMat`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L151).

> The operator `M ⊗ 1` on a larger region: `M` on the sites of `X` and the identity on the other
> sites.

```lean
def inclMat {X Y : Finset S} (h : X ≤ Y) (M : Alg Ω X) : Alg Ω Y
```

**`CondensedMatter.QuasiLocal.inclMat_apply`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L155).

```lean
lemma inclMat_apply {X Y : Finset S} (h : X ≤ Y) (M : Alg Ω X) (c c' : Cfg Ω Y) :
    inclMat h M c c' = if Agree h c c' then M (restr h c) (restr h c') else 0
```

**`CondensedMatter.QuasiLocal.inclMat_one`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L159).

```lean
lemma inclMat_one {X Y : Finset S} (h : X ≤ Y) : inclMat h (1 : Alg Ω X) = 1
```

**`CondensedMatter.QuasiLocal.inclMat_add`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L172).

```lean
lemma inclMat_add {X Y : Finset S} (h : X ≤ Y) (M N : Alg Ω X) :
    inclMat h (M + N) = inclMat h M + inclMat h N
```

**`CondensedMatter.QuasiLocal.inclMat_smul`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L177).

```lean
lemma inclMat_smul {X Y : Finset S} (h : X ≤ Y) (r : ℂ) (M : Alg Ω X) :
    inclMat h (r • M) = r • inclMat h M
```

**`CondensedMatter.QuasiLocal.inclMat_conjTranspose`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L182).

```lean
lemma inclMat_conjTranspose {X Y : Finset S} (h : X ≤ Y) (M : Alg Ω X) :
    inclMat h Mᴴ = (inclMat h M)ᴴ
```

**`CondensedMatter.QuasiLocal.inclMat_mul`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L191).

```lean
lemma inclMat_mul {X Y : Finset S} (h : X ≤ Y) (M N : Alg Ω X) :
    inclMat h (M * N) = inclMat h M * inclMat h N
```

**`CondensedMatter.QuasiLocal.inclMat_refl`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L227).

```lean
lemma inclMat_refl {X : Finset S} (M : Alg Ω X) : inclMat (le_refl X) M = M
```

**`CondensedMatter.QuasiLocal.agree_trans_iff`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L234).

```lean
lemma agree_trans_iff {X Y Z : Finset S} (h₁ : X ≤ Y) (h₂ : Y ≤ Z) (c c' : Cfg Ω Z) :
    Agree (h₁.trans h₂) c c' ↔ Agree h₂ c c' ∧ Agree h₁ (restr h₂ c) (restr h₂ c')
```

**`CondensedMatter.QuasiLocal.inclMat_trans`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L245).

```lean
lemma inclMat_trans {X Y Z : Finset S} (h₁ : X ≤ Y) (h₂ : Y ≤ Z) (M : Alg Ω X) :
    inclMat (h₁.trans h₂) M = inclMat h₂ (inclMat h₁ M)
```

**`CondensedMatter.QuasiLocal.inclStarAlg`**, a def, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean#L258).

> The operator `M ⊗ 1` as a unital `*`-homomorphism.

```lean
def inclStarAlg {X Y : Finset S} (h : X ≤ Y) : Alg Ω X →⋆ₐ[ℂ] Alg Ω Y
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Local.lean)
