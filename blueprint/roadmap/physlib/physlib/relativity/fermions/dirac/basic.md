---
declaration: module
origin: cited
lean: Fermion.Dirac, Fermion.Dirac.decomposeEquiv, Fermion.Dirac.left_add, Fermion.Dirac.dualRight_add, Fermion.Dirac.left_smul, Fermion.Dirac.dualRight_smul, Fermion.Dirac.decomposeLinEquiv, Fermion.Dirac.chiralBasis
statement: formalized
proof: formalized
---

# Dirac fermions

The module `Physlib.Relativity.Fermions.Dirac.Basic`, [Physlib/Relativity/Fermions/Dirac/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean): 17 declarations (2 instances with no name), 8 with a docstring.

> In this file we define Dirac fermions.
> This corresponds to a combination of two Weyl fermions (ψ^α, χ\_\{dot α})
> That is a LeftHandedWeyl and a DualRightHandedWeyl.
> The algebra equivalence `Dirac.endEquivMatrix` expresses their endomorphisms
> as matrices in the Dirac representation, using an explicit change from the chiral basis.

## References

> * arXiv:0812.1594 page 197. [ref: Dreiner:2008tw]

**`Fermion.Dirac`**, a structure, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L37).

> A Dirac fermion, consisting of a left handed Weyl fermion and a dual
> right handed Weyl fermion.

```lean
structure Dirac where
  /-- The left handed component of the Dirac fermion. -/
  left : LeftHandedWeyl
  /-- The right handed component of the Dirac fermion. -/
  dualRight : DualRightHandedWeyl
```

## The underlying module structure

> We inherit the module structure on dirac fermions
> from the module structure on left handed and dual right handed Weyl fermions.

**`Fermion.Dirac.decomposeEquiv`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L56).

> The decomposition of a Dirac fermion into its left handed and
> dual right handed components.

```lean
def decomposeEquiv : Dirac ≃ LeftHandedWeyl × DualRightHandedWeyl
```

**An instance with no name**, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L62).

```lean
instance : AddCommGroup Dirac
```

**An instance with no name**, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L64).

```lean
instance : Module ℂ Dirac
```

**`Fermion.Dirac.left_add`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L67).

```lean
lemma left_add (d₁ d₂ : Dirac) : (d₁ + d₂).left = d₁.left + d₂.left
```

**`Fermion.Dirac.dualRight_add`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L70).

```lean
lemma dualRight_add (d₁ d₂ : Dirac) : (d₁ + d₂).dualRight = d₁.dualRight + d₂.dualRight
```

**`Fermion.Dirac.left_smul`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L73).

```lean
lemma left_smul (c : ℂ) (d : Dirac) : (c • d).left = c • d.left
```

**`Fermion.Dirac.dualRight_smul`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L76).

```lean
lemma dualRight_smul (c : ℂ) (d : Dirac) : (c • d).dualRight = c • d.dualRight
```

**`Fermion.Dirac.decomposeLinEquiv`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L79).

> The linear equivalence between `Dirac` and `LeftHandedWeyl × DualRightHandedWeyl`.

```lean
def decomposeLinEquiv : Dirac ≃ₗ[ℂ] LeftHandedWeyl × DualRightHandedWeyl
```

## The chiral basis

**`Fermion.Dirac.chiralBasis`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L93).

> The chiral basis of the Dirac fermions.

```lean
def chiralBasis : Basis (Fin 4) ℂ Dirac
```

**`Fermion.Dirac.chiralBasis_cast_add`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L97).

```lean
lemma chiralBasis_cast_add (i : Fin 2) : chiralBasis (Fin.castAdd 2 i) =
    ⟨LeftHandedWeyl.basis i, 0⟩
```

**`Fermion.Dirac.chiralBasis_nat_add`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L105).

```lean
lemma chiralBasis_nat_add (i : Fin 2) : chiralBasis (Fin.natAdd 2 i) =
    ⟨0, DualRightHandedWeyl.basis i⟩
```

**`Fermion.Dirac.endEquivMatrix`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L116).

> Dirac endomorphisms as matrices in the Dirac representation. The change of coordinates
> from the chiral representation is `S = [1, 1; -1, 1]`, with `2 × 2` blocks, so this map sends
> `f` to `S [f] S⁻¹`. The common normalization factor `1 / √2` cancels in conjugation.

```lean
def endEquivMatrix : Module.End ℂ Dirac ≃ₐ[ℂ] Matrix (Fin 4) (Fin 4) ℂ
```

**`Fermion.Dirac.endEquivMatrix_apply`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L128).

> The change of coordinates from the chiral representation to the Dirac representation.

```lean
lemma endEquivMatrix_apply (f : Module.End ℂ Dirac) :
    endEquivMatrix f =
      !![1, 0, 1, 0; 0, 1, 0, 1; -1, 0, 1, 0; 0, -1, 0, 1] *
        LinearMap.toMatrix chiralBasis chiralBasis f *
        ((2 : ℂ)⁻¹ • !![1, 0, -1, 0; 0, 1, 0, -1; 1, 0, 1, 0; 0, 1, 0, 1])
```

## The representation of the Lorentz group

**`Fermion.Dirac.rep`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L150).

> The representation of `SL(2, ℂ)` on Dirac fermions.

```lean
def rep : Representation ℂ SL(2,ℂ) Dirac
```

**`Fermion.Dirac.rep_apply_mk`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L161).

```lean
lemma rep_apply_mk (g : SL(2,ℂ)) (ψ : LeftHandedWeyl) (χ : DualRightHandedWeyl) :
    rep g ⟨ψ, χ⟩ = ⟨LeftHandedWeyl.rep g ψ, DualRightHandedWeyl.rep g χ⟩
```

**`Fermion.Dirac.decomposeRepEquiv`**, a def, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean#L166).

> The equivalence between the representation on `Dirac` and the representation
> on `LeftHandedWeyl × DualRightHandedWeyl`.

```lean
def decomposeRepEquiv : rep.Equiv ((LeftHandedWeyl.rep).prod (DualRightHandedWeyl.rep))
```

## Depends on

- [Dual right handed Weyl fermions](../weyl/dualrighthanded.md)
- [Left handed Weyl fermions](../weyl/lefthanded.md)

## Sources

- [Physlib/Relativity/Fermions/Dirac/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Dirac/Basic.lean)
