---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.fineStructureConstant, PhyslibAlpha.Hydrogen.relativisticShift, PhyslibAlpha.Hydrogen.spinOrbitShift, PhyslibAlpha.Hydrogen.darwinShift, PhyslibAlpha.Hydrogen.fineStructureShift, PhyslibAlpha.Hydrogen.levelIndex_sub_one, PhyslibAlpha.Hydrogen.ls_upper, PhyslibAlpha.Hydrogen.ls_lower
statement: formalized
proof: formalized
---

# The fine structure of hydrogen

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.FineStructure`, [PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean): 11 declarations, 8 with a docstring.

> The first-order fine structure of hydrogen: relativistic kinetic, spin–orbit and Darwin
> corrections, evaluated with the radial expectation values of `RadialFunctions.lean` and the
> spin–orbit eigenvalues of `SpinOrbit.lean`, add up to a shift that depends on `j` only.

## i. Overview

> For the level `(ν, l, j)` with Bohr energy `E_ν = -Ry/ν²` and `α = k/(ℏc)` the three standard
> first-order corrections are
>
> - `E_rel = -⟨(E_ν - V)²⟩/(2mc²)` with `V = -k/r`,
> - `E_SO = k/(2m²c²) ⟨1/r³⟩ ⟨L · S⟩`,
> - `E_D = π k ℏ²/(2m²c²) |ψ(0)|²`, non-zero only for `l = 0`.
>
> Inserting the proved values of `⟨1/r⟩`, `⟨1/r²⟩`, `⟨1/r³⟩`, `|R(0)|²` and of `L · S` on the
> `j = l ± 1/2` states gives
>
> `E_rel + E_SO + E_D = E_ν α²/ν² (ν/(j + 1/2) - 3/4)`
>
> in both cases (`fineStructureShift_upper`, `fineStructureShift_lower`), so `2s_{1/2}` and
> `2p_{1/2}` stay degenerate (`fineStructureShift_upper_eq_lower`).
>
> What is taken as physical input: the three perturbation operators and the first-order formula
> `ΔE = ⟨H'⟩`, the identity `⟨p⁴⟩ = 4m²⟨(E - V)²⟩`, and `|ψ(0)|² = |R(0)|²/(4π)`. What is proved:
> the radial equation, the radial integrals, the `L · S` eigenvalues and the algebra that combines
> them.

## ii. Key results

> - `relativisticShift`, `spinOrbitShift`, `darwinShift`, `fineStructureShift`: the corrections.
> - `fineStructureShift_upper`: the formula for `j = l + 1/2`, including `l = 0`.
> - `fineStructureShift_lower`: the formula for `j = l - 1/2`, `l ≥ 1`.
> - `fineStructureShift_upper_eq_lower`: the shift depends on `j` only.

## iv. References

> - H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms*, Springer
>   (1957).
> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 5.3.

## A. The three first-order corrections

**`PhyslibAlpha.Hydrogen.fineStructureConstant`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L75).

> The fine-structure constant `α = k/(ℏ c)` of the atom.

```lean
def fineStructureConstant : ℝ
```

**`PhyslibAlpha.Hydrogen.relativisticShift`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L80).

> The relativistic kinetic correction `-⟨p⁴⟩/(8 m³ c²) = -⟨(E - V)²⟩/(2 m c²)` in the state
> `(ν, l)`, written with `p² = 2m(E - V)`, `V = -k/r` and the radial expectation values
> `⟨1/r⟩ = ⟨1/ρ⟩/a`, `⟨1/r²⟩ = ⟨1/ρ²⟩/a²`.

```lean
def relativisticShift (ν l : ℕ) : ℝ
```

**`PhyslibAlpha.Hydrogen.spinOrbitShift`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L86).

> The spin–orbit correction `k/(2 m² c²) ⟨1/r³⟩ ⟨L · S⟩`, where `⟨L · S⟩ = ℏ² ls`.

```lean
def spinOrbitShift (ν l : ℕ) (ls : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.darwinShift`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L91).

> The Darwin correction `π k ℏ²/(2 m² c²) |ψ(0)|²`, which is non-zero only for `s` states;
> there `|ψ(0)|² = |R(0)|²/(4π)` with `R` normalised in physical units.

```lean
def darwinShift (ν l : ℕ) : ℝ
```

**`PhyslibAlpha.Hydrogen.fineStructureShift`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L98).

> The total first-order fine-structure shift of the level `(ν, l)` with `⟨L · S⟩ = ℏ² ls`.

```lean
def fineStructureShift (ν l : ℕ) (ls : ℝ) : ℝ
```

## B. The fine-structure formula

**`PhyslibAlpha.Hydrogen.levelIndex_sub_one`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L109).

```lean
lemma levelIndex_sub_one (hν : 1 ≤ ν) : HydrogenAtom.levelIndex 3 (ν - 1) = ν
```

**`PhyslibAlpha.Hydrogen.ls_upper`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L114).

```lean
lemma ls_upper {ls : ℝ} (hls : (ls : ℂ) = Sl2.spinOrbitValue (2 * l) 1 0) : ls = l / 2
```

**`PhyslibAlpha.Hydrogen.ls_lower`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L121).

```lean
lemma ls_lower (hl1 : 1 ≤ l) {ls : ℝ} (hls : (ls : ℂ) = Sl2.spinOrbitValue (2 * l) 1 1) :
    ls = -((l : ℝ) + 1) / 2
```

**`PhyslibAlpha.Hydrogen.fineStructureShift_upper`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L134).

> **Fine structure, `j = l + 1/2`.** With `⟨L · S⟩/ℏ²` the eigenvalue of `L · S` on the
> `j = l + 1/2` string (`Sl2.dot_coupled_stringVec`), the three corrections add up to
> `E_ν α²/ν² (ν/(j + 1/2) - 3/4)`. For `l = 0` the spin–orbit term vanishes and the Darwin term
> takes its place.

```lean
lemma fineStructureShift_upper (hk : 0 < H.k) (hl : l < ν) {ls : ℝ}
    (hls : (ls : ℂ) = Sl2.spinOrbitValue (2 * l) 1 0) :
    fineStructureShift H c ν l ls = H.energyLevel (ν - 1) * fineStructureConstant H c ^ 2 /
      (ν : ℝ) ^ 2 * ((ν : ℝ) / ((l + 1 / 2 : ℝ) + 1 / 2) - 3 / 4)
```

**`PhyslibAlpha.Hydrogen.fineStructureShift_lower`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L162).

> **Fine structure, `j = l - 1/2`.** For `l ≥ 1` the three corrections add up to
> `E_ν α²/ν² (ν/(j + 1/2) - 3/4)` with `j = l - 1/2`.

```lean
lemma fineStructureShift_lower (hk : 0 < H.k) (hl : l < ν) (hl1 : 1 ≤ l)
    {ls : ℝ} (hls : (ls : ℂ) = Sl2.spinOrbitValue (2 * l) 1 1) :
    fineStructureShift H c ν l ls = H.energyLevel (ν - 1) * fineStructureConstant H c ^ 2 /
      (ν : ℝ) ^ 2 * ((ν : ℝ) / ((l - 1 / 2 : ℝ) + 1 / 2) - 3 / 4)
```

**`PhyslibAlpha.Hydrogen.fineStructureShift_upper_eq_lower`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean#L184).

> **The fine-structure shift depends on `j` only.** The levels `(ν, l, j = l + 1/2)` and
> `(ν, l + 1, j = l + 1/2)` are shifted by the same amount; for `ν = 2`, `l = 0` this is the
> degeneracy of `2s_{1/2}` and `2p_{1/2}` that the Lamb shift lifts.

```lean
lemma fineStructureShift_upper_eq_lower (hk : 0 < H.k) (hl : l + 1 < ν)
    {ls ls' : ℝ} (hls : (ls : ℂ) = Sl2.spinOrbitValue (2 * l) 1 0)
    (hls' : (ls' : ℂ) = Sl2.spinOrbitValue (2 * (l + 1)) 1 1) :
    fineStructureShift H c ν l ls = fineStructureShift H c ν (l + 1) ls'
```

## Depends on

- [Spin–orbit coupling](../angularmomentum/spinorbit.md)
- [The radial functions of the hydrogen atom](radialfunctions.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/FineStructure.lean)
