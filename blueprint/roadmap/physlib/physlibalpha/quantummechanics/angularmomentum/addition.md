---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.AngularMomentumRepresentation.tensor, PhyslibAlpha.Sl2.AngularMomentumRepresentation.tensor_Jp, PhyslibAlpha.Sl2.AngularMomentumRepresentation.tensor_Jm, PhyslibAlpha.Sl2.AngularMomentumRepresentation.ρE_mul_ρF, PhyslibAlpha.Sl2.AngularMomentumRepresentation.ρH_mul_ρE, PhyslibAlpha.Sl2.AngularMomentumRepresentation.ρH_mul_ρF, PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJx, PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJy
statement: formalized
proof: formalized
---

# Addition of angular momenta

The module `PhyslibAlpha.QuantumMechanics.AngularMomentum.Addition`, [PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean): 26 declarations, 14 with a docstring.

> Couples two angular momenta and identifies the total angular momentum on the
> Clebsch–Gordan decomposition.

## i. Overview

> Two angular momentum representations on `V` and `W` give one on `V ⊗ W`, with total angular
> momentum `J = J₁ ⊗ 1 + 1 ⊗ J₂`. The standard module `V(n)` carries the spin-`n/2`
> representation with `Jz = H/2`, `J+ = E` and `J- = F`. For spins `j₁ = m/2` and `j₂ = n/2` the
> total `J²` acts on the `k`-th lowering string of `V(m) ⊗ V(n)` by `J(J + 1)` with
> `J = j₁ + j₂ - k`, and `Jz` acts on its `l`-th vector by `J - l`. As `k` runs from `0` to
> `min m n`, `J` runs from `j₁ + j₂` down to `|j₁ - j₂|`. The Clebsch–Gordan equivalence
> `cgEquiv` intertwines `Jz`, `J+` and `J-` of the coupled system with those of the spin-`J`
> representations on the summands.

## ii. Key results

> - `AngularMomentumRepresentation.tensor` is the coupled representation on `V ⊗ W`.
> - `AngularMomentumRepresentation.standard` is the spin-`n/2` representation on `V(n)`.
> - `Jsq_coupled_stringVec` and `Jz_coupled_stringVec` give the total `J²` and `Jz` on the
>   lowering strings.
> - `cgEquiv_Jz_coupled`, `cgEquiv_Jp_coupled` and `cgEquiv_Jm_coupled` give the intertwining
>   with the summands.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Coupled angular momentum

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.tensor`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L69).

> The coupled angular momentum `J = J₁ ⊗ 1 + 1 ⊗ J₂` on `V ⊗ W`.

```lean
def tensor (ρ₁ : AngularMomentumRepresentation V) (ρ₂ : AngularMomentumRepresentation W) :
    AngularMomentumRepresentation (V ⊗[ℂ] W)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.tensor_Jp`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L78).

```lean
lemma tensor_Jp (ρ₁ : AngularMomentumRepresentation V) (ρ₂ : AngularMomentumRepresentation W) :
    (tensor ρ₁ ρ₂).Jp = diagEnd ρ₁.Jp ρ₂.Jp
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.tensor_Jm`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L82).

```lean
lemma tensor_Jm (ρ₁ : AngularMomentumRepresentation V) (ρ₂ : AngularMomentumRepresentation W) :
    (tensor ρ₁ ρ₂).Jm = diagEnd ρ₁.Jm ρ₂.Jm
```

## B. The spin-`n/2` representation on `V(n)`

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.ρE_mul_ρF`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L91).

> `EF = FE + H` on `V(n)`, the associative form of `⁅E, F⁆ = H`.

```lean
lemma ρE_mul_ρF :
    (ρE : Module.End ℂ (StandardSl2Module ℂ n)) * ρF = ρF * ρE + ρH
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.ρH_mul_ρE`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L99).

> `HE = EH + 2E` on `V(n)`, the associative form of `⁅H, E⁆ = 2E`.

```lean
lemma ρH_mul_ρE :
    (ρH : Module.End ℂ (StandardSl2Module ℂ n)) * ρE = ρE * ρH + (2 : ℂ) • ρE
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.ρH_mul_ρF`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L107).

> `HF = FH - 2F` on `V(n)`, the associative form of `⁅H, F⁆ = -2F`.

```lean
lemma ρH_mul_ρF :
    (ρH : Module.End ℂ (StandardSl2Module ℂ n)) * ρF = ρF * ρH + (-2 : ℂ) • ρF
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJx`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L115).

> `Jx = (E + F)/2` on `V(n)`.

```lean
def stdJx : Module.End ℂ (StandardSl2Module ℂ n)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJy`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L118).

> `Jy = -i(E - F)/2` on `V(n)`.

```lean
def stdJy : Module.End ℂ (StandardSl2Module ℂ n)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJz`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L121).

> `Jz = H/2` on `V(n)`.

```lean
def stdJz : Module.End ℂ (StandardSl2Module ℂ n)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJx_stdJy`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L123).

```lean
lemma stdJx_stdJy : ⁅stdJx n, stdJy n⁆ = Complex.I • stdJz n
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJy_stdJz`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L128).

```lean
lemma stdJy_stdJz : ⁅stdJy n, stdJz n⁆ = Complex.I • stdJx n
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.stdJz_stdJx`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L133).

```lean
lemma stdJz_stdJx : ⁅stdJz n, stdJx n⁆ = Complex.I • stdJy n
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.standard`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L140).

> The spin-`n/2` representation on `V(n)`: `Jz = H/2`, `Jx = (E + F)/2`,
> `Jy = -i(E - F)/2`, so that `J+ = E` and `J- = F`.

```lean
def standard : AngularMomentumRepresentation (StandardSl2Module ℂ n)
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.standard_Jp`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L148).

```lean
lemma standard_Jp : (standard n).Jp = ρE
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.standard_Jm`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L152).

```lean
lemma standard_Jm : (standard n).Jm = ρF
```

**`PhyslibAlpha.Sl2.AngularMomentumRepresentation.standard_Jz`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L156).

```lean
lemma standard_Jz : (standard n).Jz = (1 / 2 : ℂ) • ρH
```

## C. Total angular momentum on `V(m) ⊗ V(n)`

### C.1. Eigenvalues on the lowering strings

**`PhyslibAlpha.Sl2.coupled`**, an abbrev, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L169).

> The coupled representation of spins `m/2` and `n/2` on `V(m) ⊗ V(n)`.

```lean
abbrev coupled (m n : ℕ) :
    AngularMomentumRepresentation (StandardSl2Module ℂ m ⊗[ℂ] StandardSl2Module ℂ n)
```

**`PhyslibAlpha.Sl2.coupled_Jz`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L173).

```lean
lemma coupled_Jz : (coupled m n).Jz = (1 / 2 : ℂ) • tensorH m n
```

**`PhyslibAlpha.Sl2.coupled_Jp`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L176).

```lean
lemma coupled_Jp : (coupled m n).Jp = tensorE m n
```

**`PhyslibAlpha.Sl2.coupled_Jm`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L179).

```lean
lemma coupled_Jm : (coupled m n).Jm = tensorF m n
```

**`PhyslibAlpha.Sl2.Jz_coupled_stringVec`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L189).

> `Jz` acts on the `l`-th vector of the `k`-th string by `J - l`, `J = (m + n - 2k)/2`.

```lean
lemma Jz_coupled_stringVec (l : ℕ) :
    (coupled m n).Jz (stringVec m n k l) =
      (((m + n - 2 * k : ℕ) : ℂ) / 2 - l) • stringVec m n k l
```

**`PhyslibAlpha.Sl2.Jsq_coupled_stringVec`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L197).

> The total `J²` acts on the `k`-th string by `J(J + 1)`, `J = (m + n - 2k)/2`.

```lean
lemma Jsq_coupled_stringVec (l : ℕ) :
    (coupled m n).Jsq (stringVec m n k l) =
      (((m + n - 2 * k : ℕ) : ℂ) / 2 * (((m + n - 2 * k : ℕ) : ℂ) / 2 + 1)) •
        stringVec m n k l
```

### C.2. Intertwining with the summands

**`PhyslibAlpha.Sl2.sumEnd_smul`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L211).

```lean
lemma sumEnd_smul (c : ℂ) (A : ∀ k, Module.End ℂ (CGSummand ℂ m n k)) (y : CGSum ℂ m n) :
    sumEnd (fun k => c • A k) y = c • sumEnd A y
```

**`PhyslibAlpha.Sl2.cgEquiv_Jz_coupled`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L219).

> `cgEquiv` intertwines the total `Jz` with `Jz` of the spin-`J` summands.

```lean
lemma cgEquiv_Jz_coupled (hmn : 0 < m + n)
    (x : StandardSl2Module ℂ m ⊗[ℂ] StandardSl2Module ℂ n) :
    cgEquiv hmn ((coupled m n).Jz x) = sumEnd (fun _ => (standard _).Jz) (cgEquiv hmn x)
```

**`PhyslibAlpha.Sl2.cgEquiv_Jp_coupled`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L226).

> `cgEquiv` intertwines the total `J+` with `J+` of the spin-`J` summands.

```lean
lemma cgEquiv_Jp_coupled (hmn : 0 < m + n)
    (x : StandardSl2Module ℂ m ⊗[ℂ] StandardSl2Module ℂ n) :
    cgEquiv hmn ((coupled m n).Jp x) = sumEnd (fun _ => (standard _).Jp) (cgEquiv hmn x)
```

**`PhyslibAlpha.Sl2.cgEquiv_Jm_coupled`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean#L232).

> `cgEquiv` intertwines the total `J-` with `J-` of the spin-`J` summands.

```lean
lemma cgEquiv_Jm_coupled (hmn : 0 < m + n)
    (x : StandardSl2Module ℂ m ⊗[ℂ] StandardSl2Module ℂ n) :
    cgEquiv hmn ((coupled m n).Jm x) = sumEnd (fun _ => (standard _).Jm) (cgEquiv hmn x)
```

## Depends on

- [The equivariant Clebsch–Gordan decomposition](../../mathematics/part-02/representationtheory/sl2-tensordecomposition.md)
- [Abstract angular momentum representations](basic.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/AngularMomentum/Addition.lean)
