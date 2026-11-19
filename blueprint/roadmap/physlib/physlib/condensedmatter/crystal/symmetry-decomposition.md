---
declaration: module
origin: cited
lean: Physlib.CondensedMatter.Crystal.Symmetry.label_apply, Physlib.CondensedMatter.Crystal.Symmetry.labelPerm, Physlib.CondensedMatter.Crystal.Symmetry.labelPerm_apply, Physlib.CondensedMatter.Crystal.Symmetry.shift, Physlib.CondensedMatter.Crystal.Symmetry.apply_eq, Physlib.CondensedMatter.Crystal.Symmetry.ofParts, Physlib.CondensedMatter.Crystal.Symmetry.ofParts_apply, Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_ofParts
statement: formalized
proof: formalized
---

# Decomposition of crystal symmetries

The module `Physlib.CondensedMatter.Crystal.Symmetry.Decomposition`, [Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean): 15 declarations (1 instance with no name), 10 with a docstring.

> Every crystal symmetry is a lattice automorphism, a permutation of labels and a shift.

## i. Overview

> A symmetry sends all sites with the same label to sites with one common label, so it permutes
> the labels of the unit cell by a permutation `σ`. It maps the lattice vectors by an automorphism
> `A` and moves the sites with label `j` by a lattice vector `s j`. These three pieces describe its
> action on every site:
>
> `⟨n, i⟩ ↦ ⟨A n + s (σ i), σ i⟩`.
>
> Conversely every choice of `A`, `σ` and `s` defines a symmetry. In graphene, shifting only the
> carbon atoms of one sublattice by a lattice vector is a symmetry with `A = 1` and `σ = 1`. It is
> not a translation.
>
> Composing two symmetries composes their automorphisms and permutations. The shifts of the second
> symmetry are transformed by `A` and relabelled by `σ` before they are added. The symmetry group is
> therefore the semidirect product of the shifts by the lattice automorphisms and label
> permutations.

## ii. Key results

> - `Crystal.Symmetry.labelPerm` : the permutation `σ` of the labels of a symmetry.
> - `Crystal.Symmetry.shift` : the shifts `s` of a symmetry.
> - `Crystal.Symmetry.apply_eq` : a symmetry acts as `⟨n, i⟩ ↦ ⟨A n + s (σ i), σ i⟩`.
> - `Crystal.Symmetry.ofParts` : the symmetry built from `A`, `σ` and `s`.
> - `Crystal.Symmetry.semidirectEquiv` : the symmetry group is the semidirect product of the shifts
>   by the lattice automorphisms and label permutations.

## iv. References

> * None.

## A. The permutation of labels

**`Physlib.CondensedMatter.Crystal.Symmetry.label_apply`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L69).

> The label of an image site depends only on the label of the site.

```lean
lemma label_apply (φ : Symmetry C) (x : C.Site) :
    (φ x).label = (φ (Site.ref x.label)).label
```

**An instance with no name**, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L76).

> Symmetries permute the labels of the unit cell.

```lean
instance : MulAction (Symmetry C) C.UnitCell
```

**`Physlib.CondensedMatter.Crystal.Symmetry.labelPerm`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L82).

> The permutation of labels of a symmetry.

```lean
def labelPerm (φ : Symmetry C) : Equiv.Perm C.UnitCell
```

**`Physlib.CondensedMatter.Crystal.Symmetry.labelPerm_apply`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L84).

```lean
lemma labelPerm_apply (φ : Symmetry C) (i : C.UnitCell) : φ.labelPerm i = φ • i
```

## B. The shifts of a symmetry

**`Physlib.CondensedMatter.Crystal.Symmetry.shift`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L90).

> The shift of a symmetry at the label `j`: the cell of the image of the reference site that
> the symmetry sends to label `j`.

```lean
def shift (φ : Symmetry C) (j : C.UnitCell) : G
```

**`Physlib.CondensedMatter.Crystal.Symmetry.apply_eq`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L93).

> A symmetry acts as `⟨n, i⟩ ↦ ⟨A n + s (σ i), σ i⟩`.

```lean
lemma apply_eq (φ : Symmetry C) (x : C.Site) :
    φ x = ⟨φ.latticeAut x.cell + φ.shift (φ.labelPerm x.label), φ.labelPerm x.label⟩
```

## C. Symmetries from their parts

**`Physlib.CondensedMatter.Crystal.Symmetry.ofParts`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L103).

> The symmetry `⟨n, i⟩ ↦ ⟨A n + s (σ i), σ i⟩` with lattice automorphism `A`, label
> permutation `σ` and shifts `s`.

```lean
def ofParts (C : Crystal G) (A : G ≃+ G) (σ : Equiv.Perm C.UnitCell) (s : C.UnitCell → G) :
    Symmetry C
```

**`Physlib.CondensedMatter.Crystal.Symmetry.ofParts_apply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L114).

```lean
lemma ofParts_apply (x : C.Site) :
    ofParts C A σ s x = ⟨A x.cell + s (σ x.label), σ x.label⟩
```

**`Physlib.CondensedMatter.Crystal.Symmetry.latticeAut_ofParts`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L117).

```lean
lemma latticeAut_ofParts : (ofParts C A σ s).latticeAut = A
```

**`Physlib.CondensedMatter.Crystal.Symmetry.labelPerm_ofParts`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L119).

```lean
lemma labelPerm_ofParts : (ofParts C A σ s).labelPerm = σ
```

**`Physlib.CondensedMatter.Crystal.Symmetry.shift_ofParts`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L121).

```lean
lemma shift_ofParts : (ofParts C A σ s).shift = s
```

**`Physlib.CondensedMatter.Crystal.Symmetry.ofParts_eq`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L127).

> Every symmetry is built from its lattice automorphism, label permutation and shifts.

```lean
lemma ofParts_eq (φ : Symmetry C) :
    ofParts C φ.latticeAut φ.labelPerm φ.shift = φ
```

**`Physlib.CondensedMatter.Crystal.Symmetry.ofParts_mul`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L135).

> Composition composes the automorphisms and permutations. The shifts of the second symmetry
> are transformed by `A` and relabelled by `σ`.

```lean
lemma ofParts_mul :
    ofParts C A σ s * ofParts C B τ t = ofParts C (B.trans A) (σ * τ) (s + A ∘ t ∘ σ.symm)
```

## D. The semidirect product

**`Physlib.CondensedMatter.Crystal.Symmetry.shiftAction`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L144).

> Lattice automorphisms and label permutations act on shifts by `s ↦ A ∘ s ∘ σ⁻¹`.

```lean
def shiftAction (C : Crystal G) :
    Multiplicative (AddAut G) × Equiv.Perm C.UnitCell →*
      MulAut (Multiplicative (C.UnitCell → G))
```

**`Physlib.CondensedMatter.Crystal.Symmetry.semidirectEquiv`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean#L153).

> The symmetry group is the semidirect product of the shifts by the lattice automorphisms and
> label permutations.

```lean
def semidirectEquiv (C : Crystal G) :
    Multiplicative (C.UnitCell → G) ⋊[shiftAction C]
      (Multiplicative (AddAut G) × Equiv.Perm C.UnitCell) ≃* Symmetry C
```

## Depends on

- [Symmetries of a crystal](symmetry-basic.md)

## Sources

- [Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/CondensedMatter/Crystal/Symmetry/Decomposition.lean)
