---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.cfgEquiv, CondensedMatter.QuasiLocal.quantumIso, CondensedMatter.QuasiLocal.smul_mono, CondensedMatter.QuasiLocal.restr_cfgEquiv, CondensedMatter.QuasiLocal.agree_cfgEquiv, CondensedMatter.QuasiLocal.quantumIso_incl, CondensedMatter.QuasiLocal.cfgCast, CondensedMatter.QuasiLocal.regionIso
statement: formalized
proof: formalized
---

# Symmetries of the quantum net

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.Symmetry`, [PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean): 19 declarations, 10 with a docstring.

> A group acting on the sites acts on the operators of regions by `*`-isomorphisms, compatibly with
> the inclusions.

## i. Overview

> Let a group `Γ` act on the sites, all of which carry the same finite configuration space `Ω₀`. The
> group moves a region `X` to `γ • X`, and a configuration of `γ • X` to one of `X` by reading the
> value at `γ • x` for `x ∈ X`. This moves an operator of `X` to an operator of `γ • X`: it is a
> `*`-isomorphism `A X → A (γ • X)`. It is compatible with the inclusion of regions, because it moves
> the sites outside `X` to the sites outside `γ • X`.

## ii. Key results

> - `cfgEquiv` : a configuration of `γ • X` is a configuration of `X`.
> - `quantumIso` : the `*`-homomorphism of operators carried by `γ`.
> - `quantumIso_incl` : naturality with respect to the inclusions of regions.
> - `symAction` : the group acts on the quasi-local algebra by `*`-automorphisms.

## iv. References

> * None.

## A. Configurations of a moved region

**`CondensedMatter.QuasiLocal.cfgEquiv`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L63).

> A configuration of the region `γ • X` is a configuration of `X`: read it at `γ • x`.

```lean
def cfgEquiv (γ : Γ) (X : Finset S) : Cfg (fun _ : S => Ω₀) (γ • X) ≃ Cfg (fun _ : S => Ω₀) X
```

## B. The moved operators

**`CondensedMatter.QuasiLocal.quantumIso`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L78).

> The operator of `γ • X` that acts as `M` after moving the configurations back to `X`.

```lean
def quantumIso (γ : Γ) (X : Finset S) :
    Alg (fun _ : S => Ω₀) X →⋆ₐ[ℂ] Alg (fun _ : S => Ω₀) (γ • X)
```

**`CondensedMatter.QuasiLocal.smul_mono`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L101).

```lean
lemma smul_mono (γ : Γ) {X Y : Finset S} (h : X ≤ Y) : γ • X ≤ γ • Y
```

**`CondensedMatter.QuasiLocal.restr_cfgEquiv`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L106).

```lean
lemma restr_cfgEquiv (γ : Γ) {X Y : Finset S} (h : X ≤ Y)
    (c : Cfg (fun _ : S => Ω₀) (γ • Y)) :
    restr h (cfgEquiv Γ Ω₀ γ Y c) = cfgEquiv Γ Ω₀ γ X (restr (smul_mono γ h) c)
```

**`CondensedMatter.QuasiLocal.agree_cfgEquiv`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L112).

```lean
lemma agree_cfgEquiv (γ : Γ) {X Y : Finset S} (h : X ≤ Y)
    (c c' : Cfg (fun _ : S => Ω₀) (γ • Y)) :
    Agree h (cfgEquiv Γ Ω₀ γ Y c) (cfgEquiv Γ Ω₀ γ Y c') ↔ Agree (smul_mono γ h) c c'
```

**`CondensedMatter.QuasiLocal.quantumIso_incl`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L127).

> **Naturality**: moving operators commutes with extending them by the identity.

```lean
lemma quantumIso_incl (γ : Γ) {X Y : Finset S} (h : X ≤ Y) (M : Alg (fun _ : S => Ω₀) X) :
    quantumIso γ Y (inclMat h M) = inclMat (smul_mono γ h) (quantumIso γ X M)
```

## C. The action on the quasi-local algebra

**`CondensedMatter.QuasiLocal.cfgCast`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L140).

> Transport of configurations along an equality of regions.

```lean
def cfgCast {X Y : Finset S} (e : X = Y) (c : Cfg (fun _ : S => Ω₀) Y) :
    Cfg (fun _ : S => Ω₀) X
```

**`CondensedMatter.QuasiLocal.regionIso`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L145).

> Transport of operators along an equality of regions.

```lean
def regionIso {X Y : Finset S} (e : X = Y) :
    Alg (fun _ : S => Ω₀) X →⋆ₐ[ℂ] Alg (fun _ : S => Ω₀) Y
```

**`CondensedMatter.QuasiLocal.regionIso_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L150).

```lean
lemma regionIso_apply {X Y : Finset S} (e : X = Y) (M : Alg (fun _ : S => Ω₀) X)
    (c c' : Cfg (fun _ : S => Ω₀) Y) :
    regionIso e M c c' = M (cfgCast e c) (cfgCast e c')
```

**`CondensedMatter.QuasiLocal.uniformNet`**, an abbrev, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L156).

> The quantum net of a system whose sites all carry the same finite configuration space.

```lean
abbrev uniformNet (Ω₀ : Type*) [Fintype Ω₀] [DecidableEq Ω₀] : AlgebraNet S
```

**`CondensedMatter.QuasiLocal.of_regionIso`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L159).

```lean
lemma of_regionIso {X Y : Finset S} (e : X = Y) (M : Alg (fun _ : S => Ω₀) X) :
    (uniformNet Ω₀).of Y (regionIso e M) = (uniformNet Ω₀).of X M
```

**`CondensedMatter.QuasiLocal.symAct`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L165).

> **The action of a site symmetry on the quasi-local algebra**: an endomorphism that moves the
> observables of a region `X` to those of `γ • X`.

```lean
def symAct (γ : Γ) :
    (uniformNet (S := S) Ω₀).Quasilocal →⋆ₐ[ℂ] (uniformNet (S := S) Ω₀).Quasilocal
```

**`CondensedMatter.QuasiLocal.symAct_of`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L170).

```lean
lemma symAct_of (γ : Γ) (X : Finset S) (M : Alg (fun _ : S => Ω₀) X) :
    symAct (Ω₀ := Ω₀) γ ((uniformNet Ω₀).of X M) = (uniformNet Ω₀).of (γ • X) (quantumIso γ X M)
```

**`CondensedMatter.QuasiLocal.quantumIso_mul`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L174).

```lean
lemma quantumIso_mul (γ₁ γ₂ : Γ) (X : Finset S) (M : Alg (fun _ : S => Ω₀) X) :
    regionIso (mul_smul γ₁ γ₂ X) (quantumIso (γ₁ * γ₂) X M) =
      quantumIso γ₁ (γ₂ • X) (quantumIso γ₂ X M)
```

**`CondensedMatter.QuasiLocal.quantumIso_one`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L187).

```lean
lemma quantumIso_one (X : Finset S) (M : Alg (fun _ : S => Ω₀) X) :
    regionIso (one_smul Γ X) (quantumIso (1 : Γ) X M) = M
```

**`CondensedMatter.QuasiLocal.symAct_mul`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L199).

> The action of site symmetries is multiplicative.

```lean
lemma symAct_mul (γ₁ γ₂ : Γ) :
    symAct (Ω₀ := Ω₀) (S := S) (γ₁ * γ₂) = (symAct γ₁).comp (symAct γ₂)
```

**`CondensedMatter.QuasiLocal.symAct_one`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L215).

```lean
lemma symAct_one : symAct (Ω₀ := Ω₀) (S := S) (1 : Γ) = StarAlgHom.id ℂ _
```

**`CondensedMatter.QuasiLocal.symEquiv`**, a def, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L225).

> **A group acting on the sites acts on the quasi-local algebra by automorphisms.**

```lean
def symEquiv (γ : Γ) : (uniformNet (S := S) Ω₀).Quasilocal ≃⋆ₐ[ℂ]
    (uniformNet (S := S) Ω₀).Quasilocal
```

**`CondensedMatter.QuasiLocal.symAction`**, a def, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean#L233).

> **The symmetry action** of a group on the sites, as a homomorphism to the automorphisms of the
> quasi-local algebra.

```lean
def symAction : Γ →* ((uniformNet (S := S) Ω₀).Quasilocal ≃⋆ₐ[ℂ]
    (uniformNet (S := S) Ω₀).Quasilocal)
```

## Depends on

- [The quantum and classical nets of a system with finite site spaces](instances.md)

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Symmetry.lean)
