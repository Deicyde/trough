---
declaration: module
origin: cited
lean: LorentzGroup.det_eq_one_or_neg_one, LorentzGroup.coeForℤ₂, LorentzGroup.detContinuous, LorentzGroup.detContinuous_eq_one, LorentzGroup.detContinuous_eq_zero, LorentzGroup.detContinuous_eq_iff_det_eq, LorentzGroup.detRep, LorentzGroup.detRep_continuous
statement: formalized
proof: formalized
---

# The Proper Lorentz Group

The module `Physlib.Relativity.LorentzGroup.Proper`, [Physlib/Relativity/LorentzGroup/Proper.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean): 20 declarations (4 instances with no name), 17 with a docstring.

> The proper Lorentz group is the subgroup of the Lorentz group with determinant `1`.
>
> We define the give a series of lemmas related to the determinant of the Lorentz group.

**`LorentzGroup.det_eq_one_or_neg_one`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L35).

> The determinant of a member of the Lorentz group is `1` or `-1`.

```lean
lemma det_eq_one_or_neg_one (Λ : 𝓛 d) : Λ.1.det = 1 ∨ Λ.1.det = -1
```

**An instance with no name**, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L43).

> The instance of a topological space on `ℤ₂` corresponding to the discrete topology.

```lean
instance : TopologicalSpace ℤ₂
```

**An instance with no name**, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L46).

> The topological space defined by `ℤ₂` is discrete.

```lean
instance : DiscreteTopology ℤ₂
```

**An instance with no name**, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L50).

> The instance of a topological group on `ℤ₂` defined via the discrete topology.

```lean
instance : IsTopologicalGroup ℤ₂
```

**`LorentzGroup.coeForℤ₂`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L54).

> A continuous function from `({-1, 1} : Set ℝ)` to `ℤ₂`.

```lean
def coeForℤ₂ : C(({-1, 1} : Set ℝ), ℤ₂)
```

**`LorentzGroup.detContinuous`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L60).

> The continuous map taking a Lorentz matrix to its determinant.

```lean
def detContinuous : C(𝓛 d, ℤ₂)
```

**`LorentzGroup.detContinuous_eq_one`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L70).

```lean
lemma detContinuous_eq_one (Λ : LorentzGroup d) :
    detContinuous Λ = Additive.toMul 0 ↔ Λ.1.det = 1
```

**`LorentzGroup.detContinuous_eq_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L84).

```lean
lemma detContinuous_eq_zero (Λ : LorentzGroup d) :
    detContinuous Λ = Additive.toMul (1 : ZMod 2) ↔ Λ.1.det = - 1
```

**`LorentzGroup.detContinuous_eq_iff_det_eq`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L104).

```lean
lemma detContinuous_eq_iff_det_eq (Λ Λ' : LorentzGroup d) :
    detContinuous Λ = detContinuous Λ' ↔ Λ.1.det = Λ'.1.det
```

**`LorentzGroup.detRep`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L126).

> The representation taking a Lorentz matrix to its determinant.

```lean
def detRep : 𝓛 d →* ℤ₂
```

**`LorentzGroup.detRep_continuous`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L152).

> The representation of the Lorentz group defined by taking the determinant `detRep` is
> continuous.

```lean
lemma detRep_continuous : Continuous (@detRep d)
```

**`LorentzGroup.det_on_connected_component`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L156).

> Two Lorentz transformations which are in the same connected component have the same
> determinant.

```lean
lemma det_on_connected_component {Λ Λ' : LorentzGroup d} (h : Λ' ∈ connectedComponent Λ) :
    Λ.1.det = Λ'.1.det
```

**`LorentzGroup.detRep_on_connected_component`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L168).

> Two Lorentz transformations which are in the same connected component have the same
> image under `detRep`, the determinant representation.

```lean
lemma detRep_on_connected_component {Λ Λ' : LorentzGroup d} (h : Λ' ∈ connectedComponent Λ) :
    detRep Λ = detRep Λ'
```

**`LorentzGroup.det_of_joined`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L175).

> Two Lorentz transformations which are joined by a path have the same determinant.

```lean
lemma det_of_joined {Λ Λ' : LorentzGroup d} (h : Joined Λ Λ') : Λ.1.det = Λ'.1.det
```

**`LorentzGroup.IsProper`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L180).

> A Lorentz Matrix is proper if its determinant is 1.

```lean
def IsProper (Λ : LorentzGroup d) : Prop
```

**An instance with no name**, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L183).

> The predicate `IsProper` is decidable.

```lean
instance : DecidablePred (@IsProper d)
```

**`LorentzGroup.isProper_mul`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L188).

> The product of two proper Lorentz transformations is proper.

```lean
lemma isProper_mul {Λ Λ' : LorentzGroup d}
    (h : IsProper Λ) (h' : IsProper Λ') : IsProper (Λ * Λ')
```

**`LorentzGroup.isProper_iff`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L194).

> A Lorentz transformation is proper if its image under the det-representation
> `detRep` is `1`.

```lean
lemma isProper_iff (Λ : LorentzGroup d) : IsProper Λ ↔ detRep Λ = 1
```

**`LorentzGroup.isProper_id`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L200).

> The identity Lorentz transformation is proper.

```lean
lemma isProper_id : @IsProper d 1
```

**`LorentzGroup.isProper_on_connected_component`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean#L205).

> If two Lorentz transformations are in the same connected component, and one is proper then
> the other is also proper.

```lean
lemma isProper_on_connected_component {Λ Λ' : LorentzGroup d} (h : Λ' ∈ connectedComponent Λ) :
    IsProper Λ ↔ IsProper Λ'
```

## Depends on

- [The Lorentz Group](basic.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Proper.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Proper.lean)
